import json
import os
import pandas as pd

# 1. Load JSON file
with open('indiafilings-services.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

services = data.get('services', data) if isinstance(data, dict) else data

# 2. Extract and format records
rows = []
os.makedirs('extracted_content', exist_ok=True)

if not isinstance(services, list):
    services = [services]

for idx, item in enumerate(services):
    if isinstance(item, dict):
        name = item.get('service_name', f'Service_{idx+1}')
        category = item.get('category', 'General')
        price = item.get('starting_price', 'N/A')
        url = item.get('url', '')
        key_pts = "\n".join(item.get('key_points', [])) if isinstance(item.get('key_points'), list) else str(item.get('key_points', ''))
        sections = "\n".join(item.get('content_sections', [])) if isinstance(item.get('content_sections'), list) else str(item.get('content_sections', ''))

        rows.append({
            'Service Name': name,
            'Category': category,
            'Starting Price': price,
            'URL': url,
            'Key Points': key_pts,
            'Content Sections': sections
        })

        # Save individual Markdown files
        clean_name = "".join(c for c in name if c.isalnum() or c in (' ', '_')).rstrip().replace(' ', '_').lower()
        if not clean_name:
            clean_name = f"service_{idx+1}"
            
        md_content = f"# {name}\n\n**Category:** {category}\n**Price:** {price}\n**URL:** {url}\n\n## Key Points\n{key_pts}\n\n## Content Sections\n{sections}\n"
        with open(f'extracted_content/{clean_name}.md', 'w', encoding='utf-8') as mf:
            mf.write(md_content)

# 3. Save CSV
df = pd.DataFrame(rows)
df.to_csv('craftegon_services_extracted.csv', index=False, encoding='utf-8-sig')
print("Successfully generated 'craftegon_services_extracted.csv' and individual Markdown files in 'extracted_content/'!")