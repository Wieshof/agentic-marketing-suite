/* Optional first-party aggregate pageview counter. No cookies, identifiers or query strings. */
'use strict';
(() => {
  if (navigator.doNotTrack === '1' || navigator.globalPrivacyControl === true) return;
  const script = document.currentScript;
  const endpoint = new URL(script?.dataset.endpoint || '/api/analytics.php', location.href);
  if (endpoint.origin !== location.origin) return;
  fetch(endpoint, {method:'POST', headers:{'Content-Type':'application/json'},
    body:JSON.stringify({page:location.pathname}), credentials:'omit', redirect:'error',
    cache:'no-store', keepalive:true}).catch(() => {});
})();
