"""Actual offline CLI handoffs and Suite contracts; supplied illustrative data only."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.suite/tools'))
from validate_records import check

MODULE = ROOT / 'business-dna/.business-dna'
EXAMPLES = MODULE / 'beispiele/topaca'
REQUEST = json.loads((MODULE / 'beispiele/request-branding.json').read_text())


class BusinessDNAIntegrationTests(unittest.TestCase):
    def run_request(self, request, extra=(), claims=None, sources=None):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'request.json'
            path.write_text(json.dumps(request))
            claim_path = EXAMPLES / 'claims.jsonl'
            source_path = EXAMPLES / 'sources.jsonl'
            if claims is not None:
                claim_path = Path(temp) / 'claims.jsonl'
                claim_path.write_text('\n'.join(map(json.dumps, claims))+'\n')
            if sources is not None:
                source_path = Path(temp) / 'sources.jsonl'
                source_path.write_text('\n'.join(map(json.dumps, sources))+'\n')
            return subprocess.run(
                [sys.executable, str(MODULE / 'tools/build_context.py'),
                 str(claim_path), '--sources', str(source_path),
                 '--request', str(path), *extra], capture_output=True, text=True)

    def test_business_dna_can_lead_support_and_own_without_status_promotion(self):
        order = dict(id='dna-job', objective='Check relevant organization facts',
                     lead_module='business-dna', supporting_modules=['branding', 'marketing'],
                     status='proposed', created_at='2026-10-27T12:00:00+01:00', input_refs=[])
        check('work-order', order)
        check('work-order', dict(order, lead_module='branding', supporting_modules=['business-dna']))
        artifact = dict(id='dna-context', owner_module='business-dna',
                        path='business-dna/kontext/context.json', version=1, status='draft',
                        contains_personal_data=False, rights_status='pending')
        check('artifact', artifact)

    def test_real_requests_for_all_ten_consumers_preserve_plan_and_provenance(self):
        originals = {c['claim_id']: c for c in
                     map(json.loads, (EXAMPLES / 'claims.jsonl').read_text().splitlines()) if c}
        for requester in ('marketing', 'branding', 'creative', 'pr', 'social-media',
                          'website', 'advertising', 'noCRM', 'analytics', 'e-commerce'):
            with self.subTest(requester=requester):
                request = dict(REQUEST, requester=requester)
                result = self.run_request(request)
                self.assertEqual(result.returncode, 0, result.stderr)
                pack = json.loads(result.stdout)
                self.assertEqual(pack['request_id'], request['request_id'])
                self.assertEqual(pack['requester'], requester)
                self.assertTrue(pack['claims'])
                self.assertTrue(any(c['status'] == 'planned' for c in pack['claims']))
                for claim in pack['claims']:
                    self.assertEqual(claim, originals[claim['claim_id']])
                    self.assertNotEqual(claim['visibility'], 'restricted')
                    self.assertTrue(set(claim['source_refs']) <= {s['source_id'] for s in pack['sources']})
                self.assertTrue(all(s['visibility'] != 'restricted' for s in pack['sources']))

    def test_request_validates_scope_and_never_emits_a_partial_pack_on_failure(self):
        bad = [dict(REQUEST, visibility_max='world'), dict(REQUEST, max_characters=True),
               dict(REQUEST, max_characters=499), dict(REQUEST, as_of='2026-02-30'),
               dict(REQUEST, purpose=' '), dict(REQUEST, topics='product'),
               dict(REQUEST, topics=[3]), dict(REQUEST, unknown='field')]
        missing = copy.deepcopy(REQUEST)
        del missing['request_id']
        for request in bad + [missing]:
            with self.subTest(request=request):
                result = self.run_request(request)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, '')
        self.assertNotEqual(self.run_request(REQUEST, ('--visibility', 'public')).returncode, 0)

    def test_public_export_also_filters_nonpublic_sources(self):
        result = self.run_request(dict(REQUEST, visibility_max='public', topics=[]))
        self.assertEqual(result.returncode, 0, result.stderr)
        pack = json.loads(result.stdout)
        self.assertEqual(pack['claims'], [])
        self.assertEqual(pack['sources'], [])

    def test_public_claim_requires_public_source_and_current_validity(self):
        claim = json.loads((EXAMPLES / 'claims.jsonl').read_text().splitlines()[0])
        source = json.loads((EXAMPLES / 'sources.jsonl').read_text().splitlines()[0])
        claim['visibility'] = 'public'
        source['visibility'] = 'public'
        request = dict(REQUEST, visibility_max='public', topics=[])
        visible = self.run_request(request, claims=[claim], sources=[source])
        self.assertEqual(visible.returncode, 0, visible.stderr)
        self.assertEqual(json.loads(visible.stdout)['claims'], [claim])
        for edits in ({'valid_until': '2026-10-26'}, {'valid_from': '2026-10-28'},
                      {'status': 'disputed'}, {'status': 'superseded'}, {'status': 'hypothesis'}):
            with self.subTest(edits=edits):
                result = self.run_request(request, claims=[dict(claim, **edits)], sources=[source])
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)['claims'], [])
        for visibility in ('shared', 'restricted'):
            result = self.run_request(request, claims=[claim], sources=[dict(source, visibility=visibility)])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['claims'], [])
            self.assertEqual(json.loads(result.stdout)['sources'], [])

    def test_snapshot_date_and_budget_are_respected(self):
        old = self.run_request(dict(REQUEST, as_of='2026-10-26'))
        self.assertEqual(old.returncode, 0, old.stderr)
        self.assertEqual(json.loads(old.stdout)['claims'], [])
        small = self.run_request(dict(REQUEST, topics=['product'], max_characters=950))
        self.assertEqual(small.returncode, 0, small.stderr)
        pack = json.loads(small.stdout)
        self.assertLessEqual(len(json.dumps(pack, ensure_ascii=False)), 950)
        self.assertGreater(pack['excluded_count'], 0)

    def test_private_working_sets_are_ignored_but_tools_examples_are_not(self):
        private = ['business-dna/%s/private.json' % name for name in
                   ('wissen', 'unternehmen', 'angebote', 'kontext', 'input', 'archiv')]
        public = ['business-dna/.business-dna/beispiele/request-branding.json',
                  'business-dna/.business-dna/tools/build_context.py', 'business-dna/AGENT.md']
        result = subprocess.run(['git', 'check-ignore', '--no-index', '--stdin'], cwd=ROOT,
                                input='\n'.join(private + public) + '\n', text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(result.stdout.splitlines()), set(private))


if __name__ == '__main__':
    unittest.main()
