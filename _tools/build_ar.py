#!/usr/bin/env python3
"""Generates the Arabic (right-to-left) version of the Hisab site in <site folder>/ar/.

Usage: python3 _tools/build_ar.py <site folder>   (run after build.py)

Same pages, photos and form as the English site. Every page links to its English twin
(English pages link back with the "العربية" button). Assets are loaded from the site root (../).
"""
import json, os, sys

OUT = sys.argv[1]
AR = os.path.join(OUT, "ar")
os.makedirs(AR, exist_ok=True)
SITE = "https://hisabtechnical.com"
PHONE = "+971 55 828 5372"
TEL = "tel:+971558285372"
WA = "https://wa.me/971558285372?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D9%8B%20%D8%AD%D8%B3%D8%A7%D8%A8%D8%8C%20%D8%A3%D8%B1%D8%BA%D8%A8%20%D9%81%D9%8A%20%D9%85%D8%B9%D8%A7%D9%8A%D9%86%D8%A9%20%D9%85%D8%AC%D8%A7%D9%86%D9%8A%D8%A9%20%D9%84%D9%84%D9%85%D9%88%D9%82%D8%B9."
EMAIL = "hvac@hisabtechnical.com"
IG = "https://instagram.com/hisab_technical_services_llc"
R = "../"  # path to the site root

def ltr(t):
    return f'<bdi dir="ltr">{t}</bdi>'

def photo(name):
    return os.path.exists(os.path.join(OUT, "assets", "photos", name))

NAV = [("index.html", "الرئيسية"), ("ac-systems.html", "أنظمة التكييف"), ("projects.html", "المشاريع"),
       ("about.html", "من نحن"), ("contact.html", "تواصل معنا")]

WA_ICON = '<svg class="wa" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'

ICON = {
 "shield": '<svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
 "tool": '<svg viewBox="0 0 24 24"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24"><path d="M5 19c0-8 5-13 15-14-1 10-6 15-14 15"/><path d="M5 19l7-7"/></svg>',
 "users": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.5-4 3-6 6.5-6s6 2 6.5 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.5 0 4 1.5 4.5 4.5"/></svg>',
}

