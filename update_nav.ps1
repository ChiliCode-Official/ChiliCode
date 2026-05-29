$files = @(
    "index.html",
    "nosotros.html",
    "artesanias.html",
    "experiencia.html",
    "plan-landing.html",
    "mantenimientos.html",
    "como-funciona.html"
)

$menuOverlayHTML = @"

    <!-- Fullscreen Menu Overlay -->
    <div class="menu-overlay">
        <ul class="menu-links">
            <li><a href="experiencia.html">Experiencia</a></li>
            <li><a href="plan-landing.html">Landing Pages</a></li>
            <li><a href="como-funciona.html">Chili Loyalty (Nuevo)</a></li>
            <li><a href="mantenimientos.html">Mantenimiento</a></li>
            <li><a href="nosotros.html#ceo-section">El Fundador</a></li>
            <li><a href="index.html#proyectos">Proyectos</a></li>
        </ul>
    </div>
"@

function Get-ConsistentNavLinks($activePage) {
    $activeClassIndex = ""
    $activeClassNosotros = ""
    $activeClassArtesanias = ""
    if ($activePage -eq "index") { $activeClassIndex = ' class="active"' }
    if ($activePage -eq "nosotros") { $activeClassNosotros = ' class="active"' }
    if ($activePage -eq "artesanias") { $activeClassArtesanias = ' class="active"' }

    $artesaniasText = "Artesan" + [char]0xED + "as"

    $links = @"
<ul class="nav-links">
                <li><a href="index.html"$activeClassIndex>
                    <svg viewBox="0 0 24 24" class="nav-icon-std"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <img src="https://i.imgur.com/QTzmlBC.png" alt="Inicio" class="nav-logo-mobile">
                    <span class="nav-text">Inicio</span>
                </a></li>
                <li><a href="nosotros.html"$activeClassNosotros><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>Estudio</a></li>
                <li><a href="artesanias.html"$activeClassArtesanias><svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path></svg>$artesaniasText</a></li>
            </ul>
            <a href="https://wa.me/525574123521?text=Hola!%20Me%20interesa%20saber%20m%C3%A1s%20sobre%20tus%20servicios%20en%20ChilliCode." class="nav-cta" target="_blank">Hablemos</a>
            <button class="hamburger-btn" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>
`$menuOverlayHTML
"@
    return $links
}

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = [System.IO.File]::ReadAllText((Resolve-Path $file), [System.Text.Encoding]::UTF8)
        $activePage = $file.Replace(".html", "")
        
        $pattern = "(?s)<ul class=""nav-links"">.*?<\/nav>\s*(?:<!-- Fullscreen Menu Overlay -->\s*<div class=""menu-overlay"">.*?<\/div>)?"
        $newNav = Get-ConsistentNavLinks $activePage
        
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, $newNav)
        [System.IO.File]::WriteAllText((Resolve-Path $file), $content, (New-Object System.Text.UTF8Encoding($false)))
        Write-Host "Updated $file"
    }
}
