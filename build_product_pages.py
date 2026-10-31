# -*- coding: utf-8 -*-
"""
Builds the 12 High-Intent Phase 1 Product Pages with the new modern LegalTech UI/UX design:
- Plus Jakarta Sans typography
- Sky Blue (#0284C7), Sky Light (#E0F2FE), Slate (#F1F5F9), Gold (#D97706), Dark (#0F172A)
- 9-Part High-Conversion Layout
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

PRODUCT_DETAILS = {
    "private-limited-company-incorporation": {
        "statutory_badge_note": "",
        "detailed_framework": """Under Section 7 of the Companies Act, 2013 and Rule 12 of the Companies (Incorporation) Rules, 2014, the incorporation of a Private Limited Company is processed electronically through the Ministry of Corporate Affairs (MCA) V3 portal via the integrated web form <strong>SPICe+ (INC-32)</strong>.<br><br>
        The SPICe+ architecture encompasses:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Part A:</strong> Reservation of company name through Reserve Unique Name (RUN) web service.</li>
          <li><strong>Part B:</strong> Unified statutory application covering incorporation, allotment of Director Identification Numbers (DIN), mandatory e-MOA (INC-33) and e-AOA (INC-34).</li>
          <li><strong>AGILE-PRO-S (INC-35):</strong> Simultaneous integration for mandatory GSTIN, EPFO, ESIC, Professional Tax Registration (where applicable), Opening of Scheduled Bank Current Account, and Shops & Establishment Code.</li>
          <li><strong>PAN & TAN:</strong> Automated allocation through NSDL/CBDT database integration embedded within Certificate of Incorporation (COI).</li>
        </ul>""",
        "deadlines_table": [
            ("Within 30 Days", "First Board Meeting of Directors", "Section 173(1)", "Mandatory minutes maintenance"),
            ("Within 30 Days", "Appointment of First Statutory Auditor", "Form ADT-1 (Section 139)", "Penalty of ₹100/day on delay"),
            ("Within 180 Days", "Declaration of Commencement of Business", "Form INC-20A (Section 10A)", "Inability to borrow capital; strike-off risk"),
            ("Annual (30 days from AGM)", "Filing Financial Statements", "Form AOC-4 (Section 137)", "₹100 per day continuing penalty"),
            ("Annual (60 days from AGM)", "Filing Annual Return", "Form MGT-7A (Section 92)", "₹100 per day continuing penalty")
        ]
    },
    "llp-registration": {
        "statutory_badge_note": "",
        "detailed_framework": """Limited Liability Partnerships in India are governed under the <strong>Limited Liability Partnership Act, 2008</strong> as amended by the <strong>LLP (Amendment) Act, 2021</strong>, which decriminalized minor procedural defaults.<br><br>
        Incorporation is executed via the <strong>FiLLiP (Form for Incorporation of Limited Liability Partnership)</strong> web form on the MCA V3 portal:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Name Reservation:</strong> RUN-LLP service enabling two proposed name choices reflecting permitted business activities.</li>
          <li><strong>DPIN / DIN Allocation:</strong> Up to two Designated Partners can obtain DPIN directly through FiLLiP without prior standalone filing.</li>
          <li><strong>LLP Agreement (Form 3):</strong> Governed by Section 23 of the LLP Act; must be drafted, stamped per state stamp act rules, and filed within 30 days of registration.</li>
          <li><strong>Permanent Establishment:</strong> Direct issuance of LLPIN, PAN, and TAN on incorporation certificate.</li>
        </ul>""",
        "deadlines_table": [
            ("Within 30 Days", "Filing of LLP Agreement with ROC", "Form 3 (Section 23)", "₹100/day penalty without cap"),
            ("By May 30 Annually", "Annual Return of LLP", "Form 11 (Section 35)", "₹100/day penalty"),
            ("By October 30 Annually", "Statement of Account & Solvency", "Form 8 (Section 34)", "Audit compulsory if turnover > ₹40L or capital > ₹25L")
        ]
    },
    "gst-registration": {
        "statutory_badge_note": "GST litigation before the Appellate Tribunal or High Court is executed via independent licensed Advocates.",
        "detailed_framework": """Goods and Services Tax registration is regulated under Chapter VI (Sections 22 to 30) of the <strong>Central Goods and Services Tax (CGST) Act, 2017</strong> read with Chapter III of the <strong>CGST Rules, 2017</strong>.<br><br>
        Key regulatory contours:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Threshold Limits (Section 22):</strong> ₹40 Lakhs for exclusive supply of goods (₹20 Lakhs in Special Category States) and ₹20 Lakhs for service providers (₹10 Lakhs in Special Category States).</li>
          <li><strong>Compulsory Registration (Section 24):</strong> Irrespective of turnover for inter-state taxable supply, casual taxable persons, reverse charge liability, non-resident taxable persons, and e-commerce operators/suppliers.</li>
          <li><strong>Aadhaar Authentication:</strong> Mandated under Rule 8 for promoters/partners. Failure triggers automated biometric-based physical site verification by GST field officers under Rule 9.</li>
          <li><strong>Form GST REG-01:</strong> Part A (TRN generation) and Part B (comprehensive premise, bank, HSN/SAC, and authorized signatory submission).</li>
        </ul>""",
        "deadlines_table": [
            ("Within 30 Days of Threshold", "Application for GST Registration", "Form GST REG-01", "Loss of input tax credit; Section 122 penalty"),
            ("Monthly by 11th", "Filing Outward Supplies", "Form GSTR-1", "Late fee ₹50/day (₹20 for Nil)"),
            ("Monthly by 20th", "Filing Monthly Return & Tax Settlement", "Form GSTR-3B", "Interest @ 18% p.a. on net tax liability")
        ]
    },
    "monthly-quarterly-gst-return-filing": {
        "statutory_badge_note": "Reconciliation statements under GSTR-9C are audited and certified independently by qualified Chartered Accountants.",
        "detailed_framework": """Continuous indirect tax compliance is governed by Sections 37, 38, and 39 of the <strong>CGST Act, 2017</strong> and Central Tax Notification rules.<br><br>
        Operational mechanism:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Form GSTR-1 (Section 37):</strong> Invoice-wise reporting of B2B outward supplies, export transactions, debit/credit notes, and HSN 4/6-digit summary statements.</li>
          <li><strong>GSTR-2B Automated Reconciliation:</strong> Static monthly statement auto-populated on the 14th reflecting eligible and ineligible ITC. Adherence to Rule 36(4) is strictly enforced.</li>
          <li><strong>Form GSTR-3B (Section 39):</strong> Summary declaration of outward liability, eligible ITC claims, reverse charge liabilities, and cash ledger settlement through PMT-06 challans.</li>
          <li><strong>QRMP Scheme:</strong> Quarterly Return Monthly Payment scheme available for taxpayers with aggregate annual turnover up to ₹5 Crore.</li>
        </ul>""",
        "deadlines_table": [
            ("11th of every month", "GSTR-1 Monthly Outward Supply", "Section 37 / Rule 59", "E-Way Bill generation blocked if 2 periods missed"),
            ("20th of every month", "GSTR-3B Monthly Return & Tax Payment", "Section 39 / Rule 61", "Late fee ₹50/day + 18% interest on cash tax"),
            ("December 31 Annually", "Annual Return Filing", "Form GSTR-9 (Section 44)", "₹200/day late fee subject to 0.5% turnover cap")
        ]
    },
    "annual-mca-roc-filings": {
        "statutory_badge_note": "Statutory audit reports forming the basis of Form AOC-4 are issued independently by qualified Chartered Accountants.",
        "detailed_framework": """Every company registered under the <strong>Companies Act, 2013</strong> is mandated to maintain statutory registers, convene an Annual General Meeting (AGM), and file audited annual returns with the Registrar of Companies (ROC).<br><br>
        Core statutory obligations:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Form AOC-4 (Section 137):</strong> Filing of audited financial statements, balance sheet, profit and loss account, auditor's report, and directors' report within 30 days of the AGM.</li>
          <li><strong>Form MGT-7 / MGT-7A (Section 92):</strong> Annual Return containing shareholding structure, directorship changes, indebtedness, and board meeting disclosures within 60 days of AGM.</li>
          <li><strong>DIR-3 KYC (Rule 12A):</strong> Mandatory annual verification of director credentials by September 30 via Web form or e-Form with personal mobile/email OTP.</li>
          <li><strong>Secretarial Standards:</strong> Compliance with SS-1 (Board Meetings) and SS-2 (General Meetings) issued by ICSI.</li>
        </ul>""",
        "deadlines_table": [
            ("By September 30", "Annual General Meeting (AGM)", "Section 96(1)", "Mandatory within 6 months of FY close"),
            ("By September 30", "Director DIR-3 KYC Filing", "Rule 12A", "Deactivation of DIN; ₹5,000 penalty for reactivation"),
            ("Within 30 Days of AGM", "Filing Financial Statements (AOC-4)", "Section 137", "Continuing penalty of ₹100/day on company and officers"),
            ("Within 60 Days of AGM", "Filing Annual Return (MGT-7/7A)", "Section 92", "Continuing penalty of ₹100/day")
        ]
    },
    "director-kyc-appointment-resignation": {
        "statutory_badge_note": "",
        "detailed_framework": """Corporate board governance, director onboarding, credential maintenance, and resignations are governed under Chapter XI (Sections 149 to 172) of the <strong>Companies Act, 2013</strong> read with the <strong>Companies (Appointment and Qualification of Directors) Rules, 2014</strong>.<br><br>
        Procedural mandates:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>DIR-3 KYC Web / e-Form:</strong> Governed by Rule 12A. Annual re-verification of personal contact details and DSC. Non-filing marks DIN as 'Deactivated due to non-filing of DIR-3 KYC'.</li>
          <li><strong>Director Appointment (Form DIR-12):</strong> Submission of consent in Form DIR-2, intimation of disqualification in DIR-8, MBP-1 disclosure of interest, and ROC filing within 30 days.</li>
          <li><strong>Director Resignation (Form DIR-11 & DIR-12):</strong> Resigning director intimates ROC in Form DIR-11; company files notice of resignation in Form DIR-12 with board resolution.</li>
          <li><strong>Board Quorum:</strong> Ensuring minimum 2 directors for Private Limited and 3 for Public Limited remain active at all times.</li>
        </ul>""",
        "deadlines_table": [
            ("September 30 Annually", "Annual DIR-3 KYC Filing", "Rule 12A", "DIN deactivation; ₹5,000 reactivation fee"),
            ("Within 30 Days of Event", "Intimation of Appointment / Resignation", "Form DIR-12 (Section 152/168)", "Additional MCA late filing slab fees"),
            ("Within 30 Days of Resignation", "Director Individual Resignation Notice", "Form DIR-11 (Section 168)", "Optional but recommended statutory record")
        ]
    },
    "corporate-income-tax-return-filing": {
        "statutory_badge_note": "Tax Audits under Section 44AB and Transfer Pricing Certifications are issued independently by qualified Chartered Accountants.",
        "detailed_framework": """Corporate income tax assessments and annual return filing are governed by the <strong>Income Tax Act, 1961</strong> and annual Finance Acts.<br><br>
        Core tax mechanics:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Form ITR-6:</strong> Compulsory electronic filing for all companies registered in India, signed digitally via Class 3 DSC of the managing director or authorized signatory.</li>
          <li><strong>Section 115BAA Regime:</strong> Concessional corporate tax rate of 22% (effective 25.17% with surcharge and cess) subject to forfeiture of specific exemptions and MAT exemption.</li>
          <li><strong>Minimum Alternate Tax (MAT):</strong> Section 115JB applies to companies in the regular tax regime where normal tax liability is lower than 15% of book profits.</li>
          <li><strong>Advance Tax (Section 208-211):</strong> Four quarterly statutory installments (June 15, Sept 15, Dec 15, March 15) to avoid interest under Sections 234B and 234C.</li>
        </ul>""",
        "deadlines_table": [
            ("October 31 of AY", "ITR-6 Filing for Corporate Audited Entities", "Section 139(1)", "Penal interest under 234A; Section 234F fee"),
            ("Quarterly (15th Jun/Sep/Dec/Mar)", "Advance Tax Installments (15%, 45%, 75%, 100%)", "Section 211", "Interest @ 1% per month under Sections 234B & 234C"),
            ("December 31 of AY", "Belated or Revised Return Deadline", "Section 139(4) & 139(5)", "No revisions permitted after this statutory cutoff")
        ]
    },
    "tds-registration-quarterly-returns": {
        "statutory_badge_note": "",
        "detailed_framework": """Withholding tax compliance is regulated under Chapter XVII-B (Sections 192 to 206CCA) of the <strong>Income Tax Act, 1961</strong> and Rule 31A of the <strong>Income Tax Rules, 1962</strong>.<br><br>
        Procedural mandates:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Tax Deduction Account Number (TAN):</strong> Mandatory 10-digit alphanumeric code obtained via Form 49B for deducting and remitting TDS.</li>
          <li><strong>Key Deductions:</strong> Section 192 (Salaries), 194C (Contractors), 194J (Professional / Technical Fees), 194I (Rent), 194Q (Purchase of Goods).</li>
          <li><strong>Quarterly Returns:</strong> Form 24Q for salary deductions; Form 26Q for non-salary domestic deductions; Form 27Q for non-resident payments.</li>
          <li><strong>TRACES Certificates:</strong> Generating system-validated Form 16 (annual salary) and Form 16A (quarterly non-salary) for deductees.</li>
        </ul>""",
        "deadlines_table": [
            ("7th of following month", "Monthly TDS Deposit (ITNS 281)", "Section 200(1)", "Interest @ 1.5% per month on late deposit"),
            ("July 31, Oct 31, Jan 31, May 31", "Quarterly TDS Returns (24Q/26Q)", "Rule 31A", "Late fee of ₹200/day under Section 234E"),
            ("Within 15 days of filing", "Issuance of Form 16A to Deductees", "Section 203", "Penalty of ₹100/day under Section 272A(2)(g)")
        ]
    },
    "trademark-registration-filing": {
        "statutory_badge_note": "Trademark opposition proceedings before the Trade Marks Registry and judicial appeals are represented by licensed Trademark Advocates.",
        "detailed_framework": """Brand registration and monopoly protections in India are governed under the <strong>Trade Marks Act, 1999</strong> and the <strong>Trade Marks Rules, 2017</strong> administered by the Controller General of Patents, Designs and Trade Marks (CGPDTM).<br><br>
        Registration journey:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Prior Art Conflict Search:</strong> Comprehensive clearance on the IP India database across relevant Nice Classification classes (1 to 45).</li>
          <li><strong>Form TM-A Filing:</strong> Electronic application filing with applicant identity, digital signature, goods/services description, and user affidavit if prior use is claimed.</li>
          <li><strong>Fee Concession:</strong> 50% discount on statutory government fees for MSME (Udyam) and DPIIT-recognized startup entities.</li>
          <li><strong>Examination & Journal Publication:</strong> Review under Sections 9 (absolute grounds) and 11 (relative grounds), followed by 4-month opposition window in the Trade Marks Journal before registration.</li>
        </ul>""",
        "deadlines_table": [
            ("Day 1-3", "Filing & Allocation of TM Application Number", "Form TM-A", "Authorization to use the ™ symbol immediately"),
            ("Within 30 Days of Notice", "Response to Examination Report (if objected)", "Section 9 & 11", "Application abandoned if reply not filed"),
            ("Every 10 Years", "Renewal of Registered Trademark", "Form TM-R (Section 25)", "Mark removed from register if renewal missed")
        ]
    },
    "trademark-examination-reply-objection": {
        "statutory_badge_note": "Formal oral hearings before the Registrar of Trade Marks are argued by qualified independent Trademark Advocates.",
        "detailed_framework": """When an application is flagged by the Trade Marks Registry, an Examination Report is issued raising statutory objections under the <strong>Trade Marks Act, 1999</strong>.<br><br>
        Statutory grounds:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Section 9 Objections (Absolute Grounds):</strong> Refusal based on lack of distinctiveness, descriptive character of goods/services, or generic industry terminology. Rebutted via evidence of acquired distinctiveness and commercial usage.</li>
          <li><strong>Section 11 Objections (Relative Grounds):</strong> Refusal based on phonetic, visual, or conceptual identity/similarity with an earlier cited registered mark. Rebutted via difference in customer base, market channels, and visual differences.</li>
          <li><strong>Form TM-MISC Written Reply:</strong> Detailed legal submission accompanied by turnover certificates, marketing collateral, invoices, and relevant High Court / Supreme Court precedents.</li>
          <li><strong>Show Cause Hearing:</strong> Scheduled if written submissions require verbal substantiation before the Assistant Registrar.</li>
        </ul>""",
        "deadlines_table": [
            ("Within 30 Days of Dispatch", "Filing Formal Written Reply", "Rule 33", "Application marked 'Abandoned' upon lapse of deadline"),
            ("Within 30 Days of Hearing Notice", "Filing Attendance / Adjournment Request", "Form TM-M", "Refusal order passed ex-parte if absent")
        ]
    },
    "employment-agreements-ndas-noncompete": {
        "statutory_badge_note": "Labour tribunal representation and formal employment litigation are conducted exclusively by licensed Advocates.",
        "detailed_framework": """Employment structuring in India intersects the <strong>Indian Contract Act, 1872</strong>, the <strong>Specific Relief Act, 1963</strong>, the <strong>Information Technology Act, 2000</strong>, and state-specific Shops & Commercial Establishments Acts.<br><br>
        Contractual architecture:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Section 27 Contract Act Restrictions:</strong> Agreements restraining trade are void in India. Post-employment non-compete covenants are generally unenforceable in Indian courts; enforceability is preserved through robust non-solicitation, confidentiality, and garden leave structures.</li>
          <li><strong>Proprietary Information & Inventions (PIIA):</strong> Comprehensive assignment of all source code, patents, models, and intellectual property created by employees during service to the corporate entity.</li>
          <li><strong>Confidentiality & Trade Secrets:</strong> Detailed definition of proprietary data, client lists, algorithms, and strict perpetual non-disclosure covenants.</li>
          <li><strong>DPDP Act 2023 Conformance:</strong> Employee consent and data processing provisions tailored to meet digital privacy mandates.</li>
        </ul>""",
        "deadlines_table": [
            ("Prior to Onboarding", "Execution of Employment Agreement & PIIA", "Section 10 Contract Act", "Unprotected intellectual property and trade secrets"),
            ("At Termination / Exit", "Execution of Relieving & Non-Disclosure Affirmation", "Contractual covenant", "Protects client lists and non-solicitation enforcement")
        ]
    },
    "dpdp-act-data-privacy-readiness": {
        "statutory_badge_note": "Legal representation before the Data Protection Board of India (DPBI) and High Courts is conducted by licensed Advocates.",
        "detailed_framework": """The <strong>Digital Personal Data Protection Act, 2023 (DPDP Act)</strong> establishes a comprehensive framework for processing digital personal data in India, governing corporate Data Fiduciaries and Significant Data Fiduciaries (SDF).<br><br>
        Statutory compliance pillars:
        <ul class="list-disc pl-5 mt-2 space-y-1">
          <li><strong>Notice & Consent Architecture (Section 6):</strong> Clear, transparent consent notices in plain language, accessible in English and 22 languages specified in the Eighth Schedule to the Constitution.</li>
          <li><strong>Data Principal Rights (Sections 11-14):</strong> Providing automated mechanisms for data access, correction, erasure, grievance redressal, and nomination.</li>
          <li><strong>Data Security Safeguards (Section 8):</strong> Mandatory technical and organizational measures to prevent personal data breaches; failure triggers penalties up to ₹250 Crore.</li>
          <li><strong>Breach Notification:</strong> Compulsory intimations to the Data Protection Board of India and affected Data Principals upon detection of data security compromises.</li>
        </ul>""",
        "deadlines_table": [
            ("Continuous / Real-Time", "Consent Recording & Verification Logs", "Section 6 DPDP Act", "Invalid processing; severe monetary penalties"),
            ("Immediate upon Detection", "Mandatory Breach Notification to DPBI", "Section 8(6)", "Penalties up to ₹250 Crore for concealment"),
            ("Within 30 Days of Request", "Data Principal Correction/Erasure Resolution", "Section 12", "Escalation to Data Protection Board of India")
        ]
    }
}

def render_product_page(service):
    sid = service["id"]
    cat = service["category"]
    title = service["title"]
    details = PRODUCT_DETAILS.get(sid, {})
    
    statutory_badge_note = details.get("statutory_badge_note", "")
    detailed_framework = details.get("detailed_framework", service["short_description"])
    deadlines_table = details.get("deadlines_table", [])
    
    eligibility_items = "".join([f'<li class="flex items-start gap-3 text-xs sm:text-sm text-slate-700"><span class="text-emerald-600 font-bold shrink-0">✓</span><span>{item}</span></li>' for item in service.get("eligibility", [])])
    
    docs = service.get("documents_required", {})
    doc_tabs_html = ""
    for group, doc_list in docs.items():
        doc_cards = "".join([f'<li class="flex items-center gap-2 text-xs text-slate-700 py-1.5 border-b border-slate-100 last:border-0"><span class="text-brand-sky font-bold">•</span><span>{d}</span></li>' for d in doc_list])
        doc_tabs_html += f"""
        <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
          <h4 class="text-xs font-bold uppercase tracking-wider text-brand-sky mb-4">{group.replace('_', ' ').title()} Checklist</h4>
          <ul class="space-y-1">
            {doc_cards}
          </ul>
        </div>
        """
        
    steps = service.get("execution_steps", [])
    steps_html = ""
    for s in steps:
        steps_html += f"""
        <div class="flex items-start gap-4 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm">
          <div class="w-9 h-9 rounded-xl bg-brand-skyLight text-brand-sky flex items-center justify-center font-bold text-sm shrink-0 shadow-sm">
            {s['step']}
          </div>
          <div>
            <h4 class="text-sm font-bold text-brand-dark">{s['title']}</h4>
            <p class="text-xs text-slate-500 mt-1">Processed digitally with real-time statutory portal verification.</p>
          </div>
        </div>
        """
        
    deadlines_rows = ""
    for dl in deadlines_table:
        deadlines_rows += f"""
        <tr class="border-b border-slate-100 text-xs hover:bg-slate-50">
          <td class="py-3.5 px-4 font-mono font-bold text-brand-dark">{dl[0]}</td>
          <td class="py-3.5 px-4 font-medium text-slate-700">{dl[1]}</td>
          <td class="py-3.5 px-4 font-mono font-bold text-brand-sky">{dl[2]}</td>
          <td class="py-3.5 px-4 text-slate-500">{dl[3]}</td>
        </tr>
        """

    disclaimer_hero_badge = ""
    if statutory_badge_note:
        disclaimer_hero_badge = f"""
        <div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center gap-2.5 max-w-2xl">
          <span class="text-base">⚠️</span>
          <span><strong>Statutory Practice Notice:</strong> {statutory_badge_note}</span>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | CraftEgon Corporate Services</title>
  <meta name="description" content="{service['short_description']}" />
  <link rel="canonical" href="https://corporateservices.craftegon.com{service['product_path']}" />
  
  <!-- Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- Production Compiled Stylesheets -->
  <link rel="stylesheet" href="/assets/css/output.css" />
  <link rel="stylesheet" href="/assets/css/theme.css" />
