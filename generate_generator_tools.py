# -*- coding: utf-8 -*-
"""
Enginewheels Generator Tools Generator and Rebuilder
"""

import os
import json
import re

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
GEN_DIR = os.path.join(ROOT_DIR, "generator-tools")
os.makedirs(GEN_DIR, exist_ok=True)

# Import calculators
from data_finance_health import FINANCE_CALCS, HEALTH_CALCS
from data_edu_biz_const import EDU_CALCS, BUSINESS_CALCS, CONST_CALCS
from data_travel_math import TRAVEL_CALCS, MATH_CALCS
from data_time_seo_life import TIME_CALCS, SEO_CALCS, LIFE_CALCS

ALL_CALCULATORS = []
ALL_CALCULATORS.extend(FINANCE_CALCS)
ALL_CALCULATORS.extend(HEALTH_CALCS)
ALL_CALCULATORS.extend(EDU_CALCS)
ALL_CALCULATORS.extend(BUSINESS_CALCS)
ALL_CALCULATORS.extend(CONST_CALCS)
ALL_CALCULATORS.extend(TRAVEL_CALCS)
ALL_CALCULATORS.extend(MATH_CALCS)
ALL_CALCULATORS.extend(TIME_CALCS)
ALL_CALCULATORS.extend(SEO_CALCS)
ALL_CALCULATORS.extend(LIFE_CALCS)

# Import text tools
from data_text_basic_case import BASIC_TEXT_CALCS, CASE_CONVERTER_CALCS
from data_text_format_replace import FORMATTER_CALCS, REPLACE_CALCS
from data_text_seo_writing import SEO_TEXT_CALCS, WRITING_CALCS
from data_text_social_dev import SOCIAL_CALCS, DEVELOPER_CALCS
from data_text_conv_url import CONVERTER_CALCS, URL_CALCS
from data_text_rand_adv_ai import RANDOM_CALCS, ADVANCED_CALCS, AI_CALCS

ALL_TEXT_TOOLS = []
ALL_TEXT_TOOLS.extend(BASIC_TEXT_CALCS)
ALL_TEXT_TOOLS.extend(CASE_CONVERTER_CALCS)
ALL_TEXT_TOOLS.extend(FORMATTER_CALCS)
ALL_TEXT_TOOLS.extend(REPLACE_CALCS)
ALL_TEXT_TOOLS.extend(SEO_TEXT_CALCS)
ALL_TEXT_TOOLS.extend(WRITING_CALCS)
ALL_TEXT_TOOLS.extend(SOCIAL_CALCS)
ALL_TEXT_TOOLS.extend(DEVELOPER_CALCS)
ALL_TEXT_TOOLS.extend(CONVERTER_CALCS)
ALL_TEXT_TOOLS.extend(URL_CALCS)
ALL_TEXT_TOOLS.extend(RANDOM_CALCS)
ALL_TEXT_TOOLS.extend(ADVANCED_CALCS)
ALL_TEXT_TOOLS.extend(AI_CALCS)

# Import security tools
from data_sec_password_hash import PASSWORD_TOOLS, HASH_GENERATOR_TOOLS
from data_sec_encoding_token import ENCODING_DECODING_TOOLS, TOKEN_KEY_GENERATOR_TOOLS
from data_sec_encrypt_analysis import ENCRYPTION_TOOLS, SECURITY_ANALYSIS_TOOLS
from data_sec_network_web import NETWORK_SECURITY_TOOLS, WEB_SECURITY_TOOLS
from data_sec_dev_privacy_crypto import DEVELOPER_SECURITY_TOOLS, PRIVACY_TOOLS, CRYPTOGRAPHY_TOOLS

ALL_SECURITY_TOOLS = []
ALL_SECURITY_TOOLS.extend(PASSWORD_TOOLS)
ALL_SECURITY_TOOLS.extend(HASH_GENERATOR_TOOLS)
ALL_SECURITY_TOOLS.extend(ENCODING_DECODING_TOOLS)
ALL_SECURITY_TOOLS.extend(TOKEN_KEY_GENERATOR_TOOLS)
ALL_SECURITY_TOOLS.extend(ENCRYPTION_TOOLS)
ALL_SECURITY_TOOLS.extend(SECURITY_ANALYSIS_TOOLS)
ALL_SECURITY_TOOLS.extend(NETWORK_SECURITY_TOOLS)
ALL_SECURITY_TOOLS.extend(WEB_SECURITY_TOOLS)
ALL_SECURITY_TOOLS.extend(DEVELOPER_SECURITY_TOOLS)
ALL_SECURITY_TOOLS.extend(PRIVACY_TOOLS)
ALL_SECURITY_TOOLS.extend(CRYPTOGRAPHY_TOOLS)

DEDUPLICATED_SECURITY_TOOLS = []
seen_sec_slugs = set()
for tool in ALL_SECURITY_TOOLS:
    if tool["slug"] not in seen_sec_slugs:
        seen_sec_slugs.add(tool["slug"])
        DEDUPLICATED_SECURITY_TOOLS.append(tool)

# Import image tools
from data_img_editing_converter import IMAGE_EDITING_TOOLS, IMAGE_CONVERTER_TOOLS
from data_img_opt_encoding import IMAGE_OPTIMIZATION_TOOLS, IMAGE_CONVERSION_ENCODING_TOOLS
from data_img_social_design import SOCIAL_MEDIA_IMAGE_TOOLS, DESIGN_TOOLS
from data_img_screenshot_watermark import SCREENSHOT_CAPTURE_TOOLS, WATERMARK_TOOLS
from data_img_photo_ai_pdf_seo import PHOTO_TOOLS, AI_IMAGE_UTILITIES, PDF_IMAGE_TOOLS, IMAGE_SEO_TOOLS

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
seen_img_slugs = set()
for tool in ALL_IMAGE_TOOLS:
    if tool["slug"] not in seen_img_slugs:
        seen_img_slugs.add(tool["slug"])
        DEDUPLICATED_IMAGE_TOOLS.append(tool)

# Import time tools
from data_time_clocks_calcs import CLOCK_TOOLS
from data_time_dates_ages import DATE_AGES_TOOLS
from data_time_countdowns_productivity import COUNTDOWN_PRODUCTIVITY_TOOLS
from data_time_stopwatches_scheduling import STOPWATCH_SCHEDULING_TOOLS
from data_time_conversions_business import CONVERSIONS_BUSINESS_TOOLS
from data_time_events_natural import EVENTS_NATURAL_TOOLS

