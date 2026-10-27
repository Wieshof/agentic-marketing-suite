#!/usr/bin/env python3
import unittest,sys,json,tempfile
from pathlib import Path
from copy import deepcopy
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from lint_records import lint
from build_brand_context import build
E=HERE.parent/'beispiele';S=HERE.parent/'schemas'
load=lambda name:json.loads((E/name).read_text(encoding='utf-8'))
class ContractTests(unittest.TestCase):
 def setUp(self):
  self.ap=load('demo-brand-approved.json');self.draft=load('demo-brand-draft.json');self.request=load('demo-request-public.json')
 def test_profile_valid(self):self.assertFalse(lint(self.ap,'brand-profile'))
 def test_draft_valid(self):self.assertFalse(lint(self.draft,'brand-profile'))
 def test_approved_needs_human(self):
  p=deepcopy(self.ap);p.pop('approved_by');self.assertTrue(lint(p,'brand-profile'))
 def test_approved_needs_timestamp(self):
  p=deepcopy(self.ap);p.pop('approved_at');self.assertTrue(lint(p,'brand-profile'))
 def test_approved_needs_decision(self):
  p=deepcopy(self.ap);p.pop('decision_ref');self.assertTrue(lint(p,'brand-profile'))
 def test_approved_invalid_timestamp(self):
  p=deepcopy(self.ap);p['approved_at']='no';self.assertTrue(lint(p,'brand-profile'))
 def test_naive_time_rejected(self):
  p=deepcopy(self.ap);p['updated_at']='2026-10-27T11:00:00';self.assertTrue(lint(p,'brand-profile'))
 def test_bad_visibility(self):
  p=deepcopy(self.ap);p['visibility']='world';self.assertTrue(lint(p,'brand-profile'))
 def test_invalid_status(self):
  p=deepcopy(self.ap);p['status']='certified';self.assertTrue(lint(p,'brand-profile'))
 def test_request_valid(self):self.assertFalse(lint(self.request,'brand-context-request'))
 def test_request_needs_topics(self):
  q=deepcopy(self.request);q['topics']=[];self.assertTrue(lint(q,'brand-context-request'))
 def test_pack_valid(self):
  result=build(self.request,[self.ap]);self.assertFalse(lint(result,'brand-context-pack'))
 def test_public_approved_included(self):
  r=build(self.request,[self.ap]);self.assertEqual(1,len(r['profiles']))
 def test_public_draft_excluded(self):
  r=build(self.request,[self.draft]);self.assertEqual(0,len(r['profiles']))
 def test_shared_profile_from_public_excluded(self):
  p=deepcopy(self.ap);p['visibility']='shared';r=build(self.request,[p]);self.assertEqual(0,len(r['profiles']))
 def test_restricted_profile_from_shared_excluded(self):
  p=deepcopy(self.ap);p['visibility']='restricted';q=deepcopy(self.request);q['audience']='shared';r=build(q,[p]);self.assertEqual(0,len(r['profiles']))
 def test_allowed_shared_included(self):
  p=deepcopy(self.ap);p['visibility']='shared';q=deepcopy(self.request);q['audience']='shared';r=build(q,[p]);self.assertEqual(1,len(r['profiles']))
 def test_only_requested_topics(self):
  r=build(self.request,[self.ap]);self.assertEqual({'positioning','promise','voice'},set(r['profiles'][0]['brand_platform']))
 def test_unknown_topics_rejected(self):
  q=deepcopy(self.request);q['topics']=['private_notes'];self.assertRaises(ValueError,build,q,[self.ap])
 def test_filter_by_brand_id(self):
  q=deepcopy(self.request);q['brand_ids']=['something-else'];r=build(q,[self.ap]);self.assertEqual([],r['profiles'])
 def test_decision_valid(self):self.assertFalse(lint(load('demo-decision.json'),'brand-decision'))
 def test_decision_requires_approver(self):
  d=load('demo-decision.json');d.pop('approved_by');self.assertTrue(lint(d,'brand-decision'))
 def test_review_valid(self):self.assertFalse(lint(load('demo-review.json'),'brand-review'))
 def test_all_schemas_json(self):
  for p in S.glob('*.json'):self.assertIsInstance(json.loads(p.read_text(encoding='utf-8')),dict)
 def test_schema_profile_logic_with_optional_jsonschema(self):
  try:import jsonschema
  except ImportError:return
  s=json.loads((S/'brand-profile.schema.json').read_text(encoding='utf-8'))
  jsonschema.Draft202012Validator(s,format_checker=jsonschema.FormatChecker()).validate(self.ap)
  bad=deepcopy(self.ap);bad.pop('approved_by')
  with self.assertRaises(jsonschema.ValidationError):jsonschema.validate(bad,s)
if __name__=='__main__':unittest.main(verbosity=2)
