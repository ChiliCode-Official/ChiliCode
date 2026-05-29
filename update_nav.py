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
    'plan-sitio-web.html'
]

menuOverlayHTML = """
    <!-- Fullscreen Menu Overlay -->
    <div class="menu-overlay">
        <ul class="menu-links">
            <li><a href="experiencia.html">Experiencia</a></li>
            <li class="has-details">
                <details>
                    <summary>Planes Web</summary>
                    <ul class="dropdown-menu">
                        <li><a href="plan-landing.html">Landing Page</a></li>
                        <li><a href="plan-sitio-web.html">ChiliCode Corporativo</a></li>
                        <li><a href="plan-profesional.html">ChiliCode Profesional</a></li>
                    </ul>
                </details>
            </li>
            <li><a href="como-funciona.html">Chili Loyalty (Nuevo)</a></li>
            <li><a href="mantenimientos.html">Mantenimiento</a></li>
            <li><a href="chili-mods.html">Chili Mods</a></li>
            <li><a href="nosotros.html#ceo-section">El Fundador</a></li>
            <li><a href="index.html#proyectos">Proyectos</a></li>
        </ul>
    </div>
"""

def getConsistentNavLinks(activePage):
    return f"""<ul class="nav-links">
                <li><a href="index.html"{' class="active"' if activePage == 'index' else ''}>
                    <svg viewBox="0 0 24 24" class="nav-icon-std"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <img src="https://i.imgur.com/QTzmlBC.png" alt="Inicio" class="nav-logo-mobile">
                    <span class="nav-text">Inicio</span>
                </a></li>
                <li><a href="nosotros.html"{' class="active"' if activePage == 'nosotros' else ''}><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>Estudio</a></li>
                <li><a href="artesanias.html"{' class="active"' if activePage == 'artesanias' else ''}><svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path></svg>Artesanías</a></li>
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
    # Match from <ul class="nav-links"> to the end of the menu overlay container or $menuOverlayHTML
    navRegex = re.compile(r'<ul class="nav-links">[\s\S]*?<\/nav>\s*(?:<!-- Fullscreen Menu Overlay -->\s*<div class="menu-overlay">[\s\S]*?<\/div>|\$menuOverlayHTML(?:<!--.*?-->)?)?')
    
    if navRegex.search(content):
        content = navRegex.sub(getConsistentNavLinks(activePage), content)
        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Could not find nav-links in {file}")
