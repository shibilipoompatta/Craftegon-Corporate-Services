# -*- coding: utf-8 -*-
"""
Generates the legal compliance pages:
1. /terms/index.html & terms.html (Terms & Conditions)
2. /privacy/index.html & privacy.html (Privacy Policy)
3. /data-policy/index.html & data-policy.html (Data Protection Policy - DPDP Act 2023)
4. /about/index.html & about.html (About Us in modern LegalTech design)
"""
import os

EDITED_REGULATORY_NOTE = """Regulatory Notice: CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform. CCS is not a law firm and does not provide court litigation or judicial representation before courts or tribunals. All court litigation and tribunal appearances are executed exclusively through independent, licensed advocates or associate law firms in accordance with the Advocates Act, 1961. Statutory audits, tax certifications, and regulated professional services are fulfilled by qualified, independent Chartered Accountants, Company Secretaries, and registered professionals in compliance with ICAI, ICSI, and statutory guidelines."""

ANNOUNCEMENT_BAR = """<div class="bg-gradient-to-r from-brand-sky to-brand-skyHover text-white text-xs md:text-sm py-2.5 px-4 text-center font-medium shadow-sm flex items-center justify-center gap-2">
  <span>🚀 Special Offer: Get <strong>20% OFF</strong> MCA Filing &amp; Free Expert Consultation this week!</span>
  <a href="/#contact" class="underline hover:text-brand-goldLight font-bold transition">Claim Offer &rarr;</a>
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
      <a href="/workforce-digital/" class="hover:text-brand-sky transition">Workforce &amp; Digital</a>
    </nav>

    <!-- CTA Buttons -->
    <div class="flex items-center gap-3">
      <a href="https://wa.me/919995204905" target="_blank" rel="noopener" class="hidden sm:flex items-center gap-2 text-xs font-bold text-slate-700 bg-brand-slate px-4 py-2.5 rounded-lg border border-slate-200 hover:bg-slate-200 transition">
        <span class="text-emerald-600 font-bold">●</span> Desk: +91 99952 04905
      </a>
      <a href="/#contact" class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs md:text-sm px-5 py-2.5 rounded-lg shadow-md hover:shadow-lg transition">
        Get Started
      </a>
      <button id="mobileMenuBtn" class="lg:hidden text-slate-700 p-2 rounded-lg hover:bg-slate-100 min-touch flex items-center justify-center" aria-label="Toggle Menu">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div id="mobileMenu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 py-4 space-y-3 shadow-lg">
    <a href="/business-setup/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Business Setup &amp; Formation</a>
    <a href="/gst-advisory/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">GST Advisory &amp; Filings</a>
    <a href="/corporate-governance/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Corporate Governance &amp; MCA</a>
    <a href="/direct-tax/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Direct Tax &amp; TDS</a>
    <a href="/brand-protection/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Brand Protection &amp; Trademarks</a>
    <a href="/workforce-digital/" class="block text-sm font-semibold text-slate-700 hover:text-brand-sky py-2 border-b border-slate-100">Workforce &amp; Digital Infrastructure</a>
    <div class="pt-2">
      <a href="/#contact" class="block w-full text-center bg-brand-sky text-white font-bold text-sm py-3 rounded-lg shadow">Get Free Consultation</a>
    </div>
  </div>
</header>"""

