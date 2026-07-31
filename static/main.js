/* =============================================
   CODEFY STUDIO — main.js
   ============================================= */

/* --- Pricing Category Filter --- */
function filterCategory(cat, btn) {
  const buttons = document.querySelectorAll('.pricing-tab-btn');
  buttons.forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  const blocks = document.querySelectorAll('.cat-block');
  blocks.forEach(block => {
    if (cat === 'all' || block.getAttribute('data-category') === cat) {
      block.classList.remove('hidden');
    } else {
      block.classList.add('hidden');
    }
  });
}

/* --- Portfolio Toggle --- */
function toggleProjects() {
  const hiddenProjects = document.querySelectorAll('.hidden-project');
  const btn = document.getElementById('toggle-projects-btn');
  let isExpanded = false;

  hiddenProjects.forEach(card => {
    if (card.style.display === 'none' || card.style.display === '') {
      card.style.display = 'block';
      isExpanded = true;
    } else {
      card.style.display = 'none';
    }
  });

  if (isExpanded) {
    btn.innerHTML = "Qisqartirish ↑";
  } else {
    const total = document.querySelectorAll('.hidden-project').length + 3;
    btn.innerHTML = `Hammasini ko'rish (${total}) ↓`;
  }
}

/* --- Mobile Hamburger Menu --- */
document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.getElementById('hamburger-btn');
  const mobileNav = document.getElementById('mobile-nav');

  if (!hamburger || !mobileNav) return;

  hamburger.addEventListener('click', function () {
    hamburger.classList.toggle('open');
    mobileNav.classList.toggle('open');
    document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
  });

  /* Close menu on link click */
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function () {
      hamburger.classList.remove('open');
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  /* Close menu on outside click */
  document.addEventListener('click', function (e) {
    if (!hamburger.contains(e.target) && !mobileNav.contains(e.target)) {
      hamburger.classList.remove('open');
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
});
