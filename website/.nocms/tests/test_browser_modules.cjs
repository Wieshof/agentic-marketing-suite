'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const root=path.resolve(__dirname,'../module');
class Element {
  constructor(tag){this.tag=tag;this.children=[];this.textContent='';this.listeners={};this.dataset={};this.value='';}
  append(...items){this.children.push(...items);}
  replaceChildren(...items){this.children=items;}
  addEventListener(type,fn){(this.listeners[type] ||= []).push(fn);}
  set innerHTML(_){throw Error('HTML injection is forbidden');}
}
test('search terms stay local; attacker URLs and HTML do not become executable content',async()=>{
  const form=new Element('form'),input=new Element('input'),results=new Element('ul'),status=new Element('p');
  form.querySelector=()=>input;const calls=[];
  const context={URL,location:{origin:'https://example.invalid',href:'https://example.invalid/search.html'},document:{querySelector:()=>form,getElementById:id=>id==='search-results'?results:status,createElement:tag=>new Element(tag)},fetch:async(...args)=>{calls.push(args);return {ok:true,json:async()=>[{title:'<img onerror=bad>',text:'private search match',url:'/good.html'},{title:'Bad',text:'private',url:'//evil.invalid'},{title:'Bad',text:'private',url:'/\t/evil.invalid'}]};}};
  await vm.runInNewContext(fs.readFileSync(path.join(root,'site-search/site-search.js'),'utf8'),context);
  input.value='private';let prevented=false;
  for(const handler of form.listeners.submit)handler({preventDefault(){prevented=true;}});
  assert.equal(prevented,true);assert.equal(calls.length,1);assert.equal(calls[0][0].pathname,'/search-index.json');
  assert.equal(results.children.length,1);assert.equal(results.children[0].children[0].textContent,'<img onerror=bad>');
  assert.equal(results.children[0].children[0].href,'/good.html');
});
test('analytics respects DNT/GPC, emits no identity/query, and refuses cross-origin endpoints',async()=>{
  const script=fs.readFileSync(path.join(root,'analytics-lite/analytics-lite.js'),'utf8');
  for(const mode of ['normal','dnt','gpc','foreign']){
    const calls=[];const context={URL,navigator:{doNotTrack:mode==='dnt'?'1':'0',globalPrivacyControl:mode==='gpc'},location:{origin:'https://example.invalid',href:'https://example.invalid/about.html?email=private',pathname:'/about.html'},document:{currentScript:{dataset:{endpoint:mode==='foreign'?'https://evil.invalid/collect':'/api/analytics.php'}}},fetch:(...args)=>{calls.push(args);return Promise.resolve({});}};
    vm.runInNewContext(script,context);
    assert.equal(calls.length,mode==='normal'?1:0);
    if(calls.length){const options=calls[0][1];assert.equal(options.credentials,'omit');assert.equal(options.body,JSON.stringify({page:'/about.html'}));assert.equal(options.redirect,'error');}
  }
});
