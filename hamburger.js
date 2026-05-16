document.addEventListener('DOMContentLoaded', () => {
    const btn = document.querySelector('.hamburger-btn');
    const overlay = document.querySelector('.menu-overlay');
    if (!btn || !overlay) return;

    btn.addEventListener('click', () => {
        btn.classList.toggle('active');
        overlay.classList.toggle('active');
        document.body.style.overflow = overlay.classList.contains('active') ? 'hidden' : '';
    });

    const links = overlay.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            btn.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
});