def head(title, desc, path, extra=""):
    slug = "" if path == "index.html" else path.replace(".html", "")
    url, en_url = SITE + "/ar/" + slug, SITE + "/" + slug
    menu = "".join(f'<a href="{h}"' + (' aria-current="page"' if h == path else '') + f'>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ar_AE">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1020">
<link rel="icon" type="image/png" href="{R}assets/favicon.png">
<link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}styles.css">
{extra}</head>
<body>
<a class="skip" href="#main">انتقل إلى المحتوى</a>
<div class="topbar"><div class="wrap"><span>تكييف سبليت · VRF · سبليت مخفي بالدكت<span class="hide-sm"> · مبانٍ وفلل جديدة · دبي والشارقة</span></span><span class="top-links"><a href="{WA}" target="_blank" rel="noopener">واتساب</a><a href="{TEL}">{ltr(PHONE)}</a></span></div></div>
<header class="header"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="حساب للخدمات الفنية – الرئيسية"><img src="{R}assets/hisab-logo-header-v3.png" alt="حساب للخدمات الفنية ذ.م.م – شريكك الموثوق لحلول التكييف والتهوية" width="576" height="203"></a>
<div class="nav-end"><nav class="menu" id="menu" aria-label="القائمة الرئيسية">{menu}<a class="btn btn-red" href="contact.html#book">معاينة مجانية للموقع</a></nav>
<a class="lang-switch" href="{R}{path}" hreflang="en" lang="en">English</a><button class="menu-toggle" aria-label="فتح القائمة" aria-expanded="false" aria-controls="menu">☰</button></div>
</div></header>
<main id="main">
"""

FOOT = f"""</main>
<footer class="footer"><div class="wrap">
<div class="footer-grid">
<div><img src="{R}assets/hisab-logo.png" alt="حساب للخدمات الفنية ذ.م.م" width="590" height="235" loading="lazy"><p>تكييف سبليت وأنظمة VRF وسبليت مخفي بالدكت للمباني والأبراج والفلل الجديدة في دبي والشارقة.</p></div>
<div><h4>أنظمة التكييف</h4><a href="ac-systems.html#split">تكييف سبليت</a><a href="ac-systems.html#vrf">أنظمة VRF / VRV</a><a href="ac-systems.html#ducted">سبليت مخفي وأعمال الدكت</a></div>
<div><h4>الشركة</h4><a href="about.html">من نحن</a><a href="projects.html">المشاريع</a><a href="contact.html#book">معاينة مجانية للموقع</a></div>
<div><h4>تواصل معنا</h4><a href="{TEL}">{ltr(PHONE)}</a><a href="{WA}" target="_blank" rel="noopener">واتساب</a><a href="mailto:{EMAIL}">{EMAIL}</a><p>دبي، الإمارات العربية المتحدة<br>رخصة دائرة الاقتصاد والسياحة رقم {ltr("1229557")}</p></div>
</div>
<div class="footer-base footer-credit" dir="ltr"><span>© 2026 Hisab Technical Services LLC.</span><span>Designed By Alexis FZC LLC</span></div>
</div></footer>
<div class="callbar"><a href="{TEL}">اتصل</a><a href="{WA}" target="_blank" rel="noopener">واتساب</a></div>
<script src="{R}site.js"></script>
</body>
</html>
"""

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"

BUSINESS = {
    "@context": "https://schema.org", "@type": "HVACBusiness", "name": "حساب للخدمات الفنية ذ.م.م",
    "alternateName": "Hisab Technical Services LLC", "inLanguage": "ar",
    "slogan": "شريكك الموثوق لحلول التكييف والتهوية", "url": SITE + "/ar/", "telephone": "+971558285372", "email": EMAIL,
    "image": SITE + "/assets/og-image.jpg", "logo": SITE + "/assets/hisab-logo.png", "foundingDate": "2023-08",
    "address": {"@type": "PostalAddress", "addressLocality": "دبي", "addressCountry": "AE"},
    "areaServed": [{"@type": "City", "name": "دبي"}, {"@type": "City", "name": "الشارقة"}, {"@type": "Country", "name": "الإمارات العربية المتحدة"}],
    "sameAs": [IG],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "تركيب أنظمة التكييف", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "توريد وتركيب تكييف سبليت للمباني والفلل الجديدة"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "تصميم وتركيب وتشغيل أنظمة تكييف VRF / VRV"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "تصميم وتركيب تكييف سبليت مخفي وأعمال الدكت"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "معاينة مجانية للموقع"}}]},
}

FAQ = [
 ("هل معاينة الموقع مجانية؟",
  "نعم. كل مشروع مختلف، لذلك نعاين الموقع أولاً. المعاينة مجانية، وبعدها تستلم عرض سعر مكتوباً."),
 ("ما نظام التكييف المناسب لمبناي أو فيلتي؟",
  "يعتمد ذلك على عدد الغرف والمساحة فوق السقف وطريقة استخدام المبنى. الوحدات السبليت تناسب الغرف المنفردة والشقق. السبليت المخفي بالدكت يخفي الوحدة الداخلية فوق السقف المستعار ويناسب الفلل والمساحات المفتوحة. نظام VRF يناسب الفلل الكبيرة والأبراج والمباني متعددة الغرف على نظام خارجي واحد. نوصي بالنظام المناسب بعد معاينة الموقع."),
 ("ما الفرق بين نظام VRF والسبليت المخفي بالدكت؟",
  "نظام السبليت المخفي يستخدم وحدة داخلية واحدة توزّع الهواء البارد عبر مجاري الدكت إلى عدة غرف، وغالباً بثرموستات واحد لكل نظام. أما نظام VRF (تدفق متغير لوسيط التبريد، ويُسمّى أيضاً VRV) فيربط عدة وحدات داخلية بوحدة خارجية واحدة، فيمكن ضبط حرارة كل غرفة على حدة."),
 ("هل تعملون في المشاريع الجديدة قيد الإنشاء؟",
  "نعم. التركيبات الجديدة هي تخصصنا: التكييف وأعمال الدكت للمباني والأبراج والفلل الجديدة، من مرحلة التصميم حتى التركيب والاختبار والتسليم."),
 ("هل تقدمون خدمة الصيانة؟",
  "نحن متخصصون في التركيبات الجديدة. نقدم الصيانة للأنظمة التي قمنا بتركيبها خلال فترة الضمان."),
 ("ما المناطق التي تغطونها؟",
  "مقرنا في دبي ونعمل في دبي والشارقة، ولدينا مشاريع منجزة في الشارقة والذيد وأم القيوين ودبي."),
]

def faq_ld():
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "ar", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]})

def faq_html():
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

CTA = f"""<section class="section"><div class="wrap"><div class="cta">
<div><h2>تبني أو تُنهي<br>فيلا أو برجاً؟</h2><p>كل مشروع مختلف. احجز معاينة مجانية للموقع واحصل على عرض سعر مكتوب لنظام التكييف المناسب.</p></div>
<div class="actions"><a class="btn btn-red" href="contact.html#book">احجز معاينة مجانية</a><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{WA_ICON} راسلنا على واتساب</a></div>
</div></div></section>
"""

STEPS = """<div class="steps">
<div class="step"><h3>معاينة مجانية للموقع</h3><p>نزور الموقع أو نراجع المخططات: الغرف، المساحة فوق السقف، الشفتات، مكان الوحدات الخارجية والكهرباء.</p></div>
<div class="step"><h3>التصميم وعرض السعر</h3><p>نحسب الحمل الحراري، ونختار بين السبليت أو المخفي أو VRF، ونرسل عرض سعر مكتوباً.</p></div>
<div class="step"><h3>التركيب</h3><p>يركّب فريقنا الوحدات والدكت وأنابيب وسيط التبريد بالتنسيق مع البرنامج الزمني للإنشاء.</p></div>
<div class="step"><h3>الاختبار والتسليم</h3><p>اختبار الضغط والتشغيل والتسليم، مع الصيانة خلال فترة الضمان.</p></div>
</div>"""

PKG = [
 ("split", "الباقة 1", "تكييف سبليت", "pkg-split.jpg", "فنيو حساب بالزي الموحد يركّبون وحدة تكييف سبليت في شقة جديدة في دبي",
  "وحدات سبليت جدارية للشقق والغرف والمكاتب في المباني والفلل الجديدة.",
  "الشقق في الأبراج الجديدة، غرف الفلل، المكاتب",
  ["فحص الحمل الحراري لكل غرفة", "توريد وحدات سبليت إنفرتر", "أنابيب نحاس وعزل وخطوط تصريف",
   "تثبيت الوحدة الخارجية والحوامل", "الاختبار والتشغيل والتسليم"]),
 ("vrf", "الباقة 2", "نظام تكييف VRF / VRV", "pkg-vrf.jpg", "فنيو حساب يركّبون وحدات VRF خارجية على سطح مبنى في دبي",
  "نظام خارجي واحد لعدة وحدات داخلية، وكل غرفة بدرجة حرارتها الخاصة. مصمم للأبراج والفلل الكبيرة والمباني.",
  "الأبراج، المباني متعددة الطوابق، الفلل الكبيرة، المشاريع العامة والتراثية",
  ["حساب الحمل الحراري وتصميم النظام", "وحدات داخلية: كاسيت أو مخفية أو جدارية",
   "أنابيب وسيط التبريد ووصلات التفريع والعزل", "وحدات تحكم مركزية وفردية",
   "اختبار الضغط والتفريغ وشحن الغاز والتشغيل"]),
 ("ducted", "الباقة 3", "سبليت مخفي وأعمال الدكت", "pkg-ducted.jpg", "فنيو حساب يركّبون مجاري هواء معزولة في فيلا جديدة",
  "الوحدة الداخلية مخفية فوق السقف المستعار، ولا يظهر إلا فتحات أنيقة. تبريد متساوٍ وهادئ للفلل والمساحات المفتوحة.",
  "الفلل، المساحات المفتوحة، صالات العرض والمكاتب ذات الأسقف المستعارة",
  ["تصميم الدكت وحساب تدفق الهواء", "وحدات داخلية مخفية ووحدات خارجية",
   "تصنيع وتركيب مجاري هواء معزولة", "فتحات التوزيع والشبكات والثرموستات وأنظمة التحكم",
   "موازنة الهواء والاختبار والتشغيل"]),
]

def pkg_cards():
    out = ['<div class="packages">']
    for key, tag, name, img, alt, desc, best, items in PKG:
        out.append(f"""<article class="pkg"><img src="{R}assets/photos/{img}" alt="{alt}" loading="lazy" width="800" height="500"><div class="pkg-body">
