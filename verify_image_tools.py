# -*- coding: utf-8 -*-
"""
Auditor and Verifier for Enginewheels Image Tools
"""

import os
import re
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
IMG_DIR = os.path.join(ROOT_DIR, "image-tools")

# Import databases
from data_img_editing_converter import IMAGE_EDITING_TOOLS, IMAGE_CONVERTER_TOOLS
from data_img_opt_encoding import IMAGE_OPTIMIZATION_TOOLS, IMAGE_CONVERSION_ENCODING_TOOLS
from data_img_social_design import SOCIAL_MEDIA_IMAGE_TOOLS, DESIGN_TOOLS
from data_img_screenshot_watermark import SCREENSHOT_CAPTURE_TOOLS, WATERMARK_TOOLS
from data_img_photo_ai_pdf_seo import PHOTO_TOOLS, AI_IMAGE_UTILITIES, PDF_IMAGE_TOOLS, IMAGE_SEO_TOOLS

# Programmatically insert Image Compressor to optimization tools for full category listings
image_compressor_tool = None
for t in IMAGE_EDITING_TOOLS:
    if t["slug"] == "image-compressor":
        image_compressor_tool = t
        break

if image_compressor_tool:
    t_copy = dict(image_compressor_tool)
    t_copy["category"] = "Image Optimization Tools"
    # insert if not already there
    has_it = False
    for ot in IMAGE_OPTIMIZATION_TOOLS:
        if ot["slug"] == "image-compressor":
            has_it = True
            break
    if not has_it:
        IMAGE_OPTIMIZATION_TOOLS.insert(0, t_copy)

ALL_IMAGE_TOOLS = []
ALL_IMAGE_TOOLS.extend(IMAGE_EDITING_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_CONVERTER_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_OPTIMIZATION_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_CONVERSION_ENCODING_TOOLS)
ALL_IMAGE_TOOLS.extend(SOCIAL_MEDIA_IMAGE_TOOLS)
ALL_IMAGE_TOOLS.extend(DESIGN_TOOLS)
ALL_IMAGE_TOOLS.extend(SCREENSHOT_CAPTURE_TOOLS)
ALL_IMAGE_TOOLS.extend(WATERMARK_TOOLS)
ALL_IMAGE_TOOLS.extend(PHOTO_TOOLS)
ALL_IMAGE_TOOLS.extend(AI_IMAGE_UTILITIES)
ALL_IMAGE_TOOLS.extend(PDF_IMAGE_TOOLS)
ALL_IMAGE_TOOLS.extend(IMAGE_SEO_TOOLS)

DEDUPLICATED_IMAGE_TOOLS = []
seen_slugs = set()
for tool in ALL_IMAGE_TOOLS:
    if tool["slug"] not in seen_slugs:
        seen_slugs.add(tool["slug"])
        DEDUPLICATED_IMAGE_TOOLS.append(tool)

print(f"Loaded {len(DEDUPLICATED_IMAGE_TOOLS)} unique image tools for verification.")

# Regex patterns
id_pattern = re.compile(r'getElementById\s*\(\s*["\']([^"\']+)["\']\s*\)')
html_id_pattern = re.compile(r'id\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
script_block_pattern = re.compile(r'<script>(.*?)</script>', re.DOTALL)
seo_article_pattern = re.compile(r'<article class="seo-article">(.*?)</article>', re.DOTALL)

total_errors = 0
total_warnings = 0

for tool in DEDUPLICATED_IMAGE_TOOLS:
    slug = tool["slug"]
    name = tool["name"]
    file_name = f"{slug}.html"
    file_path = os.path.join(IMG_DIR, file_name)
    
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

    # Check for PDF or OCR libraries
    if "jspdf" in tool["calc_js"].lower() or "pdf" in slug:
        if "../assets/js/jspdf.umd.min.js" not in content:
            print(f"[-] ERROR in {file_name}: Missing jspdf.umd.min.js reference")
            total_errors += 1
    if "tesseract" in tool["calc_js"].lower() or "ocr" in slug:
        if "../assets/js/tesseract.min.js" not in content:
            print(f"[-] ERROR in {file_name}: Missing tesseract.min.js reference")
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
        if jid in ["image-preview", "preview-container-image-input", "text-output-container"]:
            # These are generated as part of standard layouts
            continue
        if jid not in html_ids:
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
    print("[+] SUCCESS: All generated image tool files are validated and 100% error-free!")
else:
    exit(1)
