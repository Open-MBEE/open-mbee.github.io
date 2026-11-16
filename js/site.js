(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }
  var subs = document.querySelectorAll('.has-sub');
  subs.forEach(function (li) {
    var btn = li.querySelector('button');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var willOpen = !li.classList.contains('open');
      subs.forEach(function (o) { o.classList.remove('open'); o.querySelector('button').setAttribute('aria-expanded', 'false'); });
      if (willOpen) { li.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    });
  });
  document.addEventListener('click', function () {
    subs.forEach(function (o) { o.classList.remove('open'); o.querySelector('button').setAttribute('aria-expanded', 'false'); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      subs.forEach(function (o) { o.classList.remove('open'); o.querySelector('button').setAttribute('aria-expanded', 'false'); });
      if (nav) nav.classList.remove('open');
    }
  });

  // Click-to-copy buttons (brand colour values)
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var label = btn.textContent;
    btn.addEventListener('click', function () {
      var value = btn.getAttribute('data-copy');
      function done(ok) {
        btn.textContent = ok ? 'Copied ' + value : 'Copy failed';
        btn.classList.toggle('done', ok);
        setTimeout(function () { btn.textContent = label; btn.classList.remove('done'); }, 1600);
      }
      try {
        navigator.clipboard.writeText(value).then(function () { done(true); }, function () { done(false); });
      } catch (e) { done(false); }
    });
  });
})();
