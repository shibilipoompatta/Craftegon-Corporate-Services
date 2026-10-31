"""
build_knowledge_pages.py
Compiles dedicated, SEO-optimized standalone Knowledge Guide pages into /knowledge/
from data/craftegon-knowledge-hub.json.
"""

import json
import os
import html
import re

CATEGORY_HUBS = {
    "business-setup": {"name": "Business Setup & Formation", "hub_url": "/business-setup/"},
    "gst-advisory": {"name": "GST Advisory & Filings", "hub_url": "/gst-advisory/"},
    "corporate-governance": {"name": "Corporate Governance & MCA", "hub_url": "/corporate-governance/"},
    "direct-tax": {"name": "Direct Tax & TDS Advisory", "hub_url": "/direct-tax/"},
    "brand-protection": {"name": "Brand Protection & Trademarks", "hub_url": "/brand-protection/"},
    "workforce-digital": {"name": "Workforce & Digital Infrastructure", "hub_url": "/workforce-digital/"}
}

NAVBAR_HTML = """
    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-brand-sky to-brand-skyHover text-white text-xs md:text-sm py-2 px-4 text-center font-medium shadow-sm flex items-center justify-center gap-2">
        <span>🚀 <strong>Special Offer:</strong> Get 20% OFF MCA Filing &amp; Free Expert Consultation this week!</span>
        <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20want%20to%20claim%20the%2020%25%20OFF%20MCA%20Filing%20offer." target="_blank" rel="noopener noreferrer" class="underline hover:text-brand-goldLight font-bold transition ml-2">Claim Offer &rarr;</a>
    </div>

    <!-- Header Navigation -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <a href="/" class="flex items-center gap-3 group">
                <div class="w-10 h-10 bg-gradient-to-tr from-brand-sky to-brand-gold rounded-xl flex items-center justify-center text-white font-black text-xl shadow-md group-hover:scale-105 transition">
                    C
                </div>
                <div class="flex flex-col">
                    <span class="font-extrabold text-base tracking-tight text-brand-dark group-hover:text-brand-sky transition">CRAFTEGON</span>
                    <span class="text-[10px] tracking-widest text-slate-500 font-semibold uppercase">Corporate Services</span>
                </div>
            </a>

            <!-- Desktop Nav Links -->
            <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold text-slate-700">
                <a href="/business-setup/" class="hover:text-brand-sky transition">Business Setup</a>
                <a href="/gst-advisory/" class="hover:text-brand-sky transition">GST Advisory</a>
                <a href="/corporate-governance/" class="hover:text-brand-sky transition">Governance &amp; MCA</a>
                <a href="/direct-tax/" class="hover:text-brand-sky transition">Direct Tax</a>
                <a href="/brand-protection/" class="hover:text-brand-sky transition">Brand &amp; IP</a>
                <a href="/workforce-digital/" class="hover:text-brand-sky transition">Workforce &amp; Digital</a>
            </nav>

            <!-- Actions -->
            <div class="hidden sm:flex items-center gap-4">
                <a href="tel:+918606918247" class="text-xs font-bold text-slate-700 hover:text-brand-sky flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span>Desk: +91 86069 18247</span>
                </a>
                <a href="/experts.html" class="bg-brand-sky hover:bg-brand-skyHover text-white text-xs font-bold px-4 py-2.5 rounded-lg shadow-sm hover:shadow transition">
                    Book Consultation
                </a>
            </div>

            <!-- Mobile Menu Toggle Button -->
            <button id="mobileMenuBtn" aria-label="Toggle Navigation Menu" class="lg:hidden p-2 rounded-lg text-slate-600 hover:text-brand-sky hover:bg-slate-100 transition min-touch flex items-center justify-center">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>

        <!-- Mobile Drawer Navigation -->
        <div id="mobileMenu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 pt-3 pb-6 space-y-3 shadow-xl">
            <a href="/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">&larr; Home</a>
            <a href="/business-setup/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Business Setup &amp; Formation</a>
            <a href="/gst-advisory/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">GST Advisory &amp; Filings</a>
            <a href="/corporate-governance/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Corporate Governance &amp; MCA</a>
            <a href="/direct-tax/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Direct Tax &amp; TDS</a>
            <a href="/brand-protection/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Brand Protection &amp; Trademarks</a>
            <a href="/workforce-digital/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Workforce &amp; Digital Infrastructure</a>
            <a href="/knowledge/" class="block text-sm font-semibold text-brand-sky py-2 border-b border-slate-100">Knowledge Hub</a>
            <a href="/experts.html" class="flex text-sm font-semibold text-brand-sky py-2 border-b border-slate-100 items-center justify-between">
                <span>Talk to CA/CS Experts</span>
                <span class="bg-brand-goldLight text-brand-gold text-[10px] px-2 py-0.5 rounded-full font-bold uppercase">Live</span>
            </a>
            <div class="pt-2 flex flex-col gap-2">
                <a href="tel:+918606918247" class="block w-full text-center bg-slate-100 text-slate-800 font-bold text-sm py-2.5 rounded-lg border border-slate-200">
                    📞 Call: +91 86069 18247
                </a>
            </div>
        </div>
    </header>
"""