<div class="tag">{tag}</div><h3>{name}</h3><p>{desc}</p><div class="best"><b>الأنسب لـ:</b> {best}</div>
<ul>{''.join(f'<li>{i}</li>' for i in items)}</ul>
<div class="actions"><a class="btn btn-red" href="contact.html?system={key}#book">اطلب عرض سعر</a><a class="link" href="ac-systems.html#{key}">التفاصيل</a></div>
</div></article>""")
    out.append("</div>")
    return "\n".join(out)

def team_section():
    if not (photo("team.jpg") and photo("uniform-back.jpg")):
        return ""
    return f"""<section class="section"><div class="wrap split">
<img src="{R}assets/photos/team.jpg" alt="فريق تركيب حساب للخدمات الفنية في موقع إنشاء" loading="lazy" width="900" height="600">
<div><div class="eyebrow">فريقنا</div><h2>فريق واحد في الموقع، من البداية حتى التسليم.</h2>
<p>يعمل فريق التركيب لدينا بالتنسيق مع المقاول الرئيسي: الدكت والأنابيب قبل إغلاق الأسقف، والوحدات وأنظمة التحكم قبل التسليم. معدات السلامة دائماً، والالتزام بقواعد الموقع، وترك مناطق العمل نظيفة.</p>
<img src="{R}assets/photos/uniform-back.jpg" alt="فني من حساب يحمل شعار الشركة على زيه ويحمل أنابيب نحاس في موقع فيلا" loading="lazy" width="400" height="500" style="max-width:260px;margin-top:10px"></div>
</div></section>
"""

def write(name, html):
    with open(os.path.join(AR, name), "w") as f:
        f.write(html)

SHJ, DXB, UAQ, DHAID, WAS = "الشارقة", "دبي", "أم القيوين", "الذيد", "وادي الصفا"
MUB = "Mubadara / Amjad Nazwa Bldg. Cont."
PROJ = [
 ("heera", "مجلس الحيرة الأدبي", SHJ, MUB, [
  ("heera-interior", "قاعة الفناء مع الجلسات"), ("heera-hall", "قاعة بأعمدة وسقف خشبي"),
  ("heera-night", "واجهة المبنى عند الغروب"), ("heera-exterior", "ساحة المدخل عند الغروب")]),
 ("dibba", "سوق دبا التراثي", SHJ, "Sandook Al Inarah", [
  ("dibba-front", "المدخل الرئيسي"), ("dibba-ceiling", "سقف خشبي مع فتحات هواء طولية"),
  ("dibba-wide", "مبنى السوق والأروقة"), ("dibba-ceiling2", "سقف الممر المغطى")]),
 ("fili", "حصن فلي", SHJ, MUB, [
  ("fili-corridor", "ممر بعد الترميم"), ("fili-camels", "الحصن والزوار"), ("fili-units", "صف من وحدات VRF الخارجية"),
  ("fili-courtyard", "فناء مظلل"), ("fili-tower", "برج الحصن والفناء"), ("fili-distant", "الحصن عند الغروب"),
  ("fili-wall", "غرفة مع شبكة هواء"), ("fili-display", "قاعة عرض"), ("fili-display2", "جدار العرض مع شبكة هواء"),
  ("fili-arch", "شبكة خشبية مقوسة"), ("fili-sand", "مبنى الحصن"), ("fili-plaque", "لوحة الافتتاح")]),
 ("dhaid", "برج حصن الذيد", "الذيد، الشارقة", MUB, [
  ("dhaid-tower", "برج الحصن عند الغروب"), ("dhaid-ceiling", "سقف خشبي داخلي مع شبكة هواء"), ("dhaid-carts", "يوم افتتاح الحصن"),
  ("dhaid-room1", "غرفة بعد الترميم"), ("dhaid-room2", "ممر بعد الترميم"), ("dhaid-room3", "غرفة داخلية")]),
 ("steps", "حضانة ليتل ستبس", SHJ, "Al Shamsi Properties", [
  ("steps-exterior", "واجهة مبنى الحضانة"), ("steps-interior", "فصل دراسي مع فتحات هواء في السقف"),
  ("steps-exterior2", "واجهة الحضانة"), ("steps-tree", "منطقة اللعب الداخلية")]),
]
REFS = [
 ("مجلس الحيرة الأدبي", SHJ, MUB, "heera"),
 ("سوق دبا التراثي", SHJ, "Sandook Al Inarah", "dibba"),
 ("حصن فلي", SHJ, MUB, "fili"),
 ("برج حصن الذيد", SHJ, MUB, "dhaid"),
 ("حضانة ليتل ستبس", SHJ, "Al Shamsi Properties", "steps"),
 ("مجلس ومسجد نحوة", SHJ, MUB, ""),
 ("فلل", SHJ, "Al Tameer Cont. / ZB Construction", ""),
 ("مستودع", DXB, "ZB Construction", ""),
 ("مبنى أرضي + 2", UAQ, "ZB Construction", ""),
 ("مبنى أرضي + 1", WAS, "A &amp; A Building Contracting LLC", ""),
 ("مبنى أرضي + 4", WAS, "A &amp; A Building Contracting LLC", ""),
 ("مبنى أرضي + 6", DHAID, "Kenna Hilal Ali", ""),
]

def ref_cards(link_prefix="projects.html"):
    out = []
    for i, (p, l, c, key) in enumerate(REFS, 1):
        name = f'<a href="{link_prefix}#{key}">{p}</a>' if key else p
        out.append(f'<div class="ref"><span class="num">{i:02d}</span><div><h3>{name}</h3><p>{l}<br><small>العميل: {ltr(c)}</small></p></div></div>')
    return '<div class="ref-grid">' + "".join(out) + "</div>"

# ---------- Home ----------
home = head("تركيب تكييف سبليت وVRF ومخفي بالدكت للمباني والفلل في دبي | حساب للخدمات الفنية",
            "حساب للخدمات الفنية تركّب تكييف سبليت وأنظمة VRF/VRV وسبليت مخفي مع أعمال الدكت للمباني والأبراج والفلل الجديدة في دبي والشارقة. معاينة مجانية للموقع.",
            "index.html", ld(BUSINESS) + faq_ld())
home += f"""<section class="hero"><div class="hero-bg" role="img" aria-label="فنيو حساب يركّبون وحدات VRF خارجية على سطح مبنى في دبي"></div><div class="wrap">
<div class="eyebrow">تركيب أنظمة التكييف · دبي والشارقة</div>
<h1>حلول التكييف والتهوية للمباني الجديدة. <span class="accent">تركيب صحيح من أول مرة.</span></h1>
<p class="tagline">الراحة نظام متكامل. ونحن نجعله يعمل.</p>
<p class="lead">أنظمة سبليت وVRF وسبليت مخفي مع أعمال الدكت، للأبراج والمباني والفلل الجديدة في دبي والشارقة. من التصميم حتى التسليم.</p>
<div class="hero-actions"><a class="btn btn-red" href="contact.html#book">احجز معاينة مجانية للموقع</a><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{WA_ICON} راسلنا على واتساب</a></div>
<div class="hero-chips"><span class="chip">تكييف سبليت</span><span class="chip">أنظمة VRF / VRV</span><span class="chip">سبليت مخفي</span><span class="chip">أعمال الدكت</span></div>
</div></section>
<section class="trust"><div class="wrap">
<div><b>+25 عاماً</b><span>خبرة الشريك المؤسس في التكييف والتهوية</span></div>
<div><b>12 مشروعاً</b><span>منجزة في الشارقة ودبي وأم القيوين والذيد</span></div>
<div><b>مجاناً</b><span>معاينة الموقع قبل كل عرض سعر</span></div>
<div><b>مرخّصة</b><span>رخصة دبي رقم {ltr("1229557")}</span></div>
</div></section>