ALL_TIME_TOOLS = []
ALL_TIME_TOOLS.extend(CLOCK_TOOLS)
ALL_TIME_TOOLS.extend(DATE_AGES_TOOLS)
ALL_TIME_TOOLS.extend(COUNTDOWN_PRODUCTIVITY_TOOLS)
ALL_TIME_TOOLS.extend(STOPWATCH_SCHEDULING_TOOLS)
ALL_TIME_TOOLS.extend(CONVERSIONS_BUSINESS_TOOLS)
ALL_TIME_TOOLS.extend(EVENTS_NATURAL_TOOLS)

DEDUPLICATED_TIME_TOOLS = []
seen_time_slugs = set()
for tool in ALL_TIME_TOOLS:
    if tool["slug"] not in seen_time_slugs:
        seen_time_slugs.add(tool["slug"])
        DEDUPLICATED_TIME_TOOLS.append(tool)

# Import developer tools
from data_dev_formatters import FORMATTER_TOOLS
from data_dev_converters import CONVERTER_TOOLS
from data_dev_web_dev import WEB_DEV_TOOLS
from data_dev_api_data import API_DATA_TOOLS
from data_dev_text_encoding import TEXT_ENCODING_TOOLS
from data_dev_regex_validation import REGEX_VALIDATION_TOOLS
from data_dev_database import DATABASE_TOOLS
from data_dev_date_time import DATE_TIME_TOOLS
from data_dev_network_internet import NETWORK_INTERNET_TOOLS
from data_dev_color_design import COLOR_DESIGN_TOOLS
from data_dev_productivity import PRODUCTIVITY_TOOLS
from data_dev_seo_webmaster import SEO_WEBMASTER_TOOLS

ALL_DEV_TOOLS = []
ALL_DEV_TOOLS.extend(FORMATTER_TOOLS)
ALL_DEV_TOOLS.extend(CONVERTER_TOOLS)
ALL_DEV_TOOLS.extend(WEB_DEV_TOOLS)
ALL_DEV_TOOLS.extend(API_DATA_TOOLS)
ALL_DEV_TOOLS.extend(TEXT_ENCODING_TOOLS)
ALL_DEV_TOOLS.extend(REGEX_VALIDATION_TOOLS)
ALL_DEV_TOOLS.extend(DATABASE_TOOLS)
ALL_DEV_TOOLS.extend(DATE_TIME_TOOLS)
ALL_DEV_TOOLS.extend(NETWORK_INTERNET_TOOLS)
ALL_DEV_TOOLS.extend(COLOR_DESIGN_TOOLS)
ALL_DEV_TOOLS.extend(PRODUCTIVITY_TOOLS)
ALL_DEV_TOOLS.extend(SEO_WEBMASTER_TOOLS)

DEDUPLICATED_DEV_TOOLS = []
seen_dev_slugs = set()
for tool in ALL_DEV_TOOLS:
    if tool["slug"] not in seen_dev_slugs:
        seen_dev_slugs.add(tool["slug"])
        DEDUPLICATED_DEV_TOOLS.append(tool)

# Import new generator tools
from data_gen_text_names import TEXT_GENERATORS
from data_gen_security_content import SECURITY_GENERATORS
from data_gen_seo_social import SEO_GENERATORS
from data_gen_business_design import BUSINESS_GENERATORS
from data_gen_random_fun import RANDOM_GENERATORS
from data_gen_dev_ai import DEV_GENERATORS

ALL_GENERATORS = []
ALL_GENERATORS.extend(TEXT_GENERATORS)
ALL_GENERATORS.extend(SECURITY_GENERATORS)
ALL_GENERATORS.extend(SEO_GENERATORS)
ALL_GENERATORS.extend(BUSINESS_GENERATORS)
ALL_GENERATORS.extend(RANDOM_GENERATORS)
ALL_GENERATORS.extend(DEV_GENERATORS)

DEDUPLICATED_GENERATOR_TOOLS = []
seen_gen_slugs = set()
for tool in ALL_GENERATORS:
    if tool["slug"] not in seen_gen_slugs:
        seen_gen_slugs.add(tool["slug"])
        DEDUPLICATED_GENERATOR_TOOLS.append(tool)

print(f"Loaded {len(DEDUPLICATED_GENERATOR_TOOLS)} unique generator tools.")

