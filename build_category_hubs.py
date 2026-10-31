# -*- coding: utf-8 -*-
"""
Generates all 6 Category Hub pages with the new modern LegalTech UI/UX design:
- Plus Jakarta Sans typography
- Sky Blue (#0284C7), Sky Light (#E0F2FE), Slate (#F1F5F9), Gold (#D97706), Dark (#0F172A)
- Dual-Mode Switcher (A La Carte / Packages)
- Interactive Fee Calculator
- FAQ Accordion
- Standardized Footer with Mandatory Disclaimer
"""
import os
import json

MANDATORY_DISCLAIMER = """<p class="text-xs text-slate-400 leading-relaxed text-justify">
  <strong class="text-brand-gold font-bold uppercase">Regulatory Notice:</strong> CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform. CCS is not a law firm and does not provide court litigation or judicial representation before courts or tribunals. All court litigation and tribunal appearances are executed exclusively through independent, licensed advocates or associate law firms in accordance with the Advocates Act, 1961. Statutory audits, tax certifications, and regulated professional services are fulfilled by qualified, independent Chartered Accountants, Company Secretaries, and registered professionals in compliance with ICAI, ICSI, and statutory guidelines.
</p>"""

ANNOUNCEMENT_BAR = """<div class="bg-gradient-to-r from-brand-sky to-brand-skyHover text-white text-xs md:text-sm py-2 px-4 text-center font-medium shadow-sm flex items-center justify-center gap-2">
  <span>🚀 <strong>Special Offer:</strong> Get 20% OFF MCA Filing &amp; Free Expert Consultation this week!</span>
  <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20want%20to%20claim%20the%2020%25%20OFF%20MCA%20Filing%20offer." target="_blank" rel="noopener noreferrer" class="underline hover:text-brand-goldLight font-bold transition ml-2">Claim Offer &rarr;</a>
</div>"""

NAV_HTML = """<header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
    <!-- Logo -->
    <a href="/" class="flex items-center gap-3 group">
      <div class="w-10 h-10 bg-gradient-to-tr from-brand-sky to-brand-gold rounded-xl flex items-center justify-center text-white font-extrabold text-xl shadow-md group-hover:scale-105 transition-transform">
        C
      </div>
      <div>
        <span class="text-xl font-extrabold text-brand-dark tracking-tight">CRAFTEGON</span>
        <span class="block text-[10px] font-bold text-brand-sky tracking-widest uppercase">Corporate Services</span>
      </div>
    </a>

    <!-- Desktop Nav -->
    <nav class="hidden lg:flex items-center space-x-7 text-sm font-semibold text-slate-600">
      <a href="/business-setup/" class="hover:text-brand-sky transition">Business Setup</a>
      <a href="/gst-advisory/" class="hover:text-brand-sky transition">GST Advisory</a>
      <a href="/corporate-governance/" class="hover:text-brand-sky transition">Governance &amp; MCA</a>
      <a href="/direct-tax/" class="hover:text-brand-sky transition">Direct Tax</a>
      <a href="/brand-protection/" class="hover:text-brand-sky transition">Brand &amp; IP</a>
      <a href="/licenses.html" class="hover:text-brand-sky transition">Licenses</a>
      <a href="/experts.html" class="hover:text-brand-sky transition flex items-center gap-1.5 text-brand-sky">
        <span>Talk to Experts</span>
        <span class="bg-brand-goldLight text-brand-gold text-[10px] px-2 py-0.5 rounded-full font-bold uppercase">Live</span>
      </a>
    </nav>

    <!-- CTA Buttons -->
    <div class="flex items-center gap-3">
      <a href="tel:+918606918247" class="hidden sm:flex items-center gap-2 text-xs font-bold text-slate-700 bg-brand-slate px-4 py-2.5 rounded-lg border border-slate-200 hover:bg-slate-200 transition">
        <span class="text-emerald-600 font-bold">●</span> +91 86069 18247
      </a>
      <a href="#inquiry" class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs md:text-sm px-5 py-2.5 rounded-lg shadow-md hover:shadow-lg transition">
        Get Started
      </a>
      <button id="mobile-menu-toggle" class="lg:hidden text-slate-700 p-2 rounded-lg hover:bg-slate-100 min-touch flex items-center justify-center" aria-label="Toggle Menu">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 py-4 space-y-3 shadow-lg">
    <a href="/business-setup/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Business Setup &amp; Formation</a>
    <a href="/gst-advisory/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">GST Advisory &amp; Filings</a>
    <a href="/corporate-governance/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Corporate Governance &amp; MCA</a>
    <a href="/direct-tax/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Direct Tax &amp; TDS</a>
    <a href="/brand-protection/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Brand Protection &amp; Trademarks</a>
    <a href="/licenses.html" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Licenses &amp; Certifications</a>
    <a href="/workforce-digital/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Workforce &amp; Digital Infrastructure</a>
    <a href="/experts.html" class="flex text-sm font-semibold text-brand-sky py-2 border-b border-slate-100 items-center justify-between">
      <span>Talk to CA/CS Experts</span>
      <span class="bg-brand-goldLight text-brand-gold text-[10px] px-2 py-0.5 rounded-full font-bold uppercase">Live</span>
    </a>
    <a href="/about.html" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">About CraftEgon</a>
    <a href="/contact.html" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Contact &amp; Grievance Desk</a>
    <div class="pt-2 flex flex-col gap-2">
      <a href="tel:+918606918247" class="block w-full text-center bg-slate-100 text-slate-800 font-bold text-sm py-2.5 rounded-lg border border-slate-200">
        📞 Call: +91 86069 18247
      </a>
      <a href="#inquiry" class="block w-full text-center bg-brand-sky text-white font-bold text-sm py-2.5 rounded-lg shadow">
        Get Free Consultation
      </a>
    </div>
  </div>
</header>"""