<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">باقات التكييف</div><h2>ثلاثة أنظمة.<br>فريق واحد متخصص.</h2></div>
<p>نركّب أنظمة التكييف في المشاريع الجديدة. اختر النظام المناسب لمشروعك، أو دعنا نوصي به بعد معاينة مجانية للموقع.</p></div>
{pkg_cards()}
</div></section>

<section class="section alt"><div class="wrap split">
<img src="{R}assets/photos/why.jpg" alt="قاعة بأعمدة وسقف خشبي في مجلس الحيرة الأدبي، أحد مشاريع حساب" loading="lazy" width="900" height="600">
<div><div class="eyebrow">لماذا حساب</div><h2>التركيبات الجديدة هي كل ما نفعله.</h2>
<p>النظام غير المناسب أو المركّب بشكل خاطئ يكلّف مالك المبنى فواتير كهرباء مرتفعة وضجيجاً وشكاوى لسنوات. نحن نركّز على تركيب التكييف في المباني والفلل الجديدة، فيحظى كل تصميم وكل مسار دكت وكل تسليم بالاهتمام الكامل.</p>
<ul class="ticks"><li>بقيادة مهندس تكييف بخبرة تزيد على 25 عاماً</li><li>معاينة مجانية للموقع وعرض سعر مكتوب وواضح قبل بدء العمل</li><li>عمل مخطط وفق البرنامج الزمني للمقاول الرئيسي</li><li>صيانة خلال فترة الضمان لكل نظام نركّبه</li></ul>
<a class="link" href="about.html">تعرّف على فريقنا</a></div>
</div></section>
{team_section()}
<section class="section dark"><div class="wrap">
<div class="head"><div><div class="eyebrow">كيف نعمل</div><h2>من المعاينة المجانية<br>حتى التسليم.</h2></div><p>نفس الخطوات لفيلا واحدة أو لمبنى كامل.</p></div>
{STEPS}
</div></section>

