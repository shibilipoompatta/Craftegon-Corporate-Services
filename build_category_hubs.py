# -*- coding: utf-8 -*-
"""
Generates the remaining 4 Category Hub pages:
- gst-advisory/index.html
- direct-tax/index.html
- brand-protection/index.html
- workforce-digital/index.html
"""
import os
import json

MANDATORY_DISCLAIMER = """<p class="text-xs text-gray-400 leading-relaxed">
  <strong class="text-gold">Regulatory Notice:</strong> CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform. CCS is not a law firm and does not provide court litigation or judicial representation. All court litigation and tribunal appearances are executed exclusively through independent, licensed advocates or associate law firms (such as Everest Law Firm) in accordance with the Advocates Act, 1961. Statutory audits, tax certifications, and regulated professional services are fulfilled by qualified, independent Chartered Accountants, Company Secretaries, and registered professionals in compliance with ICAI, ICSI, and statutory guidelines.
</p>"""

NAV_HTML = """<header class="sticky top-0 z-50 bg-[#0e1712] border-b border-white/10 shadow-lg backdrop-blur-md">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
    <a href="/" class="flex items-center space-x-3">
      <span class="font-serif text-2xl font-bold tracking-wider text-white">Craft<span class="text-[#c5a059]">Egon</span></span>
      <span class="text-[10px] font-mono tracking-widest uppercase bg-[#c5a059]/20 text-[#c5a059] px-2 py-0.5 rounded border border-[#c5a059]/40">Corporate Services</span>
    </a>
    <nav class="hidden lg:flex items-center space-x-6 text-sm font-medium text-gray-200">
      <a href="/business-setup/" class="hover:text-[#c5a059] transition">Business Setup</a>
      <a href="/gst-advisory/" class="hover:text-[#c5a059] transition">GST Advisory</a>
      <a href="/corporate-governance/" class="hover:text-[#c5a059] transition">Governance & MCA</a>
      <a href="/direct-tax/" class="hover:text-[#c5a059] transition">Direct Tax</a>
      <a href="/brand-protection/" class="hover:text-[#c5a059] transition">Brand & IP</a>
      <a href="/workforce-digital/" class="hover:text-[#c5a059] transition">Workforce & Digital</a>
    </nav>
    <div class="hidden sm:flex items-center space-x-4">
      <a href="https://wa.me/919995204905" target="_blank" class="text-sm font-medium text-gray-300 hover:text-white flex items-center gap-1.5">
        <i data-lucide="message-square" class="w-4 h-4 text-[#c5a059]"></i>
        <span>WhatsApp</span>
      </a>
      <a href="#inquiry" class="bg-[#c5a059] hover:bg-[#c59b27] text-[#0e1712] font-semibold text-sm px-4 py-2.5 rounded-lg transition shadow-md">
        Get Consultation
      </a>
    </div>
    <button id="mobile-menu-btn" class="lg:hidden text-gray-300 hover:text-white p-2">
      <i data-lucide="menu" class="w-6 h-6"></i>
    </button>
  </div>
  <div id="mobile-menu" class="hidden lg:hidden bg-[#090d16] border-b border-white/10 px-4 py-4 space-y-3">
    <a href="/business-setup/" class="block text-gray-200 hover:text-[#c5a059]">Business Setup</a>
    <a href="/gst-advisory/" class="block text-gray-200 hover:text-[#c5a059]">GST Advisory</a>
    <a href="/corporate-governance/" class="block text-gray-200 hover:text-[#c5a059]">Corporate Governance</a>
    <a href="/direct-tax/" class="block text-gray-200 hover:text-[#c5a059]">Direct Tax</a>
    <a href="/brand-protection/" class="block text-gray-200 hover:text-[#c5a059]">Brand Protection</a>
    <a href="/workforce-digital/" class="block text-gray-200 hover:text-[#c5a059]">Workforce & Digital</a>
    <a href="#inquiry" class="block w-full text-center bg-[#c5a059] text-[#0e1712] py-2 rounded font-semibold mt-2">Get Free Consultation</a>
  </div>
</header>"""