FOOTER_HTML = f"""<footer class="bg-brand-dark text-slate-400 text-xs py-14 border-t border-slate-800">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <div>
        <div class="flex items-center gap-3 mb-4">
          <div class="w-8 h-8 bg-gradient-to-tr from-brand-sky to-brand-gold rounded-lg flex items-center justify-center text-white font-extrabold text-lg shadow">
            C
          </div>
          <span class="text-lg font-bold text-white tracking-tight">CRAFTEGON</span>
        </div>
        <p class="text-slate-400 text-xs leading-relaxed mb-4">
          India's enterprise corporate technology, secretarial governance, and compliance operations platform.
        </p>
        <p class="text-slate-400 text-xs">Markaz Knowledge City HQ, Kozhikode &amp; Technopark, Trivandrum, Kerala, India</p>
        <p class="text-slate-400 text-xs mt-1">support@craftegon.com | +91 86069 18247</p>
      </div>

      <div>
        <h5 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Practice Hubs</h5>
        <ul class="space-y-2">
          <li><a href="/business-setup/" class="hover:text-brand-sky transition">Business Setup &amp; Formation</a></li>
          <li><a href="/gst-advisory/" class="hover:text-brand-sky transition">GST Advisory &amp; Filings</a></li>
          <li><a href="/corporate-governance/" class="hover:text-brand-sky transition">Corporate Governance &amp; MCA</a></li>
          <li><a href="/direct-tax/" class="hover:text-brand-sky transition">Direct Tax &amp; TDS</a></li>
          <li><a href="/brand-protection/" class="hover:text-brand-sky transition">Brand &amp; IP Protection</a></li>
          <li><a href="/licenses.html" class="hover:text-brand-sky transition">Trade Licenses &amp; FSSAI</a></li>
          <li><a href="/workforce-digital/" class="hover:text-brand-sky transition">Workforce &amp; Digital</a></li>
        </ul>
      </div>

      <div>
        <h5 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Platform &amp; Legal</h5>
        <ul class="space-y-2">
          <li><a href="/about.html" class="hover:text-brand-sky transition">About CraftEgon</a></li>
          <li><a href="/terms.html" class="hover:text-brand-sky transition">Terms &amp; Conditions</a></li>
          <li><a href="/privacy.html" class="hover:text-brand-sky transition">Privacy Policy</a></li>
          <li><a href="/data-policy.html" class="hover:text-brand-sky transition">Data Protection Policy (DPDP)</a></li>
          <li><a href="/experts.html" class="hover:text-brand-sky transition">Expert CA/CS Directory</a></li>
          <li><a href="/contact.html" class="hover:text-brand-sky transition">Contact &amp; Grievance Desk</a></li>
        </ul>
      </div>

      <div>
        <h5 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Direct Case Desk</h5>
        <p class="text-slate-400 mb-3">Connect directly via WhatsApp Business for express onboarding:</p>
        <a href="https://wa.me/918606918247" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-[#25D366]/20 border border-[#25D366]/40 text-[#25D366] hover:bg-[#25D366]/30 px-3.5 py-2.5 rounded-lg text-xs font-bold transition">
          <span>💬 Direct WhatsApp Case Desk</span>
        </a>
        <a href="tel:+918606918247" class="mt-3 block text-slate-300 hover:text-white font-semibold">
          📞 +91 86069 18247
        </a>
      </div>
    </div>

    <!-- Mandatory Non-Litigation Disclaimer -->
    <div class="border-t border-slate-800 pt-8">
      <div class="p-4 rounded-xl bg-slate-900 border border-slate-800">
        {MANDATORY_DISCLAIMER}
      </div>
      <div class="mt-4 flex flex-col sm:flex-row justify-between items-center text-[11px] text-slate-500 gap-3">
        <p>&copy; 2026 CraftEgon Corporate Services. All rights reserved.</p>
        <div class="flex flex-wrap items-center gap-4 text-[11px] text-slate-400">
          <a href="/about.html" class="hover:text-white transition">About Us</a>
          <span>·</span>
          <a href="/terms.html" class="hover:text-white transition">Terms &amp; Conditions</a>
          <span>·</span>
          <a href="/privacy.html" class="hover:text-white transition">Privacy Policy</a>
          <span>·</span>
          <a href="/data-policy.html" class="hover:text-white transition">Data Policy</a>
        </div>
        <p class="font-mono">corporateservices.craftegon.com</p>
      </div>
    </div>
  </div>
</footer>"""

