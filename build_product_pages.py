# -*- coding: utf-8 -*-
"""
Builds the 12 High-Intent Phase 1 Product Pages with the 9-part high-conversion layout.
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
    
    # Eligibility list
    eligibility_items = "".join([f'<li class="flex items-start gap-3 text-xs sm:text-sm text-gray-700"><i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5"></i><span>{item}</span></li>' for item in service.get("eligibility", [])])
    
    # Documents list
    docs = service.get("documents_required", {})
    doc_tabs_html = ""
    for group, doc_list in docs.items():
        doc_cards = "".join([f'<li class="flex items-center gap-2 text-xs text-gray-700 py-1.5 border-b border-gray-100 last:border-0"><i data-lucide="file-text" class="w-4 h-4 text-[#c5a059] shrink-0"></i><span>{d}</span></li>' for d in doc_list])
        doc_tabs_html += f"""
        <div class="bg-white p-5 rounded-xl border border-gray-200/80 shadow-sm">
          <h4 class="font-serif text-sm font-bold text-[#0e1712] mb-3 uppercase tracking-wider text-[#c5a059]">{group.replace('_', ' ').title()} Checklist</h4>
          <ul class="space-y-1">
            {doc_cards}
          </ul>
        </div>
        """
        
    # Execution steps
    steps = service.get("execution_steps", [])
    steps_html = ""
    for s in steps:
        steps_html += f"""
        <div class="flex items-start gap-4 p-4 rounded-xl bg-white border border-gray-200 shadow-sm">
          <div class="w-8 h-8 rounded-full bg-[#0e1712] text-[#c5a059] flex items-center justify-center font-mono font-bold text-sm shrink-0">
            {s['step']}
          </div>
          <div>
            <h4 class="font-serif text-sm font-bold text-[#0e1712]">{s['title']}</h4>
            <p class="text-xs text-gray-500 mt-1">Managed electronically with statutory accuracy and verified via client dashboard.</p>
          </div>
        </div>
        """
        
    # Compliance deadlines table
    deadlines_rows = ""
    for dl in deadlines_table:
        deadlines_rows += f"""
        <tr class="border-b border-gray-100 text-xs">
          <td class="py-3 px-4 font-mono font-semibold text-[#0e1712]">{dl[0]}</td>
          <td class="py-3 px-4 font-medium text-gray-800">{dl[1]}</td>
          <td class="py-3 px-4 font-mono text-[#c5a059]">{dl[2]}</td>
          <td class="py-3 px-4 text-gray-500">{dl[3]}</td>
        </tr>
        """

    disclaimer_hero_badge = ""
    if statutory_badge_note:
        disclaimer_hero_badge = f"""
        <div class="mt-4 p-3 rounded-lg bg-amber-950/40 border border-amber-500/40 text-amber-200 text-xs flex items-center gap-2.5 max-w-2xl">
          <i data-lucide="shield-alert" class="w-4 h-4 text-amber-400 shrink-0"></i>
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
</head>
<body class="bg-[#f8f9f6] text-[#2e3a33] font-sans antialiased">

{NAV_HTML}

