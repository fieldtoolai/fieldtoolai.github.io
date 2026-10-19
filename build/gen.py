import os, html, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import G, TRADES, GENERAL_BLURB
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "Field Tool AI"
DOMAIN = "https://fieldtoolai.com"
EMAIL = "leonisas2026@gmail.com"
CHECKED = "October 2026"
e = html.escape

def page(path, title, desc, body, depth=0, active=""):
    p = "/" if depth < 0 else "../" * depth  # depth=-1: root-absolute (404 page served at any path)
    canon = DOMAIN + "/" + (path[:-10] if path.endswith("index.html") else path)
    nav = "".join(f'<li><a href="{p}{href}"{" aria-current=\"page\"" if active==k else ""}>{lbl}</a></li>'
                  for k, href, lbl in [("trades","index.html#trades","Trades"),("about","about.html","How we pick"),("newsletter","index.html#newsletter","Newsletter")])
    html_ = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta name="theme-color" content="#0f172a">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🧰</text></svg>">
<link rel="stylesheet" href="{p}css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="nav container" aria-label="Main">
    <a class="logo" href="{p}index.html">Field<span>Tool</span> <em>AI</em></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Menu">☰</button>
    <ul id="nav-links">{nav}<li><a class="cta-nav" href="{p}advertise.html"{" aria-current=\"page\"" if active=="advertise" else ""}>Advertise</a></li></ul>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div><a class="logo" href="{p}index.html">Field<span>Tool</span> <em>AI</em></a>
    <p>Plain-English guides to the AI tools worth a look for your trade.</p></div>
    <div><h2>Trades</h2><ul>{"".join(f'<li><a href="{p}trades/{t["slug"]}.html">{e(t["name"])}</a></li>' for t in TRADES)}</ul></div>
    <div><h2>Site</h2><ul><li><a href="{p}about.html">How we pick tools</a></li><li><a href="{p}about.html#disclosure">Affiliate disclosure</a></li><li><a href="{p}advertise.html">Advertise / Sponsor</a></li><li><a href="{p}privacy.html">Privacy</a></li></ul></div>
  </div>
  <p class="container fine">© 2026 {NAME}. Tool names and trademarks belong to their owners. We are not affiliated with any tool listed unless marked “Sponsor”. Listings last checked {CHECKED}.</p>
</footer>
<script src="{p}js/main.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html_)

def sponsor_slot(where="directory"):
    return f'''<aside class="sponsor-slot" aria-label="Sponsor placement">
  <span class="badge">Sponsor spot available</span>
  <div><h3>Your AI tool could be featured here</h3>
  <p>One clearly labeled sponsor placement at the top of the {where}, plus a mention in the newsletter.</p></div>
  <a class="btn primary" href="{{p}}advertise.html">Learn about sponsoring</a>
</aside>'''

def newsletter(p=""):
    return f'''<section id="newsletter" class="section newsletter" aria-labelledby="nl-h">
  <div class="container narrow">
    <h2 id="nl-h">One useful AI tool for your trade, every week</h2>
    <p>A short email with tools we checked, what they're good for, and what to skip. No hype.</p>
    <form class="newsletter-form" novalidate>
      <label class="sr-only" for="nl-email">Email address</label>
      <input id="nl-email" type="email" name="email" placeholder="you@yourbusiness.com" required autocomplete="email">
      <label class="sr-only" for="nl-trade">Your trade</label>
      <select id="nl-trade" name="trade"><option value="">Your trade (optional)</option>{"".join(f'<option value="{t["slug"]}">{e(t["name"])}</option>' for t in TRADES)}<option value="other">Other</option></select>
      <button class="btn primary" type="submit">Subscribe</button>
    </form>
    <p class="note" role="status" aria-live="polite">Signup isn't live yet. This form doesn't store or send your email.</p>
  </div>
</section>'''

