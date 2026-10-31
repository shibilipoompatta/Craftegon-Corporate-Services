"""
inject_technical_seo.py
Analyzes all HTML files, extracts title, description, and content,
and injects valid JSON-LD schemas (Organization, Service, BreadcrumbList, FAQPage)
along with canonical links, Open Graph, and Twitter Card meta tags.
"""

import os
import glob
import re
import json
import html

CANONICAL_DOMAIN = "https://corporateservices.craftegon.com"
DEFAULT_OG_IMAGE = f"{CANONICAL_DOMAIN}/assets/images/og-image.png"

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "CraftEgon Corporate Services",
    "alternateName": "CCS Corporate LegalTech Platform",
    "url": f"{CANONICAL_DOMAIN}/",
    "logo": f"{CANONICAL_DOMAIN}/assets/images/logo.png",
    "image": DEFAULT_OG_IMAGE,
    "description": "Enterprise Corporate LegalTech, Taxation, Company Incorporation & Secretarial Compliance Management Platform.",
    "telephone": "+91-8606918247",
    "email": "support@craftegon.com",
    "priceRange": "₹₹",
    "address": [
        {
            "@type": "PostalAddress",
            "streetAddress": "Markaz Knowledge City",
            "addressLocality": "Kozhikode",
            "addressRegion": "Kerala",
            "postalCode": "673580",
            "addressCountry": "IN"
        },
        {
            "@type": "PostalAddress",
            "streetAddress": "Technopark Phase 1",
            "addressLocality": "Thiruvananthapuram",
            "addressRegion": "Kerala",
            "postalCode": "695581",
            "addressCountry": "IN"
        }
    ],
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "19:00"
        }
    ],
    "sameAs": [
        "https://craftegon.com",
        "https://wa.me/918606918247"
    ]
}

CATEGORY_NAMES = {
    "business-setup": "Business Setup & Formation",
    "gst-advisory": "GST Advisory & Filings",
    "corporate-governance": "Corporate Governance & MCA Compliance",
    "direct-tax": "Direct Tax & TDS Advisory",
    "brand-protection": "Brand Protection & Intellectual Property",
    "workforce-digital": "Workforce & Digital Infrastructure"
}

def clean_path(filepath):
    norm = filepath.replace('\\', '/')
    if norm.startswith('./'):
        norm = norm[2:]
    if norm == 'index.html':
        return '/'
    if norm.endswith('/index.html'):
        return '/' + norm[:-10] + '/'
    return '/' + norm

def extract_meta(content):
    title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = html.unescape(title_m.group(1)).strip() if title_m else "CraftEgon Corporate Services"

    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not desc_m:
        desc_m = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', content, re.IGNORECASE | re.DOTALL)
    desc = html.unescape(desc_m.group(1)).strip() if desc_m else "Fastest Company Incorporation, GST Registration, Trademark Filing & MCA Compliance handled by expert CAs & CSs."

    return title, desc

def extract_faqs_from_html(content):
    faqs = []
    # Pattern 1: FAQ buttons with text and answer sibling
    q_matches = re.findall(r'<button[^>]*onclick=["\']toggleFaq\(\d+\)["\'][^>]*>.*?<span>(.*?)</span>.*?</button>\s*<div[^>]*class=["\'][^"\']*hidden[^"\']*["\'][^>]*>(.*?)</div>', content, re.DOTALL)
    for q, a in q_matches:
        clean_q = re.sub(r'<[^>]+>', '', q).strip()
        clean_a = re.sub(r'<[^>]+>', '', a).strip()
        if clean_q and clean_a:
            faqs.append({"question": clean_q, "answer": clean_a})
    
    # Pattern 2: Typical Q&A blocks / knowledge faq items
    if not faqs:
        items = re.findall(r'<div[^>]*class=["\'][^"\']*faq[^"\']*["\'][^>]*>.*?<h\d[^>]*>(.*?)</h\d>.*?<p[^>]*>(.*?)</p>', content, re.DOTALL | re.IGNORECASE)
        for q, a in items:
            clean_q = re.sub(r'<[^>]+>', '', q).strip()
            clean_a = re.sub(r'<[^>]+>', '', a).strip()
            if clean_q and clean_a and len(clean_q) > 5:
                faqs.append({"question": clean_q, "answer": clean_a})

    return faqs[:6]

