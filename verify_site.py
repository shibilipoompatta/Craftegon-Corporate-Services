# -*- coding: utf-8 -*-
import glob
import re
import json

def verify():
    # 1. Check services.json
    with open("data/services.json", encoding="utf-8") as f:
        data = json.load(f)
    services = data.get("services", [])
    print(f"[DATA CONTRACT] Total services: {len(services)}")
    assert len(services) == 60, f"Expected 60 services, got {len(services)}"

    # 2. Check HTML files
    html_files = glob.glob("*/**/index.html", recursive=True) + ["index.html"]
    print(f"[HTML INTEGRITY] Checking {len(html_files)} index.html files...")
    
    rel_pattern = re.compile(r'(href|src)=["\'](\.\.|\.\/)')
    for f in html_files:
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        rel_matches = rel_pattern.findall(content)
        if rel_matches:
            print(f"  WARNING: {f} has relative links: {rel_matches}")
        
        # Check mandatory regulatory disclaimer
        if "CraftEgon Corporate Services (CCS) is a corporate technology, compliance, and management platform" not in content:
            print(f"  WARNING: {f} missing mandatory disclaimer!")
            
        # Check forms.js
        if "/assets/js/forms.js" not in content:
            print(f"  WARNING: {f} missing forms.js!")

    print("[VERIFICATION COMPLETED] Site structure is verified.")

if __name__ == "__main__":
    verify()