</head>
<body class="bg-slate-50 text-brand-dark font-sans antialiased min-h-screen flex flex-col justify-between">

{ANNOUNCEMENT_BAR}
{NAV_HTML}

<!-- HERO SECTION & QUICK ONBOARDING -->
<section class="relative bg-gradient-to-b from-brand-skyLight/50 via-white to-slate-50 py-12 md:py-16 border-b border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <nav class="flex items-center space-x-2 text-xs font-semibold text-slate-500 mb-4">
      <a href="/" class="hover:text-brand-sky transition">Home</a>
      <span>/</span>
      <a href="{service['hub_path']}" class="hover:text-brand-sky transition uppercase">{cat.replace('-', ' ')}</a>
      <span>/</span>
      <span class="text-brand-sky uppercase">{sid}</span>
    </nav>
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7 space-y-4">
        <div class="flex flex-wrap items-center gap-2">
          <span class="px-3 py-1 rounded-full bg-brand-skyLight text-brand-sky border border-brand-sky/20 text-xs font-bold">
            ⏱ {service['turnaround_time']}
          </span>
          <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-600 border border-slate-200 text-xs font-semibold">
            State Duty: Transparent
          </span>
          <span class="px-3 py-1 rounded-full bg-brand-goldLight text-brand-gold border border-brand-gold/30 text-xs font-bold">
            Starting @ ₹{service['pricing']['base_professional_fee']:,}
          </span>
        </div>
        
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-brand-dark tracking-tight leading-tight">
          {title}
        </h1>
        
        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-2xl">
          {service['short_description']}
        </p>
        
        {disclaimer_hero_badge}
        
        <div class="pt-2 flex flex-wrap items-center gap-5 text-xs text-slate-600 font-medium">
          <span class="flex items-center gap-1.5"><span class="text-emerald-600 font-bold">✓</span> MCA V3 Portal Verified</span>
          <span class="flex items-center gap-1.5"><span class="text-brand-sky font-bold">⚡</span> Express Fast-Track</span>
          <span class="flex items-center gap-1.5"><span class="text-brand-gold font-bold">🔒</span> DPDP Act Compliant</span>
        </div>
      </div>
      
      <!-- QUICK ONBOARDING FORM -->
      <div class="lg:col-span-5">
        <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-xl border border-slate-200 relative overflow-hidden">
          <div class="absolute top-0 right-0 bg-brand-gold text-white text-[10px] font-bold px-4 py-1 rounded-bl-lg uppercase tracking-wider">
            Express Filing
          </div>
          
          <h3 class="text-xl font-bold text-brand-dark mb-1">Apply for {title}</h3>
          <p class="text-xs text-slate-500 mb-6">Initiate statutory documentation in 60 seconds.</p>
          
          <form data-ccs-form="true" data-category="{cat}" data-service-id="{sid}" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1">Full Legal Name *</label>
              <input type="text" name="user_name" required placeholder="e.g. Rahul Sharma" class="w-full px-4 py-2.5 text-sm rounded-lg bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition" />
            </div>
            
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Email ID *</label>
                <input type="email" name="email" required placeholder="name@company.com" class="w-full px-4 py-2.5 text-sm rounded-lg bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition" />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Phone / WhatsApp *</label>
                <input type="tel" name="phone" required placeholder="+91 98765 43210" class="w-full px-4 py-2.5 text-sm rounded-lg bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition" />
              </div>
            </div>
            
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">State *</label>
                <select name="selected_state" required class="w-full px-4 py-2.5 text-sm rounded-lg bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition">
                  <option value="Kerala">Kerala</option>
                  <option value="Maharashtra">Maharashtra</option>
                  <option value="Karnataka">Karnataka</option>
                  <option value="Delhi">Delhi</option>
                  <option value="Tamil Nadu">Tamil Nadu</option>
                  <option value="Telangana">Telangana</option>
                  <option value="Other">Other States</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Timeline</label>
                <select name="timeline" class="w-full px-4 py-2.5 text-sm rounded-lg bg-slate-50 border border-slate-200 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition">
                  <option value="Immediate">Immediate (1-3 days)</option>
                  <option value="This Month">This Month</option>
                  <option value="Planning">Information Only</option>
                </select>
              </div>
            </div>
            
            <button type="submit" class="w-full bg-gradient-to-r from-brand-sky to-brand-skyHover text-white font-bold text-sm py-3.5 rounded-lg shadow-md hover:shadow-lg transition">
              Get Started Now &rarr;
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STATUTORY FRAMEWORK -->
<section class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-b border-slate-200">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
    <div class="lg:col-span-8">
      <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Statutory Provisions</h2>
      <h3 class="text-2xl font-extrabold text-brand-dark mb-4">Current Legal Framework &amp; Regulatory Mandate</h3>
      <div class="prose prose-sm text-slate-700 leading-relaxed text-sm">
        {detailed_framework}
      </div>
    </div>
    
    <div class="lg:col-span-4 bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
      <h4 class="text-xs font-bold uppercase tracking-wider text-brand-sky">Statutory Overview</h4>
      <div class="space-y-3 text-xs">
        <div>
          <span class="block text-slate-500 font-semibold">Governing Act:</span>
          <span class="font-bold text-brand-dark">{service['statutory_framework']}</span>
        </div>
        <div>
          <span class="block text-slate-500 font-semibold">Government Portal:</span>
          <span class="font-bold text-brand-dark">Ministry of Corporate Affairs (MCA V3) / Official Portals</span>
        </div>
        <div>
          <span class="block text-slate-500 font-semibold">Filing Authority:</span>
          <span class="font-bold text-brand-dark">Registrar of Companies (ROC) / Central Board</span>
        </div>
        <div>
          <span class="block text-slate-500 font-semibold">Standard Turnaround:</span>
          <span class="font-bold text-brand-dark">{service['turnaround_time']}</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ELIGIBILITY -->