<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">مشاريع منجزة</div><h2>ثقة في مشاريع<br>بارزة في الشارقة.</h2></div><a class="link" href="projects.html">جميع المشاريع</a></div>
<div class="projects">
<a class="proj big" href="projects.html#heera"><img src="{R}assets/projects/heera-interior.jpg" alt="قاعة الفناء في مجلس الحيرة الأدبي، الشارقة" loading="lazy"><span><small>الشارقة</small><b>مجلس الحيرة الأدبي</b></span></a>
<a class="proj" href="projects.html#dibba"><img src="{R}assets/projects/dibba-ceiling.jpg" alt="سقف مع فتحات هواء طولية في سوق دبا التراثي" loading="lazy"><span><small>الشارقة</small><b>سوق دبا التراثي</b></span></a>
<a class="proj" href="projects.html#fili"><img src="{R}assets/projects/fili-corridor.jpg" alt="ممر بعد الترميم في حصن فلي" loading="lazy"><span><small>الشارقة</small><b>حصن فلي</b></span></a>
<a class="proj" href="projects.html#dhaid"><img src="{R}assets/projects/dhaid-tower.jpg" alt="برج حصن الذيد عند الغروب" loading="lazy"><span><small>الذيد، الشارقة</small><b>برج حصن الذيد</b></span></a>
<a class="proj" href="projects.html#steps"><img src="{R}assets/projects/steps-interior.jpg" alt="فصل دراسي مع فتحات هواء في السقف في حضانة ليتل ستبس" loading="lazy"><span><small>الشارقة</small><b>حضانة ليتل ستبس</b></span></a>
</div>
<h3 style="margin-top:56px">جميع المشاريع المنجزة (12)</h3>
{ref_cards()}
</div></section>

<section class="section alt"><div class="wrap">
<div class="eyebrow">أسئلة</div><h2>معلومات تهمّك</h2>
<div class="faq">{faq_html()}</div>
</div></section>
{CTA}"""
write("index.html", home + FOOT)

# ---------- AC systems ----------
def detail(key, tag, title, img, alt, intro, best, parts, good, rev=False):
    return f"""<section class="section{' alt' if rev else ''}" id="{key}"><div class="wrap split{' reverse' if rev else ''}">
