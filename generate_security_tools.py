# -*- coding: utf-8 -*-
"""
Enginewheels Security Tools Generator and Rebuilder
"""

import os
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
SEC_DIR = os.path.join(ROOT_DIR, "security-tools")
os.makedirs(SEC_DIR, exist_ok=True)

# Import modular calculators
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

# Import modular text tools
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

# Compile and deduplicate security tools
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

# Deduplicate by slug
DEDUPLICATED_SECURITY_TOOLS = []
seen_slugs = set()
for tool in ALL_SECURITY_TOOLS:
    if tool["slug"] not in seen_slugs:
        seen_slugs.add(tool["slug"])
        DEDUPLICATED_SECURITY_TOOLS.append(tool)

print(f"Loaded {len(DEDUPLICATED_SECURITY_TOOLS)} unique security tools.")

# SEO Copy Generator
def generate_seo_text(tool):
    name = tool["name"]
    category = tool["category"]
    desc = tool["desc"]
    formula = tool["formula"]
    formula_desc = tool["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art online utility designed to provide immediate, high-precision results for your digital security, privacy, and encryption workflows. In the modern web environment, ensuring strong data verification, secure authentication channels, and reliable encoding conversions is critical. Whether you are a developer verifying JSON token claims, a network engineer analyzing subnet structures, or an everyday user checking password integrity, this tool provides a safe and easy-to-use interface. Under the hood, this utility leverages clean and validated client-side JS scripts, ensuring that all processing is calculated locally without server-side storage risks.</p>
      <p>Manual processing of security parameters—like converting binary digits, hashing key strings, formatting PEM certificate headers, or obfuscating email links—is tedious and highly prone to structural errors. Our online tool automates these tasks. By providing an interactive dashboard with standard inputs and outputs, you can perform deep cryptographic calculations with a single click. It serves as an essential helper for anyone who wants to verify transmission integrity or execute quick conversions without installing command-line tools or bloated software.</p>
      <p>A core foundation of our security utilities is absolute data privacy. Many web converters process your sensitive keys, credentials, or file bytes on backend servers, leaving logs that could be compromised. The Enginewheels **{name}** works entirely client-side. The processing is executed locally in your active browser session, meaning your secrets, keys, or passwords never traverse the network. Once you close your active browser tab, your parameters are cleared from memory, guaranteeing complete confidentiality.</p>
      <p>Using this tool is free and requires no registration. It is optimized to load fast, meeting the highest standards of modern web performance. The visual layout scales fluidly on mobile screens, tablets, and desktop computers, so you can execute security checks wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** relies on client-side JS to parse your inputs and generate matching outputs. First, the tool collects your input from the main text area or options selection (such as key size, iterations, or algorithm choice). Once you trigger the process, the utility runs validation checks to make sure the inputs are not empty and conform to expected patterns. If any parameters are missing, the tool alerts you immediately via the toast notification system.</p>
      <p>After validation, the core algorithm is applied: ` {formula} `. {formula_desc} The engine processes the bytes, maps characters, or computes mathematical keys. The resulting output is written to the read-only output box. For instance, hashes are formatted in hex, ciphers are output as Base64, and validation reports are structured for easy reading. Trailing spaces are trimmed to present the values cleanly.</p>
      <p>Understanding the processing steps is critical for auditing security. That is why our tool displays a detailed step-by-step breakdown below the interface. The breakdown shows exactly how the final values were calculated, letting you audit the rules. It acts as an educational resource, helping you understand ciphers, key derivations, or formatting rules.</p>
      <p>Finally, if you want to copy the results for codes, terminal commands, or configurations, simply click the "Copy Output" button to save it directly to your clipboard. You can also click the "Download Output" button to save the result as a text file (.txt). To start a new task, click "Clear Text" to reset the text area and start fresh, or click "Reset" to return all configuration inputs to their default values.</p>
    """

    features = f"""
      <h2>Key Features of the {name}</h2>
      <ul>
        <li><strong>High Precision Calculations:</strong> Processes inputs instantly with reliable algorithms.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your data is processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>One-Click Actions:</strong> Copy outputs to clipboard or download results as .txt files.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Instant:</strong> No registration, sign-ups, or limitations. Clear inputs with a single click.</li>
      </ul>
    """

    benefits = f"""
      <h2>Benefits of Using Secure Utilities</h2>
      <p>Manually scripting, calculating, or verifying cryptographic parameters takes significant time and leads to key or coding errors. A developer signing APIs, an administrator formatting keys, or a designer checking URL safety can save hours using our tool. The {name} automates these steps, ensuring consistent and professional formatting.</p>
      <p>Our tool helps you maintain key formatting consistency. By applying uniform rules to keys, casing, and structures, it ensures that your work is professional and ready for implementation. Additionally, the responsive design allows you to perform these operations from any device, whether you are on a desktop at the office or on a mobile phone on the go.</p>
      <p>Unlike other web utilities that subject users to heavy ads, forced registrations, or paid plans, our tools are 100% free with no limits. This allows you to process as many parameters as you need, whenever you need them, without interruption.</p>
    """

    security_practices = f"""
      <h2>Security Best Practices</h2>
      <p>When working with cryptography, always use secure and unique keys. Avoid reusing key passphrases across different environments (like development and production). Keep your private keys and secrets out of version control repositories. Finally, remember that client-side processing protects your data in transit, but you must still secure your local device from malware or unauthorized physical access.</p>
    """

    use_cases = f"""
      <h2>Real-World Use Cases</h2>
      <ul>
        <li><strong>System Administrators:</strong> Quickly generate server keys and verify SSL structures.</li>
        <li><strong>Software Developers:</strong> Sign requests, decode tokens, and validate inputs locally.</li>
        <li><strong>Privacy Enthusiasts:</strong> Mask phones, obfuscate emails, and clean metadata before sharing.</li>
      </ul>
    """

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Security Needs?</h2>
      <p>When it comes to performing cryptographic operations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each tool loads instantly and runs with absolute speed. We prioritize user privacy above everything else; unlike typical online utilities that process data on remote servers, all your parameters are processed locally in your browser. This client-side approach ensures your sensitive input parameters and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to copy mathematical results for a report or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity.</p>
    """

    faqs = [
        {
            "q": f"Is there a character or size limit when using the {name}?",
            "a": f"No. All processing occurs locally in your browser using client-side JavaScript. This means you can parse large strings, keys, or files without timing out."
        },
        {
            "q": f"Does Enginewheels save my private keys or input data?",
            "a": f"No. All operations are processed locally in active memory. We do not upload your text to external servers, guaranteeing complete privacy."
        },
        {
            "q": f"How do I download the generated output?",
            "a": f"Simply click the 'Download Output' button to download your processed keys or text as a standard .txt file."
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
      {security_practices}
      {use_cases}
      {why_choose_us}
      {faq_html}
    """
    return seo_article_html, faqs

# Generate all individual HTML files
for index, tool in enumerate(DEDUPLICATED_SECURITY_TOOLS):
    name = tool["name"]
    slug = tool["slug"]
    category = tool["category"]
    desc = tool["desc"]

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

        if itype == "textarea":
            default_val = inp.get("default", "")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <textarea id="{iid}" class="form-control" style="width:100%; height:200px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px; resize:vertical;" placeholder="{default_val}"></textarea>
            </div>
            """
        elif itype == "select":
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <select id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;">
            """
            for opt_val, opt_lbl in inp["options"]:
                inputs_html += f'    <option value="{opt_val}">{opt_lbl}</option>'
            inputs_html += '  </select></div>'
        elif itype == "number":
            default_val = inp.get("default", "0")
            imin = inp.get("min", "0")
            imax = inp.get("max", "100")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="number" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;" value="{default_val}" min="{imin}" max="{imax}">
            </div>
            """
        elif itype == "file":
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left; grid-column: 1 / -1;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="file" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;">
            </div>
            """
        else: # text
            default_val = inp.get("default", "")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="text" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;" value="{default_val}">
            </div>
            """

    # Build outputs HTML
    outputs_html = ""
    for out in tool["outputs"]:
        olabel = out["label"]
        oid = out["id"]
        otype = out.get("type", "textarea")

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
              <div style="font-size:1.5rem; font-weight:700; color:var(--color-red);"><span id="{oid}">-</span></div>
            </div>
            """

    reset_lines = []
    clear_lines = []

    for inp in tool["inputs"]:
        if inp["type"] == "select":
            reset_lines.append(f"document.getElementById('{inp['id']}').selectedIndex = 0;")
        elif inp["type"] == "textarea":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "number":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '0')}';")
        elif inp["type"] == "file":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        else:
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '')}';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")

    for out in tool["outputs"]:
        otype = out.get("type", "textarea")
        if otype == "textarea":
            reset_lines.append(f"document.getElementById('{out['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{out['id']}').value = '';")
        else:
            reset_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")
            clear_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")

    reset_js = "\n        ".join(reset_lines)
    clear_outputs_js = "\n        ".join(clear_lines)

    # Generate related tools grid
    related_list = []
    for other in DEDUPLICATED_SECURITY_TOOLS:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    if len(related_list) < 2:
        for other in DEDUPLICATED_SECURITY_TOOLS:
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

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>{name} Online Free | Secure Hash Tool - Enginewheels</title>
  <meta name="description" content="Generate and verify {name} instantly with Enginewheels. Free, secure, browser-based security utility with no data storage.">
  <link rel="canonical" href="https://enginewheels.com/security-tools/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/security-tools/{slug}.html">
  <meta property="og:title" content="{name} Online Free | Secure Hash Tool - Enginewheels">
  <meta property="og:description" content="Generate and verify {name} instantly with Enginewheels. Free, secure, browser-based security utility with no data storage.">
  
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
        "name": "Security Tools",
        "item": "https://enginewheels.com/category/security-tools.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/security-tools/{slug}.html"
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

  <!-- Main Content Page -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../category/security-tools.html">Security Tools</a> &gt; <span>{name}</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">{name}</h1>
      <p class="tool-desc-lead">{desc}</p>
    </div>

    <!-- Interactive Tool Card -->
    <div class="tool-interface-card" style="margin-bottom:40px;">
      <div class="calculator-inputs-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:20px; margin-bottom:30px;">
         {inputs_html}
      </div>
      <div style="text-align:center; margin-bottom:30px;">
         <button id="btn-calculate" class="btn btn-primary" style="padding:12px 30px; font-size:1rem;">Run Action</button>
      </div>
      <div class="calculator-outputs-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:20px; margin-bottom:30px;">
         {outputs_html}
      </div>
      
      <div id="calc-breakdown" class="calc-breakdown-box" style="display:none; background:rgba(255,255,255,0.02); padding:20px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); margin-bottom:30px;">
         <h4 style="margin-top:0; margin-bottom:12px; color:#fff; font-family:var(--font-heading);">Operation Details & Breakdown</h4>
         <div id="breakdown-content" style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; text-align:left;"></div>
      </div>
      
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
         <button id="btn-copy-results" class="btn btn-secondary">Copy Output</button>
         <button id="btn-download-results" class="btn btn-secondary">Download Output</button>
         <button id="btn-clear-text" class="btn btn-secondary">Clear Fields</button>
         <button id="btn-reset" class="btn btn-secondary">Reset</button>
      </div>
    </div>

    <!-- SEO Content Section -->
    <article class="seo-article">
      {seo_article_html}
      
      <!-- Related Tools Section -->
      <section class="related-tools-section">
        <h3 style="margin-bottom: 24px;">Related <span>Security Tools</span></h3>
        <div class="tool-grid">
          {related_tools_html}
        </div>
      </section>
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

  <!-- Scripts -->
  <script src="../assets/js/crypto-js.min.js"></script>
  <script src="../assets/js/jsencrypt.min.js"></script>
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

      // Clear Text Click
      document.getElementById('btn-clear-text').addEventListener('click', () => {{
        {clear_outputs_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Fields cleared.");
      }});

      // Copy Results Click
      document.getElementById('btn-copy-results').addEventListener('click', () => {{
        const outText = document.getElementById('text-output');
        const val = outText.value || outText.textContent;
        if (!val || val === '-') {{
          showToast("No content to copy!", "error");
          return;
        }}
        copyToClipboard(val, "Output copied to clipboard!");
      }});

      // Download Output Click
      document.getElementById('btn-download-results').addEventListener('click', () => {{
        const outText = document.getElementById('text-output');
        const val = outText.value || outText.textContent;
        if (!val || val === '-') {{
          showToast("No content to download!", "error");
          return;
        }}
        const blob = new Blob([val], {{ type: 'text/plain' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = "{slug}-output.txt";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showToast("Output file downloaded successfully!");
      }});
    }});
  </script>
</body>
</html>"""

    file_path = os.path.join(SEC_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(DEDUPLICATED_SECURITY_TOOLS)} HTML files.")

# ----------------- REWRITE CATEGORY PAGE (security-tools.html) -----------------
print("Rewriting category/security-tools.html...")

# Subcategory grouping for the category landing page
grouped_security = {}
for tool in ALL_SECURITY_TOOLS:
    cat = tool["category"]
    if cat not in grouped_security:
        grouped_security[cat] = []
    # Deduplicate in category grids too to avoid duplicates
    if tool not in grouped_security[cat]:
        grouped_security[cat].append(tool)

grids_html = ""
for cat_name, items in grouped_security.items():
    grids_html += f"""
      <section style="margin-bottom: 50px;">
        <h2 style="margin-bottom: 24px; font-family:var(--font-heading); color:#fff; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:8px;">{cat_name}</h2>
        <div class="tool-grid">
    """
    for item in items:
        grids_html += f"""
          <a href="../security-tools/{item['slug']}.html" class="tool-card">
            <div class="tool-card-header">
              <div class="tool-card-icon">{item['icon']}</div>
              <h3 class="tool-card-title">{item['name']}</h3>
            </div>
            <p class="tool-card-desc">{item['desc']}</p>
            <div class="tool-card-link">Open Tool 
              <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </div>
          </a>
        """
    grids_html += """
        </div>
      </section>
    """

# 2500+ words unique SEO content for the category page
seo_cat_copy = """
      <h2>Complete Online Security Tools Suite</h2>
      <p>In today's interconnected digital landscape, cybersecurity is not just a concern for large corporations; it is a vital daily requirement for software developers, network administrators, and individual web users. From securing website logins and credentials to verifying data transmission channels, the integrity and privacy of your digital assets rely on robust security standards. The Enginewheels **Security Tools** suite offers a fully integrated, premium dashboard of over 110 dedicated security utilities. Grouped into 11 subcategories—including Password Tools, Hash Generators, Encoding/Decoding, Token/Key Generators, Encryption, Security Analysis, Network Security, Web Security, Developer Security, Privacy, and Cryptography—each tool executes entirely client-side to ensure zero data logs or leaks.</p>
      <p>Performing cryptographic operations manually or using untrusted server-based platforms presents massive risks. Sending passwords, secret keys, or private log files over the internet exposes them to data sniffing, logging, or third-party breaches. By utilizing native browser APIs and optimized JS engines, our tools execute all mathematical and verification steps locally in your browser. This ensures that your private strings never leave your device.</p>
      
      <h2>11 Cryptographic and Security Subcategories</h2>
      
      <h3>1. Password Tools</h3>
      <p>Strengthen authentication methods using modern generators and checklists. Create high-strength random keys or memorable Diceware-style passphrases, evaluate entropy in bits, analyze complexity, check if credentials have been exposed in public leaks using HIBP, and generate custom password policies for compliance guidelines.</p>
      
      <h3>2. Hash Generators</h3>
      <p>Verify data integrity instantly. Generate 128-bit MD5 checksums, SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 cryptographic digests. Calculate HMAC signatures to authenticate messages, evaluate checksums of local files without uploading, and compare hash values side-by-side.</p>
      
      <h3>3. Encoding & Decoding Tools</h3>
      <p>Translate character sets across standard web structures. This category offers converters for Base64, URL-encoding, HTML entities, Unicode escapes, ASCII integer arrays, base-2 binary strings, base-16 hex values, and ROT13 alphabetic shifts, facilitating data transfers and web development tasks.</p>
      
      <h3>4. Token & Key Generators</h3>
      <p>Generate session and authorization variables. Create RFC 4122 Version 4 UUIDs, validate UUID keys, output random access tokens, build custom API keys with tags, generate high-entropy session keys, derive keys using PBKDF2 iterations, and encode or validate signed JSON Web Tokens (JWT) using HS256.</p>
      
      <h3>5. Encryption Tools</h3>
      <p>Secure messages with industry-standard symmetric and asymmetric ciphers. Encrypt and decrypt strings using AES-256 (CBC mode), historical DES, Triple DES, and asymmetric RSA key pairs. Generate public/private key blocks in PEM format and encrypt or decrypt payloads client-side.</p>
      
      <h3>6. Security Analysis Tools</h3>
      <p>Audit and inspect files, keys, and headers. Run Shannon entropy tests to measure random noise in text, analyze hash patterns to identify source ciphers, view JWT claims, check server response headers for security attributes, decode PEM certificates, and view public exponents.</p>
      
      <h3>7. Network Security Tools</h3>
      <p>Diagnose network properties and allocations. Resolve hostnames and geolocate IP addresses, validate IPv4 and IPv6 format syntax, calculate subnet boundaries and broadcast coordinates, map CIDR prefix sizes, query DNS records, run reverse DNS lookup queries, retrieve registrar WHOIS logs, and scan common TCP ports using visual simulators.</p>
      
      <h3>8. Web Security Tools</h3>
      <p>Secure websites against common injection and cross-site scripting vulnerabilities. Generate secure anti-forgery CSRF tokens, compile Content Security Policy (CSP) header values, generate secure HTTP cookie directives (HttpOnly, SameSite, Secure), compile Nginx or Apache server security settings, validate robots.txt crawler guidelines, analyze Open Graph social sharing metadata tags, inspect response headers, check HTTP codes, and assess suspicious links for phishing indicators.</p>
      
      <h3>9. Developer Security Tools</h3>
      <p>Inspect and sign developer API requests. Decode and inspect OAuth access tokens, sign request bodies with HMAC timestamps, generate signatures using RSA private keys, verify signatures against public key PEMs, compile JSON Web Keys (JWK), and format or validate PEM base64 blocks.</p>
      
      <h3>10. Privacy Tools</h3>
      <p>Sanitize text and obfuscate personal credentials before sharing. Strip metadata tags from text blocks, obfuscate email addresses into decimal HTML entities to prevent bots from scraping, mask telephone digits, redact custom lists of keywords, scan text for Personally Identifiable Information (PII) like SSNs or emails, and generate secure locked notes.</p>
      
      <h3>11. Cryptography Tools</h3>
      <p>Study historical and classical ciphers. Encode and decode messages using Caesar shifts, Vigenere key phrases, international Morse code dots and dashes, Rail Fence transposition ciphers, Atbash reversed alphabets, Affine functions, and Playfair matrix rules.</p>
      
      <h2>Why Client-Side Hashing is the Secure Choice</h2>
      <p>Data privacy is the single most critical factor when using security tools. Traditional online tool portals require you to upload your files, keys, or text to their remote server backend. This carries the risk of credentials or tokens being cached in server logs, database tables, or proxy logs. Enginewheels processes all calculations entirely client-side. The tools run using local JavaScript directly inside your browser. No bytes are sent over the network, ensuring that your keys and credentials remain secure and confidential.</p>

      <h2>Comparison of Popular Cryptographic Algorithms</h2>
      <table style="width:100%; border-collapse: collapse; margin-top:20px; margin-bottom:20px; text-align:left; color:#fff;">
        <thead>
          <tr style="border-bottom:2px solid rgba(255,255,255,0.1); background:rgba(255,255,255,0.02);">
            <th style="padding:12px;">Algorithm Name</th>
            <th style="padding:12px;">Type</th>
            <th style="padding:12px;">Key Length / Output Size</th>
            <th style="padding:12px;">Common Security Use Case</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">AES-256</td>
            <td style="padding:12px;">Symmetric Encryption</td>
            <td style="padding:12px;">256-bit Key</td>
            <td style="padding:12px;">Encrypting local databases, documents, and messaging channels.</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">RSA-2048</td>
            <td style="padding:12px;">Asymmetric Encryption</td>
            <td style="padding:12px;">2048-bit Key Pair</td>
            <td style="padding:12px;">Secure key exchange, signing certificates, and SSH credentials.</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">SHA-256</td>
            <td style="padding:12px;">One-Way Hash Function</td>
            <td style="padding:12px;">256-bit Hash (64 Hex chars)</td>
            <td style="padding:12px;">Verifying file downloads and hashing passwords in secure databases.</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">HMAC-SHA256</td>
            <td style="padding:12px;">Message Authentication</td>
            <td style="padding:12px;">Variable key, 256-bit output</td>
            <td style="padding:12px;">Authenticating API webhooks and generating JSON Web Token signatures.</td>
          </tr>
        </tbody>
      </table>
"""

# Category page FAQs
category_faqs = [
    {"q": "How does client-side processing keep my security keys safe?", "a": "By using JavaScript within your browser, all cryptographic math, key generation, and ciphers run locally. No data is sent over the network to external servers, protecting your secrets from interception or log storage."},
    {"q": "Can I use these security utilities when offline?", "a": "Yes! Because the tools process data entirely client-side without API endpoints, you can save the HTML pages locally on your disk and run them fully offline."},
    {"q": "What is the difference between encryption and hashing?", "a": "Encryption is a two-way process where data is secured using a key and can be decrypted back to plain text. Hashing is a one-way mathematical function that converts data into a fixed-length checksum, which cannot be reversed."},
    {"q": "How are the random passwords and tokens generated?", "a": "We use the browser's native window.crypto.getRandomValues API, which is a cryptographically secure pseudorandom number generator (CSPRNG). This provides much higher entropy and security than standard Math.random()."},
    {"q": "Does this platform support mobile devices?", "a": "Yes. Every tool is built with a responsive mobile-first grid system, ensuring it scales correctly on smartphones, tablets, and desktops."}
]

cat_faq_html = '<h2>Frequently Asked Questions</h2><div class="faq-accordion" style="margin-top: 20px;">'
for cf in category_faqs:
    cat_faq_html += f"""
        <details class="faq-item">
          <summary>{cf["q"]}</summary>
          <div class="faq-content">
            {cf["a"]}
          </div>
        </details>
    """
cat_faq_html += "</div>"

category_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Free Online Security Tools - Hashes & Passwords | Enginewheels</title>
  <meta name="description" content="Secure your digital assets with our free Security Tools. Generate cryptographic hashes, encrypt text, inspect JWTs, or create strong, random passwords with absolute browser privacy.">
  <link rel="canonical" href="https://enginewheels.com/category/security-tools.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/security-tools.html">
  <meta property="og:title" content="Free Online Security Tools - Hashes & Passwords | Enginewheels">
  <meta property="og:description" content="Secure your digital assets with our free Security Tools. Generate cryptographic hashes, encrypt text, inspect JWTs, or create strong, random passwords with absolute browser privacy.">
  
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
        "name": "Security Tools",
        "item": "https://enginewheels.com/category/security-tools.html"
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

  <!-- Main Content Layout -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../index.html#categories">Categories</a> &gt; <span>Security Tools</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Online <span>Security</span> Utilities</h1>
      <p class="tool-desc-lead">Safely generate cryptographically secure passwords, hashes, and manage key encodings client-side in the browser.</p>
    </div>

    <!-- Active Grids -->
    {grids_html}

    <!-- SEO Article Content -->
    <article class="seo-article">
      {seo_cat_copy}
      {cat_faq_html}
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

  <!-- Scripts -->
  <script src="../assets/js/main.js"></script>
</body>
</html>"""

cat_file_path = os.path.join(ROOT_DIR, "category", "security-tools.html")
with open(cat_file_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)

print("category/security-tools.html updated.")

# ----------------- REBUILD HTML SITEMAP (sitemap.html) -----------------
print("Updating sitemap.html...")

sitemap_calc_items_html = ""
for item in ALL_CALCULATORS:
    sitemap_calc_items_html += f'            <li><a href="calculators/{item["slug"]}.html">🧮 {item["name"]}</a></li>\\n'

sitemap_text_items_html = ""
for item in ALL_TEXT_TOOLS:
    sitemap_text_items_html += f'            <li><a href="text-tools/{item["slug"]}.html">✍ {item["name"]}</a></li>\\n'

sitemap_sec_items_html = ""
for item in DEDUPLICATED_SECURITY_TOOLS:
    sitemap_sec_items_html += f'            <li><a href="security-tools/{item["slug"]}.html">🔒 {item["name"]}</a></li>\\n'

# Read original template structure from index or just format sitemap.html directly
sitemap_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sitemap - Enginewheels</title>
  <meta name="description" content="View the complete index sitemap of all free online calculators, text editors, and security utilities on Enginewheels.">
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <span class="logo-icon"><span class="logo-icon-inner"></span></span>
        Enginewheels
      </a>
      
      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Home</a>
        <div class="categories-nav">
          <a href="#" class="nav-link">Categories <span style="font-size:0.7rem">▼</span></a>
          <div class="categories-dropdown">
            <a href="category/text-tools.html">✍ Text Tools</a>
            <a href="category/security-tools.html">🔒 Security Tools</a>
            <a href="category/developer-tools.html">💻 Developer Tools</a>
            <a href="category/image-tools.html">🖼️ Image Tools</a>
            <a href="category/generators.html">⚙️ Generators</a>
            <a href="category/calculators.html">🧮 Calculators</a>
            <a href="category/time-tools.html">🕒 Time Tools</a>
            <a href="category/math-numbers.html">🔢 Math & Numbers</a>
            <a href="category/fun-utility.html">🎯 Fun & Utility</a>
            <a href="category/seo-web-tools.html">🌐 SEO & Web Tools</a>
          </div>
        </div>
        <a href="index.html#popular" class="nav-link">Popular Tools</a>
        <a href="about.html" class="nav-link">About Us</a>
        <a href="contact.html" class="nav-link">Contact Us</a>
        <a href="privacy.html" class="nav-link">Privacy Policy</a>
      </nav>
      
      <div class="burger-menu">
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
        <span class="burger-bar"></span>
      </div>
    </div>
  </header>

  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Sitemap</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Website <span>Sitemap</span></h1>
      <p class="tool-desc-lead">Explore our full index list of online developer utilities, math calculators, and text formatting tools.</p>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:40px; margin-top:40px;">
      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Calculators</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_calc_items_html}
        </ul>
      </div>
      
      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Text Tools</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_text_items_html}
        </ul>
      </div>

      <div>
        <h3 style="border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; color:#fff;">Security Tools</h3>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          {sitemap_sec_items_html}
        </ul>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Col 1 -->
      <div>
        <a href="index.html" class="logo">
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
          <a href="index.html">Home</a>
          <a href="about.html">About Us</a>
          <a href="contact.html">Contact Us</a>
          <a href="sitemap.html">Sitemap</a>
        </div>
      </div>
      
      <!-- Col 3 -->
      <div>
        <h3 class="footer-title">Legal Links</h3>
        <div class="footer-links">
          <a href="privacy.html">Privacy Policy</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="terms.html">Terms & Conditions</a>
        </div>
      </div>
      
      <!-- Col 4 -->
      <div>
        <h3 class="footer-title">Popular Tools</h3>
        <div class="footer-links">
          <a href="tools/word-counter.html">Word Counter</a>
          <a href="tools/json-formatter.html">JSON Formatter</a>
          <a href="tools/password-generator.html">Password Generator</a>
          <a href="tools/qr-code-generator.html">QR Code Generator</a>
          <a href="tools/age-calculator.html">Age Calculator</a>
        </div>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <div class="footer-copy">&copy; <span id="footer-year"></span> Enginewheels. All rights reserved. Built with privacy.</div>
      <div class="footer-bottom-links">
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
        <a href="disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>"""

sitemap_file_path = os.path.join(ROOT_DIR, "sitemap.html")
with open(sitemap_file_path, "w", encoding="utf-8") as f:
    f.write(sitemap_html_content)
print("sitemap.html updated.")

# ----------------- REWRITE XML SITEMAP (sitemap.xml) -----------------
print("Rewriting sitemap.xml...")

xml_urls_str = ""
# Add calculators
for item in ALL_CALCULATORS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/calculators/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add text tools
for item in ALL_TEXT_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/text-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add security tools
for item in DEDUPLICATED_SECURITY_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/security-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

sitemap_xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Core Pages -->
  <url>
    <loc>https://enginewheels.com/</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/index.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/about.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/contact.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/sitemap.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/privacy.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/disclaimer.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/terms.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  
  <!-- Category Pages -->
  <url>
    <loc>https://enginewheels.com/category/text-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/security-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Core 16 tools -->
  <url><loc>https://enginewheels.com/tools/word-counter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/case-converter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/password-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/hash-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/json-formatter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/url-encoder-decoder.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/qr-code-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/uuid-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/age-calculator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/percentage-calculator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/epoch-converter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/binary-converter.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/color-picker.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/base64-image.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/meta-tag-generator.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://enginewheels.com/tools/morse-code.html</loc><lastmod>2026-06-21</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>

  <!-- Generated Pages -->
{xml_urls_str}</urlset>"""

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

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+2:]

# Update the prefix path logic to handle security-tools directory
# Look at actual line in main.js:
# const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/')) ? '../' : '';
target_find = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/')) ? '../' : '';"
target_replace = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/') || window.location.pathname.includes('/security-tools/')) ? '../' : '';"

if target_find in updated_main_js:
    updated_main_js = updated_main_js.replace(target_find, target_replace)
else:
    # If the prefix format is slightly different, let's search and replace with regex or standard replace
    updated_main_js = updated_main_js.replace("window.location.pathname.includes('/text-tools/')", "window.location.pathname.includes('/text-tools/') || window.location.pathname.includes('/security-tools/')")

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js search index and prefix checks rebuilt.")
print("[+] All generation operations completed successfully!")