<section class="py-14 bg-white border-b border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Prerequisites</h2>
    <h3 class="text-2xl font-extrabold text-brand-dark mb-6">Eligibility Criteria &amp; Structural Minimums</h3>
    
    <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
      {eligibility_items}
    </ul>
  </div>
</section>

<!-- DOCUMENT CHECKLIST -->
<section class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-b border-slate-200">
  <div class="mb-6">
    <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Verification Checklist</h2>
    <h3 class="text-2xl font-extrabold text-brand-dark">Mandatory Document Checklist</h3>
    <p class="text-xs text-slate-500 mt-1">Ensure clear self-attested copies to avoid departmental resubmission requisitions.</p>
  </div>
  
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    {doc_tabs_html}
  </div>
</section>

<!-- 5-STEP EXECUTION FLOW -->
<section class="py-14 bg-white border-b border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="mb-8">
      <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Workflow Architecture</h2>
      <h3 class="text-2xl font-extrabold text-brand-dark">5-Step Statutory Execution Flow</h3>
      <p class="text-xs text-slate-500 mt-1">From initial digital signature verification to Certificate of Incorporation issuance.</p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-5 gap-4">
      {steps_html}
    </div>
  </div>
</section>

<!-- COMPLIANCE SCHEDULE -->
<section class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-b border-slate-200">
  <div class="mb-6">
    <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Ongoing Governance</h2>
    <h3 class="text-2xl font-extrabold text-brand-dark">Post-Registration Compliance Schedule</h3>
    <p class="text-xs text-slate-500 mt-1">Mandatory timelines following receipt of registration certificate.</p>
  </div>
  
  <div class="bg-white rounded-2xl border border-slate-200 overflow-x-auto shadow-sm">
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="bg-slate-50 border-b border-slate-200 text-slate-600 text-xs uppercase font-bold">
          <th class="py-3.5 px-4">Statutory Timeline</th>
          <th class="py-3.5 px-4">Mandatory Compliance Action</th>
          <th class="py-3.5 px-4">Section / Form</th>
          <th class="py-3.5 px-4">Non-Compliance Penalty</th>
        </tr>
      </thead>
      <tbody>
        {deadlines_rows}
      </tbody>
    </table>
  </div>
