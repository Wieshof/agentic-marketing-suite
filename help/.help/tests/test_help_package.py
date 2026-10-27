import json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'help'/'.help'
sys.path.insert(0,str(BASE/'tools'))
from scan_workspace import scan
from validate_help import validate

class HelpTests(unittest.TestCase):
    def test_complete(self):
        self.assertTrue(validate(ROOT)['ok'])
    def test_methods(self):
        self.assertGreaterEqual(validate(ROOT)['method_files'],30)
    def test_guides(self):
        self.assertGreaterEqual(validate(ROOT)['guide_files'],10)
    def test_entry(self):
        s=(ROOT/'help'/'AGENT.md').read_text(encoding='utf-8')
        self.assertIn('Wobei kann ich Ihnen mit der Agentic Marketing Suite helfen?',s)
    def test_no_harness(self):
        self.assertIn('keinen** eigenen Harness', (ROOT/'help'/'AGENT.md').read_text(encoding='utf-8'))
    def test_status_vocab(self):
        s=(BASE/'WISSENSQUELLEN.md').read_text(encoding='utf-8')
        for w in ['documented','implemented','configured','tested','unknown','unavailable']:self.assertIn(w,s)
    def test_schemas(self):
        for p in (BASE/'schemas').glob('*.json'):
            j=json.loads(p.read_text(encoding='utf-8'))
            self.assertIn('required',j)
    def test_inventory_empty(self):
        with tempfile.TemporaryDirectory() as p:
            d=scan(p)
            self.assertEqual(d['module_count_observed'],0)
            self.assertEqual(d['scope'],'file_inventory_only')
    def test_inventory_module(self):
        with tempfile.TemporaryDirectory() as p:
            q=Path(p)/'marketing';q.mkdir();(q/'AGENT.md').write_text('# agent')
            d=scan(p)
            self.assertEqual(d['module_count_observed'],1)
            self.assertEqual(d['modules'][0]['runtime_status'],'unknown')
    def test_no_contact_contents(self):
        with tempfile.TemporaryDirectory() as p:
            q=Path(p)/'noCRM';q.mkdir();(q/'AGENT.md').write_text('# test')
            (q/'contacts.csv').write_text('secret-value')
            d=json.dumps(scan(p))
            self.assertNotIn('secret-value',d)
    def test_example_contract(self):
        q=json.loads((BASE/'examples'/'request-example.json').read_text())
        a=json.loads((BASE/'examples'/'answer-example.json').read_text())
        self.assertEqual(q['schema_version'],'0.1')
        self.assertFalse(a['execution_claimed'])
    def test_integration_non_destructive(self):
        s=(ROOT/'help'/'INTEGRATION-SUITE.md').read_text(encoding='utf-8')
        self.assertIn('nicht überschreiben',s)
    def test_context_doc_not_proof(self):
        self.assertIn('kein Inhaltsnachweis',(BASE/'KONTEXT.md').read_text())

if __name__=='__main__':unittest.main()
