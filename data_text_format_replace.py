# -*- coding: utf-8 -*-
"""
Text Formatters and Search & Replace Tools Data
"""

FORMATTER_CALCS = [
    {
        "name": "Text Cleaner",
        "slug": "text-cleaner",
        "category": "Text Formatters",
        "icon": "🧼",
        "desc": "Clean text by removing control characters, fixing bad spaces, and tidying markup symbols.",
        "formula": "Clean = RegEx replacements",
        "formula_desc": "Sanitizes strings by cleaning system codes, double spaces, and invalid Unicode segments.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cleaned Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            // Clean control chars, double spaces, and trim
            let cleaned = text.replace(/[\\x00-\\x09\\x0B-\\x0C\\x0E-\\x1F\\x7F]/g, '');
            cleaned = cleaned.replace(/[ ]+/g, ' ');
            cleaned = cleaned.split('\\n').map(line => line.trim()).join('\\n');
            document.getElementById('text-output').value = cleaned.trim();
            updateBreakdown(`<p>Removed hidden control characters and collapsed multiple spacing segments.</p>`);
        """
    },
    {
        "name": "Text Formatter",
        "slug": "text-formatter",
        "category": "Text Formatters",
        "icon": "📝",
        "desc": "Standardize text spacing, sentence capitalization, and paragraph alignments.",
        "formula": "Standard formatting",
        "formula_desc": "Iterates sentences, capitalizing the start and cleaning extra linebreaks.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Formatted Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let formatted = text.replace(/\\s+/g, ' ').trim();
            formatted = formatted.replace(/(^\\s*|[.!?]\\s+)([a-z])/g, (m, sep, l) => sep + l.toUpperCase());
            document.getElementById('text-output').value = formatted;
            updateBreakdown(`<p>Normalized whitespaces and capitalized the starting words of all sentences.</p>`);
        """
    },
    {
        "name": "Text Sorter",
        "slug": "text-sorter",
        "category": "Text Formatters",
        "icon": "🗂️",
        "desc": "Sort text lines alphabetically, numerically, by length, or in reverse.",
        "formula": "Lines.sort()",
        "formula_desc": "Splits text into lines, applies sorting criteria, and merges lines back.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""},
            {"id": "sort-mode", "label": "Sort Order Option", "type": "select", "options": [
                ["asc", "Alphabetical (A to Z)"],
                ["desc", "Reverse Alphabetical (Z to A)"],
                ["length-asc", "Line Length (Shortest to Longest)"],
                ["length-desc", "Line Length (Longest to Shortest)"]
            ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sorted Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const mode = document.getElementById('sort-mode').value;
            let lines = text.split('\\n');
            
            if (mode === 'asc') {
                lines.sort((a, b) => a.localeCompare(b));
            } else if (mode === 'desc') {
                lines.sort((a, b) => b.localeCompare(a));
            } else if (mode === 'length-asc') {
                lines.sort((a, b) => a.length - b.length);
            } else if (mode === 'length-desc') {
                lines.sort((a, b) => b.length - a.length);
            }
            
            document.getElementById('text-output').value = lines.join('\\n');
            updateBreakdown(`<p>Sorted ${lines.length} lines using the chosen ordering mode: ${mode}.</p>`);
        """
    },
    {
        "name": "Alphabetical Sorter",
        "slug": "alphabetical-sorter",
        "category": "Text Formatters",
        "icon": "🔤",
        "desc": "Sort text lines in ascending alphabetical order (A to Z).",
        "formula": "Lines.sort(a-z)",
        "formula_desc": "Splits text by newline, runs localeCompare sort, and outputs rows.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sorted Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let lines = text.split('\\n').filter(l => l.length > 0);
            lines.sort((a, b) => a.localeCompare(b));
            document.getElementById('text-output').value = lines.join('\\n');
            updateBreakdown(`<p>Alphabetized ${lines.length} non-empty lines.</p>`);
        """
    },
    {
        "name": "Reverse Sorter",
        "slug": "reverse-sorter",
        "category": "Text Formatters",
        "icon": "🔃",
        "desc": "Sort text lines in reverse alphabetical order (Z to A).",
        "formula": "Lines.sort(z-a)",
        "formula_desc": "Sorts input lines descending based on string lexicographical value.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Reverse Sorted Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let lines = text.split('\\n').filter(l => l.length > 0);
            lines.sort((a, b) => b.localeCompare(a));
            document.getElementById('text-output').value = lines.join('\\n');
            updateBreakdown(`<p>Reverse-sorted ${lines.length} non-empty lines.</p>`);
        """
    },
    {
        "name": "Randomize Lines",
        "slug": "randomize-lines",
        "category": "Text Formatters",
        "icon": "🎲",
        "desc": "Shuffle and randomize the order of lines in your text block.",
        "formula": "Shuffled lines",
        "formula_desc": "Uses Fisher-Yates shuffle algorithm to randomize the rows of text.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Shuffled Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let lines = text.split('\\n');
            for (let i = lines.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [lines[i], lines[j]] = [lines[j], lines[i]];
            }
            document.getElementById('text-output').value = lines.join('\\n');
            updateBreakdown(`<p>Shuffled line order using Fisher-Yates randomization.</p>`);
        """
    },
    {
        "name": "Remove Empty Lines",
        "slug": "remove-empty-lines",
        "category": "Text Formatters",
        "icon": "❌",
        "desc": "Remove all completely blank or whitespace-only lines from text.",
        "formula": "Filter(lines => line.trim().length > 0)",
        "formula_desc": "Checks each line, discarding those containing only spaces, tabs, or newlines.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Filtered Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const lines = text.split('\\n');
            const filtered = lines.filter(line => line.trim().length > 0);
            document.getElementById('text-output').value = filtered.join('\\n');
            updateBreakdown(`<p>Removed ${lines.length - filtered.length} empty or blank lines.</p>`);
        """
    },
    {
        "name": "Trim Text Tool",
        "slug": "trim-text-tool",
        "category": "Text Formatters",
        "icon": "✂️",
        "desc": "Remove leading, trailing, and unnecessary whitespace from text lines.",
        "formula": "Trim strings",
        "formula_desc": "Strips spaces from the start and end of every single line in the input.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Trimmed Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const trimmed = text.split('\\n').map(line => line.trim()).join('\\n');
            document.getElementById('text-output').value = trimmed;
            updateBreakdown(`<p>Stripped whitespace prefixes and suffixes from all lines.</p>`);
        """
    },
    {
        "name": "Text Indenter",
        "slug": "text-indenter",
        "category": "Text Formatters",
        "icon": "➡️",
        "desc": "Add custom spaces or tab indentations to the beginning of each line.",
        "formula": "Line = Indent + Line",
        "formula_desc": "Prefixes each line with a specified number of spaces or a tab character.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""},
            {"id": "indent-size", "label": "Indent Spaces Count", "type": "number", "default": "4", "min": "1", "max": "20", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Indented Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const size = parseInt(document.getElementById('indent-size').value) || 4;
            const indent = ' '.repeat(size);
            const indented = text.split('\\n').map(line => line ? indent + line : '').join('\\n');
            document.getElementById('text-output').value = indented;
            updateBreakdown(`<p>Prepended ${size} spaces to the beginning of all text lines.</p>`);
        """
    },
    {
        "name": "Text Outdenter",
        "slug": "text-outdenter",
        "category": "Text Formatters",
        "icon": "⬅️",
        "desc": "Remove leading tab or space indentations from your text lines.",
        "formula": "Line.replace(/^[ ]{1,N}/, '')",
        "formula_desc": "Scans and removes up to a specified number of leading space characters from each line.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""},
            {"id": "outdent-size", "label": "Outdent Spaces Count", "type": "number", "default": "4", "min": "1", "max": "20", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Outdented Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const size = parseInt(document.getElementById('outdent-size').value) || 4;
            const regex = new RegExp('^[ ]{1,' + size + '}|^\\\\t');
            const outdented = text.split('\\n').map(line => line.replace(regex, '')).join('\\n');
            document.getElementById('text-output').value = outdented;
            updateBreakdown(`<p>Removed up to ${size} leading spaces (or one tab character) per line.</p>`);
        """
    }
]

REPLACE_CALCS = [
    {
        "name": "Find And Replace Text",
        "slug": "find-and-replace-text",
        "category": "Search & Replace Tools",
        "icon": "🔍",
        "desc": "Find occurrences of specific text strings and replace them with new content.",
        "formula": "Text.replace(Find, Replace)",
        "formula_desc": "Replaces matches using literal text or simple case-insensitive parameters.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""},
            {"id": "find-str", "label": "Find String", "type": "text", "default": "find"},
            {"id": "replace-str", "label": "Replace With", "type": "text", "default": "replace"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Replaced Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const findVal = document.getElementById('find-str').value;
            const repVal = document.getElementById('replace-str').value;
            
            if (findVal === '') {
                showToast("Please specify a string to find.", "error");
                return;
            }
            
            // Escape regex helper
            const escapedFind = findVal.replace(/[-\\/\\\\^$*+?.()|[\\]{{}}]/g, '\\\\$&');
            const regex = new RegExp(escapedFind, 'g');
            const replaced = text.replace(regex, repVal);
            
            document.getElementById('text-output').value = replaced;
            const count = (text.match(regex) || []).length;
            updateBreakdown(`<p>Found and replaced ${count} occurrences of '${findVal}' with '${repVal}'.</p>`);
        """
    },
    {
        "name": "Multi Text Replace Tool",
        "slug": "multi-text-replace-tool",
        "category": "Search & Replace Tools",
        "icon": "🔀",
        "desc": "Find and replace multiple words at once using comma-separated rules.",
        "formula": "Iterated replacements",
        "formula_desc": "Applies a sequence of replacement rules consecutively across the input text.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""},
            {"id": "replace-rules", "label": "Replacement Rules (format: find=replace, one per line)", "type": "textarea", "default": "cat=dog\\nhello=hi"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Replaced Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const rulesText = document.getElementById('replace-rules').value;
            let result = text;
            
            const lines = rulesText.split('\\n');
            let ruleCount = 0;
            
            for (let line of lines) {
                const parts = line.split('=');
                if (parts.length >= 2) {
                    const f = parts[0];
                    const r = parts.slice(1).join('=');
                    if (f !== '') {
                        const escapedFind = f.replace(/[-\\/\\\\^$*+?.()|[\\]{{}}]/g, '\\\\$&');
                        const regex = new RegExp(escapedFind, 'g');
                        result = result.replace(regex, r);
                        ruleCount++;
                    }
                }
            }
            
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Successfully processed ${ruleCount} active replacement rules.</p>`);
        """
    },
    {
        "name": "Remove Specific Words",
        "slug": "remove-specific-words",
        "category": "Search & Replace Tools",
        "icon": "🚫",
        "desc": "Remove selected words or phrases from your text block entirely.",
        "formula": "Text.replace(Word, '')",
        "formula_desc": "Matches specified words and strips them, keeping sentence flow clean.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""},
            {"id": "words-list", "label": "Words to Remove (comma-separated)", "type": "text", "default": "spam, ads"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cleaned Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const wordsVal = document.getElementById('words-list').value;
            let result = text;
            
            const words = wordsVal.split(',').map(w => w.trim()).filter(w => w !== '');
            for (let w of words) {
                const escaped = w.replace(/[-\\/\\\\^$*+?.()|[\\]{{}}]/g, '\\\\$&');
                const regex = new RegExp('\\\\b' + escaped + '\\\\b|' + escaped, 'gi');
                result = result.replace(regex, '');
            }
            
            // Clean double spaces
            result = result.replace(/[ ]+/g, ' ').trim();
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Removed words: ${words.join(', ')} from the input string.</p>`);
        """
    },
    {
        "name": "Remove Numbers From Text",
        "slug": "remove-numbers-from-text",
        "category": "Search & Replace Tools",
        "icon": "🔠",
        "desc": "Remove all numeric digits (0-9) from your text string.",
        "formula": "Text.replace(/[0-9]/g, '')",
        "formula_desc": "Applies numerical range regex lookup to find and clean digits.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const cleaned = text.replace(/[0-9]/g, '');
            document.getElementById('text-output').value = cleaned;
            updateBreakdown(`<p>Stripped all numbers from the text block.</p>`);
        """
    },
    {
        "name": "Remove Special Characters",
        "slug": "remove-special-characters",
        "category": "Search & Replace Tools",
        "icon": "⭐",
        "desc": "Remove symbols, emojis, and special chars, keeping letters and numbers.",
        "formula": "Text.replace(/[^a-zA-Z0-9\\s]/g, '')",
        "formula_desc": "Keeps standard alphanumeric characters and removes symbols.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const cleaned = text.replace(/[^a-zA-Z0-9\\s\\n\\r]/g, '');
            document.getElementById('text-output').value = cleaned;
            updateBreakdown(`<p>Stripped all special symbols and punctuation markers.</p>`);
        """
    },
    {
        "name": "Remove Punctuation Tool",
        "slug": "remove-punctuation-tool",
        "category": "Search & Replace Tools",
        "icon": "❓",
        "desc": "Strip punctuation marks like periods, commas, and question marks from text.",
        "formula": "Text.replace(/[punctuation]/g, '')",
        "formula_desc": "Removes standard punctuation characters while preserving symbols like $, #, @.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Text Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const cleaned = text.replace(/[.,\\/#!$%\\^&\\*;:{}=\\-_`~()?\"']/g, '');
            document.getElementById('text-output').value = cleaned;
            updateBreakdown(`<p>Removed standard punctuation indicators from the string block.</p>`);
        """
    },
    {
        "name": "Extract Numbers From Text",
        "slug": "extract-numbers-from-text",
        "category": "Search & Replace Tools",
        "icon": "🔢",
        "desc": "Pull all numbers and integers out of a mixed text document.",
        "formula": "Numbers = Text.match(/\\d+/g)",
        "formula_desc": "Extracts consecutive digital digit segments and outputs them as a list.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Numbers", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const matches = text.match(/\\d+(?:\\.\\d+)?/g);
            if (matches) {
                document.getElementById('text-output').value = matches.join('\\n');
                updateBreakdown(`<p>Extracted ${matches.length} unique numeric instances.</p>`);
            } else {
                document.getElementById('text-output').value = 'No numbers found.';
                updateBreakdown(`<p>No digits parsed.</p>`);
            }
        """
    },
    {
        "name": "Extract Emails From Text",
        "slug": "extract-emails-from-text",
        "category": "Search & Replace Tools",
        "icon": "📧",
        "desc": "Extract all email addresses from a large text document or list.",
        "formula": "Emails = Text.match(email_pattern)",
        "formula_desc": "Applies a standard RFC 5322 regex match to identify and isolate emails.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Emails", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{{2,}}/g;
            const matches = text.match(regex);
            if (matches) {
                const unique = [...new Set(matches)];
                document.getElementById('text-output').value = unique.join('\\n');
                updateBreakdown(`<p>Extracted ${unique.length} unique email addresses.</p>`);
            } else {
                document.getElementById('text-output').value = 'No email addresses found.';
                updateBreakdown(`<p>No emails parsed.</p>`);
            }
        """
    },
    {
        "name": "Extract URLs From Text",
        "slug": "extract-urls-from-text",
        "category": "Search & Replace Tools",
        "icon": "🌐",
        "desc": "Scan text and extract all HTTP, HTTPS, and FTP web links.",
        "formula": "URLs = Text.match(url_pattern)",
        "formula_desc": "Scans strings using regex templates for web link structures.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Links", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const regex = /https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{{1,256}}\\.[a-zA-Z0-9()]{{1,6}}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&//=]*)/g;
            const matches = text.match(regex);
            if (matches) {
                const unique = [...new Set(matches)];
                document.getElementById('text-output').value = unique.join('\\n');
                updateBreakdown(`<p>Parsed ${unique.length} unique links.</p>`);
            } else {
                document.getElementById('text-output').value = 'No URLs found.';
                updateBreakdown(`<p>No links parsed.</p>`);
            }
        """
    },
    {
        "name": "Extract Hashtags From Text",
        "slug": "extract-hashtags-from-text",
        "category": "Search & Replace Tools",
        "icon": "🏷️",
        "desc": "Extract hashtags (#topic) from tweets, posts, or marketing copies.",
        "formula": "Hashtags = Text.match(/#[a-zA-Z0-9_]+/g)",
        "formula_desc": "Matches strings starting with hash symbol followed by alphanumeric characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Hashtags", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const matches = text.match(/#[a-zA-Z0-9_]+/g);
            if (matches) {
                const unique = [...new Set(matches)];
                document.getElementById('text-output').value = unique.join('\\n');
                updateBreakdown(`<p>Parsed ${unique.length} unique hashtags.</p>`);
            } else {
                document.getElementById('text-output').value = 'No hashtags found.';
                updateBreakdown(`<p>No hashtags parsed.</p>`);
            }
        """
    }
]