</section>

<!-- FEE BREAKDOWN -->
<section class="py-14 bg-slate-50 border-b border-slate-200">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-8">
      <h2 class="text-xs font-bold text-brand-sky uppercase tracking-widest mb-1">Fee Transparency</h2>
      <h3 class="text-2xl font-extrabold text-brand-dark">Fee Structure &amp; Stamp Duty Breakdown</h3>
      <p class="text-xs text-slate-500 mt-1">Government stamp duties are computed based on state stamp laws.</p>
    </div>
    
    <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm" data-calc-ready="true">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
        <div>
          <label class="block text-xs font-bold uppercase text-slate-700 mb-1" for="prod-calc-state">State of Registration</label>
          <select id="prod-calc-state" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-slate-800 focus:ring-2 focus:ring-brand-sky focus:outline-none">
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
          <label class="block text-xs font-bold uppercase text-slate-700 mb-1" for="prod-calc-capital">Authorized Capital</label>
          <select id="prod-calc-capital" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-slate-800 focus:ring-2 focus:ring-brand-sky focus:outline-none">
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
          <span class="font-black text-sm text-brand-dark mt-1 block">₹{service['pricing']['base_professional_fee']:,}</span>
        </div>
        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
          <span class="block text-[10px] uppercase font-bold text-slate-500">State Stamp Duty</span>
          <span id="prod-stamp-duty" class="font-black text-sm text-brand-gold mt-1 block">₹5,000</span>
        </div>
        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
          <span class="block text-[10px] uppercase font-bold text-slate-500">GST (18%)</span>
          <span id="prod-gst-amount" class="font-black text-sm text-brand-dark mt-1 block">₹{int(service['pricing']['base_professional_fee'] * 0.18):,}</span>
        </div>
        <div class="p-3 bg-brand-skyLight rounded-xl border border-brand-sky/30">
          <span class="block text-[10px] uppercase font-bold text-brand-sky">Estimated Total</span>
          <span id="prod-total-fee" class="font-black text-sm text-brand-dark mt-1 block">₹{int(service['pricing']['base_professional_fee'] * 1.18 + 5000):,}</span>
        </div>
      </div>

      <!-- Itemized Statutory Formula Breakdown -->
      <div id="prod-breakdown-note" class="mt-4 p-3.5 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-600 leading-relaxed">
        <span class="font-semibold text-brand-dark">Statutory Breakdown (Kerala · ₹10 Lakhs Capital):</span>
        <span class="font-mono text-slate-700 ml-1">₹{service['pricing']['base_professional_fee']:,} (Prof) + ₹5,000 (Stamp Duty) + ₹{int(service['pricing']['base_professional_fee'] * 0.18):,} (GST) = <strong>₹{int(service['pricing']['base_professional_fee'] * 1.18 + 5000):,}</strong></span>
      </div>

      <!-- Direct Quote & WhatsApp Action -->
      <div class="mt-6 flex flex-wrap items-center gap-3">
        <a href="#inquiry" class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs px-5 py-2.5 rounded-lg shadow transition">
          Get a Free Quote &rarr;
        </a>
        <a href="https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20want%20a%20statutory%20fee%20quote%20for%20{title}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-[#25D366]/10 border border-[#25D366]/40 text-[#128C7E] hover:bg-[#25D366]/20 font-bold text-xs px-4 py-2.5 rounded-lg transition">
          <span>💬 Ask on WhatsApp</span>
        </a>
      </div>

      <!-- Disclaimer Alert -->
      <div class="mt-6 p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center gap-2.5">
        <span class="text-base shrink-0">ℹ️</span>
        <p class="leading-relaxed">
          Estimates are indicative. Stamp duty rates are subject to change per state government notifications.
          Government fees are charged at actuals. Final invoice will reflect current applicable rates.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- DIRECT INQUIRY FORM -->
