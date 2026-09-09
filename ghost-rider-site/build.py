#!/usr/bin/env python3
"""
Ghost Rider universe — static site generator.
Every page is a real HTML file (direct navigation works, no JS required),
sharing one layout, one nav tree, one search index and one sitemap.

    python3 build.py            # writes ./site/*.html, sitemap.xml, search-index.json
"""
import json, re, html, os, importlib, datetime
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"
SITE_URL = "https://ghostrider.example"          # replace with the deployed origin
SITE_NAME = "Ghost Rider — Spirit of Vengeance"

# --------------------------------------------------------------------------
# Navigation tree: section -> pages (slug, label, short description)
# --------------------------------------------------------------------------
NAV = [
    ("The Rider", [
        ("overview", "Ghost Rider Overview", "What the Spirit of Vengeance is, and why the name outlives its hosts."),
        ("origins", "Origins", "From a Western horseman to a stunt rider's deal with the devil."),
        ("powers", "Powers & Abilities", "Hellfire, the Penance Stare, the chain — and the limits that bind them."),
        ("spirit-of-vengeance", "The Spirit of Vengeance", "Zarathos, Noble Kale, and the entities behind the skull."),
        ("transformations", "Transformations", "How each host changes, and what triggers the burn."),
    ]),
    ("Riders", [
        ("johnny-blaze", "Johnny Blaze", "The original stunt rider, bound to Zarathos since 1972."),
        ("danny-ketch", "Danny Ketch", "The Brooklyn kid who touched a haunted motorcycle."),
        ("robbie-reyes", "Robbie Reyes", "East L.A., a 1969 Charger and the ghost of a killer."),
        ("other-riders", "Other Ghost Riders", "Carter Slade, Alejandra Jones, Kushala, Cosmic Ghost Rider and more."),
        ("characters", "Characters", "Allies, loved ones and the people who stand near the fire."),
        ("relationships", "Relationships", "Family, partners, rivals and the ties that survive Hell."),
    ]),
    ("Enemies", [
        ("villains", "Villains", "Mephisto, Blackheart, Lilith, Deathwatch and the rest of the ledger."),
        ("hell", "Hell & the Supernatural Realm", "The infernal strata, its lords and the rules of damnation."),
    ]),
    ("Arsenal", [
        ("vehicles", "Ghost Rider Vehicles", "The Hell Cycle, the Hell Charger and rides across the ages."),
        ("weapons", "Weapons & Artifacts", "Chains, hellfire shotguns, medallions and the Darkhold."),
    ]),
    ("Lore", [
        ("comic-history", "Comic Book History", "Fifty-plus years of publication, volume by volume."),
        ("storylines", "Major Storylines", "The arcs that define the Rider."),
        ("timeline", "Timeline", "Key events, in-universe and on the shelf."),
        ("multiverse", "Multiverse", "Ghost Rider 2099, Cosmic Ghost Rider and the alternate Earths."),
        ("lore", "Lore & Mythology", "The mythology of the Spirits, Heaven's design and the King of Hell."),
    ]),
    ("Media", [
        ("movies", "Movies", "The Nicolas Cage films and the 2028 Marvel Studios film."),
        ("comics", "Comics", "Where to start reading, essential runs and collections."),
        ("gallery", "Gallery", "Stills from the ride."),
        ("videos", "Videos", "Watch the ride with chapter markers."),
        ("quotes", "Quotes", "The words that ride with the Spirit."),
        ("trivia", "Trivia", "Facts from five decades of hellfire."),
        ("news", "News & Updates", "The latest on comics, film and the MCU."),
        ("about", "About the Universe", "How this site is built and sourced."),
    ]),
]
FLAT = {slug: (label, desc, section) for section, pages in NAV for slug, label, desc in pages}
FLAT["index"] = ("Home", "Ghost Rider — the complete digital universe of the Spirit of Vengeance.", "Home")
FLAT["404"] = ("Page not found", "Not found", "Site")

# --------------------------------------------------------------------------
# Shared markup
# --------------------------------------------------------------------------
FLAME_SVG = '<svg class="flame" viewBox="0 0 26 30" aria-hidden="true"><defs><linearGradient id="fg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ffe6b0"/><stop offset=".5" stop-color="#ff7a18"/><stop offset="1" stop-color="#b3121b"/></linearGradient></defs><path fill="url(#fg)" d="M13 0c1 5 6 7 6 13 0 2-1 3-2 4 2-4-1-7-3-8 1 4-4 6-4 10 0 2 1 3 2 4-5-1-8-5-8-10C4 7 10 5 13 0z"/><path fill="#fff3d6" opacity=".9" d="M13 16c1 2 3 3 3 6 0 2-1 4-3 4s-3-2-3-4c0-3 2-4 3-6z"/></svg>'