FOOTER_HTML = f"""<footer class="bg-[#090d16] text-gray-300 pt-16 pb-12 border-t border-white/10">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 mb-12">
      <div class="lg:col-span-2 space-y-4">
        <a href="/" class="flex items-center space-x-3">
          <span class="font-serif text-2xl font-bold tracking-wider text-white">Craft<span class="text-[#c5a059]">Egon</span></span>
          <span class="text-[10px] font-mono tracking-widest uppercase bg-[#c5a059]/20 text-[#c5a059] px-2 py-0.5 rounded border border-[#c5a059]/40">Corporate Services</span>
        </a>
        <p class="text-sm text-gray-400 max-w-sm leading-relaxed">
          India's enterprise legal-technology, corporate governance, and indirect tax operations platform. Orchestrating statutory precision for modern businesses.
        </p>
        <div class="pt-2 text-sm text-gray-300 space-y-1.5">
          <p><span class="text-[#c5a059] font-medium">Headquarters:</span> Technopark, Trivandrum, Kerala, India</p>
          <p><span class="text-[#c5a059] font-medium">Corporate Desk:</span> support@craftegon.com | +91 99952 04905</p>
        </div>
      </div>
      <div>
        <h4 class="font-serif text-white font-semibold mb-4 text-sm tracking-wider uppercase text-[#c5a059]">Service Verticals</h4>
        <ul class="space-y-2 text-sm">
          <li><a href="/business-setup/" class="hover:text-[#c5a059] transition">Business Setup</a></li>
          <li><a href="/gst-advisory/" class="hover:text-[#c5a059] transition">GST & Indirect Tax</a></li>
          <li><a href="/corporate-governance/" class="hover:text-[#c5a059] transition">Corporate Governance</a></li>
          <li><a href="/direct-tax/" class="hover:text-[#c5a059] transition">Direct Tax & TDS</a></li>
          <li><a href="/brand-protection/" class="hover:text-[#c5a059] transition">Brand Protection</a></li>
          <li><a href="/workforce-digital/" class="hover:text-[#c5a059] transition">Workforce & Digital</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-serif text-white font-semibold mb-4 text-sm tracking-wider uppercase text-[#c5a059]">Core Highlights</h4>
        <ul class="space-y-2 text-sm">
          <li><a href="/business-setup/private-limited-company-incorporation/" class="hover:text-[#c5a059] transition">Pvt Ltd Incorporation</a></li>
          <li><a href="/business-setup/llp-registration/" class="hover:text-[#c5a059] transition">LLP Registration</a></li>
          <li><a href="/gst-advisory/gst-registration/" class="hover:text-[#c5a059] transition">GST Registration</a></li>
          <li><a href="/corporate-governance/annual-mca-roc-filings/" class="hover:text-[#c5a059] transition">Annual ROC Filings</a></li>
          <li><a href="/brand-protection/trademark-registration-filing/" class="hover:text-[#c5a059] transition">Trademark Filing</a></li>
          <li><a href="/workforce-digital/dpdp-act-data-privacy-readiness/" class="hover:text-[#c5a059] transition">DPDP Act Compliance</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-serif text-white font-semibold mb-4 text-sm tracking-wider uppercase text-[#c5a059]">Direct Checkout</h4>
        <p class="text-xs text-gray-400 mb-3">Instant statutory case desk via WhatsApp Business Channel:</p>
        <a href="https://wa.me/919995204905" target="_blank" class="inline-flex items-center gap-2 bg-[#25D366]/20 border border-[#25D366]/40 text-[#25D366] hover:bg-[#25D366]/30 px-3.5 py-2 rounded text-xs font-semibold transition">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>Direct WhatsApp Case Desk</span>
        </a>
      </div>
    </div>
    <div class="border-t border-white/10 pt-8 mt-8">
      {MANDATORY_DISCLAIMER}
      <div class="mt-6 flex flex-col sm:flex-row justify-between items-center text-xs text-gray-500">
        <p>&copy; 2026 CraftEgon Corporate Services Platform. All rights reserved.</p>
        <p class="mt-2 sm:mt-0 font-mono">corporateservices.craftegon.com</p>
      </div>
    </div>
  </div>
</footer>"""

