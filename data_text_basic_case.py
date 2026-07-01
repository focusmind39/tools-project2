# -*- coding: utf-8 -*-
"""
Basic Text Tools and Case Converters Data
"""

BASIC_TEXT_CALCS = [
    {
        "name": "Word Counter",
        "slug": "word-counter",
        "category": "Basic Text Tools",
        "icon": "✍",
        "desc": "Count words, characters, sentences, paragraphs, and reading times in real-time.",
        "formula": "Word Count = Text.split(\\s+).length",
        "formula_desc": "Counts the number of words by splitting the input text along any whitespace characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": "Paste your text here to count words..."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Word Count Statistics", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            const chars = text.length;
            const charsNoSpace = text.replace(/\\s/g, '').length;
            const sentences = text.trim() === '' ? 0 : text.split(/[.!?]+/).filter(s => s.trim().length > 0).length;
            const paragraphs = text.trim() === '' ? 0 : text.split(/\\n+/).filter(p => p.trim().length > 0).length;
            const readTime = Math.ceil(words / 200);

            document.getElementById('text-output').value = 
                `Words: ${words}\\n` +
                `Characters (with spaces): ${chars}\\n` +
                `Characters (no spaces): ${charsNoSpace}\\n` +
                `Sentences: ${sentences}\\n` +
                `Paragraphs: ${paragraphs}\\n` +
                `Estimated Reading Time: ${readTime} min`;

            updateBreakdown(`
                <p><strong>Total Words:</strong> ${words}</p>
                <p><strong>Characters:</strong> ${chars} (without spaces: ${charsNoSpace})</p>
                <p><strong>Sentence Count:</strong> ${sentences}</p>
                <p><strong>Paragraphs:</strong> ${paragraphs}</p>
            `);
        """
    },
    {
        "name": "Character Counter",
        "slug": "character-counter",
        "category": "Basic Text Tools",
        "icon": "🔢",
        "desc": "Count total characters, letters, numbers, and symbols with or without spaces.",
        "formula": "Char Count = Text.length",
        "formula_desc": "Calculates length metrics of the text string including whitespace.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Character Statistics", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const total = text.length;
            const noSpaces = text.replace(/\\s/g, '').length;
            const letters = (text.match(/[a-zA-Z]/g) || []).length;
            const numbers = (text.match(/[0-9]/g) || []).length;
            const special = total - noSpaces - letters - numbers; // spaces count here too in original, let's count strictly non-alphanumeric
            const specialStrict = (text.match(/[^a-zA-Z0-9\\s]/g) || []).length;

            document.getElementById('text-output').value = 
                `Total Characters: ${total}\\n` +
                `Characters (no spaces): ${noSpaces}\\n` +
                `Alphabetic Letters: ${letters}\\n` +
                `Numeric Digits: ${numbers}\\n` +
                `Special Symbols: ${specialStrict}`;

            updateBreakdown(`
                <p><strong>Total characters parsed:</strong> ${total}</p>
                <p><strong>Whitespace characters:</strong> ${total - noSpaces}</p>
            `);
        """
    },
    {
        "name": "Sentence Counter",
        "slug": "sentence-counter",
        "category": "Basic Text Tools",
        "icon": "💬",
        "desc": "Count the total number of sentences in your writing instantly.",
        "formula": "Sentence Count = Text.split(/[.!?]+/).length",
        "formula_desc": "Identifies sentences by splitting at punctuation marks (. , ! , ?).",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sentence Count Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const sentences = text.trim() === '' ? 0 : text.split(/[.!?]+/).filter(s => s.trim().length > 0).length;
            document.getElementById('text-output').value = `Total Sentences: ${sentences}`;
            updateBreakdown(`<p>Found ${sentences} unique sentences separated by period, exclamation, or question marks.</p>`);
        """
    },
    {
        "name": "Paragraph Counter",
        "slug": "paragraph-counter",
        "category": "Basic Text Tools",
        "icon": "📝",
        "desc": "Calculate total paragraphs in your document, ignoring empty lines.",
        "formula": "Paragraph Count = Text.split(\\n+).length",
        "formula_desc": "Counts paragraphs by splitting text blocks on one or more newline boundaries.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Paragraph Count Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const paragraphs = text.trim() === '' ? 0 : text.split(/\\n+/).filter(p => p.trim().length > 0).length;
            document.getElementById('text-output').value = `Total Paragraphs: ${paragraphs}`;
            updateBreakdown(`<p>Paragraph separation determined by identifying blocks separated by hard carriage returns.</p>`);
        """
    },
    {
        "name": "Reading Time Calculator",
        "slug": "reading-time-calculator",
        "category": "Basic Text Tools",
        "icon": "⏳",
        "desc": "Calculate estimated reading time based on typical human WPM speeds.",
        "formula": "Minutes = Words / 200",
        "formula_desc": "Uses standard adult average silent reading speeds of 200 WPM to evaluate reading duration.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Reading Time Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            const speed = 200; // WPM
            const time = words / speed;
            const min = Math.floor(time);
            const sec = Math.round((time - min) * 60);

            document.getElementById('text-output').value = 
                `Words: ${words}\\n` +
                `Estimated Reading Time: ${min} minute(s) and ${sec} second(s)`;

            updateBreakdown(`<p>Estimated using standard reading index parameters of ${speed} WPM.</p>`);
        """
    },
    {
        "name": "Speaking Time Calculator",
        "slug": "speaking-time-calculator",
        "category": "Basic Text Tools",
        "icon": "🎤",
        "desc": "Calculate speaking time for presentations, speeches, and podcasts.",
        "formula": "Minutes = Words / 130",
        "formula_desc": "Estimates verbal speaking rate based on standard speech pace of 130 WPM.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Speaking Time Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            const speed = 130; // WPM
            const time = words / speed;
            const min = Math.floor(time);
            const sec = Math.round((time - min) * 60);

            document.getElementById('text-output').value = 
                `Words: ${words}\\n` +
                `Estimated Speaking Time: ${min} minute(s) and ${sec} second(s)`;

            updateBreakdown(`<p>Computed based on typical voice presentation metrics of ${speed} WPM.</p>`);
        """
    },
    {
        "name": "Text Reverser",
        "slug": "text-reverser",
        "category": "Basic Text Tools",
        "icon": "🔄",
        "desc": "Reverse your text letters, words, or sentences instantly.",
        "formula": "Reversed = Text.split('').reverse().join('')",
        "formula_desc": "Splits the input string into characters, reverses the array, and joins them back.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Reversed Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const reversed = text.split('').reverse().join('');
            document.getElementById('text-output').value = reversed;
            updateBreakdown(`<p>Reversed total string of length ${text.length} characters successfully.</p>`);
        """
    },
    {
        "name": "Line Counter",
        "slug": "line-counter",
        "category": "Basic Text Tools",
        "icon": "📏",
        "desc": "Count total lines, empty lines, and non-empty lines in text.",
        "formula": "Line Count = Text.split('\\n').length",
        "formula_desc": "Splits the input text by newline indicators and returns count.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Line Statistics", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const totalLines = text === '' ? 0 : text.split('\\n').length;
            const emptyLines = text === '' ? 0 : text.split('\\n').filter(line => line.trim() === '').length;
            const contentLines = totalLines - emptyLines;

            document.getElementById('text-output').value = 
                `Total Lines: ${totalLines}\\n` +
                `Content Lines: ${contentLines}\\n` +
                `Empty Lines: ${emptyLines}`;

            updateBreakdown(`<p>Parsed lines by isolating carriage return boundaries.</p>`);
        """
    },
    {
        "name": "Whitespace Remover",
        "slug": "whitespace-remover",
        "category": "Basic Text Tools",
        "icon": "🧹",
        "desc": "Remove extra spaces, tabs, and newlines from your text strings.",
        "formula": "Cleaned = Text.replace(/\\s+/g, ' ')",
        "formula_desc": "Uses regular expressions to collapse multiple whitespace characters into single spaces.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Cleaned Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const cleaned = text.replace(/\\s+/g, ' ').trim();
            document.getElementById('text-output').value = cleaned;
            updateBreakdown(`<p>Collapsed consecutive whitespace arrays into clean, isolated spaces.</p>`);
        """
    },
    {
        "name": "Duplicate Line Remover",
        "slug": "duplicate-line-remover",
        "category": "Basic Text Tools",
        "icon": "🗑️",
        "desc": "Filter out duplicate lines of text, leaving only unique rows.",
        "formula": "Unique = Set(Lines)",
        "formula_desc": "Splits text into lines, adds them to a unique JS Set, and joins back with newlines.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Unique Lines", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const lines = text.split('\\n');
            const uniqueLines = [...new Set(lines)];
            document.getElementById('text-output').value = uniqueLines.join('\\n');
            updateBreakdown(`<p>Removed ${lines.length - uniqueLines.length} duplicate lines from a total of ${lines.length} lines.</p>`);
        """
    }
]