<!-- PART 1: HERO HEADER & QUICK ONBOARDING FORM -->
<section class="bg-[#0e1712] text-white pt-12 pb-16 border-b border-white/10 relative overflow-hidden">
  <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#c5a059_1px,transparent_1px)] [background-size:16px_16px]"></div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <nav class="flex items-center space-x-2 text-xs font-mono text-gray-400 mb-6">
      <a href="/" class="hover:text-white transition">Home</a>
      <span>/</span>
      <a href="{service['hub_path']}" class="hover:text-white transition uppercase">{cat.replace('-', ' ')}</a>
      <span>/</span>
      <span class="text-[#c5a059] uppercase">{sid}</span>
    </nav>
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7 space-y-4">
        <div class="flex flex-wrap items-center gap-2">
          <span class="px-3 py-1 rounded-full bg-[#c5a059]/20 text-[#c5a059] border border-[#c5a059]/40 text-xs font-mono font-bold">
            <i data-lucide="clock" class="w-3.5 h-3.5 inline mr-1"></i> {service['turnaround_time']}
          </span>
          <span class="px-3 py-1 rounded-full bg-white/10 text-white/90 border border-white/15 text-xs font-mono">
            State Duty: Variable
          </span>
          <span class="px-3 py-1 rounded-full bg-white/10 text-white/90 border border-white/15 text-xs font-mono">
            Base: ₹{service['pricing']['base_professional_fee']:,}
          </span>
        </div>
        
        <h1 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-white leading-tight">
          {title}
        </h1>
        
        <p class="text-sm sm:text-base text-gray-300 leading-relaxed max-w-2xl">
          {service['short_description']}
        </p>
        
        {disclaimer_hero_badge}
        
        <div class="pt-2 flex items-center gap-6 text-xs text-gray-400 font-mono">
          <span class="flex items-center gap-1.5"><i data-lucide="shield-check" class="w-4 h-4 text-emerald-400"></i> MCA / Govt Verified</span>
          <span class="flex items-center gap-1.5"><i data-lucide="zap" class="w-4 h-4 text-[#c5a059]"></i> Fast-Track Filing</span>
          <span class="flex items-center gap-1.5"><i data-lucide="lock" class="w-4 h-4 text-blue-400"></i> DPDP Compliant</span>
        </div>
      </div>
      
      <!-- QUICK ONBOARDING FORM -->
      <div class="lg:col-span-5">
        <div class="bg-white rounded-2xl p-6 sm:p-7 text-[#2e3a33] shadow-2xl border border-white/10">
          <div class="mb-4">
            <span class="font-mono text-[11px] uppercase tracking-wider text-[#c5a059] font-bold">Express Docket Setup</span>
            <h3 class="font-serif text-lg font-bold text-[#0e1712]">Start {title}</h3>
            <p class="text-xs text-gray-500">Initiate statutory documentation in 60 seconds.</p>
          </div>
          
          <form data-ccs-form="true" data-category="{cat}" data-service-id="{sid}" class="space-y-3">
            <div>
              <label class="block text-[11px] font-mono uppercase text-gray-600 mb-1">Your Full Name *</label>
              <input type="text" name="user_name" required placeholder="Shibili Poompatta" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3 py-2 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
            </div>
            
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block text-[11px] font-mono uppercase text-gray-600 mb-1">Email ID *</label>
                <input type="email" name="email" required placeholder="name@company.com" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3 py-2 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
              </div>
              <div>
                <label class="block text-[11px] font-mono uppercase text-gray-600 mb-1">Phone / WhatsApp *</label>
                <input type="tel" name="phone" required placeholder="9876543210" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3 py-2 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
              </div>
            </div>
            
            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block text-[11px] font-mono uppercase text-gray-600 mb-1">State *</label>
                <select name="selected_state" required class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3 py-2 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none">
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
                <label class="block text-[11px] font-mono uppercase text-gray-600 mb-1">Timeline</label>
                <select name="timeline" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3 py-2 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none">
                  <option value="Immediate">Immediate (1-3 days)</option>
                  <option value="This Month">This Month</option>
                  <option value="Planning">Information Only</option>
                </select>
              </div>
            </div>
            
            <button type="submit" class="w-full bg-[#0e1712] hover:bg-black text-[#c5a059] font-bold text-xs uppercase tracking-wider py-3 rounded-lg transition shadow-md mt-2">
              Proceed to Onboarding &rarr;
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PART 2: STATUTORY OVERVIEW & LEGAL FRAMEWORK -->
<section class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-b border-gray-200">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
    <div class="lg:col-span-8">
      <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Statutory Provisions</span>
      <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1 mb-4">Current Legal Framework &amp; Regulatory Mandate</h2>
      <div class="prose prose-sm text-gray-700 leading-relaxed text-xs sm:text-sm">
        {detailed_framework}
      </div>
    </div>
    
    <div class="lg:col-span-4 bg-white p-6 rounded-2xl border border-gray-200 shadow-sm space-y-4">
      <h3 class="font-serif text-base font-bold text-[#0e1712] uppercase tracking-wider text-[#c5a059]">Statutory Meta</h3>
      <div class="space-y-3 text-xs">
        <div>
          <span class="block text-gray-400 font-mono">Governing Act:</span>
          <span class="font-semibold text-gray-800">{service['statutory_framework']}</span>
        </div>
        <div>
          <span class="block text-gray-400 font-mono">Government Portal:</span>
          <span class="font-semibold text-gray-800">Ministry of Corporate Affairs (MCA V3) / Official Portals</span>
        </div>
        <div>
          <span class="block text-gray-400 font-mono">Filing Authority:</span>
          <span class="font-semibold text-gray-800">Registrar of Companies (ROC) / Central Board</span>
        </div>
        <div>
          <span class="block text-gray-400 font-mono">Turnaround Standard:</span>
          <span class="font-semibold text-gray-800">{service['turnaround_time']}</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PART 3: ELIGIBILITY CRITERIA -->