<img src="{R}assets/photos/{img}" alt="{alt}" loading="lazy" width="900" height="675">
<div><div class="eyebrow">{tag}</div><h2>{title}</h2><p>{intro}</p><div class="best"><b>الأنسب لـ:</b> {best}</div>
<h3>ما تشمله الباقة</h3><ul class="ticks">{''.join(f'<li>{p}</li>' for p in parts)}</ul>
<p><b>معلومة مهمة:</b> {good}</p>
<a class="btn btn-red" href="contact.html?system={key}#book">اطلب عرض سعر</a></div>
</div></section>
"""

svc = head("أنظمة التكييف للمباني الجديدة: سبليت، VRF/VRV، سبليت مخفي | حساب للخدمات الفنية",
           "قارن بين تكييف سبليت وأنظمة VRF/VRV والسبليت المخفي للمباني والأبراج والفلل الجديدة. حساب تصمم وتورّد وتركّب وتشغّل الأنظمة الثلاثة في دبي والشارقة.",
           "ac-systems.html", ld(BUSINESS))
svc += """<section class="page-hero"><div class="wrap"><div class="eyebrow">أنظمة التكييف</div>
<h1>سبليت أم VRF أم مخفي؟<br><span class="accent-blue">نساعدك على الاختيار.</span></h1>
<p>ثلاث باقات تركيب للمباني والأبراج والفلل الجديدة. كل باقة تشمل التصميم والتوريد والتركيب والاختبار والتسليم.</p></div></section>
<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">مقارنة</div><h2>أي نظام يناسب مشروعك؟</h2></div><p>دليل سريع. الاختيار النهائي يكون بعد معاينة مجانية للموقع.</p></div>
<div class="table-scroll"><table class="compare">
<thead><tr><th></th><th>تكييف سبليت</th><th>VRF / VRV</th><th>سبليت مخفي</th></tr></thead>
<tbody>
<tr><th>المشروع المعتاد</th><td>الشقق، غرف الفلل، المكاتب الصغيرة</td><td>الأبراج، المباني متعددة الطوابق، الفلل الكبيرة</td><td>الفلل، المساحات المفتوحة، صالات العرض</td></tr>
<tr><th>ما يظهر لك</th><td>وحدة داخلية جدارية</td><td>كاسيت أو وحدات جدارية أو وحدات مخفية</td><td>فتحات أنيقة في السقف فقط</td></tr>
<tr><th>التحكم بالغرف</th><td>ريموت لكل غرفة</td><td>ضبط كل غرفة على حدة مع تحكم مركزي</td><td>ثرموستات لكل نظام أو منطقة</td></tr>
<tr><th>الوحدات الخارجية</th><td>وحدة لكل وحدة داخلية</td><td>نظام واحد لعدة وحدات داخلية</td><td>وحدة لكل نظام مخفي</td></tr>
<tr><th>يحتاج سقفاً مستعاراً</th><td>لا</td><td>حسب نوع الوحدة الداخلية</td><td>نعم</td></tr>
<tr><th>التخطيط له في</th><td>مرحلة التشطيب</td><td>مرحلة التصميم</td><td>قبل إغلاق الأسقف</td></tr>
</tbody></table></div>
</div></section>
"""
svc += detail("split", "الباقة 1", "تكييف سبليت", "pkg-split.jpg", "فنيو حساب بالزي الموحد يركّبون وحدة تكييف سبليت في شقة جديدة في دبي",
              "وحدة داخلية على الجدار ووحدة خارجية، تربطهما أنابيب نحاس معزولة. نحسب حمل كل غرفة حتى تبرّد الوحدات جيداً دون هدر للكهرباء.",
              "الشقق في الأبراج الجديدة، غرف النوم والمجالس في الفلل، المكاتب الصغيرة",
              ["فحص الحمل الحراري لكل غرفة", "توريد وحدات سبليت إنفرتر", "أنابيب نحاس وعزل وخطوط تصريف، تُمدّ قبل التشطيب",
               "تثبيت الوحدة الخارجية بحوامل أو قواعد", "اختبار الضغط والتفريغ وشحن الغاز والتشغيل والتسليم"],
              "مسارات الأنابيب أسهل وأرتب عندما يُخطط لها قبل اللياسة والدهان.")
svc += detail("vrf", "الباقة 2", "نظام تكييف VRF / VRV", "pkg-vrf.jpg", "فنيو حساب يركّبون وحدات VRF خارجية على سطح مبنى في دبي",
              "نظام التدفق المتغير لوسيط التبريد (VRF، ويُباع أيضاً باسم VRV) يربط عدة وحدات داخلية بنظام خارجي واحد. كل غرفة تعمل بدرجة حرارتها الخاصة، والوحدة الخارجية تعمل بالقدر المطلوب فقط.",
              "الأبراج، المباني متعددة الطوابق، الفلل الكبيرة، المدارس والحضانات، المشاريع التراثية والعامة",
              ["حساب الحمل الحراري وتصميم النظام", "اختيار الوحدات الداخلية: كاسيت سقفي، مخفي، جداري أو أرضي",
               "أنابيب وسيط التبريد ووصلات التفريع (Refnet) والعزل", "وحدات تحكم لكل غرفة وتحكم مركزي",
               "اختبار الضغط والتفريغ وشحن وسيط التبريد والتشغيل", "تسليم المخططات النهائية كما نُفّذت"],
              "تُخطط أنابيب نظام VRF في مرحلة التصميم. أشركنا مبكراً في مشروعك الجديد.", rev=True)
svc += detail("ducted", "الباقة 3", "سبليت مخفي وأعمال الدكت", "pkg-ducted.jpg", "فنيو حساب يركّبون مجاري هواء معزولة في فيلا جديدة",
              "وحدة داخلية مخفية فوق السقف المستعار ترسل الهواء البارد عبر مجاري الدكت إلى عدة غرف. لا يظهر لك إلا فتحات أنيقة. نصمم الدكت ونصنّعه ونركّبه بأنفسنا.",
              "الفلل، مساحات المعيشة المفتوحة، صالات العرض والمكاتب ذات الأسقف المستعارة",
              ["تصميم الدكت وحساب تدفق الهواء", "وحدة داخلية مخفية ووحدة خارجية مطابقة",
               "تصنيع وتركيب مجاري هواء معزولة", "فتحات التوزيع وشبكات الراجع والفلاتر والثرموستات وأنظمة التحكم",
               "موازنة الهواء والاختبار والتشغيل"],
              "تصميم الدكت الجيد مهم بقدر أهمية الوحدة نفسها. المقاسات الخاطئة تسبب الضجيج وتترك الغرف دافئة.")
svc += f"""<section class="section dark"><div class="wrap">
<div class="head"><div><div class="eyebrow">كيف نعمل</div><h2>نفس الخطوات الدقيقة<br>لكل نظام.</h2></div></div>
{STEPS}</div></section>
<section class="section alt"><div class="wrap">
<div class="cards three">
<div class="card"><div class="ico">{ICON['shield']}</div><h3>دعم خلال الضمان</h3><p>صيانة خلال فترة الضمان لكل نظام نركّبه.</p></div>
<div class="card"><div class="ico">{ICON['tool']}</div><h3>معاينة مجانية للموقع</h3><p>كل مشروع مختلف. نعاين أولاً، ثم نقدّم عرض السعر.</p></div>
<div class="card"><div class="ico">{ICON['users']}</div><h3>متعاونون مع المقاولين</h3><p>نعمل وفق البرنامج الزمني للمقاول الرئيسي وقواعد الموقع.</p></div>
</div></div></section>
{CTA}"""
write("ac-systems.html", svc + FOOT)

# ---------- Contact ----------
ct = head("معاينة مجانية للموقع وعرض سعر للتكييف | حساب للخدمات الفنية دبي",
          f"احجز معاينة مجانية للموقع لتركيب تكييف سبليت أو VRF أو سبليت مخفي في مبناك أو فيلتك الجديدة في دبي أو الشارقة. اتصل أو راسلنا على واتساب {PHONE}.",
          "contact.html", ld(BUSINESS))
ct += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">تواصل معنا</div>
<h1>كل مشروع مختلف.<br><span class="accent-blue">والمعاينة مجانية.</span></h1>
<p>أخبرنا عن مبناك أو فيلتك. نعاين الموقع، ونوصي بالنظام المناسب، ونرسل عرض سعر مكتوباً.</p>
<div class="hero-actions"><a class="btn btn-red" href="#book">احجز معاينة مجانية للموقع</a><a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{WA_ICON} راسلنا على واتساب</a></div></div></section>
<section class="section" id="book"><div class="wrap booking">
<div><div class="eyebrow">معاينة مجانية للموقع</div><h2>أخبرنا عن مشروعك.</h2>
<p>بعض التفاصيل تساعدنا على التحضير للمعاينة. سنتصل بك لتحديد الموعد.</p>
<div class="contact-box">
<p>اتصل</p><a href="{TEL}">{ltr(PHONE)}</a>
<p style="margin-top:16px">واتساب</p><a href="{WA}" target="_blank" rel="noopener">{WA_ICON} راسلنا</a>
<p style="margin-top:16px">البريد الإلكتروني</p><a href="mailto:{EMAIL}" style="font-size:18px">{EMAIL}</a>
<p style="margin-top:16px">دبي، الإمارات العربية المتحدة · مغلق يوم الجمعة</p></div></div>
<div class="form-card">
<form id="booking-form" name="site-inspection" method="POST" action="/ar/thank-you" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="site-inspection">
<input type="hidden" name="subject" value="طلب معاينة جديد من موقع حساب (عربي)">
<p class="hidden"><label>اترك هذا الحقل فارغاً: <input name="bot-field"></label></p>
<div class="grid-2">
<label>الاسم الكامل *<input name="name" required autocomplete="name"></label>
<label>الجوال / واتساب *<input name="phone" type="tel" required autocomplete="tel" placeholder="+971" dir="ltr"></label>
<label>البريد الإلكتروني<input name="email" type="email" autocomplete="email" placeholder="اختياري" dir="ltr"></label>
<label>موقع المشروع *<input name="location" required placeholder="مثال: البرشاء، دبي"></label>
<label>نوع المشروع *<select name="project" required><option value="">اختر</option><option>فيلا</option><option>برج / مبنى متعدد الطوابق</option><option>مبنى تجاري / مكاتب</option><option>مدرسة / حضانة / مبنى عام</option><option>أخرى</option></select></label>
<label>نظام التكييف *<select name="system" id="system" required><option value="">اختر</option><option value="split">تكييف سبليت</option><option value="vrf">نظام VRF / VRV</option><option value="ducted">سبليت مخفي وأعمال الدكت</option><option value="not-sure">لست متأكداً – انصحوني</option></select></label>
<label>مرحلة المشروع<select name="stage"><option value="">اختر</option><option>التصميم / المخططات</option><option>قيد الإنشاء</option><option>الهيكل جاهز</option><option>مرحلة التشطيب</option></select></label>
<label>الطوابق / الغرف<input name="size" placeholder="مثال: أرضي + 2، 6 غرف"></label>
</div>
<label>تفاصيل إضافية *<textarea name="message" rows="4" required placeholder="ماذا تبني، ومتى تحتاج تركيب التكييف؟"></textarea></label>
<label>رابط الموقع على خرائط جوجل<input name="maplink" type="url" placeholder="اختياري – الصق رابط الموقع" dir="ltr"></label>
<label class="check"><input type="checkbox" name="consent" required><span>أوافق على أن تتواصل معي حساب للخدمات الفنية بخصوص هذا الطلب. *</span></label>
<button class="btn btn-red" type="submit">احجز المعاينة المجانية</button>
<p class="form-status" id="form-status" aria-live="polite"></p>
<p class="form-note">نستخدم هذه البيانات فقط للرد على طلبك.</p>
</form></div>
</div></section>
<section class="section alt"><div class="wrap"><div class="eyebrow">أسئلة</div><h2>معلومات تهمّك</h2><div class="faq">{faq_html()}</div></div></section>
"""
write("contact.html", ct + FOOT)

