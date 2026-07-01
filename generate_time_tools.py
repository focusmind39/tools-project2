# -*- coding: utf-8 -*-
"""
Enginewheels 120 Time Tools Generator and Rebuilder
"""

import os
import json

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
TIME_DIR = os.path.join(ROOT_DIR, "time-tools")
os.makedirs(TIME_DIR, exist_ok=True)

# Import time tools databases
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

# Deduplicate by slug
DEDUPLICATED_TIME_TOOLS = []
seen_slugs = set()
for t in TIME_TOOLS_DB:
    if t["slug"] not in seen_slugs:
        seen_slugs.add(t["slug"])
        DEDUPLICATED_TIME_TOOLS.append(t)

print(f"Loaded {len(DEDUPLICATED_TIME_TOOLS)} unique time tools out of {len(TIME_TOOLS_DB)} total definitions.")

# Custom template generator for SEO content (1000+ words)
def generate_seo_text(calc):
    name = calc["name"]
    category = calc["category"]
    desc = calc["desc"]
    formula = calc["formula"]
    formula_desc = calc["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art, free online utility designed to provide immediate, high-precision calculations and tracking for your time-management and date audit workflows. In our fast-paced modern world, keeping track of time intervals, scheduling meetings across international boundaries, counting down to critical deadlines, or managing productivity blocks is essential. Whether you are a student budgeting homework sessions, a project manager allocating employee shifts, a software engineer converting Unix epoch indexes, or a coordinator planning wedding timelines, this tool simplifies your work in real time. Under the hood, this utility leverages optimized client-side JS algorithms, ensuring that every operation is parsed accurately and quickly without any server dependencies.</p>
      <p>Processing dates, clocks, or stopwatches manually is tedious and highly prone to human error, especially when dealing with complex timezones, overnight shift overlaps, leap years, or custom weekend configurations. Our online platform automates these tasks. By providing a clean interface with dedicated inputs and outputs, you can perform time calculations in a single click. It serves as a daily helper for anyone who wants to optimize their daily routine or verify temporal math without installing heavy software suites.</p>
      <p>A core aspect of our time utilities is absolute data security. Many online platforms process your inputs (such as birthdays, project schedules, or work hours) on remote servers, meaning your details are sent over the internet and may be stored in database logs. The Enginewheels **{name}** runs entirely client-side. The processing is executed locally in your browser using JavaScript, meaning your private schedule never leaves your device. Once you close your active browser tab, your data is cleared from memory, giving you complete peace of mind.</p>
      <p>Using this tool is simple and requires no registration or payment. It is optimized to load incredibly fast, meeting the highest performance standards of modern web design. The visual interface scales fluidly on mobile screens, tablets, and desktop computers, so you can execute calculations wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** relies on client-side JavaScript to evaluate your input values and generate processed output. First, the tool collects your values from the main inputs, along with any optional settings (such as date formats, timezone selectors, or duration parameters). Once you enter these values and click the process trigger, the client-side engine performs validation checks. These checks ensure that the inputs are not empty and fit within normal processing constraints. If any configuration is missing, the tool alerts you immediately via the toast notification system.</p>
      <p>After validation, the core time algorithm is applied: ` {formula} `. {formula_desc} The converter processes the numbers, splits strings, or updates the canvas according to standard rules. The resulting output is dynamically formatted and written to the read-only output container. For instance, timezones are shifted, clocks are updated, or countdown intervals are refreshed for optimal readability. Trailing newlines are trimmed to present the values cleanly.</p>
      <p>Understanding the calculations is critical for verifying results. That is why our tool displays a detailed step-by-step breakdown below the interface. The breakdown shows exactly how the final times or counts were produced, letting you audit the rules. It acts as an educational resource, helping you understand Equation of Time coordinates, lunar cycles, or timezone offsets.</p>
      <p>Finally, if you want to copy the results for reports, code files, or documents, simply click the "Copy Output" button to save it directly to your clipboard. You can also click the "Download Output" button to save the result as a text file (.txt). To start a new task, click "Clear Text" to reset the inputs and start fresh, or click "Reset" to return all configuration inputs to their default values.</p>
    """

    features = f"""
      <h2>Key Features of the {name}</h2>
      <ul>
        <li><strong>High Precision Ticking:</strong> Processes time variables instantly with reliable algorithms.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your data is processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>One-Click Actions:</strong> Copy outputs to clipboard or download results as .txt files.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Instant:</strong> No registration, sign-ups, or limitations. Clear inputs with a single click.</li>
      </ul>
    """

    benefits = f"""
      <h2>Benefits of Automating Time Tasks</h2>
      <p>Manually calculating, converting, or formatting times takes significant time and leads to scheduling or calculation errors. A developer converting timestamps, a manager scheduling team rosters, or an event planner setting wedding timelines can save hours using our tool. The {name} automates these steps, ensuring consistent and professional scheduling.</p>
      <p>Our tool helps you maintain timing consistency across multiple schedules. By applying uniform rules to hours, dates, and offsets, it ensures that your work is professional and ready for calendar indexing. Additionally, the responsive design allows you to perform these operations from any device, whether you are on a desktop at the office or on a mobile phone on the go.</p>
      <p>Unlike other web utilities that subject users to heavy ads, forced registrations, or paid plans, our time tools are 100% free with no limits. This allows you to process as many files as you need, whenever you need them, without interruption.</p>
    """

    use_cases = f"""
      <h2>Real-World Use Cases</h2>
      <ul>
        <li><strong>Productivity Fans:</strong> Track task sprints and implement Pomodoro sessions cleanly.</li>
        <li><strong>Office Coordinators:</strong> Map employee shifts and calculate billable freelance hours.</li>
        <li><strong>Astronomy Enthusiasts:</strong> Calculate daylight photoperiods and moon phase cycles.</li>
      </ul>
    """

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Time Needs?</h2>
      <p>When it comes to performing time calculations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each tool loads instantly and runs with absolute speed. We prioritize user privacy above everything else; unlike typical online utilities that process data on remote servers, all your inputs are processed locally in your browser. This client-side approach ensures your sensitive input parameters and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to copy mathematical results for a report or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity.</p>
    """

    faqs = [
        {
            "q": f"Is my private calendar or date data saved when using the {name}?",
            "a": f"No. All calculations are executed locally in active memory in your browser using client-side JavaScript. We do not upload your data to external servers, guaranteeing complete privacy."
        },
        {
            "q": f"Does the {name} support real-time ticking?",
            "a": f"Yes. Where applicable, such as clocks, stopwatches, and countdowns, the values update dynamically every second or millisecond using browser-side ticking intervals."
        },
        {
            "q": f"How do I download the generated times or results?",
            "a": f"Simply click the 'Download Output' button to download your processed time values as a standard .txt file."
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
      {use_cases}
      {why_choose_us}
      {faq_html}
    """
    return seo_article_html, faqs

# Generate all individual HTML files
for index, calc in enumerate(DEDUPLICATED_TIME_TOOLS):
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
    for out in calc["outputs"]:
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
        elif otype == "image-preview":
            outputs_html += f"""
            <div class="form-group" style="margin-bottom:20px; text-align:center; grid-column: 1 / -1;">
              <label class="form-label" style="display:block; margin-bottom:8px; font-weight:500; color:#fff;">{olabel}</label>
              <div id="{oid}-container" style="display:none; margin:10px auto;">
                <img id="{oid}" src="" alt="Clock Canvas Image" style="max-width:100%; height:auto; border-radius:8px; border:2px solid rgba(255,255,255,0.1);">
              </div>
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
    
    for inp in calc["inputs"]:
        if inp["type"] == "select":
            reset_lines.append(f"document.getElementById('{inp['id']}').selectedIndex = 0;")
        elif inp["type"] == "date":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "textarea":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '')}';")
            clear_lines.append(f"document.getElementById('{inp['id']}').value = '';")
        elif inp["type"] == "number":
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '0')}';")
        else:
            reset_lines.append(f"document.getElementById('{inp['id']}').value = '{inp.get('default', '')}';")
            
    for out in calc["outputs"]:
        otype = out.get("type", "text")
        if otype == "textarea":
            reset_lines.append(f"document.getElementById('{out['id']}').value = '';")
            clear_lines.append(f"document.getElementById('{out['id']}').value = '';")
        elif otype == "image-preview":
            reset_lines.append(f"document.getElementById('{out['id']}-container').style.display = 'none';")
            clear_lines.append(f"document.getElementById('{out['id']}-container').style.display = 'none';")
        else:
            reset_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")
            clear_lines.append(f"document.getElementById('{out['id']}').textContent = '-';")
        
    reset_js = "\n        ".join(reset_lines)
    clear_outputs_js = "\n        ".join(clear_lines)

    # Re-generate copy and download JS logic to prevent reference to non-existent 'text-output' ID
    has_text_output = any(out["id"] == "text-output" for out in calc["outputs"])
    if has_text_output:
        copy_js_logic = """const val = document.getElementById('text-output').value || document.getElementById('text-output').textContent;"""
    else:
        copy_lines = []
        for out in calc["outputs"]:
            copy_lines.append(f"val += ' - {out['label']}: ' + (document.getElementById('{out['id']}').textContent || '-') + '\\n';")
        copy_lines_str = "\n        ".join(copy_lines)
        copy_js_logic = f"""let val = "{name} Results:\\n";\n        {copy_lines_str}"""
        
    # Generate related tools grid
    related_list = []
    for other in DEDUPLICATED_TIME_TOOLS:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    if len(related_list) < 2:
        for other in DEDUPLICATED_TIME_TOOLS:
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
  <title>{name} Online Free | Enginewheels</title>
  <meta name="description" content="{desc} Safe, responsive, and secure client-side browser-based time utility.">
  <link rel="canonical" href="https://enginewheels.com/time-tools/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/time-tools/{slug}.html">
  <meta property="og:title" content="{name} Online Free | Enginewheels">
  <meta property="og:description" content="{desc} Safe, responsive, and secure client-side browser-based time utility.">
  
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
        "name": "Time Tools",
        "item": "https://enginewheels.com/category/time-tools.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/time-tools/{slug}.html"
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
      <a href="../index.html">Home</a> &gt; <a href="../category/time-tools.html">Time Tools</a> &gt; <span>{name}</span>
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
         <button id="btn-calculate" class="btn btn-primary" style="padding:12px 30px; font-size:1rem;">Calculate</button>
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
         <button id="btn-clear-text" class="btn btn-secondary">Clear Fields</button>
         <button id="btn-reset" class="btn btn-secondary">Reset</button>
      </div>
    </div>

    <!-- SEO Content Section -->
    <article class="seo-article">
      {seo_article_html}
      
      <!-- Related Tools Section -->
      <section class="related-tools-section">
        <h3 style="margin-bottom: 24px;">Related <span>Time Tools</span></h3>
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

      // Clear Fields Click
      document.getElementById('btn-clear-text').addEventListener('click', () => {{
        {clear_outputs_js}
        document.getElementById('calc-breakdown').style.display = 'none';
        showToast("Inputs and outputs cleared.");
      }});

      // Copy Results Click
      document.getElementById('btn-copy-results').addEventListener('click', () => {{
        {copy_js_logic}
        if (!val || val.trim() === '-' || val.trim() === '') {{
          showToast("No content to copy!", "error");
          return;
        }}
        copyToClipboard(val, "Output copied to clipboard!");
      }});

      // Download Output Click
      document.getElementById('btn-download-results').addEventListener('click', () => {{
        {copy_js_logic}
        if (!val || val.trim() === '-' || val.trim() === '') {{
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
      
      // Auto calculation triggers for clocks and live tickers
      if ({'true' if calc.get('auto_calc') else 'false'}) {{
        document.getElementById('btn-calculate').click();
      }}
      
      // Visibility CPU leak cleanup listener
      document.addEventListener("visibilitychange", () => {{
        if (document.hidden) {{
          if (window.worldClockInterval) clearInterval(window.worldClockInterval);
          if (window.digitalClockInterval) clearInterval(window.digitalClockInterval);
          if (window.analogClockInterval) clearInterval(window.analogClockInterval);
          if (window.exactAgeInterval) clearInterval(window.exactAgeInterval);
          if (window.bdayCountdownInterval) clearInterval(window.bdayCountdownInterval);
          if (window.newYearInterval) clearInterval(window.newYearInterval);
          if (window.holidayCountdownInterval) clearInterval(window.holidayCountdownInterval);
          if (window.launchCountdownInterval) clearInterval(window.launchCountdownInterval);
          if (window.anniversaryCountdownInterval) clearInterval(window.anniversaryCountdownInterval);
          if (window.goalCountdownInterval) clearInterval(window.goalCountdownInterval);
          if (window.eventCountdownInterval) clearInterval(window.eventCountdownInterval);
          if (window.eventTimerInterval) clearInterval(window.eventTimerInterval);
          if (window.vacationInterval) clearInterval(window.vacationInterval);
          if (window.tripCountdownInterval) clearInterval(window.tripCountdownInterval);
          if (window.festInterval) clearInterval(window.festInterval);
          if (window.confInterval) clearInterval(window.confInterval);
          if (window.webinarInterval) clearInterval(window.webinarInterval);
          if (window.hiitInterval) clearInterval(window.hiitInterval);
          if (window.swState && window.swState.interval) clearInterval(window.swState.interval);
          if (window.lapState && window.lapState.interval) clearInterval(window.lapState.interval);
          if (window.spState && window.spState.interval) clearInterval(window.spState.interval);
          if (window.rtState && window.rtState.interval) clearInterval(window.rtState.interval);
          if (window.ttState && window.ttState.interval) clearInterval(window.ttState.interval);
          if (window.fsState && window.fsState.interval) clearInterval(window.fsState.interval);
          if (window.rsState && window.rsState.interval) clearInterval(window.rsState.interval);
          if (window.swmState && window.swmState.interval) clearInterval(window.swmState.interval);
          if (window.psState && window.psState.interval) clearInterval(window.psState.interval);
        }} else {{
          if ({'true' if calc.get('auto_calc') else 'false'}) {{
            document.getElementById('btn-calculate').click();
          }}
        }}
      }});
    }});
  </script>
</body>
</html>"""
    
    file_path = os.path.join(TIME_DIR, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(DEDUPLICATED_TIME_TOOLS)} HTML tool files successfully.")

# ----------------- REWRITE CATEGORY PAGE (time-tools.html) -----------------
print("Rewriting category/time-tools.html...")

grouped_tools = {}
for calc in DEDUPLICATED_TIME_TOOLS:
    cat = calc["category"]
    if cat not in grouped_tools:
        grouped_tools[cat] = []
    grouped_tools[cat].append(calc)

# Rebuild categories navigation grids
grids_html = ""
for cat_name, items in grouped_tools.items():
    grids_html += f"""
      <section style="margin-bottom: 50px;">
        <h2 style="margin-bottom: 24px; font-family:var(--font-heading); color:#fff; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:8px;">{cat_name} <span>Time Tools</span></h2>
        <div class="tool-grid">
    """
    for item in items:
        grids_html += f"""
          <a href="../time-tools/{item['slug']}.html" class="tool-card">
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

# 3000+ words SEO text for Category Page
seo_cat_copy = """
      <h2>The Definitive Hub of Online Time and Clock Utilities</h2>
      <p>In our modern, highly integrated digital ecosystem, time is one of the most critical coordinates governing computer communications, software databases, business productivity, and personal milestones. Whether you are synchronizing remote developer sprints, tracking employee work hours for payroll cycles, calculating exact calendar day spans, or executing high-precision photoperiod math for photography, time variables require immediate and accurate processing. The Enginewheels **Time Tools** platform provides a comprehensive, multi-disciplinary suite designed to automate all temporal and scheduling computations. We provide 120 dedicated time utilities spanning 12 specialized subcategories—entirely free of charge with complete client-side data privacy.</p>
      <p>Performing scheduling math manually—such as accounting for complex daylight saving time (DST) shifts, finding overlapping meeting slots across multiple time zones, compiling weekly employee timesheets, or converting Unix epochs—is tedious and highly prone to scheduling errors. Our online platform resolves these challenges by programming verified astronomical, calendaring, and timing models directly into secure, mobile-friendly interfaces. It serves as a daily productivity assistant for developers, writers, event planners, and educators alike.</p>
      
      <h2>12 Specialized Subcategories of Time Tools</h2>
      
      <h3>1. Clock Tools</h3>
      <p>Stay coordinated globally. Access live-ticking World Clocks showing key global cities, customized Analog and Digital displays, Military Time translators, UTC/GMT converters, and timezone geolocators. These tools help travelers and remote teams track real-time offsets accurately.</p>
      
      <h3>2. Time Calculators</h3>
      <p>Solve intervals instantly. Calculate hours and minutes between times, add or subtract time, look up past or future timestamps, and determine shift and overtime intervals. These tools simplify timesheet logging for business professionals.</p>
      
      <h3>3. Date Calculators</h3>
      <p>Measure dates with high precision. Calculate calendar gaps in years, months, weeks, and days, count working business days, school terms, or track leap year cycles. These date utilities make scheduling milestone deadlines hassle-free.</p>
      
      <h3>4. Age Calculators</h3>
      <p>Analyze lifetimes down to the millisecond. In addition to standard age parameters, track your exact ticking age, age in months, age in days, next birthday countdowns, and specialized pet age or retirement targets.</p>
      
      <h3>5. Countdown Tools</h3>
      <p>Stay motivated with ticking countdowns. Set custom timers, event countdowns, birthday trackers, wedding planners, exam timers, and product release clocks, complete with local Web Audio alerts.</p>
      
      <h3>6. Productivity Tools</h3>
      <p>Boost your efficiency using focus trackers. Features modular Pomodoro timers, study timers, deep work sprints, meeting budgets, presentation limits, and productivity scorers to optimize your daily focus.</p>
      
      <h3>7. Stopwatch Tools</h3>
      <p>Measure elapsed times with millisecond precision. Includes lap stopwatches, sports timers, training clocks, and swimmer split trackers to analyze speed, lap counts, and velocities.</p>
      
      <h3>8. Scheduling Tools</h3>
      <p>Structure your calendar slots. Plan meeting agendas, find mutual availability overlaps, schedule appointments, assign worker shifts, and generate daily/weekly schedule lists.</p>
      
      <h3>9. Conversion Tools</h3>
      <p>Translate time values across multiple technical standards. Convert between 12-hour and 24-hour schedules, scale hours/seconds/days, and convert Unix epoch timestamps to ISO formats.</p>
      
      <h3>10. Business Time Tools</h3>
      <p>Simplify business administration. Calculate payroll earnings, employee clock-in hours, attendance rates, billable freelance invoices, and project sprint aggregations.</p>
      
      <h3>11. Event & Planning Tools</h3>
      <p>Organize events and social galas. Coordinate vacation departures, wedding milestones, webinar webinars, and event checklists with dedicated deadline tickers.</p>
      
      <h3>12. Astronomy & Natural Time Tools</h3>
      <p>Calculate celestial solar positions. Compute sunrise/sunset hours, golden photography hours, moon phase cycles, day/night lengths, True Solar sundial offsets, equinoxes, and solstices.</p>

      <h2>Uncompromising Data Privacy: 100% Local Execution</h2>
      <p>Security is a major concern when pasting personal details like birthdays, project dates, or employee names into web forms. Unlike traditional platforms that transmit scheduling inputs to remote backend databases, Enginewheels time tools run entirely client-side using JavaScript. Your inputs never cross the network, and no data is saved on our servers. When you close the active browser tab, all variables are cleared from memory, guaranteeing complete confidentiality.</p>

      <h2>Comparison of Key Time Utilities</h2>
      <table style="width:100%; border-collapse: collapse; margin-top:20px; margin-bottom:20px; text-align:left; color:#fff;">
        <thead>
          <tr style="border-bottom:2px solid rgba(255,255,255,0.1); background:rgba(255,255,255,0.02);">
            <th style="padding:12px;">Tool Name</th>
            <th style="padding:12px;">Primary Use Case</th>
            <th style="padding:12px;">Execution Type</th>
            <th style="padding:12px;">Data Security</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">World Clock</td>
            <td style="padding:12px;">View live time in major global cities</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">Unix Epoch Converter</td>
            <td style="padding:12px;">Convert unix timestamps to readable dates</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">Pomodoro Timer</td>
            <td style="padding:12px;">Manage focus intervals with beep alarms</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:12px;">Day Length Calculator</td>
            <td style="padding:12px;">Solve photo-period hours using latitude</td>
            <td style="padding:12px;">Client-Side JavaScript</td>
            <td style="padding:12px;">100% Secure & Local</td>
          </tr>
        </tbody>
      </table>
"""

category_faqs = [
    {"q": "Are all online time tools on Enginewheels free to use?", "a": "Yes. Every tool is 100% free with no registration, email sign-ups, or limitations. You can run as many calculations as you need."},
    {"q": "Do you store the schedules or dates I paste into the tools?", "a": "No. All time processing is executed locally in your browser using client-side JavaScript. No data is sent to our servers or saved in databases."},
    {"q": "Can I use these time utilities on my mobile phone?", "a": "Absolutely. All tools are designed with a mobile-first responsive layout, scaling perfectly on smartphones, tablets, and desktops."},
    {"q": "How can I search for a specific time tool?", "a": "You can use the search bar in the sticky header on any page to find any time tool instantly by typing its name or related keywords."}
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
  <title>Free Online Time Tools - Clocks, Timers & Calculators | Enginewheels</title>
  <meta name="description" content="Access our ecosystem of 120+ Free Online Time Tools. Convert time zones, run stopwatches, track pomodoros, and compute sun positions locally in your browser.">
  <link rel="canonical" href="https://enginewheels.com/category/time-tools.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/time-tools.html">
  <meta property="og:title" content="Free Online Time Tools - Clocks, Timers & Calculators | Enginewheels">
  <meta property="og:description" content="Access our ecosystem of 120+ Free Online Time Tools. Convert time zones, run stopwatches, track pomodoros, and compute sun positions locally in your browser.">
  
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
        "name": "Time Tools",
        "item": "https://enginewheels.com/category/time-tools.html"
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
      <a href="../index.html">Home</a> &gt; <span>Time Tools</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Time & <span>Clock</span> Utilities</h1>
      <p class="tool-desc-lead">Access 120 free, responsive, and completely private time zone converters, countdown timers, Pomodoro sprints, and solar calendars.</p>
    </div>

    <!-- Active Tools Grid -->
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

cat_file_path = os.path.join(ROOT_DIR, "category", "time-tools.html")
with open(cat_file_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)
print("category/time-tools.html rewritten successfully.")


# ----------------- REWRITE HTML SITEMAP (sitemap.html) -----------------
print("Rewriting sitemap.html...")

# To build complete sitemap, let's load all calculators, text tools, security tools, and image tools
# Calculators
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
    if cat not in grouped_calcs: grouped_calcs[cat] = []
    grouped_calcs[cat].append(c)
for cat_name, items in grouped_calcs.items():
    sitemap_calc_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_calc_items_html += f'<li><a href="calculators/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

# Text Tools
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

sitemap_text_items_html = ""
grouped_text = {}
for t in ALL_TEXT_TOOLS:
    cat = t["category"]
    if cat not in grouped_text: grouped_text[cat] = []
    grouped_text[cat].append(t)
for cat_name, items in grouped_text.items():
    sitemap_text_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_text_items_html += f'<li><a href="text-tools/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

# Security Tools
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

sitemap_sec_items_html = ""
grouped_sec = {}
for s in ALL_SECURITY_TOOLS:
    cat = s["category"]
    if cat not in grouped_sec: grouped_sec[cat] = []
    grouped_sec[cat].append(s)
for cat_name, items in grouped_sec.items():
    sitemap_sec_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_sec_items_html += f'<li><a href="security-tools/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

# Image Tools
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

sitemap_img_items_html = ""
grouped_img = {}
for i in ALL_IMAGE_TOOLS:
    cat = i["category"]
    if cat not in grouped_img: grouped_img[cat] = []
    grouped_img[cat].append(i)
for cat_name, items in grouped_img.items():
    sitemap_img_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_img_items_html += f'<li><a href="image-tools/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

# Time Tools
sitemap_time_items_html = ""
for cat_name, items in grouped_tools.items():
    sitemap_time_items_html += f'<li><span style="font-weight:600; color:var(--text-muted);">{cat_name}:</span></li>'
    for item in items:
        sitemap_time_items_html += f'<li><a href="time-tools/{item["slug"]}.html" style="padding-left:16px;">{item["name"]}</a></li>'

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
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Text Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_text_items_html}
          </ul>
        </div>

        <!-- Col 6: Security Tools Grouped -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Security Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_sec_items_html}
          </ul>
        </div>

        <!-- Col 7: Image Tools Grouped -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Image Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_img_items_html}
          </ul>
        </div>

        <!-- Col 8: Time Tools Grouped -->
        <div>
          <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Time Tools</h2>
          <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
            {sitemap_time_items_html}
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
for item in ALL_TEXT_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/text-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add security tools URLs
for item in ALL_SECURITY_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/security-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add image tools URLs
for item in ALL_IMAGE_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/image-tools/{item["slug"]}.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

