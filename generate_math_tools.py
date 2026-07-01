# -*- coding: utf-8 -*-
"""
Enginewheels Math & Numbers Tools Generator and Rebuilder
"""

import os
import json
import re

ROOT_DIR = r"c:\Users\Manorama Salunkhe\Downloads\Enginewheels tools"
MATH_DIR = os.path.join(ROOT_DIR, "math-tools")
os.makedirs(MATH_DIR, exist_ok=True)

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

# Import generator tools
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

# Import SEO & Web Tools
from data_seo_analysis_meta import SEO_ANALYSIS_TOOLS
from data_seo_schema_webmaster import SCHEMA_WEBMASTER_TOOLS
from data_seo_content_links import CONTENT_LINKS_TOOLS
from data_seo_social_perf import SOCIAL_PERF_TOOLS
from data_seo_domain_marketing import DOMAIN_MARKETING_TOOLS
from data_seo_google_local_ai import GOOGLE_LOCAL_AI_TOOLS

ALL_SEO_TOOLS = []
ALL_SEO_TOOLS.extend(SEO_ANALYSIS_TOOLS)
ALL_SEO_TOOLS.extend(SCHEMA_WEBMASTER_TOOLS)
ALL_SEO_TOOLS.extend(CONTENT_LINKS_TOOLS)
ALL_SEO_TOOLS.extend(SOCIAL_PERF_TOOLS)
ALL_SEO_TOOLS.extend(DOMAIN_MARKETING_TOOLS)
ALL_SEO_TOOLS.extend(GOOGLE_LOCAL_AI_TOOLS)

DEDUPLICATED_SEO_TOOLS = []
seen_seo_slugs = set()
for tool in ALL_SEO_TOOLS:
    if tool["slug"] not in seen_seo_slugs:
        seen_seo_slugs.add(tool["slug"])
        DEDUPLICATED_SEO_TOOLS.append(tool)

# Import Math & Numbers tools
from data_math_basic_numbers import BASIC_MATH_TOOLS
from data_math_algebra_geometry import ALGEBRA_GEOMETRY_TOOLS
from data_math_trig_stats import TRIG_STATS_TOOLS
from data_math_advanced_financial import ADVANCED_FINANCIAL_TOOLS
from data_math_converters_engineering import CONVERTERS_ENGINEERING_TOOLS
from data_math_education_random_gen import EDUCATION_RANDOM_GEN_TOOLS

ALL_MATH_TOOLS = []
ALL_MATH_TOOLS.extend(BASIC_MATH_TOOLS)
ALL_MATH_TOOLS.extend(ALGEBRA_GEOMETRY_TOOLS)
ALL_MATH_TOOLS.extend(TRIG_STATS_TOOLS)
ALL_MATH_TOOLS.extend(ADVANCED_FINANCIAL_TOOLS)
ALL_MATH_TOOLS.extend(CONVERTERS_ENGINEERING_TOOLS)
ALL_MATH_TOOLS.extend(EDUCATION_RANDOM_GEN_TOOLS)

DEDUPLICATED_MATH_TOOLS = []
seen_math_slugs = set()
for tool in ALL_MATH_TOOLS:
    if tool["slug"] not in seen_math_slugs:
        seen_math_slugs.add(tool["slug"])
        DEDUPLICATED_MATH_TOOLS.append(tool)

print(f"Loaded {len(DEDUPLICATED_MATH_TOOLS)} unique Math & Numbers tools.")

