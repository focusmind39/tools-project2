# -*- coding: utf-8 -*-
"""
SEO Text and Content Writing Tools Data
"""

SEO_TEXT_CALCS = [
    {
        "name": "Keyword Density Checker",
        "slug": "keyword-density-checker",
        "category": "SEO Text Tools",
        "icon": "🔑",
        "desc": "Check keyword density percentage and word frequency in your website content.",
        "formula": "Density = (Word Count / Total Words) * 100",
        "formula_desc": "Computes density values for single words and multi-word phrases.",
        "inputs": [
            {"id": "text-input", "label": "Enter your Content:", "type": "textarea", "default": ""},
            {"id": "min-len", "label": "Minimum Word Length", "type": "number", "default": "4", "min": "1", "max": "10", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Density Report", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const minLen = parseInt(document.getElementById('min-len').value) || 4;
            
            const words = text.toLowerCase().match(/[a-z0-9]+/g);
            if (!words) {
                document.getElementById('text-output').value = 'No words found.';
                return;
            }
            
            const total = words.length;
            const freq = {};
            for (let w of words) {
                if (w.length >= minLen) {
                    freq[w] = (freq[w] || 0) + 1;
                }
            }
            
            const sorted = Object.entries(freq).sort((a,b) => b[1] - a[1]).slice(0, 15);
            let report = `Total Words: ${total}\\n\\nTop Keywords Density:\\n`;
            for (let [word, count] of sorted) {
                const pct = ((count / total) * 100).toFixed(2);
                report += `- ${word}: count = ${count}, density = ${pct}%\\n`;
            }
            
            document.getElementById('text-output').value = report;
            updateBreakdown(`<p>Analyzed density for words with length >= ${minLen} characters.</p>`);
        """
    },
    {
        "name": "Meta Description Length Checker",
        "slug": "meta-description-length-checker",
        "category": "SEO Text Tools",
        "icon": "📏",
        "desc": "Verify if your meta description fits the Google 120-160 character limit guidelines.",
        "formula": "120 <= Char Count <= 160",
        "formula_desc": "Checks length and provides status warnings based on desktop/mobile limits.",
        "inputs": [
            {"id": "text-input", "label": "Enter Meta Description:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Suitability Status", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const chars = text.length;
            let status = '';
            if (chars === 0) {
                status = 'Status: Empty';
            } else if (chars < 120) {
                status = `Status: Too Short (${chars} chars). Recommended range: 120 to 160 characters.`;
            } else if (chars <= 160) {
                status = `Status: Perfect! (${chars} chars). Optimal for Google search snippet presentation.`;
            } else {
                status = `Status: Too Long (${chars} chars). Google may truncate it. Keep it under 160 chars.`;
            }
            document.getElementById('text-output').value = status;
            updateBreakdown(`<p>Desktop limits generally target 160 characters, while mobile screens truncate around 120 characters.</p>`);
        """
    },
    {
        "name": "Title Length Checker",
        "slug": "title-length-checker",
        "category": "SEO Text Tools",
        "icon": "🏷️",
        "desc": "Check your SEO meta title length against the optimal 50-60 character limits.",
        "formula": "50 <= Char Count <= 60",
        "formula_desc": "Calculates title tag lengths to verify alignment with Google SERP pixel dimensions.",
        "inputs": [
            {"id": "text-input", "label": "Enter SEO Title Tag:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Title Tag Status", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const chars = text.length;
            let status = '';
            if (chars === 0) {
                status = 'Status: Empty';
            } else if (chars < 50) {
                status = `Status: Too Short (${chars} chars). Recommended length: 50 to 60 characters for best display.`;
            } else if (chars <= 60) {
                status = `Status: Perfect! (${chars} chars). Fits nicely in standard SERP titles.`;
            } else {
                status = `Status: Too Long (${chars} chars). Will likely be truncated by Google. Keep it under 60.`;
            }
            document.getElementById('text-output').value = status;
            updateBreakdown(`<p>Search snippets generally display the first 60 characters of a web title.</p>`);
        """
    },
    {
        "name": "Word Frequency Counter",
        "slug": "word-frequency-counter",
        "category": "SEO Text Tools",
        "icon": "📊",
        "desc": "Count the frequency of each word in your text, sorting by popularity.",
        "formula": "Word counts sorted descending",
        "formula_desc": "Collates all word occurrences and prints a frequency count descending list.",
        "inputs": [
            {"id": "text-input", "label": "Enter your Text:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Word Frequencies", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.toLowerCase().match(/[a-z0-9]+/g);
            if (!words) {
                document.getElementById('text-output').value = 'No words found.';
                return;
            }
            const freq = {};
            for (let w of words) {
                freq[w] = (freq[w] || 0) + 1;
            }
            const sorted = Object.entries(freq).sort((a,b) => b[1] - a[1]);
            let output = 'Word Frequency List:\\n';
            for (let [word, count] of sorted) {
                output += `${word}: ${count}\\n`;
            }
            document.getElementById('text-output').value = output;
            updateBreakdown(`<p>Processed ${words.length} words and found ${sorted.length} unique tokens.</p>`);
        """
    },
    {
        "name": "Text Readability Checker",
        "slug": "text-readability-checker",
        "category": "SEO Text Tools",
        "icon": "📖",
        "desc": "Measure readability based on the Flesch-Kincaid Reading Ease formula.",
        "formula": "206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)",
        "formula_desc": "Evaluates readability where higher scores represent easier reading content.",
        "inputs": [
            {"id": "text-input", "label": "Enter your Text:", "type": "textarea", "default": "Paste a paragraph of text to analyze readability."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Readability Index Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const cleanText = text.trim();
            if (cleanText === '') {
                document.getElementById('text-output').value = 'Please enter some text.';
                return;
            }
            
            const words = cleanText.split(/\\s+/).length;
            const sentences = cleanText.split(/[.!?]+/).filter(s => s.trim().length > 0).length || 1;
            
            // Simple syllable counter helper
            const countSyllables = (word) => {
                let w = word.toLowerCase().replace(/[^a-z]/g, '');
                if (w.length <= 3) return 1;
                w = w.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, '');
                w = w.replace(/^y/, '');
                const matches = w.match(/[aeiouy]{1,2}/g);
                return matches ? matches.length : 1;
            };
            
            const syllables = cleanText.split(/\\s+/).reduce((sum, word) => sum + countSyllables(word), 0);
            const score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words);
            
            let level = '';
            if (score > 90) level = 'Very Easy (5th grade level)';
            else if (score > 80) level = 'Easy (6th grade level)';
            else if (score > 70) level = 'Fairly Easy (7th grade level)';
            else if (score > 60) level = 'Standard/Plain English (8th-9th grade)';
            else if (score > 50) level = 'Fairly Difficult (High School)';
            else if (score > 30) level = 'Difficult (College Student)';
            else level = 'Very Difficult (College Graduate)';

            document.getElementById('text-output').value = 
                `Flesch Reading Ease Score: ${score.toFixed(2)}\\n` +
                `Readability Level: ${level}\\n` +
                `Words: ${words} | Sentences: ${sentences} | Syllables: ${syllables}`;
            
            updateBreakdown(`<p>Computed Flesch-Kincaid indicators via character patterns and syllables.</p>`);
        """
    },
    {
        "name": "SEO Content Analyzer",
        "slug": "seo-content-analyzer",
        "category": "SEO Text Tools",
        "icon": "🔍",
        "desc": "Run content audits for target word limits, headings, and readability.",
        "formula": "Composite SEO check rules",
        "formula_desc": "Evaluates word count limits, sentence structures, and formatting metrics.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content to Analyze:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "SEO Content Analysis", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            const chars = text.length;
            
            let issues = [];
            if (words < 300) {
                issues.push("- Warning: Content is thin (< 300 words). Add more details for better indexing.");
            } else if (words >= 1000) {
                issues.push("+ Perfect: Deep SEO length (> 1000 words).");
            } else {
                issues.push("+ Good: Standard length (300-1000 words).");
            }
            
            const longSentences = text.split(/[.!?]+/).filter(s => s.trim().split(/\\s+/).length > 25).length;
            if (longSentences > 0) {
                issues.push(`- Optimization: Found ${longSentences} sentences longer than 25 words. Consider shortening them.`);
            } else {
                issues.push("+ Excellent: Readability is high, all sentences are short and clear.");
            }
            
            document.getElementById('text-output').value = `SEO Analysis Report:\\n\\n` + issues.join('\\n');
            updateBreakdown(`<p>Analyzed text against standard content writing practices.</p>`);
        """
    },
    {
        "name": "Keyword Extractor",
        "slug": "keyword-extractor",
        "category": "SEO Text Tools",
        "icon": "🏷️",
        "desc": "Extract important keywords and phrases from your text content.",
        "formula": "Token parsing & filter",
        "formula_desc": "Strips out stop words and isolates the most frequent noun/adjective keywords.",
        "inputs": [
            {"id": "text-input", "label": "Enter your Content:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Extracted Keywords", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const stopWords = ['the', 'and', 'with', 'that', 'this', 'from', 'this', 'they', 'them', 'these', 'have', 'were', 'your', 'about'];
            const words = text.toLowerCase().match(/[a-z]+/g);
            if (!words) {
                document.getElementById('text-output').value = 'No valid keywords found.';
                return;
            }
            const filtered = words.filter(w => w.length > 4 && !stopWords.includes(w));
            const freq = {};
            for (let w of filtered) {
                freq[w] = (freq[w] || 0) + 1;
            }
            const topKeywords = Object.entries(freq).sort((a,b) => b[1]-a[1]).slice(0, 10).map(x => x[0]);
            document.getElementById('text-output').value = topKeywords.join(', ');
            updateBreakdown(`<p>Extracted top 10 keywords ignoring common grammatical stop words.</p>`);
        """
    },
    {
        "name": "Keyword Position Checker",
        "slug": "keyword-position-checker",
        "category": "SEO Text Tools",
        "icon": "📍",
        "desc": "Verify where keywords appear in your article (e.g. first 100 words).",
        "formula": "PosIndex = Text.indexOf(Keyword)",
        "formula_desc": "Locates the index position of search terms in text segments.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content:", "type": "textarea", "default": ""},
            {"id": "keyword-to-find", "label": "Keyword to Locate", "type": "text", "default": "seo"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Position Results", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const kw = document.getElementById('keyword-to-find').value.trim().toLowerCase();
            
            if (kw === '') {
                showToast("Please enter a keyword.", "error");
                return;
            }
            
            const idx = text.toLowerCase().indexOf(kw);
            if (idx === -1) {
                document.getElementById('text-output').value = `Keyword '${kw}' not found in the content.`;
            } else {
                const wordsBefore = text.slice(0, idx).trim().split(/\\s+/).length;
                let feedback = `Keyword '${kw}' first appears at word index: ${wordsBefore + 1}\\n`;
                if (wordsBefore <= 100) {
                    feedback += `+ Optimal: Keyword appears in the intro (first 100 words).`;
                } else {
                    feedback += `- Tip: Move this keyword to the first 100 words for better SEO.`;
                }
                document.getElementById('text-output').value = feedback;
            }
            updateBreakdown(`<p>Checked positioning relative to general search crawling conventions.</p>`);
        """
    },
    {
        "name": "Content Density Analyzer",
        "slug": "content-density-analyzer",
        "category": "SEO Text Tools",
        "icon": "⚖️",
        "desc": "Analyze content weight parameters including sentence count ratios.",
        "formula": "Ratios = Sentences / Paragraphs",
        "formula_desc": "Measures spacing distribution to verify readability densities.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content:", "type": "textarea", "default": ""}
        ],
        "outputs": [
            {"id": "text-output", "label": "Density Analysis", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const words = text.trim() === '' ? 0 : text.trim().split(/\\s+/).length;
            const sentences = text.trim() === '' ? 0 : text.split(/[.!?]+/).filter(s => s.trim().length > 0).length || 1;
            const paragraphs = text.trim() === '' ? 0 : text.split(/\\n+/).filter(p => p.trim().length > 0).length || 1;
            
            const wordsPerSentence = (words / sentences).toFixed(1);
            const sentencesPerParagraph = (sentences / paragraphs).toFixed(1);
            
            document.getElementById('text-output').value = 
                `Average Words per Sentence: ${wordsPerSentence}\\n` +
                `Average Sentences per Paragraph: ${sentencesPerParagraph}`;
                
            updateBreakdown(`<p>Computed metrics to audit content density and readability flow.</p>`);
        """
    },
    {
        "name": "N-Gram Generator",
        "slug": "n-gram-generator",
        "category": "SEO Text Tools",
        "icon": "⛓️",
        "desc": "Generate lists of unigrams, bigrams, and trigrams from text.",
        "formula": "Sequence of N items",
        "formula_desc": "Combines consecutive words into phrases of length N for keyword research.",
        "inputs": [
            {"id": "text-input", "label": "Enter Content:", "type": "textarea", "default": ""},
            {"id": "n-size", "label": "N-Gram Size", "type": "number", "default": "2", "min": "1", "max": "5", "step": "1"}
        ],
        "outputs": [
            {"id": "text-output", "label": "N-Gram Result", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const n = parseInt(document.getElementById('n-size').value) || 2;
            const words = text.toLowerCase().match(/[a-z0-9]+/g);
            
            if (!words || words.length < n) {
                document.getElementById('text-output').value = 'Not enough words to generate N-grams.';
                return;
            }
            
            let ngrams = [];
            for (let i = 0; i <= words.length - n; i++) {
                ngrams.push(words.slice(i, i + n).join(' '));
            }
            
            const freq = {};
            for (let ng of ngrams) {
                freq[ng] = (freq[ng] || 0) + 1;
            }
            
            const sorted = Object.entries(freq).sort((a,b) => b[1]-a[1]);
            document.getElementById('text-output').value = sorted.map(x => `${x[0]}: ${x[1]}`).join('\\n');
            updateBreakdown(`<p>Generated ${ngrams.length} n-grams of size ${n}.</p>`);
        """
    }
]

WRITING_CALCS = [
    {
        "name": "Article Rewriter",
        "slug": "article-rewriter",
        "category": "Content Writing Tools",
        "icon": "✍",
        "desc": "Rewrite articles and essays by replacing words with matching synonyms.",
        "formula": "Text.replace(words, synonyms)",
        "formula_desc": "Applies a dictionary-based word mapping pattern to rewrite drafts.",
        "inputs": [
            {"id": "text-input", "label": "Enter original text:", "type": "textarea", "default": "Using this free tool is simple and fast. It is safe and secure."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Rewritten Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const dict = {
                'using': 'utilizing', 'free': 'complimentary', 'tool': 'utility',
                'simple': 'effortless', 'fast': 'rapid', 'safe': 'reliable',
                'secure': 'private', 'create': 'develop', 'easy': 'user-friendly',
                'help': 'assist', 'make': 'produce', 'work': 'operate'
            };
            let rewritten = text;
            for (let [word, syn] of Object.entries(dict)) {
                const regex = new RegExp('\\\\b' + word + '\\\\b', 'gi');
                rewritten = rewritten.replace(regex, syn);
            }
            document.getElementById('text-output').value = rewritten;
            updateBreakdown(`<p>Replaced key verbs and adjectives with high-grade synonyms.</p>`);
        """
    },
    {
        "name": "Paragraph Rewriter",
        "slug": "paragraph-rewriter",
        "category": "Content Writing Tools",
        "icon": "📝",
        "desc": "Rewrite text paragraphs automatically to change structure and flow.",
        "formula": "Synonym substitution",
        "formula_desc": "Substitutes adjectives and key verbs using a client-side dictionary.",
        "inputs": [
            {"id": "text-input", "label": "Enter Paragraph:", "type": "textarea", "default": "This online helper resolves coding challenges easily."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Rewritten Paragraph", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const dict = {
                'online': 'web-based', 'helper': 'utility', 'resolves': 'solves',
                'coding': 'programming', 'challenges': 'problems', 'easily': 'seamlessly'
            };
            let rewritten = text;
            for (let [word, syn] of Object.entries(dict)) {
                const regex = new RegExp('\\\\b' + word + '\\\\b', 'gi');
                rewritten = rewritten.replace(regex, syn);
            }
            document.getElementById('text-output').value = rewritten;
            updateBreakdown(`<p>Reconstructed paragraph sentence tokens.</p>`);
        """
    },
    {
        "name": "Sentence Rewriter",
        "slug": "sentence-rewriter",
        "category": "Content Writing Tools",
        "icon": "💬",
        "desc": "Rewrite sentences by swapping phrases and terms with equivalents.",
        "formula": "Phrase conversion",
        "formula_desc": "Swaps typical sentence starters and adjectives with matching synonyms.",
        "inputs": [
            {"id": "text-input", "label": "Enter Sentence:", "type": "textarea", "default": "I want to start a new project."}
        ],
        "outputs": [
            {"id": "text-output", "label": "Rewritten Sentence", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const text = document.getElementById('text-input').value;
            const dict = {
                'start': 'initiate', 'new': 'fresh', 'project': 'undertaking', 'want': 'intend'
            };
            let rewritten = text;
            for (let [word, syn] of Object.entries(dict)) {
                const regex = new RegExp('\\\\b' + word + '\\\\b', 'gi');
                rewritten = rewritten.replace(regex, syn);
            }
            document.getElementById('text-output').value = rewritten;
            updateBreakdown(`<p>Swapped keywords to vary sentence architecture.</p>`);
        """
    },
    {
        "name": "Headline Generator",
        "slug": "headline-generator",
        "category": "Content Writing Tools",
        "icon": "📰",
        "desc": "Generate high-CTR news, article, and essay headlines from topics.",
        "formula": "Topic patterns",
        "formula_desc": "Combines keywords with high-converting headline templates.",
        "inputs": [
            {"id": "text-input", "label": "Enter Topic/Keyword:", "type": "text", "default": "online tools"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Headline Suggestions", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const templates = [
                `Why ${topic} Will Change Your Life Forever`,
                `10 Secrets About ${topic} Experts Keep Hidden`,
                `The Ultimate Practical Guide to Master ${topic}`,
                `How ${topic} Can Boost Your Productivity Today`,
                `Is ${topic} Worth the Hype? An Honest Review`
            ];
            document.getElementById('text-output').value = templates.join('\\n\\n');
            updateBreakdown(`<p>Generated headlines using engaging title templates.</p>`);
        """
    },
    {
        "name": "Blog Title Generator",
        "slug": "blog-title-generator",
        "category": "Content Writing Tools",
        "icon": "✍",
        "desc": "Create engaging, click-worthy blog title ideas from keywords.",
        "formula": "Blog template generation",
        "formula_desc": "Generates listicles and guide titles from input subject.",
        "inputs": [
            {"id": "text-input", "label": "Enter Blog Keyword:", "type": "text", "default": "digital marketing"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Blog Titles", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a keyword.", "error");
                return;
            }
            const templates = [
                `5 Simple Ways to Optimize ${topic} in 2026`,
                `A Complete Beginner's Walkthrough to ${topic}`,
                `The Best ${topic} Tools You Should Try Right Now`,
                `What Nobody Tells You About ${topic}`,
                `Top ${topic} Trends for Content Creators`
            ];
            document.getElementById('text-output').value = templates.join('\\n\\n');
            updateBreakdown(`<p>Created blog title options for content scheduling.</p>`);
        """
    },
    {
        "name": "Meta Description Generator",
        "slug": "meta-description-generator",
        "category": "Content Writing Tools",
        "icon": "🤖",
        "desc": "Generate custom, action-oriented SEO meta descriptions instantly.",
        "formula": "Call to action template",
        "formula_desc": "Assembles topic values with active search verbs under 160 characters.",
        "inputs": [
            {"id": "text-input", "label": "Enter Target Topic:", "type": "text", "default": "best coffee beans"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Meta Descriptions", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const templates = [
                `Looking for the ultimate guide to ${topic}? Explore our expert tips, reviews, and recommendations to get the best results today!`,
                `Find out how to master ${topic} instantly. Discover top strategies, simple steps, and insights to optimize your project.`,
                `Read the latest facts about ${topic}. Compare features, benefits, and costs in our detailed online guide. Free and updated!`
            ];
            document.getElementById('text-output').value = templates.join('\\n\\n');
            updateBreakdown(`<p>Created meta tag texts matching standard SERP character parameters.</p>`);
        """
    },
    {
        "name": "Product Description Generator",
        "slug": "product-description-generator",
        "category": "Content Writing Tools",
        "icon": "🏷️",
        "desc": "Generate catchy sales descriptions for products and services.",
        "formula": "Sales template parameters",
        "formula_desc": "Combines product name with sales pitches and feature summaries.",
        "inputs": [
            {"id": "text-input", "label": "Enter Product/Service Name:", "type": "text", "default": "Smart Mug"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Product Description Ideas", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const name = document.getElementById('text-input').value.trim();
            if (name === '') {
                showToast("Please enter a product name.", "error");
                return;
            }
            const description = `Introducing the all-new ${name}! Designed to fit your modern lifestyle, the ${name} offers premium durability, exceptional performance, and a sleek layout. Whether you are at home, in the office, or traveling, it is the perfect solution. Order your ${name} today and experience the difference!`;
            document.getElementById('text-output').value = description;
            updateBreakdown(`<p>Generated Product Description template.</p>`);
        """
    },
    {
        "name": "YouTube Title Generator",
        "slug": "youtube-title-generator",
        "category": "Content Writing Tools",
        "icon": "📺",
        "desc": "Create catchy, click-worthy YouTube titles to increase video views.",
        "formula": "YouTube title template parameters",
        "formula_desc": "Pairs input topic with high-performance viral YouTube hooks.",
        "inputs": [
            {"id": "text-input", "label": "Enter Video Subject:", "type": "text", "default": "learn javascript"}
        ],
        "outputs": [
            {"id": "text-output", "label": "YouTube Titles", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const subject = document.getElementById('text-input').value.trim();
            if (subject === '') {
                showToast("Please enter a video subject.", "error");
                return;
            }
            const templates = [
                `How I Learned to ${subject} in 24 Hours! 🚀`,
                `Stop Doing This If You Want to ${subject}`,
                `The Only ${subject} Tutorial You Will Ever Need`,
                `Before You Try to ${subject}, Watch This!`,
                `My Secret to ${subject} Fast (Beginner Guide)`
            ];
            document.getElementById('text-output').value = templates.join('\\n\\n');
            updateBreakdown(`<p>Generated YT title structures built for high organic search traffic.</p>`);
        """
    },
    {
        "name": "YouTube Description Generator",
        "slug": "youtube-description-generator",
        "category": "Content Writing Tools",
        "icon": "📝",
        "desc": "Generate SEO-optimized descriptions for your YouTube videos.",
        "formula": "Structured description pattern",
        "formula_desc": "Generates a complete YouTube description structure with sections for intro, chapters, links, and hashtags.",
        "inputs": [
            {"id": "text-input", "label": "Enter Video Title/Topic:", "type": "text", "default": "how to edit photos"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Description Output", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const topic = document.getElementById('text-input').value.trim();
            if (topic === '') {
                showToast("Please enter a topic.", "error");
                return;
            }
            const description = 
                `In this video, we are sharing everything you need to know about ${topic}!\\n` +
                `Learn the top tips, standard hacks, and step-by-step methods to get started.\\n\\n` +
                `📌 TIMESTAMPS:\\n0:00 - Introduction\\n1:30 - Core Steps\\n5:45 - Troubleshooting\\n8:00 - Summary\\n\\n` +
                `🔔 Don't forget to Like, Share & Subscribe for more updates on ${topic}!\\n\\n` +
                `#${topic.replace(/\\s+/g, '')} #tutorial #howto`;
            document.getElementById('text-output').value = description;
            updateBreakdown(`<p>YouTube description template generated.</p>`);
        """
    },
    {
        "name": "Social Media Caption Generator",
        "slug": "social-media-caption-generator",
        "category": "Content Writing Tools",
        "icon": "📱",
        "desc": "Create engaging social media captions with emojis and hashtags.",
        "formula": "Caption templates + emojis",
        "formula_desc": "Combines post theme with styled hooks, emojis, and call-to-actions.",
        "inputs": [
            {"id": "text-input", "label": "Enter Post Theme:", "type": "text", "default": "new app launch"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Social Media Captions", "type": "textarea", "readonly": True}
        ],
        "calc_js": """
            const theme = document.getElementById('text-input').value.trim();
            if (theme === '') {
                showToast("Please enter a theme.", "error");
                return;
            }
            const templates = [
                `Big news! 🎉 We just launched our new app: ${theme}. Check it out at the link in our bio and let us know what you think! 🚀 #tech #${theme.replace(/\\s+/g, '')}`,
                `Looking for the best way to handle ${theme}? We've got you covered! Check out our latest updates. 💡 #${theme.replace(/\\s+/g, '')} #growth`,
                `Monday Motivation: Leveling up our work with ${theme}! What are your goals for this week? Let us know below! 👇 #${theme.replace(/\\s+/g, '')}`
            ];
            document.getElementById('text-output').value = templates.join('\\n\\n');
            updateBreakdown(`<p>Caption suggestions created.</p>`);
        """
    }
]