FOOTER_HTML = """
    <!-- Global Footer -->
    <footer class="bg-slate-900 text-slate-400 text-xs pt-16 pb-12 border-t border-slate-800 mt-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 mb-12">
                <!-- Brand Summary -->
                <div class="lg:col-span-2 space-y-4">
                    <div class="flex items-center gap-3">
                        <div class="w-9 h-9 bg-gradient-to-tr from-brand-sky to-brand-gold rounded-xl flex items-center justify-center text-white font-black text-lg">
                            C
                        </div>
                        <span class="text-white font-extrabold text-base tracking-tight">CRAFTEGON CORPORATE SERVICES</span>
                    </div>
                    <p class="text-slate-400 text-xs leading-relaxed max-w-sm">
                        Enterprise LegalTech &amp; Compliance Management Platform. Fast-tracking corporate registrations, indirect &amp; direct taxation, regulatory secretarial audits, and trademark filings for Indian and global enterprises.
                    </p>
                    <div class="pt-2 text-slate-300 font-medium space-y-1">
                        <div>🏢 <strong>HQ:</strong> Markaz Knowledge City, Calicut, Kerala 673580</div>
                        <div>📞 <strong>Grievance / Helpline:</strong> <a href="tel:+918606918247" class="text-brand-sky hover:underline">+91 86069 18247</a></div>
                        <div>💬 <strong>WhatsApp Priority:</strong> <a href="https://wa.me/918606918247" class="text-emerald-400 hover:underline">+91 86069 18247</a></div>
                    </div>
                </div>

                <!-- Strategic Practice Hubs -->
                <div>
                    <h4 class="text-white font-bold text-sm mb-4 uppercase tracking-wider">Practice Hubs</h4>
                    <ul class="space-y-2.5">
                        <li><a href="/business-setup/" class="hover:text-white transition">Business Setup &amp; Incorporation</a></li>
                        <li><a href="/gst-advisory/" class="hover:text-white transition">GST Advisory &amp; Return Filing</a></li>
                        <li><a href="/corporate-governance/" class="hover:text-white transition">Corporate Governance &amp; MCA</a></li>
                        <li><a href="/direct-tax/" class="hover:text-white transition">Direct Tax &amp; TDS Filings</a></li>
                        <li><a href="/brand-protection/" class="hover:text-white transition">Brand Protection &amp; Trademarks</a></li>
                        <li><a href="/workforce-digital/" class="hover:text-white transition">Workforce &amp; Digital Infrastructure</a></li>
                    </ul>
                </div>

                <!-- Knowledge Hub -->
                <div>
                    <h4 class="text-white font-bold text-sm mb-4 uppercase tracking-wider">Knowledge Guides</h4>
                    <ul class="space-y-2.5">
                        <li><a href="/knowledge/pvt-ltd-incorporation-guide.html" class="hover:text-white transition">Pvt Ltd Incorporation Manual</a></li>
                        <li><a href="/knowledge/gst-registration-guide.html" class="hover:text-white transition">GST Registration &amp; ITC Guide</a></li>
                        <li><a href="/knowledge/trademark-registration-guide.html" class="hover:text-white transition">Trademark Search &amp; TM-A Filing</a></li>
                        <li><a href="/knowledge/annual-roc-filing-guide.html" class="hover:text-white transition">Annual ROC Compliance (AOC-4)</a></li>
                        <li><a href="/knowledge/corporate-itr-tax-audit-guide.html" class="hover:text-white transition">Corporate ITR &amp; Tax Audit</a></li>
                        <li><a href="/knowledge/dpdp-compliance-guide.html" class="hover:text-white transition">DPDP Act 2023 Implementation</a></li>
                    </ul>
                </div>

                <!-- Corporate Legal Links -->
                <div>
                    <h4 class="text-white font-bold text-sm mb-4 uppercase tracking-wider">Corporate &amp; Legal</h4>
                    <ul class="space-y-2.5">
                        <li><a href="/about.html" class="hover:text-white transition">About CraftEgon</a></li>
                        <li><a href="/contact.html" class="hover:text-white transition">Contact &amp; Grievances</a></li>
                        <li><a href="/experts.html" class="hover:text-white transition">Empaneled CA/CS Directory</a></li>
                        <li><a href="/terms-and-conditions.html" class="hover:text-white transition">Terms &amp; Conditions</a></li>
                        <li><a href="/privacy-policy.html" class="hover:text-white transition">Privacy Policy</a></li>
                        <li><a href="/data-policy.html" class="hover:text-white transition">Data Protection Policy</a></li>
                    </ul>
                </div>
            </div>

            <!-- Mandatory Statutory Regulatory Notice -->
            <div class="pt-8 border-t border-slate-800 text-[11px] leading-relaxed text-slate-500">
                <p>
                    <strong>Regulatory Notice:</strong> CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform. CCS is not a law firm and does not provide court litigation or judicial representation before courts or tribunals. All court litigation and tribunal appearances are executed exclusively through independent, licensed advocates or associate law firms in accordance with the Advocates Act, 1961. Statutory audits, tax certifications, and regulated professional services are fulfilled by qualified, independent Chartered Accountants, Company Secretaries, and registered professionals in compliance with ICAI, ICSI, and statutory guidelines.
                </p>
                <div class="mt-4 flex flex-col sm:flex-row items-center justify-between gap-2 text-slate-600">
                    <div>&copy; 2026 CraftEgon Corporate Services Private Limited. All Rights Reserved.</div>
                    <div class="flex items-center gap-4">
                        <a href="/privacy-policy.html" class="hover:underline">Privacy Policy</a>
                        <span>&middot;</span>
                        <a href="/terms-and-conditions.html" class="hover:underline">Terms of Service</a>
                        <span>&middot;</span>
                        <a href="/data-policy.html" class="hover:underline">Data Policy</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
"""