# Math Copy Generator for individual pages
def generate_math_text(tool):
    name = tool["name"]
    category = tool["category"]
    desc = tool["desc"]
    formula = tool["formula"]
    formula_desc = tool["formula_desc"]

    intro = f"""
      <h2>Introduction to the {name}</h2>
      <p>The **{name}** is a state-of-the-art online calculator designed to provide immediate, high-precision results for students, educators, engineers, and professionals. In mathematical studies and technical fields, performing accurate calculations is crucial for solving problems, analyzing data, and verifying designs. Whether you are dealing with basic arithmetic, algebraic equations, geometry theorems, trigonometric functions, or advanced statistics, this tool offers a safe, ad-free, and easy-to-use interface. Under the hood, this utility runs entirely using client-side JavaScript, ensuring that your inputs and private datasets remain confidential, secure, and local to your web browser session.</p>
      <p>Manual computation of mathematical equations, trigonometric identities, or statistical indices can be tedious and prone to errors. Our tool automates these tasks. By providing an interactive control panel with optimal default values, you can run calculations with a single click. It serves as an essential helper for high school and university students, teachers looking to prepare materials, and engineers validating mechanical properties or chemical formulas without needing to load heavy desktop software or run command-line scripts.</p>
      <p>Data privacy is a core foundation of all Enginewheels utilities. Many online calculators upload your numbers, formulas, or financial variables to backend servers, creating logs that could compromise sensitive academic or professional research. The Enginewheels **{name}** runs completely client-side. No data ever traverses the network or gets logged to external systems. Once you close your active browser tab, your parameters are completely cleared from memory, guaranteeing absolute confidentiality.</p>
      <p>Using this tool is free and requires no registration. It is optimized to load fast, meeting the highest standards of modern web performance. The visual layout scales fluidly on mobile screens, tablets, and desktop computers, so you can execute checks wherever you are. Use our {name} today to streamline your {category.lower()} tasks.</p>
    """

    how_it_works = f"""
      <h2>How the {name} Works</h2>
      <p>Our **{name}** uses client-side mathematical algorithms to process your inputs and display matching results instantly. First, the tool collects your numeric values, expressions, or choices from the control panel. Once you click "Calculate", the utility runs validation checks to make sure the inputs are not empty, are valid numbers, and conform to mathematical constraints (such as avoiding division by zero or negative values in square roots). If any parameters are invalid, the tool alerts you immediately via the toast notification system.</p>
      <p>After validation, the core algorithm is applied: ` {formula} `. {formula_desc} The engine processes the values, performs arithmetic calculations, or evaluates formulas using Javascript's Math library. The resulting output is written to the read-only output box. For instance, decimal answers are formatted to display cleanly, while text transformations are structured for easy reading. Trailing spaces are trimmed to present the values cleanly.</p>
      <p>Understanding the mathematical steps is critical for learning and auditing. That is why our tool displays a detailed step-by-step breakdown below the interface. The breakdown shows exactly how the final values were calculated, letting you audit the rules. It acts as an educational resource, helping you understand arithmetic operations, geometry proofs, or statistical formulas.</p>
      <p>Finally, if you want to copy the results for homework, reports, or documents, simply click the "Copy Output" button to save it directly to your clipboard. To start a new calculation, click "Clear Fields" to reset the outputs and start fresh, or click "Reset" to return all configuration inputs to their default values.</p>
    """

    features = f"""
      <h2>Key Features of the {name}</h2>
      <ul>
        <li><strong>Instant Calculations:</strong> Processes inputs instantly with reliable client-side algorithms.</li>
        <li><strong>100% Client-Side Privacy:</strong> Your numbers are processed entirely in the browser and never uploaded to our servers.</li>
        <li><strong>Educational Breakdown:</strong> Shows the step-by-step mathematical steps and formulas used to get the result.</li>
        <li><strong>One-Click Actions:</strong> Copy outputs to clipboard or clear inputs with a single click.</li>
        <li><strong>Responsive Design:</strong> Works perfectly on smartphones, tablets, and desktop computers.</li>
        <li><strong>Free & Unlimited:</strong> No registration, sign-ups, or limitations. Clear inputs with a single click.</li>
      </ul>
    """

    benefits = f"""
      <h2>Benefits of Using Online Mathematical Utilities</h2>
      <p>Manually calculating formulas or verifying development parameters takes significant time and leads to mathematical errors. A student checking algebra homework, a contractor estimating tile layout areas, or an analyst compiling population averages can save hours using our tool. The {name} automates these steps, ensuring consistent and professional results.</p>
      <p>Our tool helps you maintain absolute accuracy. By applying uniform rules and mathematical formulas, it ensures that your work is professional and ready for implementation. Additionally, the responsive design allows you to perform these operations from any device, whether you are on a desktop at school or on a mobile phone on the go.</p>
      <p>Unlike other web utilities that subject users to heavy ads, forced registrations, or paid plans, our tools are 100% free with no limits. This allows you to process as many parameters as you need, whenever you need them, without interruption.</p>
    """

    academic_tips = f"""
      <h2>Academic & Practical Best Practices</h2>
      <p>When working with mathematical formulas, always double-check the order of operations (PEMDAS/BODMAS): Parentheses first, then Exponents, Multiplication and Division (from left to right), and finally Addition and Subtraction (from left to right). For geometric calculations, verify that units are consistent (e.g. converting feet to inches before calculating area). Lastly, while local tools are helpful for rapid checking, understanding the underlying mathematical concepts is essential for long-term learning and problem-solving.</p>
    """

    use_cases = f"""
      <h2>Real-World Use Cases</h2>
      <ul>
        <li><strong>Students & Educators:</strong> Students can use the calculator to check homework answers, while teachers can verify answers for worksheet generation.</li>
        <li><strong>Engineers & Tech Professionals:</strong> Quickly compute angles, conversion rates, and coordinate transforms for coding and design tasks.</li>
        <li><strong>Everyday Planning:</strong> Calculate loan repayments, interest yields, GPA distributions, and random draws for decision-making.</li>
      </ul>
    """

    why_choose_us = f"""
      <h2>Why Choose Enginewheels for Your Mathematics Needs?</h2>
      <p>When it comes to performing mathematical operations, Enginewheels offers a reliable, premium, and entirely free solution. Our platform is built using modern web technologies to ensure that each tool loads instantly and runs with absolute speed. We prioritize user privacy above everything else; unlike typical online utilities that process data on remote servers, all your parameters are processed locally in your browser. This client-side approach ensures your sensitive numbers and final values never traverse the network or get saved to an external database. Furthermore, our user-friendly, responsive interface is designed from the ground up for seamless usability on mobile devices, tablets, and desktop computers. Whether you need to copy mathematical results for a report or reset variables for a quick iteration, Enginewheels provides a frictionless, ad-light environment designed to optimize your productivity.</p>
    """

    faqs = [
        {
            "q": f"Is there a limit on how many times I can use the {name}?",
            "a": f"No. All processing occurs locally in your browser using client-side JavaScript. There are no daily limits, usage caps, or registration requirements."
        },
        {
            "q": f"Does Enginewheels save my private inputs or data?",
            "a": f"No. All operations are processed locally in active memory. We do not upload your numbers to external servers, guaranteeing complete privacy."
        },
        {
            "q": f"What formula is used by the {name} under the hood?",
            "a": f"The tool uses the formula: {formula}. A detailed step-by-step explanation of the calculation is displayed right below the tool input form."
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

    math_article_html = f"""
      {intro}
      {how_it_works}
      {features}
      {benefits}
      {academic_tips}
      {use_cases}
      {why_choose_us}
      {faq_html}
    """
    return math_article_html, faqs

# Generate all individual HTML files
for index, tool in enumerate(DEDUPLICATED_MATH_TOOLS):
    name = tool["name"]
    slug = tool["slug"]
    category = tool["category"]
    desc = tool["desc"]

    # Generate SEO article content and FAQ schema
    seo_article_html, faqs = generate_math_text(tool)

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

    has_textarea_output = any(out.get("type") == "textarea" for out in tool["outputs"])
    if has_textarea_output:
        # Find the first textarea output element ID
        txt_out_id = next(out["id"] for out in tool["outputs"] if out.get("type") == "textarea")
        copy_js_logic = f"""const val = document.getElementById('{txt_out_id}').value || document.getElementById('{txt_out_id}').textContent;"""
    else:
        copy_lines = []
        for out in tool["outputs"]:
            copy_lines.append(f"val += ' - {out['label']}: ' + (document.getElementById('{out['id']}').textContent || '-') + '\\n';")
        copy_lines_str = "\n        ".join(copy_lines)
        copy_js_logic = f"""let val = "{name} Results:\\n";\n        {copy_lines_str}"""

    # Generate related tools grid
    related_list = []
    for other in DEDUPLICATED_MATH_TOOLS:
        if other["slug"] != slug and other["category"] == category:
            related_list.append(other)
            if len(related_list) == 2:
                break
    if len(related_list) < 2:
        for other in DEDUPLICATED_MATH_TOOLS:
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
  <title>{name} Online Free | Solve & Learn Math - Enginewheels</title>
  <meta name="description" content="{desc} Safe, responsive, and secure client-side browser-based math utility.">
  <link rel="canonical" href="https://enginewheels.com/math-tools/{slug}.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/math-tools/{slug}.html">
  <meta property="og:title" content="{name} Online Free | Solve & Learn Math - Enginewheels">
  <meta property="og:description" content="{desc} Safe, responsive, and secure client-side browser-based math utility.">
  
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
        "name": "Math & Numbers",
        "item": "https://enginewheels.com/category/math-numbers.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{name}",
        "item": "https://enginewheels.com/math-tools/{slug}.html"
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

  <!-- Main Layout -->
  <main class="tool-page-layout container">
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../index.html">Home</a> &gt; <a href="../category/math-numbers.html">Math & Numbers</a> &gt; <span>{name}</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">{name}</h1>
      <p class="tool-desc-lead">{desc}</p>
    </div>

    <!-- Interface Section -->
    <section class="calculator-card glass-panel">
      <div class="calc-grid">
        <!-- Inputs Column -->
        <div class="calc-inputs">
          <div style="font-size: 1.1rem; font-weight: 600; color: #fff; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">Configure Inputs</div>
          {inputs_html}
          <div style="display: flex; gap: 12px; margin-top: 30px;">
            <button id="btn-calculate" class="btn btn-primary" style="flex: 2; padding: 12px;">Calculate</button>
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

    <!-- Related Tools Grid -->
    <section class="related-tools-section" style="margin-top: 60px;">
      <h2 style="font-size: 1.4rem; color: #fff; margin-bottom: 24px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">Related Mathematics Utilities</h2>
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
    tool_page_path = os.path.join(MATH_DIR, f"{slug}.html")
    with open(tool_page_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(DEDUPLICATED_MATH_TOOLS)} HTML tool files successfully.")

# ----------------- REWRITE CATEGORY/MATH-NUMBERS.HTML -----------------
print("Rewriting category/math-numbers.html...")

subcategories = {}
for t in DEDUPLICATED_MATH_TOOLS:
    cat = t["category"]
    if cat not in subcategories:
        subcategories[cat] = []
    subcategories[cat].append(t)

ordered_cats = [
    "Basic Math Tools",
    "Number Calculators",
    "Algebra Tools",
    "Geometry Tools",
    "Trigonometry Tools",
    "Statistics Tools",
    "Advanced Math Tools",
    "Financial Math Tools",
    "Number Converters",
    "Engineering Calculators",
    "Education Tools",
    "Random Number Tools",
    "Math Generators"
]
for cat in subcategories.keys():
    if cat not in ordered_cats:
        ordered_cats.append(cat)

grids_html = ""
for subcat in ordered_cats:
    if subcat not in subcategories or not subcategories[subcat]:
        continue
    tools_list = subcategories[subcat]
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
          <a href="../math-tools/{t['slug']}.html" class="tool-card">
            <div class="tool-card-header">
              <div class="tool-card-icon">{t['icon']}</div>
              <h3 class="tool-card-title">{t['name']}</h3>
            </div>
            <p class="tool-card-desc">{t['desc']}</p>
            <div class="tool-card-link">Open Tool &gt;</div>
          </a>
        """
    grids_html += """
      </div>
    </div>
    """

# Read 3500+ words Math text
category_math_text_path = os.path.join(ROOT_DIR, "category_math_numbers_text.txt")
if os.path.exists(category_math_text_path):
    with open(category_math_text_path, "r", encoding="utf-8") as f:
        category_math_text = f.read()
else:
    category_math_text = "<h2>Ultimate Guide to Online Math Tools & Numerical Systems</h2><p>Solve arithmetic, algebraic equations, geometric structures locally...</p>"

category_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>Math & Number Tools Online Free | Solve Equations & Algebra - Enginewheels</title>
  <meta name="description" content="Explore our free Math & Number Tools category. Solve quadratic equations, calculate geometry dimensions, run statistics mean/standard deviations, and convert bases client-side.">
  <link rel="canonical" href="https://enginewheels.com/category/math-numbers.html">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://enginewheels.com/category/math-numbers.html">
  <meta property="og:title" content="Math & Number Tools Online Free | Solve Equations & Algebra - Enginewheels">
  <meta property="og:description" content="Explore our free Math & Number Tools category. Solve quadratic equations, calculate geometry dimensions, run statistics mean/standard deviations, and convert bases client-side.">
  
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
        "name": "Math & Numbers",
        "item": "https://enginewheels.com/category/math-numbers.html"
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
      <a href="../index.html">Home</a> &gt; <a href="../index.html#categories">Categories</a> &gt; <span>Math & Numbers</span>
    </nav>

    <div class="tool-header">
      <h1 class="tool-title-h1">Math & <span>Number</span> Tools</h1>
      <p class="tool-desc-lead">Solve linear algebra, evaluate algebraic systems, run statistical standard deviations, flip bases, and calculate compound yields client-side.</p>
    </div>

    <!-- Active Tools Grid -->
    <section style="margin-bottom: 60px;">
      {grids_html}
    </section>

    <!-- Technical SEO Article -->
    <article class="seo-article">
      {category_math_text}
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

category_page_path = os.path.join(ROOT_DIR, "category", "math-numbers.html")
with open(category_page_path, "w", encoding="utf-8") as f:
    f.write(category_html_content)
print("category/math-numbers.html rewritten successfully.")

# ----------------- REWRITE SITEMAP.HTML -----------------
print("Rewriting sitemap.html...")

sitemap_html_path = os.path.join(ROOT_DIR, "sitemap.html")
with open(sitemap_html_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Group SEO tools
seo_groups = {}
for tool in DEDUPLICATED_SEO_TOOLS:
    cat = tool["category"]
    if cat not in seo_groups:
        seo_groups[cat] = []
    seo_groups[cat].append(tool)

seo_links_html = ""
for cat, tools in seo_groups.items():
    seo_links_html += f'            <li><span style="font-weight:600; color:var(--text-muted);">{cat}:</span></li>\n'
    for t in tools:
        seo_links_html += f'            <li><a href="seo-web-tools/{t["slug"]}.html" style="padding-left:16px;">{t["name"]}</a></li>\n'

# Group Math tools
math_groups = {}
for tool in DEDUPLICATED_MATH_TOOLS:
    cat = tool["category"]
    if cat not in math_groups:
        math_groups[cat] = []
    math_groups[cat].append(tool)

math_links_html = ""
for cat, tools in math_groups.items():
    math_links_html += f'            <li><span style="font-weight:600; color:var(--text-muted);">{cat}:</span></li>\n'
    for t in tools:
        math_links_html += f'            <li><a href="math-tools/{t["slug"]}.html" style="padding-left:16px;">{t["name"]}</a></li>\n'

# Check if SEO column already exists
if "<!-- START SEO TOOLS -->" in sitemap_content:
    start_target = '<!-- START SEO TOOLS -->'
    end_target = '<!-- END SEO TOOLS -->'
    start_idx = sitemap_content.find(start_target)
    end_idx = sitemap_content.find(end_target)
    sitemap_content = sitemap_content[:start_idx] + f"{start_target}\n{seo_links_html}          {end_target}" + sitemap_content[end_idx + len(end_target):]
else:
    # Append after Generator Tools
    generator_end = "<!-- END GENERATOR TOOLS -->\n        </ul>\n      </div>"
    if generator_end in sitemap_content:
        replacement = generator_end + f"""\n      
      <!-- SEO & Web Tools Column -->
      <div>
        <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">SEO & Web Tools</h2>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          <!-- START SEO TOOLS -->
{seo_links_html}          <!-- END SEO TOOLS -->
        </ul>
      </div>"""
        sitemap_content = sitemap_content.replace(generator_end, replacement)

# Check if Math column already exists
if "<!-- START MATH TOOLS -->" in sitemap_content:
    start_target = '<!-- START MATH TOOLS -->'
    end_target = '<!-- END MATH TOOLS -->'
    start_idx = sitemap_content.find(start_target)
    end_idx = sitemap_content.find(end_target)
    sitemap_content = sitemap_content[:start_idx] + f"{start_target}\n{math_links_html}          {end_target}" + sitemap_content[end_idx + len(end_target):]
else:
    # Append after SEO column
    seo_end = "<!-- END SEO TOOLS -->\n        </ul>\n      </div>"
    if seo_end in sitemap_content:
        replacement = seo_end + f"""\n      
      <!-- Math & Numbers Column -->
      <div>
        <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Math & Numbers</h2>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          <!-- START MATH TOOLS -->
{math_links_html}          <!-- END MATH TOOLS -->
        </ul>
      </div>"""
        sitemap_content = sitemap_content.replace(seo_end, replacement)
    else:
        # Fallback to generator_end if seo_end is not found
        generator_end = "<!-- END GENERATOR TOOLS -->\n        </ul>\n      </div>"
        if generator_end in sitemap_content:
            replacement = generator_end + f"""\n      
      <!-- Math & Numbers Column -->
      <div>
        <h2 style="margin-top:0; font-size:1.4rem; padding-bottom:8px; border-bottom:1px solid rgba(255,255,255,0.05);">Math & Numbers</h2>
        <ul style="list-style-type: none; padding-left: 0; margin-top:16px; line-height:2; font-size: 0.9rem; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05); padding: 12px; border-radius: 8px;">
          <!-- START MATH TOOLS -->
{math_links_html}          <!-- END MATH TOOLS -->
        </ul>
      </div>"""
            sitemap_content = sitemap_content.replace(generator_end, replacement)

with open(sitemap_html_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)
print("sitemap.html updated.")

# ----------------- REWRITE SITEMAP.XML -----------------
print("Rewriting sitemap.xml...")

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
for tool in DEDUPLICATED_SEO_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/seo-web-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
for tool in DEDUPLICATED_MATH_TOOLS:
    xml_urls.append(f"  <url><loc>https://enginewheels.com/math-tools/{tool['slug']}.html</loc><lastmod>2026-06-22</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")

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
  <url>
    <loc>https://enginewheels.com/category/seo-web-tools.html</loc>
    <lastmod>2026-06-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://enginewheels.com/category/math-numbers.html</loc>
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

# Append SEO & Web Tools
for tool in DEDUPLICATED_SEO_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"seo-web-tools/{tool['slug']}.html",
        "category": f"SEO & Web Tools ({tool['category']})",
        "desc": tool["desc"]
    })

# Append Math & Numbers tools
for tool in DEDUPLICATED_MATH_TOOLS:
    search_items.append({
        "name": tool["name"],
        "url": f"math-tools/{tool['slug']}.html",
        "category": f"Math & Numbers ({tool['category']})",
        "desc": tool["desc"]
    })

search_items_json = json.dumps(search_items, indent=2)
new_index_block = f"const ENGINYWHEELS_TOOLS = {search_items_json};"

updated_main_js = main_js_content[:start_idx] + new_index_block + main_js_content[end_idx+2:]

# Update prefix logic to support math-tools and seo-web-tools subdirectories
prefix_match = re.search(r"const prefix = \(.*?\) \? '\.\./' : '';", updated_main_js)
if prefix_match:
    clean_prefix = "const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/') || window.location.pathname.includes('/security-tools/') || window.location.pathname.includes('/image-tools/') || window.location.pathname.includes('/time-tools/') || window.location.pathname.includes('/developer-tools/') || window.location.pathname.includes('/generator-tools/') || window.location.pathname.includes('/seo-web-tools/') || window.location.pathname.includes('/math-tools/')) ? '../' : '';"
    updated_main_js = updated_main_js.replace(prefix_match.group(0), clean_prefix)

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(updated_main_js)

print("assets/js/main.js search index and prefix checks rebuilt.")
print("[+] All generation operations completed successfully!")
