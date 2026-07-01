# -*- coding: utf-8 -*-
"""
Database of 20 Random and Fun/Entertainment Generator Tools for Enginewheels
"""

RANDOM_GENERATORS = [
    {
        "category": "Random Generators",
        "name": "Random Number Generator",
        "slug": "random-number-generator-tool",
        "desc": "Generate random integers within a custom specified minimum and maximum range.",
        "formula": "Number = Min + floor(random * (Max - Min + 1))",
        "formula_desc": "Uses basic random scaling to translate standard unit interval floats into discrete custom integer intervals.",
        "icon": "🎲",
        "inputs": [
            {"id": "num-min", "label": "Minimum Value:", "type": "number", "default": "1"},
            {"id": "num-max", "label": "Maximum Value:", "type": "number", "default": "100"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Number Output:", "type": "textarea"}
        ],
        "calc_js": """
            const min = parseInt(document.getElementById('num-min').value);
            const max = parseInt(document.getElementById('num-max').value);

            if (isNaN(min) || isNaN(max)) {
                showToast("Please enter valid minimum and maximum values.", "error");
                return;
            }

            if (min > max) {
                showToast("Minimum value cannot be greater than maximum value.", "error");
                return;
            }

            const rand = min + Math.floor(Math.random() * (max - min + 1));
            document.getElementById('text-output').value = rand;
            updateBreakdown(`<p class='text-success'>Generated random number: ${rand}</p>`);
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Letter Generator",
        "slug": "random-letter-generator",
        "desc": "Generate a random letter from the English alphabet (A-Z).",
        "formula": "Alphabet index matching",
        "formula_desc": "Selects a random character by index from the 26 standard English letters.",
        "icon": "🔤",
        "inputs": [
            {"id": "let-case", "label": "Letter Case:", "type": "select", "default": "upper",
             "options": [
                 ("upper", "Uppercase (A-Z)"),
                 ("lower", "Lowercase (a-z)")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Letter Output:", "type": "textarea"}
        ],
        "calc_js": """
            const casing = document.getElementById('let-case').value;
            const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            let letter = alphabet.charAt(Math.floor(Math.random() * 26));

            if (casing === "lower") {
                letter = letter.toLowerCase();
            }

            document.getElementById('text-output').value = letter;
            updateBreakdown(`<p class='text-success'>Generated random letter: ${letter}</p>`);
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Color Generator",
        "slug": "random-color-generator-tool",
        "desc": "Generate random HEX colors and show their values.",
        "formula": "Random hex color code compiling",
        "formula_desc": "Iteratively selects 6 hexadecimal characters to build a random color hash.",
        "icon": "🎨",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Random Color Details (HEX):", "type": "textarea"}
        ],
        "calc_js": """
            const hexChars = "0123456789ABCDEF";
            let color = "#";
            for (let i = 0; i < 6; i++) {
                color += hexChars.charAt(Math.floor(Math.random() * 16));
            }

            document.getElementById('text-output').value = color;
            updateBreakdown(`<p class='text-success'>Generated random color code.</p><div style='width:50px;height:50px;background:${color};border-radius:8px;margin-top:10px;'></div>`);
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Country Generator",
        "slug": "random-country-generator",
        "desc": "Get a random country name, capital, and region detail.",
        "formula": "Geographic list mapping",
        "formula_desc": "Extracts a random entry from an embedded dictionary of 30+ sovereign nations.",
        "icon": "🌍",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Random Country:", "type": "textarea"}
        ],
        "calc_js": """
            const countries = [
                { name: "Japan", capital: "Tokyo", region: "Asia" },
                { name: "Brazil", capital: "Brasilia", region: "South America" },
                { name: "Canada", capital: "Ottawa", region: "North America" },
                { name: "Australia", capital: "Canberra", region: "Oceania" },
                { name: "Egypt", capital: "Cairo", region: "Africa" },
                { name: "France", capital: "Paris", region: "Europe" }
            ];

            const chosen = countries[Math.floor(Math.random() * countries.length)];
            document.getElementById('text-output').value = `Country: ${chosen.name}\\nCapital: ${chosen.capital}\\nRegion: ${chosen.region}`;
            updateBreakdown("<p class='text-success'>Geographic country picked.</p>");
        """
    },
    {
        "category": "Random Generators",
        "name": "Random City Generator",
        "slug": "random-city-generator",
        "desc": "Get a random famous global city name and its country.",
        "formula": "City dictionary sampling",
        "formula_desc": "Selects a random city from a list of world capitals and major metropolitan areas.",
        "icon": "🏙️",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Random City:", "type": "textarea"}
        ],
        "calc_js": """
            const cities = [
                { name: "Tokyo", country: "Japan" },
                { name: "Paris", country: "France" },
                { name: "New York City", country: "United States" },
                { name: "Sydney", country: "Australia" },
                { name: "London", country: "United Kingdom" },
                { name: "Cairo", country: "Egypt" }
            ];

            const chosen = cities[Math.floor(Math.random() * cities.length)];
            document.getElementById('text-output').value = `${chosen.name}, ${chosen.country}`;
            updateBreakdown("<p class='text-success'>Global city picked successfully.</p>");
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Date Generator",
        "slug": "random-date-generator",
        "desc": "Generate a random calendar date between two specified years.",
        "formula": "Time interval epoch calculation",
        "formula_desc": "Calculates random millisecond offsets between two boundary dates, converting back to standard Gregorian dates.",
        "icon": "📅",
        "inputs": [
            {"id": "date-min-y", "label": "Start Year:", "type": "number", "default": "2000"},
            {"id": "date-max-y", "label": "End Year:", "type": "number", "default": "2030"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Date Output:", "type": "textarea"}
        ],
        "calc_js": """
            const startYear = parseInt(document.getElementById('date-min-y').value) || 2000;
            const endYear = parseInt(document.getElementById('date-max-y').value) || 2030;

            if (startYear > endYear) {
                showToast("Start year cannot be greater than end year.", "error");
                return;
            }

            const start = new Date(startYear, 0, 1).getTime();
            const end = new Date(endYear, 11, 31).getTime();
            const randTime = start + Math.random() * (end - start);
            
            const randDate = new Date(randTime);
            const dateString = randDate.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });

            document.getElementById('text-output').value = dateString;
            updateBreakdown(`<p class='text-success'>Generated random date: ${dateString}</p>`);
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Time Generator",
        "slug": "random-time-generator",
        "desc": "Generate random clock times in 12-hour or 24-hour formatting.",
        "formula": "Hour & Minute scaling",
        "formula_desc": "Picks random hours (0-23) and minutes (0-59), padding with zero digits.",
        "icon": "⏰",
        "inputs": [
            {"id": "time-format", "label": "Time Format:", "type": "select", "default": "12",
             "options": [
                 ("12", "12-Hour (AM/PM)"),
                 ("24", "24-Hour")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Random Time Output:", "type": "textarea"}
        ],
        "calc_js": """
            const fmt = document.getElementById('time-format').value;
            const hours = Math.floor(Math.random() * 24);
            const minutes = String(Math.floor(Math.random() * 60)).padStart(2, '0');

            let result = "";
            if (fmt === "24") {
                result = `${String(hours).padStart(2, '0')}:${minutes}`;
            } else {
                const ampm = hours >= 12 ? 'PM' : 'AM';
                let h12 = hours % 12;
                h12 = h12 ? h12 : 12; // hour '0' should be '12'
                result = `${h12}:${minutes} ${ampm}`;
            }

            document.getElementById('text-output').value = result;
            updateBreakdown(`<p class='text-success'>Generated random time: ${result}</p>`);
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Emoji Generator",
        "slug": "random-emoji-generator",
        "desc": "Get a random emoji from common smiley, nature, and food categories.",
        "formula": "Unicode index lookup",
        "formula_desc": "Picks random indexes from standard unicode emoji categories.",
        "icon": "😀",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Random Emoji:", "type": "textarea"}
        ],
        "calc_js": """
            const emojis = [
                "😀", "🚀", "🎉", "🔥", "🎨", "🌟", "🍔", "🍕", "🐶", "🐱", 
                "💻", "💡", "🔑", "🛡️", "🏁", "📦", "🏢", "📊", "🎯", "🤖"
            ];
            const chosen = emojis[Math.floor(Math.random() * emojis.length)];
            document.getElementById('text-output').value = chosen;
            updateBreakdown("<p class='text-success'>Emoji picked successfully.</p>");
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Fact Generator",
        "slug": "random-fact-generator",
        "desc": "Get interesting, funny, or educational random facts.",
        "formula": "Fact database lookup",
        "formula_desc": "Selects random science or history trivia statements from an internal list.",
        "icon": "🧠",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Random Fact:", "type": "textarea"}
        ],
        "calc_js": """
            const facts = [
                "Honey never spoils. You can theoretically eat 3,000-year-old honey.",
                "Bananas are berries, but strawberries aren't.",
                "Wombat poop is cube-shaped, preventing it from rolling away.",
                "The heart of a shrimp is located in its head.",
                "A day on Venus is longer than a year on Venus.",
                "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion."
            ];

            const chosen = facts[Math.floor(Math.random() * facts.length)];
            document.getElementById('text-output').value = chosen;
            updateBreakdown("<p class='text-success'>Random fact displayed.</p>");
        """
    },
    {
        "category": "Random Generators",
        "name": "Random Challenge Generator",
        "slug": "random-challenge-generator",
        "desc": "Get random mini challenges for coding, fitness, or self-improvement.",
        "formula": "Habit trigger lookup",
        "formula_desc": "Randomly selects task prompts encouraging learning and physical activity.",
        "icon": "🎯",
        "inputs": [
            {"id": "chal-type", "label": "Challenge Type:", "type": "select", "default": "productivity",
             "options": [
                 ("productivity", "Productivity & Self-Care"),
                 ("coding", "Coding Challenges")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Your Challenge Task:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('chal-type').value;

            const prod = [
                "Drink 3 liters of water today.",
                "Walk for 30 minutes outside without checking your phone.",
                "Write down three things you are grateful for today.",
                "Clean your workspace and organize your physical files.",
                "Read 10 pages of a non-fiction book today."
            ];

            const code = [
                "Code for 1 hour without opening any social media tabs.",
                "Refactor an old function to improve its readability.",
                "Write unit tests for a utility helper you recently wrote.",
                "Learn how to use a new CSS layout property (e.g. flexbox/grid).",
                "Explain a complex coding concept to a non-programmer."
            ];

            let pool = prod;
            if (type === "coding") pool = code;

            const chosen = pool[Math.floor(Math.random() * pool.length)];
            document.getElementById('text-output').value = chosen;
            updateBreakdown("<p class='text-success'>Challenge generated. Have fun!</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Fantasy Character Generator",
        "slug": "fantasy-character-generator",
        "desc": "Generate detailed fantasy character attributes, stats, and backstories.",
        "formula": "D&D attribute stats + backstory templates",
        "formula_desc": "Generates typical RPG stats (STR, AGI, INT) using 3d6 random dice rolls and appends class titles.",
        "icon": "🧙‍♂️",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Fantasy Character Profile:", "type": "textarea"}
        ],
        "calc_js": """
            const races = ["Elf", "Dwarf", "Human", "Orc", "Halfling"];
            const classes = ["Wizard", "Warrior", "Rogue", "Cleric", "Ranger"];
            const backstories = [
                "who is looking to avenge their lost mentor.",
                "seeking the ancient artifacts of the moon temple.",
                "running away from a mistaken crime.",
                "striving to protect their homeland from shadows."
            ];

            const rollStat = () => 6 + Math.floor(Math.random() * 5) + Math.floor(Math.random() * 5);

            const r = races[Math.floor(Math.random() * races.length)];
            const c = classes[Math.floor(Math.random() * classes.length)];
            const b = backstories[Math.floor(Math.random() * backstories.length)];

            const str = rollStat();
            const agi = rollStat();
            const int = rollStat();

            const profile = `Race: ${r}\\nClass: ${c}\\nBackstory: A brave adventurer ${b}\\n\\nStats:\\n- Strength: ${str}\\n- Agility: ${agi}\\n- Intelligence: ${int}`;
            document.getElementById('text-output').value = profile;
            updateBreakdown("<p class='text-success'>Character attributes and stats rolled.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Superhero Name Generator",
        "slug": "superhero-name-generator",
        "desc": "Generate epic superhero aliases for comics and writing.",
        "formula": "Heroic compounding prefix + noun",
        "formula_desc": "Combines heroic adjectives (Captain, Wonder, Mega) with elements and power nouns.",
        "icon": "🦸",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Superhero Names:", "type": "textarea"}
        ],
        "calc_js": """
            const prefix = ["Captain", "Wonder", "Super", "Mega", "Iron", "Shadow", "Aqua", "Doctor"];
            const suffix = ["Force", "Knight", "Ranger", "Glow", "Storm", "Frost", "Shield", "Blade"];

            let names = [];
            for (let i = 0; i < 5; i++) {
                let p = prefix[Math.floor(Math.random() * prefix.length)];
                let s = suffix[Math.floor(Math.random() * suffix.length)];
                names.push(`${p} ${s}`);
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Superhero name ideas compiled.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Villain Name Generator",
        "slug": "villain-name-generator",
        "desc": "Generate dark and menacing villain name concepts.",
        "formula": "Sinister prefix + dark noun",
        "formula_desc": "Combines villainous titles (Lord, Baron, Doctor) with dark elements and synonyms of doom.",
        "icon": "🦹",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Villain Names:", "type": "textarea"}
        ],
        "calc_js": """
            const prefix = ["Doctor", "Baron", "Lord", "Count", "Shadow", "Dark", "General", "Madam"];
            const suffix = ["Doom", "Wraith", "Viper", "Slash", "Phantom", "Ruin", "Malice", "Blight"];

            let names = [];
            for (let i = 0; i < 5; i++) {
                let p = prefix[Math.floor(Math.random() * prefix.length)];
                let s = suffix[Math.floor(Math.random() * suffix.length)];
                names.push(`${p} ${s}`);
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Villain names compiled.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Team Name Generator",
        "slug": "team-name-generator",
        "desc": "Generate catchy team names for sports, gaming, or work projects.",
        "formula": "Fierce adjective + plural noun",
        "formula_desc": "Pairs team adjectives (Mighty, Golden, Royal, Neon) with animal or object plural nouns.",
        "icon": "👥",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Team Names:", "type": "textarea"}
        ],
        "calc_js": """
            const adjs = ["Mighty", "Golden", "Royal", "Neon", "Cyber", "Iron", "Apex", "Velo"];
            const nouns = ["Panthers", "Wolves", "Sharks", "Knights", "Titans", "Raptors", "Eagles", "Slayers"];

            let names = [];
            for (let i = 0; i < 5; i++) {
                let a = adjs[Math.floor(Math.random() * adjs.length)];
                let n = nouns[Math.floor(Math.random() * nouns.length)];
                names.push(`${a} ${n}`);
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Team names compiled successfully.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Clan Name Generator",
        "slug": "clan-name-generator",
        "desc": "Generate epic clan and guild names for multiplayer games.",
        "formula": "Clan organization + descriptor",
        "formula_desc": "Combines group organization nouns (Syndicate, Dynasty, Order) with epic descriptors.",
        "icon": "🛡️",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Clan Names:", "type": "textarea"}
        ],
        "calc_js": """
            const prefix = ["Shadow", "Blood", "Iron", "Mithril", "Storm", "Wraith", "Aether", "Frost"];
            const organization = ["Syndicate", "Dynasty", "Order", "Alliance", "Legion", "Guild", "Clan", "Guard"];

            let names = [];
            for (let i = 0; i < 5; i++) {
                let p = prefix[Math.floor(Math.random() * prefix.length)];
                let o = organization[Math.floor(Math.random() * organization.length)];
                names.push(`${p} ${o}`);
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Epic clan names compiled.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Pet Name Generator",
        "slug": "pet-name-generator",
        "desc": "Generate cute and unique names for your dog, cat, or bird.",
        "formula": "Popular pet names selection",
        "formula_desc": "Selects random popular pet names from separate category profiles.",
        "icon": "🐱",
        "inputs": [
            {"id": "pet-type", "label": "Pet Type:", "type": "select", "default": "dog",
             "options": [
                 ("dog", "Dog Names"),
                 ("cat", "Cat Names"),
                 ("cute", "Cute / General")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Pet Names:", "type": "textarea"}
        ],
        "calc_js": """
            const type = document.getElementById('pet-type').value;

            const dogs = ["Max", "Rocky", "Charlie", "Cooper", "Buddy", "Jack", "Bailey", "Bella"];
            const cats = ["Luna", "Milo", "Oliver", "Leo", "Loki", "Simba", "Chloe", "Lucy"];
            const cute = ["Peanut", "Mochi", "Cookie", "Ziggy", "Gizmo", "Coco", "Teddy", "Waffles"];

            let pool = dogs;
            if (type === "cat") pool = cats;
            else if (type === "cute") pool = cute;

            let names = [];
            let shuf = [...pool].sort(() => 0.5 - Math.random());
            document.getElementById('text-output').value = shuf.slice(0, 5).join("\\n");
            updateBreakdown("<p class='text-success'>Pet names generated successfully.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Baby Name Generator",
        "slug": "baby-name-generator",
        "desc": "Generate baby name ideas based on gender classifications.",
        "formula": "Standard baby names mapping",
        "formula_desc": "Selects random baby names from Boy, Girl, or Gender-Neutral lists.",
        "icon": "👶",
        "inputs": [
            {"id": "baby-gender", "label": "Gender Focus:", "type": "select", "default": "neutral",
             "options": [
                 ("boy", "Boy Names"),
                 ("girl", "Girl Names"),
                 ("neutral", "Gender Neutral")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Baby Name Suggestions:", "type": "textarea"}
        ],
        "calc_js": """
            const gender = document.getElementById('baby-gender').value;

            const boys = ["Liam", "Noah", "Oliver", "James", "Elijah", "William", "Lucas", "Henry"];
            const girls = ["Olivia", "Emma", "Charlotte", "Amelia", "Sophia", "Isabella", "Mia", "Evelyn"];
            const neutral = ["Avery", "Jordan", "Taylor", "Morgan", "Riley", "Casey", "Alex", "Logan"];

            let pool = neutral;
            if (gender === "boy") pool = boys;
            else if (gender === "girl") pool = girls;

            let shuf = [...pool].sort(() => 0.5 - Math.random());
            document.getElementById('text-output').value = shuf.slice(0, 5).join("\\n");
            updateBreakdown("<p class='text-success'>Baby name ideas updated.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Rap Name Generator",
        "slug": "rap-name-generator",
        "desc": "Generate cool and punchy rap aliases.",
        "formula": "Lil/MC prefixing",
        "formula_desc": "Combines typical rap prefix tags (Lil, Young, MC, DJ) with custom nouns and modifiers.",
        "icon": "🎤",
        "inputs": [
            {"id": "rap-kw", "label": "Include Word (Optional):", "type": "text", "default": "Vibe"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Rap Names:", "type": "textarea"}
        ],
        "calc_js": """
            const kw = document.getElementById('rap-kw').value.trim();
            
            const prefixes = ["Lil", "MC", "Young", "DJ", "Big", "Kid", "T-"];
            const nouns = ["Money", "Glitch", "Rhyme", "Beats", "Spit", "Flow", "Wave"];

            let names = [];
            for (let i = 0; i < 5; i++) {
                let p = prefixes[Math.floor(Math.random() * prefixes.length)];
                let n = nouns[Math.floor(Math.random() * nouns.length)];
                let base = kw ? kw : n;
                names.push(`${p} ${base}`);
            }

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Rap stage name ideas compiled.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Band Name Generator",
        "slug": "band-name-generator",
        "desc": "Generate catchy rock, pop, or indie band name ideas.",
        "formula": "The + Adjective + plural noun",
        "formula_desc": "Combines atmospheric adjectives with plural nouns to output typical music band names.",
        "icon": "🎸",
        "inputs": [],
        "outputs": [
            {"id": "text-output", "label": "Suggested Band Names:", "type": "textarea"}
        ],
        "calc_js": """
            const adjs = ["Glass", "Cosmic", "Neon", "Silent", "Screaming", "Electric", "Dark", "Velvet"];
            const nouns = ["Moons", "Wolves", "Shadows", "Hearts", "Guitars", "Echoes", "Pilots", "Waves"];

            let names = [];
            for (let i = 0; i < 5; i++) {
                let a = adjs[Math.floor(Math.random() * adjs.length)];
                let n = nouns[Math.floor(Math.random() * nouns.length)];
                names.push(`The ${a} ${n}`);
                names.push(`${a} ${n}`);
            }
            names = [...new Set(names)].slice(0, 5);

            document.getElementById('text-output').value = names.join("\\n");
            updateBreakdown("<p class='text-success'>Band names compiled successfully.</p>");
        """
    },
    {
        "category": "Fun & Entertainment Generators",
        "name": "Movie Title Generator",
        "slug": "movie-title-generator",
        "desc": "Generate catch movie titles based on genres.",
        "formula": "Dramatic narrative title templates",
        "formula_desc": "Embeds dynamic nouns into standard dramatic movie title formats (The Last..., Flight of...).",
        "icon": "🎬",
        "inputs": [
            {"id": "movie-genre", "label": "Movie Genre:", "type": "select", "default": "action",
             "options": [
                 ("action", "Action / Sci-Fi"),
                 ("drama", "Drama / Mystery")
             ]}
        ],
        "outputs": [
            {"id": "text-output", "label": "Suggested Movie Titles:", "type": "textarea"}
        ],
        "calc_js": """
            const genre = document.getElementById('movie-genre').value;

            let titles = [];
            if (genre === "action") {
                const elements = ["Shadow", "Apex", "Force", "Neon", "Quantum", "Last"];
                const subjects = ["Protocol", "Horizon", "Strike", "Execution", "Agent", "Warlord"];
                for (let i = 0; i < 5; i++) {
                    let e = elements[Math.floor(Math.random() * elements.length)];
                    let s = subjects[Math.floor(Math.random() * subjects.length)];
                    titles.push(`${e} ${s}`);
                }
            } else {
                const leads = ["Secrets of", "Flight of", "The Lost", "Silence in", "The Return of"];
                const subjects = ["the Moon", "Zephyr", "Yesterday", "the Rain", "a Stranger"];
                for (let i = 0; i < 5; i++) {
                    let l = leads[Math.floor(Math.random() * leads.length)];
                    let s = subjects[Math.floor(Math.random() * subjects.length)];
                    titles.push(`${l} ${s}`);
                }
            }

            document.getElementById('text-output').value = titles.join("\\n");
            updateBreakdown("<p class='text-success'>Creative movie titles generated.</p>");
        """
    }
]