# SEO Copy Generator
def generate_seo_text(tool):
    name = tool["name"]
    category = tool["category"]
    desc = tool["desc"]
    formula = tool["formula"]
    formula_desc = tool["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art online utility designed to provide immediate, high-precision results for your content creation, web development, and branding workflows. In the modern digital landscape, generating unique brand names, secure passwords, click-worthy headlines, and structured code assets is critical for saving time and improving focus. Whether you are generating classic filler text, crafting optimized sitemaps, building styled CSS gradients, or designing random identifiers, this generator offers a safe, ad-free, and easy-to-use interface. Under the hood, this utility operates with client-side JavaScript calculations, ensuring that your inputs, variables, and outputs remain entirely secure and local to your web browser session.</p>
      <p>Manual compilation of branding structures, API response models, and security keys is a tedious and error-prone process. Our tool automates these tasks. By providing an interactive control panel with defaults, you can generate fresh, customizable variants with a single click. It serves as an essential helper for copywriters, social media managers, SEO experts, and web developers who want to produce mock layouts, security credentials, or visual assets instantly without installing external scripts or software.</p>
      <p>A core foundation of our online generators is absolute data privacy. Many platforms upload your private seeds, company name concepts, or text inputs to backend servers, saving logs that could expose your ideas or credentials. The Enginewheels **{name}** runs completely client-side in the browser. No data ever traverses the network or gets logged to external systems. Once you close your active browser tab, your parameters are completely cleared from memory, guaranteeing absolute confidentiality.</p>
      <p>Using this tool is free and requires no registration. It is optimized to load fast, meeting the highest standards of modern web performance. The visual layout scales fluidly on mobile screens, tablets, and desktop computers, so you can execute dev checks wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** uses client-side algorithms to parse your choices and assemble matching results instantly. First, the tool collects your input from the main text areas, numeric fields, or selection drop-downs. Once you click "Generate", the utility runs validation checks to make sure the inputs are not empty and conform to expected patterns. If any parameters are missing, the tool type alerts you immediately via the toast notification system.</p>
      <p>After validation, the core algorithm is applied: ` {formula} `. {formula_desc} The engine processes the syntax, maps characters, or computes values. The resulting output is written to the read-only output box. For instance, formatted code is displayed inside monospace inputs, values are aligned, and validation reports are structured for easy reading. Trailing spaces are trimmed to present the values cleanly.</p>
      <p>Understanding the processing steps is critical for debugging. That is why our tool displays a detailed step-by-step breakdown below the interface. The breakdown shows exactly how the final values were calculated, letting you audit the rules. It acts as an educational resource, helping you understand parsers, formatting schemas, or routing rules.</p>
      <p>Finally, if you want to copy the results for codes, configuration files, or scripts, simply click the "Copy Output" button to save it directly to your clipboard. You can also click the "Download Output" button to save the result as a text file (.txt). To start a new task, click "Clear Fields" to reset the text area and start fresh, or click "Reset" to return all configuration inputs to their default values.</p>
    """

    features = f"""
      <h2>Key Features of the {name}</h2>
      <ul>
        <li><strong>Instant Results:</strong> Processes inputs instantly with reliable client-side algorithms.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your data is processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>One-Click Actions:</strong> Copy outputs to clipboard or download results as .txt files.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Instant:</strong> No registration, sign-ups, or limitations. Clear inputs with a single click.</li>
      </ul>
    """

    benefits = f"""
      <h2>Benefits of Using Online Generators</h2>
      <p>Manually scripting, calculating, or verifying development parameters takes significant time and leads to key or coding errors. A frontend designer matching colors, a backend developer formatting databases, or an administrator checking SEO rules can save hours using our tool. The {name} automates these steps, ensuring consistent and professional formatting.</p>
      <p>Our tool helps you maintain key formatting consistency. By applying uniform rules to scripts, layouts, and structures, it ensures that your work is professional and ready for implementation. Additionally, the responsive design allows you to perform these operations from any device, whether you are on a desktop at the office or on a mobile phone on the go.</p>
      <p>Unlike other web utilities that subject users to heavy ads, forced registrations, or paid plans, our tools are 100% free with no limits. This allows you to process as many parameters as you need, whenever you need them, without interruption.</p>
    """

    developer_tips = f"""
      <h2>Developer Tips & Best Practices</h2>
      <p>When working with JSON or XML data payloads, always ensure that key-value pairs are properly closed and commas are not misplaced. For security parameters, keep private keys and tokens out of version control repositories. Lastly, local client-side tools protect data in transit, but you must still secure your device from external malware or unauthorized extensions.</p>
    """

    use_cases = f"""
      <h2>Real-World Use Cases</h2>
      <ul>
        <li><strong>Branding Teams:</strong> Quickly generate startup name ideas, company slogan concepts, and aesthetic domain names.</li>
        <li><strong>Content Creators:</strong> Generate viral titles, caption tag structures, and attention hooks for videos and blogs.</li>
        <li><strong>Developers & Designers:</strong> Generate secure API keys, symmetric encryption keys, box-shadows, and favicons.</li>
      </ul>
    """

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Generator Needs?</h2>
      <p>When it comes to performing coding operations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each tool loads instantly and runs with absolute speed. We prioritize user privacy above everything else; unlike typical online utilities that process data on remote servers, all your parameters are processed locally in your browser. This client-side approach ensures your sensitive input parameters and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to copy mathematical results for a report or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity.</p>
    """

    faqs = [
        {
            "q": f"Is there a character or size limit when using the {name}?",
            "a": f"No. All processing occurs locally in your browser using client-side JavaScript. This means you can parse large strings, schemas, or config files without timing out."
        },
        {
            "q": f"Does Enginewheels save my private keys or input data?",
            "a": f"No. All operations are processed locally in active memory. We do not upload your text to external servers, guaranteeing complete privacy."
        },
        {
            "q": f"How do I download the generated output?",
            "a": f"Simply click the 'Download Output' button to download your processed code or text as a standard .txt file."
        },
        {
            "q": f"Does the tool support mobile devices?",
            "a": f"Yes. Our website is fully responsive, and all tools scale fluidly on touch screens, smartphones, and tablets."
        },
        {
            "q": f"Can I copy the results of my calculations?",
            "a": f"Yes, simply click the 'Copy Output' button to save a formatted summary of all inputs and outputs to your clipboard."
        }
    ]

    faq_html = f"""
      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion" style="margin-top: 20px;">
    """
    for faq in faqs:
        faq_html += f"""
        <details class="faq-item">
          <summary>{faq["q"]}</summary>
          <div class="faq-content">
            {faq["a"]}
          </div>
        </details>
        """
    faq_html += "</div>"

    seo_article_html = f"""
      {intro}
      {how_it_works}
      {features}
      {benefits}
      {developer_tips}
      {use_cases}
      {why_choose_us}
      {faq_html}
    """
    return seo_article_html, faqs

# Generate all individual HTML files
for index, tool in enumerate(DEDUPLICATED_GENERATOR_TOOLS):
    name = tool["name"]
    slug = tool["slug"]
    category = tool["category"]
    desc = tool["desc"]
    
    # Generate SEO article content and FAQ schema
    seo_article_html, faqs = generate_seo_text(tool)
    
    faq_schema_items = []
    for faq in faqs:
        faq_schema_items.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })
    faq_schema_str = json.dumps(faq_schema_items, indent=2)
    
    # Build inputs HTML
    inputs_html = ""
    for inp in tool["inputs"]:
        label = inp["label"]
        iid = inp["id"]
        itype = inp["type"]
        
        inputs_html += f"""
        <div class="form-group" style="margin-bottom:20px; text-align:left;">
          <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
        """
        if itype == "select":
            inputs_html += f'  <select id="{iid}" class="form-control" style="width:100%;">'
            for opt_val, opt_lbl in inp["options"]:
                inputs_html += f'    <option value="{opt_val}">{opt_lbl}</option>'
            inputs_html += '  </select>'
        elif itype == "date":
            inputs_html += f'  <input type="date" id="{iid}" class="form-control" style="width:100%;">'
        elif itype == "textarea":
            default_val = inp.get("default", "")
            inputs_html += f'  <textarea id="{iid}" class="form-control" style="width:100%; height:120px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px; resize:vertical;">{default_val}</textarea>'
        elif itype == "number":
            default_val = inp.get("default", "0")
            imin = inp.get("min", "0")
            imax = inp.get("max", "100000000")
            istep = inp.get("step", "1")
            inputs_html += f'  <input type="number" id="{iid}" class="form-control" style="width:100%;" value="{default_val}" min="{imin}" max="{imax}" step="{istep}">'
        else: # text
            default_val = inp.get("default", "")
            inputs_html += f'  <input type="text" id="{iid}" class="form-control" style="width:100%;" value="{default_val}">'
            
        inputs_html += "</div>"
        
    # Build outputs HTML
    outputs_html = ""
    for out in tool["outputs"]:
        olabel = out["label"]
        oid = out["id"]
        otype = out.get("type", "text")
        oprefix = out.get("prefix", "")
        osuffix = out.get("suffix", "")
        
        if otype == "textarea":
            outputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{oid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{olabel}</label>
              <textarea id="{oid}" class="form-control" style="width:100%; height:200px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px; resize:vertical;" readonly placeholder="Results will appear here..."></textarea>
            </div>
            """
        else:
            outputs_html += f"""
            <div class="result-box" style="background:rgba(255,255,255,0.03); padding:16px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); text-align:center;">
              <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:4px;">{olabel}</div>
              <div style="font-size:1.5rem; font-weight:700; color:var(--color-red);">{oprefix}<span id="{oid}">-</span>{osuffix}</div>
            </div>
            """
        
    # Build dynamic JS bindings
    reset_lines = []
    clear_lines = []
    
    for inp in tool["inputs"]:
        if inp["type"] == "select":
            reset_lines.append(f"document.getElementById('{inp['id']}').selectedIndex = 0;")
        elif inp["type"] == "date":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "textarea":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = `{inp.get('default', '')}`;")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "number":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '0')}';")
        else:
            reset_lines.append(f"document.getElementById('{inp['id']}').value = `{inp.get('default', '')}`;")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
            
    for out in tool["outputs"]:
        otype = out.get("type", "text")
        if otype == "textarea":
            reset_lines.append(f"document.getElementById('{out['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{out['id']}').value = '';")
        else:
            reset_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")
            clear_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")
        
    reset_js = "\n        ".join(reset_lines)
    clear_outputs_js = "\n        ".join(clear_lines)

    has_text_output = any(out["id"] == "text-output" for out in tool["outputs"])
    if has_text_output:
        copy_js_logic = """const val = document.getElementById('text-output').value || document.getElementById('text-output').textContent;"""
    else:
        copy_lines = []
        for out in tool["outputs"]:
            copy_lines.append(f"val += ' - {out['label']}: ' + (document.getElementById('{out['id']}').textContent || '-') + '\\n';")
        copy_lines_str = "\n        ".join(copy_lines)
        copy_js_logic = f"""let val = "{name} Results:\\n";\n        {copy_lines_str}"""
        
    # Generate related tools grid
    related_list = []
    for other in DEDUPLICATED_GENERATOR_TOOLS:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    if len(related_list) < 2:
        for other in DEDUPLICATED_GENERATOR_TOOLS:
            if other["slug"] != slug and other not in related_list:
                related_list.append(other)
                if len(related_list) == 2:
                    break
                    
    related_tools_html = ""
    for rel in related_list:
        related_tools_html += f"""
          <a href="{rel['slug']}.html" class="tool-card">
            <div class="tool-card-header">
              <div class="tool-card-icon">{rel['icon']}</div>
              <h3 class="tool-card-title">{rel['name']}</h3>
            </div>
            <p class="tool-card-desc">{rel['desc']}</p>
            <div class="tool-card-link">Open Tool &gt;</div>
          </a>
        """
        
    # Render final page from template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>{name} Online Free | Generate Instant Results - Enginewheels</title>
  <meta name="description" content="{desc} Safe, responsive, and secure client-side browser-based utility tool.">
  <link rel="canonical" href="https://enginewheels.com/generator-tools/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/generator-tools/{slug}.html">
  <meta property="og:title" content="{name} Online Free | Generate Instant Results - Enginewheels">
  <meta property="og:description" content="{desc} Safe, responsive, and secure client-side browser-based utility tool.">
  
  <!-- CSS Link -->
  <link rel="stylesheet" href="../assets/css/styles.css">
  
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://enginewheels.com/index.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Generator Tools",
        "item": "https://enginewheels.com/category/generators.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/generator-tools/{slug}.html"
      }}
    ]
  }}
  </script>
  
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": {faq_schema_str}
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-container">
      <a href="../index.html" class="logo">
        <span class="logo-icon"><span class="logo-icon-inner"></span></span>
        Enginewheels
      </a>
      
      <nav class="nav-menu">
        <a href="../index.html" class="nav-link">Home</a>
        <div class="categories-nav">
          <a href="#" class="nav-link active">Categories <span style="font-size:0.7rem">▼</span></a>
          <div class="categories-dropdown">
            <a href="../category/text-tools.html">✍ Text Tools</a>
            <a href="../category/security-tools.html">🔒 Security Tools</a>
            <a href="../category/developer-tools.html">💻 Developer Tools</a>
            <a href="../category/image-tools.html">🖼️ Image Tools</a>
            <a href="../category/generators.html">⚙️ Generators</a>
            <a href="../category/calculators.html">🧮 Calculators</a>
            <a href="../category/time-tools.html">🕒 Time Tools</a>
            <a href="../category/math-numbers.html">🔢 Math & Numbers</a>
            <a href="../category/fun-utility.html">🎯 Fun & Utility</a>
            <a href="../category/seo-web-tools.html">🌐 SEO & Web Tools</a>
          </div>
        </div>
        <a href="../index.html#popular" class="nav-link">Popular Tools</a>
        <a href="../about.html" class="nav-link">About Us</a>
        <a href="../contact.html" class="nav-link">Contact Us</a>
        <a href="../privacy.html" class="nav-link">Privacy Policy</a>
      </nav>
      
      <div class="burger-menu">
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
      </div>
    </div>
  </header>

  <!-- Main Calculator Layout -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../category/generators.html">Generators</a> &gt; <span>{name}</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">{name}</h1>
      <p class="tool-desc-lead">{desc}</p>
    </div>

    <!-- Calculator Section -->
    <section class="calculator-card glass-panel">
      <div class="calc-grid">
        <!-- Inputs Column -->
        <div class="calc-inputs">
          <div style="font-size: 1.1rem; font-weight: 600; color: #fff; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">Configure Inputs</div>
          {inputs_html}
          <div style="display: flex; gap: 12px; margin-top: 30px;">
            <button id="btn-calculate" class="btn btn-primary" style="flex: 2; padding: 12px;">Generate</button>
            <button id="btn-reset" class="btn btn-secondary" style="flex: 1; padding: 12px;">Reset</button>
          </div>
        </div>

        <!-- Outputs Column -->
        <div class="calc-outputs" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="font-size: 1.1rem; font-weight: 600; color: #fff; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">Generated Output</div>
            <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
              {outputs_html}
            </div>
          </div>
          <div style="display: flex; gap: 12px; margin-top: 30px;">
            <button id="btn-copy-results" class="btn btn-primary" style="flex: 1; background: var(--color-red); border-color: var(--color-red); padding: 12px;">Copy Output</button>
            <button id="btn-clear-text" class="btn btn-secondary" style="flex: 1; padding: 12px;">Clear Fields</button>
          </div>
        </div>
      </div>

      <!-- Action Step breakdown log -->
      <div id="calc-breakdown" class="calc-breakdown" style="display: none; margin-top: 30px; padding: 20px; border-top: 1px solid rgba(255,255,255,0.05); background: rgba(0,0,0,0.1); border-radius: 8px;">
        <div style="font-weight: 600; color: #fff; margin-bottom: 10px;">Step-by-Step Breakdown</div>
        <div id="breakdown-content" style="font-size: 0.9rem; line-height: 1.6; color: var(--text-muted);"></div>
      </div>
    </section>

    <!-- Popular Tools Grid in Sidebar or Bottom -->
    <section class="related-tools-section" style="margin-top: 60px;">
      <h2 style="font-size: 1.4rem; color: #fff; margin-bottom: 24px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">Related Generators</h2>
      <div class="tool-grid">
        {related_tools_html}
      </div>
    </section>

    <!-- Technical SEO Article -->
    <article class="seo-article">
      {seo_article_html}
    </article>
  </main>

  <!-- Footer Section -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Col 1 -->
      <div>
        <a href="../index.html" class="logo">
          <span class="logo-icon"><span class="logo-icon-inner"></span></span>
          Enginewheels
        </a>
        <p class="footer-col-desc">A premium ecosystem of free, fast, and privacy-oriented online tools. Process your files, text, hashes, and configurations safely in your browser.</p>
        <div class="social-links">
          <a href="#" class="social-icon" aria-label="Facebook">FB</a>
          <a href="#" class="social-icon" aria-label="Instagram">IG</a>
          <a href="#" class="social-icon" aria-label="Twitter">X</a>
          <a href="#" class="social-icon" aria-label="LinkedIn">LN</a>
          <a href="#" class="social-icon" aria-label="YouTube">YT</a>
        </div>
      </div>
      
      <!-- Col 2 -->
      <div>
        <h3 class="footer-title">Quick Links</h3>
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About Us</a>
          <a href="../contact.html">Contact Us</a>
          <a href="../sitemap.html">Sitemap</a>
        </div>
      </div>
      
      <!-- Col 3 -->
      <div>
        <h3 class="footer-title">Legal Links</h3>
        <div class="footer-links">
          <a href="../privacy.html">Privacy Policy</a>
          <a href="../disclaimer.html">Disclaimer</a>
          <a href="../terms.html">Terms & Conditions</a>
        </div>
      </div>
      
      <!-- Col 4 -->
      <div>
        <h3 class="footer-title">Popular Tools</h3>
        <div class="footer-links">
          <a href="../tools/word-counter.html">Word Counter</a>
          <a href="../tools/json-formatter.html">JSON Formatter</a>
          <a href="../tools/password-generator.html">Password Generator</a>
          <a href="../tools/qr-code-generator.html">QR Code Generator</a>
          <a href="../tools/age-calculator.html">Age Calculator</a>
        </div>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <div class="footer-copy">&copy; <span id="footer-year"></span> Enginewheels. All rights reserved. Built with privacy.</div>
      <div class="footer-bottom-links">
        <a href="../privacy.html">Privacy</a>
        <a href="../terms.html">Terms</a>
        <a href="../disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </footer>

  <script src="../assets/js/main.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {{
      // Update Breakdown helper
      function updateBreakdown(htmlContent) {{
        const breakdown = document.getElementById('calc-breakdown');
        const content = document.getElementById('breakdown-content');
        if (breakdown && content) {{
          content.innerHTML = htmlContent;
          breakdown.style.display = 'block';
        }}
      }}

      // Calculate Click
      document.getElementById('btn-calculate').addEventListener('click', () => {{
        {tool["calc_js"]}
      }});

      // Reset Click
      document.getElementById('btn-reset').addEventListener('click', () => {{
        {reset_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Inputs reset to defaults.");
      }});

      // Clear Fields Click
      document.getElementById('btn-clear-text').addEventListener('click', () => {{
        {clear_outputs_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Inputs and outputs cleared.");
      }});

      // Copy Results Click
      document.getElementById('btn-copy-results').addEventListener('click', () => {{
        {copy_js_logic}
        if (!val || val === '-') {{
          showToast("No generated results to copy!", "error");
          return;
        }}
        navigator.clipboard.writeText(val).then(() => {{
          showToast("Copied results to clipboard!");
        }}).catch(err => {{
          showToast("Failed to copy: " + err, "error");
        }});
      }});
      
      // Load current year in footer
      const yearSpan = document.getElementById('footer-year');
      if (yearSpan) {{
        yearSpan.textContent = new Date().getFullYear();
      }}
    }});
  </script>
</body>
</html>
"""
    
    # Save the file
    tool_page_path = os.path.join(GEN_DIR, f"{slug}.html")
    with open(tool_page_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(DEDUPLICATED_GENERATOR_TOOLS)} HTML tool files successfully.")

# ----------------- REWRITE CATEGORY/GENERATORS.HTML -----------------
print("Rewriting category/generators.html...")

subcategories = {
    "Text Generators": TEXT_GENERATORS,
    "Username & Name Generators": SECURITY_GENERATORS,  # Note: mapping is logical
    "Password & Security Generators": SEO_GENERATORS,
    "Content Creator Generators": BUSINESS_GENERATORS,
    "SEO Generators": RANDOM_GENERATORS,
    "Social Media Generators": DEV_GENERATORS,
    "Email & Business Generators": BUSINESS_GENERATORS,
    "Design Generators": BUSINESS_GENERATORS,
    "Random Generators": RANDOM_GENERATORS,
    "Fun & Entertainment Generators": RANDOM_GENERATORS,
    "Developer Generators": DEV_GENERATORS,
    "AI & Productivity Generators": DEV_GENERATORS
}

# Mapping exact tools to categories
subcategories = {
    "Text Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Text Generators"],
    "Username & Name Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Username & Name Generators"],
    "Password & Security Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Password & Security Generators"],
    "Content Creator Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Content Creator Generators"],
    "SEO Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "SEO Generators"],
    "Social Media Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Social Media Generators"],
    "Email & Business Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Email & Business Generators"],
    "Design Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Design Generators"],
    "Random Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Random Generators"],
    "Fun & Entertainment Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Fun & Entertainment Generators"],
    "Developer Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "Developer Generators"],
    "AI & Productivity Generators": [t for t in DEDUPLICATED_GENERATOR_TOOLS if t["category"] == "AI & Productivity Generators"]
}

