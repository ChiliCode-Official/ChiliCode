import os
import re

files = [
    'index.html',
    'nosotros.html',
    'artesanias.html',
    'experiencia.html',
    'plan-landing.html',
    'mantenimientos.html',
    'como-funciona.html',
    'chili-mods.html',
    'partners.html',
    'plan-profesional.html',
    'plan-sitio-web.html',
    'privacidad.html',
    'terminos.html',
    'startups-experience-high.html',
    'express.html'
]

menuOverlayHTML = """
    <!-- Fullscreen Menu Overlay -->
    <div class="menu-overlay">
        <ul class="menu-links">
            <li><a href="experiencia.html">Experiencia<span class="menu-desc">Trayectoria y portafolio de proyectos de autor</span></a></li>
            <li class="has-details">
                <details>
                    <summary>Planes Web<span class="menu-desc">Soluciones a medida para cada negocio</span></summary>
                    <ul class="dropdown-menu">
                        <li><a href="plan-landing.html">Landing Page</a></li>
                        <li><a href="plan-sitio-web.html">ChiliCode Corporativo</a></li>
                        <li><a href="plan-profesional.html">ChiliCode Profesional</a></li>
                    </ul>
                </details>
            </li>
            <li><a href="como-funciona.html">Chili Loyalty<span class="menu-desc">Sistemas de lealtad para retener tus clientes</span></a></li>
            <li><a href="mantenimientos.html">Mantenimiento<span class="menu-desc">Soporte y actualizaciones t&eacute;cnicas de primer nivel</span></a></li>
            <li><a href="chili-mods.html">Chili Mods<span class="menu-desc">M&oacute;dulos avanzados para potenciar tu sitio web</span></a></li>
            <li><a href="index.html#proyectos">Proyectos<span class="menu-desc">Galer&iacute;a de nuestras artesan&iacute;as digitales</span></a></li>
            <li><a href="express.html">Express<span class="menu-desc">P&aacute;ginas web premium listas en 48 horas</span></a></li>
        </ul>
    </div>
"""

def getConsistentNavLinks(activePage):
    active_idx = ' class="active"' if activePage == 'index' else ''
    active_nos = ' class="active"' if activePage == 'nosotros' else ''
    active_art = ' class="active"' if activePage == 'artesanias' else ''
    active_sta = ' class="active"' if activePage == 'startups-experience-high' else ''
    active_exp = ' class="active"' if activePage == 'express' else ''

    return f"""<ul class="nav-links">
                <li><a href="index.html"{active_idx}>
                    <svg viewBox="0 0 24 24" class="nav-icon-std"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <img src="https://i.imgur.com/QTzmlBC.png" alt="Inicio" class="nav-logo-mobile">
                    <span class="nav-text">Inicio</span>
                </a></li>
                <li><a href="nosotros.html"{active_nos}><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>Estudio</a></li>
                <li><a href="artesanias.html"{active_art}><svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path></svg>Artesan&iacute;as</a></li>
                <li><a href="startups-experience-high.html"{active_sta}><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.5 16.5c-1.5 1.5-2 4-2 4s2.5-.5 4-2l7.5-7.5-5-5L4.5 16.5z"></path><path d="M9 15L21 3"></path><polyline points="15 3 21 3 21 9"></polyline></svg>Startups</a></li>
                <li><a href="express.html"{active_exp}><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>Express</a></li>
            </ul>
            <a href="https://wa.me/525574123521?text=Hola!%20Me%20interesa%20saber%20m%C3%A1s%20sobre%20tus%20servicios%20en%20ChilliCode." class="nav-cta" target="_blank">Hablemos</a>
            <button class="hamburger-btn" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>
{menuOverlayHTML}"""

for file in files:
    filePath = file
    if not os.path.exists(filePath):
        print(f"File not found: {file}")
        continue
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read()

    activePage = file.replace('.html', '')
    navRegex = re.compile(r'<ul class="nav-links">[\s\S]*?<\/nav>\s*(?:<!-- Fullscreen Menu Overlay -->\s*<div class="menu-overlay">[\s\S]*?<\/div>|\$menuOverlayHTML(?:<!--.*?-->)?)?')
    
    if navRegex.search(content):
        content = navRegex.sub(getConsistentNavLinks(activePage), content)
        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Could not find nav-links in {file}")