# ---------- Projects ----------
pj = head("مشاريع تكييف منجزة في الشارقة ودبي | حساب للخدمات الفنية",
          "مشاريع تكييف منجزة من حساب للخدمات الفنية: مجلس الحيرة الأدبي، سوق دبا التراثي، حصن فلي، برج حصن الذيد، حضانة ليتل ستبس، فلل ومبانٍ من أرضي + 1 إلى أرضي + 6.",
          "projects.html", ld(BUSINESS))
pj += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">مشاريع منجزة</div>
<h1>معالم تراثية،<br><span class="accent-blue">فلل ومبانٍ جديدة.</span></h1>
<p>12 مشروعاً منجزاً في الشارقة ودبي وأم القيوين والذيد. الصور من سجلات مشاريع حساب.</p></div></section>
<section class="section"><div class="wrap">
<div class="head"><div><div class="eyebrow">جميع المشاريع</div><h2>قائمة المشاريع المنجزة</h2></div><p>من ملف الشركة التعريفي.</p></div>
{ref_cards("")}
</div></section>
<section class="section alt"><div class="wrap">
"""
for key, title, loc, client, imgs in PROJ:
    gal = "".join(f'<img src="{R}assets/projects/{i}.jpg" alt="{a} – {title}، {loc}" loading="lazy">' for i, a in imgs)
    pj += f'<article class="project-block" id="{key}"><div class="eyebrow">مشروع منجز · {len(imgs)} صور</div><h2>{title}</h2><p class="meta">{loc} · العميل: {ltr(client)}</p><div class="gallery">{gal}</div></article>\n'
pj += f"""<p class="note">اضغط على أي صورة لعرضها بحجم أكبر. المزيد على <a class="link" href="{IG}" target="_blank" rel="noopener">إنستغرام</a>.</p>
</div></section>
{CTA}"""
write("projects.html", pj + FOOT)

# ---------- About ----------
ab = head("من نحن | حساب للخدمات الفنية – شركة تركيب تكييف في دبي",
          "حساب للخدمات الفنية ذ.م.م شركة تركيب تكييف في دبي تأسست عام 2023 (رخصة 1229557)، بقيادة مهندس تكييف بخبرة تزيد على 25 عاماً.",
          "about.html", ld(BUSINESS))
white = lambda k: ICON[k].replace('<svg', '<svg style="stroke:#fff"')
ab += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">من نحن</div>
<h1>شريكك الموثوق<br><span class="accent-blue">لحلول التكييف والتهوية.</span></h1>
<p>شركة في دبي تتمحور حول أمر واحد: التكييف في المباني والفلل الجديدة، بالحجم الصحيح والتركيب الصحيح.</p></div></section>
<section class="section"><div class="wrap split">
<div><div class="eyebrow">قصتنا</div><h2>تأسست في دبي عام 2023.</h2>
<p>تأسست حساب للخدمات الفنية ذ.م.م في أغسطس 2023 في دبي، الإمارات العربية المتحدة، وهي مسجلة لدى دائرة الاقتصاد والسياحة في دبي برخصة رقم {ltr("1229557")}.</p>
<p>نصمم ونورّد ونركّب تكييف سبليت وأنظمة VRF/VRV والسبليت المخفي مع أعمال الدكت للمباني والأبراج والفلل الجديدة في دبي والشارقة، بما في ذلك المعالم التراثية والمباني متعددة الطوابق.</p></div>
<img src="{R}assets/projects/heera-exterior.jpg" alt="مبنى مجلس الحيرة الأدبي في الشارقة، أحد مشاريع حساب" loading="lazy" width="560" height="690" style="aspect-ratio:4/4.4">
</div></section>
<section class="section alt"><div class="wrap">
<div class="eyebrow">القيادة</div><h2>خبرة هندسية،<br>وانضباط في الإدارة.</h2>
<div class="people">
<div class="person"><small>الشريك المؤسس</small><h3>م. محمد رفيق عطار</h3><p>أكثر من 25 عاماً في مجال التكييف والتهوية، شملت العمل مع شركات راسخة في الإمارات. يقود الجانب الفني: تصميم الأنظمة وتركيبها.</p></div>
<div class="person"><small>الشريك المؤسس والمدير العام</small><h3>محمد سعادت شفقت، {ltr("ACA")}</h3><p>محاسب قانوني وعضو في معهد المحاسبين القانونيين في باكستان (ICAP)، بخبرة تزيد على 10 سنوات في المحاسبة. يدير الشؤون المالية والتشغيلية.</p></div>
</div></div></section>
{team_section()}
<section class="section"><div class="wrap split">
<div><div class="eyebrow">رؤيتنا</div><h2>شريك التكييف الذي يعود إليه المقاولون.</h2><p>أن نكون شريكاً موثوقاً لحلول التكييف والتهوية لعملائنا في القطاعين التجاري والسكني.</p></div>
<div><div class="eyebrow">رسالتنا</div><h2>عمل عالي الجودة بسعر عادل.</h2><p>أن نقدم لعملائنا تكييفاً عالي الجودة ضمن ميزانية اقتصادية، لنخفف العبء عنهم وهم يبنون منازلهم وأعمالهم.</p></div>
</div></section>
<section class="section dark"><div class="wrap">
<div class="eyebrow">مبادئنا</div><h2>أربعة مبادئ. في كل عمل.</h2>
<div class="cards">
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('shield')}</div><h3>النزاهة</h3><p>عروض أسعار واضحة، ونصيحة صادقة، والتزامات يمكن الاعتماد عليها.</p></div>
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('tool')}</div><h3>الجودة</h3><p>تركيب دقيق، واختبار سليم، وتسليم نظيف.</p></div>
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('leaf')}</div><h3>السلامة</h3><p>معدات السلامة، وأساليب عمل آمنة، واحترام قواعد الموقع.</p></div>
<div class="card"><div class="ico" style="background:rgba(255,255,255,.1)">{white('users')}</div><h3>العمل الجماعي</h3><p>فريق واحد منسّق من المعاينة حتى التسليم.</p></div>
</div></div></section>
{CTA}"""
write("about.html", ab + FOOT)