grids_html = ""
for subcat, tools_list in subcategories.items():
    grids_html += f"""
    <div class="category-section" style="margin-bottom:50px;">
      <h2 style="font-size:1.6rem; border-bottom:2px solid #7C3AED; padding-bottom:8px; margin-bottom:24px; color:#fff;">{subcat}</h2>
      <div class="tool-grid">
    """
    cat_seen = set()
    for t in tools_list:
        if t["slug"] in cat_seen:
            continue
        cat_seen.add(t["slug"])
        grids_html += f"""
          <a href="../generator-tools/{t['slug'].replace('-tool', '')}.html" class="tool-card">
            <div class="tool-card-header">
              <div class="tool-card-icon">{t['icon']}</div>
              <h3 class="tool-card-title">{t['name']}</h3>
            </div>
            <p class="tool-card-desc">{t['desc']}</p>
            <div class="tool-card-link">Open Tool &gt;</div>
          </a>
        """
    # Quick fallback if category has no tools
    if not tools_list:
        grids_html += """<div style='color:var(--text-muted); padding:10px;'>Coming Soon</div>"""
    grids_html += """
      </div>
    </div>
    """

# 3500+ words SEO Text targeting Generator Tools
category_seo_text_path = os.path.join(ROOT_DIR, "category_seo_text.txt")
if os.path.exists(category_seo_text_path):
    with open(category_seo_text_path, "r", encoding="utf-8") as f:
        category_seo_text = f.read()
