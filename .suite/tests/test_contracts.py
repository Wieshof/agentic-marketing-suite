import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from validate_records import check,CheckError
T='2026-10-23T13:00:00+02:00'
class TestSuiteContracts(unittest.TestCase):
 def test_work_order(self):
  check('work-order',dict(id='abcd',objective='Build a relevant campaign',lead_module='marketing',status='proposed',created_at=T,input_refs=[]))
 def test_invalid_module(self):
  with self.assertRaises(CheckError):check('work-order',dict(id='abcd',objective='Build a relevant campaign',lead_module='imaginary',status='proposed',created_at=T,input_refs=[]))
 def test_artifact_relpath(self):
  r=dict(id='abcd',owner_module='creative',path='../secrets',version=1,status='draft',contains_personal_data=False,rights_status='pending')
  with self.assertRaises(CheckError):check('artifact',r)
 def test_artifact_draft(self):
  r=dict(id='abcd',owner_module='creative',path='creative/projekt/x.svg',version=1,status='draft',contains_personal_data=False,rights_status='pending')
  check('artifact',r)
 def test_review_requires_evidence(self):
  r=dict(id='abcd',artifact_id='item1',artifact_version=1,dimension='legal',status='pass',reviewed_at=T,findings=[])
  with self.assertRaises(CheckError):check('review',r)
 def test_review_warning(self):
  r=dict(id='abcd',artifact_id='item1',artifact_version=1,dimension='legal',status='warning',reviewed_at=T,findings=[dict(severity='minor',message='Need current terms')])
  check('review',r)
 def test_spend_budget(self):
  r=dict(id='abcd',artifact_id='item1',artifact_version=1,artifact_sha256='a'*64,action='spend',target='google_ads',decision='approved',authorizer='authorized person',decided_at=T)
  with self.assertRaises(CheckError):check('action-approval',r)
 def test_confirmed_requires_id(self):
  r=dict(id='abcd',artifact_id='item1',artifact_version=1,artifact_sha256='a'*64,action='publish',target='website',decision='approved',authorizer='authorized person',decided_at=T,execution_status='confirmed')
  with self.assertRaises(CheckError):check('action-approval',r)
 def test_basic_action(self):
  r=dict(id='abcd',artifact_id='item1',artifact_version=1,artifact_sha256='a'*64,action='publish',target='website',decision='pending',authorizer='authorized person',decided_at=T,execution_status='not_attempted')
  check('action-approval',r)
 def test_boolean_version_rejected(self):
  r=dict(id='abcd',owner_module='creative',path='creative/file.svg',version=True,status='draft',contains_personal_data=False,rights_status='pending')
  with self.assertRaises(CheckError):check('artifact',r)
if __name__=='__main__':unittest.main()
