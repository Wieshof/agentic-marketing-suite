#!/usr/bin/env python3
"""Local offline unit tests for Business-DNA reference tools."""
import json
import tempfile
import unittest
from pathlib import Path
from lint_records import load_jsonl,validate_claims
from build_context import compose

ROOT=Path(__file__).resolve().parent.parent / 'beispiele' / 'topaca'

class TestContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims=load_jsonl(ROOT/'claims.jsonl')
        cls.sources=load_jsonl(ROOT/'sources.jsonl')
    def pack(self,**kw):
        return compose(self.claims,self.sources,kw.get('requester','advertising'),
                       kw.get('purpose','product check'),kw.get('topics',['product']),
                       kw.get('visibility','shared'),'2026-10-27',kw.get('max_characters',6000))
    def test_jsonl_loads(self):self.assertEqual(len(self.claims),5)
    def test_example_passes(self):self.assertEqual(validate_claims(self.claims,self.sources),[])
    def test_restricted_not_exported(self):
        x=self.pack(topics=[],visibility='shared')
        self.assertNotIn('claim-topaca-005',[t['claim_id'] for t in x['claims']])
    def test_public_source_is_not_shared(self):self.assertEqual(len(self.pack(visibility='public')['claims']),0)
    def test_planned_status_preserved(self):
        x=self.pack()
        self.assertEqual([c['status'] for c in x['claims'] if c['claim_id']=='claim-topaca-003'],['planned'])
    def test_filter_by_topic(self):
        x=self.pack(topics=['stage'])
        self.assertEqual([c['claim_id'] for c in x['claims']],['claim-topaca-002'])
    def test_unknown_source_rejected(self):
        bad=[dict(x) for x in self.claims]
        bad[0]['source_refs']=['missing']
        self.assertTrue(any('missing source' in x for x in validate_claims(bad,self.sources)))
    def test_verified_without_strong_source_rejected(self):
        bad=[dict(x) for x in self.claims];bad[0]['status']='verified'
        self.assertTrue(any('verified without' in x for x in validate_claims(bad,self.sources)))
    def test_duplicate_ids_rejected(self):
        self.assertTrue(any('duplicate claim_id' in x for x in validate_claims(self.claims+[self.claims[0]],self.sources)))
    def test_invalid_timestamp_rejected(self):
        bad=[dict(x) for x in self.claims];bad[0]['updated_at']='yesterday'
        self.assertTrue(any('invalid updated_at' in x for x in validate_claims(bad,self.sources)))
    def test_budget_observed(self):
        x=self.pack(max_characters=950)
        self.assertLessEqual(len(json.dumps(x,ensure_ascii=False)),950)
    def test_historical_as_of_excludes_newer_claims(self):
        x=compose(self.claims,self.sources,'marketing','history',['product'],'shared','2026-10-26',6000)
        self.assertEqual(x['claims'],[])
    def test_invalid_jsonl_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'bad.jsonl';p.write_text('{not json}',encoding='utf-8')
            with self.assertRaises(ValueError):load_jsonl(p)

if __name__=='__main__':unittest.main(verbosity=2)