GLOBAL_FOOTER = f"""<footer class="bg-brand-dark text-slate-400 text-xs py-14 border-t border-slate-800">
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
        <p class="text-slate-400 text-xs">Technopark, Trivandrum, Kerala, India</p>
        <p class="text-slate-400 text-xs mt-1">support@craftegon.com | +91 99952 04905</p>
      </div>

      <div>
        <h5 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Practice Hubs</h5>
        <ul class="space-y-2">
          <li><a href="/business-setup/" class="hover:text-brand-sky transition">Business Setup &amp; Formation</a></li>
          <li><a href="/gst-advisory/" class="hover:text-brand-sky transition">GST Advisory &amp; Filings</a></li>
          <li><a href="/corporate-governance/" class="hover:text-brand-sky transition">Corporate Governance &amp; MCA</a></li>
          <li><a href="/direct-tax/" class="hover:text-brand-sky transition">Direct Tax &amp; TDS</a></li>
          <li><a href="/brand-protection/" class="hover:text-brand-sky transition">Brand &amp; IP Protection</a></li>
          <li><a href="/workforce-digital/" class="hover:text-brand-sky transition">Workforce &amp; Digital</a></li>
        </ul>
      </div>

      <div>
        <h5 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Platform &amp; Legal</h5>
        <ul class="space-y-2">
          <li><a href="/about/" class="hover:text-brand-sky transition">About CraftEgon</a></li>
          <li><a href="/terms/" class="hover:text-brand-sky transition">Terms &amp; Conditions</a></li>
          <li><a href="/privacy/" class="hover:text-brand-sky transition">Privacy Policy</a></li>
          <li><a href="/data-policy/" class="hover:text-brand-sky transition">Data Protection Policy (DPDP)</a></li>
          <li><a href="/experts.html" class="hover:text-brand-sky transition">Expert CA/CS Directory</a></li>
          <li><a href="/contact.html" class="hover:text-brand-sky transition">Contact &amp; Grievance Desk</a></li>
        </ul>
      </div>

      <div>
        <h5 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Direct Case Desk</h5>
        <p class="text-slate-400 mb-3">Connect directly via WhatsApp Business for express onboarding &amp; fee inquiries:</p>
        <a href="https://wa.me/919995204905" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-[#25D366]/20 border border-[#25D366]/40 text-[#25D366] hover:bg-[#25D366]/30 px-3.5 py-2.5 rounded-lg text-xs font-bold transition">
          <span>💬 Direct WhatsApp Case Desk</span>
        </a>
      </div>
    </div>

    <!-- Mandatory Non-Litigation Disclaimer -->
    <div class="border-t border-slate-800 pt-8">
      <div class="p-4 rounded-xl bg-slate-900 border border-slate-800">
        <p class="text-[11px] text-slate-400 leading-relaxed text-justify">
          <strong class="text-brand-gold uppercase">{EDITED_REGULATORY_NOTE.split(':')[0]}:</strong>{EDITED_REGULATORY_NOTE[len(EDITED_REGULATORY_NOTE.split(':')[0]) + 1:]}
        </p>
      </div>
      <div class="mt-4 flex flex-col sm:flex-row justify-between items-center text-[11px] text-slate-500 gap-3">
        <p>&copy; 2026 CraftEgon Corporate Services. All rights reserved.</p>
        <div class="flex flex-wrap items-center gap-4 text-[11px] text-slate-400">
          <a href="/about/" class="hover:text-white transition">About Us</a>
          <span>·</span>
          <a href="/terms/" class="hover:text-white transition">Terms &amp; Conditions</a>
          <span>·</span>
          <a href="/privacy/" class="hover:text-white transition">Privacy Policy</a>
          <span>·</span>
          <a href="/data-policy/" class="hover:text-white transition">Data Policy</a>
        </div>
        <p class="font-mono">corporateservices.craftegon.com</p>
      </div>
    </div>
  </div>
</footer>"""

def render_page(title, meta_desc, canonical_path, badge, heading, subtitle, content_html):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | CraftEgon Corporate Services</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="canonical" href="https://corporateservices.craftegon.com{canonical_path}" />
  
  <!-- Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- Production Compiled Stylesheet -->
  <link rel="stylesheet" href="/assets/css/theme.css" />
</head>
<body class="bg-slate-50 text-brand-dark font-sans antialiased min-h-screen flex flex-col justify-between">

{ANNOUNCEMENT_BAR}
{NAV_HTML}