<section class="py-14 bg-white border-b border-gray-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Statutory Prerequisites</span>
    <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1 mb-6">Eligibility Criteria &amp; Structural Minimums</h2>
    
    <ul class="grid grid-cols-1 md:grid-cols-2 gap-4">
      {eligibility_items}
    </ul>
  </div>
</section>

<!-- PART 4: MANDATORY DOCUMENT CHECKLIST -->
<section class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-b border-gray-200">
  <div class="mb-6">
    <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Verification Matrix</span>
    <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1">Mandatory Document Checklist</h2>
    <p class="text-xs text-gray-500 mt-1">Ensure self-attested, clear scanned copies to avoid ROC / departmental resubmission requisitions.</p>
  </div>
  
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    {doc_tabs_html}
  </div>
</section>

<!-- PART 5: 5-STEP EXECUTION FLOW -->
<section class="py-14 bg-[#fcfbf7] border-b border-gray-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="mb-8">
      <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Workflow Blueprint</span>
      <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1">5-Step Statutory Execution Architecture</h2>
      <p class="text-xs text-gray-500 mt-1">From digital signature acquisition to formal registration issuance.</p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-5 gap-4">
      {steps_html}
    </div>
  </div>
</section>

<!-- PART 6: POST-REGISTRATION COMPLIANCE SCHEDULE -->
<section class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-b border-gray-200">
  <div class="mb-6">
    <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Lifecycle Governance</span>
    <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1">Post-Registration Compliance Schedule</h2>
    <p class="text-xs text-gray-500 mt-1">Critical statutory timelines following receipt of registration certificate.</p>
  </div>
  
  <div class="bg-white rounded-xl border border-gray-200 overflow-x-auto shadow-sm">
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="bg-gray-50 border-b border-gray-200 text-gray-600 font-mono text-[11px] uppercase">
          <th class="py-3 px-4">Statutory Timeline</th>
          <th class="py-3 px-4">Mandatory Compliance Action</th>
          <th class="py-3 px-4">Statutory Form / Section</th>
          <th class="py-3 px-4">Non-Compliance Consequence</th>
        </tr>
      </thead>
      <tbody>
        {deadlines_rows}
      </tbody>
    </table>
  </div>
</section>

<!-- PART 7: INTERACTIVE FEE BREAKDOWN CALCULATOR -->
<section class="py-14 bg-[#0e1712] text-white border-b border-white/10">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-8">
      <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Transparent Fee Matrix</span>
      <h2 class="font-serif text-2xl font-bold text-white mt-1">Fee Structure &amp; Stamp Duty Breakdown</h2>
      <p class="text-xs text-gray-400 mt-1">Government stamp duties are computed dynamically according to state stamp laws.</p>
    </div>
    
    <div class="bg-[#090d16] p-6 rounded-xl border border-white/15" data-ccs-calculator="{sid}">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
        <div>
          <label class="block text-xs font-mono uppercase text-gray-400 mb-1">State / Union Territory</label>
          <select id="prod-calc-state" class="w-full bg-[#0e1712] border border-white/20 rounded-lg px-3 py-2 text-xs text-white focus:border-[#c5a059] focus:outline-none">
            <option value="Kerala" selected>Kerala</option>
            <option value="Maharashtra">Maharashtra</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Delhi">Delhi</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Telangana">Telangana</option>
            <option value="Gujarat">Gujarat</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-mono uppercase text-gray-400 mb-1">Authorized Capital</label>
          <select id="prod-calc-capital" class="w-full bg-[#0e1712] border border-white/20 rounded-lg px-3 py-2 text-xs text-white focus:border-[#c5a059] focus:outline-none">
            <option value="100000">₹1,00,000</option>
            <option value="1000000" selected>₹10,00,000 (Standard)</option>
            <option value="2500000">₹25,00,000</option>
            <option value="5000000">₹50,00,000</option>
            <option value="10000000">₹1,00,00,000</option>
          </select>
        </div>
      </div>
      
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center pt-4 border-t border-white/10">
        <div class="p-3 bg-[#0e1712] rounded-lg">
          <span class="block text-[10px] font-mono text-gray-400 uppercase">Professional Fee</span>
          <span class="font-mono text-sm font-bold text-white mt-1 block">₹{service['pricing']['base_professional_fee']:,}</span>
        </div>
        <div class="p-3 bg-[#0e1712] rounded-lg">
          <span class="block text-[10px] font-mono text-gray-400 uppercase">State Stamp Duty</span>
          <span id="prod-stamp-duty" class="font-mono text-sm font-bold text-[#c5a059] mt-1 block">₹2,000</span>
        </div>
        <div class="p-3 bg-[#0e1712] rounded-lg">
          <span class="block text-[10px] font-mono text-gray-400 uppercase">GST (18%)</span>
          <span class="font-mono text-sm font-bold text-white mt-1 block">₹{int(service['pricing']['base_professional_fee'] * 0.18):,}</span>
        </div>
        <div class="p-3 bg-[#c5a059]/15 rounded-lg border border-[#c5a059]/30">
          <span class="block text-[10px] font-mono text-[#c5a059] uppercase font-bold">Estimated Total</span>
          <span id="prod-total-fee" class="font-mono text-sm font-bold text-white mt-1 block">₹{int(service['pricing']['base_professional_fee'] * 1.18 + 2000):,}</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PART 8: SERVICE-SPECIFIC DIRECT INQUIRY FORM -->
