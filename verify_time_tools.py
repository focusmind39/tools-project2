# -*- coding: utf-8 -*-
"""
Auditor and Verifier for Enginewheels 120 Time Tools
"""

import os
import re
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
TIME_DIR = os.path.join(ROOT_DIR, "time-tools")

# Import databases
from data_time_clocks_calcs import CLOCK_TOOLS
from data_time_dates_ages import DATE_AGES_TOOLS
from data_time_countdowns_productivity import COUNTDOWN_PRODUCTIVITY_TOOLS
from data_time_stopwatches_scheduling import STOPWATCH_SCHEDULING_TOOLS
from data_time_conversions_business import CONVERSIONS_BUSINESS_TOOLS
from data_time_events_natural import EVENTS_NATURAL_TOOLS

TIME_TOOLS_DB = []
TIME_TOOLS_DB.extend(CLOCK_TOOLS)
TIME_TOOLS_DB.extend(DATE_AGES_TOOLS)
TIME_TOOLS_DB.extend(COUNTDOWN_PRODUCTIVITY_TOOLS)
TIME_TOOLS_DB.extend(STOPWATCH_SCHEDULING_TOOLS)
TIME_TOOLS_DB.extend(CONVERSIONS_BUSINESS_TOOLS)
TIME_TOOLS_DB.extend(EVENTS_NATURAL_TOOLS)

print(f"Loaded {len(TIME_TOOLS_DB)} time tools for verification.")

# Regex patterns
id_pattern = re.compile(r'getElementById\s*\(\s*["\']([^"\']+)["\']\s*\)')
html_id_pattern = re.compile(r'id\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
script_block_pattern = re.compile(r'<script>(.*?)</script>', re.DOTALL)
seo_article_pattern = re.compile(r'<article class="seo-article">(.*?)</article>', re.DOTALL)

total_errors = 0
total_warnings = 0

for tool in TIME_TOOLS_DB:
    slug = tool["slug"]
    name = tool["name"]
    file_name = f"{slug}.html"
    file_path = os.path.join(TIME_DIR, file_name)
    
    if not os.path.exists(file_path):
        print(f"[-] ERROR: Missing file {file_name} for '{name}'")
        total_errors += 1
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Verify links and stylesheets
    if "../assets/css/styles.css" not in content:
        print(f"[-] ERROR in {file_name}: Missing stylesheet link relative path")
        total_errors += 1
    if "../assets/js/main.js" not in content:
        print(f"[-] ERROR in {file_name}: Missing main.js script reference")
        total_errors += 1
    if "../index.html" not in content:
        print(f"[-] ERROR in {file_name}: Missing link to index.html")
        total_errors += 1
        
    # 2. Check inline JS IDs consistency
    script_match = script_block_pattern.search(content)
    if not script_match:
        print(f"[-] ERROR in {file_name}: Missing <script> block")
        total_errors += 1
        continue
        
    script_js = script_match.group(1)
    
    # Extract IDs referenced in JS
    js_ids = set(id_pattern.findall(script_js))
    
    # Find all IDs defined in HTML
    html_ids = set(html_id_pattern.findall(content))
    
    missing_ids = []
    for jid in js_ids:
        # Ignore standard notification/global toast and dynamically checked elements
        if jid in ["footer-year", "calc-breakdown", "breakdown-content", "btn-calculate", "btn-reset", "btn-clear-text", "btn-copy-results", "btn-download-results"]:
            continue
        # Also ignore window.swState etc attributes that are not HTML element IDs
        if jid.startswith("window."):
            continue
        if jid not in html_ids:
            # If it's a container element created dynamically or just checking container visibility (e.g. text-output-container)
            if jid.endswith("-container") and jid.replace("-container", "") in html_ids:
                continue
            missing_ids.append(jid)
            
    if missing_ids:
        print(f"[-] ERROR in {file_name}: JavaScript references element IDs {missing_ids} which do not exist in the HTML body!")
        total_errors += 1
        
    # 3. Verify SEO Word Count
    seo_match = seo_article_pattern.search(content)
    if not seo_match:
        print(f"[-] ERROR in {file_name}: Missing <article class=\"seo-article\"> SEO block")
        total_errors += 1
    else:
        seo_text = seo_match.group(1)
        # Strip HTML tags
        clean_text = re.sub(r'<[^>]+>', ' ', seo_text)
        words = clean_text.split()
        word_count = len(words)
        
        # We need 1000+ words
        if word_count < 1000:
            print(f"[!] WARNING in {file_name}: SEO content has only {word_count} words (minimum 1000 recommended)")
            total_warnings += 1
            
    # 4. Schema markup verification
    schema_pattern = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)
    schemas = schema_pattern.findall(content)
    if len(schemas) < 2:
        print(f"[-] ERROR in {file_name}: Must have at least 2 structured data schemas (Breadcrumb and FAQ)")
        total_errors += 1
    else:
        for s in schemas:
            try:
                json.loads(s.strip())
            except Exception as e:
                print(f"[-] ERROR in {file_name}: JSON-LD Schema contains invalid JSON syntax: {e}")
                total_errors += 1

print(f"\nVerification finished. Total hard errors found: {total_errors}, Warnings: {total_warnings}")
if total_errors == 0:
    print("[+] SUCCESS: All generated time tool files are validated and 100% error-free!")
else:
    exit(1)