CASE_CONVERTER_CALCS = [
    {
        "name": "Uppercase Converter",
        "slug": "uppercase-converter",
        "category": "Case Converters",
        "icon": "🔠",
        "desc": "Convert all alphabetical characters in your text to uppercase letters.",
        "formula": "Text = Text.toUpperCase()",
        "formula_desc": "Iterates through characters, replacing lowercase letters with their capitalized Unicode equivalents.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Uppercase Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            document.getElementById('text-output').value = text.toUpperCase();
            updateBreakdown(`<p>Successfully converted all letters to uppercase format.</p>`);
        """
    },
    {
        "name": "Lowercase Converter",
        "slug": "lowercase-converter",
        "category": "Case Converters",
        "icon": "🔡",
        "desc": "Convert all alphabetical characters in your text to lowercase letters.",
        "formula": "Text = Text.toLowerCase()",
        "formula_desc": "Transforms characters by converting uppercase letters to lowercase equivalents.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Lowercase Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            document.getElementById('text-output').value = text.toLowerCase();
            updateBreakdown(`<p>Successfully converted all letters to lowercase format.</p>`);
        """
    },
    {
        "name": "Title Case Converter",
        "slug": "title-case-converter",
        "category": "Case Converters",
        "icon": "📛",
        "desc": "Format text with capitalized principal words for book, essay, or email titles.",
        "formula": "Cap(words) except minor prepositions",
        "formula_desc": "Capitalizes the first letter of major words while ignoring minor words like and, of, in.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Title Case Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const minorWords = ['a', 'an', 'the', 'and', 'but', 'for', 'or', 'nor', 'on', 'in', 'at', 'to', 'by', 'of', 'for', 'with', 'from', 'as'];
            const converted = text.toLowerCase().split(/(\\s+)/).map((word) => {
                if (word.trim() === '') return word;
                const cleanWord = word.toLowerCase();
                if (minorWords.includes(cleanWord)) return cleanWord;
                return word.charAt(0).toUpperCase() + word.slice(1);
            }).join('');
            
            // Capitalize first character anyway
            const firstLetterMatch = converted.match(/[a-zA-Z]/);
            let finalStr = converted;
            if (firstLetterMatch) {
                const idx = firstLetterMatch.index;
                finalStr = converted.slice(0, idx) + converted.charAt(idx).toUpperCase() + converted.slice(idx + 1);
            }
            document.getElementById('text-output').value = finalStr;
            updateBreakdown(`<p>Standard title-casing rules applied, preserving minor prepositions.</p>`);
        """
    },
    {
        "name": "Sentence Case Converter",
        "slug": "sentence-case-converter",
        "category": "Case Converters",
        "icon": "📝",
        "desc": "Capitalize the first letter of each sentence, setting others to lowercase.",
        "formula": "Cap(first letter of sentence)",
        "formula_desc": "Splits text on terminal punctuation marks and capitalizes the first alphabetical character.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Sentence Case Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.toLowerCase().replace(/(^\\s*|[.!?]\\s+)([a-z])/g, (match, separator, letter) => separator + letter.toUpperCase());
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Converted characters using punctuation boundaries to establish sentence starts.</p>`);
        """
    },
    {
        "name": "Toggle Case Converter",
        "slug": "toggle-case-converter",
        "category": "Case Converters",
        "icon": "🔄",
        "desc": "Invert the capitalization of every single letter in your text.",
        "formula": "Letter = Inverse(Capitalization)",
        "formula_desc": "Loops over letters and swaps uppercase with lowercase and vice-versa.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Toggle Case Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.split('').map(c => c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()).join('');
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Capitalization flags toggled across all letters.</p>`);
        """
    },
    {
        "name": "Capitalize Words Tool",
        "slug": "capitalize-words-tool",
        "category": "Case Converters",
        "icon": "🅰️",
        "desc": "Capitalize the first letter of every single word in your text.",
        "formula": "Cap(all words)",
        "formula_desc": "Capitalizes the first character of each space-delimited substring.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Capitalized Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.split(/(\\s+)/).map(word => {
                if (word.trim() === '') return word;
                return word.charAt(0).toUpperCase() + word.slice(1);
            }).join('');
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Capitalized every single isolated word token.</p>`);
        """
    },
    {
        "name": "camelCase Converter",
        "slug": "camelcase-converter",
        "category": "Case Converters",
        "icon": "🐪",
        "desc": "Convert text into camelCase variable naming convention style.",
        "formula": "camelCase formatting",
        "formula_desc": "Strips spaces and non-alphanumeric chars, and capitalizes subsequent word tokens.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "camelCase Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.replace(/[^a-zA-Z0-9]+(.)/g, (match, char) => char.toUpperCase()).replace(/^(.)/, match => match.toLowerCase());
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Rebuilt variables in camelCase layout format.</p>`);
        """
    },
    {
        "name": "PascalCase Converter",
        "slug": "pascalcase-converter",
        "category": "Case Converters",
        "icon": "📐",
        "desc": "Convert text to PascalCase format, popular for class structures in coding.",
        "formula": "PascalCase formatting",
        "formula_desc": "Strips symbols, and capitalizes all starting letters including the first word.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "PascalCase Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.replace(/[^a-zA-Z0-9]+(.)/g, (match, char) => char.toUpperCase()).replace(/^(.)/, match => match.toUpperCase());
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Rebuilt strings in PascalCase syntax.</p>`);
        """
    },
    {
        "name": "snake_case Converter",
        "slug": "snake-case-converter",
        "category": "Case Converters",
        "icon": "🐍",
        "desc": "Convert text into snake_case format, commonly used in database schema names.",
        "formula": "snake_case formatting",
        "formula_desc": "Converts string to lowercase and joins tokens with underscores.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "snake_case Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.trim().toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Formatted strings into lowercase underscore structure.</p>`);
        """
    },
    {
        "name": "kebab-case Converter",
        "slug": "kebab-case-converter",
        "category": "Case Converters",
        "icon": "🍢",
        "desc": "Convert text into kebab-case format, ideal for URL slug conventions.",
        "formula": "kebab-case formatting",
        "formula_desc": "Converts string to lowercase and joins word segments with hyphens.",
        "inputs": [
            {"id": "text-input", "label": "Enter or Paste your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "kebab-case Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const converted = text.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
            document.getElementById('text-output').value = converted;
            updateBreakdown(`<p>Formatted strings into lowercase hyphenated structure.</p>`);
        """
    }
]
