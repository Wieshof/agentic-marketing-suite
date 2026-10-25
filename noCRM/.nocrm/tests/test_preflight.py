import importlib.util
from pathlib import Path
import unittest
from datetime import datetime, timezone, timedelta

spec=importlib.util.spec_from_file_location('preflight',Path(__file__).parents[1]/'tools'/'preflight.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
NOW=datetime(2026,10,23,tzinfo=timezone.utc)

def contact(): return {'contact_id':'D-1','display_name':'Demo','email':'demo@example.invalid','phone':'+4300000000'}
def consent(status='granted',evidence='test-proof',when=None):
    return {'contact_id':'D-1','channel':'email','purpose':'marketing','status':status,'recorded_at':when or '2026-10-20T12:00:00+00:00','evidence_ref':evidence,'basis':'consent','valid_until':''}
def draft(**kw):
    d={'draft_id':'DRAFT-1','contact_id':'D-1','channel':'email','purpose':'marketing','body':'Example', 'status':'approved','review':{'approved':True},'authorization':{'allowed':True},'idempotency_key':'K-1'}
    d.update(kw);return d
class TestNoCRM(unittest.TestCase):
    def eligible(self,d,c=None,x=None):return mod.run(c if c is not None else [contact()],x if x is not None else [consent()],d,now=NOW)
    def test_valid_eligible_but_never_sends(self):
        r=self.eligible(draft());self.assertTrue(r['eligible']);self.assertEqual(r['action'],'DRY_RUN_ONLY')
    def test_unknown_is_blocked(self):self.assertFalse(self.eligible(draft(),x=[consent('unknown')])['eligible'])
    def test_revoked_is_blocked(self):self.assertFalse(self.eligible(draft(),x=[consent('revoked')])['eligible'])
    def test_denied_is_blocked(self):self.assertFalse(self.eligible(draft(),x=[consent('denied')])['eligible'])
    def test_expired_is_blocked(self):
        x=consent();x['valid_until']='2026-10-22T12:00:00+00:00';self.assertFalse(self.eligible(draft(),x=[x])['eligible'])
    def test_evidence_missing(self):self.assertFalse(self.eligible(draft(),x=[consent(evidence='')])['eligible'])
    def test_future_consent(self):self.assertFalse(self.eligible(draft(),x=[consent(when='2027-01-01T12:00:00+00:00')])['eligible'])
    def test_contact_missing(self):self.assertFalse(self.eligible(draft(contact_id='other'))['eligible'])
    def test_duplicate_contact(self):self.assertFalse(self.eligible(draft(),c=[contact(),contact()])['eligible'])
    def test_authorization_missing(self):self.assertFalse(self.eligible(draft(authorization={'allowed':False}))['eligible'])
    def test_review_missing(self):self.assertFalse(self.eligible(draft(review={'approved':False}))['eligible'])
    def test_empty_body(self):self.assertFalse(self.eligible(draft(body=''))['eligible'])
    def test_nonmarketing_context_missing(self):self.assertFalse(self.eligible(draft(purpose='service'))['eligible'])
    def test_nonmarketing_verified(self):self.assertTrue(self.eligible(draft(purpose='service',context_verified=True),x=[])['eligible'])
    def test_whatsapp_window_missing(self):
        d=draft(channel='whatsapp',purpose='service',context_verified=True);self.assertFalse(self.eligible(d,x=[])['eligible'])
    def test_telegram_initiation_missing(self):
        d=draft(channel='telegram',purpose='service',context_verified=True);self.assertFalse(self.eligible(d,x=[])['eligible'])
    def test_ai_disclosure(self):
        self.assertFalse(self.eligible(draft(direct_ai_interaction=True))['eligible'])
    def test_idempotency(self):self.assertFalse(self.eligible(draft(idempotency_key=''))['eligible'])
    def test_invalid_state(self):self.assertFalse(self.eligible(draft(status='sent'))['eligible'])
    def test_valid_whatsapp_service(self):
        d=draft(channel='whatsapp',purpose='service',context_verified=True,within_24h=True,escalation_route_confirmed=True)
        self.assertTrue(self.eligible(d,x=[])['eligible'])
if __name__=='__main__':unittest.main()