else:
    category_seo_text = """
    <h2>Complete Guide to Generator Tools & Online Productivity Utilities</h2>
    <p>In modern digital operations, the demand for fast, automated, and secure text generation, credential creation, and styling layout generation is at an all-time high. Generator tools serve as essential instruments that optimize this workload. From lorem ipsum layout text block synthesis and secure password key configurations to SEO meta tag descriptions and dynamic colored avatar vector codes, these online tools handle complex configurations. This ensures designers, copywriters, social media managers, and developers can focus on core project goals instead of formatting details.</p>
    
    <h3>Text and Placeholder Mock Generators</h3>
    <p>A crucial step in designing websites, flyers, and applications is laying out visual grids before copy is finalized. Text generators automate the creation of placeholder layouts. A Lorem Ipsum generator compiles paragraphs or words matching custom counts based on Latin dictionaries. Similarly, a Dummy Text Generator creates readable scrambled English, pangrams, or gibberish character rows. These placeholder texts preserve natural sentence lengths without distracting clients with readable paragraphs during design reviews.</p>
    
    <h3>Name & Branding Idea Generators</h3>
    <p>Establishing a brand starts with finding a memorable and available name. Naming generators use cross-industry compound databases to suggest concepts. A Business Name Generator blends core keywords with startup prefixes (Smart, Omni, Apex) and suffixes (Grid, Base). Similarly, a Brand Name Generator applies phonetic vowel-consonant blending to suggest short, trademarkable abstract names. Domain name generators append standard extension suffixes (.com, .net, .org, .io) and check length requirements, allowing entrepreneurs to register domains without wasting time on exhausted queries.</p>
    
    <h3>Password & Cryptographic Security Key Generators</h3>
    <p>Web security relies on high-entropy passwords, session IDs, and signing keys. Manual typing is predictable and prone to guessable patterns. Security generators resolve this problem. A Password Generator uses random pools of mixed uppercase, lowercase, numbers, and symbols to compile credentials. A Secure Password Generator takes this further by employing the browser-native Web Crypto API to ensure cryptographically secure, high-entropy outputs. Additional token and key generators synthesize version 4 UUIDs, standard API key secret tokens, and 256-bit AES symmetric keys for secure cookie and JWT payload signatures.</p>
    
    <h3>Content Creation and Social Media Optimizers</h3>
    <p>Marketers and digital content creators require consistent copy to boost reach. Social media generators draft posts that capture attention. YouTube Title Generators combine keywords with viral, curiosity-inducing patterns to boost click-through rates (CTR). Social Media Caption Generators format posts with clean paragraph spacing, hashtags, and emojis tailored for platforms like Instagram, LinkedIn, and Twitter/X. Hashtag generators extend reach by matching seed terms with high-ranking tag suffixes.</p>
    
    <h3>Local Client-Side Operations for Complete Privacy</h3>
    <p>Data privacy is critical when generating sensitive credentials like passphrases, API secret keys, or business ideas. Pasting these seeds into typical online generators poses significant risks if the tools transmit inputs to remote servers. At Enginewheels, all calculations are executed entirely inside your active browser session using client-side JavaScript. Inputs, seeds, and final values are processed locally, never traversing the network or saving to databases. Once you close your active browser tab, all variables are cleared from memory, securing your data from third-party logs.</p>
"""