# ---------- Home ----------
cards = "".join(f'''<a class="trade-card" href="trades/{t["slug"]}.html">
  <span class="icon" aria-hidden="true">{t["icon"]}</span>
  <h3>{e(t["name"])}</h3>
  <p>{len(t["tools"])} tools checked</p>
  <span class="arrow" aria-hidden="true">→</span></a>''' for t in TRADES)
gen_cards = "".join(f'''<div class="tool-card compact"><h3><a href="{G[k][1]}" target="_blank" rel="noopener">{e(G[k][0])}</a></h3><span class="tag">{e(G[k][2])}</span><p>{e(GENERAL_BLURB[k])}</p></div>''' for k in ["chatgpt","claude","gemini","copilot","canva","grammarly","otter","fyxer"])
home = f'''<section class="hero">
  <div class="container">
    <p class="eyebrow">For plumbers, salons, restaurants, realtors and every trade in between</p>
    <h1>The AI tools worth using in <span class="hl">your</span> line of work</h1>
    <p class="sub">Real tools, checked against their official sites, explained in plain English by trade. Find what saves you time on calls, quotes, bookings and books.</p>
    <div class="hero-actions">
      <a href="#trades" class="btn primary">Find tools for my trade</a>
      <a href="#newsletter" class="btn ghost">Get the weekly email</a>
    </div>
    <ul class="trust"><li>✓ Every link goes to the official site</li><li>✓ No made-up reviews or stats</li><li>✓ Sponsors always labeled</li></ul>
  </div>
</section>
<section class="section"><div class="container">
{sponsor_slot("directory").replace("{p}","")}
</div></section>
<section id="trades" class="section alt" aria-labelledby="trades-h"><div class="container">
  <h2 id="trades-h">Browse by trade</h2>
  <p class="section-desc">Pick your trade to see AI tools built for that work, and what you'd actually use each one for.</p>
  <div class="trade-grid">{cards}</div>
</div></section>
<section class="section" aria-labelledby="gen-h"><div class="container">
  <h2 id="gen-h">General AI tools that work for any trade</h2>
  <p class="section-desc">Start here if you've never used AI for your business. These handle writing, design, notes and email for almost anyone.</p>
  <div class="tool-grid">{gen_cards}</div>
</div></section>
<section class="section alt" aria-labelledby="how-h"><div class="container">
  <h2 id="how-h">How we build this list</h2>
  <div class="steps">
    <div><span>1</span><h3>Real tools only</h3><p>Every tool is a live product. We open its official site before listing it.</p></div>
    <div><span>2</span><h3>What it does for you</h3><p>We describe the AI features the company itself lists, applied to everyday jobs in your trade.</p></div>
    <div><span>3</span><h3>No invented numbers</h3><p>No made-up prices, ratings or user counts. Check the official site for current pricing.</p></div>
  </div>
  <p><a href="about.html">Read our full methodology →</a></p>
</div></section>
{newsletter()}'''
page("index.html", f"{NAME}: AI Tools for Small Businesses, by Trade",
     "Find the AI tools worth using for your small business. Plain-English guides by trade for plumbers, HVAC, realtors, salons, restaurants, contractors, accountants, retail and cleaners.",
     home, 0)