def render_category_hub(cat_slug, title, subtitle, badges, hero_disclaimer, intro_text, services, packages, faqs):
    # JSON-LD FAQ
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            } for q, a in faqs
        ]
    }
    
    # Render Services Grid
    services_cards = []
    for s in services:
        link_target = s.get("product_path") if s.get("phase") == 1 else "#inquiry"
        link_label = "View Execution Process &rarr;" if s.get("phase") == 1 else "Inquire for Service &rarr;"
        fee_badge = f"From ₹{s['pricing']['base_professional_fee']:,}"
        time_badge = s.get("turnaround_time", "Statutory Timeline")
        card = f"""
        <div class="bg-white rounded-xl p-6 border border-gray-200/80 shadow-sm hover:shadow-md hover:border-[#c5a059]/60 transition flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-lg bg-[#0e1712] text-[#c5a059]">
                <i data-lucide="{s.get('icon', 'file-text')}" class="w-5 h-5"></i>
              </span>
              <span class="text-xs font-mono px-2.5 py-1 rounded bg-[#f8f9f6] text-[#2e3a33] border border-gray-200">{time_badge}</span>
            </div>
            <h3 class="font-serif text-lg font-bold text-[#0e1712] mb-2">{s['title']}</h3>
            <p class="text-xs text-gray-600 leading-relaxed mb-4">{s['short_description']}</p>
          </div>
          <div class="pt-4 border-t border-gray-100 flex items-center justify-between">
            <span class="font-mono text-sm font-semibold text-[#c5a059]">{fee_badge}</span>
            <a href="{link_target}" class="text-xs font-semibold text-[#0e1712] hover:text-[#c5a059] transition flex items-center gap-1">
              <span>{link_label}</span>
            </a>
          </div>
        </div>
        """
        services_cards.append(card)
        
    services_grid_html = "\n".join(services_cards)
    
    # Render Packages
    package_cards = []
    for p in packages:
        featured_border = "border-2 border-[#c5a059] shadow-lg relative" if p.get("featured") else "border border-gray-200 shadow-sm"
        badge_html = '<span class="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#c5a059] text-[#0e1712] font-mono text-[10px] uppercase font-bold tracking-widest px-3 py-0.5 rounded-full">Most Popular</span>' if p.get("featured") else ""
        items_html = "".join([f'<li class="flex items-start gap-2 text-xs text-gray-700"><i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i><span>{item}</span></li>' for item in p['features']])
        
        card = f"""
        <div class="bg-white rounded-xl p-6 {featured_border} flex flex-col justify-between">
          {badge_html}
          <div>
            <div class="mb-4">
              <span class="font-mono text-xs text-[#c5a059] uppercase tracking-wider font-semibold">{p['tier']}</span>
              <h3 class="font-serif text-xl font-bold text-[#0e1712] mt-1">{p['name']}</h3>
              <p class="text-xs text-gray-500 mt-1">{p['description']}</p>
            </div>
            <div class="py-4 border-y border-gray-100 mb-6">
              <span class="font-serif text-3xl font-extrabold text-[#0e1712]">₹{p['price']:,}</span>
              <span class="text-xs text-gray-500"> {p['period']}</span>
            </div>
            <ul class="space-y-2.5 mb-6">
              {items_html}
            </ul>
          </div>
          <a href="#inquiry" class="w-full text-center py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition {'bg-[#c5a059] hover:bg-[#c59b27] text-[#0e1712]' if p.get('featured') else 'bg-[#0e1712] hover:bg-black text-white'}">
            Select Package &rarr;
          </a>
        </div>
        """
        package_cards.append(card)
        
    packages_grid_html = "\n".join(package_cards)
    
    # Render FAQs
    faq_items = []
    for idx, (q, a) in enumerate(faqs):
        faq_items.append(f"""
        <div class="border border-gray-200 rounded-lg overflow-hidden bg-white">
          <button class="w-full text-left px-5 py-4 flex items-center justify-between font-serif text-sm font-semibold text-[#0e1712] focus:outline-none faq-btn" data-faq-target="faq-{cat_slug}-{idx}">
            <span>{q}</span>
            <i data-lucide="chevron-down" class="w-4 h-4 text-[#c5a059] transition-transform duration-200"></i>
          </button>
          <div id="faq-{cat_slug}-{idx}" class="hidden px-5 pb-4 text-xs text-gray-600 leading-relaxed border-t border-gray-100 pt-3">
            {a}
          </div>
        </div>
        """)
    faqs_html = "\n".join(faq_items)
    
    badges_html = "".join([f'<span class="px-3 py-1 rounded-full bg-white/10 text-white/90 border border-white/15 text-xs font-mono">{b}</span>' for b in badges])

    disclaimer_hero_badge = ""
    if hero_disclaimer:
        disclaimer_hero_badge = f"""
        <div class="max-w-4xl mx-auto mb-6 p-3 rounded-lg bg-amber-950/40 border border-amber-500/40 text-amber-200 text-xs flex items-center gap-2.5">
          <i data-lucide="shield-alert" class="w-5 h-5 text-amber-400 shrink-0"></i>
          <span><strong>Statutory Practice Clarification:</strong> {hero_disclaimer}</span>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | CraftEgon Corporate Services</title>
  <meta name="description" content="{subtitle}" />
  <link rel="canonical" href="https://corporateservices.craftegon.com/{cat_slug}/" />
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=DM+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Manrope', 'sans-serif'],
            serif: ['Cinzel', 'serif'],
            mono: ['DM Mono', 'monospace'],
          }},
          colors: {{
            gold: {{ DEFAULT: '#c5a059', deep: '#c59b27' }},
            dark: {{ DEFAULT: '#0e1712', alt: '#090d16' }},
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="/assets/css/theme.css" />
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- Schema.org FAQ -->
  <script type="application/ld+json">
  {json.dumps(faq_schema, indent=2)}
  </script>
</head>
<body class="bg-[#f8f9f6] text-[#2e3a33] font-sans antialiased">

{NAV_HTML}

<!-- HERO SECTION -->
<section class="bg-[#0e1712] text-white pt-14 pb-20 border-b border-white/10 relative overflow-hidden">
  <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#c5a059_1px,transparent_1px)] [background-size:16px_16px]"></div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <nav class="flex items-center space-x-2 text-xs font-mono text-gray-400 mb-6">
      <a href="/" class="hover:text-white transition">Home</a>
      <span>/</span>
      <span class="text-[#c5a059] uppercase">{cat_slug.replace('-', ' ')}</span>
    </nav>
    
    <div class="flex flex-wrap gap-2 mb-6">
      {badges_html}
    </div>
    
    <h1 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-white max-w-4xl leading-tight mb-4">
      {title}
    </h1>
    
    <p class="text-sm sm:text-base text-gray-300 max-w-3xl leading-relaxed mb-6">
      {subtitle}
    </p>
    
    {disclaimer_hero_badge}
    
    <div class="flex flex-wrap items-center gap-4">
      <a href="#services-view" class="bg-[#c5a059] hover:bg-[#c59b27] text-[#0e1712] font-semibold text-xs uppercase tracking-wider px-6 py-3 rounded-lg transition shadow-md">
        Explore Services &amp; Fees &darr;
      </a>
      <a href="#inquiry" class="bg-white/10 hover:bg-white/15 text-white font-semibold text-xs uppercase tracking-wider px-6 py-3 rounded-lg border border-white/20 transition">
        Talk to a Specialist
      </a>
    </div>
  </div>
</section>

<!-- MAIN SECTION: DUAL-MODE VIEW SWITCHER -->
<section id="services-view" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
    <div>
      <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Catalog &amp; Retainers</span>
      <h2 class="font-serif text-2xl sm:text-3xl font-bold text-[#0e1712] mt-1">Service Execution Models</h2>
      <p class="text-xs text-gray-500 mt-1">Choose between independent a la carte solutions or comprehensive operational retainers.</p>
    </div>
    
    <!-- View Switcher -->
    <div class="inline-flex p-1 bg-gray-200/80 rounded-xl border border-gray-300">
      <button id="btn-mode-alacarte" class="px-4 py-2 rounded-lg text-xs font-bold transition bg-[#0e1712] text-white shadow-sm">
        A La Carte Services (10)
      </button>
      <button id="btn-mode-packages" class="px-4 py-2 rounded-lg text-xs font-bold transition text-gray-700 hover:text-black">
        Package Bundles &amp; Retainers (3)
      </button>
    </div>
  </div>

  <!-- A LA CARTE VIEW -->
  <div id="view-alacarte" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {services_grid_html}
  </div>

  <!-- PACKAGES VIEW -->
  <div id="view-packages" class="hidden grid grid-cols-1 md:grid-cols-3 gap-8">
    {packages_grid_html}
  </div>
</section>

<!-- INTERACTIVE CALCULATOR SECTION -->
<section class="py-16 bg-[#0e1712] text-white border-y border-white/10">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-10">
      <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Dynamic Pricing Engine</span>
      <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white mt-1">Interactive Statutory Fee Calculator</h2>
      <p class="text-xs text-gray-400 mt-2 max-w-xl mx-auto">
        State stamp duties and statutory registry fees vary across jurisdictions. Calculate your precise compliance investment.
      </p>
    </div>
    
    <div class="bg-[#090d16] border border-white/15 rounded-2xl p-6 sm:p-8 shadow-xl" data-ccs-calculator="{cat_slug}">
      <!-- Calculator mounts here via /assets/js/calculator.js -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label class="block text-xs font-mono uppercase text-gray-400 mb-2">Select State / Jurisdiction</label>
          <select id="calc-state-select" class="w-full bg-[#0e1712] border border-white/20 rounded-lg px-3.5 py-2.5 text-sm text-white focus:border-[#c5a059] focus:outline-none">
            <option value="Maharashtra">Maharashtra</option>
            <option value="Delhi">Delhi</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Kerala" selected>Kerala</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Gujarat">Gujarat</option>
            <option value="Telangana">Telangana</option>
            <option value="Uttar Pradesh">Uttar Pradesh</option>
            <option value="West Bengal">West Bengal</option>
            <option value="Rajasthan">Rajasthan</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-mono uppercase text-gray-400 mb-2">Authorized Capital / Scale</label>
          <select id="calc-capital-select" class="w-full bg-[#0e1712] border border-white/20 rounded-lg px-3.5 py-2.5 text-sm text-white focus:border-[#c5a059] focus:outline-none">
            <option value="100000">₹1,00,000 (Standard Minimum)</option>
            <option value="500000">₹5,00,000</option>
            <option value="1000000" selected>₹10,00,000 (Recommended Startup Base)</option>
            <option value="2500000">₹25,00,000</option>
            <option value="5000000">₹50,00,000</option>
            <option value="10000000">₹1,00,00,000 (1 Crore)</option>
          </select>
        </div>
      </div>
      
      <div class="mt-8 pt-6 border-t border-white/10">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
          <div class="p-3 bg-[#0e1712] rounded-lg border border-white/5">
            <span class="block text-[11px] font-mono text-gray-400 uppercase">Professional Fee</span>
            <span id="calc-prof-fee" class="font-mono text-lg font-bold text-white mt-1 block">₹7,999</span>
          </div>
          <div class="p-3 bg-[#0e1712] rounded-lg border border-white/5">
            <span class="block text-[11px] font-mono text-gray-400 uppercase">State Stamp Duty</span>
            <span id="calc-stamp-duty" class="font-mono text-lg font-bold text-[#c5a059] mt-1 block">₹2,000</span>
          </div>
          <div class="p-3 bg-[#0e1712] rounded-lg border border-white/5">
            <span class="block text-[11px] font-mono text-gray-400 uppercase">GST (18%)</span>
            <span id="calc-gst" class="font-mono text-lg font-bold text-white mt-1 block">₹1,440</span>
          </div>
          <div class="p-3 bg-[#c5a059]/15 rounded-lg border border-[#c5a059]/30">
            <span class="block text-[11px] font-mono text-[#c5a059] uppercase font-bold">Total Investment</span>
            <span id="calc-total" class="font-mono text-lg font-bold text-white mt-1 block">₹11,439</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ SECTION -->
<section class="py-16 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Statutory &amp; Operational FAQ</span>
    <h2 class="font-serif text-2xl sm:text-3xl font-bold text-[#0e1712] mt-1">Frequently Asked Questions</h2>
    <p class="text-xs text-gray-500 mt-1">Key legal citations, compliance timelines, and procedural guidelines.</p>
  </div>
  
  <div class="space-y-3">
    {faqs_html}
  </div>
</section>

<!-- INQUIRY FORM DRAWER -->
<section id="inquiry" class="py-16 bg-[#fcfbf7] border-t border-gray-200">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white rounded-2xl p-8 border border-gray-200 shadow-md">
      <div class="text-center mb-6">
        <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Priority Engagement</span>
        <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1">Initiate Your {title} Mandate</h2>
        <p class="text-xs text-gray-500 mt-1">Submit your specifications. Our legal-tech desk responds within 2 business hours.</p>
      </div>
      
      <form data-ccs-form="true" data-category="{cat_slug}" data-service-id="{cat_slug}-general" class="space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Your Name *</label>
            <input type="text" name="user_name" required placeholder="Shibili Poompatta" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Business Email *</label>
            <input type="email" name="email" required placeholder="shibili@company.com" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
          </div>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Mobile / WhatsApp Number *</label>
            <input type="tel" name="phone" required placeholder="9876543210" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Jurisdiction / State *</label>
            <select name="selected_state" required class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none">
              <!-- Populated by forms.js with fallback -->
              <option value="Kerala">Kerala</option>
              <option value="Maharashtra">Maharashtra</option>
              <option value="Karnataka">Karnataka</option>
              <option value="Delhi">Delhi</option>
              <option value="Tamil Nadu">Tamil Nadu</option>
              <option value="Telangana">Telangana</option>
              <option value="Other">Other States / UT</option>
            </select>
          </div>
        </div>
        
        <div>
          <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Service Requirements / Inquiries</label>
          <textarea name="custom_message" rows="3" placeholder="Briefly describe your company stage, transaction volume, or specific compliance goals..." class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none"></textarea>
        </div>
        
        <button type="submit" class="w-full bg-[#0e1712] hover:bg-black text-[#c5a059] font-bold text-xs uppercase tracking-wider py-3.5 rounded-lg transition shadow-md">
          Submit Mandate Request &rarr;
        </button>
      </form>
    </div>
  </div>
</section>

{FOOTER_HTML}

<!-- SCRIPTS -->
<script src="/assets/js/forms.js"></script>
<script src="/assets/js/calculator.js"></script>
<script>
  // Initialize Lucide Icons
  if (window.lucide) {{ lucide.createIcons(); }}

  // Mobile menu toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (mobileBtn && mobileMenu) {{
    mobileBtn.addEventListener('click', () => {{
      mobileMenu.classList.toggle('hidden');
    }});
  }}

  // Dual-Mode View Switcher
  const btnAlacarte = document.getElementById('btn-mode-alacarte');
  const btnPackages = document.getElementById('btn-mode-packages');
  const viewAlacarte = document.getElementById('view-alacarte');
  const viewPackages = document.getElementById('view-packages');

  if (btnAlacarte && btnPackages && viewAlacarte && viewPackages) {{
    btnAlacarte.addEventListener('click', () => {{
      btnAlacarte.className = 'px-4 py-2 rounded-lg text-xs font-bold transition bg-[#0e1712] text-white shadow-sm';
      btnPackages.className = 'px-4 py-2 rounded-lg text-xs font-bold transition text-gray-700 hover:text-black';
      viewAlacarte.classList.remove('hidden');
      viewPackages.classList.add('hidden');
    }});

    btnPackages.addEventListener('click', () => {{
      btnPackages.className = 'px-4 py-2 rounded-lg text-xs font-bold transition bg-[#0e1712] text-white shadow-sm';
      btnAlacarte.className = 'px-4 py-2 rounded-lg text-xs font-bold transition text-gray-700 hover:text-black';
      viewPackages.classList.remove('hidden');
      viewAlacarte.classList.add('hidden');
    }});
  }}

  // FAQ Accordion
  document.querySelectorAll('.faq-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const targetId = btn.getAttribute('data-faq-target');
      const content = document.getElementById(targetId);
      const icon = btn.querySelector('svg');
      
      if (content) {{
        content.classList.toggle('hidden');
        if (icon) {{
          icon.classList.toggle('rotate-180');
        }}
      }}
    }});
  }});

  // Calculator interaction fallback
  const stateSel = document.getElementById('calc-state-select');
  const capSel = document.getElementById('calc-capital-select');
  function recalc() {{
    if (window.CCSCalculator && window.CCSCalculator.calculateTotalFee) {{
      const res = window.CCSCalculator.calculateTotalFee(7999, stateSel.value, parseInt(capSel.value));
      document.getElementById('calc-prof-fee').textContent = '₹' + res.professional_fee.toLocaleString('en-IN');
      document.getElementById('calc-stamp-duty').textContent = '₹' + res.stamp_duty.toLocaleString('en-IN');
      document.getElementById('calc-gst').textContent = '₹' + res.gst_amount.toLocaleString('en-IN');
      document.getElementById('calc-total').textContent = '₹' + res.total.toLocaleString('en-IN');
    }}
  }}
  if (stateSel && capSel) {{
    stateSel.addEventListener('change', recalc);
    capSel.addEventListener('change', recalc);
  }}
</script>
</body>
</html>
"""
    return html

