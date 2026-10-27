"""Mocked HTTP only; no Google account, token or network is used."""
from datetime import date
import csv
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import fetch_google
from evaluate_csv import main as evaluate

GA4_PAGE = {'rowCount': 2, 'rows': [
    {'dimensionValues': [{'value': '20261001'}, {'value': 'Organic Search'}],
     'metricValues': [{'value': '120'}, {'value': '80'}, {'value': '100'}, {'value': '4'}]},
    {'dimensionValues': [{'value': '20261020'}, {'value': 'Organic Search'}],
     'metricValues': [{'value': '150'}, {'value': '90'}, {'value': '130'}, {'value': '6'}]}]}
GSC_PAGE = {'rows': [{'keys': ['2026-10-01'], 'clicks': 10, 'impressions': 200, 'ctr': 0.05, 'position': 7.5}]}


class FetchTests(unittest.TestCase):
    def run_fetch(self, argv, response):
        calls = []

        def post(url, body, token):
            calls.append((url, body, token))
            return response
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        with mock.patch.dict('os.environ', {'GOOGLE_OAUTH_ACCESS_TOKEN': 'fictional-token'}):
            code = fetch_google.main(argv + ['--out-dir', temp.name], post=post, today=date(2026, 10, 27))
        self.assertEqual(code, 0)
        return Path(temp.name), calls

    def test_ga4_writes_csv_and_manifest_without_token(self):
        out, calls = self.run_fetch(['ga4', '--property', '123'], GA4_PAGE)
        self.assertEqual(calls[0][1]['dateRanges'], [{'startDate': '2026-09-27', 'endDate': '2026-10-26'}])
        csv_path = out / 'ga4-123-2026-09-27-2026-10-26.csv'
        rows = list(csv.DictReader(csv_path.read_text(encoding='utf-8').splitlines()))
        self.assertEqual(rows[0]['date'], '2026-10-01')
        manifest_text = (out / 'ga4-123-2026-09-27-2026-10-26.manifest.json').read_text(encoding='utf-8')
        self.assertNotIn('fictional-token', manifest_text + csv_path.read_text(encoding='utf-8'))
        self.assertEqual(json.loads(manifest_text)['metric_definitions']['sessions']['aggregation'], 'sum')
        # Output is directly usable by the existing evaluator.
        self.assertEqual(evaluate(['--input', str(csv_path), '--metric', 'sessions',
                                   '--period-a', '2026-10-01:2026-10-10', '--period-b', '2026-10-11:2026-10-26']), 0)

    def test_gsc_keeps_position_additive_and_lags(self):
        out, calls = self.run_fetch(['gsc', '--site', 'sc-domain:example.org'], GSC_PAGE)
        self.assertIn('sc-domain%3Aexample.org', calls[0][0])
        self.assertEqual(calls[0][1]['endDate'], '2026-10-24')
        rows = list(csv.DictReader(next(out.glob('*.csv')).read_text(encoding='utf-8').splitlines()))
        self.assertEqual(rows[0]['position_x_impressions'], '1500.0')

    def test_missing_token_is_refused(self):
        with mock.patch.dict('os.environ', {}, clear=True), self.assertRaises(SystemExit):
            fetch_google.main(['ga4', '--property', '1', '--out-dir', '.'])


if __name__ == '__main__':
    unittest.main()
