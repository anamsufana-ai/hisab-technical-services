// Mobile menu
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('#menu');
if (toggle && menu) {
  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
    toggle.textContent = open ? '✕' : '☰';
  });
}

// Footer year
const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear();

// Pre-select the AC system when coming from a package button (?system=vrf)
const system = document.querySelector('#system');
if (system) {
  const wanted = new URLSearchParams(location.search).get('system');
  if (wanted && system.querySelector(`option[value="${wanted}"]`)) system.value = wanted;
}

// Send the request without leaving the page (Netlify Forms), fall back to normal submit
const form = document.querySelector('#booking-form');
if (form) {
  form.addEventListener('submit', async event => {
    event.preventDefault();
    const status = document.querySelector('#form-status');
    const button = form.querySelector('button[type="submit"]');
    button.disabled = true;
    status.textContent = 'Sending…';
    try {
      const res = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form)).toString()
      });
      if (!res.ok) throw new Error(res.status);
      window.location.href = '/thank-you';
    } catch (e) {
      status.textContent = 'Sorry, the request could not be sent. Please call +971 55 828 5372.';
      button.disabled = false;
    }
  });
}

// Project photos: tap to see larger
document.querySelectorAll('.project-block .gallery img').forEach(img => {
  img.addEventListener('click', () => {
    const box = document.createElement('div');
    box.className = 'lightbox';
    box.innerHTML = `<img src="${img.src}" alt=""><p></p>`;
    box.querySelector('img').alt = img.alt;
    box.querySelector('p').textContent = img.alt;
    box.addEventListener('click', () => box.remove());
    document.body.appendChild(box);
  });
});