<section id="inquiry" class="py-16 bg-[#fcfbf7]">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white rounded-2xl p-8 border border-gray-200 shadow-md">
      <div class="text-center mb-6">
        <span class="font-mono text-xs uppercase tracking-widest text-[#c5a059] font-bold">Direct Docket Engagement</span>
        <h2 class="font-serif text-2xl font-bold text-[#0e1712] mt-1">Initiate {title}</h2>
        <p class="text-xs text-gray-500 mt-1">Submit your details or proceed to instant WhatsApp direct checkout.</p>
      </div>
      
      <form data-ccs-form="true" data-category="{cat}" data-service-id="{sid}" class="space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Your Full Name *</label>
            <input type="text" name="user_name" required placeholder="Shibili Poompatta" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Business Email *</label>
            <input type="email" name="email" required placeholder="shibili@domain.com" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
          </div>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Mobile / WhatsApp *</label>
            <input type="tel" name="phone" required placeholder="9876543210" class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none" />
          </div>
          <div>
            <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Jurisdiction / State *</label>
            <select name="selected_state" required class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none">
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
          <label class="block text-xs font-mono uppercase text-gray-600 mb-1">Specific Instructions / Existing Registrations</label>
          <textarea name="custom_message" rows="3" placeholder="Provide any details regarding proposed company names, existing DINs, turnover brackets, or special requirements..." class="w-full bg-[#f8f9f6] border border-gray-300 rounded-lg px-3.5 py-2.5 text-xs text-[#0e1712] focus:border-[#c5a059] focus:outline-none"></textarea>
        </div>
        
        <button type="submit" class="w-full bg-[#0e1712] hover:bg-black text-[#c5a059] font-bold text-xs uppercase tracking-wider py-3.5 rounded-lg transition shadow-md">
          Submit Service Mandate &rarr;
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
  if (window.lucide) {{ lucide.createIcons(); }}

  // Mobile menu toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (mobileBtn && mobileMenu) {{
    mobileBtn.addEventListener('click', () => {{
      mobileMenu.classList.toggle('hidden');
    }});
  }}

  // Stamp duty local calculation
  const pState = document.getElementById('prod-calc-state');
  const pCap = document.getElementById('prod-calc-capital');
  const pDuty = document.getElementById('prod-stamp-duty');
  const pTotal = document.getElementById('prod-total-fee');
  const baseFee = {service['pricing']['base_professional_fee']};

  function updateProdCalc() {{
    if (window.CCSCalculator && window.CCSCalculator.calculateTotalFee && pState && pCap) {{
      const res = window.CCSCalculator.calculateTotalFee(baseFee, pState.value, parseInt(pCap.value));
      pDuty.textContent = '₹' + res.stamp_duty.toLocaleString('en-IN');
      pTotal.textContent = '₹' + res.total.toLocaleString('en-IN');
    }}
  }}

  if (pState && pCap) {{
    pState.addEventListener('change', updateProdCalc);
    pCap.addEventListener('change', updateProdCalc);
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

