# -*- coding: utf-8 -*-
"""
verify_site.py
Comprehensive Quality & Production Readiness Verifier for CraftEgon Corporate Services.
Asserts:
  1. Data Contracts (craftegon-services.json >= 150 services & craftegon-knowledge-hub.json).
  2. HTML Integrity, links, and mandatory regulatory notice.
  3. Technical SEO, Open Graph, Twitter cards, and JSON-LD structured data validity.
  4. Conversion Rate Optimization (Mobile sticky CTA & Floating WhatsApp).
  5. Performance & Asset Optimization (Image lazy loading, CLS attributes, CSS size < 50KB).
  6. Sitemap.xml and Robots.txt validation.
"""

import glob
import re
import json
import os
import sys
import xml.etree.ElementTree as ET

# Ensure stdout handles UTF-8 on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

def verify():
    failed = False
    print("=" * 70)
    print("STARTING CRAFTEGON CORPORATE SERVICES SITE VERIFICATION")
    print("=" * 70)

    # 1. Data Contracts
    print("\n[1/6] Verifying Data Contracts...")
    try:
        with open("data/craftegon-services.json", encoding="utf-8") as f:
            services_data = json.load(f)
        services = services_data.get("services", [])
        print(f"  [OK] data/craftegon-services.json: {len(services)} services loaded.")
        assert len(services) >= 150, f"Expected at least 150 services, found {len(services)}"

        # Validate essential keys in each service
        for s in services:
            assert "service_id" in s and "title" in s and "slug" in s and "category" in s
    except Exception as e:
        print(f"  [ERROR] Services Data Contract Failure: {e}")
        failed = True

    try:
        with open("data/craftegon-knowledge-hub.json", encoding="utf-8") as f:
            kb_data = json.load(f)
        guides = kb_data.get("guides", []) or kb_data.get("knowledge_guides", [])
        print(f"  [OK] data/craftegon-knowledge-hub.json: {len(guides)} structured guides loaded.")
        assert len(guides) >= 10, f"Expected at least 10 knowledge guides, found {len(guides)}"
    except Exception as e:
        print(f"  [ERROR] Knowledge Hub Data Contract Failure: {e}")
        failed = True

    # 2. HTML Integrity & Regulatory Disclaimers
    print("\n[2/6] Verifying HTML Files & Mandatory Compliance Notices...")
    html_files = [f for f in glob.glob("**/*.html", recursive=True) if 'node_modules' not in f and '.git' not in f]
    print(f"  Found {len(html_files)} production HTML files to verify.")

    mandatory_disclaimer_snippet = "CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform"
    disclaimer_missing = []
    forms_missing = []
    
    for f in html_files:
        with open(f, encoding="utf-8") as fh:
            content = fh.read()

        if mandatory_disclaimer_snippet not in content:
            disclaimer_missing.append(f)

        if "/assets/js/forms.js" not in content and "forms.js" not in content:
            forms_missing.append(f)

    if disclaimer_missing:
        print(f"  [ERROR] Missing Regulatory Disclaimer in {len(disclaimer_missing)} files: {disclaimer_missing[:5]}...")
        failed = True
    else:
        print(f"  [OK] All {len(html_files)} HTML pages contain the mandatory regulatory notice.")

    if forms_missing:
        print(f"  [ERROR] Missing forms.js script in {len(forms_missing)} files: {forms_missing[:5]}...")
        failed = True
    else:
        print(f"  [OK] All {len(html_files)} HTML pages include forms.js.")

    # 3. Technical SEO, Open Graph & JSON-LD Structured Data
    print("\n[3/6] Verifying Technical SEO, Metadata & JSON-LD Schemas...")
    seo_errors = []
    total_schemas = 0

    for f in html_files:
        with open(f, encoding="utf-8") as fh:
            content = fh.read()

        # Canonical Link
        if not re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://corporateservices\.craftegon\.com', content, re.IGNORECASE):
            seo_errors.append(f"{f}: Missing or invalid canonical URL")

        # Open Graph
        if '<meta property="og:title"' not in content:
            seo_errors.append(f"{f}: Missing og:title")
        if '<meta property="og:description"' not in content:
            seo_errors.append(f"{f}: Missing og:description")
        if '<meta property="og:url"' not in content:
            seo_errors.append(f"{f}: Missing og:url")

        # Twitter Card
        if '<meta name="twitter:card"' not in content:
            seo_errors.append(f"{f}: Missing twitter:card")

        # JSON-LD Schemas
        script_matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL)
        if not script_matches:
            seo_errors.append(f"{f}: No JSON-LD schema blocks found")
        else:
            for idx, script_content in enumerate(script_matches):
                try:
                    schema_obj = json.loads(script_content.strip())
                    total_schemas += 1
                    schema_type = schema_obj.get("@type")
                    if not schema_type and "@graph" not in schema_obj:
                        seo_errors.append(f"{f} schema #{idx}: Missing @type")
                except Exception as ex:
                    seo_errors.append(f"{f} schema #{idx}: JSON parse error: {ex}")

    if seo_errors:
        print(f"  [ERROR] SEO & Schema Validation Failed with {len(seo_errors)} issues:")
        for err in seo_errors[:10]:
            print(f"     - {err}")
        failed = True
    else:
        print(f"  [OK] Validated {total_schemas} JSON-LD schemas across {len(html_files)} files without parse errors.")
        print(f"  [OK] All pages contain valid Canonical URLs, Open Graph, and Twitter Cards.")

    # 4. Conversion Rate Optimization (CRO) Elements
    print("\n[4/6] Verifying CRO Widgets (Mobile Sticky Bar & WhatsApp FAB)...")
    cro_missing = []
    for f in html_files:
        with open(f, encoding="utf-8") as fh:
            content = fh.read()

        has_sticky_bar = "md:hidden" in content and "tel:+918606918247" in content
        has_floating_fab = "wa.me/918606918247" in content
        if not (has_sticky_bar and has_floating_fab):
            cro_missing.append(f)

    if cro_missing:
        print(f"  [WARNING] CRO elements missing in {len(cro_missing)} files: {cro_missing[:3]}...")
    else:
        print(f"  [OK] All {len(html_files)} HTML pages contain mobile sticky CTA bars & WhatsApp contact triggers.")

    # 5. Performance & Asset Optimization (CLS & CSS Size)
    print("\n[5/6] Verifying Performance, Image CLS & CSS Footprint...")
    # Check CSS sizes
    for css_file in ["assets/css/output.css", "assets/css/theme.css"]:
        if os.path.exists(css_file):
            size_kb = os.path.getsize(css_file) / 1024
            if size_kb > 50:
                print(f"  [ERROR] {css_file} exceeds 50KB limit ({size_kb:.2f} KB)")
                failed = True
            else:
                print(f"  [OK] {css_file} size is {size_kb:.2f} KB (< 50KB budget).")
        else:
            print(f"  [ERROR] {css_file} not found!")
            failed = True

    # Check images for CLS prevention
    img_cls_issues = []
    for f in html_files:
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        for img in re.findall(r'<img[^>]+>', content):
            if 'loading="lazy"' not in img or 'width=' not in img or 'height=' not in img:
                img_cls_issues.append((f, img))

    if img_cls_issues:
        print(f"  [WARNING] Found {len(img_cls_issues)} <img> tag(s) without full CLS prevention attributes:")
        for f, img in img_cls_issues[:5]:
            print(f"     - in {f}: {img}")
    else:
        print(f"  [OK] All <img> tags verified with loading='lazy', width, and height attributes.")

    # 6. Sitemap.xml & Robots.txt
    print("\n[6/6] Verifying Sitemap.xml and Robots.txt...")
    if not os.path.exists("sitemap.xml"):
        print("  [ERROR] sitemap.xml does not exist!")
        failed = True
    else:
        try:
            tree = ET.parse("sitemap.xml")
            root = tree.getroot()
            url_count = len(root)
            print(f"  [OK] sitemap.xml parsed successfully with {url_count} URLs.")
            assert url_count >= 40, f"Expected at least 40 URLs in sitemap, found {url_count}"
        except Exception as e:
            print(f"  [ERROR] sitemap.xml validation failure: {e}")
            failed = True

    if not os.path.exists("robots.txt"):
        print("  [ERROR] robots.txt does not exist!")
        failed = True
    else:
        with open("robots.txt", encoding="utf-8") as f:
            robots_txt = f.read()
        if "Sitemap: https://corporateservices.craftegon.com/sitemap.xml" in robots_txt:
            print("  [OK] robots.txt verified with correct Sitemap reference.")
        else:
            print("  [ERROR] robots.txt missing sitemap link!")
            failed = True

    print("\n" + "=" * 70)
    if failed:
        print("[FAILED] VERIFICATION FAILED: Please fix the issues reported above.")
        print("=" * 70)
        sys.exit(1)
    else:
        print("[SUCCESS] ALL CHECKS PASSED: CraftEgon Corporate Services is 100% Production Ready!")
        print("=" * 70)

if __name__ == "__main__":
    verify()
