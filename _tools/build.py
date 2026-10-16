#!/usr/bin/env python3
"""Generates the Hisab static site pages with one shared header and footer.

Usage: python3 _tools/build.py <site folder>

Photos live in assets/photos/ under fixed names (hero.jpg, pkg-split.jpg, pkg-vrf.jpg,
pkg-ducted.jpg, why.jpg). Replace a file to change the picture; no code change needed.
Optional: team.jpg and uniform-back.jpg switch on the "Our team" section when present.
"""
import json, os, sys

OUT = sys.argv[1]
SITE = "https://hisab-technical-services.netlify.app"
PHONE = "+971 55 828 5372"
TEL = "tel:+971558285372"
WA = "https://wa.me/971558285372?text=Hello%20Hisab%2C%20I%20would%20like%20a%20free%20site%20inspection."
EMAIL = "mss.ca@outlook.com"
IG = "https://instagram.com/hisab_technical_services_llc"

def photo(name):
    return os.path.exists(os.path.join(OUT, "assets", "photos", name))

NAV = [("index.html", "Home"), ("ac-systems.html", "AC Systems"), ("projects.html", "Projects"),
       ("about.html", "About"), ("contact.html", "Contact")]

WA_ICON = '<svg class="wa" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'

ICON = {
 "shield": '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
 "tool": '<svg viewBox="0 0 24 24"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24"><path d="M5 19c0-8 5-13 15-14-1 10-6 15-14 15"/><path d="M5 19l7-7"/></svg>',
 "users": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.5-4 3-6 6.5-6s6 2 6.5 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.5 0 4 1.5 4.5 4.5"/></svg>',
}