# ---------- Thank you ----------
ty = head("شكراً لك | حساب للخدمات الفنية", "تم إرسال طلبك إلى حساب للخدمات الفنية.", "thank-you.html", '<meta name="robots" content="noindex">\n')
ty += f"""<section class="page-hero"><div class="wrap"><div class="eyebrow">تم استلام الطلب</div><h1>شكراً لك.<br><span class="accent-blue">سنتصل بك قريباً.</span></h1>
<p>سيتواصل معك فريقنا لتحديد موعد المعاينة المجانية للموقع. تحتاجنا بشكل أسرع؟ اتصل أو راسلنا على واتساب {ltr(PHONE)}.</p>
<div class="hero-actions"><a class="btn btn-red" href="{WA}" target="_blank" rel="noopener">{WA_ICON} راسلنا على واتساب</a><a class="btn btn-ghost" href="index.html">العودة إلى الرئيسية</a></div></div></section>"""
write("thank-you.html", ty + FOOT)

# ---------- sitemap (both languages) ----------
pages = ["", "ac-systems", "projects", "about", "contact"]
def url_entry(p):
    en, ar = f"{SITE}/{p}", f"{SITE}/ar/{p}"
    links = f'<xhtml:link rel="alternate" hreflang="en" href="{en}"/><xhtml:link rel="alternate" hreflang="ar" href="{ar}"/>'
    return f"  <url><loc>{en}</loc>{links}</url>\n  <url><loc>{ar}</loc>{links}</url>\n"
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "".join(url_entry(p) for p in pages) + "</urlset>\n")
print("built ar")
