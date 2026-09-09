/* GHOST RIDER universe — site runtime (no dependencies) */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ------------------------------------------------------------------
     1. Background video — persistent, muted, resumes across page loads
     ------------------------------------------------------------------ */
  var video = $('#bgVideo');
  var wrap = $('.bg-video');
  var gate = $('#playGate');

  function pickSource() {
    if (!video) return;
    var conn = navigator.connection || {};
    var small = window.innerWidth < 720;
    var frugal = conn.saveData || /2g/.test(conn.effectiveType || '');
    var src = (small || frugal) ? video.dataset.srcSd : video.dataset.srcHd;
    /* Browsers without H.264 (some open-source builds) fall back to the VP9 WebM */
    if (!video.canPlayType('video/mp4; codecs="avc1.640028"') && video.canPlayType('video/webm; codecs="vp9"') && video.dataset.srcWebm) {
      src = video.dataset.srcWebm;
    }
    if (video.getAttribute('src') !== src) video.setAttribute('src', src);
  }

  function tryPlay() {
    if (!video) return;
    var p = video.play();
    if (p && p.then) {
      p.then(function () {
        wrap.classList.add('is-playing');
        gate.classList.remove('is-visible');
      }).catch(function (err) {
        /* Autoplay blocked: show a one-tap igniter, keep poster visible.
           A decode/format failure is not the user's problem, so stay quiet. */
        if (!err || err.name !== 'NotSupportedError') gate.classList.add('is-visible');
      });
    }
  }

  if (video) {
    pickSource();
    var t = parseFloat(sessionStorage.getItem('gr-video-t') || '0');
    if (t > 0 && t < 28) {
      video.addEventListener('loadedmetadata', function () { try { video.currentTime = t; } catch (e) {} }, { once: true });
    }
    video.addEventListener('playing', function () { wrap.classList.add('is-playing'); });
    tryPlay();
    gate.addEventListener('click', tryPlay);
    ['click', 'touchstart', 'keydown'].forEach(function (ev) {
      document.addEventListener(ev, function once() {
        if (video.paused) tryPlay();
        document.removeEventListener(ev, once);
      }, { passive: true });
    });
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) video.pause(); else tryPlay();
    });
    setInterval(function () {
      if (!video.paused) sessionStorage.setItem('gr-video-t', String(video.currentTime));
    }, 500);
    window.addEventListener('pagehide', function () { sessionStorage.setItem('gr-video-t', String(video.currentTime)); });
  }

  function applyVideoPosition() {
    var pos = document.body.getAttribute('data-vid-pos');
    document.documentElement.style.setProperty('--vid-pos', pos || '50% 50%');
  }

  /* ------------------------------------------------------------------
     2. Embers — a light canvas of rising sparks
     ------------------------------------------------------------------ */
  (function embers() {
    var c = $('#embers');
    if (!c || reduceMotion) { if (c) c.remove(); return; }
    var ctx = c.getContext('2d');
    var W, H, parts = [], N = window.innerWidth < 720 ? 28 : 60, raf;
    function size() { W = c.width = window.innerWidth; H = c.height = window.innerHeight; }
    function spawn(p) {
      p.x = Math.random() * W; p.y = H + Math.random() * 40;
      p.r = 0.6 + Math.random() * 1.9; p.vy = 0.25 + Math.random() * 0.8; p.vx = (Math.random() - 0.5) * 0.35;
      p.life = 0; p.max = 260 + Math.random() * 260; p.hue = 18 + Math.random() * 22; p.w = Math.random() * 6.28;
      return p;
    }
    size(); for (var i = 0; i < N; i++) { var p = spawn({}); p.y = Math.random() * H; p.life = Math.random() * p.max; parts.push(p); }
    function frame() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        p.life++; p.w += 0.02;
        p.x += p.vx + Math.sin(p.w) * 0.3; p.y -= p.vy;
        var a = Math.sin((p.life / p.max) * Math.PI);
        if (p.life > p.max || p.y < -10) spawn(p);
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.28);
        ctx.fillStyle = 'hsla(' + p.hue + ',100%,62%,' + (a * 0.85) + ')';
        ctx.shadowColor = 'rgba(255,120,20,.9)'; ctx.shadowBlur = 8;
        ctx.fill();
      }
      raf = requestAnimationFrame(frame);
    }
    frame();
    window.addEventListener('resize', size);
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) cancelAnimationFrame(raf); else frame();
    });
  })();

  /* ------------------------------------------------------------------
     3. Header state, mobile drawer, dropdowns
     ------------------------------------------------------------------ */
  var header = $('.site-header');
  var toTop = $('#toTop');
  function onScroll() {
    var y = window.scrollY || 0;
    header.classList.toggle('is-scrolled', y > 24);
    toTop.classList.toggle('is-visible', y > 900);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  toTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }); });

  var drawer = $('#navMobile');
  function openDrawer() { drawer.classList.add('is-open'); document.body.classList.add('nav-open'); $('#navClose').focus(); }
  function closeDrawer() { drawer.classList.remove('is-open'); document.body.classList.remove('nav-open'); }
  $('#burger').addEventListener('click', openDrawer);
  $('#navClose').addEventListener('click', closeDrawer);

  $$('.nav-desktop > li > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentNode, open = li.classList.contains('is-open');
      $$('.nav-desktop > li.is-open').forEach(function (x) { x.classList.remove('is-open'); });
      if (!open) li.classList.add('is-open');
      b.setAttribute('aria-expanded', String(!open));
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-desktop')) $$('.nav-desktop > li.is-open').forEach(function (x) { x.classList.remove('is-open'); });
  });

  function markActive() {
    var path = location.pathname.split('/').pop() || 'index.html';
    $$('.nav-desktop li, .nav-desktop a, .nav-mobile a').forEach(function (n) { n.classList.remove('is-active'); n.removeAttribute('aria-current'); });
    $$('a[href]').forEach(function (a) {
      if (!a.closest('.site-header, .nav-mobile')) return;
      var href = a.getAttribute('href').split('#')[0];
      if (href === path) {
        a.classList.add('is-active'); a.setAttribute('aria-current', 'page');
        var top = a.closest('.nav-desktop > li'); if (top) top.classList.add('is-active');
      }
    });
  }
  markActive();

  /* ------------------------------------------------------------------
     4. Search — static JSON index, fuzzy-ish scoring
     ------------------------------------------------------------------ */
  var overlay = $('#searchOverlay'), input = $('#searchInput'), results = $('#searchResults');
  var index = null;
  function loadIndex() {
    if (index) return Promise.resolve(index);
    return fetch('search-index.json').then(function (r) { return r.json(); }).then(function (j) { index = j; return j; });
  }
  function openSearch() { overlay.classList.add('is-open'); document.body.classList.add('nav-open'); input.value = ''; results.innerHTML = ''; setTimeout(function () { input.focus(); }, 30); loadIndex(); }
  function closeSearch() { overlay.classList.remove('is-open'); document.body.classList.remove('nav-open'); }
  $$('[data-open-search]').forEach(function (b) { b.addEventListener('click', function () { closeDrawer(); openSearch(); }); });
  $('#searchClose').addEventListener('click', closeSearch);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeSearch(); closeDrawer(); closeLightbox(); }
    if ((e.key === '/' || (e.key === 'k' && (e.metaKey || e.ctrlKey))) && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); }
  });
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function search(q) {
    q = q.trim().toLowerCase();
    if (!q || !index) { results.innerHTML = ''; return; }
    var terms = q.split(/\s+/);
    var scored = index.map(function (p) {
      var hay = (p.title + ' ' + p.keywords + ' ' + p.text).toLowerCase();
      var s = 0;
      terms.forEach(function (t) {
        if (p.title.toLowerCase().indexOf(t) > -1) s += 12;
        if (p.keywords.toLowerCase().indexOf(t) > -1) s += 6;
        var n = hay.split(t).length - 1; s += Math.min(n, 8);
      });
      return { p: p, s: s };
    }).filter(function (x) { return x.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 12);
    if (!scored.length) { results.innerHTML = '<li><p class="search-hint">Nothing in the ledger matches that. Try a name, a place, or a power.</p></li>'; return; }
    results.innerHTML = scored.map(function (x) {
      var p = x.p, i = p.text.toLowerCase().indexOf(terms[0]);
      var snip = i > -1 ? p.text.slice(Math.max(0, i - 70), i + 110) : p.text.slice(0, 160);
      snip = esc(snip);
      terms.forEach(function (t) { snip = snip.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); });
      return '<li><a href="' + p.url + '"><span class="sr-crumb">' + esc(p.section) + '</span><span class="sr-title">' + esc(p.title) + '</span><span class="sr-snip">…' + snip + '…</span></a></li>';
    }).join('');
  }
  var st; input.addEventListener('input', function () { clearTimeout(st); st = setTimeout(function () { search(input.value); }, 60); });
  results.addEventListener('click', function (e) { if (e.target.closest('a')) closeSearch(); });

  /* ------------------------------------------------------------------
     5. Scroll reveal (one subtle rise per block)
     ------------------------------------------------------------------ */
  var io;
  function bindReveal() {
    if (reduceMotion) { $$('.reveal').forEach(function (n) { n.classList.add('is-in'); }); return; }
    if (!io) io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    $$('.reveal:not(.is-in)').forEach(function (n) { io.observe(n); });
  }

  /* ------------------------------------------------------------------
     6. Gallery lightbox + theater chapters (page-scoped widgets)
     ------------------------------------------------------------------ */
  var lb = $('#lightbox'), lbImg = $('#lightboxImg'), lbCap = $('#lightboxCap'), lbItems = [], lbIdx = 0;
  function showLb(i) {
    if (!lbItems.length) return;
    lbIdx = (i + lbItems.length) % lbItems.length;
    var f = lbItems[lbIdx], img = f.querySelector('img');
    lbImg.src = img.getAttribute('data-full') || img.src; lbImg.alt = img.alt; lbCap.textContent = f.querySelector('figcaption').textContent;
    lb.classList.add('is-open'); document.body.classList.add('nav-open');
  }
  function closeLightbox() { if (lb) { lb.classList.remove('is-open'); document.body.classList.remove('nav-open'); } }
  if (lb) {
    $('#lbClose').addEventListener('click', closeLightbox);
    $('#lbPrev').addEventListener('click', function () { showLb(lbIdx - 1); });
    $('#lbNext').addEventListener('click', function () { showLb(lbIdx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLightbox(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'ArrowRight') showLb(lbIdx + 1); if (e.key === 'ArrowLeft') showLb(lbIdx - 1);
    });
  }
  function bindWidgets() {
    lbItems = $$('.gallery figure');
    lbItems.forEach(function (f, i) { f.addEventListener('click', function () { showLb(i); }); f.setAttribute('tabindex', '0'); f.addEventListener('keydown', function (e) { if (e.key === 'Enter') showLb(i); }); });

    var tv = $('#theaterVideo');
    if (tv) {
      var chapters = $$('.chapters button');
      chapters.forEach(function (b) {
        b.addEventListener('click', function () {
          tv.currentTime = parseFloat(b.dataset.t); tv.play();
          chapters.forEach(function (x) { x.classList.remove('is-active'); }); b.classList.add('is-active');
        });
      });
      tv.addEventListener('timeupdate', function () {
        var cur = tv.currentTime;
        chapters.forEach(function (b) { b.classList.toggle('is-active', cur >= parseFloat(b.dataset.t) && cur < parseFloat(b.dataset.end)); });
      });
      var fs = $('#theaterFs'); if (fs) fs.addEventListener('click', function () { (tv.requestFullscreen || tv.webkitEnterFullscreen || function () {}).call(tv); });
      var mute = $('#theaterMute'); if (mute) mute.addEventListener('click', function () { tv.muted = !tv.muted; mute.textContent = tv.muted ? 'Unmute' : 'Mute'; });
    }
    var yr = $('#year'); if (yr) yr.textContent = new Date().getFullYear();
  }

  /* ------------------------------------------------------------------
     7. Soft navigation — swap <main>, keep the video burning
        Every page is a real HTML file, so direct loads and no-JS work.
     ------------------------------------------------------------------ */
  var veil = $('#veil');
  var supportsSoft = !!(window.fetch && window.history && window.history.pushState && window.DOMParser);
  var navigating = false;

  function sameOrigin(a) {
    return a.origin === location.origin && !a.hasAttribute('download') && !a.target && /\.html?$|\/$/.test(a.pathname);
  }
  function swapPage(html, url, push) {
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var newMain = doc.querySelector('main');
    if (!newMain) { location.href = url; return; }
    document.title = doc.title;
    ['description', 'og:title', 'og:description', 'og:url'].forEach(function (name) {
      var sel = name.indexOf(':') > -1 ? 'meta[property="' + name + '"]' : 'meta[name="' + name + '"]';
      var a = $(sel), b = doc.querySelector(sel); if (a && b) a.setAttribute('content', b.getAttribute('content'));
    });
    var canon = $('link[rel="canonical"]'), canon2 = doc.querySelector('link[rel="canonical"]'); if (canon && canon2) canon.href = canon2.href;
    var old = $('main');
    $$('video', old).forEach(function (v) { v.pause(); v.removeAttribute('src'); v.load(); });
    old.replaceWith(newMain);
    document.body.setAttribute('data-vid-pos', doc.body.getAttribute('data-vid-pos') || '50% 50%');
    document.body.className = doc.body.className;
    applyVideoPosition();
    if (push) history.pushState({ url: url }, '', url);
    window.scrollTo(0, 0);
    newMain.classList.add('is-entering');
    markActive(); bindReveal(); bindWidgets();
    var h = url.split('#')[1]; if (h) { var target = document.getElementById(h); if (target) target.scrollIntoView(); }
    if (window.gtag) gtag('event', 'page_view', { page_path: url });
  }
  function go(url, push) {
    if (navigating) return; navigating = true;
    closeDrawer(); closeSearch();
    var main = $('main');
    if (!reduceMotion) { veil.classList.remove('out'); veil.classList.add('in'); main.classList.add('is-leaving'); }
    fetch(url, { headers: { 'X-Requested-With': 'soft-nav' } }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); }).then(function (html) {
      var wait = reduceMotion ? 0 : 380;
      setTimeout(function () {
        swapPage(html, url, push);
        veil.classList.remove('in'); veil.classList.add('out');
        setTimeout(function () { veil.classList.remove('out'); navigating = false; }, 520);
      }, wait);
    }).catch(function () { location.href = url; });
  }
  if (supportsSoft && location.protocol !== 'file:') {
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      if (!sameOrigin(a)) return;
      var url = a.getAttribute('href');
      if (url.charAt(0) === '#') return;
      var abs = new URL(a.href);
      if (abs.pathname === location.pathname && abs.hash) return;
      e.preventDefault();
      go(url, true);
    });
    window.addEventListener('popstate', function () { go(location.pathname.split('/').pop() + location.search + location.hash, false); });
    history.replaceState({ url: location.href }, '', location.href);
  }

  applyVideoPosition();
  bindReveal();
  bindWidgets();
})();