<!-- HERO / TITLE -->
<section class="relative bg-gradient-to-b from-brand-skyLight/50 via-white to-slate-50 py-12 md:py-16 border-b border-slate-200">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <nav class="flex items-center space-x-2 text-xs font-semibold text-slate-500 mb-4">
      <a href="/" class="hover:text-brand-sky transition">Home</a>
      <span>/</span>
      <span class="text-slate-400">Legal &amp; Platform Governance</span>
      <span>/</span>
      <span class="text-brand-dark font-bold">{heading}</span>
    </nav>
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-skyLight text-brand-sky border border-brand-sky/20 text-xs font-bold mb-4">
      {badge}
    </div>
    <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-brand-dark tracking-tight mb-4">
      {heading}
    </h1>
    <p class="text-slate-600 text-sm md:text-base max-w-3xl leading-relaxed">
      {subtitle}
    </p>
  </div>
</section>

<!-- MAIN CONTENT -->
<main class="py-12 md:py-16 bg-white flex-grow">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="prose prose-slate max-w-none space-y-8 text-sm text-slate-700 leading-relaxed">
      {content_html}
    </div>
  </div>
</main>

{GLOBAL_FOOTER}

<script src="/assets/js/forms.js"></script>
<script>
  const mBtn = document.getElementById('mobileMenuBtn');
  const mMenu = document.getElementById('mobileMenu');
  if (mBtn && mMenu) {{
    mBtn.addEventListener('click', () => mMenu.classList.toggle('hidden'));
  }}