# ---------- Trade pages ----------
for t in TRADES:
    items = []
    for i, tool in enumerate(t["tools"]):
        n, url, cat, desc = tool[:4]
        extra = f' <a href="{tool[4]}" target="_blank" rel="noopener">More on the AI assistant</a>.' if len(tool) > 4 else ""
        items.append(f'''<li class="tool-card" id="{n.lower().replace(' ','-').replace('.','')}">
  <div class="tool-head"><h3>{e(n)}</h3><span class="tag">{e(cat)}</span></div>
  <p>{e(desc)}{extra}</p>
  <a class="tool-link" href="{url}" target="_blank" rel="noopener">Visit {e(n)} official site ↗</a>
</li>''')
    gens = "".join(f'<li><a href="{G[k][1]}" target="_blank" rel="noopener">{e(G[k][0])}</a>: {e(GENERAL_BLURB[k])}</li>' for k in t["general"])
    others = "".join(f'<li><a href="{o["slug"]}.html">{o["icon"]} {e(o["name"])}</a></li>' for o in TRADES if o is not t)
    ld = {"@context":"https://schema.org","@type":"ItemList","name":t["title"],
          "itemListElement":[{"@type":"ListItem","position":i+1,"name":x[0],"url":x[1]} for i,x in enumerate(t["tools"])]}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":t["name"],"item":f"{DOMAIN}/trades/{t['slug']}.html"}]}
    body = f'''<section class="page-hero"><div class="container">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <span>{e(t["name"])}</span></nav>
  <h1><span aria-hidden="true">{t["icon"]}</span> {e(t["title"])}</h1>
  <p class="sub">{e(t["intro"])}</p>
  <p class="meta">{len(t["tools"])} tools · Listings checked {CHECKED} · Not a ranking: order doesn't mean better</p>
</div></section>
<section class="section"><div class="container">
{sponsor_slot(t["name"] + " list").replace("{p}","../")}
  <h2>AI tools for {e(t["name"])}</h2>
  <ol class="tool-list">{"".join(items)}</ol>
  <div class="callout"><h2>Also useful: general AI assistants</h2><ul>{gens}</ul></div>
  <p class="disclaimer">Features change fast. Descriptions are based on what each company's official website showed in {CHECKED}. Check current features and pricing on their site before you buy. Some links may become affiliate links; see our <a href="../about.html#disclosure">disclosure</a>.</p>
</div></section>
<section class="section alt"><div class="container"><h2>Other trades</h2><ul class="chip-list">{others}</ul></div></section>
{newsletter()}
<script type="application/ld+json">{json.dumps(ld)}</script>
<script type="application/ld+json">{json.dumps(crumbs)}</script>'''
    page(f"trades/{t['slug']}.html", f"{t['title']} ({CHECKED}) | {NAME}",
         f"{t['intro']} {len(t['tools'])} real tools, checked {CHECKED}, with what each one is good for."[:300],
         body, 1, "trades")

# ---------- Advertise ----------
adv = f'''<section class="page-hero"><div class="container">
  <h1>Advertise or sponsor on {NAME}</h1>
  <p class="sub">Reach small business owners who are actively looking for AI tools for their trade.</p>
</div></section>
<section class="section"><div class="container">
  <h2>Sponsorship options</h2>
  <div class="tool-grid">
    <div class="tool-card"><h3>Featured directory spot</h3><p>A clearly labeled “Sponsor” placement at the top of the home page directory.</p></div>
    <div class="tool-card"><h3>Trade page sponsor</h3><p>Top placement on one trade page (for example, Restaurants or Contractors), so you reach exactly the businesses your tool is built for.</p></div>
    <div class="tool-card"><h3>Newsletter sponsor</h3><p>A sponsored slot in the weekly email, marked as sponsored.</p></div>
    <div class="tool-card"><h3>Bundles</h3><p>Combine directory, trade page and newsletter placements.</p></div>
  </div>
  <h2 class="mt">Rates</h2>
  <p><strong>Contact for rates.</strong> We're a new site, so we'll share current audience numbers with you directly instead of quoting figures here.</p>
  <h2 class="mt">Our rules</h2>
  <ul class="list">
    <li>Sponsored placements are always labeled “Sponsor”.</li>
    <li>Sponsors don't change our descriptions of other tools, and sponsorship doesn't buy a regular listing.</li>
    <li>We only feature real, working products that are relevant to small businesses.</li>
  </ul>
  <div class="callout"><h2>Get in touch</h2><p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> for sponsor options and current rates.</p></div>
</div></section>'''
page("advertise.html", f"Advertise / Sponsor | {NAME}",
     f"Sponsor options on {NAME}: featured directory placement, trade page sponsorship and newsletter sponsorship. Contact for rates.", adv, 0, "advertise")