GUIDE_SCRIPTS = """
    <!-- Knowledge Guide Interactive Scripts -->
    <script src="/assets/js/main.js"></script>
    <script src="/assets/js/forms.js"></script>
    <script src="/assets/js/knowledge-hub.js"></script>
    <script>
        // Toggle FAQ accordions
        function toggleFaq(index) {
            var answer = document.getElementById('faq-answer-' + index);
            var icon = document.getElementById('faq-icon-' + index);
            if (answer) {
                var isHidden = answer.classList.contains('hidden');
                answer.classList.toggle('hidden');
                if (icon) {
                    icon.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
                }
            }
        }

        // Mobile nav toggle
        var mobBtn = document.getElementById('mobileMenuBtn');
        var mobMenu = document.getElementById('mobileMenu');
        if (mobBtn && mobMenu) {
            mobBtn.addEventListener('click', function() {
                mobMenu.classList.toggle('hidden');
            });
        }

        // Sidebar consultation submission
        function handleSidebarSubmit(e) {
            e.preventDefault();
            var form = e.target;
            var btn = document.getElementById('sidebarSubmitBtn');
            var data = Object.fromEntries(new FormData(form));

            btn.disabled = true;
            btn.innerHTML = 'Connecting to Legal Desk...';

            var waMsg = encodeURIComponent(
                '*Craftegon Knowledge Hub Inquiry*\\n' +
                '• Name: ' + data.name + '\\n' +
                '• Phone: ' + data.phone + '\\n' +
                '• Topic: ' + data.service + '\\n' +
                '• Desk: Requesting 10-Minute CA Consultation'
            );

            setTimeout(function() {
                window.open('https://wa.me/918606918247?text=' + waMsg, '_blank');
                btn.disabled = false;
                btn.innerHTML = 'Connected! Thank you.';
                btn.classList.add('bg-emerald-600');
                form.reset();
            }, 500);
        }
    </script>
"""