def render_category_hub(cat_slug, title, subtitle, badges, hero_disclaimer, intro_text, services, packages, faqs):
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

    services_cards = []
    for s in services:
        link_target = s.get("product_path") if s.get("phase") == 1 else "#inquiry"
        link_label = "View Execution Process &rarr;" if s.get("phase") == 1 else "Apply Now &rarr;"
        fee_badge = f"Starting @ ₹{s['pricing']['base_professional_fee']:,}"
        time_badge = s.get("turnaround_time", "Statutory Timeline")
        card = f"""
        <div class="bg-white rounded-2xl p-6 border border-slate-200 hover:shadow-lg hover:border-brand-sky/40 transition flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <div class="w-12 h-12 bg-brand-skyLight text-brand-sky rounded-xl flex items-center justify-center font-bold text-xl shadow-sm">
                <i data-lucide="{s.get('icon', 'file-text')}" class="w-6 h-6"></i>
              </div>
              <span class="text-xs font-mono px-2.5 py-1 rounded-full bg-slate-100 text-slate-600 border border-slate-200">{time_badge}</span>
            </div>
            <h3 class="text-xl font-bold text-brand-dark mb-2">{s['title']}</h3>
            <p class="text-xs text-slate-600 leading-relaxed mb-6">{s['short_description']}</p>
          </div>
          <div class="flex items-center justify-between border-t border-slate-200 pt-4">
            <span class="text-xs font-bold text-brand-gold">{fee_badge}</span>
            <a href="{link_target}" class="text-xs font-bold text-brand-sky hover:underline flex items-center gap-1">
              <span>{link_label}</span>
            </a>
          </div>
        </div>
        """
        services_cards.append(card)
        
    services_grid_html = "\n".join(services_cards)

    package_cards = []
    for p in packages:
        featured_border = "border-2 border-brand-sky shadow-xl relative bg-white" if p.get("featured") else "border border-slate-200 shadow-sm bg-white"
        badge_html = '<span class="absolute -top-3 left-1/2 -translate-x-1/2 bg-brand-sky text-white text-[10px] uppercase font-extrabold tracking-widest px-3 py-1 rounded-full shadow">Most Popular</span>' if p.get("featured") else ""
        items_html = "".join([f'<li class="flex items-start gap-2 text-xs text-slate-700"><span class="text-emerald-600 font-bold shrink-0">✓</span><span>{item}</span></li>' for item in p['features']])
        
        card = f"""
        <div class="rounded-2xl p-6 {featured_border} flex flex-col justify-between">
          {badge_html}
          <div>
            <div class="mb-4">
              <span class="text-xs font-bold text-brand-sky uppercase tracking-wider">{p['tier']}</span>
              <h3 class="text-2xl font-extrabold text-brand-dark mt-1">{p['name']}</h3>
              <p class="text-xs text-slate-500 mt-1">{p['description']}</p>
            </div>
            <div class="py-4 border-y border-slate-100 mb-6">
              <span class="text-3xl font-black text-brand-dark">₹{p['price']:,}</span>
              <span class="text-xs text-slate-500 font-medium"> {p['period']}</span>
            </div>
            <ul class="space-y-2.5 mb-6">
              {items_html}
            </ul>
          </div>
          <a href="#inquiry" class="w-full text-center py-3 rounded-lg text-xs font-bold uppercase tracking-wider transition {'bg-brand-sky hover:bg-brand-skyHover text-white shadow-md' if p.get('featured') else 'bg-slate-100 hover:bg-slate-200 text-brand-dark'}">
            Select Package &rarr;
          </a>
        </div>
        """
        package_cards.append(card)
        
    packages_grid_html = "\n".join(package_cards)

    faq_items = []
    for idx, (q, a) in enumerate(faqs):
        faq_items.append(f"""
        <div class="border border-slate-200 rounded-xl overflow-hidden bg-white shadow-sm">
          <button class="w-full text-left px-5 py-4 flex items-center justify-between font-bold text-sm text-brand-dark hover:text-brand-sky focus:outline-none faq-btn transition" data-faq-target="faq-{cat_slug}-{idx}">
            <span>{q}</span>
            <svg class="w-4 h-4 text-brand-sky transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </button>
          <div id="faq-{cat_slug}-{idx}" class="hidden px-5 pb-4 text-xs text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
            {a}
          </div>
        </div>
        """)
    faqs_html = "\n".join(faq_items)

    badges_html = "".join([f'<span class="px-3 py-1 rounded-full bg-brand-skyLight text-brand-sky border border-brand-sky/20 text-xs font-bold">{b}</span>' for b in badges])

    disclaimer_hero_badge = ""
    if hero_disclaimer:
        disclaimer_hero_badge = f"""
        <div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center gap-2.5">
          <span class="text-base">⚠️</span>
          <span><strong>Statutory Practice Notice:</strong> {hero_disclaimer}</span>
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
  
  <!-- Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- Production Compiled Stylesheets -->
  <link rel="stylesheet" href="/assets/css/output.css" />
  <link rel="stylesheet" href="/assets/css/theme.css" />
  
  <script type="application/ld+json">
  {json.dumps(faq_schema, indent=2)}
  </script>
</head>
<body class="bg-slate-50 text-brand-dark font-sans antialiased min-h-screen flex flex-col justify-between">

{ANNOUNCEMENT_BAR}
{NAV_HTML}

<!-- HERO SECTION -->
<section class="relative bg-gradient-to-b from-brand-skyLight/50 via-white to-slate-50 py-12 md:py-16 border-b border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <nav class="flex items-center space-x-2 text-xs font-semibold text-slate-500 mb-4">
      <a href="/" class="hover:text-brand-sky transition">Home</a>
      <span>/</span>
      <span class="text-brand-sky uppercase">{cat_slug.replace('-', ' ')}</span>
    </nav>
    
    <div class="flex flex-wrap gap-2 mb-4">
      {badges_html}
    </div>
    
    <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-brand-dark tracking-tight leading-tight max-w-4xl mb-4">
      {title}
    </h1>
    
    <p class="text-slate-600 text-base md:text-lg max-w-3xl leading-relaxed mb-6">
      {subtitle}
    </p>
    
    {disclaimer_hero_badge}
    
    <div class="mt-6 flex flex-wrap items-center gap-4">
      <a href="#services-view" class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs uppercase tracking-wider px-6 py-3.5 rounded-lg shadow-md transition">
        Explore Services &amp; Fees &darr;
      </a>
      <a href="#inquiry" class="bg-white hover:bg-slate-50 text-slate-800 font-bold text-xs uppercase tracking-wider px-6 py-3.5 rounded-lg border border-slate-300 shadow-sm transition">
        Talk to an Expert
      </a>
    </div>
  </div>
</section>

<!-- DUAL-MODE VIEW SWITCHER -->
<section id="services-view" class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
    <div>
      <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Service Execution Models</h2>
      <h3 class="text-2xl md:text-3xl font-extrabold text-brand-dark">Standalone Solutions &amp; Retainer Packages</h3>
      <p class="text-xs text-slate-500 mt-1">Select between individual a la carte statutory filings or turnkey operational retainers.</p>
    </div>
    
    <div class="inline-flex p-1 bg-slate-200/80 rounded-xl border border-slate-300">
      <button id="btn-mode-alacarte" class="px-4 py-2 rounded-lg text-xs font-bold transition bg-brand-sky text-white shadow-sm">
        A La Carte Services (10)
      </button>
      <button id="btn-mode-packages" class="px-4 py-2 rounded-lg text-xs font-bold transition text-slate-700 hover:text-black">
        Package Bundles &amp; Retainers (3)
      </button>
    </div>
  </div>

  <div id="view-alacarte" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    {services_grid_html}
  </div>

  <div id="view-packages" class="hidden grid grid-cols-1 md:grid-cols-3 gap-8">
    {packages_grid_html}
  </div>
</section>

<!-- DYNAMIC CALCULATOR -->
<section class="py-16 bg-white border-y border-slate-200">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-8">
      <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Fee Transparency Engine</h2>
      <h3 class="text-2xl md:text-3xl font-extrabold text-brand-dark">Interactive Statutory Fee Calculator</h3>
      <p class="text-xs text-slate-500 mt-1">Government stamp duties vary by state. Compute your exact investment.</p>
    </div>

    <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
        <div>
          <label class="block text-xs font-bold uppercase text-slate-700 mb-1">Select State / Jurisdiction</label>
          <select id="calc-state-select" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm text-slate-800 focus:ring-2 focus:ring-brand-sky focus:outline-none">
            <option value="Kerala" selected>Kerala</option>
            <option value="Maharashtra">Maharashtra</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Delhi">Delhi</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Gujarat">Gujarat</option>
            <option value="Telangana">Telangana</option>
            <option value="Uttar Pradesh">Uttar Pradesh</option>
            <option value="West Bengal">West Bengal</option>
            <option value="Rajasthan">Rajasthan</option>
            <option value="Haryana">Haryana</option>
            <option value="Punjab">Punjab</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold uppercase text-slate-700 mb-1">Authorized Capital</label>
          <select id="calc-capital-select" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-sm text-slate-800 focus:ring-2 focus:ring-brand-sky focus:outline-none">
            <option value="100000">₹1 Lakh (Minimum)</option>
            <option value="500000">₹5 Lakhs</option>
            <option value="1000000" selected>₹10 Lakhs (Standard)</option>
            <option value="2500000">₹25 Lakhs</option>
            <option value="5000000">₹50 Lakhs</option>
            <option value="10000000">₹1 Crore</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center pt-4 border-t border-slate-200">
        <div class="p-3 bg-white rounded-xl border border-slate-200">
          <span class="block text-[10px] uppercase font-bold text-slate-500">Professional Fee</span>
          <span id="calc-prof-fee" class="font-black text-sm text-brand-dark mt-1 block">₹7,999</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-slate-200">
          <span class="block text-[10px] uppercase font-bold text-slate-500">State Stamp Duty</span>
          <span id="calc-stamp-duty" class="font-black text-sm text-brand-gold mt-1 block">₹5,000</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-slate-200">
          <span class="block text-[10px] uppercase font-bold text-slate-500">GST (18%)</span>
          <span id="calc-gst" class="font-black text-sm text-brand-dark mt-1 block">₹1,440</span>
        </div>
        <div class="p-3 bg-brand-skyLight rounded-xl border border-brand-sky/30">
          <span class="block text-[10px] uppercase font-bold text-brand-sky">Total Investment</span>
          <span id="calc-total" class="font-black text-sm text-brand-dark mt-1 block">₹14,439</span>
        </div>
      </div>

      <div id="hub-calc-note" class="mt-4 p-3 bg-white rounded-xl border border-slate-200 text-xs text-slate-600 leading-relaxed">
        <span class="font-semibold text-brand-dark">Statutory Formula (Kerala · ₹10 Lakhs Capital):</span>
        <span class="font-mono text-slate-700 ml-1">₹7,999 (Prof) + ₹5,000 (Stamp Duty) + ₹1,440 (GST) = <strong>₹14,439</strong></span>
      </div>
    </div>
  </div>
</section>

<!-- FAQS -->
<section class="py-16 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Frequently Asked Questions</h2>
    <h3 class="text-2xl md:text-3xl font-extrabold text-brand-dark">Statutory &amp; Operational Clarifications</h3>
  </div>
  
  <div class="space-y-3">
    {faqs_html}
  </div>
</section>

<!-- INQUIRY FORM -->
<section id="inquiry" class="py-16 bg-white border-t border-slate-200">
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-200 shadow-md">
      <div class="text-center mb-6">
        <h3 class="text-xl font-bold text-brand-dark">Initiate Your {title} Mandate</h3>
        <p class="text-xs text-slate-500 mt-1">Our corporate desk reviews and responds within 2 business hours.</p>
      </div>

      <form data-ccs-form="true" data-category="{cat_slug}" data-service-id="{cat_slug}-general" class="space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Full Name *</label>
            <input type="text" name="user_name" required placeholder="e.g. Rahul Sharma" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Email ID *</label>
            <input type="email" name="email" required placeholder="rahul@enterprise.com" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none" />
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Mobile / WhatsApp *</label>
            <input type="tel" name="phone" required placeholder="+91 98765 43210" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">State *</label>
            <select name="selected_state" required class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none">
              <option value="Kerala">Kerala</option>
              <option value="Maharashtra">Maharashtra</option>
              <option value="Karnataka">Karnataka</option>
              <option value="Delhi">Delhi</option>
              <option value="Tamil Nadu">Tamil Nadu</option>
              <option value="Telangana">Telangana</option>
              <option value="Other">Other States</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Specific Requirements</label>
          <textarea name="custom_message" rows="3" placeholder="Provide details regarding company stage or transaction timeline..." class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none"></textarea>
        </div>

        <button type="submit" class="w-full bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs uppercase tracking-wider py-3.5 rounded-lg shadow-md transition">
          Submit Mandate Request &rarr;
        </button>
      </form>
    </div>
  </div>
</section>

{FOOTER_HTML}

<script src="/assets/js/forms.js"></script>
<script src="/assets/js/calculator.js"></script>
<script src="/assets/js/main.js"></script>
<script>
  if (window.lucide) {{ lucide.createIcons(); }}

  const mBtn = document.getElementById('mobile-menu-toggle') || document.getElementById('mobileMenuBtn');
  const mMenu = document.getElementById('mobile-menu') || document.getElementById('mobileMenu');
  if (mBtn && mMenu) {{
    mBtn.addEventListener('click', () => mMenu.classList.toggle('hidden'));
  }}

  const bAla = document.getElementById('btn-mode-alacarte');
  const bPkg = document.getElementById('btn-mode-packages');
  const vAla = document.getElementById('view-alacarte');
  const vPkg = document.getElementById('view-packages');

  if (bAla && bPkg && vAla && vPkg) {{
    bAla.addEventListener('click', () => {{
      bAla.className = 'px-4 py-2 rounded-lg text-xs font-bold transition bg-brand-sky text-white shadow-sm';
      bPkg.className = 'px-4 py-2 rounded-lg text-xs font-bold transition text-slate-700 hover:text-black';
      vAla.classList.remove('hidden');
      vPkg.classList.add('hidden');
    }});
    bPkg.addEventListener('click', () => {{
      bPkg.className = 'px-4 py-2 rounded-lg text-xs font-bold transition bg-brand-sky text-white shadow-sm';
      bAla.className = 'px-4 py-2 rounded-lg text-xs font-bold transition text-slate-700 hover:text-black';
      vPkg.classList.remove('hidden');
      vAla.classList.add('hidden');
    }});
  }}

  document.querySelectorAll('.faq-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const target = document.getElementById(btn.getAttribute('data-faq-target'));
      const icon = btn.querySelector('svg');
      if (target) {{
        target.classList.toggle('hidden');
        if (icon) icon.classList.toggle('rotate-180');
      }}
    }});
  }});

  const sSel = document.getElementById('calc-state-select');
  const cSel = document.getElementById('calc-capital-select');
  const hNote = document.getElementById('hub-calc-note');
  function runCalc() {{
    if (window.CCSCalculator && window.CCSCalculator.calculateTotalFee && sSel && cSel) {{
      const state = sSel.value;
      const capital = parseInt(cSel.value, 10);
      const res = window.CCSCalculator.calculateTotalFee(7999, state, capital);
      document.getElementById('calc-prof-fee').textContent = '₹' + res.professional_fee.toLocaleString('en-IN');
      document.getElementById('calc-stamp-duty').textContent = '₹' + res.stamp_duty.toLocaleString('en-IN');
      document.getElementById('calc-gst').textContent = '₹' + res.gst_amount.toLocaleString('en-IN');
      document.getElementById('calc-total').textContent = '₹' + res.total.toLocaleString('en-IN');
      if (hNote) {{
        hNote.innerHTML = '<span class="font-semibold text-brand-dark">Statutory Formula (' + state + ' · ₹' + capital.toLocaleString('en-IN') + ' Capital):</span> <span class="font-mono text-slate-700 ml-1">₹7,999 (Prof) + ₹' + res.stamp_duty.toLocaleString('en-IN') + ' (Stamp Duty) + ₹' + res.gst_amount.toLocaleString('en-IN') + ' (GST 18%) = <strong>₹' + res.total.toLocaleString('en-IN') + '</strong></span>';
      }}
    }}
  }}
  if (sSel && cSel) {{
    sSel.addEventListener('change', runCalc);
    cSel.addEventListener('change', runCalc);
    runCalc();
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

    # 1. Business Setup
    bs_faqs = [
        ("What is SPICe+ and how does it work?", "SPICe+ (INC-32) is the integrated web form on MCA V3 combining Name Reservation (RUN), DIN Allotment, Incorporation (e-MOA/AOA), PAN/TAN, EPFO/ESIC, and bank account setup in a single filing."),
        ("How long does Private Limited Company incorporation take?", "Typically 7-10 working days, subject to MCA V3 verification timelines and name approval."),
        ("What is the minimum capital required?", "Under the Companies (Amendment) Act 2015, there is zero mandatory minimum paid-up capital requirement. ₹1 Lakh or ₹10 Lakhs is standardly chosen."),
        ("Can non-resident foreign citizens be directors?", "Yes, as long as at least one director on the board is a Resident of India (stayed 182+ days in India in the previous calendar year)."),
        ("What is Form INC-20A?", "Declaration of Commencement of Business, mandatory to be filed within 180 days of incorporation confirming that subscribers deposited their capital.")
    ]
    bs_packages = [
        {"name": "Starter Incorporation", "tier": "Startup", "price": 5999, "period": "+ govt fees", "description": "Core incorporation for bootstrapped founders.", "features": ["Name Approval (RUN)", "SPICe+ Part B Filing", "DIN Allotment for 2 Directors", "e-MOA & e-AOA Drafting", "PAN & TAN Allocation", "Bank Account Facilitation"]},
        {"name": "Growth Startup Bundle", "tier": "Scale", "price": 14999, "period": "+ govt fees", "featured": True, "description": "Complete statutory kit for venture-ready teams.", "features": ["All Starter Features", "GST Registration", "MSME / Udyam Certificate", "Startup India DPIIT Recognition", "Trademark Search & Class Filing", "First Board Minutes & ADT-1"]},
        {"name": "Enterprise Corporate Setup", "tier": "Enterprise", "price": 29999, "period": "+ govt fees", "description": "Turnkey multi-director entity or foreign subsidiary.", "features": ["All Growth Features", "Foreign Inward Remittance (FC-GPR)", "Shareholder Agreement Drafting", "Annual ROC Secretarial Retainer (1 Year)", "Dedicated Senior CA Manager"]}
    ]
    os.makedirs("business-setup", exist_ok=True)
    with open("business-setup/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "business-setup",
            "Business Setup & Company Incorporation",
            "End-to-end corporate formation under Companies Act 2013 — Private Limited, LLP, OPC, Foreign Subsidiary & DPIIT Startup Recognition.",
            ["Companies Act 2013", "SPICe+ MCA V3", "e-MOA/e-AOA", "AGILE-PRO-S", "DPIIT"],
            "",
            "Complete company setup architecture with transparent fixed fee schedules.",
            services_by_cat.get("business-setup", []),
            bs_packages,
            bs_faqs
        ))
    print("Updated business-setup/index.html")

    # 2. GST Advisory
    gst_faqs = [
        ("Who is mandatorily required to register under GST?", "Under Section 22 of the CGST Act 2017, registration is compulsory when annual turnover exceeds ₹40 Lakhs for goods (₹20 Lakhs in Special Category States) or ₹20 Lakhs for services."),
        ("What is the difference between GSTR-1 and GSTR-3B?", "GSTR-1 is the monthly statement of outward supplies filed by 11th. GSTR-3B is the monthly summary tax return filed by 20th."),
        ("What is E-Invoicing and who must comply?", "Under Rule 48(4), E-invoicing on the IRP portal is mandatory for B2B transactions of businesses with aggregate turnover > ₹5 Crore in any preceding financial year."),
        ("What is Rule 36(4) ITC matching?", "Input Tax Credit cannot be claimed unless vendor invoices are uploaded and reflected in auto-drafted Form GSTR-2B."),
        ("When is the GSTR-9 Annual Return due?", "Mandatory for registered taxpayers with turnover > ₹2 Crore, due by December 31 following the close of the financial year.")
    ]
    gst_packages = [
        {"name": "Starter GST Desk", "tier": "Essential", "price": 2499, "period": "/ month", "description": "Ideal for startups and growing service entities.", "features": ["Monthly GSTR-1 & GSTR-3B Filing", "GSTR-2B ITC Matching", "PMT-06 Challan Generation", "Annual GSTR-9 Preparation"]},
        {"name": "Growth E-Commerce & Invoicing", "tier": "Scale", "price": 5999, "period": "/ month", "featured": True, "description": "Tailored for mid-market suppliers and multi-state vendors.", "features": ["All Starter Desk Features", "API E-Invoicing & IRN Generation", "Rule 36(4) Vendor Default Tracking", "Notice Handling (up to 2 notices/yr)", "LUT Export Filing for Zero-Rated Supply"]},
        {"name": "Enterprise Indirect Tax Retainer", "tier": "Enterprise", "price": 11999, "period": "/ month", "description": "Full-scale corporate indirect tax management and audit support.", "features": ["All Growth Features Included", "Form GSTR-9C CA Reconciliation Support", "Departmental Audit Support", "Advance Ruling Advisory", "Dedicated Senior Tax Architect"]}
    ]
    os.makedirs("gst-advisory", exist_ok=True)
    with open("gst-advisory/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "gst-advisory",
            "GST Registration, Returns & Indirect Tax Advisory",
            "Statutory Indirect Tax Operations Aligned with CGST/SGST Act 2017, E-Invoicing Mandates & GSTR-2B Reconciliations.",
            ["CGST/SGST Act 2017", "GSTR-1 & 3B", "E-Invoicing IRN", "GSTR-9 & 9C", "ITC Rule 36(4)"],
            "Departmental appeals before the Appellate Authority for Advance Rulings (AAAR) and High Courts are executed through licensed independent Advocates and CAs.",
            "Complete GST lifecycle management from initial registration to automated e-invoicing.",
            services_by_cat.get("gst-advisory", []),
            gst_packages,
            gst_faqs
        ))
    print("Updated gst-advisory/index.html")

    # 3. Corporate Governance
    cg_faqs = [
        ("What forms are required for annual ROC filing?", "Every private limited company must file Form AOC-4 (Financial Statements within 30 days of AGM) and Form MGT-7/7A (Annual Return within 60 days of AGM)."),
        ("What is DIR-3 KYC and when is it due?", "Mandatory annual director credential verification under Rule 12A, due by September 30 annually. Failure results in DIN deactivation and ₹5,000 reactivation fee."),
        ("What happens if annual ROC filings are missed?", "A continuing statutory penalty of ₹100 per day per form applies without an upper ceiling since the 2018 amendment."),
        ("How to change a company's registered office?", "Within the same city via Form INC-22; between cities/ROC jurisdictions with Regional Director approval via Form INC-23."),
        ("What is the procedure for director appointment?", "Obtain consent in Form DIR-2, pass board resolution, and file Form DIR-12 with ROC within 30 days.")
    ]
    cg_packages = [
        {"name": "Basic ROC Pack", "tier": "Essential", "price": 9999, "period": "/ year", "description": "Core annual statutory secretarial filings.", "features": ["Form AOC-4 Financials Filing", "Form MGT-7A Annual Return", "DIR-3 KYC for 2 Directors", "AGM Documentation Drafts"]},
        {"name": "Corporate Governance Retainer", "tier": "Scale", "price": 19999, "period": "/ year", "featured": True, "description": "Complete year-round secretarial compliance.", "features": ["All Basic ROC Features", "Statutory Register Maintenance", "4 Quarterly Board Meeting Resolutions", "Director Appointment/Resignation Filing", "ACTIVE INC-22A Compliance"]},
        {"name": "Enterprise Secretarial Retainer", "tier": "Enterprise", "price": 49999, "period": "/ year", "description": "Full corporate governance for funded entities.", "features": ["All Governance Retainer Features", "EGM & Special Resolution Filings (MGT-14)", "FEMA / RBI Filings", "ESOP Pool Creation & Capital Expansion", "Dedicated Company Secretary"]}
    ]
    os.makedirs("corporate-governance", exist_ok=True)
    with open("corporate-governance/index.html", "w", encoding="utf-8") as f:
        f.write(render_category_hub(
            "corporate-governance",
            "Corporate Governance & MCA / ROC Secretarial Compliance",
            "Annual MCA Filings (AOC-4/MGT-7), Director KYC, Board Resolutions, MOA Alterations, and Statutory Registers under Companies Act 2013.",
            ["Companies Act 2013", "Form AOC-4", "Form MGT-7/7A", "DIR-3 KYC", "MCA V3"],
            "",
            "Year-round secretarial peace of mind with zero late filing penalties.",
            services_by_cat.get("corporate-governance", []),
            cg_packages,
            cg_faqs
        ))
    print("Updated corporate-governance/index.html")

    # 4. Direct Tax
    dt_faqs = [
        ("Which ITR form applies to Private Limited Companies?", "Private and Public Limited companies mandatorily file Form ITR-6 electronically with a Class 3 Digital Signature under Section 139(1)."),
        ("What are corporate income tax rates for FY 2024-25?", "Under Section 115BAA, domestic corporate entities can opt for a concessional base tax rate of 22% (effective 25.17% with surcharge and cess)."),
        ("When is a Tax Audit under Section 44AB mandatory?", "When business turnover exceeds ₹1 Crore (or ₹10 Crore if cash transactions are under 5%)."),
        ("What are quarterly TDS return deadlines?", "Form 24Q/26Q are due quarterly: July 31 (Q1), October 31 (Q2), January 31 (Q3), and May 31 (Q4)."),
        ("What is Form 15CA and Form 15CB?", "Statutory online declarations and CA certifications required for foreign outbound remittances under Section 195.")
    ]
    dt_packages = [
        {"name": "Startup Direct Tax Retainer", "tier": "Basic", "price": 14999, "period": "/ year", "description": "Complete year-round income tax and quarterly withholding.", "features": ["Corporate Form ITR-6 Filing", "Quarterly TDS (24Q & 26Q) Filing", "Advance Tax Computation (4 Quarters)", "Form 26AS & AIS Reconciliation"]},
        {"name": "Growth Corporate Tax Desk", "tier": "Scale", "price": 24999, "period": "/ year", "featured": True, "description": "Designed for funded startups and mid-market entities.", "features": ["All Startup Tax Features", "Form 3CD Tax Audit Data Coordination", "TDS Certificates (Form 16/16A) Issuance", "Income Tax Notice Reply Coordination", "Section 115BAA Regime Advisory"]},
        {"name": "Enterprise Cross-Border Tax", "tier": "Enterprise", "price": 49999, "period": "/ year", "description": "Comprehensive corporate tax, transfer pricing, and treaty structuring.", "features": ["All Growth Features Included", "Transfer Pricing Local File Review", "Form 15CA/15CB Remittance Certification", "Permanent Establishment Risk Review", "Dedicated Senior Corporate Tax Specialist"]}
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
    print("Updated direct-tax/index.html")

    # 5. Brand Protection
    bp_faqs = [
        ("What is the legal difference between ™ and ® symbols?", "The ™ symbol indicates an unregistered trademark application has been filed. The ® symbol can only be legally displayed after the Trade Marks Registry has granted a final Certificate of Registration."),
        ("How does Nice Classification operate?", "Trademarks are categorized into 45 international classes: Classes 1-34 for physical goods, Classes 35-45 for services."),
        ("What is a Section 9 vs Section 11 objection?", "Section 9 objections relate to absolute grounds (lacking distinctiveness). Section 11 objections pertain to relative grounds (similarity with earlier marks)."),
        ("What is the statutory opposition window?", "A statutory 4-month public opposition window opens once advertised in the Trade Marks Journal."),
        ("How long does trademark protection remain valid?", "10 years from the date of application, renewable indefinitely every 10 years via Form TM-R.")
    ]
    bp_packages = [
        {"name": "Brand Inception Pack", "tier": "Essential", "price": 6999, "period": "/ mark + govt", "description": "Single-class filing with comprehensive clearance search.", "features": ["IP India Database Conflict Search", "Drafting Goods/Services Description", "Form TM-A Filing with Digital Signature", "TM Symbol Usage Authorization", "Application Status Tracking"]},
        {"name": "Complete Brand Armor", "tier": "Popular", "price": 14999, "period": "/ mark + govt", "featured": True, "description": "Dual-class registration with full examination rebuttal guarantee.", "features": ["Filing Across 2 Nice Classes", "Section 9/11 Examination Reply Drafting", "Acquired Distinctiveness Evidence Compilation", "Copyright Filing for Logo/Artistic Work", "Watch Services for 12 Months"]},
        {"name": "Enterprise IP Portfolio Desk", "tier": "Enterprise", "price": 39999, "period": "/ portfolio", "description": "Complete intellectual property orchestration for tech ventures.", "features": ["Up to 5 Trademark Classes Filed", "Comprehensive Patent Search Advisory", "Industrial Design Filing (1 Product)", "Trademark Assignment & Licensing Deeds", "Dedicated Intellectual Property Manager"]}
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
    print("Updated brand-protection/index.html")

    # 6. Workforce & Digital
    wd_faqs = [
        ("What are corporate obligations under DPDP Act 2023?", "Data fiduciaries must provide clear multilingual consent notices, process data only for declared purposes, implement technical safeguards, and report breaches within prescribed windows."),
        ("What are penalties under DPDP Act?", "Monetary penalties up to ₹250 Crore for failure to take reasonable security safeguards to prevent personal data breaches."),
        ("Is a POSH Internal Committee (IC) mandatory?", "Yes. Under Section 4 of the POSH Act 2013, any workplace employing 10 or more employees must mandatorily constitute an Internal Committee."),
        ("Are post-employment non-compete clauses enforceable in India?", "Under Section 27 of the Indian Contract Act 1872, agreements in restraint of trade are void. Non-solicitation and confidentiality clauses provide enforceable alternatives."),
        ("When is an establishment required to register with EPFO and ESIC?", "EPFO registration is compulsory for 20+ employees. ESIC registration applies to 10+ employees earning up to ₹21,000/month in notified areas.")
    ]
    wd_packages = [
        {"name": "Foundational HR Pack", "tier": "Essential", "price": 9999, "period": "/ one-time", "description": "Core statutory contracts and templates for early-stage teams.", "features": ["Executive & Employee Agreements", "Unilateral & Mutual NDAs", "Proprietary Information & Invention Assignment (PIIA)", "Offer Letter & Relieving Documentation", "Workplace Code of Conduct"]},
        {"name": "Scale-Up Governance & POSH", "tier": "Scale", "price": 24999, "period": "/ one-time", "featured": True, "description": "Statutory compliance for companies crossing 10+ team members.", "features": ["All Foundational Pack Documents", "POSH Policy & IC Constitution Order", "ESIC & EPFO Code Allotment Setup", "DPDP Act Readiness Gap Audit", "Shop & Establishment License Application"]},
        {"name": "Enterprise Digital Trust Retainer", "tier": "Enterprise", "price": 59999, "period": "/ one-time", "description": "Complete digital privacy, AI governance, and ESG architecture.", "features": ["Full DPDP Act Privacy Implementation", "Enterprise AI Acceptable Use Policy", "ESG Sustainability Charter & BRSR Framework", "Co-Founder Agreement & Shareholders' Agreement", "Dedicated Compliance Legal-Tech Architect"]}
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
    print("Updated workforce-digital/index.html")

if __name__ == "__main__":
    main()
