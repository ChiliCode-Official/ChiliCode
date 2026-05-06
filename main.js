/**
 * Bottle Code Agency - Digital Craftsmanship
 * Animation Engine: Fanta-Style Section Transitions
 */

gsap.registerPlugin(ScrollTrigger);

const modelViewer = document.getElementById('skull-model') || document.getElementById('skull-model-static');

function updateOrbit(azimuth, polar, distance) {
    if (!modelViewer) return;
    modelViewer.cameraOrbit = `${azimuth}deg ${polar}deg ${distance}m`;
}

function initAnimations() {
    if (!modelViewer) return;

    // 1. Initial State (Hero)
    const isMobile = window.innerWidth < 768;
    gsap.set(modelViewer, { 
        xPercent: isMobile ? 0 : 30, 
        yPercent: isMobile ? -5 : 0, 
        scale: isMobile ? 0.6 : 1.2, 
        opacity: 0 
    });
    updateOrbit(0, 75, 2);
    
    gsap.to(modelViewer, { opacity: 1, duration: 1.5 });

    // 2. Transition: Hero -> Servicios
    const tl1 = gsap.timeline({
        scrollTrigger: {
            trigger: ".services",
            start: "top 90%",
            end: "top 10%",
            scrub: 1,
        }
    });

    tl1.to(modelViewer, {
        xPercent: -35,
        scale: 0.7,
        onUpdate: function() {
            const p = this.progress();
            const azimuth = gsap.utils.interpolate(0, 180, p);
            const polar = gsap.utils.interpolate(75, 90, p);
            const dist = gsap.utils.interpolate(2, 2.8, p);
            updateOrbit(azimuth, polar, dist);
        }
    });

    // 3. Transition: Servicios -> Proyectos
    const tl2 = gsap.timeline({
        scrollTrigger: {
            trigger: ".projects",
            start: "top bottom",
            end: "top 20%",
            scrub: 1,
        }
    });

    tl2.to(modelViewer, {
        xPercent: 100,
        yPercent: -50,
        scale: 0.2,
        opacity: 0,
        duration: 1,
        ease: "power2.inOut",
        onUpdate: function() {
            const p = this.progress();
            const azimuth = gsap.utils.interpolate(180, 360, p);
            const polar = gsap.utils.interpolate(90, 45, p);
            const dist = gsap.utils.interpolate(2.8, 6, p);
            updateOrbit(azimuth, polar, dist);
        }
    });

    // 4. Transition: Proyectos -> Contacto
    // The skull remains invisible during the contact section
    const tl3 = gsap.timeline({
        scrollTrigger: {
            trigger: ".cta",
            start: "top bottom",
            end: "top 50%",
            scrub: 1,
        }
    });

    tl3.to(modelViewer, {
        opacity: 0,
    });
}

// Navbar Scroll Effect
function initNavbar() {
    const nav = document.querySelector('.pill-nav');
    if (!nav) return;
    ScrollTrigger.create({
        start: "top -50",
        onUpdate: (self) => {
            if (self.direction === 1) {
                gsap.to(nav, { y: -20, opacity: 0.8, duration: 0.3 });
            } else {
                gsap.to(nav, { y: 0, opacity: 1, duration: 0.3 });
            }
        }
    });
}

// Reveal animations for text
function initReveals() {
    const revealElements = document.querySelectorAll('.content-wrapper, .service-card, .project-item, .section-header');
    
    revealElements.forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 95%",
                toggleActions: "play none none reverse",
                fastScrollEnd: true,
            },
            y: 30,
            opacity: 0,
            duration: 0.8,
            ease: "expo.out",
            lazy: true
        });
    });
}

function initCarousel() {
    const cards = Array.from(document.querySelectorAll('.carousel-card'));
    const dots  = Array.from(document.querySelectorAll('.dot'));
    if (cards.length === 0) return;

    let currentIndex = 0;
    let intervalId;
    const totalCards = cards.length;

    // Entrance animation: fan cards in from below with satisfying stagger
    gsap.from(cards, {
        scrollTrigger: {
            trigger: '#fanCarousel',
            start: 'top 85%',
            once: true,
        },
        y: 140,
        opacity: 0,
        scale: 0.75,
        rotation: 0,
        duration: 1.1,
        ease: 'back.out(1.8)',
        stagger: { amount: 0.5, from: 'center' }
    });

    function updateDots(index) {
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
    }

    function updateCarousel(newIndex) {
        if (newIndex < 0) newIndex = totalCards - 1;
        if (newIndex >= totalCards) newIndex = 0;

        currentIndex = newIndex;

        cards.forEach((card, i) => {
            card.classList.remove('active', 'prev', 'next', 'far-prev', 'far-next');

            if (i === currentIndex) {
                card.classList.add('active');
            } else if (i === (currentIndex - 1 + totalCards) % totalCards) {
                card.classList.add('prev');
            } else if (i === (currentIndex + 1) % totalCards) {
                card.classList.add('next');
            } else if (i === (currentIndex - 2 + totalCards) % totalCards) {
                card.classList.add('far-prev');
            } else {
                card.classList.add('far-next');
            }
        });

        updateDots(currentIndex);
        resetInterval();
    }

    function resetInterval() {
        clearInterval(intervalId);
        const currentCard = cards[currentIndex];
        const isCeo = currentCard.classList.contains('ceo-card');
        // CEO card lingers longer so viewers notice the glow + badge
        const duration = isCeo ? 5500 : 2800;

        intervalId = setInterval(() => {
            updateCarousel(currentIndex + 1);
        }, duration);
    }

    // Click on cards
    cards.forEach((card, i) => {
        card.addEventListener('click', () => updateCarousel(i));
    });

    // Click on dots
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => updateCarousel(i));
    });

    // Arrows
    const leftArrow = document.querySelector('.left-arrow');
    const rightArrow = document.querySelector('.right-arrow');

    if (leftArrow) {
        leftArrow.addEventListener('click', () => updateCarousel(currentIndex - 1));
    }
    if (rightArrow) {
        rightArrow.addEventListener('click', () => updateCarousel(currentIndex + 1));
    }

    updateCarousel(0);
}

window.addEventListener('load', () => {
    initAnimations();
    initNavbar();
    initReveals();
    initCarousel();
});
