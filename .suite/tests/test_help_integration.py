"""Actual Help CLI inventory, standalone package and additive Suite contracts."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.suite/tools'))
from validate_records import check


class HelpIntegrationTests(unittest.TestCase):
    def test_help_can_lead_support_and_own_explanations(self):
        order = dict(id='help-job', objective='Explain an existing campaign plan',
                     lead_module='help', supporting_modules=['marketing'],
                     status='proposed', created_at='2026-10-27T12:00:00+01:00', input_refs=[])
        check('work-order', order)
        check('work-order', dict(order, lead_module='marketing', supporting_modules=['help']))
        check('artifact', dict(id='help-guide', owner_module='help',
                              path='help/anleitungen/erster-auftrag.md', version=1, status='draft',
                              contains_personal_data=False, rights_status='pending'))

    def test_real_suite_inventory_agrees_with_contract_without_runtime_claims(self):
        result = subprocess.run([sys.executable, str(ROOT / 'help/.help/tools/scan_workspace.py'),
                                 '--root', str(ROOT)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        inventory = json.loads(result.stdout)
        expected = json.loads((ROOT / '.suite/contracts/work-order.schema.json').read_text())['properties']['lead_module']['enum']
        self.assertEqual({m['name'] for m in inventory['modules']}, set(expected))
        self.assertEqual(inventory['module_count_observed'], len(expected))
        self.assertEqual(inventory['scope'], 'file_inventory_only')
        self.assertTrue(all(m['runtime_status'] == 'unknown' for m in inventory['modules']))
        self.assertTrue(inventory['suite_governance_present'])

    def test_help_operates_and_tests_without_suite_or_other_modules(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            shutil.copytree(ROOT / 'help', folder / 'help', ignore=shutil.ignore_patterns('__pycache__'))
            scan = subprocess.run([sys.executable, str(folder / 'help/.help/tools/scan_workspace.py'),
                                   '--root', str(folder)], capture_output=True, text=True)
            self.assertEqual(scan.returncode, 0, scan.stderr)
            inventory = json.loads(scan.stdout)
            self.assertFalse(inventory['suite_governance_present'])
            self.assertEqual([m['name'] for m in inventory['modules']], ['help'])
            validate = subprocess.run([sys.executable, str(folder / 'help/.help/tools/validate_help.py'),
                                       '--root', str(folder)], capture_output=True, text=True)
            self.assertEqual(validate.returncode, 0, validate.stderr)
            self.assertTrue(json.loads(validate.stdout)['ok'])
            tests = subprocess.run([sys.executable, '-m', 'unittest', 'discover',
                                    '-s', str(folder / 'help/.help/tests'), '-v'],
                                   cwd=folder, capture_output=True, text=True)
            self.assertEqual(tests.returncode, 0, tests.stderr)

    def test_help_check_fails_when_a_linked_guide_is_missing(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            shutil.copytree(ROOT / 'help', folder / 'help', ignore=shutil.ignore_patterns('__pycache__'))
            guide = folder / 'help/.help/guides/grundlagen/was-ist-die-suite.md'
            guide.unlink()
            result = subprocess.run([sys.executable, str(folder / 'help/.help/tools/validate_help.py'),
                                     '--root', str(folder)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            report = json.loads(result.stdout)
            self.assertFalse(report['ok'])
            self.assertTrue(any('Linkziel fehlt' in issue for issue in report['issues']))


if __name__ == '__main__':
    unittest.main()