def build_breadcrumbs(url_path, title):
    segments = [s for s in url_path.strip('/').split('/') if s]
    items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": f"{CANONICAL_DOMAIN}/"
        }
    ]
    
    if not segments:
        return None

    current_path = ""
    for idx, seg in enumerate(segments):
        current_path += "/" + seg
        is_last = (idx == len(segments) - 1)
        
        # Determine name
        if seg in CATEGORY_NAMES:
            seg_name = CATEGORY_NAMES[seg]
        elif seg == 'knowledge':
            seg_name = "Knowledge Hub"
        elif seg.endswith('.html'):
            seg_clean = seg[:-5].replace('-', ' ').title()
            seg_name = title.split('|')[0].split('-')[0].strip() if is_last else seg_clean
        else:
            seg_name = title.split('|')[0].split('-')[0].strip() if is_last else seg.replace('-', ' ').title()

        item_url = f"{CANONICAL_DOMAIN}{current_path}"
        if not current_path.endswith('.html') and not current_path.endswith('/'):
            item_url += '/'

        items.append({
            "@type": "ListItem",
            "position": idx + 2,
            "name": seg_name,
            "item": item_url
        })

    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def build_service_schema(title, desc, url, price="4999"):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": title.split('|')[0].strip(),
        "serviceType": "Corporate Legal & Financial Compliance",
        "description": desc,
        "url": url,
        "provider": {
            "@type": "ProfessionalService",
            "name": "CraftEgon Corporate Services",
            "url": f"{CANONICAL_DOMAIN}/",
            "telephone": "+91-8606918247"
        },
        "areaServed": {
            "@type": "Country",
            "name": "India"
        },
        "offers": {
            "@type": "Offer",
            "price": price,
            "priceCurrency": "INR",
            "availability": "https://schema.org/InStock"
        }
    }

def build_faq_schema(faqs):
    if not faqs:
        return None
    entity_list = []
    for f in faqs:
        entity_list.append({
            "@type": "Question",
            "name": f["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["answer"]
            }
        })
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entity_list
    }

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    url_path = clean_path(filepath)
    canonical_url = f"{CANONICAL_DOMAIN}{url_path}"
    title, desc = extract_meta(content)

    # Check for price in page content
    price_m = re.search(r'₹([\d,]+)', content)
    price_val = price_m.group(1).replace(',', '') if price_m else "4999"
    if not price_val.isdigit() or int(price_val) < 500:
        price_val = "2499"

    # Construct Schemas
    schemas_to_inject = [ORG_SCHEMA]

    # Breadcrumbs
    if url_path != '/':
        bc = build_breadcrumbs(url_path, title)
        if bc:
            schemas_to_inject.append(bc)

    # Service Schema (for product pages, hub pages, and service landing pages)
    is_service_page = any(cat in url_path for cat in CATEGORY_NAMES) or any(s in url_path for s in ['pvt-ltd', 'gst', 'trademark', 'licenses'])
    if is_service_page and url_path != '/':
        schemas_to_inject.append(build_service_schema(title, desc, canonical_url, price_val))

    # FAQ Schema
    faqs = extract_faqs_from_html(content)
    if faqs:
        faq_schema = build_faq_schema(faqs)
        if faq_schema:
            schemas_to_inject.append(faq_schema)

    # Open Graph & Twitter meta tags
    safe_title = html.escape(title)
    safe_desc = html.escape(desc)
    og_type = "article" if "/knowledge/" in url_path and not url_path.endswith('/knowledge/') else "website"

    og_meta = f"""    <!-- Canonical URL -->
    <link rel="canonical" href="{canonical_url}" />

    <!-- Open Graph / Facebook Meta Tags -->
    <meta property="og:type" content="{og_type}" />
    <meta property="og:site_name" content="CraftEgon Corporate Services" />
    <meta property="og:title" content="{safe_title}" />
    <meta property="og:description" content="{safe_desc}" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:image" content="{DEFAULT_OG_IMAGE}" />

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@craftegon" />
    <meta name="twitter:title" content="{safe_title}" />
    <meta name="twitter:description" content="{safe_desc}" />
    <meta name="twitter:image" content="{DEFAULT_OG_IMAGE}" />"""

    # Format JSON-LD script tags
    jsonld_tags = "\n    <!-- Structured Data (JSON-LD) -->\n"
    for s in schemas_to_inject:
        jsonld_tags += f'    <script type="application/ld+json">\n{json.dumps(s, indent=4, ensure_ascii=False)}\n    </script>\n'

    # Remove existing canonical, JSON-LD scripts, and OG/Twitter tags to prevent duplicates
    cleaned_content = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>', '', content, flags=re.IGNORECASE)
    cleaned_content = re.sub(r'<!--\s*(Canonical|Open Graph|Twitter Card|Structured Data).*?-->', '', cleaned_content, flags=re.DOTALL)
    cleaned_content = re.sub(r'<meta\s+property=["\']og:[^"\']*["\'][^>]*>', '', cleaned_content)
    cleaned_content = re.sub(r'<meta\s+name=["\']twitter:[^"\']*["\'][^>]*>', '', cleaned_content)
    cleaned_content = re.sub(r'<script\s+type=["\']application/ld\+json["\']>.*?</script>', '', cleaned_content, flags=re.DOTALL)

    # Inject right before </head>
    replacement = f"{og_meta}\n{jsonld_tags}\n</head>"
    if '</head>' in cleaned_content:
        new_content = cleaned_content.replace('</head>', replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    html_files = glob.glob('*.html') + glob.glob('**/*.html', recursive=True)
    count = 0
    for f in html_files:
        norm = f.replace('\\', '/')
        if 'node_modules' in norm or '.git' in norm:
            continue
        if process_file(f):
            count += 1
            print(f"Injected SEO & JSON-LD: {f}")

    print(f"Successfully processed {count} HTML files.")

if __name__ == '__main__':
    main()
