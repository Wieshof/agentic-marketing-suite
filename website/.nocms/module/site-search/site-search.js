/* Client-only search. Search terms never leave this page. */
'use strict';
(async () => {
  const form = document.querySelector('[data-site-search]');
  if (!form) return;
  const input = form.querySelector('input[type="search"]');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-status');
  form.addEventListener('submit', event => event.preventDefault());
  let pages;
  const normalize = text => text.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('de');
  try {
    const url = new URL(form.dataset.index || '/search-index.json', location.href);
    if (url.origin !== location.origin) throw Error('origin');
    const response = await fetch(url, {credentials:'omit', redirect:'error', cache:'no-cache'});
    if (!response.ok) throw Error('load');
    const data = await response.json();
    if (!Array.isArray(data) || data.length > 1000) throw Error('index');
    pages = data.filter(page => typeof page.title==='string' && typeof page.text==='string' && typeof page.url==='string' && page.url.startsWith('/') && !page.url.startsWith('//') && !page.url.includes('\\'));
  } catch { status.textContent = 'Die Suche ist derzeit nicht verfügbar.'; return; }
  form.addEventListener('submit', event => {
    event.preventDefault();results.replaceChildren();
    const query = normalize(input.value.trim().slice(0, 200));
    if (query.length < 2) {status.textContent='Bitte mindestens zwei Zeichen eingeben.';return;}
    const words = query.split(/\s+/).filter(Boolean);
    const matches = pages.filter(page => words.every(word => normalize(page.title+' '+page.text).includes(word))).slice(0, 50);
    for (const page of matches) {
      const item=document.createElement('li'),link=document.createElement('a'),excerpt=document.createElement('p');
      link.href=page.url;link.textContent=page.title;excerpt.textContent=page.text.slice(0,180);item.append(link,excerpt);results.append(item);
    }
    status.textContent = matches.length ? matches.length+' Treffer' : 'Keine passenden Seiten gefunden.';
  });
})();