INDEX_SCRIPTS = """
    <script src="/assets/js/main.js"></script>
    <script src="/assets/js/forms.js"></script>
    <script src="/assets/js/knowledge-hub.js"></script>
    <script>
        var mobBtn = document.getElementById('mobileMenuBtn');
        var mobMenu = document.getElementById('mobileMenu');
        if (mobBtn && mobMenu) {
            mobBtn.addEventListener('click', function() {
                mobMenu.classList.toggle('hidden');
            });
        }
    </script>
"""

def generate_guide_page(guide):
    title = html.escape(guide['title'])
    meta_desc = html.escape(guide['meta_description'])
    slug = guide['slug']
    cat_key = guide.get('category', 'business-setup')
    cat_info = CATEGORY_HUBS.get(cat_key, {"name": "Corporate Compliance", "hub_url": "/"})
    hub_name = html.escape(cat_info['name'])
    hub_url = cat_info['hub_url']
    sections = guide.get('detailed_sections', {})

    # Steps HTML
    steps_html = ""
    for s in sections.get('step_by_step_procedure', []):
        steps_html += f"""
        <div class="flex gap-4 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-brand-sky/40 transition">
            <div class="w-10 h-10 rounded-xl bg-brand-sky text-white flex items-center justify-center font-extrabold text-base shrink-0 shadow-sm">
                {s['step']}
            </div>
            <div>
                <h4 class="text-base font-bold text-brand-dark mb-1">{html.escape(s['title'])}</h4>
                <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">{html.escape(s['detail'])}</p>
            </div>
        </div>
        """

    # Eligibility HTML
    eligibility_html = "".join([f'<li class="flex items-start gap-2.5 text-xs sm:text-sm text-slate-700"><span class="text-emerald-500 font-bold shrink-0">✓</span><span>{html.escape(item)}</span></li>' for item in sections.get('eligibility', [])])

    # Documents HTML
    docs_html = "".join([f'<div class="flex items-start gap-2.5 p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700 font-medium"><span class="text-brand-sky font-bold shrink-0">📄</span><span>{html.escape(item)}</span></div>' for item in sections.get('required_documents', [])])

    # Compliance Checklist Table
    compliance_rows = "".join([f'<tr class="border-b border-slate-100 hover:bg-slate-50 transition"><td class="py-3 px-4 font-bold text-brand-dark text-xs whitespace-nowrap">{html.escape(item.get("timeline", ""))}</td><td class="py-3 px-4 text-slate-600 text-xs">{html.escape(item.get("compliance", ""))}</td></tr>' for item in sections.get('compliance_checklist', [])])

    # FAQs HTML
    faqs_html = ""
    for idx, f in enumerate(guide.get('faqs', [])):
        faqs_html += f"""
        <div class="border border-slate-200 rounded-xl overflow-hidden bg-white">
            <button onclick="toggleFaq({idx})" class="w-full text-left px-5 py-4 font-bold text-xs sm:text-sm text-brand-dark flex items-center justify-between hover:bg-slate-50 transition">
                <span>{html.escape(f['question'])}</span>
                <span id="faq-icon-{idx}" class="text-slate-400 font-bold ml-2 transition-transform transform">▼</span>
            </button>
            <div id="faq-answer-{idx}" class="hidden px-5 pb-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                {html.escape(f['answer'])}
            </div>
        </div>
        """

    page_html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | CraftEgon Knowledge Hub</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://corporateservices.craftegon.com/knowledge/{slug}.html" />
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- Production Compiled Stylesheets -->
    <link rel="stylesheet" href="/assets/css/output.css" />
    <link rel="stylesheet" href="/assets/css/theme.css" />