<section id="inquiry" class="py-16 bg-white">
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-200 shadow-md">
      <div class="text-center mb-6">
        <h3 class="text-xl font-bold text-brand-dark">Initiate {title}</h3>
        <p class="text-xs text-slate-500 mt-1">Connect with our specialized CA/CS team for fast-track processing.</p>
      </div>
      
      <form data-ccs-form="true" data-category="{cat}" data-service-id="{sid}" class="space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Full Legal Name *</label>
            <input type="text" name="user_name" required placeholder="e.g. Rahul Sharma" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Work Email ID *</label>
            <input type="email" name="email" required placeholder="rahul@company.com" class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none" />
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
          <label class="block text-xs font-bold text-slate-700 mb-1">Specific Requirements / Notes</label>
          <textarea name="custom_message" rows="3" placeholder="Provide any details regarding proposed company names, existing DINs, or special timeline requirements..." class="w-full bg-white border border-slate-300 rounded-lg px-3.5 py-2.5 text-xs text-brand-dark focus:ring-2 focus:ring-brand-sky focus:outline-none"></textarea>
        </div>
        
        <button type="submit" class="w-full bg-gradient-to-r from-brand-sky to-brand-skyHover text-white font-bold text-xs uppercase tracking-wider py-3.5 rounded-lg shadow-md hover:shadow-lg transition">
          Submit Service Request &rarr;
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

  const pState = document.getElementById('prod-calc-state');
  const pCap = document.getElementById('prod-calc-capital');
  const pDuty = document.getElementById('prod-stamp-duty');
  const pGst = document.getElementById('prod-gst-amount');
  const pTotal = document.getElementById('prod-total-fee');
  const pNote = document.getElementById('prod-breakdown-note');
  const baseFee = {service['pricing']['base_professional_fee']};

  function updateProdCalc() {{
    if (window.CCSCalculator && window.CCSCalculator.calculateTotalFee && pState && pCap) {{
      const state = pState.value;
      const capital = parseInt(pCap.value, 10);
      const res = window.CCSCalculator.calculateTotalFee(baseFee, state, capital);
      if (pDuty) pDuty.textContent = '₹' + res.stamp_duty.toLocaleString('en-IN');
      if (pGst) pGst.textContent = '₹' + res.gst_amount.toLocaleString('en-IN');
      if (pTotal) pTotal.textContent = '₹' + res.total.toLocaleString('en-IN');
      if (pNote) {{
        pNote.innerHTML = '<span class="font-semibold text-brand-dark">Statutory Breakdown (' + state + ' · ₹' + capital.toLocaleString('en-IN') + ' Capital):</span> <span class="font-mono text-slate-700 ml-1">₹' + baseFee.toLocaleString('en-IN') + ' (Prof) + ₹' + res.stamp_duty.toLocaleString('en-IN') + ' (Stamp Duty) + ₹' + res.gst_amount.toLocaleString('en-IN') + ' (GST 18%) = <strong>₹' + res.total.toLocaleString('en-IN') + '</strong></span>';
      }}
    }}
  }}

  if (pState && pCap) {{
    pState.addEventListener('change', updateProdCalc);
    pCap.addEventListener('change', updateProdCalc);
    // Initialize immediately on page load
    updateProdCalc();
  }}
</script>
</body>
</html>
"""
    return html

def main():
    with open("data/services.json", encoding="utf-8") as f:
        data = json.load(f)

    phase_1_services = [s for s in data["services"] if s.get("phase") == 1]
    print(f"Found {len(phase_1_services)} Phase 1 services to generate.")

    for s in phase_1_services:
        cat = s["category"]
        sid = s["id"]
        target_dir = os.path.join(cat, sid)
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, "index.html")

        html_content = render_product_page(s)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated: {target_file}")

if __name__ == "__main__":
    main()
