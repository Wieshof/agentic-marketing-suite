import importlib.util
import json
import os
from pathlib import Path
import shlex
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[3]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
web=load('webmodules','website/.nocms/tools/webmodules.py')
sftp=load('publisher','website/.nocms/integrationen/sftp/publisher.py')


class WebCapabilityTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.site=self.root/'site';self.site.mkdir();(self.site/'index.html').write_text('<title>Start</title><h1>Grüße</h1><script>SECRET_SCRIPT</script>')
        self.config=dict(type='sftp',source='site',target='/public_html',host='example.invalid',port=22,username='web',credential_ref='WEB',delete_remote=False,verify_upload=True)
    def test_selected_runtime_installation_is_independent_and_preserves_local_files(self):
        self.assertFalse((self.site/'api').exists())
        web.install(self.site,'contact-form');web.install(self.site,'newsletter');web.install(self.site,'analytics-lite')
        self.assertTrue((self.site/'api/contact.php').exists());self.assertFalse((self.site/'AGENT.md').exists())
        web.install(self.site,'contact-form')
        (self.site/'api/contact.php').write_text('custom')
        with self.assertRaises(web.ModuleError):web.install(self.site,'contact-form')
        self.assertEqual((self.site/'api/contact.php').read_text(),'custom')
    def test_search_and_sitemap_exclude_private_noindex_and_script_data(self):
        (self.site/'.env.html').write_text('PRIVATE')
        (self.site/'private.html').write_text('<meta name="robots" content="noindex">PRIVATE')
        web.install(self.site,'site-search');web.build_search(self.site)
        data=json.loads((self.site/'search-index.json').read_text())
        self.assertEqual(len(data),1);self.assertEqual(data[0]['url'],'/');self.assertIn('Grüße',data[0]['text']);self.assertNotIn('SECRET',data[0]['text'])
        web.build_sitemap(self.site,'https://example.invalid')
        tree=ET.parse(self.site/'sitemap.xml');self.assertEqual([e.text for e in tree.findall('.//{*}loc')],['https://example.invalid/'])
        with self.assertRaises(web.ModuleError):web.build_sitemap(self.site,'https://user:pass@example.invalid')
    def test_redirects_are_exact_local_and_cannot_overwrite_or_loop(self):
        web.build_redirects(self.site,[{'from':'/old.html','to':'/new.html','status':301}])
        self.assertIn('^/old\\.html$',(self.site/'.htaccess').read_text())
        with self.assertRaises(web.ModuleError):web.build_redirects(self.site,[])
        (self.site/'.htaccess').unlink()
        for rules in ([{'from':'/a','to':'//evil.invalid','status':302}], [{'from':'/a','to':'/b','status':301},{'from':'/b','to':'/a','status':301}], [{'from':'/a\nInjected','to':'/b','status':301}]):
            with self.subTest(rules=rules),self.assertRaises(web.ModuleError):web.build_redirects(self.site,rules)
        self.assertFalse((self.site/'.htaccess').exists())
    def test_plan_refuses_private_symlink_and_unsafe_commands(self):
        value=sftp.plan(self.root,self.config);self.assertEqual(value['files'][0]['path'],'index.html')
        for field,changed in [('host','-oProxyCommand=evil'),('target','/public\nrm /'),('source','../outside'),('delete_remote',True),('verify_upload',False)]:
            with self.subTest(field=field),self.assertRaises((sftp.CapabilityError,ValueError)):
                sftp.plan(self.root,dict(self.config,**{field:changed}))
        secret=self.site/'.env';secret.write_text('secret')
        with self.assertRaises(sftp.CapabilityError):sftp.plan(self.root,self.config)
        secret.unlink();(self.site/'alias').symlink_to(self.site/'index.html')
        with self.assertRaises(sftp.CapabilityError):sftp.plan(self.root,self.config)
    def test_sftp_checks_host_keys_stages_and_verifies_exact_remote_bytes(self):
        value=sftp.plan(self.root,self.config);remote={};commands=[]
        key=self.root/'key';known=self.root/'known';key.write_text('fictional');known.write_text('fictional')
        def runner(command,**kwargs):
            commands.append(command)
            for line in kwargs['input'].splitlines():
                parts=shlex.split(line)
                if parts[0]=='put':remote[parts[2]]=Path(parts[1]).read_bytes()
                if parts[0]=='get':Path(parts[2]).write_bytes(remote[parts[1]])
                if parts[0]=='rename':remote[parts[2]]=remote.pop(parts[1])
            return SimpleNamespace(returncode=0)
        with patch.dict(os.environ,{'WEB_KEY_FILE':str(key),'WEB_KNOWN_HOSTS_FILE':str(known)}),patch.object(sftp.shutil,'which',return_value='/usr/bin/sftp'):
            result=sftp.transfer(value,self.root,runner)
        self.assertEqual(result['status'],'confirmed');self.assertEqual(len(commands),3)
        self.assertIn('-oStrictHostKeyChecking=yes',commands[0]);self.assertIn('-oBatchMode=yes',commands[0])
        self.assertEqual(remote['/public_html/index.html'],(self.site/'index.html').read_bytes())
    def test_changed_release_and_failed_readback_never_claim_success(self):
        value=sftp.plan(self.root,self.config);(self.site/'index.html').write_text('changed')
        with self.assertRaises(sftp.CapabilityError):sftp.transfer(value,self.root)
        value=sftp.plan(self.root,self.config);key=self.root/'key';known=self.root/'known';key.write_text('fictional');known.write_text('fictional')
        def runner(command,**kwargs):
            for line in kwargs['input'].splitlines():
                parts=shlex.split(line)
                if parts[0]=='get':Path(parts[2]).write_text('wrong')
            return SimpleNamespace(returncode=0)
        with patch.dict(os.environ,{'WEB_KEY_FILE':str(key),'WEB_KNOWN_HOSTS_FILE':str(known)}),patch.object(sftp.shutil,'which',return_value='/usr/bin/sftp'):
            with self.assertRaises(sftp.CapabilityError):sftp.transfer(value,self.root,runner)
    def test_symlinked_install_and_index_paths_are_refused(self):
        external=self.root/'external';external.mkdir();(self.site/'api').symlink_to(external)
        with self.assertRaises(web.ModuleError):web.install(self.site,'contact-form')
        (self.site/'public.html').symlink_to(self.root/'outside.html');(self.root/'outside.html').write_text('secret')
        with self.assertRaises(web.ModuleError):web.public_pages(self.site)