</head>
<body class="bg-slate-50 text-brand-dark font-sans antialiased min-h-screen flex flex-col justify-between">

{NAVBAR_HTML}

    <!-- Main Content Container -->
    <main class="flex-grow py-10 md:py-14">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Breadcrumbs -->
            <nav class="flex items-center gap-2 text-xs text-slate-500 mb-6 font-medium" aria-label="Breadcrumb">
                <a href="/" class="hover:text-brand-sky transition">Home</a>
                <span>/</span>
                <a href="/knowledge/" class="hover:text-brand-sky transition">Knowledge Hub</a>
                <span>/</span>
                <a href="{hub_url}" class="hover:text-brand-sky transition">{hub_name}</a>
                <span>/</span>
                <span class="text-slate-800 font-semibold truncate max-w-xs">{title}</span>
            </nav>

            <!-- Guide Header Hero -->
            <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-sm mb-10">
                <div class="flex flex-wrap items-center gap-2 mb-4">
                    <span class="bg-brand-skyLight text-brand-sky text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">
                        {hub_name}
                    </span>
                    <span class="bg-slate-100 text-slate-600 text-xs font-medium px-3 py-1 rounded-full">
                        ⏱️ {guide.get('read_time', '6 min read')}
                    </span>
                    <span class="bg-emerald-50 text-emerald-700 text-xs font-semibold px-3 py-1 rounded-full">
                        Verified 2026 Edition
                    </span>
                </div>

                <h1 class="text-2xl sm:text-3xl md:text-4xl font-extrabold text-brand-dark tracking-tight leading-tight mb-4">
                    {title}
                </h1>

                <p class="text-sm sm:text-base text-slate-600 leading-relaxed max-w-4xl">
                    {html.escape(sections.get('overview', ''))}
                </p>

                <div class="mt-6 pt-6 border-t border-slate-100 flex flex-wrap items-center justify-between gap-4 text-xs text-slate-500">
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-brand-sky text-white flex items-center justify-center font-bold text-xs">
                            CE
                        </div>
                        <div>
                            <span class="font-bold text-brand-dark block">CraftEgon Legal &amp; Tax Research Desk</span>
                            <span>Reviewed by Fellow Chartered Accountants &amp; Company Secretaries</span>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20have%20a%20question%20regarding%20{title}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-[#25D366] hover:bg-[#20bd5a] text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-sm transition">
                            <span>💬 Ask CA on WhatsApp</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Two-Column Article Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
                <!-- Main Article Column (8 Cols) -->
                <div class="lg:col-span-8 space-y-10">
                    
                    <!-- Table of Contents -->
                    <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm">
                        <h3 class="text-sm font-bold text-brand-dark uppercase tracking-wider mb-3 flex items-center gap-2">
                            <span>📌</span> In This Practical Manual
                        </h3>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-semibold text-brand-sky">
                            <a href="#eligibility" class="hover:underline flex items-center gap-1.5 p-1"><span>1.</span> Eligibility &amp; Prerequisites</a>
                            <a href="#procedure" class="hover:underline flex items-center gap-1.5 p-1"><span>2.</span> Step-by-Step Filing Procedure</a>
                            <a href="#documents" class="hover:underline flex items-center gap-1.5 p-1"><span>3.</span> Mandatory Document Checklist</a>
                            <a href="#compliance" class="hover:underline flex items-center gap-1.5 p-1"><span>4.</span> Post-Approval Compliance Slabs</a>
                            <a href="#faqs" class="hover:underline flex items-center gap-1.5 p-1"><span>5.</span> Frequently Asked Questions</a>
                            <a href="#advisory" class="hover:underline flex items-center gap-1.5 p-1"><span>6.</span> Expert CA/CS Consultation</a>
                        </div>
                    </div>

                    <!-- Section: Eligibility -->
                    <section id="eligibility" class="scroll-mt-24 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="text-2xl">📋</span>
                            <h2 class="text-xl sm:text-2xl font-extrabold text-brand-dark">1. Eligibility Criteria &amp; Statutory Requirements</h2>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                            Prior to initiating electronic filings on government portals (MCA V3, GSTN, or IP India), ensure full compliance with the following statutory parameters:
                        </p>
                        <ul class="space-y-3 pt-2">
                            {eligibility_html}
                        </ul>
                    </section>

                    <!-- Section: Step-by-Step Procedure -->
                    <section id="procedure" class="scroll-mt-24 space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="text-2xl">⚙️</span>
                            <h2 class="text-xl sm:text-2xl font-extrabold text-brand-dark">2. Step-by-Step Filing Procedure</h2>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-600">
                            Our streamlined end-to-end execution workflow designed to minimize rejection queries and achieve fastest statutory approval:
                        </p>
                        <div class="space-y-4 pt-2">
                            {steps_html}
                        </div>
                    </section>

                    <!-- Section: Documents Required -->
                    <section id="documents" class="scroll-mt-24 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="text-2xl">📁</span>
                            <h2 class="text-xl sm:text-2xl font-extrabold text-brand-dark">3. Mandatory Document Checklist</h2>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-600">
                            Keep these documents scanned and self-attested in clear high-resolution PDF/JPEG format:
                        </p>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                            {docs_html}
                        </div>
                    </section>

                    <!-- Section: Compliance Timelines -->
                    <section id="compliance" class="scroll-mt-24 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="text-2xl">⏳</span>
                            <h2 class="text-xl sm:text-2xl font-extrabold text-brand-dark">4. Post-Registration Compliance Slabs</h2>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-600">
                            Failure to adhere to post-registration filing dates attracts heavy recurring statutory fines and director disqualification risks:
                        </p>
                        <div class="overflow-x-auto rounded-xl border border-slate-200 mt-2">
                            <table class="w-full text-left border-collapse">
                                <thead>
                                    <tr class="bg-slate-100 text-slate-700 text-xs uppercase tracking-wider font-bold">
                                        <th class="py-3 px-4">Statutory Due Date</th>
                                        <th class="py-3 px-4">Compliance Requirement</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {compliance_rows}
                                </tbody>
                            </table>
                        </div>
                    </section>

                    <!-- Section: FAQs -->
                    <section id="faqs" class="scroll-mt-24 space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="text-2xl">💡</span>
                            <h2 class="text-xl sm:text-2xl font-extrabold text-brand-dark">5. Frequently Asked Questions</h2>
                        </div>
                        <div class="space-y-3 pt-2">
                            {faqs_html}
                        </div>
                    </section>

                    <!-- Section: Next Steps CTA -->
                    <div id="advisory" class="p-8 rounded-3xl bg-gradient-to-r from-brand-sky to-brand-skyHover text-white shadow-lg space-y-4">
                        <h3 class="text-xl sm:text-2xl font-black">Need Dedicated CA/CS Assistance for {title}?</h3>
                        <p class="text-xs sm:text-sm text-sky-100 leading-relaxed max-w-xl">
                            Our team of empaneled Chartered Accountants and Corporate Lawyers manage your entire drafting, digital signature verification, and government filing with guaranteed turnaround times.
                        </p>
                        <div class="flex flex-wrap gap-4 pt-2">
                            <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20want%20to%20apply%20for%20{title}" target="_blank" rel="noopener noreferrer" class="bg-white text-brand-sky hover:bg-slate-100 font-extrabold text-xs sm:text-sm px-6 py-3.5 rounded-xl shadow transition">
                                Start Application via WhatsApp &rarr;
                            </a>
                            <a href="tel:+918606918247" class="bg-sky-800/80 hover:bg-sky-800 text-white font-bold text-xs sm:text-sm px-5 py-3.5 rounded-xl transition border border-white/20">
                                📞 Call Direct Desk
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Sticky Sidebar (4 Cols) -->
                <div class="lg:col-span-4 space-y-6">
                    <!-- Quick Lead Intake Card -->
                    <div class="sticky top-28 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-xl space-y-5">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold uppercase tracking-wider text-brand-sky bg-brand-skyLight px-2.5 py-1 rounded-md">Instant Filing</span>
                            <span class="text-[11px] font-bold text-emerald-600 flex items-center gap-1">
                                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                                Specialist Online
                            </span>
                        </div>

                        <div>
                            <h3 class="text-lg font-bold text-brand-dark">Request 10-Min Callback</h3>
                            <p class="text-xs text-slate-500 mt-1">Get immediate quote &amp; timeline from an empaneled professional.</p>
                        </div>

                        <form id="knowledgeSidebarForm" class="space-y-4" onsubmit="handleSidebarSubmit(event)">
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1">Your Full Name *</label>
                                <input type="text" name="name" required placeholder="e.g. Vikram Malhotra" class="w-full px-3.5 py-2.5 text-xs sm:text-sm rounded-xl bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1">WhatsApp / Phone Number *</label>
                                <input type="tel" name="phone" required placeholder="+91 86069 18247" class="w-full px-3.5 py-2.5 text-xs sm:text-sm rounded-xl bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1">Target Service</label>
                                <input type="text" name="service" readonly value="{title}" class="w-full px-3.5 py-2.5 text-xs rounded-xl bg-slate-100 border border-slate-200 text-slate-600 font-semibold cursor-not-allowed">
                            </div>

                            <button type="submit" id="sidebarSubmitBtn" class="w-full bg-brand-sky hover:bg-brand-skyHover text-white font-extrabold text-xs sm:text-sm py-3 rounded-xl shadow-md hover:shadow-lg transition">
                                Request Priority Consultation &rarr;
                            </button>
                        </form>

                        <div class="pt-4 border-t border-slate-100 flex items-center justify-center gap-3 text-slate-500 text-xs">
                            <span>🛡️ 100% Confidential</span>
                            <span>·</span>
                            <span>⚡ 10-Min Response</span>
                        </div>

                        <!-- Hub Quick Links -->
                        <div class="pt-4 border-t border-slate-100">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Explore {hub_name}</h4>
                            <a href="{hub_url}" class="block text-xs font-bold text-brand-sky hover:underline">
                                Browse all {hub_name} services &rarr;
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

{FOOTER_HTML}

{GUIDE_SCRIPTS}
</body>
</html>
"""
    return page_html

def generate_knowledge_index(guides):
    cards_html = ""
    for g in guides:
        cat_key = g.get('category', 'business-setup')
        cat_info = CATEGORY_HUBS.get(cat_key, {"name": "Corporate Law", "hub_url": "/"})
        title = html.escape(g['title'])
        meta = html.escape(g['meta_description'])
        slug = g['slug']
        read_time = g.get('read_time', '5 min read')
        hub_name = html.escape(cat_info['name'])

        cards_html += f"""
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between group">
            <div>
                <div class="flex items-center justify-between mb-4">
                    <span class="text-[11px] font-bold text-brand-sky uppercase bg-brand-skyLight px-3 py-1 rounded-full">
                        {hub_name}
                    </span>
                    <span class="text-xs text-slate-400 font-medium">⏱️ {read_time}</span>
                </div>
                <h3 class="text-lg font-bold text-brand-dark group-hover:text-brand-sky transition line-clamp-2 mb-2">
                    <a href="/knowledge/{slug}.html">{title}</a>
                </h3>
                <p class="text-xs sm:text-sm text-slate-500 leading-relaxed line-clamp-3 mb-6">
                    {meta}
                </p>
            </div>
            <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                <a href="/knowledge/{slug}.html" class="text-xs font-bold text-brand-sky hover:text-brand-skyHover flex items-center gap-1">
                    <span>Read Complete Manual</span>
                    <span>&rarr;</span>
                </a>
                <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20have%20questions%20regarding%20{title}" target="_blank" rel="noopener noreferrer" class="text-[11px] font-bold text-emerald-600 hover:text-emerald-700">
                    Ask on WhatsApp
                </a>
            </div>
        </div>
        """

    index_html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corporate Compliance &amp; Legal Knowledge Hub | CraftEgon Corporate Services</title>
    <meta name="description" content="Official regulatory guides and statutory manuals for Private Limited company setup, GST registration, Trademark filing, Annual ROC compliance, and DPDP Act in India.">
    <link rel="canonical" href="https://corporateservices.craftegon.com/knowledge/" />
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- Production Compiled Stylesheets -->
    <link rel="stylesheet" href="/assets/css/output.css" />
    <link rel="stylesheet" href="/assets/css/theme.css" />
</head>
<body class="bg-slate-50 text-brand-dark font-sans antialiased min-h-screen flex flex-col justify-between">

{NAVBAR_HTML}

    <main class="flex-grow py-12 md:py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Header Hero -->
            <div class="text-center max-w-3xl mx-auto mb-14">
                <span class="text-xs font-bold text-brand-sky uppercase tracking-widest bg-brand-skyLight px-3.5 py-1.5 rounded-full inline-block mb-3">
                    Corporate LegalTech Knowledge Engine
                </span>
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-brand-dark tracking-tight mb-4">
                    Statutory Manuals &amp; Compliance Guides
                </h1>
                <p class="text-sm sm:text-base text-slate-600 leading-relaxed">
                    Authoritative, step-by-step procedures, MCA V3 electronic filing checklists, and regulatory tax guidelines authored and verified by practicing Chartered Accountants and Company Secretaries.
                </p>
            </div>

            <!-- Guides Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {cards_html}
            </div>
        </div>
    </main>

{FOOTER_HTML}

{INDEX_SCRIPTS}
</body>
</html>
"""
    return index_html

def main():
    print("Compiling Standalone Knowledge Pages...")
    with open('data/craftegon-knowledge-hub.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    guides = data.get('guides', [])
    os.makedirs('knowledge', exist_ok=True)

    # 1. Generate individual guide pages
    for g in guides:
        slug = g['slug']
        filepath = os.path.join('knowledge', f"{slug}.html")
        page_content = generate_guide_page(g)
        with open(filepath, 'w', encoding='utf-8') as out_f:
            out_f.write(page_content)
        print(f"Generated: {filepath}")

    # 2. Generate knowledge index page
    index_content = generate_knowledge_index(guides)
    index_path = os.path.join('knowledge', 'index.html')
    with open(index_path, 'w', encoding='utf-8') as out_f:
        out_f.write(index_content)
    print(f"Generated: {index_path}")

    print(f"Successfully compiled {len(guides)} standalone knowledge guide pages in /knowledge/!")

if __name__ == '__main__':
    main()