# ---------- About ----------
about = f'''<section class="page-hero"><div class="container"><h1>How we pick tools</h1>
<p class="sub">What gets listed, how we describe it, and how the site makes money.</p></div></section>
<section class="section"><div class="container narrow prose">
  <h2>What we list</h2>
  <p>Only real products with a working official website. Before a tool goes on a trade page, we open its official site and confirm the product exists and offers the AI features we mention.</p>
  <h2>How we describe tools</h2>
  <p>Each description says what the company itself says the tool does, then explains how a business in that trade would use it. We don't invent prices, ratings, user numbers or testimonials. The order on a page isn't a ranking.</p>
  <h2>Updates</h2>
  <p>AI tools change quickly. Each page shows when it was last checked (currently {CHECKED}). Always confirm current features and pricing on the official site.</p>
  <h2 id="disclosure">Affiliate & sponsor disclosure</h2>
  <p>{NAME} is free to use. We may earn money from affiliate links (if you sign up through a link, we may earn a commission at no extra cost to you) and from sponsors. Sponsored placements are always labeled “Sponsor”. Affiliate deals and sponsorships don't change how we describe tools.</p>
  <h2>Spot a mistake?</h2>
  <p>If a listing is out of date, email us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>'''
page("about.html", f"How We Pick AI Tools & Affiliate Disclosure | {NAME}",
     f"How {NAME} checks and describes AI tools for small businesses, and how the site is funded through sponsors and affiliate links.", about, 0, "about")

priv = f'''<section class="page-hero"><div class="container"><h1>Privacy</h1></div></section>
<section class="section"><div class="container narrow prose">
<p>This early version of {NAME} doesn't collect personal information. The newsletter form isn't connected to any service yet and doesn't store what you type.</p>
<p>When we connect a newsletter service or analytics, we'll update this page to explain what's collected and why.</p>
<p><em>Last updated {CHECKED}.</em></p></div></section>'''
page("privacy.html", f"Privacy | {NAME}", f"Privacy information for {NAME}.", priv, 0)

nf = '''<section class="page-hero"><div class="container"><h1>Page not found</h1><p class="sub">That page doesn't exist. <a href="/index.html">Go to the home page</a>.</p></div></section>'''
page("404.html", f"Page not found | {NAME}", "Page not found.", nf, -1)

# ---------- SEO files ----------
urls = ["", "advertise.html", "about.html", "privacy.html"] + [f"trades/{t['slug']}.html" for t in TRADES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{DOMAIN}/{u}</loc><lastmod>2026-10-15</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
llms = [f"# {NAME}", "", f"> {NAME} is a free directory of real AI tools for small businesses, organized by trade. Each listing links to the tool's official site and explains, in plain English, how a business in that trade would use it. Listings were checked against official sites in {CHECKED}. No pricing, ratings or usage statistics are invented; order on a page is not a ranking. Sponsored placements are labeled.", "", "## Trades"]
for t in TRADES:
    llms.append(f"- [{t['title']}]({DOMAIN}/trades/{t['slug']}.html): " + ", ".join(x[0] for x in t["tools"]))
llms += ["", "## General AI tools for any trade"] + [f"- [{G[k][0]}]({G[k][1]}): {GENERAL_BLURB[k]}" for k in ["chatgpt","claude","gemini","copilot","canva","grammarly","otter","fyxer"]]
llms += ["", "## About", f"- [How we pick tools and affiliate disclosure]({DOMAIN}/about.html)", f"- [Advertise / Sponsor]({DOMAIN}/advertise.html): featured directory, trade page and newsletter sponsorships; contact for rates."]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms) + "\n")
open(os.path.join(ROOT, "vercel.json"), "w").write(json.dumps({"cleanUrls": False, "trailingSlash": False}, indent=2) + "\n")
print("built", len(urls), "pages")
