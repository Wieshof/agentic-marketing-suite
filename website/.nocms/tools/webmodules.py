#!/usr/bin/env python3
"""Install selected standalone templates; build static search/sitemap/Apache redirect outputs."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from pathlib import PurePosixPath
import re
import sys
from urllib.parse import quote, urlsplit, unquote
import xml.etree.ElementTree as ET

MODULES = Path(__file__).resolve().parents[1] / 'module'
TEMPLATES = {
    'contact-form': [('contact-form/contact.php','api/contact.php'), ('common/runtime.php','api/_runtime.php'), ('common/maintenance.php','api/maintenance.php')],
    'newsletter': [('newsletter/newsletter.php','api/newsletter.php'), ('common/runtime.php','api/_runtime.php'), ('common/maintenance.php','api/maintenance.php')],
    'analytics-lite': [('analytics-lite/analytics.php','api/analytics.php'), ('analytics-lite/analytics-lite.js','js/analytics-lite.js'), ('common/runtime.php','api/_runtime.php'), ('common/maintenance.php','api/maintenance.php')],
    'site-search': [('site-search/site-search.js','js/site-search.js'), ('site-search/search.html','search.html')],
}


class ModuleError(ValueError):pass


def safe_root(site):
    site = Path(site)
    if site.is_symlink():raise ModuleError('Site root must not be a symlink')
    site.mkdir(parents=True, exist_ok=True)
    return site.resolve(strict=True)


def output_path(site, relative):
    path = site / relative
    for parent in (path, *path.parents):
        if parent == site:break
        if parent.is_symlink():raise ModuleError('Generated paths must not be symlinks')
    if path.exists() and not path.is_file():raise ModuleError('Output path is not a regular file')
    return path


def install(site, module):
    site = safe_root(site)
    if module not in TEMPLATES:raise ModuleError('This module is a build function, not a runtime template')
    outputs = [(output_path(site, relative), (MODULES / source).read_bytes()) for source, relative in TEMPLATES[module]]
    # Check all collisions before writing any selected template.
    for path, data in outputs:
        if path.exists() and path.read_bytes() != data:raise ModuleError('Existing local file differs; merge manually: '+str(path.relative_to(site)))
    for path, data in outputs:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('xb') as stream:stream.write(data)
    return [path.relative_to(site).as_posix() for path, _ in outputs]


class TextPage(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.ignored=0;self.in_title=False;self.title=[];self.text=[];self.noindex=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag in ('script','style','template'):self.ignored += 1
        if tag=='title':self.in_title=True
        if tag=='meta' and (attrs.get('name') or '').lower()=='robots' and 'noindex' in (attrs.get('content') or '').lower():self.noindex=True
    def handle_endtag(self, tag):
        if tag in ('script','style','template') and self.ignored:self.ignored -= 1
        if tag=='title':self.in_title=False
    def handle_data(self, data):
        if self.ignored:return
        if self.in_title:self.title.append(data)
        self.text.append(data)


def public_pages(site):
    site = Path(site).resolve(strict=True)
    pages=[]
    for path in sorted(site.rglob('*.html')):
        relative=path.relative_to(site)
        if any(part.startswith('.') or part in ('node_modules','archiv','input') for part in relative.parts):continue
        if any(parent.is_symlink() for parent in (path,*path.parents) if parent!=site and site in parent.parents) or path.is_symlink():raise ModuleError('Symlinked pages are not indexed')
        if path.stat().st_size>1024*1024:raise ModuleError('HTML page exceeds 1 MiB')
        parser=TextPage();parser.feed(path.read_text(encoding='utf-8'))
        if parser.noindex:continue
        url='/' + quote(relative.as_posix(),safe='/')
        if url.endswith('/index.html'):url=url[:-len('index.html')]
        pages.append({'url':url,'title':' '.join(' '.join(parser.title).split()) or relative.stem,'text':' '.join(' '.join(parser.text).split())[:20000]})
        if len(pages)>1000:raise ModuleError('Search index exceeds 1000 pages')
    return pages


def site_url(value):
    parsed=urlsplit(value)
    if parsed.scheme!='https' or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path not in ('','/'):
        raise ModuleError('HTTPS site origin without credentials, path or query required')
    return value.rstrip('/')


def build_search(site):
    site=Path(site).resolve(strict=True)
    data=json.dumps(public_pages(site),ensure_ascii=False,indent=2)+'\n'
    if len(data.encode())>5*1024*1024:raise ModuleError('Search index exceeds 5 MiB')
    output_path(site,'search-index.json').write_text(data,encoding='utf-8')
    return 'search-index.json'


def build_sitemap(site, origin):
    site=Path(site).resolve(strict=True);origin=site_url(origin)
    root=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for page in public_pages(site):ET.SubElement(ET.SubElement(root,'url'),'loc').text=origin+page['url']
    ET.ElementTree(root).write(output_path(site,'sitemap.xml'),encoding='utf-8',xml_declaration=True)
    return 'sitemap.xml'


def redirect_path(value):
    if not isinstance(value,str) or not re.fullmatch(r'/(?!/)[A-Za-z0-9/._~%-]*',value) or '..' in unquote(value).split('/') or '\\' in unquote(value) or any(ord(c)<32 for c in unquote(value)):
        raise ModuleError('Redirects require safe local URL paths')
    return value


def build_redirects(site, rules):
    site=Path(site).resolve(strict=True)
    if not isinstance(rules,list):raise ModuleError('Redirect mappings must be an array')
    edges={};lines=['# Generated exact redirects. Apache mod_alias required. Review before deployment.']
    for rule in rules:
        if not isinstance(rule,dict) or set(rule)!={'from','to','status'} or type(rule['status']) is not int or rule['status'] not in (301,302):raise ModuleError('Redirect supports explicit 301/302 mappings')
        source,destination=redirect_path(rule['from']),redirect_path(rule['to'])
        if source in edges or source==destination:raise ModuleError('Duplicate or self redirect')
        edges[source]=destination
        lines.append(f'RedirectMatch {rule["status"]} "^{re.escape(source)}$" "{destination}"')
    for start in edges:
        seen=set();node=start
        while node in edges:
            if node in seen:raise ModuleError('Redirect cycle detected')
            seen.add(node);node=edges[node]
    path=output_path(site,'.htaccess')
    if path.exists():raise ModuleError('Existing .htaccess must be merged manually, never replaced')
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return '.htaccess'


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--site',type=Path,required=True)
    sub=parser.add_subparsers(dest='command',required=True)
    item=sub.add_parser('install');item.add_argument('module',choices=sorted(TEMPLATES))
    sub.add_parser('search-index')
    item=sub.add_parser('sitemap');item.add_argument('--origin',required=True)
    item=sub.add_parser('redirects');item.add_argument('--input',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.command=='install':result=install(args.site,args.module)
        elif args.command=='search-index':result=build_search(args.site)
        elif args.command=='sitemap':result=build_sitemap(args.site,args.origin)
        else:result=build_redirects(args.site,json.loads(args.input.read_text()))
        print(json.dumps({'status':'local_files_created','files':result}));return 0
    except (ModuleError,OSError,ValueError,TypeError):
        print('WEBMODULE_BLOCKED: invalid configuration, unsafe path or existing local file',file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
