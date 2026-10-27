#!/usr/bin/env python3
"""Read-only inventory of module entrypoints. No process, API or account checks."""
import argparse,json
from pathlib import Path

def scan(root):
    root=Path(root).resolve()
    if not root.is_dir(): raise ValueError(f'Workspace nicht gefunden: {root}')
    exclude={'input','archiv','tests','docs','examples','node_modules','.git'}
    modules=[]
    for p in sorted(root.iterdir(),key=lambda x:x.name.lower()):
        if not p.is_dir() or p.name.startswith('.') or p.name in exclude: continue
        agent=p/'AGENT.md'
        if not agent.is_file(): continue
        internal_dirs=[x for x in p.iterdir() if x.is_dir() and x.name.startswith('.')]
        methods=sum(1 for d in internal_dirs for f in (d/'methoden').rglob('*.md') if f.is_file())
        modules.append({'name':p.name,'agent_present':True,'internal_dirs':[x.name for x in internal_dirs], 'method_files_observed':methods, 'runtime_status':'unknown'})
    return {'root':str(root),'suite_governance_present':(root/'.suite').is_dir(), 'module_count_observed':len(modules),'modules':modules,'scope':'file_inventory_only','warning':'Dateiexistenz ist kein Nachweis konfigurierter oder getesteter Laufzeitfähigkeiten.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Read-only Suite-Dateiinventar')
    parser.add_argument('--root',default='.')
    parser.add_argument('--output',default=None)
    args=parser.parse_args()
    out=json.dumps(scan(args.root),ensure_ascii=False,indent=2)
    if args.output:
        Path(args.output).write_text(out+'\n',encoding='utf-8')
    else: print(out)