category_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Generator Tools Online Free | Brand Name & Password Generators - Enginewheels</title>
  <meta name="description" content="Explore our free Generator Tools category. Generate business names, secure passwords, click-worthy titles, CSS gradients, and random numbers locally in your browser.">
  <link rel="canonical" href="https://enginewheels.com/category/generators.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/generators.html">
  <meta property="og:title" content="Generator Tools Online Free | Brand Name & Password Generators - Enginewheels">
  <meta property="og:description" content="Explore our free Generator Tools category. Generate business names, secure passwords, click-worthy titles, CSS gradients, and random numbers locally in your browser.">
  
  <!-- CSS Link -->
  <link rel="stylesheet" href="../assets/css/styles.css">
  
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://enginewheels.com/index.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Generators",
        "item": "https://enginewheels.com/category/generators.html"
      }}
    ]
  }}
  </script>
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-container">
      <a href="../index.html" class="logo">
        <span class="logo-icon"><span class="logo-icon-inner"></span></span>
        Enginewheels
      </a>
      
      <nav class="nav-menu">
        <a href="../index.html" class="nav-link">Home</a>
        <div class="categories-nav">
          <a href="#" class="nav-link active">Categories <span style="font-size:0.7rem">▼</span></a>
          <div class="categories-dropdown">
            <a href="text-tools.html">✍ Text Tools</a>
            <a href="security-tools.html">🔒 Security Tools</a>
            <a href="developer-tools.html">💻 Developer Tools</a>
            <a href="image-tools.html">🖼️ Image Tools</a>
            <a href="generators.html">⚙️ Generators</a>
            <a href="calculators.html">🧮 Calculators</a>
            <a href="time-tools.html">🕒 Time Tools</a>
            <a href="math-numbers.html">🔢 Math & Numbers</a>
            <a href="fun-utility.html">🎯 Fun & Utility</a>
            <a href="seo-web-tools.html">🌐 SEO & Web Tools</a>
          </div>
        </div>
        <a href="../index.html#popular" class="nav-link">Popular Tools</a>
        <a href="../about.html" class="nav-link">About Us</a>
        <a href="../contact.html" class="nav-link">Contact Us</a>
        <a href="../privacy.html" class="nav-link">Privacy Policy</a>
      </nav>
      
      <div class="burger-menu">
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
      </div>
    </div>
  </header>

  <!-- Category Content Layout -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../index.html#categories">Categories</a> &gt; <span>Generators</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Online <span>Generator</span> Tools</h1>
      <p class="tool-desc-lead">Generate secure passwords, brand business names, click-worthy headlines, and design CSS gradient styling codes client-side with complete privacy.</p>
    </div>

    <!-- Active Tools Grid -->
    <section style="margin-bottom: 60px;">
      {grids_html}
    </section>

    <!-- Technical SEO Article -->
    <article class="seo-article">
      {category_seo_text}
    </article>
  </main>

  <!-- Footer Section -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Col 1 -->
      <div>
        <a href="../index.html" class="logo">
          <span class="logo-icon"><span class="logo-icon-inner"></span></span>
          Enginewheels
        </a>
        <p class="footer-col-desc">A premium ecosystem of free, fast, and privacy-oriented online tools. Process your files, text, hashes, and configurations safely in your browser.</p>
        <div class="social-links">
          <a href="#" class="social-icon" aria-label="Facebook">FB</a>
          <a href="#" class="social-icon" aria-label="Instagram">IG</a>
          <a href="#" class="social-icon" aria-label="Twitter">X</a>
          <a href="#" class="social-icon" aria-label="LinkedIn">LN</a>
          <a href="#" class="social-icon" aria-label="YouTube">YT</a>
        </div>
      </div>
      
      <!-- Col 2 -->
      <div>
        <h3 class="footer-title">Quick Links</h3>
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About Us</a>
          <a href="../contact.html">Contact Us</a>
          <a href="../sitemap.html">Sitemap</a>
        </div>
      </div>
      
      <!-- Col 3 -->
      <div>
        <h3 class="footer-title">Legal Links</h3>
        <div class="footer-links">
          <a href="../privacy.html">Privacy Policy</a>
          <a href="../disclaimer.html">Disclaimer</a>
          <a href="../terms.html">Terms & Conditions</a>
        </div>
      </div>
      
      <!-- Col 4 -->
      <div>
        <h3 class="footer-title">Popular Tools</h3>
        <div class="footer-links">
          <a href="../tools/word-counter.html">Word Counter</a>
          <a href="../tools/json-formatter.html">JSON Formatter</a>
          <a href="../tools/password-generator.html">Password Generator</a>
          <a href="../tools/qr-code-generator.html">QR Code Generator</a>
          <a href="../tools/age-calculator.html">Age Calculator</a>
        </div>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <div class="footer-copy">&copy; <span id="footer-year"></span> Enginewheels. All rights reserved. Built with privacy.</div>
      <div class="footer-bottom-links">
        <a href="../privacy.html">Privacy</a>
        <a href="../terms.html">Terms</a>
        <a href="../disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </footer>

  <script src="../assets/js/main.js"></script>
