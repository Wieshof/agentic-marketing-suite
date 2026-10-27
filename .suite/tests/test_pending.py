"""Fictional demo logs and temporary files only; read-only, no decisions."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import pending

SUITE = Path(__file__).resolve().parents[1]


class PendingTests(unittest.TestCase):
    def test_demo_logs(self):
        demo = SUITE / 'beispiele/approval-demo'
        items, errors = pending.collect([('demo', demo / 'approvals-demo.jsonl'),
                                         ('revoked', demo / 'approvals-revoked-demo.jsonl')])
        self.assertEqual(errors, [])
        self.assertTrue(all(item['status'] in pending.OPEN for item in items))

    def test_broken_log_is_an_error_not_all_clear(self):
        with tempfile.TemporaryDirectory() as temp:
            broken = Path(temp) / 'approvals.jsonl'
            broken.write_text('{not json\n', encoding='utf-8')
            self.assertEqual(pending.main(['--log', str(broken)]), 2)


if __name__ == '__main__':
    unittest.main()
