/* Neon Knuckle — site.js : language toggle, reveal-on-scroll, screenshot lightbox */
(function () {
  var root = document.documentElement;

  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  /* ----- language (EN default, KO toggle) ----- */
  function setLang(l) {
    root.lang = l;
    store('nk-lang', l);
    document.querySelectorAll('[data-lang-btn]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-lang-btn') === l));
    });
    var t = document.querySelector('title');
    if (t && t.getAttribute('data-' + l)) document.title = t.getAttribute('data-' + l);
    var m = document.querySelector('meta[name="description"]');
    if (m && m.getAttribute('data-' + l)) m.setAttribute('content', m.getAttribute('data-' + l));
  }
  setLang(root.lang === 'ko' ? 'ko' : 'en');

  document.addEventListener('click', function (e) {
    var lb = e.target.closest('[data-lang-btn]');
    if (lb) { setLang(lb.getAttribute('data-lang-btn')); return; }
    var g = e.target.closest('.gallery button');
    if (g) openLightbox(g.querySelector('img'));
  });

  /* ----- reveal on scroll ----- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  /* ----- lightbox ----- */
  var dlg;
  function openLightbox(img) {
    if (!img) return;
    if (!dlg) {
      dlg = document.createElement('dialog');
      dlg.className = 'lightbox';
      dlg.innerHTML = '<img alt="">';
      dlg.addEventListener('click', function () { dlg.close(); });
      document.body.appendChild(dlg);
    }
    var i = dlg.querySelector('img');
    i.src = img.getAttribute('data-full') || img.src;
    i.alt = img.alt || '';
    if (typeof dlg.showModal === 'function') dlg.showModal();
  }

  /* ----- footer year ----- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
