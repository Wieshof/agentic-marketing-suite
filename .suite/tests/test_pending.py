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

class FailClosedPendingTests(unittest.TestCase):
    def setUp(self):
        import shutil
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.log = self.root / 'approvals.jsonl'
        shutil.copyfile(SUITE / 'beispiele/approval-demo/approvals-demo.jsonl', self.log)
        self.before = self.log.read_bytes()

    def test_locked_missing_symlink_and_oversized_log_never_clear(self):
        from unittest.mock import patch
        lock = self.log.with_name(self.log.name + '.lock')
        lock.touch()
        self.assertTrue(pending.collect([('locked', self.log)])[1])
        lock.unlink()
        alias = self.root / 'alias.jsonl'
        alias.symlink_to(self.log)
        self.assertTrue(pending.collect([('alias', alias)])[1])
        self.assertTrue(pending.collect([('missing', self.root / 'missing.jsonl')])[1])
        with patch.object(pending, 'MAX_LOG_BYTES', 1):
            self.assertTrue(pending.collect([('large', self.log)])[1])
        self.assertEqual(self.before, self.log.read_bytes())

    def test_lock_appearing_during_replay_discards_that_source(self):
        from unittest.mock import patch
        original = pending.summarize
        def read(*args, **kwargs):
            result = original(*args, **kwargs)
            self.log.with_name(self.log.name + '.lock').touch()
            return result
        with patch.object(pending, 'summarize', side_effect=read):
            items, errors = pending.collect([('updating', self.log)])
        self.assertFalse(items)
        self.assertTrue(errors)

    def test_partial_failure_preserves_valid_rows_and_returns_two(self):
        import contextlib, io, json
        broken = self.root / 'bad.jsonl'
        broken.write_text('not json\n')
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = pending.main(['--log', str(self.log), '--log', str(broken), '--json', '--strict'])
        self.assertEqual(code, 2)
        data = json.loads(output.getvalue())
        self.assertTrue(data['open'])
        self.assertTrue(data['errors'])
        self.assertEqual(self.before, self.log.read_bytes())

    def test_configuration_validation_relative_paths_and_strict_json(self):
        import contextlib, io, json
        cfg = self.root / 'dashboard.json'
        good = {'approvals': {'logs': [{'id': 'demo', 'label': 'Demo', 'path': 'approvals.jsonl'}]}}
        cfg.write_text(json.dumps(good))
        self.assertEqual(pending.configured_logs(cfg), [('Demo', self.log)])
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(pending.main(['--config', str(cfg), '--strict', '--json']), 1)
        self.assertTrue(json.loads(output.getvalue())['open'])
        for value in ('{bad', '[]', '{"approvals":{"logs":[{"id":"oops"}]}}', '{}'):
            cfg.write_text(value)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(pending.main(['--config', str(cfg), '--json']), 2)
            self.assertTrue(json.loads(output.getvalue())['errors'])


if __name__ == '__main__':
    unittest.main()
