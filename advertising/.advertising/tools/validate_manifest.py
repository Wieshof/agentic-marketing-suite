#!/usr/bin/env python3
"""Lokaler Preflight für kanonische Advertising-Manifeste. Keine externen Requests."""
import json,sys,re,datetime
from decimal import Decimal,InvalidOperation
from pathlib import Path

def check(x):
    e=[]
    required=['schema_version','campaign_id','platform','action','status','account_ref','objective','currency','budget','creatives','landing_url','approval']
    if not isinstance(x,dict): return ['JSON muss ein Objekt sein']
    e += ['Pflichtfeld fehlt: '+k for k in required if k not in x]
    if e:return e
    if x['schema_version']!='0.1':e.append('Version nicht unterstützt')
    if x['action'] not in ['draft','stage_paused','activate','update','pause','report']:e.append('Unbekannte Aktion')
    if x['status'] not in ['draft','ready_for_review','approved','staged','active','paused','completed','error','rejected']:e.append('Status ungültig')
    if not isinstance(x['currency'],str) or not re.fullmatch('[A-Z]{3}',x['currency']):e.append('Währung muss ISO-artiger Großbuchstabencode sein')
    if not isinstance(x['landing_url'],str) or not x['landing_url'].startswith('https://'):e.append('HTTPS-Landingpage nötig')
    if not isinstance(x['creatives'],list) or not x['creatives']:e.append('Mindestens ein Creative/Briefing erforderlich')
    b=x.get('budget',{})
    try:
        lifetime=Decimal(b['lifetime_max']); daily=Decimal(b['daily_max'])
        if lifetime<0 or daily<0: e.append('Budget negativ')
        if lifetime>0 and daily>lifetime: e.append('Daily Cap > Lifetime Cap')
        if any(not re.fullmatch(r'(0|[1-9][0-9]*)(\.[0-9]{1,2})?',str(v)) for v in (b['lifetime_max'],b['daily_max'])): e.append('Budgetformat: maximal zwei Dezimalstellen, keine Exponenten')
        start=datetime.date.fromisoformat(b['period_start']); end=datetime.date.fromisoformat(b['period_end'])
        if end<start:e.append('Enddatum vor Startdatum')
    except (KeyError,TypeError,ValueError,InvalidOperation):e.append('Budget oder Zeitraum unbrauchbar'); lifetime=Decimal('-1')
    a=x.get('action'); app=x.get('approval',{})
    if not isinstance(app,dict):app={}
    external=a in ['stage_paused','activate','update','pause']
    if external:
        if str(x.get('account_ref','')).upper() in {'','NOT_CONNECTED','DEMO'}:e.append('Keine reale Kontoreferenz')
        if not x.get('platform_account_verified'):e.append('Plattformkonto nicht verifiziert')
        if not x.get('capability_preflight'):e.append('Live-Capability nicht geprüft')
        if not x.get('claims_reviewed') or not x.get('legal_reviewed'):e.append('Claims-/Rechtsprüfung fehlt')
        if not app.get('ref') or not app.get('approved_by'):e.append('Genehmigungsreferenz fehlt')
        if app.get('approved_action')!=a:e.append('Freigabe deckt angefragte Aktion nicht')
        try:
            approved=Decimal(str(app.get('approved_budget')))
            if lifetime>approved:e.append('Budget größer als genehmigt')
        except (InvalidOperation,TypeError):e.append('Freigegebener Budgetbetrag fehlt')
        if a=='activate' and x.get('status') not in ['approved','staged']:e.append('Aktivierung nur nach approved/staged')
        if a=='stage_paused' and x.get('status') not in ['approved','ready_for_review']:e.append('Staging nur nach review/approval')
        if a in ['update','pause'] and not x.get('external_ids'):e.append('Update/Pause ohne bestehende Plattform-ID')
    if a=='draft' and x['status'] not in ['draft','ready_for_review']:e.append('Draft-Aktion mit unzulässigem Status')
    return e

def main():
    if len(sys.argv)!=2:sys.exit('Nutzung: validate_manifest.py manifest.json')
    try: x=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as exc:sys.exit('ERROR: '+str(exc))
    errors=check(x)
    if errors:
        print('BLOCKED — '+str(len(errors))+' Problem(e):')
        for err in errors:print(' - '+err)
        sys.exit(2)
    print('PASS — lokale Struktur- und Sicherheitslogik. KEINE AUTHENTIFIZIERUNG, FREIGABE ODER AUSFÜHRUNG.')
if __name__=='__main__':main()
