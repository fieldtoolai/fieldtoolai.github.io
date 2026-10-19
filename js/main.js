// Mobile nav toggle
const t = document.querySelector('.nav-toggle');
const links = document.getElementById('nav-links');
if (t && links) t.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  t.setAttribute('aria-expanded', open);
});
// Newsletter placeholder: no backend yet, nothing is stored or sent.
document.querySelectorAll('.newsletter-form').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const input = form.querySelector('input[type=email]');
    const note = form.parentElement.querySelector('.note');
    if (!input.value || !input.checkValidity()) { note.textContent = 'Please enter a valid email address.'; input.focus(); return; }
    note.textContent = "Thanks! Signup isn't live yet, so your email wasn't saved. Check back soon.";
    form.reset();
  });
});