FLAME_SVG_REF = FLAME_SVG.replace('<defs><linearGradient id="fg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ffe6b0"/><stop offset=".5" stop-color="#ff7a18"/><stop offset="1" stop-color="#b3121b"/></linearGradient></defs>', '')

def icon(name):
    return {
        "search": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
        "close": '<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg>',
        "up": '<svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
        "left": '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
        "right": '<svg viewBox="0 0 24 24"><path d="m9 5 7 7-7 7"/></svg>',
        "chev": '<svg class="chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>',
        "play": '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
    }[name]

def nav_desktop():
    out = []
    for section, pages in NAV:
        wide = " wide" if len(pages) > 6 else ""
        items = "".join(f'<li><a href="{s}.html">{l}</a></li>' for s, l, _ in pages)
        out.append(f'<li><button type="button" aria-haspopup="true" aria-expanded="false">{section}{icon("chev")}</button><ul class="menu{wide}">{items}</ul></li>')
    return f'<ul class="nav-desktop">{"".join(out)}</ul>'

def nav_mobile():
    out = []
    for section, pages in NAV:
        items = "".join(f'<li><a href="{s}.html">{l}</a></li>' for s, l, _ in pages)
        out.append(f'<h3>{section}</h3><ul>{items}</ul>')
    return "".join(out)

def footer():
    cols = "".join(
        f'<div><h4>{section}</h4><ul>' + "".join(f'<li><a href="{s}.html">{l}</a></li>' for s, l, _ in pages) + "</ul></div>"
        for section, pages in NAV[:5]
    )
    media = NAV[5]
    media_col = f'<div><h4>{media[0]}</h4><ul>' + "".join(f'<li><a href="{s}.html">{l}</a></li>' for s, l, _ in media[1]) + "</ul></div>"
    return f'''
<footer class="site-footer">
  <div class="foot-grid">
    <div class="foot-brand">
      <a class="brand" href="index.html">{FLAME_SVG_REF}<span class="brand-word">GHOST RIDER<small>SPIRIT OF VENGEANCE</small></span></a>
      <p>A reference universe for the Spirits of Vengeance: hosts, enemies, machines, storylines and the road from 1972 to the 2028 film.</p>
      <p><a href="index.html">Home</a> · <a href="about.html">About</a> · <a href="news.html">News</a></p>
    </div>
    {cols}
    {media_col}
  </div>
  <div class="foot-legal">
    <span>Ghost Rider and related characters are trademarks of Marvel Characters, Inc. This is an unofficial reference and fan site.</span>
    <span>&copy; <span id="year">{datetime.date.today().year}</span> Ghost Rider Universe reference project</span>
  </div>
</footer>'''

def crumbs(slug):
    if slug in ("index", "404"):
        return ""
    label, _, section = FLAT[slug]
    return f'<ol class="crumbs" aria-label="Breadcrumb"><li><a href="index.html">Home</a></li><li>{section}</li><li aria-current="page">{label}</li></ol>'

def related(slugs):
    items = "".join(f'<li><a href="{s}.html">{FLAT[s][0]}</a></li>' for s in slugs)
    return f'<section class="band related"><h2>Keep riding</h2><ul>{items}</ul></section>'

def layout(slug, title, desc, body, keywords="", vid_pos="50% 50%", body_class="", jsonld=None):
    url = f"{SITE_URL}/{'' if slug=='index' else slug + '.html'}"
    ld = jsonld or {
        "@context": "https://schema.org",
        "@type": "WebPage" if slug != "index" else "WebSite",
        "name": title, "description": desc, "url": url,
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": SITE_URL + "/"},
    }
    if slug not in ("index", "404"):
        label, _, section = FLAT[slug]
        ld["breadcrumb"] = {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": section},
            {"@type": "ListItem", "position": 3, "name": label, "item": url}]}
    full_title = title if slug == "index" else f"{title} — {SITE_NAME}"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="keywords" content="{html.escape('Ghost Rider, Spirit of Vengeance, Johnny Blaze, Danny Ketch, Robbie Reyes, Marvel, ' + keywords)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0a0908">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{html.escape(SITE_NAME)}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/img/poster.jpg">