</body>
</html>
"""

category_page_path = os.path.join(ROOT_DIR, "category", "generators.html")
with open(category_page_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)
print("category/generators.html rewritten successfully.")

# ----------------- REWRITE SITEMAP.HTML -----------------
print("Rewriting sitemap.html...")

sitemap_html_path = os.path.join(ROOT_DIR, "sitemap.html")
with open(sitemap_html_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Replace generator tools section inside sitemap.html
start_target = '<!-- START GENERATOR TOOLS -->'
end_target = '<!-- END GENERATOR TOOLS -->'

start_idx = sitemap_content.find(start_target)
end_idx = sitemap_content.find(end_target)

gen_sitemap_links = ""
for t in DEDUPLICATED_GENERATOR_TOOLS:
    gen_sitemap_links += f'          <li><a href="generator-tools/{t["slug"]}.html">{t["name"]}</a></li>\n'

if start_idx != -1 and end_idx != -1:
    new_sitemap_block = f"{start_target}\n{gen_sitemap_links}          {end_target}"
    sitemap_content = sitemap_content[:start_idx] + new_sitemap_block + sitemap_content[end_idx + len(end_target):]
    with open(sitemap_html_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("sitemap.html updated in-place.")
else:
    # If comments do not exist, insert the column dynamically next to Developer Tools
    target_to_replace = "    </div>\n  </div>\n</main>"
    replacement = f"""      <div>
        <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Generator Tools</h2>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
{start_target}
{gen_sitemap_links}          {end_target}
        </ul>
      </div>
    </div>
  </div>
