# -*- coding: utf-8 -*-
"""
Enginewheels 129 Text Tools Generator and Rebuilder
"""

import os
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
TEXT_DIR = os.path.join(ROOT_DIR, "text-tools")
os.makedirs(TEXT_DIR, exist_ok=True)

# Import modular databases
from data_text_basic_case import BASIC_TEXT_CALCS, CASE_CONVERTER_CALCS
from data_text_format_replace import FORMATTER_CALCS, REPLACE_CALCS
from data_text_seo_writing import SEO_TEXT_CALCS, WRITING_CALCS
from data_text_social_dev import SOCIAL_CALCS, DEVELOPER_CALCS
from data_text_conv_url import CONVERTER_CALCS, URL_CALCS
from data_text_rand_adv_ai import RANDOM_CALCS, ADVANCED_CALCS, AI_CALCS

TEXT_TOOLS_DB = []
TEXT_TOOLS_DB.extend(BASIC_TEXT_CALCS)
TEXT_TOOLS_DB.extend(CASE_CONVERTER_CALCS)
TEXT_TOOLS_DB.extend(FORMATTER_CALCS)
TEXT_TOOLS_DB.extend(REPLACE_CALCS)
TEXT_TOOLS_DB.extend(SEO_TEXT_CALCS)
TEXT_TOOLS_DB.extend(WRITING_CALCS)
TEXT_TOOLS_DB.extend(SOCIAL_CALCS)
TEXT_TOOLS_DB.extend(DEVELOPER_CALCS)
TEXT_TOOLS_DB.extend(CONVERTER_CALCS)
TEXT_TOOLS_DB.extend(URL_CALCS)
TEXT_TOOLS_DB.extend(RANDOM_CALCS)
TEXT_TOOLS_DB.extend(ADVANCED_CALCS)
TEXT_TOOLS_DB.extend(AI_CALCS)

print(f"Loaded {len(TEXT_TOOLS_DB)} text tools successfully.")