<meta property="og:image:width" content="1280"><meta property="og:image:height" content="720">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(full_title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{SITE_URL}/assets/img/poster.jpg">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/BigShouldersDisplay.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/Barlow-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css">
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body data-vid-pos="{vid_pos}" class="{body_class}">
<a class="skip" href="#main">Skip to content</a>

<div class="bg-video" aria-hidden="true">
  <img class="video-poster" src="assets/img/poster.jpg" alt="" width="1280" height="720" fetchpriority="high">
  <video id="bgVideo" autoplay muted loop playsinline preload="auto" poster="assets/img/poster.jpg"
         data-src-hd="assets/video/ghost-rider-bg.mp4" data-src-sd="assets/video/ghost-rider-bg-sd.mp4" data-src-webm="assets/video/ghost-rider-bg.webm"
         src="assets/video/ghost-rider-bg.mp4"></video>
</div>
<canvas id="embers" aria-hidden="true"></canvas>
<button id="playGate" class="play-gate" type="button" aria-label="Play background video">{icon("play")}<span>Ignite the ride</span></button>

<header class="site-header">
  <a class="brand" href="index.html" aria-label="Ghost Rider home">{FLAME_SVG}<span class="brand-word">GHOST RIDER<small>SPIRIT OF VENGEANCE</small></span></a>
  <nav aria-label="Primary">{nav_desktop()}</nav>
  <div class="nav-actions">
    <button class="icon-btn" type="button" data-open-search aria-label="Search the universe">{icon("search")}</button>
    <button class="icon-btn burger" id="burger" type="button" aria-label="Open menu" aria-controls="navMobile"><span></span><span></span><span></span></button>
  </div>
</header>

<nav class="nav-mobile" id="navMobile" aria-label="Mobile">
  <button class="icon-btn close" id="navClose" type="button" aria-label="Close menu">{icon("close")}</button>
  <a class="brand" href="index.html">{FLAME_SVG_REF}<span class="brand-word">GHOST RIDER<small>SPIRIT OF VENGEANCE</small></span></a>
  <h3>Search</h3><p><button class="btn ghost" type="button" data-open-search>{icon("search")} Search the universe</button></p>
  {nav_mobile()}
</nav>

<div class="search-overlay" id="searchOverlay" role="dialog" aria-modal="true" aria-label="Search">
  <button class="icon-btn close" id="searchClose" type="button" aria-label="Close search">{icon("close")}</button>
  <div class="search-box">
    <label class="visually-hidden" for="searchInput">Search the Ghost Rider universe</label>
    <input id="searchInput" type="search" placeholder="Search riders, villains, storylines…" autocomplete="off">
    <p class="search-hint">Press / anywhere to open search. Esc to close.</p>
    <ul class="search-results" id="searchResults"></ul>
  </div>
</div>

<main id="main" class="page">
{body}
</main>

{footer()}

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="icon-btn close" id="lbClose" type="button" aria-label="Close">{icon("close")}</button>
  <button class="icon-btn prev" id="lbPrev" type="button" aria-label="Previous">{icon("left")}</button>
  <img id="lightboxImg" alt="">
  <button class="icon-btn next" id="lbNext" type="button" aria-label="Next">{icon("right")}</button>
  <p class="cap" id="lightboxCap"></p>
</div>
<button class="icon-btn to-top" id="toTop" type="button" aria-label="Back to top">{icon("up")}</button>
<div class="veil" id="veil" aria-hidden="true"></div>
<script src="assets/js/main.js" defer></script>
</body>
</html>'''

# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def strip_text(markup):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", markup, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()

def main():
    OUT.mkdir(exist_ok=True)
    pages_dir = ROOT / "pages"
    index, urls = [], []
    for f in sorted(pages_dir.glob("*.py")):
        if f.name.startswith("_"):
            continue
        mod = importlib.import_module(f"pages.{f.stem}")
        page = mod.page()
        slug = page["slug"]
        html_out = layout(slug, page["title"], page["desc"], page["body"],
                          keywords=page.get("keywords", ""), vid_pos=page.get("vid_pos", "50% 50%"),
                          body_class=page.get("body_class", ""), jsonld=page.get("jsonld"))
        (OUT / f"{slug}.html").write_text(html_out, encoding="utf-8")
        label, _, section = FLAT.get(slug, (page["title"], "", "Site"))
        if slug == "404":
            continue
        index.append({"url": f"{slug}.html", "title": page["title"], "section": section,
                      "keywords": page.get("keywords", ""), "text": strip_text(page["body"])[:6000]})
        urls.append(slug)
        print(f"  built {slug}.html")

    (OUT / "search-index.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    today = datetime.date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for s in urls:
        loc = SITE_URL + "/" + ("" if s == "index" else s + ".html")
        pr = "1.0" if s == "index" else "0.8"
        sm.append(f"<url><loc>{loc}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    (OUT / "site.webmanifest").write_text(json.dumps({
        "name": SITE_NAME, "short_name": "Ghost Rider", "start_url": "index.html", "display": "standalone",
        "background_color": "#0a0908", "theme_color": "#0a0908",
        "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}), encoding="utf-8")
    print(f"done — {len(urls)} pages")

if __name__ == "__main__":
    main()
