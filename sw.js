/* Iron Ledger offline cache. The app shell is served from the cache first, so it
   opens with no signal; when there is signal, a fresh copy is fetched in the
   background and used next launch. */
const CACHE = 'ironledger-2026.11.16-2';
const ASSETS = [
  './',
  'index.html',
  'manifest.webmanifest',
  'icon-180.png',
  'icon-192.png',
  'icon-512.png',
  'fonts/big-shoulders-display-latin-700-normal.woff2',
  'fonts/big-shoulders-display-latin-800-normal.woff2',
  'fonts/ibm-plex-sans-latin-400-normal.woff2',
  'fonts/ibm-plex-sans-latin-500-normal.woff2',
  'fonts/ibm-plex-sans-latin-600-normal.woff2',
  'fonts/ibm-plex-sans-latin-700-normal.woff2',
  'fonts/ibm-plex-mono-latin-400-normal.woff2',
  'fonts/ibm-plex-mono-latin-500-normal.woff2',
  'fonts/ibm-plex-mono-latin-600-normal.woff2',
  'fonts/fonts.css'
];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); })
    .then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) {
      return k.indexOf('ironledger-') === 0 && k !== CACHE;
    }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('fetch', function (e) {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  const isPage = req.mode === 'navigate';
  const key = isPage ? new URL('index.html', self.registration.scope).href : req;

  e.respondWith(caches.open(CACHE).then(function (c) {
    return c.match(key, { ignoreSearch: true }).then(function (hit) {
      const fresh = fetch(req).then(function (res) {
        if (res && res.ok) c.put(key, res.clone());
        return res;
      }).catch(function () { return null; });
      if (hit) { e.waitUntil(fresh); return hit; }
      return fresh.then(function (res) {
        return res || new Response('Offline and not cached yet', { status: 503 });
      });
    });
  }));
});