</script>
</body>
</html>
"""

def generate_terms():
    content = """
    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 mb-8">
      <div class="flex items-center justify-between flex-wrap gap-2 text-xs text-slate-500">
        <span><strong>Effective Date:</strong> October 2026</span>
        <span><strong>Governing Law:</strong> Republic of India (Companies Act 2013, IT Act 2000, DPDP Act 2023)</span>
        <span><strong>Version:</strong> 2.4</span>
      </div>
    </div>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">1. Acceptance of Terms &amp; Digital Contract Formation</h2>
      <p>By accessing, browsing, registering an inquiry, paying professional fees, or utilizing the technology services provided by CraftEgon Corporate Services (CCS) via <code>corporateservices.craftegon.com</code>, you ("Client", "User", "Data Principal") agree to be bound legally by these Terms and Conditions. If you do not accept these terms, you must refrain from utilizing our platform and services.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">2. Nature of Platform &amp; Regulatory Non-Litigation Demarcation</h2>
      <div class="p-4 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs leading-relaxed">
        <strong>Strict Non-Law Firm Positioning:</strong> CraftEgon Corporate Services is a specialized corporate technology, compliance, secretarial facilitation, and business management operations platform. CCS is <strong>not a law firm</strong>, does not maintain a statutory law practice, and does not provide judicial advocacy, court appearances, or litigation representation before Courts of Law, Tribunals (NCLT, NCLAT, High Courts, Supreme Court), or Quasi-Judicial Benches.
      </div>
      <p>All legal drafting requiring court filing, judicial dispute representation, and statutory advocate appearances are carried out strictly and independently by licensed advocates and associate legal practitioners enrolled with the Bar Council of India in accordance with the Advocates Act, 1961.</p>
      <p>Statutory audits under Section 139/141 of the Companies Act 2013, tax audits under Section 44AB of the Income Tax Act 1961, Secretarial Audits (MR-3), and regulated attestations are performed exclusively by independent practicing Chartered Accountants (ICAI) and Company Secretaries (ICSI).</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">3. Scope of Technology &amp; Compliance Facilitation</h2>
      <p>CraftEgon provides digital software tools, automated document intake workflows, statutory calculation engines, DIN/DSC coordination, and filing facilitation for government portals including the Ministry of Corporate Affairs (MCA V3), GST Portal (GSTN), Income Tax TRACES / e-filing portal, and the Controller General of Patents, Designs and Trade Marks (CGPDTM).</p>
      <p>You acknowledge that government portal processing timelines, name approvals, registrar queries, and certificate issuances depend on the discretionary verification of government examiners and registrar authorities.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">4. Client Responsibilities &amp; Document Authenticity</h2>
      <p>Clients are solely responsible for ensuring that all documents, identity proofs (PAN, Aadhaar, Passport), registered office proofs (utility bills, NOCs), and shareholder records provided to CCS are genuine, authentic, and legally valid. CCS and its empanelled professionals bear no liability for departmental penalties, notices, or criminal prosecutions arising from forged, misstated, or fraudulent documents submitted by the client.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">5. Split-Fee Pricing, Stamp Duties &amp; Government Dues</h2>
      <p>All quotes provided on the platform explicitly differentiate between:</p>
      <ul class="list-disc pl-5 space-y-1">
        <li><strong>CraftEgon Professional Fee:</strong> Remuneration for secretarial drafting, filing preparation, document review, and case coordination (subject to 18% GST).</li>
        <li><strong>Official Government &amp; MCA Filing Fees:</strong> Statutory fees remitted directly to the Central Government or state exchequer.</li>
        <li><strong>State Stamp Duty:</strong> Computed dynamically based on state stamp acts and authorized capital schedules.</li>
      </ul>
      <p>Any increase in government fees, departmental inspection charges, or stamp duties during the course of incorporation or filing shall be borne by the client at actuals.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">6. Resubmission &amp; Requisition Policy</h2>
      <p>MCA V3 and Trademark portals typically grant up to 2 statutory resubmission windows to cure examiner requisitions. CCS facilitates these standard resubmissions at zero additional professional fees, provided the requisition is curable by supplemental documentation. In the event of outright name rejection or structural alteration requested by the client, nominal government re-filing fees shall apply.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">7. Limitation of Liability &amp; Force Majeure</h2>
      <p>To the maximum extent permitted by applicable Indian law, CraftEgon Corporate Services shall not be liable for indirect, incidental, or consequential damages resulting from downtime of government portals (MCA V3, GSTN, TRACES, IP India), regulatory changes, or sudden government fee hikes. CCS's total aggregate liability for any service failure shall be capped at the professional fees actually received by CCS for that specific mandate.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">8. Governing Law &amp; Dispute Resolution</h2>
      <p>These terms shall be governed by and construed in accordance with the laws of the Republic of India. Any disputes arising out of or in connection with these terms shall be subject to the exclusive jurisdiction of the competent courts in Trivandrum / Ernakulam, Kerala, India.</p>
    </section>
    """
    return render_page(
        title="Terms & Conditions",
        meta_desc="Terms and Conditions governing the use of CraftEgon Corporate Services legal-tech platform, split-fee pricing, client covenants, and non-litigation positioning.",
        canonical_path="/terms/",
        badge="📜 Statutory User Agreement",
        heading="Terms & Conditions",
        subtitle="Operational standards, platform boundaries, statutory fee policies, and legal covenants governing client mandates on CraftEgon Corporate Services.",
        content_html=content
    )

def generate_privacy():
    content = """
    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 mb-8">
      <div class="flex items-center justify-between flex-wrap gap-2 text-xs text-slate-500">
        <span><strong>Effective Date:</strong> October 2026</span>
        <span><strong>Compliance:</strong> Information Technology Act, 2000 &amp; SPDI Rules</span>
        <span><strong>Data Controller:</strong> CraftEgon Corporate Services</span>
      </div>
    </div>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">1. Privacy Commitment &amp; Scope</h2>
      <p>CraftEgon Corporate Services (CCS) respects and safeguards the privacy of our clients, directors, shareholders, and website visitors. This Privacy Policy details how we collect, store, process, and protect your personal and corporate financial data across our legal technology infrastructure.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">2. Information We Collect</h2>
      <p>To successfully process incorporation, tax filings, and corporate licenses, we collect the following categories of information:</p>
      <ul class="list-disc pl-5 space-y-1">
        <li><strong>Identity &amp; KYC Data:</strong> Permanent Account Number (PAN), Aadhaar, Passport, Voter ID, and Director Identification Numbers (DIN).</li>
        <li><strong>Contact &amp; Demographic Data:</strong> Legal name, email address, mobile/WhatsApp telephone number, registered office address, and utility bills.</li>
        <li><strong>Corporate Records:</strong> Proposed company names, shareholding structures, capitalization figures, Memorandum and Articles of Association.</li>
        <li><strong>Financial &amp; Tax Data:</strong> Bank account statements, cancelled cheques, GSTIN numbers, turnover details, and previous tax assessments.</li>
        <li><strong>Digital Credentials:</strong> Class 3 Digital Signature Certificate (DSC) files and PINs (processed strictly for authorized statutory portal signing).</li>
      </ul>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">3. Purpose of Processing &amp; Lawful Basis</h2>
      <p>We process your data exclusively for statutory fulfillment, including:</p>
      <ul class="list-disc pl-5 space-y-1">
        <li>Uploading statutory web forms to the Ministry of Corporate Affairs (SPICe+, DIR-3 KYC, AOC-4, MGT-7).</li>
        <li>Submitting GST registrations (REG-01) and monthly returns (GSTR-1, GSTR-3B).</li>
        <li>Filing corporate income tax returns (ITR-6) and withholding tax statements (24Q, 26Q).</li>
        <li>Transmitting trademark applications (TM-A) to the Trade Marks Registry.</li>
        <li>Facilitating client communication, statutory deadline reminders, and invoicing.</li>
      </ul>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">4. Data Sharing &amp; Third-Party Disclosures</h2>
      <p><strong>Zero Commercial Selling:</strong> CCS does not sell, rent, or lease your personal or corporate data to third-party telemarketers or advertisers.</p>
      <p>Data is disclosed solely to:</p>
      <ul class="list-disc pl-5 space-y-1">
        <li><strong>Statutory &amp; Government Portals:</strong> MCA V3, GSTN, TRACES, Income Tax Department, IP India, EPFO, and ESIC.</li>
        <li><strong>Empanelled Regulated Professionals:</strong> Qualified Chartered Accountants, Company Secretaries, and Trademark Attorneys engaged in executing your specific mandate.</li>
        <li><strong>Cloud &amp; Infrastructure Providers:</strong> Secure Tier-4 data centers within India operating under strict non-disclosure agreements.</li>
      </ul>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">5. Data Security &amp; Encryption Standards</h2>
      <p>We deploy bank-grade security protocols, including 256-bit SSL encryption in transit, AES-256 encryption at rest, role-based access controls, and document watermarking to prevent unauthorized disclosure or leakage of client KYC documents.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">6. Grievance Redressal Officer</h2>
      <p>In accordance with Information Technology Act, 2000 and rules made thereunder, inquiries or grievances regarding your data may be addressed to:</p>
      <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs">
        <p><strong>Grievance Officer:</strong> Compliance &amp; Data Security Desk</p>
        <p><strong>Entity:</strong> CraftEgon Corporate Services</p>
        <p><strong>Email:</strong> support@craftegon.com | privacy@craftegon.com</p>
        <p><strong>Desk:</strong> +91 99952 04905</p>
        <p><strong>Location:</strong> Technopark, Trivandrum, Kerala, India</p>
      </div>
    </section>
    """
    return render_page(
        title="Privacy Policy",
        meta_desc="Privacy Policy of CraftEgon Corporate Services detailing client KYC protection, zero commercial data sharing, and bank-grade encryption protocols.",
        canonical_path="/privacy/",
        badge="🔒 Data Privacy Standards",
        heading="Privacy Policy",
        subtitle="How CraftEgon Corporate Services collects, protects, and handles sensitive personal and corporate data in compliance with Indian regulatory standards.",
        content_html=content
    )

def generate_data_policy():
    content = """
    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 mb-8">
      <div class="flex items-center justify-between flex-wrap gap-2 text-xs text-slate-500">
        <span><strong>Statutory Governance:</strong> Digital Personal Data Protection Act, 2023 (DPDP Act)</span>
        <span><strong>Jurisdiction:</strong> Republic of India</span>
        <span><strong>Status:</strong> Active &amp; Enforceable</span>
      </div>
    </div>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">1. Legislative Framework &amp; DPDP Act, 2023 Alignment</h2>
      <p>CraftEgon Corporate Services (CCS) complies strictly with the <strong>Digital Personal Data Protection Act, 2023 (DPDP Act)</strong> enacted by the Parliament of India. This Data Policy sets forth our institutional architecture for managing digital personal data belonging to directors, promoters, key managerial personnel, and enterprise stakeholders.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">2. Roles: Data Fiduciary &amp; Data Processor</h2>
      <p>Under the DPDP Act, 2023:</p>
      <ul class="list-disc pl-5 space-y-2">
        <li><strong>CraftEgon as Data Fiduciary:</strong> When determining the purposes and means of processing personal data directly provided by clients for advisory, onboarding, and platform accounts.</li>
        <li><strong>CraftEgon as Data Processor:</strong> When processing employee payroll data, POSH inquiries, or HR governance records on behalf of client enterprise accounts.</li>
      </ul>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">3. Itemized Consent &amp; Notice Protocol</h2>
      <p>In accordance with Section 6 of the DPDP Act, 2023, data intake on CCS is governed by clear, standalone notices outlining:</p>
      <ul class="list-disc pl-5 space-y-1">
        <li>The specific personal data requested (e.g. Aadhaar, PAN, Passport).</li>
        <li>The precise statutory purpose (e.g. DIN allotment, MCA SPICe+ filing).</li>
        <li>The manner in which the Data Principal may exercise statutory rights or file grievances.</li>
      </ul>
      <p>Consent is collected via explicit affirmative digital actions and can be managed or reviewed via our compliance desk.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">4. Statutory Data Retention vs. Right to Erasure</h2>
      <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs leading-relaxed">
        <strong>Statutory Legal Override:</strong> Under Section 8(7) of the DPDP Act, 2023, personal data must be erased upon withdrawal of consent unless retention is mandated by law.<br><br>
        Because corporate records are governed by the <strong>Companies Act, 2013</strong> (requiring 8-year statutory retention of books and filings), the <strong>Income Tax Act, 1961</strong> (6 to 10 years assessment audit retention), and the <strong>Prevention of Money Laundering Act (PMLA), 2002</strong>, certain KYC records cannot be expunged prior to the expiration of mandatory statutory periods.
      </div>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">5. Data Principal Rights Architecture</h2>
      <p>Every Data Principal interacting with CraftEgon retains enforceable statutory rights:</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <h4 class="font-bold text-brand-dark text-xs uppercase mb-1">Right to Access</h4>
          <p class="text-xs text-slate-600">Request a summary of personal data being processed and identities of all professional entities with whom it was shared.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <h4 class="font-bold text-brand-dark text-xs uppercase mb-1">Right to Correction</h4>
          <p class="text-xs text-slate-600">Correct misleading, inaccurate, or outdated KYC and directorship records across active platform accounts.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <h4 class="font-bold text-brand-dark text-xs uppercase mb-1">Right to Grievance Redressal</h4>
          <p class="text-xs text-slate-600">Access rapid institutional resolution of privacy concerns prior to escalating to the Data Protection Board of India.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <h4 class="font-bold text-brand-dark text-xs uppercase mb-1">Right to Nominate</h4>
          <p class="text-xs text-slate-600">Nominate an individual to exercise data rights in the event of death or incapacity of the corporate principal.</p>
        </div>
      </div>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">6. Data Localization &amp; Cross-Border Transfers</h2>
      <p>All primary corporate client registries, encrypted DSC tokens, and statutory e-forms are hosted exclusively in Tier-4 enterprise data centers geographically located within the sovereign borders of the Republic of India, adhering strictly to Central Government transfer restrictions.</p>
    </section>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">7. Data Protection Officer (DPO) Contact</h2>
      <p>For data protection inquiries or to exercise your statutory rights under the DPDP Act, 2023, contact our designated Data Protection Officer:</p>
      <div class="p-4 rounded-xl bg-brand-skyLight/50 border border-brand-sky/20 text-xs">
        <p><strong>Designation:</strong> Data Protection Officer (DPO)</p>
        <p><strong>Email:</strong> dpo@craftegon.com | support@craftegon.com</p>
        <p><strong>Telephone:</strong> +91 99952 04905</p>
        <p><strong>Address:</strong> CraftEgon Corporate Services, Technopark, Trivandrum, Kerala 695581, India</p>
      </div>
    </section>
    """
    return render_page(
        title="Data Protection Policy (DPDP Act, 2023)",
        meta_desc="CraftEgon Corporate Services statutory Data Protection Policy aligned with the Digital Personal Data Protection Act 2023 (DPDP Act), Data Principal rights, and DPO desk.",
        canonical_path="/data-policy/",
        badge="🛡️ DPDP Act, 2023 Statutory Compliance",
        heading="Data Protection Policy",
        subtitle="Our institutional compliance framework under the Digital Personal Data Protection Act, 2023 (DPDP Act), governing client KYC protection and Data Principal rights.",
        content_html=content
    )

def generate_about():
    content = """
    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 mb-8">
      <div class="flex items-center justify-between flex-wrap gap-2 text-xs text-slate-500">
        <span><strong>Headquarters:</strong> Technopark, Trivandrum, Kerala, India</span>
        <span><strong>Focus:</strong> Enterprise Corporate Technology &amp; Regulatory Compliance</span>
        <span><strong>Empanelled:</strong> 100+ Chartered Accountants &amp; Secretarial Fellows</span>
      </div>
    </div>

    <section class="space-y-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">Democratizing Corporate LegalTech for Indian &amp; Global Enterprises</h2>
      <p>CraftEgon Corporate Services (CCS) is India's next-generation corporate legal technology, compliance management, and secretarial operations platform. We engineer modern digital workflows, transparent fee calculators, and AI-assisted document intake to simplify entity incorporation, ongoing ROC governance, tax filings, and intellectual property protection.</p>
      <p>We bridge the gap between high-growth founders and complex statutory frameworks by removing bureaucratic friction, eliminating hidden costs, and automating routine compliance tasks.</p>
    </section>

    <section class="space-y-6 pt-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">Our Three Architectural Pillars</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="w-10 h-10 rounded-xl bg-brand-skyLight text-brand-sky flex items-center justify-center font-bold text-lg mb-3 shadow-sm">
            💎
          </div>
          <h3 class="text-base font-bold text-brand-dark mb-1">100% Fee Transparency</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Every engagement clearly separates official Ministry/ROC government fees and state stamp duties from our professional consultation fees. Zero hidden surprise invoices.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="w-10 h-10 rounded-xl bg-brand-skyLight text-brand-sky flex items-center justify-center font-bold text-lg mb-3 shadow-sm">
            ⚡
          </div>
          <h3 class="text-base font-bold text-brand-dark mb-1">Digital Execution Engine</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Paperless workflows integrated directly with the MCA V3 portal, GSTN APIs, Income Tax TRACES, and IP India Trade Marks Registry for rapid statutory turnarounds.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="w-10 h-10 rounded-xl bg-brand-skyLight text-brand-sky flex items-center justify-center font-bold text-lg mb-3 shadow-sm">
            🤝
          </div>
          <h3 class="text-base font-bold text-brand-dark mb-1">Empanelled Senior Specialists</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Direct access to practicing FCA/FCS fellows, registered trademark attorneys, and compliance leads across 60 specialized corporate practice areas.
          </p>
        </div>
      </div>
    </section>

    <section class="space-y-4 pt-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">Institutional Regulatory Positioning</h2>
      <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-700 leading-relaxed space-y-2">
        <p>CraftEgon Corporate Services is proudly positioned as a corporate technology, compliance, and management platform. CCS is not a law firm and does not provide court litigation or judicial representation before courts or tribunals.</p>
        <p>All judicial proceedings and tribunal appearances are executed exclusively through independent, licensed advocates or associate law firms in accordance with the Advocates Act, 1961. Statutory audits, tax certifications, and secretarial audits are performed independently by licensed Chartered Accountants (ICAI) and Company Secretaries (ICSI).</p>
      </div>
    </section>

    <section class="space-y-4 pt-4">
      <h2 class="text-xl font-bold text-brand-dark border-b border-slate-200 pb-2">Corporate Office &amp; Connect</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-slate-600">
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <h4 class="font-bold text-brand-dark text-xs uppercase mb-1">Registered Corporate Desk</h4>
          <p>CraftEgon Corporate Services</p>
          <p>Technopark Phase 1, Trivandrum, Kerala 695581, India</p>
          <p class="mt-2 text-brand-sky font-semibold">support@craftegon.com</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
          <h4 class="font-bold text-brand-dark text-xs uppercase mb-1">Direct Advisory WhatsApp Desk</h4>
          <p>Direct priority routing to a senior secretarial associate:</p>
          <p class="font-bold text-brand-dark mt-1">+91 99952 04905</p>
          <a href="https://wa.me/919995204905" target="_blank" rel="noopener" class="inline-block mt-2 text-emerald-600 font-bold hover:underline">Chat on WhatsApp &rarr;</a>
        </div>
      </div>
    </section>
    """
    return render_page(
        title="About Us",
        meta_desc="About CraftEgon Corporate Services: Next-generation legal technology and corporate compliance operations platform for Indian and international enterprises.",
        canonical_path="/about/",
        badge="🏛️ Corporate LegalTech Platform",
        heading="About CraftEgon Corporate Services",
        subtitle="Empowering Indian founders and global enterprises with transparent fee architecture, automated secretarial workflows, and empanelled CA/CS specialists.",
        content_html=content
    )

def main():
    # 1. Terms
    os.makedirs("terms", exist_ok=True)
    terms_html = generate_terms()
    with open("terms/index.html", "w", encoding="utf-8") as f:
        f.write(terms_html)
    with open("terms.html", "w", encoding="utf-8") as f:
        f.write(terms_html)
    print("Generated: terms/index.html and terms.html")

    # 2. Privacy
    os.makedirs("privacy", exist_ok=True)
    privacy_html = generate_privacy()
    with open("privacy/index.html", "w", encoding="utf-8") as f:
        f.write(privacy_html)
    with open("privacy.html", "w", encoding="utf-8") as f:
        f.write(privacy_html)
    print("Generated: privacy/index.html and privacy.html")

    # 3. Data Policy
    os.makedirs("data-policy", exist_ok=True)
    data_policy_html = generate_data_policy()
    with open("data-policy/index.html", "w", encoding="utf-8") as f:
        f.write(data_policy_html)
    with open("data-policy.html", "w", encoding="utf-8") as f:
        f.write(data_policy_html)
    print("Generated: data-policy/index.html and data-policy.html")

    # 4. About
    os.makedirs("about", exist_ok=True)
    about_html = generate_about()
    with open("about/index.html", "w", encoding="utf-8") as f:
        f.write(about_html)
    with open("about.html", "w", encoding="utf-8") as f:
        f.write(about_html)
    print("Generated: about/index.html and about.html")

if __name__ == "__main__":
    main()