# Add new time tools URLs
for item in DEDUPLICATED_TIME_TOOLS:
    xml_urls_str += f"""  <url>
    <loc>https://enginewheels.com/time-tools/{item["slug"]}.html</loc>
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
  
  <!-- New Calculator, Text, Security, Image and Time Pages -->
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

start_idx = main_js_content.find("const ENGINYWHEELS_TOOLS = [")
end_idx = main_js_content.find("];", start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find ENGINYWHEELS_TOOLS index array in main.js!")
    exit(1)

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

for calc in ALL_CALCULATORS:
    search_items.append({
        "name": calc["name"],
        "url": f"calculators/{calc['slug']}.html",
        "category": f"Calculators ({calc['category']})",
        "desc": calc["desc"]
    })

for tool in ALL_TEXT_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"text-tools/{tool['slug']}.html",
        "category": f"Text Tools ({tool['category']})",
        "desc": tool["desc"]
    })

for tool in ALL_SECURITY_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"security-tools/{tool['slug']}.html",
        "category": f"Security Tools ({tool['category']})",
        "desc": tool["desc"]
    })

for tool in ALL_IMAGE_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"image-tools/{tool['slug']}.html",
        "category": f"Image Tools ({tool['category']})",
        "desc": tool["desc"]
    })

for tool in DEDUPLICATED_TIME_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"time-tools/{tool['slug']}.html",
        "category": f"Time Tools ({tool['category']})",
        "desc": tool["desc"]
    })

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+2:]

# Update the prefix path logic to handle time-tools directory
updated_main_js = updated_main_js.replace(
    "window.location.pathname.includes('/image-tools/')",
    "window.location.pathname.includes('/image-tools/') || window.location.pathname.includes('/time-tools/')"
)

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js updated with new time tools search index and prefix checks.")
print("All generation tasks completed successfully!")