def head(title, desc, path, extra=""):
    url = SITE + "/" + ("" if path == "index.html" else path.replace(".html", ""))
    menu = "".join(f'<a href="{h}"' + (' aria-current="page"' if h == path else '') + f'>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1020">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span>Split AC · VRF · Ducted split AC<span class="hide-sm"> · New buildings &amp; villas · Dubai &amp; Sharjah</span></span><span class="top-links"><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="{TEL}">{PHONE}</a></span></div></div>
<header class="header"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="Hisab Technical Services home"><img src="assets/hisab-logo.png" alt="Hisab Technical Services LLC – your trusted partner for HVAC solutions" width="590" height="235"></a>
<button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">☰</button>
<nav class="menu" id="menu" aria-label="Main">{menu}<a class="btn btn-red" href="contact.html#book">Free site inspection</a></nav>
</div></header>
<main id="main">
"""

FOOT = f"""</main>
<footer class="footer"><div class="wrap">
<div class="footer-grid">
<div><img src="assets/hisab-logo.png" alt="Hisab Technical Services LLC" width="590" height="235" loading="lazy"><p>Split AC, VRF and ducted split air conditioning for new buildings, towers and villas in Dubai and Sharjah.</p></div>
<div><h4>AC systems</h4><a href="ac-systems.html#split">Split AC</a><a href="ac-systems.html#vrf">VRF / VRV systems</a><a href="ac-systems.html#ducted">Ducted split AC &amp; ductwork</a></div>
<div><h4>Company</h4><a href="about.html">About us</a><a href="projects.html">Projects</a><a href="contact.html#book">Free site inspection</a></div>
<div><h4>Contact</h4><a href="{TEL}">{PHONE}</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:{EMAIL}">{EMAIL}</a><p>Dubai, United Arab Emirates<br>DED licence no. 1229557</p></div>
</div>
<div class="footer-base"><span>© <span id="year">2026</span> Hisab Technical Services LLC</span><span>Air conditioning installation · VRF · Ducted split · Dubai · Sharjah · UAE</span><span>© 2026 Designed by ALEXIS FZC LLC</span></div>
</div></footer>
<div class="callbar"><a href="{TEL}">Call</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
<script src="site.js"></script>
</body>
</html>
"""

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"

BUSINESS = {
    "@context": "https://schema.org", "@type": "HVACBusiness", "name": "Hisab Technical Services LLC",
    "slogan": "Your trusted partner for HVAC solutions", "url": SITE, "telephone": "+971558285372", "email": EMAIL,
    "image": SITE + "/assets/og-image.jpg", "logo": SITE + "/assets/hisab-logo.png", "foundingDate": "2023-08",
    "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
    "areaServed": [{"@type": "City", "name": "Dubai"}, {"@type": "City", "name": "Sharjah"}, {"@type": "Country", "name": "United Arab Emirates"}],
    "sameAs": [IG],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Air conditioning installation", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Split AC supply and installation for new buildings and villas"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "VRF / VRV air conditioning design, installation and commissioning"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Ducted split AC and ductwork design and installation"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Free site inspection"}}]},
}

FAQ = [
 ("Is the site inspection free?",
  "Yes. Every project is different, so we inspect the site first. The inspection is free, and you receive a written quotation afterwards."),
 ("Which AC system is right for my building or villa?",
  "It depends on the number of rooms, the ceiling space and how the building is used. Split units suit individual rooms and apartments. Ducted split AC hides the indoor unit above a false ceiling and suits villas and open-plan spaces. VRF suits larger villas, towers and buildings with many rooms on one outdoor system. We recommend a system after the site inspection."),
 ("What is the difference between VRF and ducted split AC?",
  "A ducted split system uses one indoor unit that sends cooled air through ducts to several rooms, usually with one thermostat per system. A VRF (variable refrigerant flow, also called VRV) system connects many indoor units to one outdoor unit, so each room can be set to its own temperature."),
 ("Do you work on new construction?",
  "Yes. New installations are our focus: AC and ductwork for new buildings, towers and villas, from design stage through installation, testing and handover."),
 ("Do you offer maintenance?",
  "We focus on new installations. Maintenance is provided for systems we installed, during the warranty period."),
 ("Which areas do you cover?",
  "We are based in Dubai and work across Dubai and Sharjah, with project references in Sharjah, Al Dhaid, Umm Al Quwain and Dubai."),
]

def faq_ld():
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]})

def faq_html():
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

CTA = f"""<section class="section"><div class="wrap"><div class="cta">
<div><h2>Building or finishing<br>a villa or tower?</h2><p>Every project is different. Book a free site inspection and get a written quote for the right AC system.</p></div>
<div class="actions"><a class="btn btn-red" href="contact.html#book">Book a free site inspection</a><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a></div>
</div></div></section>
"""

STEPS = """<div class="steps">
<div class="step"><h3>Free site inspection</h3><p>We visit the site or review the drawings: rooms, ceiling space, shafts, outdoor unit location and power.</p></div>
<div class="step"><h3>Design &amp; quotation</h3><p>We calculate the cooling load, choose split, ducted or VRF, and send a written quotation.</p></div>
<div class="step"><h3>Installation</h3><p>Our team installs units, ductwork and refrigerant piping in step with the construction programme.</p></div>
<div class="step"><h3>Testing &amp; handover</h3><p>Pressure testing, commissioning and handover, with maintenance during the warranty period.</p></div>
</div>"""

PKG = [
 ("split", "Package 1", "Split AC", "assets/photos/pkg-split.jpg", "Hisab technicians in branded uniforms mounting a split AC unit in a new Dubai apartment",
  "Wall-mounted split units for apartments, rooms and offices in new buildings and villas.",
  "Apartments in new towers, villa rooms, offices",
  ["Cooling load check for every room", "Supply of inverter split units", "Copper piping, insulation and drain lines",
   "Outdoor unit mounting and brackets", "Testing, commissioning and handover"]),
 ("vrf", "Package 2", "VRF / VRV AC system", "assets/photos/pkg-vrf.jpg", "Hisab technicians installing VRF outdoor units on a Dubai rooftop",
  "One outdoor system, many indoor units, each room at its own temperature. Built for towers, large villas and buildings.",
  "Towers, multi-storey buildings, large villas, public and heritage projects",
  ["Heat load calculation and system design", "Indoor units: cassette, ducted or wall-mounted",
   "Refrigerant piping, branch kits and insulation", "Central and individual controllers",
   "Pressure testing, vacuum, charging and commissioning"]),
 ("ducted", "Package 3", "Ducted split AC &amp; ductwork", "assets/photos/pkg-ducted.jpg", "Hisab technicians installing insulated ductwork in a new villa",
  "The indoor unit hides above the false ceiling. Only slim grilles show. Even, quiet cooling for villas and open spaces.",
  "Villas, open-plan spaces, showrooms and offices with false ceilings",
  ["Duct design and airflow calculation", "Concealed ducted indoor and outdoor units",
   "Fabrication and installation of insulated ductwork", "Diffusers, grilles, thermostat and controls",
   "Air balancing, testing and commissioning"]),
]

def pkg_cards():
    out = ['<div class="packages">']
    for key, tag, name, img, alt, desc, best, items in PKG:
        out.append(f"""<article class="pkg"><img src="{img}" alt="{alt}" loading="lazy" width="800" height="500"><div class="pkg-body">
<div class="tag">{tag}</div><h3>{name}</h3><p>{desc}</p><div class="best"><b>Best for:</b> {best}</div>
<ul>{''.join(f'<li>{i}</li>' for i in items)}</ul>
<div class="actions"><a class="btn btn-red" href="contact.html?system={key}#book">Get a quote</a><a class="link" href="ac-systems.html#{key}">Details</a></div>
</div></article>""")
    out.append("</div>")
    return "\n".join(out)

def team_section():
    if not (photo("team.jpg") and photo("uniform-back.jpg")):
        return ""
    return """<section class="section"><div class="wrap split">
<img src="assets/photos/team.jpg" alt="Hisab Technical Services installation team on a construction site" loading="lazy" width="900" height="600">
<div><div class="eyebrow">Our team</div><h2>One team on site, start to handover.</h2>
<p>Our installation team works in step with the main contractor: ductwork and piping before the ceilings close, units and controls before handover. Safety gear on, site rules followed, work areas left clean.</p>
<img src="assets/photos/uniform-back.jpg" alt="Hisab technician with the company logo on his uniform, carrying copper pipe on a villa site" loading="lazy" width="400" height="500" style="max-width:260px;margin-top:10px"></div>
</div></section>
"""

def write(name, html):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)

PROJ = [
 ("heera", "Al Heera Literary Council", "Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", [
  ("heera-interior", "Courtyard hall with seating"), ("heera-hall", "Columned hall with timber ceiling"),
  ("heera-night", "Building exterior at dusk"), ("heera-exterior", "Entrance plaza at dusk")]),
 ("dibba", "Dibba Heritage Souq", "Sharjah", "Sandook Al Inarah", [
  ("dibba-front", "Main entrance"), ("dibba-ceiling", "Timber ceiling with linear air diffusers"),
  ("dibba-wide", "Souq building and arcade"), ("dibba-ceiling2", "Covered walkway ceiling")]),
 ("fili", "Al Hisn Fili Fort", "Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", [
  ("fili-corridor", "Restored corridor"), ("fili-camels", "Fort and visitors"), ("fili-units", "Row of outdoor VRF condensing units"),
  ("fili-courtyard", "Shaded courtyard"), ("fili-tower", "Fort tower and courtyard"), ("fili-distant", "Fort at sunset"),
  ("fili-wall", "Room with air grille"), ("fili-display", "Exhibition room"), ("fili-display2", "Exhibition wall with air grille"),
  ("fili-arch", "Arched timber grille"), ("fili-sand", "Fort building"), ("fili-plaque", "Opening plaque")]),
 ("dhaid", "Al Dhaid Fort Tower", "Al Dhaid, Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", [
  ("dhaid-tower", "Fort tower at dusk"), ("dhaid-ceiling", "Interior timber ceiling with air grille"), ("dhaid-carts", "Opening day at the fort"),
  ("dhaid-room1", "Restored room"), ("dhaid-room2", "Restored passage"), ("dhaid-room3", "Interior room")]),
 ("steps", "Little Steps Nursery", "Sharjah", "Al Shamsi Properties", [
  ("steps-exterior", "Nursery building exterior"), ("steps-interior", "Classroom with ceiling air diffusers"),
  ("steps-exterior2", "Nursery facade"), ("steps-tree", "Indoor play area")]),
]
REFS = [
 ("Al Heera Literary Council", "Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", "heera"),
 ("Dibba Heritage Souq", "Sharjah", "Sandook Al Inarah", "dibba"),
 ("Al Hisn Fili Fort", "Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", "fili"),
 ("Al Dhaid Fort Tower", "Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", "dhaid"),
 ("Little Steps Nursery", "Sharjah", "Al Shamsi Properties", "steps"),
 ("Nahwa Majlis &amp; Masjid", "Sharjah", "Mubadara / Amjad Nazwa Bldg. Cont.", ""),
 ("Villas", "Sharjah", "Al Tameer Cont. / ZB Construction", ""),
 ("Warehouse", "Dubai", "ZB Construction", ""),
 ("G+2 building", "Umm Al Quwain", "ZB Construction", ""),
 ("G+1 building", "Wadi Al Safa", "A &amp; A Building Contracting LLC", ""),
 ("G+4 building", "Wadi Al Safa", "A &amp; A Building Contracting LLC", ""),
 ("G+6 building", "Al Dhaid", "Kenna Hilal Ali", ""),
]

def ref_cards(link_prefix="projects.html"):
    out = []
    for i, (p, l, c, key) in enumerate(REFS, 1):
        name = f'<a href="{link_prefix}#{key}">{p}</a>' if key else p
        out.append(f'<div class="ref"><span class="num">{i:02d}</span><div><h3>{name}</h3><p>{l}<br><small>Client: {c}</small></p></div></div>')
    return '<div class="ref-grid">' + "".join(out) + "</div>"

# ---------- Home ----------
home = head("AC, VRF & Ducted Split AC Installation for Buildings & Villas in Dubai | Hisab Technical Services",
            "Hisab Technical Services installs split AC, VRF/VRV and ducted split air conditioning with ductwork for new buildings, towers and villas in Dubai and Sharjah. Free site inspection.",
            "index.html", ld(BUSINESS) + faq_ld())
home += f"""<section class="hero"><div class="hero-bg" role="img" aria-label="Hisab technicians installing VRF outdoor units on a Dubai rooftop"></div><div class="wrap">
<div class="eyebrow">Air conditioning installation · Dubai &amp; Sharjah</div>
<h1>AC for new buildings and villas. <span class="accent">Installed right.</span></h1>
<p class="lead">Split AC, VRF and ducted split systems with ductwork, for new towers, buildings and villas across Dubai and Sharjah. From design to handover.</p>
<div class="hero-actions"><a class="btn btn-red" href="contact.html#book">Book a free site inspection</a><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a></div>
<div class="hero-chips"><span class="chip">Split AC</span><span class="chip">VRF / VRV systems</span><span class="chip">Ducted split AC</span><span class="chip">Ductwork</span></div>
</div></section>
<section class="trust"><div class="wrap">
<div><b>25+ years</b><span>HVAC experience of our founding partner</span></div>
<div><b>12 projects</b><span>Completed in Sharjah, Dubai, Umm Al Quwain &amp; Al Dhaid</span></div>
<div><b>Free</b><span>Site inspection before every quote</span></div>
<div><b>DED licensed</b><span>Dubai licence no. 1229557</span></div>
</div></section>

<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">Our AC packages</div><h2>Three systems.<br>One focused team.</h2></div>
<p>We install air conditioning in new construction. Choose the system that fits your project, or let us recommend one after a free site inspection.</p></div>
{pkg_cards()}
</div></section>

<section class="section alt"><div class="wrap split">
<img src="assets/photos/why.jpg" alt="Columned hall with timber ceiling at Al Heera Literary Council, a Hisab project" loading="lazy" width="900" height="600">
<div><div class="eyebrow">Why Hisab</div><h2>New installations are all we do.</h2>
<p>A badly sized or badly installed system costs the building owner in power bills, noise and complaints for years. We focus on installing AC in new buildings and villas, so every design, every duct run and every handover gets full attention.</p>
<ul class="ticks"><li>Led by an HVAC engineer with more than 25 years in the field</li><li>Free site inspection and a clear written quote before work starts</li><li>Work planned around the main contractor’s programme</li><li>Maintenance during the warranty period on every system we install</li></ul>
<a class="link" href="about.html">Meet the team</a></div>
</div></section>
{team_section()}
<section class="section dark"><div class="wrap">
<div class="head"><div><div class="eyebrow">How it works</div><h2>From free inspection<br>to handover.</h2></div><p>The same process for one villa or a full building.</p></div>
{STEPS}
</div></section>

<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">Completed projects</div><h2>Trusted on landmark<br>Sharjah projects.</h2></div><a class="link" href="projects.html">See all projects</a></div>
<div class="projects">
<a class="proj big" href="projects.html#heera"><img src="assets/projects/heera-interior.jpg" alt="Courtyard hall of the Al Heera Literary Council, Sharjah" loading="lazy"><span><small>Sharjah</small><b>Al Heera Literary Council</b></span></a>
<a class="proj" href="projects.html#dibba"><img src="assets/projects/dibba-ceiling.jpg" alt="Ceiling with linear air diffusers at Dibba Heritage Souq" loading="lazy"><span><small>Sharjah</small><b>Dibba Heritage Souq</b></span></a>
<a class="proj" href="projects.html#fili"><img src="assets/projects/fili-corridor.jpg" alt="Restored corridor at Al Hisn Fili Fort" loading="lazy"><span><small>Sharjah</small><b>Al Hisn Fili Fort</b></span></a>
<a class="proj" href="projects.html#dhaid"><img src="assets/projects/dhaid-tower.jpg" alt="Al Dhaid Fort tower at dusk" loading="lazy"><span><small>Al Dhaid, Sharjah</small><b>Al Dhaid Fort Tower</b></span></a>
<a class="proj" href="projects.html#steps"><img src="assets/projects/steps-interior.jpg" alt="Classroom with ceiling air diffusers at Little Steps Nursery" loading="lazy"><span><small>Sharjah</small><b>Little Steps Nursery</b></span></a>
</div>
<h3 style="margin-top:56px">All 12 completed projects</h3>
{ref_cards()}
</div></section>

<section class="section alt"><div class="wrap">
<div class="eyebrow">Questions</div><h2>Good to know</h2>
<div class="faq">{faq_html()}</div>
</div></section>
{CTA}"""
write("index.html", home + FOOT)

# ---------- AC systems ----------
def detail(key, tag, title, img, alt, intro, best, parts, good, rev=False):
    return f"""<section class="section{' alt' if rev else ''}" id="{key}"><div class="wrap split{' reverse' if rev else ''}">
<img src="{img}" alt="{alt}" loading="lazy" width="900" height="675">
<div><div class="eyebrow">{tag}</div><h2>{title}</h2><p>{intro}</p><div class="best"><b>Best for:</b> {best}</div>
<h3>What the package covers</h3><ul class="ticks">{''.join(f'<li>{p}</li>' for p in parts)}</ul>
<p><b>Good to know:</b> {good}</p>
<a class="btn btn-red" href="contact.html?system={key}#book">Get a quote</a></div>
</div></section>
"""

svc = head("AC Systems for New Buildings: Split AC, VRF/VRV, Ducted Split | Hisab Technical Services",
           "Compare split AC, VRF/VRV and ducted split air conditioning for new buildings, towers and villas. Hisab designs, supplies, installs and commissions all three in Dubai and Sharjah.",
           "ac-systems.html", ld(BUSINESS))
svc += """<section class="page-hero"><div class="wrap"><div class="eyebrow">AC systems</div>
<h1>Split, VRF or ducted?<br><span class="accent-blue">We help you choose.</span></h1>
<p>Three installation packages for new buildings, towers and villas. Each covers design, supply, installation, testing and handover.</p></div></section>
<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">Side by side</div><h2>Which system fits your project?</h2></div><p>A quick guide. The final choice comes after a free site inspection.</p></div>
<div class="table-scroll"><table class="compare">
<thead><tr><th></th><th>Split AC</th><th>VRF / VRV</th><th>Ducted split AC</th></tr></thead>
<tbody>
<tr><th>Typical project</th><td>Apartments, villa rooms, small offices</td><td>Towers, multi-storey buildings, large villas</td><td>Villas, open-plan spaces, showrooms</td></tr>
<tr><th>What you see</th><td>Wall-mounted indoor unit</td><td>Cassettes, wall units or hidden ducted units</td><td>Only slim grilles in the ceiling</td></tr>
<tr><th>Room control</th><td>One remote per room</td><td>Each room set separately, plus central control</td><td>One thermostat per system or zone</td></tr>
<tr><th>Outdoor units</th><td>One per indoor unit</td><td>One system for many indoor units</td><td>One per ducted system</td></tr>
<tr><th>Needs false ceiling</th><td>No</td><td>Depends on indoor unit type</td><td>Yes</td></tr>
<tr><th>Plan it at</th><td>Finishing stage</td><td>Design stage</td><td>Before ceilings close</td></tr>
</tbody></table></div>
</div></section>
"""
svc += detail("split", "Package 1", "Split AC", "assets/photos/pkg-split.jpg", "Hisab technicians in branded uniforms mounting a split AC unit in a new Dubai apartment",
              "An indoor unit on the wall, an outdoor unit outside, connected by insulated copper pipes. We size every room so the units cool well without wasting power.",
              "Apartments in new towers, villa bedrooms and majlis, small offices",
              ["Cooling load check per room", "Supply of inverter split units", "Copper piping, insulation and drain lines, routed before finishing",
               "Outdoor unit mounting with brackets or stands", "Pressure test, vacuum, gas charge, commissioning and handover"],
              "piping routes are easier and neater when they are planned before plaster and paint.")
svc += detail("vrf", "Package 2", "VRF / VRV AC system", "assets/photos/pkg-vrf.jpg", "Hisab technicians installing VRF outdoor units on a Dubai rooftop",
              "Variable refrigerant flow (VRF, also sold as VRV) connects many indoor units to one outdoor system. Each room runs at its own temperature and the outdoor unit only works as hard as needed.",
              "Towers, multi-storey buildings, large villas, schools, nurseries, heritage and public projects",
              ["Heat load calculation and system design", "Indoor unit selection: ceiling cassette, ducted, wall-mounted or floor standing",
               "Refrigerant piping, branch (refnet) joints and insulation", "Individual room controllers and central control",
               "Pressure testing, vacuum, refrigerant charging and commissioning", "As-built handover"],
              "VRF piping is planned at design stage. Bring us in early on a new build.", rev=True)
svc += detail("ducted", "Package 3", "Ducted split AC &amp; ductwork", "assets/photos/pkg-ducted.jpg", "Hisab technicians installing insulated ductwork in a new villa",
              "A concealed indoor unit sits above the false ceiling and sends cool air through ducts to several rooms. You only see neat grilles. We design, fabricate and install the ductwork ourselves.",
              "Villas, open-plan living areas, showrooms and offices with false ceilings",
              ["Duct design and airflow calculation", "Concealed ducted indoor unit and matching outdoor unit",
               "Fabrication and installation of insulated ductwork", "Supply diffusers, return grilles, filters, thermostat and controls",
               "Air balancing, testing and commissioning"],
              "good duct design matters as much as the unit. Wrong duct sizes make noise and leave rooms warm.")
svc += f"""<section class="section dark"><div class="wrap">
<div class="head"><div><div class="eyebrow">How we work</div><h2>The same careful process<br>for every system.</h2></div></div>
{STEPS}</div></section>
<section class="section alt"><div class="wrap">
<div class="cards three">
<div class="card"><div class="ico">{ICON['shield']}</div><h3>Warranty support</h3><p>Maintenance during the warranty period on every system we install.</p></div>
<div class="card"><div class="ico">{ICON['tool']}</div><h3>Free site inspection</h3><p>Every project is different. We inspect first, then quote.</p></div>
<div class="card"><div class="ico">{ICON['users']}</div><h3>Contractor-friendly</h3><p>We work to the main contractor’s programme and site rules.</p></div>
</div></div></section>
{CTA}"""
write("ac-systems.html", svc + FOOT)

# ---------- Contact ----------
ct = head("Free Site Inspection & AC Quote | Hisab Technical Services Dubai",
          f"Book a free site inspection for split AC, VRF or ducted split AC installation in your new building or villa in Dubai or Sharjah. Call or WhatsApp {PHONE}.",
          "contact.html", ld(BUSINESS))
ct += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">Contact</div>
<h1>Every project is different.<br><span class="accent-blue">The inspection is free.</span></h1>
<p>Tell us about your building or villa. We inspect the site, recommend the right system and send a written quote.</p>
<div class="hero-actions"><a class="btn btn-red" href="#book">Book a free site inspection</a><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a></div></div></section>
<section class="section" id="book"><div class="wrap booking">
<div><div class="eyebrow">Free site inspection</div><h2>Tell us about your project.</h2>
<p>A few details help us prepare for the inspection. We will call you back to agree a time.</p>
<div class="contact-box">
<p>Call</p><a href="{TEL}">{PHONE}</a>
<p style="margin-top:16px">WhatsApp</p><a href="{WA}" target="_blank" rel="noopener">{WA_ICON} Message us</a>
<p style="margin-top:16px">E-mail</p><a href="mailto:{EMAIL}" style="font-size:18px">{EMAIL}</a>
<p style="margin-top:16px">Dubai, United Arab Emirates · Closed on Fridays</p></div></div>
<div class="form-card">
<form id="booking-form" name="site-inspection" method="POST" action="/thank-you" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="site-inspection">
<input type="hidden" name="subject" value="New site inspection request from the Hisab website">
<p class="hidden"><label>Leave this empty: <input name="bot-field"></label></p>
<div class="grid-2">
<label>Full name *<input name="name" required autocomplete="name"></label>
<label>Mobile / WhatsApp *<input name="phone" type="tel" required autocomplete="tel" placeholder="+971"></label>
<label>Email<input name="email" type="email" autocomplete="email" placeholder="Optional"></label>
<label>Project location *<input name="location" required placeholder="e.g. Al Barsha, Dubai"></label>
<label>Project type *<select name="project" required><option value="">Choose one</option><option>Villa</option><option>Tower / multi-storey building</option><option>Commercial building / office</option><option>School / nursery / public building</option><option>Other</option></select></label>
<label>AC system *<select name="system" id="system" required><option value="">Choose one</option><option value="split">Split AC</option><option value="vrf">VRF / VRV system</option><option value="ducted">Ducted split AC &amp; ductwork</option><option value="not-sure">Not sure yet – advise me</option></select></label>
<label>Project stage<select name="stage"><option value="">Choose one</option><option>Design / drawings</option><option>Under construction</option><option>Shell &amp; core ready</option><option>Finishing stage</option></select></label>
<label>Floors / rooms<input name="size" placeholder="e.g. G+2, 6 rooms"></label>
</div>
<label>Tell us more *<textarea name="message" rows="4" required placeholder="What are you building, and when do you need the AC installed?"></textarea></label>
<label>Google Maps location link<input name="maplink" type="url" placeholder="Optional – paste a location link"></label>
<label class="check"><input type="checkbox" name="consent" required><span>I agree that Hisab Technical Services may contact me about this request. *</span></label>
<button class="btn btn-red" type="submit">Book free inspection</button>
<p class="form-status" id="form-status" aria-live="polite"></p>
<p class="form-note">We only use these details to answer your request.</p>
</form></div>
</div></section>
<section class="section alt"><div class="wrap"><div class="eyebrow">Questions</div><h2>Good to know</h2><div class="faq">{faq_html()}</div></div></section>
"""
write("contact.html", ct + FOOT)

# ---------- Projects ----------
pj = head("Completed Air Conditioning Projects in Sharjah & Dubai | Hisab Technical Services",
          "Completed air conditioning projects by Hisab Technical Services: Al Heera Literary Council, Dibba Heritage Souq, Al Hisn Fili Fort, Al Dhaid Fort Tower, Little Steps Nursery, villas and G+1 to G+6 buildings.",
          "projects.html", ld(BUSINESS))
pj += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">Completed projects</div>
<h1>Heritage landmarks,<br><span class="accent-blue">villas and new buildings.</span></h1>
<p>12 completed projects across Sharjah, Dubai, Umm Al Quwain and Al Dhaid. Photos are from Hisab’s project records.</p></div></section>
<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">All projects</div><h2>Completed project list</h2></div><p>From our company profile.</p></div>
{ref_cards("")}
</div></section>
<section class="section alt"><div class="wrap">
"""
for key, title, loc, client, imgs in PROJ:
    gal = "".join(f'<img src="assets/projects/{i}.jpg" alt="{a} – {title}, {loc}" loading="lazy">' for i, a in imgs)
    pj += f'<article class="project-block" id="{key}"><div class="eyebrow">Completed project · {len(imgs)} photos</div><h2>{title}</h2><p class="meta">{loc} · Client: {client}</p><div class="gallery">{gal}</div></article>\n'
pj += f"""<p class="note">Tap a photo to see it larger. More on <a class="link" href="{IG}" target="_blank" rel="noopener">Instagram</a>.</p>
</div></section>
{CTA}"""
write("projects.html", pj + FOOT)

# ---------- About ----------
ab = head("About Hisab Technical Services | AC Installation Company in Dubai",
          "Hisab Technical Services LLC is a Dubai air conditioning installation company established in 2023 (DED licence 1229557), led by an HVAC engineer with more than 25 years of experience.",
          "about.html", ld(BUSINESS))
white = lambda k: ICON[k].replace('<svg', '<svg style="stroke:#fff"')
ab += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">About us</div>
<h1>Your trusted partner<br><span class="accent-blue">for HVAC solutions.</span></h1>
<p>A Dubai company built around one thing: air conditioning in new buildings and villas, sized right and installed right.</p></div></section>
<section class="section"><div class="wrap split">
<div><div class="eyebrow">Our story</div><h2>Established in Dubai, 2023.</h2>
<p>Hisab Technical Services LLC was established in August 2023 in Dubai, United Arab Emirates, and is registered with the Dubai Department of Economy and Tourism (DED) under licence no. 1229557.</p>
<p>We design, supply and install split AC, VRF/VRV and ducted split air conditioning with ductwork for new buildings, towers and villas across Dubai and Sharjah, including heritage landmarks and multi-storey buildings.</p></div>
<img src="assets/projects/heera-exterior.jpg" alt="Al Heera Literary Council building in Sharjah, a Hisab project" loading="lazy" width="560" height="690" style="aspect-ratio:4/4.4">
</div></section>
<section class="section alt"><div class="wrap">
<div class="eyebrow">Leadership</div><h2>Engineering experience,<br>business discipline.</h2>
<div class="people">
<div class="person"><small>Founding partner</small><h3>Eng. Mohammad Rafique Attar</h3><p>More than 25 years in HVAC, including roles with established UAE companies. He leads the technical side: system design and installation.</p></div>
<div class="person"><small>Co-founder &amp; Managing Director</small><h3>Muhammad Saadat Shafqat, ACA</h3><p>Chartered Accountant and member of the Institute of Chartered Accountants of Pakistan (ICAP), with more than 10 years in accountancy. He manages finance and operations.</p></div>
</div></div></section>
{team_section()}
<section class="section"><div class="wrap split">
<div><div class="eyebrow">Vision</div><h2>The AC partner contractors call again.</h2><p>To become a trusted partner for HVAC solutions for our commercial and residential customers.</p></div>
<div><div class="eyebrow">Mission</div><h2>Quality work at a fair price.</h2><p>To give our clients quality air conditioning within an economical budget, easing the load on their pockets while they build their homes and businesses.</p></div>
</div></section>
<section class="section dark"><div class="wrap">
<div class="eyebrow">How we work</div><h2>Four principles. Every job.</h2>
<div class="cards">
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('shield')}</div><h3>Integrity</h3><p>Clear quotes, honest advice and commitments people can count on.</p></div>
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('tool')}</div><h3>Quality</h3><p>Careful installation, proper testing and a clean handover.</p></div>
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('leaf')}</div><h3>Safety</h3><p>Safety gear, safe work methods and respect for site rules.</p></div>
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('users')}</div><h3>Teamwork</h3><p>One coordinated team from inspection to handover.</p></div>
</div></div></section>
{CTA}"""
write("about.html", ab + FOOT)

# ---------- Thank you / 404 ----------
ty = head("Thank you | Hisab Technical Services", "Your request has been sent to Hisab Technical Services.", "thank-you.html", '<meta name="robots" content="noindex">\n')
ty += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">Request received</div><h1>Thank you.<br><span class="accent-blue">We’ll call you back.</span></h1>
<p>Our team will contact you to arrange your free site inspection. Need us sooner? Call or WhatsApp {PHONE}.</p>
<div class="hero-actions"><a class="btn btn-red" href="{WA}" target="_blank" rel="noopener">{WA_ICON} WhatsApp us</a><a class="btn btn-ghost" href="index.html">Back to home</a></div></div></section>"""
write("thank-you.html", ty + FOOT)
nf = head("Page not found | Hisab Technical Services", "This page does not exist.", "404.html", '<meta name="robots" content="noindex">\n')
nf += """<section class="page-hero"><div class="wrap"><div class="eyebrow">404</div><h1>This page isn’t here.</h1>
<p>Try the AC systems page or go back home.</p><div class="hero-actions"><a class="btn btn-red" href="ac-systems.html">AC systems</a><a class="btn btn-ghost" href="index.html">Home</a></div></div></section>"""
write("404.html", nf + FOOT)

# ---------- sitemap / robots ----------
pages = ["", "ac-systems", "projects", "about", "contact"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"  <url><loc>{SITE}/{p}</loc></url>\n" for p in pages) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("built")