</main>"""
    sitemap_content = sitemap_content.replace(target_to_replace, replacement)
    with open(sitemap_html_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("sitemap.html updated by adding Generator Tools column.")

# ----------------- REWRITE SITEMAP.XML -----------------
print("Rewriting sitemap.xml...")

# We will collect all generated tools urls
xml_urls = []
for calc in ALL_CALCULATORS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/calculators/{calc['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in ALL_TEXT_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/text-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in DEDUPLICATED_SECURITY_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/security-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in DEDUPLICATED_IMAGE_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/image-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in DEDUPLICATED_TIME_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/time-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in DEDUPLICATED_DEV_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/developer-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in DEDUPLICATED_GENERATOR_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/generator-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")

xml_urls_str = "\n".join(xml_urls)

sitemap_xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Core Information Pages -->
  <url>
    <loc>https://enginewheels.com/index.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/about.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/contact.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/sitemap.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/privacy.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/terms.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  
  <!-- Category Pages -->
  <url>
    <loc>https://enginewheels.com/category/text-tools.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/security-tools.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/developer-tools.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/image-tools.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/time-tools.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/generators.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Core 16 tools -->
  <url><loc>https://enginewheels.com/tools/word-counter.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/case-converter.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/password-generator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/hash-generator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/json-formatter.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/url-encoder-decoder.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/qr-code-generator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/uuid-generator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/age-calculator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/percentage-calculator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/epoch-converter.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/binary-converter.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/color-picker.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/base64-image.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/meta-tag-generator.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/morse-code.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>

  <!-- Generated Pages -->
{xml_urls_str}
</urlset>"""

sitemap_xml_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_xml_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)
print("sitemap.xml rebuilt.")

# ----------------- REWRITE ASSETS/JS/MAIN.JS SEARCH INDEX -----------------
print("Updating assets/js/main.js search index...")

main_js_path = os.path.join(ROOT_DIR, "assets", "js", "main.js")
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js_content = f.read()

start_idx = main_js_content.find("const ENGINYWHEELS_TOOLS = [")
end_idx = main_js_content.find("];", start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not locate search index array in main.js!")
    exit(1)

# Base tools
search_items = [
  { "name": "Word Counter", "url": "tools/word-counter.html", "category": "Text Tools", "desc": "Count words, characters, sentences, paragraphs, and reading time." },
  { "name": "Case Converter", "url": "tools/case-converter.html", "category": "Text Tools", "desc": "Convert text to UPPERCASE, lowercase, Title Case, Sentence case, and more." },
  { "name": "Password Generator", "url": "tools/password-generator.html", "category": "Security Tools", "desc": "Create secure custom passwords with entropy assessment." },
  { "name": "Hash Generator", "url": "tools/hash-generator.html", "category": "Security Tools", "desc": "Generate MD5, SHA-1, SHA-256, and SHA-512 cryptographic hashes." },
  { "name": "JSON Formatter & Validator", "url": "tools/json-formatter.html", "category": "Developer Tools", "desc": "Format, validate, beautify, and minify raw JSON data." },
  { "name": "URL Encoder & Decoder", "url": "tools/url-encoder-decoder.html", "category": "Developer Tools", "desc": "Encode or decode strings to match standard URL format." },
  { "name": "QR Code Generator", "url": "tools/qr-code-generator.html", "category": "Generators", "desc": "Generate and download custom QR codes for links, text, and emails." },
  { "name": "UUID Generator", "url": "tools/uuid-generator.html", "category": "Generators", "desc": "Generate secure version 4 UUIDs (single or bulk)." },
  { "name": "Age Calculator", "url": "tools/age-calculator.html", "category": "Calculators", "desc": "Calculate your exact age in years, months, days, and breakdown details." },
  { "name": "Percentage Calculator", "url": "tools/percentage-calculator.html", "category": "Calculators", "desc": "Perform standard percentage calculations easily." },
  { "name": "Epoch Time Converter", "url": "tools/epoch-converter.html", "category": "Time Tools", "desc": "Convert Unix timestamps to human-readable dates and vice-versa." },
  { "name": "Binary Converter", "url": "tools/binary-converter.html", "category": "Math & Numbers", "desc": "Convert numbers or text between Binary, Decimal, Hex, and Octal formats." },
  { "name": "Color Picker & Converter", "url": "tools/color-picker.html", "category": "Image Tools", "desc": "Translate colors between HEX, RGB, HSL, and CMYK formats." },
  { "name": "Base64 Image Encoder", "url": "tools/base64-image.html", "category": "Image Tools", "desc": "Convert images to Base64 data strings for inline usage." },
  { "name": "Meta Tag Generator", "url": "tools/meta-tag-generator.html", "category": "SEO & Web Tools", "desc": "Generate complete meta tags for SEO, OpenGraph, and Twitter." },
  { "name": "Morse Code Translator", "url": "tools/morse-code.html", "category": "Fun & Utility", "desc": "Translate text to Morse code and back with Web Audio playback." }
]

# Append calculators
for calc in ALL_CALCULATORS:
    search_items.append({
        "name": calc["name"],
        "url": f"calculators/{calc['slug']}.html",
        "category": f"Calculators ({calc['category']})",
        "desc": calc["desc"]
    })

# Append text tools
for tool in ALL_TEXT_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"text-tools/{tool['slug']}.html",
        "category": f"Text Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append security tools
for tool in DEDUPLICATED_SECURITY_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"security-tools/{tool['slug']}.html",
        "category": f"Security Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append image tools
for tool in DEDUPLICATED_IMAGE_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"image-tools/{tool['slug']}.html",
        "category": f"Image Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append time tools
for tool in DEDUPLICATED_TIME_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"time-tools/{tool['slug']}.html",
        "category": f"Time Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append developer tools
for tool in DEDUPLICATED_DEV_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"developer-tools/{tool['slug']}.html",
        "category": f"Developer Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append generator tools
for tool in DEDUPLICATED_GENERATOR_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"generator-tools/{tool['slug']}.html",
        "category": f"Generator Tools ({tool['category']})",
        "desc": tool["desc"]
    })

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+2:]

# Update the prefix path logic to handle generator-tools directory
prefix_match = re.search(r"const prefix = \(.*?\) \? '\.\./' : '';", updated_main_js)
if prefix_match:
    clean_prefix = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/') || window.location.pathname.includes('/security-tools/') || window.location.pathname.includes('/image-tools/') || window.location.pathname.includes('/time-tools/') || window.location.pathname.includes('/developer-tools/') || window.location.pathname.includes('/generator-tools/')) ? '../' : '';"
    updated_main_js = updated_main_js.replace(prefix_match.group(0), clean_prefix)

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js search index and prefix checks rebuilt.")
print("[+] All generation operations completed successfully!")