def main():
    with open("data/services.json", encoding="utf-8") as f:
        data = json.load(f)
    services_by_cat = {}
    for s in data["services"]:
        services_by_cat.setdefault(s["category"], []).append(s)

    # 1. GST Advisory
    gst_faqs = [
        ("Who is mandatorily required to register under GST?", "Under Section 22 of the CGST Act 2017, registration is compulsory when annual turnover exceeds ₹40 Lakhs for goods (₹20 Lakhs in Special Category States) or ₹20 Lakhs for service providers. Compulsory registration without threshold applies to inter-state suppliers, e-commerce vendors, and reverse-charge payers under Section 24."),
        ("What is the difference between GSTR-1 and GSTR-3B?", "GSTR-1 (filed by 11th of every month) is the detailed statutory statement of outward supplies and invoice-level details. GSTR-3B (filed by 20th) is the monthly consolidated summary return where tax liabilities are self-assessed, ITC is credited, and net tax is settled via cash or credit ledger."),
        ("What are the mandatory thresholds for E-Invoicing?", "Under Rule 48(4) of the CGST Rules, electronic invoicing via the Invoice Registration Portal (IRP) is compulsory for all B2B and export transactions of taxpayers whose aggregate turnover exceeds ₹5 Crore in any preceding financial year since 2017-18."),
        ("How does Rule 36(4) impact Input Tax Credit (ITC) reconciliation?", "Input Tax Credit cannot be claimed in GSTR-3B unless invoices are uploaded by vendors and accurately reflected in auto-drafted Form GSTR-2B. Non-matching vendor invoices result in statutory disallowance with interest penalties under Section 50."),
        ("When is the GSTR-9 Annual Return mandatory?", "Filing of annual Form GSTR-9 is compulsory for registered taxpayers with aggregate turnover exceeding ₹2 Crore in the relevant financial year, due by December 31 following the close of the financial year.")
    ]
    gst_packages = [
        {"name": "Starter GST Desk", "tier": "Essential", "price": 3999, "period": "/ month", "description": "Ideal for startups and growing service entities with regular outward supplies.", "features": ["Monthly GSTR-1 & GSTR-3B Filing", "GSTR-2B ITC Matching & Advisory", "PMT-06 Challan Generation", "Annual GSTR-9 Preparation"]},
        {"name": "Growth E-Commerce & Invoicing", "tier": "Scale", "price": 7999, "period": "/ month", "featured": True, "description": "Tailored for mid-market suppliers, manufacturers, and multi-state vendors.", "features": ["All Starter Desk Features", "API E-Invoicing & IRN Generation", "Rule 36(4) Vendor Default Tracking", "Notice Handling (up to 2 notices/yr)", "LUT Export Filing for Zero-Rated Supply"]},
        {"name": "Enterprise Indirect Tax Retainer", "tier": "Enterprise", "price": 14999, "period": "/ month", "description": "Full-scale corporate indirect tax management and reconciliation.", "features": ["All Growth Features Included", "Form GSTR-9C CA Reconciliation Support", "Departmental Audit Support", "Advance Ruling & Appellate Advisory", "Dedicated Senior Tax Architect"]}
    ]
    os.makedirs("gst-advisory", exist_ok=True)
    with open("gst-advisory/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "gst-advisory",
            "GST Registration, Returns & Indirect Tax Advisory",
            "Statutory Indirect Tax Operations Aligned with CGST/SGST Act 2017, E-Invoicing Mandates & GSTR-2B Reconciliations.",
            ["CGST/SGST Act 2017", "GSTR-1 & 3B", "E-Invoicing IRN", "GSTR-9 & 9C", "ITC Rule 36(4)"],
            "Departmental appeals before the Appellate Authority for Advance Rulings (AAAR) and High Courts are executed through licensed independent Advocates and CAs.",
            "Complete GST lifecycle management from initial registration to automated e-invoicing and dispute mitigation.",
            services_by_cat.get("gst-advisory", []),
            gst_packages,
            gst_faqs
        ))
    print("Created gst-advisory/index.html")

    # 2. Direct Tax
    dt_faqs = [
        ("Which ITR form applies to Private Limited Companies and LLPs?", "Private and Public Limited companies mandatorily file Form ITR-6 electronically with a digital signature under Section 139(1). Limited Liability Partnerships file Form ITR-5."),
        ("What are the corporate income tax rates for FY 2024-25 / AY 2025-26?", "Under Section 115BAA, domestic corporate entities can opt for a concessional base tax rate of 22% (effective 25.17% including 10% surcharge and 4% cess), subject to forgoing specific exemptions/deductions. Standard rate remains 25% for companies with turnover up to ₹400 Cr in FY 2022-23."),
        ("When is a Tax Audit under Section 44AB mandatory?", "Tax audit is compulsory when total business sales or turnover exceeds ₹1 Crore. The threshold extends to ₹10 Crore if cash receipts and cash payments do not exceed 5% of aggregate transactions."),
        ("What are the quarterly deadlines for TDS returns?", "TDS returns (Form 24Q for salaries, Form 26Q for non-salaries) are due quarterly: Q1 by July 31, Q2 by October 31, Q3 by January 31, and Q4 by May 31."),
        ("What is Form 15CA and Form 15CB?", "Form 15CA is an online declaration filed by remitters for outbound international payments. Form 15CB is a statutory certification issued by an independent Chartered Accountant verifying taxability and DTAA rates.")
    ]
    dt_packages = [
        {"name": "Startup Direct Tax Retainer", "tier": "Basic", "price": 14999, "period": "/ year", "description": "Complete year-round income tax and quarterly withholding compliance.", "features": ["Corporate Form ITR-6 Filing", "Quarterly TDS (24Q & 26Q) Filing", "Advance Tax Computation (4 Installments)", "Form 26AS & AIS Reconciliation"]},
        {"name": "Growth Corporate Tax Desk", "tier": "Scale", "price": 29999, "period": "/ year", "featured": True, "description": "Designed for funded startups and mid-market entities requiring audit coordination.", "features": ["All Startup Tax Features", "Form 3CD Tax Audit Data Coordination", "TDS Certificates (Form 16/16A) Issuance", "Income Tax Notice Reply Coordination", "Section 115BAA Regime Advisory"]},
        {"name": "Enterprise Cross-Border Tax", "tier": "Enterprise", "price": 59999, "period": "/ year", "description": "Comprehensive corporate tax, transfer pricing, and treaty structuring.", "features": ["All Growth Features Included", "Transfer Pricing Local File Review", "Form 15CA/15CB Remittance Certification", "Permanent Establishment Risk Review", "Dedicated Senior Corporate Tax Specialist"]}
    ]
    os.makedirs("direct-tax", exist_ok=True)
    with open("direct-tax/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "direct-tax",
            "Direct Tax, Corporate ITR & TDS Compliance",
            "Income Tax Act 1961 Structuring, Form ITR-6 Corporate Filings, Quarterly Withholding Tax, and Form 3CD Audit Coordination.",
            ["Income Tax Act 1961", "Form ITR-6", "Section 115BAA", "Form 3CD Audit", "TDS Form 26Q"],
            "Statutory Tax Audits under Section 44AB and Certifications (Form 15CB) are issued exclusively by qualified, independent Chartered Accountants as mandated by ICAI regulations.",
            "Precision direct tax computation and electronic filing for high-growth enterprises.",
            services_by_cat.get("direct-tax", []),
            dt_packages,
            dt_faqs
        ))
    print("Created direct-tax/index.html")

    # 3. Brand Protection
    bp_faqs = [
        ("What is the legal difference between ™ and ® symbols?", "The ™ symbol indicates an unregistered trademark for which an application has been filed or rights are claimed in commerce. The ® symbol can only be legally displayed after the Trade Marks Registry has granted a final Certificate of Registration."),
        ("How does the Nice Classification system operate?", "Trademarks are categorized into 45 international classes: Classes 1 to 34 cover physical goods, and Classes 35 to 45 cover services. SaaS, software, and tech platforms typically protect Classes 9, 35, 38, and 42."),
        ("What constitutes a Section 9 vs Section 11 examination objection?", "Section 9 objections relate to absolute grounds (mark lacks distinctiveness or is purely descriptive of the goods/services). Section 11 objections pertain to relative grounds (identical or deceptively similar to an earlier registered or pending mark)."),
        ("What is the statutory opposition window after journal publication?", "Once advertised in the Trade Marks Journal, a statutory 4-month public opposition window opens under Section 21 of the Trade Marks Act 1999."),
        ("How long does trademark protection remain valid in India?", "A registered trademark is valid for 10 years from the date of application and can be renewed indefinitely every 10 years via Form TM-R.")
    ]
    bp_packages = [
        {"name": "Brand Inception Pack", "tier": "Essential", "price": 9999, "period": "/ mark", "description": "Single-class filing with comprehensive prior art clearance.", "features": ["IP India Database Conflict Search", "Drafting Goods/Services Specification", "Form TM-A Filing with Digital Signature", "TM Symbol Usage Authorization", "Application Status Tracking"]},
        {"name": "Complete Brand Armor", "tier": "Popular", "price": 19999, "period": "/ multi-class", "featured": True, "description": "Dual-class registration with full examination rebuttal guarantee.", "features": ["Filing Across 2 Nice Classes", "Section 9/11 Examination Reply Drafting", "Acquired Distinctiveness Evidence Compilation", "Copyright Filing for Logo/Artistic Work", "Watch Services for 12 Months"]},
        {"name": "Enterprise IP Portfolio Desk", "tier": "Enterprise", "price": 49999, "period": "/ portfolio", "description": "Complete intellectual property orchestration for tech ventures.", "features": ["Up to 5 Trademark Classes Filed", "Comprehensive Patent Search Advisory", "Industrial Design Filing (1 Product)", "Trademark Assignment & Licensing Deeds", "Dedicated Intellectual Property Manager"]}
    ]
    os.makedirs("brand-protection", exist_ok=True)
    with open("brand-protection/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "brand-protection",
            "Brand Protection, Trademarks & Intellectual Property",
            "Comprehensive Intellectual Property Preservation under Trade Marks Act 1999, Copyright Act 1957, and Patents Framework.",
            ["Trade Marks Act 1999", "Nice Classification", "Form TM-A", "Section 9 & 11 Replies", "Copyright Act 1957"],
            "Trademark opposition hearings before the Trade Marks Registry and IPAB/High Court litigation are conducted by licensed Trademark Advocates.",
            "Protecting enterprise branding, source code, and industrial aesthetics.",
            services_by_cat.get("brand-protection", []),
            bp_packages,
            bp_faqs
        ))
    print("Created brand-protection/index.html")

    # 4. Workforce & Digital
    wd_faqs = [
        ("What are the key corporate obligations under DPDP Act 2023?", "Under the Digital Personal Data Protection Act 2023, data fiduciaries must provide clear multilingual consent notices, process data only for declared purposes, implement technical safeguards, honor data principal rights, and report breaches within prescribed windows."),
        ("What are the statutory penalties for non-compliance under DPDP Act?", "The DPDP Act 2023 prescribes monetary penalties up to ₹250 Crore for failure to take reasonable security safeguards to prevent personal data breaches, and up to ₹200 Crore for failure to notify breaches."),
        ("Is a POSH Internal Committee (IC) mandatory for all businesses?", "Yes. Under Section 4 of the POSH Act 2013, any workplace employing 10 or more employees must mandatorily constitute an Internal Committee headed by a senior woman employee and an external member."),
        ("Are post-employment non-compete clauses enforceable in India?", "Under Section 27 of the Indian Contract Act 1872, agreements in restraint of trade are void. Non-compete covenants are enforceable during active employment, but post-employment restrictions are largely unenforceable; non-solicitation and confidentiality clauses provide enforceable alternatives."),
        ("When is an establishment required to register with EPFO and ESIC?", "EPFO registration is compulsory for establishments employing 20 or more persons. ESIC registration applies to establishments with 10 or more employees earning up to ₹21,000/month in notified areas.")
    ]
    wd_packages = [
        {"name": "Foundational HR Pack", "tier": "Essential", "price": 14999, "period": "/ one-time", "description": "Core statutory contracts and templates for early-stage teams.", "features": ["Executive & Employee Agreements", "Unilateral & Mutual NDAs", "Proprietary Information & Invention Assignment (PIIA)", "Offer Letter & Relieving Documentation", "Workplace Code of Conduct"]},
        {"name": "Scale-Up Governance & POSH", "tier": "Scale", "price": 34999, "period": "/ one-time", "featured": True, "description": "Statutory compliance for companies crossing 10+ team members.", "features": ["All Foundational Pack Documents", "POSH Policy & IC Constitution Order", "ESIC & EPFO Code Allotment Setup", "DPDP Act Readiness Gap Audit", "Shop & Establishment License Application"]},
        {"name": "Enterprise Digital Trust Retainer", "tier": "Enterprise", "price": 79999, "period": "/ one-time", "description": "Complete digital privacy, AI governance, and ESG architecture.", "features": ["Full DPDP Act Privacy Implementation", "Enterprise AI Acceptable Use Policy", "ESG Sustainability Charter & BRSR Framework", "Co-Founder Agreement & Shareholders' Agreement", "Dedicated Compliance Legal-Tech Architect"]}
    ]
    os.makedirs("workforce-digital", exist_ok=True)
    with open("workforce-digital/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "workforce-digital",
            "Workforce Governance, Labour Compliance & DPDP Act",
            "Employment Contracts, POSH Frameworks, EPF/ESIC Compliance, and DPDP Act 2023 Digital Privacy Readiness.",
            ["DPDP Act 2023", "POSH Act 2013", "Contract Act 1872", "EPFO & ESIC", "AI Governance"],
            "Labour tribunal representation and judicial data privacy litigation are represented exclusively by independent licensed advocates.",
            "Safeguarding intellectual capital, workplace equity, and digital consumer trust.",
            services_by_cat.get("workforce-digital", []),
            wd_packages,
            wd_faqs
        ))
    print("Created workforce-digital/index.html")

if __name__ == "__main__":
    main()
