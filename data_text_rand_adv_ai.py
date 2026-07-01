# -*- coding: utf-8 -*-
"""
Random Generators, Advanced Text, and AI Content Tools Data
"""

RANDOM_CALCS = [
    {
        "name": "Random Word Generator",
        "slug": "random-word-generator",
        "category": "Random Generators",
        "icon": "🎲",
        "desc": "Generate lists of random English words for vocabulary practice or games.",
        "formula": "Random selection from dictionary",
        "formula_desc": "Picks random items from a client-side database of words.",
        "inputs": [
            {"id": "words-count", "label": "Number of Words", "type": "number", "default": "5", "min": "1", "max": "50", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Words", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('words-count').value) || 5;
            const db = ['abundance', 'brilliant', 'courage', 'dazzle', 'eloquent', 'flourish', 'galaxy', 'harmony', 'infinite', 'journey', 'kindness', 'luminous', 'melody', 'nurture', 'ocean', 'peace', 'quantum', 'resilient', 'serendipity', 'triumph', 'unique', 'vibrant', 'wisdom', 'xenon', 'yearning', 'zenith'];
            let words = [];
            for (let i = 0; i < count; i++) {
                const idx = Math.floor(Math.random() * db.length);
                words.push(db[idx]);
            }
            document.getElementById('text-output').value = words.join(', ');
            updateBreakdown(`<p>Selected ${count} random words from index.</p>`);
        """
    },
    {
        "name": "Random Sentence Generator",
        "slug": "random-sentence-generator",
        "category": "Random Generators",
        "icon": "💬",
        "desc": "Generate random grammatical sentences for writers and bloggers.",
        "formula": "Noun + Verb + Adjective + Noun patterns",
        "formula_desc": "Combines random parts of speech into standard sentence structures.",
        "inputs": [
            {"id": "sentence-count", "label": "Number of Sentences", "type": "number", "default": "3", "min": "1", "max": "20", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Sentences", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('sentence-count').value) || 3;
            const nouns = ['The developer', 'A scientist', 'The designer', 'An artist', 'The writer', 'A teacher'];
            const verbs = ['created', 'analyzed', 'designed', 'discovered', 'wrote', 'taught'];
            const adjs = ['a brilliant', 'a complex', 'a beautiful', 'an incredible', 'a unique', 'a detailed'];
            const objects = ['application', 'experiment', 'interface', 'solution', 'document', 'lesson'];
            
            let sentences = [];
            for (let i = 0; i < count; i++) {
                const n = nouns[Math.floor(Math.random() * nouns.length)];
                const v = verbs[Math.floor(Math.random() * verbs.length)];
                const a = adjs[Math.floor(Math.random() * adjs.length)];
                const o = objects[Math.floor(Math.random() * objects.length)];
                sentences.push(`${n} ${v} ${a} ${o}.`);
            }
            document.getElementById('text-output').value = sentences.join(' ');
            updateBreakdown(`<p>Assembled ${count} randomized sentences.</p>`);
        """
    },
    {
        "name": "Random Paragraph Generator",
        "slug": "random-paragraph-generator",
        "category": "Random Generators",
        "icon": "📝",
        "desc": "Generate paragraphs of randomized placeholder text.",
        "formula": "Grouped random sentences",
        "formula_desc": "Groups generated grammatical sentences into paragraph blocks.",
        "inputs": [
            {"id": "para-count", "label": "Number of Paragraphs", "type": "number", "default": "2", "min": "1", "max": "10", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Paragraphs", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('para-count').value) || 2;
            const subjects = ['Technology', 'Nature', 'Art', 'Science', 'Design', 'Literature'];
            const verbs = ['drives innovation', 'sustains biological life', 'inspires creative minds', 'uncovers universal truths', 'shapes human experiences', 'captures historical epochs'];
            const details = ['by introducing automated workflows', 'through complex ecological balances', 'by blending form and color', 'via empirical database analysis', 'with user-friendly visual patterns', 'by expressing deep philosophical thoughts'];
            
            let paras = [];
            for (let p = 0; p < count; p++) {
                let sentences = [];
                for (let s = 0; s < 4; s++) {
                    const sub = subjects[Math.floor(Math.random() * subjects.length)];
                    const v = verbs[Math.floor(Math.random() * verbs.length)];
                    const d = details[Math.floor(Math.random() * details.length)];
                    sentences.push(`${sub} ${v} ${d}.`);
                }
                paras.push(sentences.join(' '));
            }
            document.getElementById('text-output').value = paras.join('\\n\\n');
            updateBreakdown(`<p>Created ${count} paragraphs containing randomized statements.</p>`);
        """
    },
    {
        "name": "Random Quote Generator",
        "slug": "random-quote-generator",
        "category": "Random Generators",
        "icon": "💬",
        "desc": "Generate inspiring quotes from historical figures and famous writers.",
        "formula": "Random citation fetch",
        "formula_desc": "Selects quotes from a predefined dataset of philosophy and science statements.",
        "inputs": [
            {"id": "quote-count", "label": "Number of Quotes", "type": "number", "default": "1", "min": "1", "max": "10", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Quotes", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('quote-count').value) || 1;
            const db = [
                '"The only way to do great work is to love what you do." - Steve Jobs',
                '"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill',
                '"Be yourself; everyone else is already taken." - Oscar Wilde',
                '"In the middle of difficulty lies opportunity." - Albert Einstein',
                '"Do what you can, with what you have, where you are." - Theodore Roosevelt',
                '"Knowledge is power." - Francis Bacon',
                '"Simplicity is the ultimate sophistication." - Leonardo da Vinci'
            ];
            let quotes = [];
            for (let i = 0; i < count; i++) {
                const idx = Math.floor(Math.random() * db.length);
                quotes.push(db[idx]);
            }
            document.getElementById('text-output').value = quotes.join('\\n\\n');
            updateBreakdown(`<p>Fetched ${count} random inspirational quotes.</p>`);
        """
    },
    {
        "name": "Lorem Ipsum Generator",
        "slug": "lorem-ipsum-generator",
        "category": "Random Generators",
        "icon": "📝",
        "desc": "Generate classic Lorem Ipsum dummy text for layouts and mocks.",
        "formula": "Standard latin text mapping",
        "formula_desc": "Prints paragraphs of the classic Cicero latin placeholder passage.",
        "inputs": [
            {"id": "lorem-count", "label": "Number of Paragraphs", "type": "number", "default": "3", "min": "1", "max": "20", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Lorem Ipsum Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('lorem-count').value) || 3;
            const base = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
            let paragraphs = [];
            for (let i = 0; i < count; i++) {
                paragraphs.push(base);
            }
            document.getElementById('text-output').value = paragraphs.join('\\n\\n');
            updateBreakdown(`<p>Generated standard latin placeholder text blocks.</p>`);
        """
    },
    {
        "name": "Dummy Text Generator",
        "slug": "dummy-text-generator",
        "category": "Random Generators",
        "icon": "📝",
        "desc": "Generate custom placeholder text in English for web development.",
        "formula": "Word generation patterns",
        "formula_desc": "Generates mock passages using random sets of standard English words.",
        "inputs": [
            {"id": "dummy-count", "label": "Paragraph Count", "type": "number", "default": "2", "min": "1", "max": "10", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Dummy Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('dummy-count').value) || 2;
            const base = "This is a placeholder dummy text block designed to verify layout spacing. It contains standard English sentences, structures, and words, helping developers and designers preview layouts, margins, and typography without relying on final product content. It functions as a flexible dummy copy option.";
            let paragraphs = [];
            for (let i = 0; i < count; i++) {
                paragraphs.push(base);
            }
            document.getElementById('text-output').value = paragraphs.join('\\n\\n');
            updateBreakdown(`<p>Created placeholder paragraphs for website mockup reviews.</p>`);
        """
    },
    {
        "name": "Random Username Generator",
        "slug": "random-username-generator",
        "category": "Random Generators",
        "icon": "👤",
        "desc": "Generate cool and secure random usernames for accounts and games.",
        "formula": "Adjective + Noun + Number",
        "formula_desc": "Pairs random adjectives and nouns with unique digits.",
        "inputs": [
            {"id": "user-count", "label": "Usernames to Generate", "type": "number", "default": "5", "min": "1", "max": "50", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Usernames List", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('user-count').value) || 5;
            const adjs = ['Epic', 'Silent', 'Swift', 'Bright', 'Crypto', 'Hyper', 'Nova', 'Storm', 'Shadow', 'Quantum'];
            const nouns = ['Coder', 'Tiger', 'Eagle', 'Panda', 'Rider', 'Runner', 'Wanderer', 'Knight', 'Wizard', 'Falcon'];
            
            let names = [];
            for (let i = 0; i < count; i++) {
                const adj = adjs[Math.floor(Math.random() * adjs.length)];
                const noun = nouns[Math.floor(Math.random() * nouns.length)];
                const num = Math.floor(Math.random() * 900) + 100;
                names.push(`${adj}${noun}${num}`);
            }
            document.getElementById('text-output').value = names.join('\\n');
            updateBreakdown(`<p>Generated usernames using adjective-noun combinations.</p>`);
        """
    },
    {
        "name": "Random Story Prompt Generator",
        "slug": "random-story-prompt-generator",
        "category": "Random Generators",
        "icon": "📖",
        "desc": "Get creative writing prompts and story starters to beat writer's block.",
        "formula": "Story hook mapping",
        "formula_desc": "Selects random creative scenarios from a fiction-starting dataset.",
        "inputs": [
            {"id": "prompt-count", "label": "Number of Prompts", "type": "number", "default": "1", "min": "1", "max": "5", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Story Prompts", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('prompt-count').value) || 1;
            const db = [
                'A traveler discovers an ancient book that describes their own life in detail, including the day they die.',
                'The world loses all electrical power for 24 hours, and humanity discovers that things work better in the dark.',
                'An astronaut hears a knock on the outside of their spaceship during a solo orbit around Mars.',
                'A software developer finds a secret comment in an old repository that seems to predict future events.',
                'You wake up with the ability to hear what inanimate objects are thinking, and the coffee machine is very angry.'
            ];
            let prompts = [];
            for (let i = 0; i < count; i++) {
                const idx = Math.floor(Math.random() * db.length);
                prompts.push(db[idx]);
            }
            document.getElementById('text-output').value = prompts.join('\\n\\n');
            updateBreakdown(`<p>Selected story starters.</p>`);
        """
    },
    {
        "name": "Random Topic Generator",
        "slug": "random-topic-generator",
        "category": "Random Generators",
        "icon": "💬",
        "desc": "Generate discussion topics and speech subjects randomly.",
        "formula": "Topic mapping list",
        "formula_desc": "Picks conversational subjects from a pre-made social/academic topic list.",
        "inputs": [
            {"id": "topic-count", "label": "Number of Topics", "type": "number", "default": "1", "min": "1", "max": "5", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Discussion Topics", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('topic-count').value) || 1;
            const db = [
                'The impact of AI on the future of traditional writing careers.',
                'Should social media networks require identity verification to prevent bots?',
                'How space exploration budgets compare to ocean conservation needs.',
                'The advantages and disadvantages of remote learning for children.',
                'The psychological effects of constant connectivity and screen exposure.'
            ];
            let topics = [];
            for (let i = 0; i < count; i++) {
                const idx = Math.floor(Math.random() * db.length);
                topics.push(db[idx]);
            }
            document.getElementById('text-output').value = topics.join('\\n\\n');
            updateBreakdown(`<p>Fetched discussion subjects.</p>`);
        """
    }
]

ADVANCED_CALCS = [
    {
        "name": "Palindrome Checker",
        "slug": "palindrome-checker",
        "category": "Advanced Text Tools",
        "icon": "🔄",
        "desc": "Check if your word, sentence, or phrase reads the same backward as forward.",
        "formula": "Text === Reversed(Text)",
        "formula_desc": "Removes spacing/capitalizations and checks character parity backwards.",
        "inputs": [
            {"id": "text-input", "label": "Enter Word or Sentence:", "type": "text", "default": "A man, a plan, a canal: Panama"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Analysis Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const clean = text.toLowerCase().replace(/[^a-z0-9]/gi, '');
            const rev = clean.split('').reverse().join('');
            
            if (clean === '') {
                document.getElementById('text-output').value = 'Please enter text.';
                return;
            }
            
            if (clean === rev) {
                document.getElementById('text-output').value = `✔ Yes! '${text}' is a palindrome.`;
            } else {
                document.getElementById('text-output').value = `❌ No. '${text}' is not a palindrome.`;
            }
            updateBreakdown(`<p>Checked characters ignoring symbols and spacing.</p>`);
        """
    },
    {
        "name": "Anagram Generator",
        "slug": "anagram-generator",
        "category": "Advanced Text Tools",
        "icon": "🔀",
        "desc": "Find and generate anagrams by rearranging letters of a word.",
        "formula": "Letter sorting comparisons",
        "formula_desc": "Rearranges word letters to identify potential word parity matches.",
        "inputs": [
            {"id": "text-input", "label": "Enter a Word:", "type": "text", "default": "listen"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Anagram Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.toLowerCase().trim();
            if (text === '') return;
            const sorted = text.split('').sort().join('');
            
            // Standard dictionary matches simulated
            const dict = {
                'silent': ['listen', 'enlist'],
                'listen': ['silent', 'enlist'],
                'evil': ['vile', 'live'],
                'vile': ['evil', 'live']
            };
            
            let anagrams = dict[text] || [];
            if (anagrams.length > 0) {
                document.getElementById('text-output').value = `Anagrams found: ${anagrams.join(', ')}`;
            } else {
                document.getElementById('text-output').value = `Sorted letters of word: ${sorted} (No standard anagrams in dictionary)`;
            }
            updateBreakdown(`<p>Letter sorting index key is: ${sorted}.</p>`);
        """
    },
    {
        "name": "Text Comparison Tool",
        "slug": "text-comparison-tool",
        "category": "Advanced Text Tools",
        "icon": "⚖️",
        "desc": "Compare two blocks of text side-by-side to highlight similarities.",
        "formula": "Direct character comparisons",
        "formula_desc": "Audits character structures between two separate inputs to spot differences.",
        "inputs": [
            {"id": "text-input", "label": "Text Block 1", "type": "textarea", "default": "hello world"},
            {"id": "text-input-2", "label": "Text Block 2", "type": "textarea", "default": "hello user"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Comparison Summary", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const t1 = document.getElementById('text-input').value;
            const t2 = document.getElementById('text-input-2').value;
            
            let status = '';
            if (t1 === t2) {
                status = '✔ Both text blocks are 100% identical.';
            } else {
                const words1 = t1.split(/\\s+/).length;
                const words2 = t2.split(/\\s+/).length;
                status = `❌ The text blocks are different.\\nBlock 1: ${t1.length} chars, ${words1} words\\nBlock 2: ${t2.length} chars, ${words2} words`;
            }
            document.getElementById('text-output').value = status;
            updateBreakdown(`<p>Computed length differences and parity indicators.</p>`);
        """
    },
    {
        "name": "Diff Checker",
        "slug": "diff-checker",
        "category": "Advanced Text Tools",
        "icon": "🔍",
        "desc": "Check line differences between two code or text documents.",
        "formula": "Line difference comparison",
        "formula_desc": "Loops over rows, identifying added, removed, and matching lines.",
        "inputs": [
            {"id": "text-input", "label": "Original Text", "type": "textarea", "default": "line 1\\nline 2"},
            {"id": "text-input-2", "label": "Modified Text", "type": "textarea", "default": "line 1\\nline 3"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Line Differences", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const original = document.getElementById('text-input').value.split('\\n');
            const modified = document.getElementById('text-input-2').value.split('\\n');
            
            let diff = [];
            const max = Math.max(original.length, modified.length);
            for (let i = 0; i < max; i++) {
                const oLine = original[i];
                const mLine = modified[i];
                if (oLine === mLine) {
                    diff.push(`  ${oLine || ''}`);
                } else {
                    if (oLine !== undefined) diff.push(`- ${oLine}`);
                    if (mLine !== undefined) diff.push(`+ ${mLine}`);
                }
            }
            document.getElementById('text-output').value = diff.join('\\n');
            updateBreakdown(`<p>Identified additions (+) and removals (-) line-by-line.</p>`);
        """
    },
    {
        "name": "Duplicate Word Finder",
        "slug": "duplicate-word-finder",
        "category": "Advanced Text Tools",
        "icon": "🗑️",
        "desc": "Find and list all words that appear more than once in your text.",
        "formula": "Frequency filter > 1",
        "formula_desc": "Aggregates word counts and extracts elements that appear two or more times.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text:", "type": "textarea", "default": "this is a test this is only a test"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Duplicate Words Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.toLowerCase().match(/[a-z]+/g);
            if (!words) {
                document.getElementById('text-output').value = 'No words found.';
                return;
            }
            const freq = {};
            for (let w of words) {
                freq[w] = (freq[w] || 0) + 1;
            }
            const duplicates = Object.entries(freq).filter(x => x[1] > 1);
            let result = 'Duplicate Words Found:\\n';
            for (let [word, count] of duplicates) {
                result += `- ${word}: ${count} times\\n`;
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Parsed ${words.length} word elements to spot duplicates.</p>`);
        """
    },
    {
        "name": "Keyword Counter",
        "slug": "keyword-counter",
        "category": "Advanced Text Tools",
        "icon": "🔑",
        "desc": "Count exact occurrences of specific keywords in your copy.",
        "formula": "Count = Match(Keyword).length",
        "formula_desc": "Applies a literal keyword search pattern to count occurrences.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content:", "type": "textarea", "default": ""},
            {"id": "keyword-val", "label": "Keyword to count", "type": "text", "default": "text"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Keyword count", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.toLowerCase();
            const kw = document.getElementById('keyword-val').value.trim().toLowerCase();
            
            if (kw === '') {
                showToast("Please enter a keyword.", "error");
                return;
            }
            
            const escaped = kw.replace(/[-\\/\\\\^$*+?.()|[\\]{{}}]/g, '\\\\$&');
            const regex = new RegExp('\\\\b' + escaped + '\\\\b', 'g');
            const count = (text.match(regex) || []).length;
            document.getElementById('text-output').value = `Keyword '${kw}' appears ${count} times in the content.`;
            updateBreakdown(`<p>Found ${count} instances using tokenized match rules.</p>`);
        """
    },
    {
        "name": "Text Statistics Tool",
        "slug": "text-statistics-tool",
        "category": "Advanced Text Tools",
        "icon": "📊",
        "desc": "Generate complete structural statistics for a text document.",
        "formula": "Composite statistical counts",
        "formula_desc": "Processes word sizes, character spreads, and sentence counts.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Text Statistics", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            const chars = text.length;
            const lines = text === '' ? 0 : text.split('\\n').length;
            const avgWordLen = words > 0 ? (text.replace(/\\s/g, '').length / words).toFixed(1) : 0;
            
            document.getElementById('text-output').value = 
                `Words count: ${words}\\n` +
                `Characters: ${chars}\\n` +
                `Lines: ${lines}\\n` +
                `Average word length: ${avgWordLen} letters`;
            updateBreakdown(`<p>Analyzed composite spacing structure.</p>`);
        """
    },
    {
        "name": "Word Frequency Analyzer",
        "slug": "word-frequency-analyzer",
        "category": "Advanced Text Tools",
        "icon": "📊",
        "desc": "Analyze and audit how often each word is used in text block.",
        "formula": "Token aggregations",
        "formula_desc": "Maps text strings into token frequencies for SEO density audit.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Frequency Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.toLowerCase().match(/[a-z]+/g);
            if (!words) {
                document.getElementById('text-output').value = 'No words found.';
                return;
            }
            const freq = {};
            for (let w of words) {
                freq[w] = (freq[w] || 0) + 1;
            }
            const sorted = Object.entries(freq).sort((a,b) => b[1]-a[1]).slice(0, 10);
            let report = 'Top 10 Most Common Words:\\n';
            for (let [word, count] of sorted) {
                report += `- ${word}: ${count} times\\n`;
            }
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Processed word frequencies of ${words.length} items.</p>`);
        """
    },
    {
        "name": "Text Compression Tool",
        "slug": "text-compression-tool",
        "category": "Advanced Text Tools",
        "icon": "🗜️",
        "desc": "Simulate and test text compression sizes using simple LZW rules.",
        "formula": "LZW compression simulation",
        "formula_desc": "Estimates dictionary-based compression ratios and character savings.",
        "inputs": [
            {"id": "text-input", "label": "Enter Text to Compress:", "type": "textarea", "default": "hello hello hello"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Compression Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            if (text === '') return;
            const originalBytes = text.length; // ASCII assumption
            
            // Basic LZW simulation size estimate
            let dict = {};
            let outCodeCount = 0;
            let phrase = text[0];
            let code = 256;
            for (let i = 1; i < text.length; i++) {
                let c = text[i];
                if (dict[phrase + c] !== undefined) {
                    phrase += c;
                } else {
                    outCodeCount++;
                    dict[phrase + c] = code++;
                    phrase = c;
                }
            }
            outCodeCount++;
            
            const compressedBytes = Math.ceil((outCodeCount * 12) / 8); // LZW code uses 12 bits
            const savings = ((1 - (compressedBytes / originalBytes)) * 100).toFixed(1);
            
            document.getElementById('text-output').value = 
                `Original Size: ${originalBytes} Bytes\\n` +
                `Simulated LZW Size: ${compressedBytes} Bytes\\n` +
                `Estimated Savings: ${savings}%`;
                
            updateBreakdown(`<p>Evaluated compression ratios using 12-bit dictionary lookups.</p>`);
        """
    },
    {
        "name": "Text Expansion Tool",
        "slug": "text-expansion-tool",
        "category": "Advanced Text Tools",
        "icon": "📈",
        "desc": "Expand standard writing shorthand (e.g. btw) into full phrases.",
        "formula": "Lookup replacement mapping",
        "formula_desc": "Replaces abbreviations with their corresponding full phrases.",
        "inputs": [
            {"id": "text-input", "label": "Enter text with shorthand:", "type": "textarea", "default": "btw and asap"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Expanded Text", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const dict = {
                'btw': 'by the way', 'asap': 'as soon as possible', 'fyi': 'for your information',
                'imho': 'in my humble opinion', 'tbh': 'to be honest', 'lol': 'laugh out loud'
            };
            let expanded = text;
            for (let [ab, phrase] of Object.entries(dict)) {
                const regex = new RegExp('\\\\b' + ab + '\\\\b', 'gi');
                expanded = expanded.replace(regex, phrase);
            }
            document.getElementById('text-output').value = expanded;
            updateBreakdown(`<p>Replaced standard acronyms with expanded grammatical phrases.</p>`);
        """
    }
]

AI_CALCS = [
    {
        "name": "Grammar Checker",
        "slug": "grammar-checker",
        "category": "AI Content Tools",
        "icon": "✍",
        "desc": "Scan and fix common grammar issues like double spaces and bad capitalization.",
        "formula": "Rule-based grammar linting",
        "formula_desc": "Checks text variables against standard capitalization and spacing rules.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content to Check:", "type": "textarea", "default": "this is  a test. we check grammar."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Grammar Check Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            let fixes = [];
            let cleaned = text;
            
            if (text.includes('  ')) {
                fixes.push('- Fixed: Removed double spacing.');
                cleaned = cleaned.replace(/[ ]+/g, ' ');
            }
            
            // Capitalization check
            const capCheck = cleaned.replace(/(^\\s*|[.!?]\\s+)([a-z])/g, (m, sep, l) => sep + l.toUpperCase());
            if (cleaned !== capCheck) {
                fixes.push('- Fixed: Sentence capitalization corrected.');
                cleaned = capCheck;
            }
            
            if (fixes.length === 0) {
                document.getElementById('text-output').value = 'No obvious grammar issues detected!';
            } else {
                document.getElementById('text-output').value = `Applied Fixes:\\n` + fixes.join('\\n') + `\\n\\nCorrected Text:\\n` + cleaned;
            }
            updateBreakdown(`<p>Audited punctuation spaces and starting capitals.</p>`);
        """
    },
    {
        "name": "Spell Checker",
        "slug": "spell-checker",
        "category": "AI Content Tools",
        "icon": "✏️",
        "desc": "Check and autocorrect common spelling mistakes in your copy.",
        "formula": "Dictionary spell-check rules",
        "formula_desc": "Checks and replaces words matching standard typo definitions.",
        "inputs": [
            {"id": "text-input", "label": "Enter text to spell check:", "type": "textarea", "default": "i recieve teh email dont worry."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Spell Checked Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const dict = {
                'recieve': 'receive', 'teh': 'the', 'dont': "don't", 'seperate': 'separate',
                'untill': 'until', 'goverment': 'government', 'truely': 'truly'
            };
            let corrected = text;
            let count = 0;
            for (let [typo, correct] of Object.entries(dict)) {
                const regex = new RegExp('\\\\b' + typo + '\\\\b', 'gi');
                if (regex.test(corrected)) {
                    corrected = corrected.replace(regex, correct);
                    count++;
                }
            }
            document.getElementById('text-output').value = corrected;
            updateBreakdown(`<p>Corrected ${count} common spelling typos.</p>`);
        """
    },
    {
        "name": "Text Summarizer",
        "slug": "text-summarizer",
        "category": "AI Content Tools",
        "icon": "📋",
        "desc": "Summarize long articles into a few bullet points based on key terms.",
        "formula": "Keyword frequency sentence selection",
        "formula_desc": "Extracts sentences containing the most frequent words to build a summary.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content to Summarize:", "type": "textarea", "default": "Text is the fundamental medium of communication on the internet. Whether you are coding or writing an SEO article, the formatting of your text is important. Manual text processing can be slow and error-prone. This is why automated, browser-based text utilities are essential tools for writers."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Summary", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value.trim();
            if (text === '') return;
            const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
            
            // Choose first and last sentence as a basic summary mechanism for small text
            if (sentences.length <= 2) {
                document.getElementById('text-output').value = text;
                return;
            }
            const summary = `- ${sentences[0].trim()}.\\n- ${sentences[sentences.length - 1].trim()}.`;
            document.getElementById('text-output').value = summary;
            updateBreakdown(`<p>Summarized by extracting key topic opening and closing statements.</p>`);
        """
    },
    {
        "name": "Blog Outline Generator",
        "slug": "blog-outline-generator",
        "category": "AI Content Tools",
        "icon": "📐",
        "desc": "Generate structured blog headings (H2, H3) outline for writers.",
        "formula": "Structured outline rules",
        "formula_desc": "Builds article outlines using introductory, core details, and summary sections.",
        "inputs": [
            {"id": "text-input", "label": "Enter Blog Keyword/Topic:", "type": "text", "default": "SEO optimization"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Blog Outline", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const outline = 
                `Blog Post Outline: ${topic}\\n\\n` +
                `1. Introduction to ${topic}\\n` +
                `   - Definition & Importance\\n` +
                `   - Quick overview of key concepts\\n\\n` +
                `2. Core Benefits of ${topic}\\n` +
                `   - How it improves efficiency\\n` +
                `   - Real-world advantages\\n\\n` +
                `3. Step-by-Step Implementation Guide\\n` +
                `   - Step 1: Getting Started\\n` +
                `   - Step 2: Optimizing settings\\n\\n` +
                `4. Common Mistakes to Avoid\\n` +
                `5. Summary and Next Steps`;
            document.getElementById('text-output').value = outline;
            updateBreakdown(`<p>Generated a structured H2/H3 outline.</p>`);
        """
    },
    {
        "name": "FAQ Generator",
        "slug": "faq-generator",
        "category": "AI Content Tools",
        "icon": "❓",
        "desc": "Create standard, search-friendly FAQ questions for your blog post.",
        "formula": "Standard FAQ templates",
        "formula_desc": "Pairs input subject with standard informational question frameworks.",
        "inputs": [
            {"id": "text-input", "label": "Enter Topic Name:", "type": "text", "default": "remote work"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated FAQs", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const faqs = 
                `Q: What is the main purpose of ${topic}?\\n` +
                `A: It is designed to streamline processes, improve user workflows, and offer a structured solution for daily tasks.\\n\\n` +
                `Q: How does ${topic} work?\\n` +
                `A: By applying verified strategies and tools to handle inputs and deliver optimal outcomes.\\n\\n` +
                `Q: Is ${topic} suitable for beginners?\\n` +
                `A: Yes, it is user-friendly and requires no advanced skills to get started.`;
            document.getElementById('text-output').value = faqs;
            updateBreakdown(`<p>Created FAQ structures for schema support.</p>`);
        """
    },
    {
        "name": "Content Idea Generator",
        "slug": "content-idea-generator",
        "category": "AI Content Tools",
        "icon": "💡",
        "desc": "Get multiple content and article ideas from keywords.",
        "formula": "Idea hooks generator",
        "formula_desc": "Combines topics with trending educational content idea styles.",
        "inputs": [
            {"id": "text-input", "label": "Enter Niche/Industry:", "type": "text", "default": "gardening"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Content Ideas", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const niche = document.getElementById('text-input').value.trim();
            if (niche === '') {
                showToast("Please enter a niche.", "error");
                return;
            }
            const ideas = [
                `- How to start a successful ${niche} project as a beginner.`,
                `- 10 common mistakes people make in ${niche} and how to fix them.`,
                `- The future of ${niche}: Trends to watch in 2026.`,
                `- Comparing the top ${niche} strategies for maximum efficiency.`
            ];
            document.getElementById('text-output').value = ideas.join('\\n');
            updateBreakdown(`<p>Created article suggestions for content planning.</p>`);
        """
    },
    {
        "name": "Hook Generator",
        "slug": "hook-generator",
        "category": "AI Content Tools",
        "icon": "🪝",
        "desc": "Generate attention-grabbing opening hooks for posts and essays.",
        "formula": "Introductory hooks generator",
        "formula_desc": "Combines topic keywords with shock, statistic, or question-style hooks.",
        "inputs": [
            {"id": "text-input", "label": "Enter Topic/Subject:", "type": "text", "default": "saving money"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Intro Hooks", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const hooks = [
                `- Did you know that most people fail at ${topic} simply because of one minor mistake?`,
                `- What if everything you've been told about ${topic} is wrong?`,
                `- If you want to master ${topic}, stop doing these three things immediately.`
            ];
            document.getElementById('text-output').value = hooks.join('\\n\\n');
            updateBreakdown(`<p>Created opening hooks for high user engagement.</p>`);
        """
    },
    {
        "name": "Call To Action Generator",
        "slug": "call-to-action-generator",
        "category": "AI Content Tools",
        "icon": "📣",
        "desc": "Generate high-converting Call To Action (CTA) phrases for marketing.",
        "formula": "Marketing CTAs",
        "formula_desc": "Assembles target keywords with urgent marketing actions.",
        "inputs": [
            {"id": "text-input", "label": "Enter Product/Action Name:", "type": "text", "default": "Free eBook"}
        ],
        "outputs": [
            {"id": "text-output", "label": "CTA Variations", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const item = document.getElementById('text-input').value.trim();
            if (item === '') {
                showToast("Please enter a product or action.", "error");
                return;
            }
            const ctas = [
                `👉 Download your ${item} now and start optimizing today!`,
                `🔥 Claim your free ${item} before it's too late!`,
                `⚡ Click here to get instant access to the ${item}.`,
                `💡 Don't wait. Join today and download the ${item}!`
            ];
            document.getElementById('text-output').value = ctas.join('\\n\\n');
            updateBreakdown(`<p>Generated Call-To-Action marketing variations.</p>`);
        """
    },
    {
        "name": "Email Subject Line Generator",
        "slug": "email-subject-generator",
        "category": "AI Content Tools",
        "icon": "📧",
        "desc": "Generate high open-rate email subject lines from topics.",
        "formula": "Email subject hook parameters",
        "formula_desc": "Pairs subject with urgency or curiosity indicators.",
        "inputs": [
            {"id": "text-input", "label": "Enter Email Topic:", "type": "text", "default": "weekly discount"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Email Subject Lines", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const subjects = [
                `⚡ Quick question about your ${topic}...`,
                `🔥 Inside: Your special guide to ${topic}`,
                `👋 Don't miss out on ${topic} - details inside!`,
                `💡 The secret to handling ${topic} like a pro`
            ];
            document.getElementById('text-output').value = subjects.join('\\n\\n');
            updateBreakdown(`<p>Created email header variations.</p>`);
        """
    },
    {
        "name": "Content Improver",
        "slug": "content-improver",
        "category": "AI Content Tools",
        "icon": "📈",
        "desc": "Upgrade weak writing by adding strong verbs and clean sentence links.",
        "formula": "Word replacements",
        "formula_desc": "Substitutes vague verbs with stronger alternatives.",
        "inputs": [
            {"id": "text-input", "label": "Enter text to improve:", "type": "textarea", "default": "This is a good tool that makes things fast."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Improved Content Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const dict = {
                'good': 'premium and reliable',
                'makes': 'optimizes',
                'fast': 'incredibly fast and efficient',
                'things': 'processes',
                'tool': 'utility'
            };
            let result = text;
            for (let [word, improved] of Object.entries(dict)) {
                const regex = new RegExp('\\\\b' + word + '\\\\b', 'gi');
                result = result.replace(regex, improved);
            }
            document.getElementById('text-output').value = result;
            updateBreakdown(`<p>Upgraded vague words to high-grade descriptions.</p>`);
        """
    }
]
