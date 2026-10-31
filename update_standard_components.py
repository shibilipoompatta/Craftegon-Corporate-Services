# -*- coding: utf-8 -*-
"""
Helper script to standardize experts.html, contact.html, and embed fee calculator into pvt-ltd.html.
"""
import re

ANNOUNCEMENT_BAR = """    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-brand-sky to-brand-skyHover text-white text-xs md:text-sm py-2 px-4 text-center font-medium shadow-sm flex items-center justify-center gap-2">
        <span>🚀 <strong>Special Offer:</strong> Get 20% OFF MCA Filing &amp; Free Expert Consultation this week!</span>
        <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20want%20to%20claim%20the%2020%25%20OFF%20MCA%20Filing%20offer." target="_blank" rel="noopener noreferrer" class="underline hover:text-brand-goldLight font-bold transition ml-2">Claim Offer &rarr;</a>
    </div>"""

GLOBAL_HEADER = """    <!-- Header Navigation -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200">
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

            <!-- CTA Buttons & Mobile Toggle -->
            <div class="flex items-center gap-3">
                <a href="tel:+918606918247" class="hidden sm:flex items-center gap-2 text-xs font-bold text-slate-700 bg-brand-slate px-4 py-2.5 rounded-lg border border-slate-200 hover:bg-slate-200 transition">
                    <span class="text-emerald-600 font-bold">●</span> +91 86069 18247
                </a>
                <a href="/contact.html" class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs md:text-sm px-5 py-2.5 rounded-lg shadow-md hover:shadow-lg transition">
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
            <a href="/experts.html" class="block text-sm font-semibold text-brand-sky py-2 border-b border-slate-100 flex items-center justify-between">
                <span>Talk to CA/CS Experts</span>
                <span class="bg-brand-goldLight text-brand-gold text-[10px] px-2 py-0.5 rounded-full font-bold uppercase">Live</span>
            </a>
            <a href="/about.html" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">About CraftEgon</a>
            <a href="/contact.html" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Contact &amp; Grievance Desk</a>
            <div class="pt-2 flex flex-col gap-2">
                <a href="tel:+918606918247" class="block w-full text-center bg-slate-100 text-slate-800 font-bold text-sm py-2.5 rounded-lg border border-slate-200">
                    📞 Call: +91 86069 18247
                </a>
                <a href="/contact.html" class="block w-full text-center bg-brand-sky text-white font-bold text-sm py-2.5 rounded-lg shadow">
                    Get Free Consultation
                </a>
            </div>
        </div>
    </header>"""

