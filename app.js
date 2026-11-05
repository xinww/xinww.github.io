/* PrismNote 落地页交互 —— 所有内容来自 data.js */
(function () {
  'use strict';

  var SITE = window.SITE || {};
  var $ = function (sel) { return document.querySelector(sel); };
  var $$ = function (sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); };
  var esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  };

  /* ---------- 轻量提示 ---------- */
  var toastTimer;
  function toast(msg) {
    var el = $('#toast');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.classList.remove('show'); }, 2600);
  }

  /* ---------- 全站文案 / 导航 / 页脚 ---------- */
  function applyText() {
    var text = SITE.text || {};
    $$('[data-text]').forEach(function (el) {
      var key = el.getAttribute('data-text');
      if (Object.prototype.hasOwnProperty.call(text, key)) el.textContent = text[key];
    });
    var brand = text.brandName || 'PrismNote';
    document.title = brand + ' | 官方下载与视频教程';
    var y = $('#year'); if (y) y.textContent = new Date().getFullYear();
  }

  function renderNav() {
    var nav = $('#site-nav');
    if (!nav || !SITE.nav) return;
    nav.innerHTML = SITE.nav.map(function (item) {
      return '<a href="' + esc(item.href) + '">' + esc(item.label) + '</a>';
    }).join('');
  }

  /* ---------- 特性条 ---------- */
  function renderFeatures() {
    var box = $('#features');
    if (!box || !SITE.features) return;
    box.innerHTML = SITE.features.map(function (f) {
      return '<p><span class="f-icon" aria-hidden="true">' + esc(f.icon) + '</span>' + esc(f.label) + '</p>';
    }).join('');
  }

  /* ---------- 平台识别 ---------- */
  function detectPlatform() {
    var ua = navigator.userAgent || '';
    var platform = navigator.platform || '';
    if (/Windows/i.test(ua)) return 'windows';
    if (/Linux/i.test(ua) && !/Android/i.test(ua)) return 'linux';
    if (/Mac|iPhone|iPad/i.test(ua) || /Mac/i.test(platform)) return 'mac';
    return 'other';
  }

  /* ---------- 下载面板 ---------- */
  function renderDownloads() {
    var box = $('#download-list');
    if (!box || !SITE.downloads) return;
    var platform = detectPlatform();
    var recommendedSet = false;
    box.innerHTML = SITE.downloads.map(function (d) {
      var isRecommended = !recommendedSet && (
        (platform === 'mac' && d.platform === 'mac') ||
        (platform === 'other' && d.primary)
      );
      if (isRecommended) recommendedSet = true;
      var tag = isRecommended && d.recommendLabel
        ? '<span class="tag">' + esc(d.recommendLabel) + '</span>' : '';
      return '<a class="download-button' + (d.primary ? '' : ' secondary') + '" href="' + esc(d.href) + '"' +
        (d.href === '#download' ? ' data-placeholder="1"' : '') + '>' +
        '<span class="btn-label">' + esc(d.label) + tag + '</span><span aria-hidden="true">↓</span></a>' +
        '<p class="compat">' + esc(d.detail) + '</p>';
    }).join('');
  }

  function renderOtherPlatforms() {
    var box = $('#other-platforms');
    if (!box || !SITE.otherPlatforms) return;
    var platform = detectPlatform();
    box.innerHTML = SITE.otherPlatforms.map(function (p, i) {
      var mine = (platform === 'windows' && i === 0) || (platform === 'linux' && i === 1);
      return '<details class="other-platform"' + (mine ? ' open' : '') + '>' +
        '<summary>' + esc(p.title) + (mine ? ' · 你的平台' : '') + '</summary>' +
        '<a href="' + esc(p.href) + '"' + (p.href === '#download' ? ' data-placeholder="1"' : '') + '>' + esc(p.linkLabel) + '</a>' +
        '<p>' + esc(p.note) + '<a href="' + esc(p.integrityAnchor) + '">文件校验</a></p>' +
        '</details>';
    }).join('');
  }

  /* ---------- 教程：切换 / 播放 / 章节导览 ---------- */
  var activeTutorial = 0;

  function renderTutorialTabs() {
    var box = $('#tutorial-tabs');
    if (!box || !SITE.tutorials) return;
    box.innerHTML = SITE.tutorials.map(function (t, i) {
      return '<button type="button" data-tutorial="' + i + '" aria-pressed="' + (i === activeTutorial) + '">' + esc(t.label) + '</button>';
    }).join('');
    box.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-tutorial]');
      if (!btn) return;
      activeTutorial = Number(btn.dataset.tutorial);
      $$('#tutorial-tabs button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b === btn));
      });
      closePlayer();
      syncTutorial();
    });
  }

  function syncTutorial() {
    var t = (SITE.tutorials || [])[activeTutorial];
    if (!t) return;
    var poster = $('#tutorial-poster');
    if (poster) { poster.src = t.poster; poster.alt = t.label + ' 教程封面'; }
    $('#tutorial-caption').textContent = t.caption;
    $('#tutorial-watch').href = t.poster;
    var note = $('#tutorial-note');
    if (note) note.innerHTML = '<a href="' + esc(t.poster) + '" target="_blank" rel="noopener">' +
      esc(t.label) + ' · ' + esc(t.duration) + ' · 固定观看入口 ↗</a>';
    var playBtn = $('#tutorial-play');
    if (playBtn) playBtn.innerHTML = '<span aria-hidden="true">▶</span> 播放完整教程';
  }

  function closePlayer() {
    var player = $('#tutorial-player');
    if (!player) return;
    player.hidden = true;
    player.innerHTML = '';
    $('#tutorial-start').hidden = false;
  }

  function openPlayer() {
    var t = (SITE.tutorials || [])[activeTutorial];
    var player = $('#tutorial-player');
    if (!t || !player) return;
    var head = '<div class="player-head"><strong>' + esc(t.label) + ' · ' + esc(t.duration) +
      '</strong><button type="button" id="player-close">收起 ✕</button></div>';
    var body;
    if (t.src) {
      body = '<video controls playsinline autoplay poster="' + esc(t.poster) + '">' +
        '<source src="' + esc(t.src) + '" type="video/mp4">你的浏览器不支持视频播放。</video>' + head;
    } else {
      body = head + '<ul class="chapters">' + (t.chapters || []).map(function (c) {
        return '<li><span class="time">' + esc(c.time) + '</span><span class="chapter-title">' + esc(c.title) + '</span></li>';
      }).join('') + '</ul><p class="player-note">演示站点未附带视频文件：在 data.js 的 tutorials[].src 填入 mp4 地址，这里就会直接播放。</p>';
    }
    player.innerHTML = body;
    player.hidden = false;
    $('#tutorial-start').hidden = true;
    var close = $('#player-close');
    if (close) close.addEventListener('click', closePlayer);
    player.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }

  /* ---------- 界面截图画廊 ---------- */
  function renderGallery() {
    var box = $('#gallery-controls');
    if (!box || !SITE.shots) return;
    box.innerHTML = SITE.shots.map(function (s, i) {
      return '<button type="button" data-shot="' + i + '" aria-pressed="' + (i === 0) + '">' + esc(s.label) + '</button>';
    }).join('');
    box.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-shot]');
      if (!btn) return;
      var shot = SITE.shots[Number(btn.dataset.shot)];
      if (!shot) return;
      $$('#gallery-controls button').forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      var img = $('#gallery-image');
      img.src = shot.image;
      img.alt = 'PrismNote ' + shot.label + ' 界面';
      $('#gallery-link').href = shot.image;
      $('#gallery-caption').textContent = shot.caption;
    });
    var first = SITE.shots[0];
    if (first) {
      $('#gallery-image').src = first.image;
      $('#gallery-link').href = first.image;
      $('#gallery-caption').textContent = first.caption;
    }
  }

  /* ---------- FAQ ---------- */
  function checksumRow(c) {
    return '<div class="checksum-row"><span class="cs-label">' + esc(c.label) + '</span>' +
      '<code>' + esc(c.value) + '</code>' +
      '<button type="button" class="copy-btn" data-copy="' + esc(c.value) + '">复制</button></div>';
  }

  function renderFAQ() {
    var box = $('#faq-list');
    if (!box || !SITE.faqs) return;
    box.innerHTML = SITE.faqs.map(function (f) {
      var html = '<details' + (f.id ? ' id="' + esc(f.id) + '"' : '') + '><summary>' + esc(f.title) + '</summary>';
      (f.paragraphs || []).forEach(function (p) { html += '<p>' + esc(p) + '</p>'; });
      (f.checksums || []).forEach(function (c) { html += checksumRow(c); });
      (f.paragraphsAfter || []).forEach(function (p) { html += '<p>' + esc(p) + '</p>'; });
      return html + '</details>';
    }).join('');
  }

  function bindFAQTools() {
    var all = $$('#faq-list details');
    var ex = $('#faq-expand'), co = $('#faq-collapse');
    if (ex) ex.addEventListener('click', function () { all.forEach(function (d) { d.open = true; }); });
    if (co) co.addEventListener('click', function () { all.forEach(function (d) { d.open = false; }); });
  }

  /* ---------- 复制校验值 ---------- */
  function copyText(value) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(value);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = value;
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy') ? resolve() : reject(); }
      catch (err) { reject(err); }
      finally { document.body.removeChild(ta); }
    });
  }

  /* ---------- 导航高亮 ---------- */
  function bindScrollSpy() {
    var links = $$('#site-nav a[href^="#"]');
    if (!links.length) return;
    var ids = links.map(function (a) { return a.getAttribute('href').slice(1); });
    function update() {
      var pos = window.scrollY + 140;
      var current = ids[0];
      ids.forEach(function (id) {
        var el = document.getElementById(id);
        if (el && el.offsetTop <= pos) current = id;
      });
      links.forEach(function (a) {
        a.classList.toggle('active', a.getAttribute('href') === '#' + current);
      });
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  /* ---------- 全局事件 ---------- */
  function bindGlobal() {
    var play = $('#tutorial-play');
    if (play) play.addEventListener('click', openPlayer);

    document.addEventListener('click', function (e) {
      var copy = e.target.closest('[data-copy]');
      if (copy) {
        copyText(copy.getAttribute('data-copy')).then(function () {
          toast('校验值已复制');
          copy.textContent = '已复制';
          setTimeout(function () { copy.textContent = '复制'; }, 1600);
        }).catch(function () { toast('复制失败，请手动选择文本'); });
        return;
      }
      var dl = e.target.closest('a[data-placeholder]');
      if (dl) {
        e.preventDefault();
        toast('演示站点：把 data.js 里的 href 换成真实安装包地址即可下载');
      }
    });
  }

  /* ---------- 启动 ---------- */
  function init() {
    applyText();
    renderNav();
    renderFeatures();
    renderDownloads();
    renderOtherPlatforms();
    renderTutorialTabs();
    syncTutorial();
    renderGallery();
    renderFAQ();
    bindFAQTools();
    bindScrollSpy();
    bindGlobal();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
