"""
build_sitemap.py
Crawls all HTML pages in the CraftEgon Corporate Services repository and generates
valid sitemap.xml and robots.txt files for search engine indexing.
"""

import os
import glob
import re
from datetime import datetime

CANONICAL_DOMAIN = "https://corporateservices.craftegon.com"

# Priority and frequency mapping
PAGE_RULES = {
    # Homepage
    "/": {"priority": "1.0", "changefreq": "daily"},
    # Category Hubs
    "/business-setup/": {"priority": "0.9", "changefreq": "weekly"},
    "/gst-advisory/": {"priority": "0.9", "changefreq": "weekly"},
    "/corporate-governance/": {"priority": "0.9", "changefreq": "weekly"},
    "/direct-tax/": {"priority": "0.9", "changefreq": "weekly"},
    "/brand-protection/": {"priority": "0.9", "changefreq": "weekly"},
    "/workforce-digital/": {"priority": "0.9", "changefreq": "weekly"},
    # Knowledge Hub
    "/knowledge/": {"priority": "0.9", "changefreq": "weekly"},
    # High-Priority Services
    "/gst.html": {"priority": "0.85", "changefreq": "weekly"},
    "/pvt-ltd.html": {"priority": "0.85", "changefreq": "weekly"},
    "/trademark.html": {"priority": "0.85", "changefreq": "weekly"},
    "/licenses.html": {"priority": "0.85", "changefreq": "weekly"},
    "/experts.html": {"priority": "0.8", "changefreq": "weekly"},
    # Informational & Legal
    "/about.html": {"priority": "0.7", "changefreq": "monthly"},
    "/contact.html": {"priority": "0.7", "changefreq": "monthly"},
    "/terms-and-conditions.html": {"priority": "0.5", "changefreq": "monthly"},
    "/terms.html": {"priority": "0.5", "changefreq": "monthly"},
    "/privacy-policy.html": {"priority": "0.5", "changefreq": "monthly"},
    "/privacy.html": {"priority": "0.5", "changefreq": "monthly"},
    "/data-policy.html": {"priority": "0.5", "changefreq": "monthly"},
}

def clean_url_path(filepath):
    normalized = filepath.replace('\\', '/')
    if normalized.startswith('./'):
        normalized = normalized[2:]
        
    if normalized == 'index.html':
        return '/'
    if normalized.endswith('/index.html'):
        return '/' + normalized[:-10]  # remove index.html, keep trailing slash
    return '/' + normalized

def get_priority_and_freq(url_path):
    if url_path in PAGE_RULES:
        return PAGE_RULES[url_path]
    if '/knowledge/' in url_path:
        return {"priority": "0.8", "changefreq": "weekly"}
    if any(h in url_path for h in ['business-setup', 'gst-advisory', 'corporate-governance', 'direct-tax', 'brand-protection', 'workforce-digital']):
        return {"priority": "0.8", "changefreq": "weekly"}
    return {"priority": "0.6", "changefreq": "monthly"}

def generate_sitemap():
    print("Generating sitemap.xml...")
    # Find all html files excluding templates/node_modules/tests
    all_files = glob.glob('*.html') + glob.glob('**/*.html', recursive=True)
    
    unique_urls = {}
    today_str = datetime.now().strftime("%Y-%m-%d")

    for f in all_files:
        norm = f.replace('\\', '/')
        if 'node_modules' in norm or '.git' in norm:
            continue
        
        url_path = clean_url_path(f)
        full_url = f"{CANONICAL_DOMAIN}{url_path}"
        
        # Get file modification date if possible
        try:
            mtime = os.path.getmtime(f)
            mod_date = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
        except:
            mod_date = today_str

        rule = get_priority_and_freq(url_path)
        unique_urls[full_url] = {
            "lastmod": mod_date,
            "changefreq": rule["changefreq"],
            "priority": rule["priority"]
        }

    # Sort URLs: root first, then highest priority
    sorted_urls = sorted(
        unique_urls.items(),
        key=lambda item: (-float(item[1]["priority"]), item[0])
    )

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for loc, meta in sorted_urls:
        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{loc}</loc>')
        xml_lines.append(f'    <lastmod>{meta["lastmod"]}</lastmod>')
        xml_lines.append(f'    <changefreq>{meta["changefreq"]}</changefreq>')
        xml_lines.append(f'    <priority>{meta["priority"]}</priority>')
        xml_lines.append('  </url>')

    xml_lines.append('</urlset>')

    sitemap_content = '\n'.join(xml_lines)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print(f"Generated sitemap.xml with {len(sorted_urls)} URLs.")

def generate_robots():
    print("Generating robots.txt...")
    robots_content = f"""# Robots.txt for CraftEgon Corporate Services
# https://corporateservices.craftegon.com/

User-agent: *
Allow: /

# Sitemaps
Sitemap: {CANONICAL_DOMAIN}/sitemap.xml
"""
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots_content)
    print("Generated robots.txt successfully.")

if __name__ == '__main__':
    generate_sitemap()
    generate_robots()