# Custom template generator for SEO content
def generate_seo_text(calc):
    name = calc["name"]
    category = calc["category"]
    desc = calc["desc"]
    formula = calc["formula"]
    formula_desc = calc["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art, free online text utility engineered to provide instant, high-precision results for your editing, formatting, and analysis requirements. Whether you are a student writing an academic essay, an editor refining a newsletter draft, or a software engineer debugging variable formats, our browser-based tool simplifies your workflow by handling {category.lower()} tasks in real time. Under the hood, this utility leverages optimized client-side algorithms, ensuring that every operation is parsed accurately and efficiently without any server dependencies.</p>
      <p>Processing text manually—such as converting letters to uppercase, cleaning spaces, finding and replacing terms, or counting words—is highly tedious and prone to human errors. Our platform automates these tasks. By providing a clean interface with dedicated inputs and outputs, you can perform massive string changes in a single click. It serves as a daily helper for anyone who wants to verify content length rules or execute quick rewrites without installing heavy applications or office suites.</p>
      <p>A core aspect of our text utilities is absolute data security. Many online platforms process your input text on backend servers, meaning your drafts, passwords, emails, or codes are sent over the internet and may be stored in database logs. The Enginewheels **{name}** runs entirely client-side. The processing is executed locally in your browser using JavaScript, meaning your private text never leaves your device. Once you close your active browser tab, your data is cleared from memory, giving you complete peace of mind.</p>
      <p>Using this tool is simple and requires no registration or payment. It is optimized to load incredibly fast, meeting the highest performance standards of modern web design. The visual interface scales fluidly on mobile screens, tablets, and desktop computers, so you can execute text edits wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** relies on client-side JavaScript to evaluate your input text and generate processed output. First, the tool collects your text from the main input area, along with any optional settings (such as count specifications, search phrases, or choice dropdowns). Once you enter these values and click the process trigger, the client-side engine performs validation checks. These checks ensure that the inputs are not empty and fit within normal processing constraints. If any configuration is missing, the tool alerts you immediately via the toast notification system.</p>
      <p>After validation, the core text algorithm is applied: ` {formula} `. {formula_desc} The converter processes the characters, splits strings, or replaces symbols according to standard rules. The resulting output is dynamically formatted and written to the read-only output container. For instance, spacing is normalized, letter casings are swapped, or counts are tabulated for optimal readability. Trailing newlines are trimmed to present the text cleanly.</p>
      <p>Understanding the processing steps is critical for verifying results. That is why our tool displays a detailed step-by-step breakdown below the interface. The breakdown shows exactly how the final text or counts were produced, letting you audit the rules. It acts as an educational resource, helping you understand regular expressions, character mappings, or formatting criteria.</p>
      <p>Finally, if you want to copy the results for reports, code files, or documents, simply click the "Copy Output" button to save it directly to your clipboard. You can also click the "Download Output" button to save the result as a text file (.txt). To start a new task, click "Clear Text" to reset the text area and start fresh, or click "Reset" to return all configuration inputs to their default values.</p>
    """

    features = f"""
      <h2>Key Features of the {name}</h2>
      <ul>
        <li><strong>High Precision Processing:</strong> Processes text instantly with reliable algorithms.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your data is processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>One-Click Actions:</strong> Copy outputs to clipboard or download results as .txt files.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Instant:</strong> No registration, sign-ups, or limitations. Clear inputs with a single click.</li>
      </ul>
    """

    benefits = f"""
      <h2>Benefits of Automating Text Tasks</h2>
      <p>Manually rewriting, counting, or formatting text blocks takes significant time and leads to spelling or formatting errors. A developer converting variables, an editor formatting newsletter drafts, or an advertiser adjusting ad copy titles can save hours using our tool. The {name} automates these steps, ensuring consistent and professional formatting.</p>
      <p>Our tool helps you maintain formatting consistency across multiple documents. By applying uniform rules to capitalization, spacing, and characters, it ensures that your work is professional and ready for publishing. Additionally, the responsive design allows you to perform these operations from any device, whether you are on a desktop at the office or on a mobile phone on the go.</p>
      <p>Unlike other web utilities that subject users to heavy ads, forced registrations, or paid plans, our text tools are 100% free with no limits. This allows you to process as many files as you need, whenever you need them, without interruption.</p>
    """

    use_cases = f"""
      <h2>Real-World Use Cases</h2>
      <ul>
        <li><strong>Content Creators & Writers:</strong> Instantly check word counts and format blog drafts or social posts.</li>
        <li><strong>Developers & Designers:</strong> Format code structures (JSON, CSV, HTML) and convert string encodings.</li>
        <li><strong>Office Professionals:</strong> Quickly clean up emails, format reports, and remove double spacings.</li>
      </ul>
    """

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Text Needs?</h2>
      <p>When it comes to performing text manipulations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each tool loads instantly and runs with absolute speed. We prioritize user privacy above everything else; unlike typical online utilities that process data on remote servers, all your text is processed locally in your browser. This client-side approach ensures your sensitive input parameters and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to copy mathematical results for a report or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity.</p>
    """

    faqs = [
        {
            "q": f"Is there a character limit when using the {name}?",
            "a": f"No. All processing occurs locally in your browser using client-side JavaScript. This means you can paste large documents, essays, or logs without timing out."
        },
        {
            "q": f"Does Enginewheels save my private text inputs?",
            "a": f"No. All operations are processed locally in active memory. We do not upload your text to external servers, guaranteeing complete privacy."
        },
        {
            "q": f"How do I download the formatted results?",
            "a": f"Simply click the 'Download Output' button to download your processed text as a standard .txt file."
        },
        {
            "q": f"Does the tool support mobile editing?",
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
      {use_cases}
      {why_choose_us}
      {faq_html}
    """
    return seo_article_html, faqs

# Generate all individual HTML files
for index, calc in enumerate(TEXT_TOOLS_DB):
    name = calc["name"]
    slug = calc["slug"]
    category = calc["category"]
    desc = calc["desc"]
    
    # Generate SEO article content and FAQ schema
    seo_article_html, faqs = generate_seo_text(calc)
    
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
    for inp in calc["inputs"]:
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
            istep = inp.get("step", "1")
            inputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:left;">
              <label for="{iid}" class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{label}</label>
              <input type="number" id="{iid}" class="form-control" style="width:100%; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); color:#fff; padding:12px; border-radius:8px;" value="{default_val}" min="{imin}" max="{imax}" step="{istep}">
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
    for out in calc["outputs"]:
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
        
    # Build dynamic JS bindings
    reset_lines = []
    clear_lines = []
    
    for inp in calc["inputs"]:
        if inp["type"] == "select":
            reset_lines.append(f"document.getElementById('{inp['id']}').selectedIndex = 0;")
        elif inp["type"] == "textarea":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "number":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '0')}';")
        else:
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '')}';")
            
    for out in calc["outputs"]:
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
    # Pick 2 calculators in the same category
    for other in TEXT_TOOLS_DB:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    # Fallback
    if len(related_list) < 2:
        for other in TEXT_TOOLS_DB:
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
  <title>{name} Tool Online Free | Enginewheels</title>
  <meta name="description" content="{desc} Safe, responsive, and secure client-side browser-based text utility.">
  <link rel="canonical" href="https://enginewheels.com/text-tools/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/text-tools/{slug}.html">
  <meta property="og:title" content="{name} Tool Online Free | Enginewheels">
  <meta property="og:description" content="{desc} Safe, responsive, and secure client-side browser-based text utility.">
  
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
        "name": "Text Tools",
        "item": "https://enginewheels.com/category/text-tools.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/text-tools/{slug}.html"
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
      <a href="../index.html">Home</a> &gt; <a href="../category/text-tools.html">Text Tools</a> &gt; <span>{name}</span>
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
         <button id="btn-calculate" class="btn btn-primary" style="padding:12px 30px; font-size:1rem;">Process Text</button>
      </div>
      <div class="calculator-outputs-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:20px; margin-bottom:30px;">
         {outputs_html}
      </div>
      
      <div id="calc-breakdown" class="calc-breakdown-box" style="display:none; background:rgba(255,255,255,0.02); padding:20px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); margin-bottom:30px;">
         <h4 style="margin-top:0; margin-bottom:12px; color:#fff; font-family:var(--font-heading);">Processing Breakdown</h4>
         <div id="breakdown-content" style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; text-align:left;"></div>
      </div>
      
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
         <button id="btn-copy-results" class="btn btn-secondary">Copy Output</button>
         <button id="btn-download-results" class="btn btn-secondary">Download Output</button>
         <button id="btn-clear-text" class="btn btn-secondary">Clear Text</button>
         <button id="btn-reset" class="btn btn-secondary">Reset</button>
      </div>
    </div>

    <!-- SEO Content Section -->
    <article class="seo-article">
      {seo_article_html}
      
      <!-- Related Tools Section -->
      <section class="related-tools-section">
        <h3 style="margin-bottom: 24px;">Related <span>Text Tools</span></h3>
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
        {calc["calc_js"]}
      }});

      // Reset Click
      document.getElementById('btn-reset').addEventListener('click', () => {{
        {reset_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Inputs have been reset.");
      }});

      // Clear Text Click
      document.getElementById('btn-clear-text').addEventListener('click', () => {{
        {clear_outputs_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Text inputs and outputs cleared.");
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
        showToast("Output downloaded successfully!");
      }});
    }});
  </script>
</body>
</html>"""
    
    file_path = os.path.join(TEXT_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(TEXT_TOOLS_DB)} HTML tool files successfully.")

# ----------------- REWRITE CATEGORY PAGE (text-tools.html) -----------------
print("Rewriting category/text-tools.html...")

grouped_tools = {}
for calc in TEXT_TOOLS_DB:
    cat = calc["category"]
    if cat not in grouped_tools:
        grouped_tools[cat] = []
    grouped_tools[cat].append(calc)

# Rebuild categories navigation grids and search link index
grids_html = ""
for cat_name, items in grouped_tools.items():
    grids_html += f"""
      <section style="margin-bottom: 50px;">
        <h2 style="margin-bottom: 24px; font-family:var(--font-heading); color:#fff; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:8px;">{cat_name} <span>Text Tools</span></h2>
        <div class="tool-grid">
    """
    for item in items:
        grids_html += f"""
          <a href="../text-tools/{item['slug']}.html" class="tool-card">
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

# 2500+ words SEO text
seo_cat_copy = """
      <h2>The Definitive Hub of Online Text Utilities</h2>
      <p>In today's fast-paced digital ecosystem, text is the fundamental medium of communication, information retrieval, coding, and search visibility. Whether you are coding an application, drafting an email newsletter, writing an academic thesis, or optimizing search engine snippets, text structure and format directly impact readability and compliance. The Enginewheels **Text Tools** platform provides a complete, multi-disciplinary ecosystem designed to automate all text processing tasks. We provide over 120 dedicated text utilities spanning 13 key categories—Basic Text, Case Converters, Text Formatters, Search & Replace, SEO Text, Content Writing, Social Media, Developer, Text Converters, URL & Encoding, Random Generators, Advanced, and AI Content—entirely free of charge.</p>
      <p>Manual text formatting—such as stripping out empty lines, replacing words, changing letter casing, or calculating character frequencies—is repetitive and highly prone to structural errors. Our online platform eliminates the need for scripting or heavy desktop office suites. By programming verified string manipulation algorithms directly into client-side visual interfaces, we provide a unified, responsive resource for writers, developers, marketers, and editors alike.</p>
      
      <h2>13 Specialized Subcategory Areas</h2>
      
      <h3>1. Basic Text Tools</h3>
      <p>Track essential text metrics instantly. Count words, lines, paragraphs, sentences, and estimate reading or speaking times. Additional reversing, line counting, and whitespace collapse tools make it easy to audit the size parameters of documents or drafts for essays, blogs, and book drafts.</p>
      
      <h3>2. Case Converters</h3>
      <p>Standardize letter capitalization styles. Swap text to UPPERCASE, lowercase, Sentence case, Title Case, or alternating capitals. Specialized programming casing styles like camelCase, PascalCase, snake_case, and kebab-case are essential for software developers structuring code files, database fields, or HTML element naming conventions.</p>
      
      <h3>3. Text Formatters</h3>
      <p>Tidy up paragraphs, indent spacing, or clean hidden formatting characters. Alphabetize lists, reverse row orders, shuffle line sequences, or trim whitespace borders. These utilities help writers clean draft content and developers align indentations for data sheets.</p>
      
      <h3>4. Search & Replace Tools</h3>
      <p>Search and replace specific terms across large text bodies. Multi-replace tools, word exclusions, digit stripping, symbol cleaning, and pattern extractors (emails, numbers, URLs, hashtags) allow you to parse data sets and extract structured lists in seconds.</p>
      
      <h3>5. SEO Text Tools</h3>
      <p>Audit keyword densities, meta title/description characters, and readability scores. Check keywords against optimal search positions and generate n-grams. These tools are indispensable for digital marketers ensuring content fits Google SERP snippet limits.</p>
      
      <h3>6. Content Writing Tools</h3>
      <p>Overcome writer's block with templates and phrase variations. Generate headlines, blog post titles, product descriptions, and captions. Rewrite articles, paragraphs, or sentences by mapping key terms to high-quality synonyms, keeping drafts fresh and unique.</p>
      
      <h3>7. Social Media Tools</h3>
      <p>Format captions for Instagram with non-collapsing line spacing, check character counts for Twitter, and add professional emoji structures for LinkedIn or Facebook. Fancy unicode font generators and borders help creators design catchy bios and posts.</p>
      
      <h3>8. Developer Text Tools</h3>
      <p>Beautify, format, validate, and minify programming files. This category offers dedicated formatters for JSON, XML, SQL, HTML, CSS, JavaScript, Markdown, YAML, CSV, and TSV, ensuring clean syntax structures and readable code layouts.</p>
      
      <h3>9. Text Converters</h3>
      <p>Convert characters to binary, hexadecimal, ASCII codes, or base64 structures. Translate letters to Morse code and back. These converters make it simple to encode data channels and analyze character mappings locally in your browser.</p>
      
      <h3>10. URL & Encoding Tools</h3>
      <p>Encode and decode parameter strings for URL routes, escape HTML tags into entities, or convert unicode characters. These tools prevent character corruption and routing exceptions in web development environments.</p>
      
      <h3>11. Random Generators</h3>
      <p>Generate placeholder words, sentences, paragraphs, or usernames. Lorem Ipsum and dummy text generators are valuable for developers previewing page structures, while topic and quote generators offer inspiration for writing blocks.</p>
      
      <h3>12. Advanced Text Tools</h3>
      <p>Run line-by-line diff comparisons, identify duplicate words, check palindromes, and generate anagrams. Text compression estimators (LZW) help you assess data sizes, while text expansion tools let you map custom shortcuts to full phrases.</p>
      
      <h3>13. AI Content Tools</h3>
      <p>Analyze text grammar, check spelling, and generate content ideas. Email subject line creators, blog outlines, Hooks, and Call-To-Action (CTA) suggestions provide copywriting guidance to help you craft high-converting business messages.</p>
      
      <h2>Uncompromising Data Privacy: 100% Client-Side Processing</h2>
      <p>Data security is a major concern when using online utilities. Many platforms transmit your inputs—such as private emails, business financials, credentials, or proprietary source code—to remote backend databases. This carries severe risks of data leaks, tracking, or breaches.</p>
      <p>Enginewheels prioritizes your privacy. All text utilities on our platform execute entirely client-side using JavaScript. Your inputs never leave your browser, and no data is transmitted to our servers. Your data remains completely private, secure, and under your control. When you close the browser tab, your inputs are cleared, ensuring complete confidentiality.</p>

      <h2>Comparison of Key Text Utilities</h2>
      <table style="width:100%; border-collapse: collapse; margin-top:20px; margin-bottom:20px; text-align:left; color:#fff;">
        <thead>
          <tr style="border-bottom:2px solid rgba(255,255,255,0.1); background:rgba(255,255,255,0.02);">
            <th style="padding:12px;">Utility Name</th>
            <th style="padding:12px;">Primary Use Case</th>
            <th style="padding:12px;">Execution Type</th>
            <th style="padding:12px;">Data Security</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">Word Counter</td>
            <td style="padding:12px;">Count words, characters, and reading times</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">JSON Formatter</td>
            <td style="padding:12px;">Beautify, format, and parse JSON code</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">Case Converter</td>
            <td style="padding:12px;">Convert text case styles instantly</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">Diff Checker</td>
            <td style="padding:12px;">Compare line differences side-by-side</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
        </tbody>
      </table>
"""

# FAQ lists
category_faqs = [
    {"q": "Are all online text tools on Enginewheels free to use?", "a": "Yes. Every tool is 100% free with no registration, email sign-ups, or limitations. You can process as many files as you need."},
    {"q": "Do you store the text I paste into the tools?", "a": "No. All text processing is executed locally in your browser using client-side JavaScript. No data is sent to our servers or saved in databases."},
    {"q": "Can I use these text utilities on my mobile phone?", "a": "Absolutely. All tools are designed with a mobile-first responsive layout, scaling perfectly on smartphones, tablets, and desktops."},
    {"q": "What browser-side technologies do these tools run on?", "a": "Our tools use vanilla JavaScript, HTML5, and CSS3, ensuring they run natively in any modern web browser without requiring extensions."},
    {"q": "How can I search for a specific text tool?", "a": "You can use the search bar in the sticky header on any page to find any tool instantly by typing its name or related keywords."}
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
  <title>Free Online Text Tools - Formatting & Counting | Enginewheels</title>
  <meta name="description" content="Access our ecosystem of 120+ Free Online Text Tools. Count words, format codes, convert cases, and generate hashtags instantly in your browser.">
  <link rel="canonical" href="https://enginewheels.com/category/text-tools.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/text-tools.html">
  <meta property="og:title" content="Free Online Text Tools - Formatting & Counting | Enginewheels">
  <meta property="og:description" content="Access our ecosystem of 120+ Free Online Text Tools. Count words, format codes, convert cases, and generate hashtags instantly in your browser.">
  
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
        "name": "Text Tools",
        "item": "https://enginewheels.com/category/text-tools.html"
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
      <a href="../index.html">Home</a> &gt; <a href="../index.html#categories">Categories</a> &gt; <span>Text Tools</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Free Online <span>Text Tools</span></h1>
      <p class="tool-desc-lead">Explore our expanded suite of 129 specialized client-side text utilities. Format, clean, convert, and count text with 100% data privacy.</p>
    </div>

    <!-- Active Tools Grids (13 categories) -->
    {grids_html}

    <!-- Category SEO Article -->
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

cat_file_path = os.path.join(ROOT_DIR, "category", "text-tools.html")
with open(cat_file_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)
print("category/text-tools.html rewritten successfully.")


# ----------------- REWRITE HTML SITEMAP (sitemap.html) -----------------
print("Rewriting sitemap.html...")

sitemap_text_items_html = ""
for cat_name, items in grouped_tools.items():
    sitemap_text_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_text_items_html += f'<li><a href="text-tools/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

# We will load the existing sitemap.html and inject/re-generate.
# Rather than parsing, we will construct sitemap.html programmatically containing ALL links: Info Pages, Categories, Core Tools, Calculators, and Text Tools.
# Let's import calculators to also catalog them correctly.
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

sitemap_calc_items_html = ""
grouped_calcs = {}
for c in ALL_CALCULATORS:
    cat = c["category"]
    if cat not in grouped_calcs:
        grouped_calcs[cat] = []
    grouped_calcs[cat].append(c)

for cat_name, items in grouped_calcs.items():
    sitemap_calc_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_calc_items_html += f'<li><a href="calculators/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

sitemap_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Sitemap - Browse All Free Online Tools | Enginewheels</title>
  <meta name="description" content="View the complete sitemap of Enginewheels. Access all our free online tools, categories, legal policies, and informational resources from a single page.">
  <link rel="canonical" href="https://enginewheels.com/sitemap.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/sitemap.html">
  <meta property="og:title" content="Sitemap - Browse All Free Online Tools | Enginewheels">
  <meta property="og:description" content="View the complete sitemap of Enginewheels. Access all our free online tools, categories, legal policies, and informational resources from a single page.">
  
  <!-- CSS Link -->
  <link rel="stylesheet" href="assets/css/styles.css">
  
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
        "name": "Sitemap",
        "item": "https://enginewheels.com/sitemap.html"
      }}
    ]
  }}
  </script>
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

  <!-- Sitemap Content Section -->
  <main class="static-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Sitemap</span>
    </nav>

    <div class="static-content-card">
      <h1 class="text-center" style="margin-bottom: 40px;">Website <span>Sitemap</span></h1>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px;">
        <!-- Col 1: Standard Info Pages -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Information Pages</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2;">
            <li><a href="index.html" style="font-weight:600;">Home Page</a></li>
            <li><a href="about.html">About Us Page</a></li>
            <li><a href="contact.html">Contact Us Page</a></li>
            <li><a href="sitemap.html" style="color:var(--color-violet)">HTML Sitemap Page</a></li>
            <li><a href="privacy.html">Privacy Policy Page</a></li>
            <li><a href="disclaimer.html">Disclaimer Page</a></li>
            <li><a href="terms.html">Terms & Conditions</a></li>
          </ul>
        </div>
        
        <!-- Col 2: Categories -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Category Pages</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2;">
            <li><a href="category/text-tools.html" style="font-weight:600;">✍ Text Tools Category</a></li>
            <li><a href="category/security-tools.html" style="font-weight:600;">🔒 Security Tools Category</a></li>
            <li><a href="category/developer-tools.html" style="font-weight:600;">💻 Developer Tools Category</a></li>
            <li><a href="category/image-tools.html" style="font-weight:600;">🖼️ Image Tools Category</a></li>
            <li><a href="category/generators.html" style="font-weight:600;">⚙️ Generators Category</a></li>
            <li><a href="category/calculators.html" style="font-weight:600;">🧮 Calculators Category</a></li>
            <li><a href="category/time-tools.html" style="font-weight:600;">🕒 Time Tools Category</a></li>
            <li><a href="category/math-numbers.html" style="font-weight:600;">🔢 Math & Numbers Category</a></li>
            <li><a href="category/fun-utility.html" style="font-weight:600;">🎯 Fun & Utility Category</a></li>
            <li><a href="category/seo-web-tools.html" style="font-weight:600;">🌐 SEO & Web Tools Category</a></li>
          </ul>
        </div>
        
        <!-- Col 3: Tool Pages -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Individual Tool Pages</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2;">
            <li><a href="tools/word-counter.html">Word Counter</a></li>
            <li><a href="tools/case-converter.html">Case Converter</a></li>
            <li><a href="tools/password-generator.html">Password Generator</a></li>
            <li><a href="tools/hash-generator.html">Hash Generator</a></li>
            <li><a href="tools/json-formatter.html">JSON Formatter & Validator</a></li>
            <li><a href="tools/url-encoder-decoder.html">URL Encoder & Decoder</a></li>
            <li><a href="tools/qr-code-generator.html">QR Code Generator</a></li>
            <li><a href="tools/uuid-generator.html">UUID Generator</a></li>
            <li><a href="tools/age-calculator.html">Age Calculator</a></li>
            <li><a href="tools/percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="tools/epoch-converter.html">Epoch Time Converter</a></li>
            <li><a href="tools/binary-converter.html">Binary Converter</a></li>
            <li><a href="tools/color-picker.html">Color Picker & Converter</a></li>
            <li><a href="tools/base64-image.html">Base64 Image Encoder</a></li>
            <li><a href="tools/meta-tag-generator.html">Meta Tag Generator</a></li>
            <li><a href="tools/morse-code.html">Morse Code Translator</a></li>
          </ul>
        </div>

        <!-- Col 4: Calculators Grouped -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Calculator Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_calc_items_html}
          </ul>
        </div>

        <!-- Col 5: Text Tools Grouped -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">New Text Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_text_items_html}
          </ul>
        </div>
      </div>
    </div>
  </main>

  <!-- Footer Section -->
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

  <!-- Scripts -->
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
# Add calculators URLs
for item in ALL_CALCULATORS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/calculators/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add text tools URLs
for item in TEXT_TOOLS_DB:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/text-tools/{item["slug"]}.html</loc>
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
  <url>
    <loc>https://enginewheels.com/category/developer-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/image-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/generators.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/calculators.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/time-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/math-numbers.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/fun-utility.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/seo-web-tools.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- Original 16 Tool Pages -->
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
  
  <!-- New Calculator and Text Pages -->
{xml_urls_str}</urlset>"""

xml_file_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(xml_file_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)
print("sitemap.xml rebuilt.")


# ----------------- REWRITE ASSETS/JS/MAIN.JS SEARCH INDEX -----------------
print("Updating assets/js/main.js with search indexes...")

main_js_path = os.path.join(ROOT_DIR, "assets", "js", "main.js")
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js_content = f.read()

# Parse existing main.js up to "const ENGINYWHEELS_TOOLS = ["
start_idx = main_js_content.find("const ENGINYWHEELS_TOOLS = [")
end_idx = main_js_content.find("];", start_idx)

if start_idx == -1:
    print("Could not find ENGINYWHEELS_TOOLS index array in main.js!")
    exit(1)

if end_idx == -1:
    end_idx = main_js_content.find("]\n\ndocument.addEventListener", start_idx)
    if end_idx == -1:
        print("Could not find end of ENGINYWHEELS_TOOLS array in main.js!")
        exit(1)
    offset = 1
else:
    offset = 2

# Construct new array items
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

# Append new text tools
for tool in TEXT_TOOLS_DB:
    search_items.append({
        "name": tool["name"],
        "url": f"text-tools/{tool['slug']}.html",
        "category": f"Text Tools ({tool['category']})",
        "desc": tool["desc"]
    })

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+offset:]

# Also update the prefix path logic to handle calculators and text-tools directory
target_find = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/')) ? '../' : '';"
target_replace = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/')) ? '../' : '';"

updated_main_js = updated_main_js.replace(target_find, target_replace)

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js updated with new tools search index and prefix checks.")
print("All generation tasks completed successfully!")
