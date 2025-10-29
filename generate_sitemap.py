#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate sitemap.xml for GitHub Pages site
"""

import os
import re
from datetime import datetime

# Base URL for GitHub Pages
BASE_URL = "https://skiltermonn-cmyk.github.io/bazy-dannykh-kompaniy-katalog/"

# Get all HTML files in the root directory
html_files = []
for file in os.listdir('.'):
    if file.endswith('.html'):
        html_files.append(file)

# Sort files alphabetically
html_files.sort()

# Start sitemap XML
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Add index.html (highest priority)
sitemap_content += '  <url>\n'
sitemap_content += f'    <loc>{BASE_URL}index.html</loc>\n'
sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
sitemap_content += '    <changefreq>weekly</changefreq>\n'
sitemap_content += '    <priority>1.0</priority>\n'
sitemap_content += '  </url>\n'

# Add KATALOG-BAZ-DANNYKH.md (high priority)
sitemap_content += '  <url>\n'
sitemap_content += f'    <loc>{BASE_URL}KATALOG-BAZ-DANNYKH.md</loc>\n'
sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
sitemap_content += '    <changefreq>weekly</changefreq>\n'
sitemap_content += '    <priority>0.9</priority>\n'
sitemap_content += '  </url>\n'

# Add all HTML files (excluding index.html)
for html_file in html_files:
    if html_file != 'index.html':
        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{BASE_URL}{html_file}</loc>\n'
        sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
        sitemap_content += '    <changefreq>monthly</changefreq>\n'
        sitemap_content += '    <priority>0.8</priority>\n'
        sitemap_content += '  </url>\n'

# Close sitemap
sitemap_content += '</urlset>\n'

# Write to sitemap.xml
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Sitemap generated successfully with {len(html_files)} HTML files!")
print(f"Total URLs in sitemap: {len(html_files) + 1}")  # +1 for KATALOG-BAZ-DANNYKH.md
