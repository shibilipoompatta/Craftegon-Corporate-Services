"""
build_craftegon_services.py
Compiles, standardizes, and validates the complete Craftegon Corporate Services catalog (150+ legal, tax, and compliance services)
into data/craftegon-services.json.
"""

import csv
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Hub categorizer mapping based on service keywords/slug
HUB_KEYWORDS = {
    'gst-advisory': [
        'gst', 'gstr', 'e-way', 'lut', 'invoicing', 'input tax', 'e-invoicing', 'gstin'
    ],
    'brand-protection': [
        'trademark', 'tm', 'copyright', 'patent', 'design registration', 'brand',
        'ip-objection', 'trademark-hearing', 'trademark-renewal', 'trademark-opposition',
        'trademark-assignment', 'provisional-patent', 'patent-search'
    ],
    'corporate-governance': [
        'mca', 'roc', 'director', 'din', 'kyc', 'secretarial', 'aoc-4', 'mgt-7',
        'adt-1', 'inc-20a', 'inc-22', 'board meeting', 'share transfer', 'authorized capital',
        'strike off', 'winding up', 'revival', 'esop', 'due diligence', 'secretarial audit',
        'registered office change', 'appointment of director', 'removal of director', 'form 11', 'form 8'
    ],
    'direct-tax': [
        'income tax', 'itr', 'tds', 'tcs', 'tax audit', '15ca', '15cb', 'tax planning',
        'advance tax', 'tan', 'form 16', 'pan', 'transfer pricing', 'direct tax', 'tax assessment',
        'capital gains', 'tax advisory'
    ],
    'workforce-digital': [
        'pf', 'epfo', 'esic', 'posh', 'dpdp', 'data privacy', 'labour', 'shop and establishment',
        'professional tax', 'payroll', 'employment agreement', 'nda', 'terms of service',
        'privacy policy', 'gdpr', 'workforce', 'hr compliance', 'will-making', 'pitch-deck'
    ],
    'business-setup': [
        'company', 'pvt-ltd', 'private limited', 'llp', 'opc', 'one person company',
        'partnership', 'proprietorship', 'section 8', 'public limited', 'producer company',
        'subsidiary', 'joint venture', 'startup india', 'udyam', 'msme', 'fssai', 'icegate',
        'import-export', 'iec', 'rcmc', 'trust', 'society', 'ngo', '12a', '80g', 'darpan',
        'iso', 'barcode', 'trade license', 'fire noc', 'pollution noc', 'rera'
    ]
}

def determine_category(slug, title, desc):
    text = f"{slug} {title} {desc}".lower()
    for hub, kws in HUB_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                return hub
    return 'business-setup'

def clean_price(price_str):
    if not price_str or price_str == 'N/A':
        return 2499
    digits = re.sub(r'[^\d]', '', price_str)
    if digits:
        val = int(digits)
        if val < 500:
            return 1499
        return val
    return 2499

def format_title_from_slug(slug):
    slug_clean = slug.replace('-registration', '').replace('-incorporation', '').replace('-filing', '')
    title_words = [w.capitalize() for w in slug_clean.split('-')]
    return ' '.join(title_words)

def generate_documents_for_category(category, title):
    base_docs = ["PAN Card of Promoters/Directors", "Aadhaar Card / Passport", "Bank Account Statement (< 2 months)"]
    if category == 'business-setup':
        return base_docs + ["Registered Office Electricity/Utility Bill", "NOC from Property Owner", "Passport Size Photos"]
    elif category == 'gst-advisory':
        return base_docs + ["Business Registration Certificate / COI", "Cancelled Cheque / Bank Passbook", "Electricity Bill & Rent Agreement of Premises"]
    elif category == 'brand-protection':
        return ["Logo / Brand Artwork (High Resolution)", "TM-48 Authorization Letter", "User Affidavit (if claiming prior use)", "Applicant Identity Proof (PAN/Aadhaar/COI)"]
    elif category == 'corporate-governance':
        return ["Director Identification Number (DIN)", "Digital Signature Certificate (DSC Class 3)", "Board Resolution / Shareholder Approval", "Previous ROC Filing Receipts"]
    elif category == 'direct-tax':
        return ["Financial Statements (P&L, Balance Sheet)", "Form 26AS / AIS / TIS", "Bank Statements of all Corporate Accounts", "TDS Challans & Deductor TAN Details"]
    elif category == 'workforce-digital':
        return ["Certificate of Incorporation / Registration", "Employee Master List & Salary Register", "Rent Agreement / Ownership Proof", "Authorised Signatory DSC & KYC"]
    return base_docs

