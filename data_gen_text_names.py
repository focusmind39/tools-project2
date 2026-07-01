# -*- coding: utf-8 -*-
"""
Database of 20 Text and Name Generator Tools for Enginewheels
"""

TEXT_GENERATORS = [
    {
        "category": "Text Generators",
        "name": "Lorem Ipsum Generator",
        "slug": "lorem-ipsum-generator",
        "desc": "Generate classic Lorem Ipsum placeholder text for layouts and designs.",
        "formula": "Lorem Ipsum words/paragraphs synthesis",
        "formula_desc": "Loops through predefined Latin word grids to assemble sentences or paragraphs matching the requested counts.",
        "icon": "📝",
        "inputs": [
            {"id": "lorem-type", "label": "Generation Unit:", "type": "select", "default": "paragraphs", 
             "options": [
                 ("paragraphs", "Paragraphs"),
                 ("sentences", "Sentences"),
                 ("words", "Words")
             ]},
            {"id": "lorem-count", "label": "Amount to Generate:", "type": "number", "default": "3"},
            {"id": "lorem-start", "label": "Start with standard 'Lorem ipsum dolor...':", "type": "select", "default": "yes",
             "options": [
                 ("yes", "Yes"),
                 ("no", "No")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Placeholder Text:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('lorem-type').value;
            const count = parseInt(document.getElementById('lorem-count').value) || 1;
            const startWithStandard = document.getElementById('lorem-start').value === 'yes';

            const latinWords = [
                "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do",
                "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "ut",
                "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris",
                "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat", "duis", "aute", "irure",
                "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse", "cillum", "dolore",
                "eu", "fugiat", "nulla", "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non",
                "proident", "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
            ];

            function generateWord() {
                return latinWords[Math.floor(Math.random() * latinWords.length)];
            }

            function generateSentence() {
                const len = 5 + Math.floor(Math.random() * 10);
                const words = [];
                for (let i = 0; i < len; i++) {
                    words.push(generateWord());
                }
                let sentence = words.join(" ");
                return sentence.charAt(0).toUpperCase() + sentence.slice(1) + ".";
            }

            function generateParagraph() {
                const len = 3 + Math.floor(Math.random() * 4);
                const sentences = [];
                for (let i = 0; i < len; i++) {
                    sentences.push(generateSentence());
                }
                return sentences.join(" ");
            }

            let result = "";
            if (type === "words") {
                const words = [];
                if (startWithStandard && count >= 5) {
                    words.push("Lorem", "ipsum", "dolor", "sit", "amet");
                    for (let i = 5; i < count; i++) words.push(generateWord());
                } else {
                    for (let i = 0; i < count; i++) words.push(generateWord());
                }
                result = words.join(" ");
            } else if (type === "sentences") {
                const sentences = [];
                for (let i = 0; i < count; i++) {
                    if (i === 0 && startWithStandard) {
                        sentences.push("Lorem ipsum dolor sit amet, consectetur adipiscing elit.");
                    } else {
                        sentences.push(generateSentence());
                    }
                }
                result = sentences.join(" ");
            } else {
                const paragraphs = [];
                for (let i = 0; i < count; i++) {
                    if (i === 0 && startWithStandard) {
                        paragraphs.push("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " + generateParagraph());
                    } else {
                        paragraphs.push(generateParagraph());
                    }
                }
                result = paragraphs.join("\\n\\n");
            }

            document.getElementById('text-output').value = result;
            updateBreakdown(`<p class='text-success'>Generated ${count} ${type} of Lorem Ipsum text successfully.</p>`);
        """
    },
    {
        "category": "Text Generators",
        "name": "Dummy Text Generator",
        "slug": "dummy-text-generator",
        "desc": "Generate custom mock sentences, pangrams, and random gibberish.",
        "formula": "Predefined layout templates",
        "formula_desc": "Combines typical copywriting pangrams, mock messages, or randomized character arrays.",
        "icon": "📝",
        "inputs": [
            {"id": "dummy-mode", "label": "Text Type:", "type": "select", "default": "pangram", 
             "options": [
                 ("pangram", "Pangrams (Quick Brown Fox)"),
                 ("scrambled", "Scrambled English Words"),
                 ("gibberish", "Random Character Gibberish")
             ]},
            {"id": "dummy-count", "label": "Paragraph Count:", "type": "number", "default": "2"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Dummy Text:", "type": "textarea"}
        ],
        "calc_js": """
            const mode = document.getElementById('dummy-mode').value;
            const count = parseInt(document.getElementById('dummy-count').value) || 1;
            
            const pangrams = [
                "The quick brown fox jumps over the lazy dog.",
                "Pack my box with five dozen liquor jugs.",
                "How vexingly quick daft zebras jump!",
                "Sphinx of black quartz, judge my vow.",
                "Jackdaws love my big sphinx of quartz."
            ];

            const words = ["framework", "database", "analytics", "integration", "dashboard", "interface", "optimization", "synergy", "paradigm", "scalability", "pipeline", "deployment", "repository", "microservices", "efficiency"];

            let paragraphs = [];
            for (let p = 0; p < count; p++) {
                if (mode === "pangram") {
                    let sentences = [];
                    for (let s = 0; s < 5; s++) {
                        sentences.push(pangrams[Math.floor(Math.random() * pangrams.length)]);
                    }
                    paragraphs.push(sentences.join(" "));
                } else if (mode === "scrambled") {
                    let sentences = [];
                    for (let s = 0; s < 4; s++) {
                        let ws = [];
                        const len = 6 + Math.floor(Math.random() * 8);
                        for (let w = 0; w < len; w++) {
                            ws.push(words[Math.floor(Math.random() * words.length)]);
                        }
                        let sentence = ws.join(" ");
                        sentences.push(sentence.charAt(0).toUpperCase() + sentence.slice(1) + ".");
                    }
                    paragraphs.push(sentences.join(" "));
                } else {
                    let chars = "abcdefghijklmnopqrstuvwxyz   ";
                    let words_list = [];
                    for (let w = 0; w < 40; w++) {
                        let word = "";
                        let word_len = 3 + Math.floor(Math.random() * 8);
                        for (let c = 0; c < word_len; c++) {
                            word += chars.charAt(Math.floor(Math.random() * 26));
                        }
                        words_list.push(word);
                    }
                    paragraphs.push(words_list.join(" ") + ".");
                }
            }

            document.getElementById('text-output').value = paragraphs.join("\\n\\n");
            updateBreakdown("<p class='text-success'>Generated dummy text for mock layouts.</p>");
        """
    },
    {
        "category": "Text Generators",
        "name": "Random Word Generator",
        "slug": "random-word-generator",
        "desc": "Generate lists of random verbs, nouns, adjectives, or general English words.",
        "formula": "Random array element sampling",
        "formula_desc": "Uses cryptographic or pseudo-random indexes to extract distinct entries from an embedded dictionary.",
        "icon": "🔤",
        "inputs": [
            {"id": "word-type", "label": "Word Type:", "type": "select", "default": "all",
             "options": [
                 ("all", "Mixed Words"),
                 ("nouns", "Nouns Only"),
                 ("verbs", "Verbs Only"),
                 ("adjectives", "Adjectives Only")
             ]},
            {"id": "word-qty", "label": "Number of Words:", "type": "number", "default": "10"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Words Output:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('word-type').value;
            const qty = parseInt(document.getElementById('word-qty').value) || 5;

            const nouns = ["apple", "building", "cloud", "desert", "elephant", "forest", "galaxy", "harbor", "island", "jungle", "kingdom", "lantern", "mountain", "notebook", "ocean", "pyramid", "river", "satellite", "tunnel", "valley"];
            const verbs = ["run", "create", "discover", "launch", "inspire", "build", "navigate", "calculate", "visualize", "optimize", "succeed", "explore", "design", "transform", "analyze", "coordinate", "compile", "validate", "achieve", "deliver"];
            const adjectives = ["quick", "bright", "silent", "ancient", "modern", "vibrant", "glowing", "creative", "efficient", "robust", "scalable", "elegant", "dynamic", "mysterious", "limitless", "precise", "harmonious", "peaceful", "infinite", "bold"];

            let pool;
            if (type === "nouns") pool = nouns;
            else if (type === "verbs") pool = verbs;
            else if (type === "adjectives") pool = adjectives;
            else pool = [...nouns, ...verbs, ...adjectives];

            let chosen = [];
            for (let i = 0; i < qty; i++) {
                chosen.push(pool[Math.floor(Math.random() * pool.length)]);
            }

            document.getElementById('text-output').value = chosen.join("\\n");
            updateBreakdown(`<p class='text-success'>Extracted ${qty} random words from pool.</p>`);
        """
    },
    {
        "category": "Text Generators",
        "name": "Random Sentence Generator",
        "slug": "random-sentence-generator",
        "desc": "Generate grammatically correct random sentences for typing tests or placeholders.",
        "formula": "Subject-Verb-Object synthesis",
        "formula_desc": "Maps sentence patterns (Subject + Verb + Direct Object + Prepositional Phrase) to random word grids.",
        "icon": "📝",
        "inputs": [
            {"id": "sent-count", "label": "Sentences to Generate:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Sentences Output:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('sent-count').value) || 5;

            const subjects = ["The software engineer", "A quick rabbit", "The massive spacecraft", "Our project manager", "The curious cat", "An advanced AI system", "The client", "A data analyst"];
            const verbs = ["developed", "chased", "launched into", "approved", "investigated", "optimized", "requested", "calculated", "designed", "discovered"];
            const objects = ["the nested code block", "the carrot", "deep orbit", "the final milestone", "the cardboard box", "the neural network weight", "a clean report", "a beautiful gradient layout"];
            const modifiers = ["yesterday morning", "with absolute precision", "under high pressure", "smoothly", "using a modern framework", "without any warnings", "secretly", "at midnight"];

            let sentences = [];
            for (let i = 0; i < count; i++) {
                let sub = subjects[Math.floor(Math.random() * subjects.length)];
                let verb = verbs[Math.floor(Math.random() * verbs.length)];
                let obj = objects[Math.floor(Math.random() * objects.length)];
                let mod = modifiers[Math.floor(Math.random() * modifiers.length)];
                sentences.push(`${sub} ${verb} ${obj} ${mod}.`);
            }

            document.getElementById('text-output').value = sentences.join(" ");
            updateBreakdown(`<p class='text-success'>Assembled ${count} randomized grammatical sentences.</p>`);
        """
    },
    {
        "category": "Text Generators",
        "name": "Random Paragraph Generator",
        "slug": "random-paragraph-generator",
        "desc": "Assemble cohesive-looking paragraphs consisting of randomized sentences.",
        "formula": "Sentence cluster compilation",
        "formula_desc": "Packs random sentences of varying lengths into cohesive, indentation-ready text paragraphs.",
        "icon": "📝",
        "inputs": [
            {"id": "para-count", "label": "Paragraphs to Generate:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Paragraphs Output:", "type": "textarea"}
        ],
        "calc_js": """
            const count = parseInt(document.getElementById('para-count').value) || 3;

            const leads = ["In the software development lifecycle, optimization is key.", "Many engineers believe that simple code is the best code.", "Let us explore the core implications of computing.", "Developing user interfaces requires an artistic touch.", "Data structures dictate how applications scale."];
            const bodies = ["By using client-side scripts, security is greatly improved.", "The team launched the new database index to speed up response latency.", "Every calculation is audited inside the browser breakdown log.", "The designer chosen an HSL palette with a modern violet color.", "A responsive design adapts smoothly to various desktop sizes."];
            const tails = ["This ensures maximum efficiency.", "Ultimately, user experience dictates overall success.", "No registration or credentials are required.", "Everything operates seamlessly.", "That is the foundation of high-performance tools."];

            let paras = [];
            for (let p = 0; p < count; p++) {
                let sentences = [];
                sentences.push(leads[Math.floor(Math.random() * leads.length)]);
                for (let s = 0; s < 3; s++) {
                    sentences.push(bodies[Math.floor(Math.random() * bodies.length)]);
                }
                sentences.push(tails[Math.floor(Math.random() * tails.length)]);
                paras.push(sentences.join(" "));
            }

            document.getElementById('text-output').value = paras.join("\\n\\n");
            updateBreakdown(`<p class='text-success'>Assembled ${count} readable dummy paragraphs.</p>`);
        """
    },
    {
        "category": "Text Generators",
        "name": "Random Story Generator",
        "slug": "random-story-generator",
        "desc": "Create fun, randomized short stories using structural mad-lib templates.",
        "formula": "Structural template substitution",
        "formula_desc": "Selects random names, settings, conflicts, and resolutions, mapping them to pre-written story templates.",
        "icon": "📖",
        "inputs": [
            {"id": "story-genre", "label": "Story Genre:", "type": "select", "default": "sci-fi",
             "options": [
                 ("sci-fi", "Sci-Fi / Space Opera"),
                 ("fantasy", "Medieval Fantasy"),
                 ("mystery", "Classic Detective Noir")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Short Story:", "type": "textarea"}
        ],
        "calc_js": """
            const genre = document.getElementById('story-genre').value;
            
            let story = "";
            if (genre === "sci-fi") {
                const names = ["Captain Zorg", "X-204", "Dr. Nova", "Astrid"];
                const planets = ["Zephyr-9", "Neon Core", "Omega Prime", "The Dust Belt"];
                const items = ["quantum stabilizer", "warp drive key", "nanotech canister", "plasma battery"];
                const threats = ["space pirates", "solar flare blast", "AI rebellion", "asteroid cluster"];
                
                story = `Deep in the sector of ${planets[Math.floor(Math.random() * planets.length)]}, ${names[Math.floor(Math.random() * names.length)]} realized the ship's control console was flashing red. The target was close, but a nearby ${threats[Math.floor(Math.random() * threats.length)]} was blocking their path. 'Secure the ${items[Math.floor(Math.random() * items.length)]}!' they shouted. With only minutes remaining before hyperdrive failure, they initiated the secondary engines, slipped past the obstacles, and safely entered the wormhole, saving the crew from certain doom.`;
            } else if (genre === "fantasy") {
                const heroes = ["Sir Galahad", "Eldrin the Elf", "Grom the Orc", "Lyra the Bard"];
                const locations = ["Whispering Woods", "Stonekeep Castle", "Dragon's Ridge", "Sunken Temple"];
                const relics = ["Crystal Sword", "Ring of Wisdom", "Elixir of Life", "Golden Shield"];
                const enemies = ["goblin horde", "ancient fire dragon", "dark sorcerer", "stone golem"];
                
                story = `It was a cold night in the ${locations[Math.floor(Math.random() * locations.length)]} when ${heroes[Math.floor(Math.random() * heroes.length)]} spotted the enemy campfire. A dangerous ${enemies[Math.floor(Math.random() * enemies.length)]} was guarding the entrance to the cave. Clenching the legendary ${relics[Math.floor(Math.random() * relics.length)]}, they rushed forward with a fierce battle cry. The clash was legendary, but using the relic's hidden magic, the guardian was vanquished and peace was restored to the kingdom.`;
            } else {
                const detectives = ["Jack Spade", "Detective Vance", "Inspector Clouse", "Vicky Sterling"];
                const locations = ["rain-slicked streets of Chicago", "old library attic", "abandoned harbor dock", "private mansion office"];
                const clues = ["torn code snippet", "smudged lipstick note", "broken pocket watch", "mysterious gold key"];
                const suspects = ["the butler", "a shadowy programmer", "the rival tycoon", "the jazz singer"];
                
                story = `The rain beat against the window pane in the ${locations[Math.floor(Math.random() * locations.length)]}. ${detectives[Math.floor(Math.random() * detectives.length)]} lit a cigarette, staring at the evidence: a ${clues[Math.floor(Math.random() * clues.length)]}. Every lead pointed towards ${suspects[Math.floor(Math.random() * suspects.length)]}, but something didn't add up. With a sudden burst of realization, they noticed the timestamp matched. The case was cracked, and the mystery was finally put to rest.`;
            }

            document.getElementById('text-output').value = story;
            updateBreakdown("<p class='text-success'>Story generated dynamically using mad-libs schema.</p>");
        """
    },
    {
        "category": "Text Generators",
        "name": "Random Topic Generator",
        "slug": "random-topic-generator",
        "desc": "Generate interesting discussion prompts, debate questions, or essay topics.",
        "formula": "Topic category array classification",
        "formula_desc": "Pulls unique questions and topics based on the chosen category (tech, philosophy, lifestyle).",
        "icon": "💡",
        "inputs": [
            {"id": "topic-cat", "label": "Topic Area:", "type": "select", "default": "tech",
             "options": [
                 ("tech", "Technology & Society"),
                 ("philosophy", "Philosophy & Ethics"),
                 ("creative", "Creative Writing & Art")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated Topics Output:", "type": "textarea"}
        ],
        "calc_js": """
            const cat = document.getElementById('topic-cat').value;

            const tech = [
                "Should artificial intelligence have copyright over the art it creates?",
                "How does social media design impact the attention span of younger generations?",
                "The ethical implications of editing human genomes to cure diseases.",
                "Will quantum computing render modern cryptography useless?",
                "How does working remotely affect team collaboration and mental health?"
            ];

            const philosophy = [
                "If a machine can think, does it possess a soul or consciousness?",
                "Is it better to prioritize absolute freedom or absolute safety?",
                "What is the definition of a 'good life' in the modern era?",
                "Are human morals learned through society or are they biological traits?",
                "Does history repeat itself or do we just repeat our mistakes?"
            ];

            const creative = [
                "Write about a world where people can trade their memories like currency.",
                "Explain the beauty of a sunset to someone who has never been able to see.",
                "An astronaut gets left behind on Mars, but finds a thriving underground library.",
                "Design a dialogue between a shadow and the person who casts it.",
                "Describe a city where it rains keys instead of water."
            ];

            let pool = tech;
            if (cat === "philosophy") pool = philosophy;
            else if (cat === "creative") pool = creative;

            // Select 3 random unique topics
            let shuf = [...pool].sort(() => 0.5 - Math.random());
            let result = shuf.slice(0, 3).map((t, idx) => `${idx+1}. ${t}`).join("\\n\\n");

            document.getElementById('text-output').value = result;
            updateBreakdown("<p class='text-success'>Generated three unique discussion topics.</p>");
        """
    },
    {
        "category": "Text Generators",
        "name": "Quote Generator",
        "slug": "quote-generator",
        "desc": "Get classic, inspiring, and historic quotes from famous figures.",
        "formula": "Historic quote extraction",
        "formula_desc": "Selects random entries from a compiled list of historic quotes, maintaining authorship attributes.",
        "icon": "💬",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Inspirational Quote:", "type": "textarea"}
        ],
        "calc_js": """
            const quotes = [
                { text: "The only limit to our realization of tomorrow will be our doubts of today.", author: "Franklin D. Roosevelt" },
                { text: "Life is what happens when you're busy making other plans.", author: "John Lennon" },
                { text: "Science is what you know, philosophy is what you don't know.", author: "Bertrand Russell" },
                { text: "Simplicity is the ultimate sophistication.", author: "Leonardo da Vinci" },
                { text: "Strive not to be a success, but rather to be of value.", author: "Albert Einstein" },
                { text: "The unexamined life is not worth living.", author: "Socrates" }
            ];

            const chosen = quotes[Math.floor(Math.random() * quotes.length)];
            document.getElementById('text-output').value = `"${chosen.text}"\\n\\n— ${chosen.author}`;
            updateBreakdown("<p class='text-success'>Quote fetched successfully.</p>");
        """
    },
    {
        "category": "Text Generators",
        "name": "Motivational Quote Generator",
        "slug": "motivational-quote-generator",
        "desc": "Get direct motivational quotes to boost your productivity and focus.",
        "formula": "Mindset booster lookup",
        "formula_desc": "Selects a random motivational quote focused on effort, hard work, and persistence.",
        "icon": "🔥",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Motivational Boost:", "type": "textarea"}
        ],
        "calc_js": """
            const quotes = [
                "Don't stop when you're tired. Stop when you're done.",
                "Great things never came from comfort zones.",
                "Dream it. Wish it. Do it.",
                "Success doesn't just find you. You have to go out and get it.",
                "The key to success is to focus on goals, not obstacles.",
                "Action is the foundational key to all success."
            ];

            const chosen = quotes[Math.floor(Math.random() * quotes.length)];
            document.getElementById('text-output').value = chosen;
            updateBreakdown("<p class='text-success'>Motivational boost updated.</p>");
        """
    },
    {
        "category": "Text Generators",
        "name": "Writing Prompt Generator",
        "slug": "writing-prompt-generator",
        "desc": "Get random story prompts combining genre, character, conflict, and key objects.",
        "formula": "Prompt matrix compilation",
        "formula_desc": "Combines random elements from four separate creative categories to compose a story prompt.",
        "icon": "🖊️",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Story Prompt:", "type": "textarea"}
        ],
        "calc_js": """
            const genres = ["A fantasy story", "A sci-fi thriller", "A mystery thriller", "A historical drama", "A romantic comedy"];
            const characters = ["about a keymaker who can hear locks whisper", "featuring an astronomer who discovers a new moon made of glass", "about a time traveler stuck in a single Monday", "featuring a lighthouse keeper who talks to sea monsters"];
            const conflicts = ["who must escape a city before the shadows come alive", "who has to hide a secret chest from the king", "who must decode a message hidden in old piano sheets", "who is trying to find their lost shadow"];
            const key_elements = ["with a mysterious golden key.", "with a clock that ticks backwards.", "with a notebook that writes back.", "with a compass that points to what they want most."];

            const prompt = `${genres[Math.floor(Math.random() * genres.length)]} ${characters[Math.floor(Math.random() * characters.length)]} ${conflicts[Math.floor(Math.random() * conflicts.length)]} ${key_elements[Math.floor(Math.random() * key_elements.length)]}`;

            document.getElementById('text-output').value = prompt;
            updateBreakdown("<p class='text-success'>Assembled writing prompt elements.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Username Generator",
        "slug": "username-generator",
        "desc": "Generate clean, modern, and unique usernames using word blending.",
        "formula": "Noun-Adjective synthesis",
        "formula_desc": "Combines list dictionaries of nouns, adjectives, and random numbers to format standard username strings.",
        "icon": "👤",
        "inputs": [
            {"id": "user-keyword", "label": "Include Keyword (Optional):", "type": "text", "default": ""},
            {"id": "user-nums", "label": "Include Numbers:", "type": "select", "default": "yes",
             "options": [
                 ("yes", "Yes"),
                 ("no", "No")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Username Ideas:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('user-keyword').value.trim();
            const includeNums = document.getElementById('user-nums').value === 'yes';

            const adjs = ["Swift", "Cool", "Epic", "Neon", "Tech", "Glitch", "Cyber", "Mega", "Delta", "Nexus", "Pixel", "Cosmic"];
            const nouns = ["Coder", "Rider", "Ghost", "Runner", "Wizard", "Knight", "Hustler", "Master", "Creator", "Nomad", "Seeker", "Developer"];

            let ideas = [];
            for (let i = 0; i < 5; i++) {
                let adj = adjs[Math.floor(Math.random() * adjs.length)];
                let noun = nouns[Math.floor(Math.random() * nouns.length)];
                let num = includeNums ? Math.floor(Math.random() * 999) : "";
                
                let base = kw ? kw : (adj + noun);
                if (kw) {
                    // Combine keyword with prefix or suffix
                    if (Math.random() > 0.5) {
                        base = adj + base;
                    } else {
                        base = base + noun;
                    }
                }
                ideas.push(base + num);
            }

            document.getElementById('text-output').value = ideas.join("\\n");
            updateBreakdown("<p class='text-success'>Generated five unique username suggestions.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Instagram Username Generator",
        "slug": "instagram-username-generator",
        "desc": "Generate aesthetic Instagram usernames using dots, underscores, and keyword styles.",
        "formula": "Aesthetic word layout mapping",
        "formula_desc": "Combines branding keywords with Instagram-popular suffixes (the, official, daily, design) and dividers.",
        "icon": "📸",
        "inputs": [
            {"id": "ig-keyword", "label": "Your Name / Niche Keyword:", "type": "text", "default": "lyra"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Instagram Usernames:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('ig-keyword').value.trim().toLowerCase().replace(/[^a-z0-9]/g, '');
            if (!kw) {
                showToast("Please enter a valid keyword.", "error");
                return;
            }

            const prefix = ["the_", "iam_", "official_", "its_", "hello_", "daily_"];
            const suffix = ["_design", "_official", "_studio", "_creative", "_diary", "_clicks"];

            let ideas = [];
            ideas.push(kw);
            ideas.push(`${kw}.${suffix[Math.floor(Math.random() * suffix.length)].replace('_', '')}`);
            ideas.push(`${prefix[Math.floor(Math.random() * prefix.length)]}${kw}`);
            ideas.push(`${kw}_clicks`);
            ideas.push(`its.${kw}`);
            ideas.push(`${kw}_official`);

            document.getElementById('text-output').value = ideas.join("\\n");
            updateBreakdown("<p class='text-success'>Aesthetic Instagram usernames compiled.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "YouTube Channel Name Generator",
        "slug": "youtube-channel-name-generator",
        "desc": "Generate catching names for your YouTube channel based on category niches.",
        "formula": "Niche naming matrix",
        "formula_desc": "Pairs user keywords with channel suffix categories (Gaming, Tech, Vlogs, Education, Cooking).",
        "icon": "🎥",
        "inputs": [
            {"id": "yt-keyword", "label": "Topic / Niche Keyword:", "type": "text", "default": "Byte"},
            {"id": "yt-niche", "label": "Niche Category:", "type": "select", "default": "tech",
             "options": [
                 ("tech", "Tech & Coding"),
                 {"value": "gaming", "label": "Gaming & Let's Plays"},
                 ("vlogs", "Life Vlogs & Travel"),
                 ("learning", "Education & Science")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Channel Names:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('yt-keyword').value.trim();
            const niche = document.getElementById('yt-niche').value;
            if (!kw) {
                showToast("Please enter a keyword.", "error");
                return;
            }

            let suffix = [];
            if (niche === "tech") {
                suffix = ["Bytes", "Tech", "Labs", "Codes", "Space", "Developer", "Matrix"];
            } else if (niche === "gaming") {
                suffix = ["Gaming", "Plays", "Arcade", "Zone", "Pixel", "Slayer", "Quest"];
            } else if (niche === "vlogs") {
                suffix = ["Vlogs", "Life", "Diaries", "Daily", "Journey", "Escape", "Vibe"];
            } else {
                suffix = ["Academy", "Explains", "Facts", "Hub", "Science", "Theory", "HQ"];
            }

            let names = [];
            for (let i = 0; i < 5; i++) {
                let suf = suffix[Math.floor(Math.random() * suffix.length)];
                names.push(`${kw} ${suf}`);
                names.push(`${suf} with ${kw}`);
            }
            names = [...new Set(names)].slice(0, 5);

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>YouTube channel names compiled based on niche preferences.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Business Name Generator",
        "slug": "business-name-generator",
        "desc": "Generate catchy and brandable ideas for your company or business.",
        "formula": "Keyword combination suffixes",
        "formula_desc": "Blends user business keywords with startup prefixes (Smart, Omni, Apex) and suffixes (Grid, Scale, Base).",
        "icon": "🏢",
        "inputs": [
            {"id": "biz-keyword", "label": "Core Product / Keyword:", "type": "text", "default": "Cloud"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Business Names:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('biz-keyword').value.trim();
            if (!kw) {
                showToast("Please enter a core keyword.", "error");
                return;
            }

            const prefix = ["Apex", "Omni", "Core", "Smart", "Nova", "Prime", "Quantum", "Nexus"];
            const suffix = ["Base", "Grid", "Scale", "Force", "Flow", "Shift", "Spark", "Labs"];

            let ideas = [];
            ideas.push(`${kw}ify`);
            ideas.push(`${kw}ly`);
            for (let i = 0; i < 3; i++) {
                let p = prefix[Math.floor(Math.random() * prefix.length)];
                let s = suffix[Math.floor(Math.random() * suffix.length)];
                ideas.push(`${p} ${kw}`);
                ideas.push(`${kw} ${s}`);
            }

            document.getElementById('text-output').value = ideas.join("\\n");
            updateBreakdown("<p class='text-success'>Business name concepts created based on core keywords.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Brand Name Generator",
        "slug": "brand-name-generator",
        "desc": "Generate unique, abstract, and brandable names using vowel-consonant blending.",
        "formula": "Phonetic syllable blending",
        "formula_desc": "Combines phonetic syllables (CVC / VCV structure) to assemble abstract, easily trademarked brand names.",
        "icon": "🏷️",
        "inputs": [
            {"id": "brand-len", "label": "Name Length style:", "type": "select", "default": "medium",
             "options": [
                 ("short", "Short (4-5 chars)"),
                 ("medium", "Medium (6-7 chars)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Abstract Brand Names:", "type": "textarea"}
        ],
        "calc_js": """
            const lenStyle = document.getElementById('brand-len').value;
            const vowels = ["a", "e", "i", "o", "u", "y"];
            const consonants = ["b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "z"];

            function genShort() {
                // Consonant + Vowel + Consonant + Vowel (+ Consonant)
                let name = consonants[Math.floor(Math.random() * consonants.length)].toUpperCase() +
                           vowels[Math.floor(Math.random() * vowels.length)] +
                           consonants[Math.floor(Math.random() * consonants.length)] +
                           vowels[Math.floor(Math.random() * vowels.length)];
                if (Math.random() > 0.5) {
                    name += consonants[Math.floor(Math.random() * consonants.length)];
                }
                return name;
            }

            function genMedium() {
                return genShort().toLowerCase() + 
                       vowels[Math.floor(Math.random() * vowels.length)] + 
                       consonants[Math.floor(Math.random() * consonants.length)];
            }

            let names = [];
            for (let i = 0; i < 5; i++) {
                names.push(lenStyle === "short" ? genShort() : genMedium());
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Abstract brand names synthesized phonetically.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Startup Name Generator",
        "slug": "startup-name-generator",
        "desc": "Generate modern, punchy, tech-focused startup name ideas.",
        "formula": "Tech keyword prefixing",
        "formula_desc": "Combines trendy tech terms (Byte, Cloud, Data, Stack) with action suffix endings.",
        "icon": "🚀",
        "inputs": [
            {"id": "start-niche", "label": "Startup Focus Niche:", "type": "select", "default": "saas",
             "options": [
                 ("saas", "SaaS / Web App"),
                 ("fintech", "Fintech / Payments"),
                 ("ai", "AI & Automation")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Startup Names:", "type": "textarea"}
        ],
        "calc_js": """
            const niche = document.getElementById('start-niche').value;
            
            let bases = [];
            let suffixes = [];
            if (niche === "saas") {
                bases = ["Stack", "Sync", "Hub", "Desk", "Flow", "Grid"];
                suffixes = ["ify", "ly", "wise", "able", "grid", "scale"];
            } else if (niche === "fintech") {
                bases = ["Pay", "Ledger", "Coin", "Mint", "Vault", "Capital"];
                suffixes = ["io", "co", "link", "net", "safe", "hub"];
            } else {
                bases = ["Byte", "Neural", "Cognitive", "Cortex", "Node", "Mind"];
                suffixes = ["ai", "bot", "lab", "tech", "scale", "wise"];
            }

            let names = [];
            for (let i = 0; i < 5; i++) {
                let base = bases[Math.floor(Math.random() * bases.length)];
                let suf = suffixes[Math.floor(Math.random() * suffixes.length)];
                names.push(base + suf);
                names.push(base.toLowerCase() + "." + suf);
            }
            names = [...new Set(names)].slice(0, 5);

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Tech startup names generated successfully.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Domain Name Generator",
        "slug": "domain-name-generator",
        "desc": "Check domain name availability suggestions based on your name or brand.",
        "formula": "TLD extension mapping",
        "formula_desc": "Generates domain layouts using standard top-level domain extensions (.com, .net, .org, .io, .co).",
        "icon": "🌐",
        "inputs": [
            {"id": "domain-kw", "label": "Domain Keyword:", "type": "text", "default": "enginewheels"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Domain Suggestions:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('domain-kw').value.trim().toLowerCase().replace(/[^a-z0-9-]/g, '');
            if (!kw) {
                showToast("Please enter a valid keyword.", "error");
                return;
            }

            const tlds = [".com", ".net", ".io", ".co", ".app", ".org"];
            const prefix = ["get", "try", "use", "my", "the"];

            let domains = [];
            tlds.forEach(tld => {
                domains.push(kw + tld);
            });
            prefix.forEach(p => {
                domains.push(p + kw + ".com");
            });

            document.getElementById('text-output').value = domains.slice(0, 8).join("\\n");
            updateBreakdown("<p class='text-success'>Domain name ideas created with popular TLDs.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Nickname Generator",
        "slug": "nickname-generator",
        "desc": "Generate cute, funny, or cool nicknames based on standard traits.",
        "formula": "Adjective + Name modification",
        "formula_desc": "Alters user first names by appending diminutive endings (y, ie, z) or cool modifiers.",
        "icon": "🏷️",
        "inputs": [
            {"id": "nick-name", "label": "Your First Name:", "type": "text", "default": "Sarah"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Nicknames:", "type": "textarea"}
        ],
        "calc_js": """
            const name = document.getElementById('nick-name').value.trim();
            if (!name) {
                showToast("Please enter a name.", "error");
                return;
            }

            const modifiers = ["Tiny", "Silly", "Chief", "Captain", "Agent", "Super", "Lucky"];
            
            let nicks = [];
            nicks.push(`${name}y`);
            nicks.push(`${name}z`);
            nicks.push(`${name}ie`);
            nicks.push(`${modifiers[Math.floor(Math.random() * modifiers.length)]} ${name}`);
            nicks.push(`${name} the Great`);

            document.getElementById('text-output').value = nicks.join("\\n");
            updateBreakdown("<p class='text-success'>Nicknames compiled based on first name parameters.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Gamer Name Generator",
        "slug": "gamer-name-generator",
        "desc": "Generate epic gamer tags and multiplayer aliases.",
        "formula": "Gaming prefix/suffix grid",
        "formula_desc": "Combines action verbs, fierce creatures, elements, and gaming codes.",
        "icon": "🎮",
        "inputs": [
            {"id": "gamer-theme", "label": "Gaming Style Niche:", "type": "select", "default": "action",
             "options": [
                 ("action", "Action / FPS (Fierce)"),
                 ("magic", "RPG / Fantasy (Magic)"),
                 ("stealth", "Stealth / Sniper (Shadow)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Gamer Tags:", "type": "textarea"}
        ],
        "calc_js": """
            const theme = document.getElementById('gamer-theme').value;

            let prefix = [];
            let suffix = [];
            if (theme === "action") {
                prefix = ["Apex", "Steel", "Blaze", "Vortex", "Iron", "Nova"];
                suffix = ["Slayer", "Hunter", "Reaper", "Raider", "Fury", "Viper"];
            } else if (theme === "magic") {
                prefix = ["Aero", "Mystic", "Lunar", "Rune", "Ether", "Sage"];
                suffix = ["Mage", "Knight", "Frost", "Wraith", "Weaver", "Gale"];
            } else {
                prefix = ["Silent", "Ghost", "Shadow", "Phantom", "Rogue", "Veil"];
                suffix = ["Sniper", "Stalker", "Specter", "Shade", "Blade", "Echo"];
            }

            let tags = [];
            for (let i = 0; i < 5; i++) {
                let p = prefix[Math.floor(Math.random() * prefix.length)];
                let s = suffix[Math.floor(Math.random() * suffix.length)];
                let num = Math.random() > 0.5 ? Math.floor(Math.random() * 99) : "";
                tags.push(p + s + num);
            }

            document.getElementById('text-output').value = tags.join("\\n");
            updateBreakdown("<p class='text-success'>Epic gamer tags assembled successfully.</p>");
        """
    },
    {
        "category": "Username & Name Generators",
        "name": "Fantasy Name Generator",
        "slug": "fantasy-name-generator",
        "desc": "Generate medieval, elven, or dwarven fantasy names for games and writing.",
        "formula": "Fictional race syllable parsing",
        "formula_desc": "Builds fantasy names matching phonetic profiles of popular fantasy races (Elven, Dwarven, Human).",
        "icon": "🧝",
        "inputs": [
            {"id": "race-type", "label": "Fantasy Race:", "type": "select", "default": "elven",
             "options": [
                 ("elven", "Elven (Graceful)"),
                 ("dwarven", "Dwarven (Rugged)"),
                 ("wizard", "Spellcasters / Wizards")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Fantasy Character Names:", "type": "textarea"}
        ],
        "calc_js": """
            const race = document.getElementById('race-type').value;

            function genElven() {
                const prefix = ["Ae", "Cel", "El", "Fael", "Gala", "Loth", "Mith", "Sael"];
                const middle = ["an", "ar", "en", "il", "ir", "or", "ur"];
                const suffix = ["dor", "las", "morn", "thil", "val", "wyn", "rial"];
                return prefix[Math.floor(Math.random() * prefix.length)] +
                       middle[Math.floor(Math.random() * middle.length)] +
                       suffix[Math.floor(Math.random() * suffix.length)];
            }

            function genDwarven() {
                const prefix = ["Bal", "Bof", "Dain", "Gim", "Kili", "Thor", "Thra"];
                const middle = ["in", "ur", "or", "ar"];
                const suffix = ["dur", "bur", "kil", "mir", "li", "grim"];
                return prefix[Math.floor(Math.random() * prefix.length)] +
                       middle[Math.floor(Math.random() * middle.length)] +
                       suffix[Math.floor(Math.random() * suffix.length)];
            }

            function genWizard() {
                const prefix = ["Gandal", "Albu", "Saru", "Merli", "Rada"];
                const suffix = ["f", "s", "dore", "man", "n", "gald"];
                return prefix[Math.floor(Math.random() * prefix.length)] +
                       suffix[Math.floor(Math.random() * suffix.length)] + " the " + 
                       ["Grey", "White", "Wise", "Ancient", "Sage"][Math.floor(Math.random() * 5)];
            }

            let names = [];
            for (let i = 0; i < 5; i++) {
                if (race === "elven") names.push(genElven());
                else if (race === "dwarven") names.push(genDwarven());
                else names.push(genWizard());
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Fantasy names compiled according to race grammar patterns.</p>");
        """
    }
]
