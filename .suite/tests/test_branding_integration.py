"""Cross-module contracts and actual selective offline export; fictional data only."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.suite/tools'))
from validate_records import check, CheckError

EXAMPLES = ROOT / 'branding/.branding/beispiele'
T = '2026-10-27T11:30:00+01:00'


class BrandingIntegrationTests(unittest.TestCase):
    def test_branding_can_lead_support_and_own_artifacts(self):
        order = dict(id='brand-job', objective='Prepare brand guidelines',
                     lead_module='branding', supporting_modules=['creative', 'analytics'],
                     status='proposed', created_at=T, input_refs=[])
        check('work-order', order)
        check('work-order', dict(order, lead_module='website', supporting_modules=['branding']))
        check('artifact', dict(id='brand-profile', owner_module='branding',
                              path='branding/strategie/profile.json', version=1, status='draft',
                              contains_personal_data=False, rights_status='pending'))

    def test_real_cli_export_keeps_only_authorized_current_topics(self):
        request = json.loads((EXAMPLES / 'demo-request-public.json').read_text())
        approved = json.loads((EXAMPLES / 'demo-brand-approved.json').read_text())
        for requester in ('marketing', 'creative', 'pr', 'social-media', 'website',
                          'advertising', 'noCRM', 'analytics', 'e-commerce'):
            with self.subTest(requester=requester), tempfile.TemporaryDirectory() as temp:
                folder = Path(temp)
                request['requester'] = requester
                (folder / 'request.json').write_text(json.dumps(request))
                profiles = [approved]
                for updates in ({'status': 'draft'}, {'status': 'superseded'},
                                {'visibility': 'shared'}, {'visibility': 'restricted'}):
                    profile = copy.deepcopy(approved)
                    profile.update(updates)
                    profiles.append(profile)
                paths = []
                for index, profile in enumerate(profiles):
                    path = folder / ('profile-%d.json' % index)
                    path.write_text(json.dumps(profile))
                    paths.append(str(path))
                output = folder / 'context.json'
                result = subprocess.run(
                    [sys.executable, str(ROOT / 'branding/.branding/tools/build_brand_context.py'),
                     '--request', str(folder / 'request.json'), '--profiles', *paths,
                     '--out', str(output)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                pack = json.loads(output.read_text())
                self.assertEqual(pack['requester'], requester)
                self.assertEqual(pack['excluded_count'], 4)
                self.assertEqual(len(pack['profiles']), 1)
                profile = pack['profiles'][0]
                self.assertEqual(profile['version'], approved['version'])
                self.assertEqual(profile['decision_ref'], approved['decision_ref'])
                self.assertEqual(set(profile['brand_platform']), set(request['topics']))

    def test_brand_warning_needs_explicit_suite_review(self):
        brand = json.loads((EXAMPLES / 'demo-review.json').read_text())
        review = dict(id=brand['review_id'], artifact_id=brand['artifact_id'],
                      artifact_version=brand['artifact_version'], dimension='consistency',
                      reviewed_at=brand['reviewed_at'], status='warning',
                      evidence_refs=['branding/.branding/beispiele/demo-review.json'],
                      findings=[dict(severity=f['severity'], message=f['issue'])
                                for f in brand['findings']])
        with self.assertRaises(CheckError):
            check('review', review)
        review['status'] = 'blocked'
        check('review', review)


if __name__ == '__main__':
    unittest.main()