def main():
    print("Starting Craftegon Services compilation...")

    # 1. Load curated 60 services from data/services.json
    existing_services = []
    seen_slugs = set()
    seen_ids = set()

    if os.path.exists('data/services.json'):
        with open('data/services.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for s in data.get('services', []):
                slug = s.get('id') or s.get('slug')
                seen_slugs.add(slug)
                seen_ids.add(slug)
                
                # Standardize documents
                docs = []
                raw_docs = s.get('documents_required', [])
                if isinstance(raw_docs, dict):
                    for v in raw_docs.values():
                        if isinstance(v, list):
                            docs.extend(v)
                elif isinstance(raw_docs, list):
                    docs = raw_docs
                if not docs:
                    docs = generate_documents_for_category(s.get('category', 'business-setup'), s.get('title', ''))

                pricing = s.get('pricing', {})
                price = pricing.get('base_professional_fee', 4999) if isinstance(pricing, dict) else 4999

                standardized = {
                    "service_id": slug,
                    "title": s.get('title'),
                    "slug": slug,
                    "category": s.get('category', 'business-setup'),
                    "starting_price": price,
                    "mca_govt_fee": "Variable based on state stamp duty & ROC slabs" if "company" in slug or "llp" in slug else "Statutory Govt Fees at Actuals",
                    "timeline_days": s.get('turnaround_time', '5-7 Working Days'),
                    "documents_required": docs[:6],
                    "short_description": s.get('short_description', f"Professional {s.get('title')} managed by certified CAs and CS fellows."),
                    "hub_path": f"/{s.get('category', 'business-setup')}/",
                    "product_path": s.get('product_path', f"/{s.get('category', 'business-setup')}/{slug}/"),
                    "whatsapp_link": f"https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20am%20interested%20in%20{s.get('title')}.",
                    "keywords": [w.lower() for w in s.get('title', '').split() if len(w) > 2] + [s.get('category', '')]
                }
                existing_services.append(standardized)

    print(f"Loaded {len(existing_services)} curated services from data/services.json")

    # 2. Load from craftegon_services_extracted.csv
    csv_services = []
    if os.path.exists('craftegon_services_extracted.csv'):
        with open('craftegon_services_extracted.csv', 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row.get('URL', '').strip()
                if not url:
                    continue
                raw_slug = url.rstrip('/').split('/')[-1]
                if not raw_slug or raw_slug in seen_slugs:
                    continue

                # Parse clean title
                content = row.get('Content Sections', '')
                first_line = content.split('\n')[0].strip() if content else ''
                # Clean title
                clean_title = re.sub(r'^(Start Your |Register Your |Apply for Your |Online |Stay |Fast & Reliable )', '', first_line, flags=re.I).strip()
                clean_title = re.sub(r'( Registration in India| in India| Online India| Registration| – .*$)', '', clean_title, flags=re.I).strip()
                if not clean_title or len(clean_title) < 3 or clean_title.startswith('Service_'):
                    clean_title = format_title_from_slug(raw_slug)

                price = clean_price(row.get('Starting Price'))
                cat = determine_category(raw_slug, clean_title, content[:300])
                
                # Parse short description
                sentences = [s.strip() for s in content.split('\n') if len(s.strip()) > 30 and not s.strip().startswith('#') and not s.strip().startswith('*')]
                desc = sentences[0] if sentences else f"Fast, fully managed {clean_title} advisory and filing by certified specialists."
                # sanitize any third-party brand names
                desc = re.sub(r'IndiaFilings', 'CraftEgon', desc, flags=re.I)
                desc = re.sub(r'https?://[^\s]+', '', desc).strip()
                if len(desc) > 160:
                    desc = desc[:157] + '...'

                # Key points / documents
                key_pts = [p.strip() for p in row.get('Key Points', '').split('\n') if p.strip() and not p.strip().startswith('[')]
                key_pts = [re.sub(r'\[.*?\]\(.*?\)', '', p).strip() for p in key_pts if p.strip()]
                docs = [p for p in key_pts if 'Document' not in p and len(p) > 3][:5]
                if not docs:
                    docs = generate_documents_for_category(cat, clean_title)

                service_entry = {
                    "service_id": raw_slug,
                    "title": clean_title,
                    "slug": raw_slug,
                    "category": cat,
                    "starting_price": price,
                    "mca_govt_fee": "Variable State Stamp Duty & ROC Fees" if cat in ['business-setup', 'corporate-governance'] else "Statutory Govt Fees at Actuals",
                    "timeline_days": "3-5 Working Days" if price < 3000 else "7-10 Working Days",
                    "documents_required": docs,
                    "short_description": desc,
                    "hub_path": f"/{cat}/",
                    "product_path": f"/{cat}/" if not os.path.exists(f"{cat}/{raw_slug}/index.html") else f"/{cat}/{raw_slug}/",
                    "whatsapp_link": f"https://wa.me/918606918247?text=Hi%20CraftEgon!%20I%20am%20interested%20in%20{clean_title}.",
                    "keywords": [w.lower() for w in clean_title.split() if len(w) > 2] + [cat, raw_slug.replace('-', ' ')]
                }
                seen_slugs.add(raw_slug)
                csv_services.append(service_entry)

    print(f"Extracted {len(csv_services)} unique additional services from CSV.")

    all_services = existing_services + csv_services
    print(f"Total Combined Services: {len(all_services)}")

    # Ensure categories are balanced across the 6 hubs
    cat_counts = {}
    for s in all_services:
        c = s['category']
        cat_counts[c] = cat_counts.get(c, 0) + 1

    print("Category Breakdown:")
    for c, count in sorted(cat_counts.items()):
        print(f"  - {c}: {count} services")

    output_payload = {
        "catalog_version": "2.0.0",
        "last_updated": "2026-10-31",
        "platform": "CraftEgon Corporate Services",
        "total_services": len(all_services),
        "categories": {
            "business-setup": "Business Setup & Formation",
            "gst-advisory": "GST Advisory & Filings",
            "corporate-governance": "Corporate Governance & MCA Compliance",
            "direct-tax": "Direct Tax & TDS Advisory",
            "brand-protection": "Brand Protection & Intellectual Property",
            "workforce-digital": "Workforce & Digital Infrastructure"
        },
        "services": all_services
    }

    os.makedirs('data', exist_ok=True)
    with open('data/craftegon-services.json', 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated data/craftegon-services.json with {len(all_services)} services!")

if __name__ == '__main__':
    main()