GLOBAL_FOOTER = """    <!-- Global Standardized Footer -->
    <footer class="bg-brand-dark text-slate-400 text-xs py-14 border-t border-slate-800">
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
                    <p class="text-[11px] text-slate-400 leading-relaxed text-justify">
                        <strong class="text-brand-gold uppercase">Regulatory Notice:</strong> CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform. CCS is not a law firm and does not provide court litigation or judicial representation before courts or tribunals. All court litigation and tribunal appearances are executed exclusively through independent, licensed advocates or associate law firms in accordance with the Advocates Act, 1961. Statutory audits, tax certifications, and regulated professional services are fulfilled by qualified, independent Chartered Accountants, Company Secretaries, and registered professionals in compliance with ICAI, ICSI, and statutory guidelines.
                    </p>
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

def update_experts():
    with open('experts.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update <head>
    head_pattern = r'<head>.*?</head>'
    new_head = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Talk to Experts &amp; CA Consultation - Craftegon Corporate Services</title>
    <meta name="description" content="Book 1-on-1 consultations with verified Chartered Accountants, Company Secretaries, and IP Attorneys across 60 corporate practice areas.">
    <link rel="canonical" href="https://corporateservices.craftegon.com/experts.html" />

    <!-- Google Fonts: Plus Jakarta Sans & DM Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- Production Compiled Stylesheets -->
    <link rel="stylesheet" href="/assets/css/output.css" />
    <link rel="stylesheet" href="/assets/css/theme.css" />
</head>"""
    html = re.sub(head_pattern, new_head, html, flags=re.DOTALL)

    # 2. Update Announcement bar and header
    top_pattern = r'<div class="bg-gradient-to-r from-brand-sky.*?<!-- Main Section -->'
    new_top = ANNOUNCEMENT_BAR + "\n\n" + GLOBAL_HEADER + "\n\n    <!-- Main Section -->"
    html = re.sub(top_pattern, new_top, html, flags=re.DOTALL)

    # 3. Update footer
    footer_pattern = r'<!-- Master Corporate Footer -->.*?</footer>'
    html = re.sub(footer_pattern, GLOBAL_FOOTER, html, flags=re.DOTALL)

    # 4. Ensure scripts at bottom
    if '/assets/js/main.js' not in html:
        html = html.replace('</body>', '    <script src="/assets/js/main.js"></script>\n    <script src="/assets/js/knowledge-hub.js"></script>\n</body>')

    with open('experts.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated experts.html")

def update_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update <head>
    head_pattern = r'<head>.*?</head>'
    new_head = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us &amp; Consultation - Craftegon Corporate Services</title>
    <meta name="description" content="Get in touch with Craftegon Corporate Services. Corporate Headquarters at Markaz Knowledge City, Kozhikode &amp; Technopark, Trivandrum.">
    <link rel="canonical" href="https://corporateservices.craftegon.com/contact.html" />

    <!-- Google Fonts: Plus Jakarta Sans & DM Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- Production Compiled Stylesheets -->
    <link rel="stylesheet" href="/assets/css/output.css" />
    <link rel="stylesheet" href="/assets/css/theme.css" />
</head>"""
    html = re.sub(head_pattern, new_head, html, flags=re.DOTALL)

    # 2. Update Announcement bar and header
    top_pattern = r'<div class="bg-gradient-to-r from-brand-sky.*?<!-- Main Content Wrapper -->'
    new_top = ANNOUNCEMENT_BAR + "\n\n" + GLOBAL_HEADER + "\n\n    <!-- Main Content Wrapper -->"
    html = re.sub(top_pattern, new_top, html, flags=re.DOTALL)

    # 3. Update footer
    footer_pattern = r'<footer class="bg-brand-dark.*?</footer>'
    html = re.sub(footer_pattern, GLOBAL_FOOTER, html, flags=re.DOTALL)

    # 4. Update scripts
    if '/assets/js/main.js' not in html:
        html = html.replace('</body>', '    <script src="/assets/js/main.js"></script>\n    <script src="/assets/js/knowledge-hub.js"></script>\n</body>')

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated contact.html")

def update_pvt_ltd():
    with open('pvt-ltd.html', 'r', encoding='utf-8') as f:
        html = f.read()

    calc_section = """
        <!-- Interactive Fee Structure & Stamp Duty Breakdown -->
        <section class="py-16 bg-slate-50 border-y border-slate-200" id="fee-calculator">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-8">
                    <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">State-Wise Fee Transparency</h2>
                    <h3 class="text-2xl md:text-3xl font-extrabold text-brand-dark">Fee Structure &amp; Stamp Duty Breakdown</h3>
                    <p class="text-xs text-slate-500 mt-1">Government stamp duties are computed based on state stamp laws and authorized capital.</p>
                </div>
                
                <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm" data-calc-ready="true">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                        <div>
                            <label class="block text-xs font-bold uppercase text-slate-700 mb-1" for="pvt-calc-state">State of Registration</label>
                            <select id="pvt-calc-state" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition-all shadow-sm">
                                <option value="Kerala" selected>Kerala</option>
                                <option value="Maharashtra">Maharashtra</option>
                                <option value="Karnataka">Karnataka</option>
                                <option value="Delhi">Delhi</option>
                                <option value="Tamil Nadu">Tamil Nadu</option>
                                <option value="Telangana">Telangana</option>
                                <option value="Gujarat">Gujarat</option>
                                <option value="Uttar Pradesh">Uttar Pradesh</option>
                                <option value="West Bengal">West Bengal</option>
                                <option value="Rajasthan">Rajasthan</option>
                                <option value="Haryana">Haryana</option>
                                <option value="Punjab">Punjab</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase text-slate-700 mb-1" for="pvt-calc-capital">Authorized Capital</label>
                            <select id="pvt-calc-capital" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition-all shadow-sm">
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
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                            <span class="block text-[10px] uppercase font-bold text-slate-500">Professional Fee</span>
                            <span class="font-black text-sm text-brand-dark mt-1 block">₹6,999</span>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                            <span class="block text-[10px] uppercase font-bold text-slate-500">State Stamp Duty</span>
                            <span id="pvt-stamp-duty" class="font-black text-sm text-brand-gold mt-1 block">₹5,000</span>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                            <span class="block text-[10px] uppercase font-bold text-slate-500">GST (18%)</span>
                            <span id="pvt-gst-amount" class="font-black text-sm text-brand-dark mt-1 block">₹1,260</span>
                        </div>
                        <div class="p-3 bg-brand-skyLight rounded-xl border border-brand-sky/30">
                            <span class="block text-[10px] uppercase font-bold text-brand-sky">Estimated Total</span>
                            <span id="pvt-total-fee" class="font-black text-sm text-brand-dark mt-1 block">₹13,259</span>
                        </div>
                    </div>

                    <!-- Itemized Statutory Formula Breakdown -->
                    <div id="pvt-breakdown-note" class="mt-4 p-3.5 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-600 leading-relaxed">
                        <span class="font-semibold text-brand-dark">Statutory Breakdown (Kerala · ₹10 Lakhs Capital):</span>
                        <span class="font-mono text-slate-700 ml-1">₹6,999 (Prof) + ₹5,000 (Stamp Duty) + ₹1,260 (GST 18%) = <strong>₹13,259</strong></span>
                    </div>

                    <!-- Direct Quote & WhatsApp Action -->
                    <div class="mt-6 flex flex-wrap items-center gap-3">
                        <a href="#pvt-form" class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs px-5 py-2.5 rounded-lg shadow transition">
                            Get a Free Quote &rarr;
                        </a>
                        <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20want%20a%20statutory%20fee%20quote%20for%20Private%20Limited%20Company%20Incorporation" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-[#25D366]/10 border border-[#25D366]/40 text-[#128C7E] hover:bg-[#25D366]/20 font-bold text-xs px-4 py-2.5 rounded-lg transition">
                            <span>💬 Ask on WhatsApp</span>
                        </a>
                    </div>

                    <!-- Disclaimer Alert -->
                    <div class="mt-6 p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center gap-2.5">
                        <span class="text-base shrink-0">ℹ️</span>
                        <p class="leading-relaxed">
                            Estimates are indicative. Stamp duty rates are subject to change per state government notifications. Government fees are charged at actuals. Final invoice will reflect current applicable rates.
                        </p>
                    </div>
                </div>
            </div>
        </section>
"""
    if 'id="fee-calculator"' not in html:
        target = '</section>\n\n        <!-- 3-Step Process Visual -->'
        replacement = '</section>\n' + calc_section + '\n        <!-- 3-Step Process Visual -->'
        if target in html:
            html = html.replace(target, replacement)
        else:
            # Try alternate newline
            target_crlf = '</section>\r\n\r\n        <!-- 3-Step Process Visual -->'
            html = html.replace(target_crlf, '</section>\r\n' + calc_section + '\r\n        <!-- 3-Step Process Visual -->')

    # Add calculator script and updater logic
    calc_script = """
    <!-- Fee Calculator Engine -->
    <script src="/assets/js/calculator.js"></script>
    <script>
        const pvtState = document.getElementById('pvt-calc-state');
        const pvtCap = document.getElementById('pvt-calc-capital');
        const pvtDuty = document.getElementById('pvt-stamp-duty');
        const pvtGst = document.getElementById('pvt-gst-amount');
        const pvtTotal = document.getElementById('pvt-total-fee');
        const pvtNote = document.getElementById('pvt-breakdown-note');
        const pvtBaseFee = 6999;

        function updatePvtCalc() {
            if (window.CCSCalculator && window.CCSCalculator.calculateTotalFee && pvtState && pvtCap) {
                const state = pvtState.value;
                const capital = parseInt(pvtCap.value, 10);
                const res = window.CCSCalculator.calculateTotalFee(pvtBaseFee, state, capital);
                if (pvtDuty) pvtDuty.textContent = '₹' + res.stamp_duty.toLocaleString('en-IN');
                if (pvtGst) pvtGst.textContent = '₹' + res.gst_amount.toLocaleString('en-IN');
                if (pvtTotal) pvtTotal.textContent = '₹' + res.total.toLocaleString('en-IN');
                if (pvtNote) {
                    pvtNote.innerHTML = '<span class="font-semibold text-brand-dark">Statutory Breakdown (' + state + ' · ₹' + capital.toLocaleString('en-IN') + ' Capital):</span> <span class="font-mono text-slate-700 ml-1">₹' + pvtBaseFee.toLocaleString('en-IN') + ' (Prof) + ₹' + res.stamp_duty.toLocaleString('en-IN') + ' (Stamp Duty) + ₹' + res.gst_amount.toLocaleString('en-IN') + ' (GST 18%) = <strong>₹' + res.total.toLocaleString('en-IN') + '</strong></span>';
                }
            }
        }

        if (pvtState && pvtCap) {
            pvtState.addEventListener('change', updatePvtCalc);
            pvtCap.addEventListener('change', updatePvtCalc);
            updatePvtCalc();
        }
    </script>
</body>"""

    if '/assets/js/calculator.js' not in html:
        html = html.replace('</body>', calc_script)

    with open('pvt-ltd.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated pvt-ltd.html with fee calculator")

if __name__ == '__main__':
    update_experts()
    update_contact()
    update_pvt_ltd()
