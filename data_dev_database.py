# -*- coding: utf-8 -*-
"""
Database of 10 Database Tools for Enginewheels
"""

DATABASE_TOOLS = [
    {
        "category": "Database Tools",
        "name": "SQL Query Formatter",
        "slug": "sql-query-formatter",
        "desc": "Beautify and format complex SQL queries with proper keywords layout.",
        "formula": "SQL Formatter Rules Engine",
        "formula_desc": "Converts SQL query strings into structured indented statements by capitalizing core keywords.",
        "icon": "🛢️",
        "inputs": [
            {"id": "text-input", "label": "Enter Raw SQL:", "type": "textarea", "default": "select id, name from users join profiles on users.id = profiles.user_id where users.status='active'"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified SQL:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter an SQL query.", "error");
                return;
            }
            const keywords = ['SELECT', 'FROM', 'WHERE', 'ORDER BY', 'GROUP BY', 'LIMIT', 'JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'INNER JOIN', 'ON', 'HAVING', 'AND', 'OR', 'SET', 'UPDATE', 'INSERT INTO', 'VALUES', 'DELETE'];
            let sql = val.replace(/\\s+/g, ' ');
            
            keywords.forEach(kw => {
                const regex = new RegExp('\\\\b' + kw + '\\\\b', 'gi');
                sql = sql.replace(regex, '\\n' + kw);
            });
            
            let lines = sql.split('\\n');
            let formatted = '';
            lines.forEach(line => {
                let trimmed = line.trim();
                if (trimmed !== '') {
                    if (trimmed.startsWith('AND') || trimmed.startsWith('OR') || trimmed.startsWith('ON')) {
                        formatted += '  ' + trimmed + '\\n';
                    } else {
                        formatted += trimmed + '\\n';
                    }
                }
            });
            
            document.getElementById('text-output').value = formatted.trim();
            updateBreakdown("<p class='text-success'>SQL query formatted and keywords capitalized.</p>");
        """
    },
    {
        "category": "Database Tools",
        "name": "SQL Beautifier",
        "slug": "sql-beautifier",
        "desc": "Indent and align SQL database statements for improved readability.",
        "formula": "SQL Beautification Regex rules",
        "formula_desc": "Capitalizes SQL keyword tags and indents block subqueries.",
        "icon": "🛢️",
        "inputs": [
            {"id": "text-input", "label": "Paste SQL Statement:", "type": "textarea", "default": "select * from customers where country='USA' and status='active'"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Beautified SQL Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter SQL statement.", "error");
                return;
            }
            const keywords = ['SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'JOIN', 'ON'];
            let sql = val.replace(/\\s+/g, ' ');
            keywords.forEach(kw => {
                const regex = new RegExp('\\\\b' + kw + '\\\\b', 'gi');
                sql = sql.replace(regex, '\\n' + kw);
            });
            document.getElementById('text-output').value = sql.trim();
            updateBreakdown("<p class='text-success'>SQL formatting complete.</p>");
        """
    },
    {
        "category": "Database Tools",
        "name": "SQL Minifier",
        "slug": "sql-minifier",
        "desc": "Compress and minify SQL query codes by removing spaces and comments.",
        "formula": "SQL Space Compression Rules",
        "formula_desc": "Filters SQL strings by removing double dashes '--', multiline comments, and collapsing line breaks.",
        "icon": "🛢️",
        "inputs": [
            {"id": "text-input", "label": "Enter SQL to Minify:", "type": "textarea", "default": "-- Select active users\\nSELECT * \\nFROM users\\nWHERE status = 'active';"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Minified SQL Output:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('text-input').value.trim();
            if (!val) {
                showToast("Please enter SQL query.", "error");
                return;
            }
            let min = val
                .replace(/\\/\\*[\\s\\S]*?\\*\\//g, '') // remove block comments
                .replace(/--[^\\n\\r]*/g, '')          // remove line comments
                .replace(/\\s+/g, ' ')                  // collapse spaces
                .trim();
            document.getElementById('text-output').value = min;
            updateBreakdown("<p class='text-success'>SQL query minified for database CLI execution.</p>");
        """
    },
    {
        "category": "Database Tools",
        "name": "SQL Query Generator",
        "slug": "sql-query-generator",
        "desc": "Generate custom SQL SELECT queries dynamically using form inputs.",
        "formula": "Table inputs -> Formatted SQL SELECT Query",
        "formula_desc": "Assembles standard SELECT query text strings based on user table, fields, and condition selections.",
        "icon": "⚙️",
        "inputs": [
            {"id": "sql-table", "label": "Table Name:", "type": "text", "default": "users"},
            {"id": "sql-fields", "label": "Fields List (comma-separated):", "type": "text", "default": "id, name, email"},
            {"id": "sql-where", "label": "Where Clause Condition (e.g. status='active'):", "type": "text", "default": "status = 'active'"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated SQL Query:", "type": "textarea"}
        ],
        "calc_js": """
            const table = document.getElementById('sql-table').value.trim();
            const fields = document.getElementById('sql-fields').value.trim();
            const where = document.getElementById('sql-where').value.trim();
            
            if (!table || !fields) {
                showToast("Table and fields list are required.", "error");
                return;
            }
            
            let query = `SELECT ${fields}\\nFROM ${table}`;
            if (where) {
                query += `\\nWHERE ${where}`;
            }
            query += ";";
            
            document.getElementById('text-output').value = query;
            updateBreakdown("<p class='text-success'>SQL Query generated successfully.</p>");
        """
    },
    {
        "category": "Database Tools",
        "name": "Database Schema Viewer",
        "slug": "database-schema-viewer",
        "desc": "Check and display database column properties inside clean schema cards.",
        "formula": "Columns Definition Parser",
        "formula_desc": "Parses custom table attributes fields, formatting them inside a visual schema grid.",
        "icon": "👁️",
        "inputs": [
            {"id": "schema-table", "label": "Table Name:", "type": "text", "default": "users"},
            {"id": "schema-cols", "label": "Columns & Types (Format: col:type, line-by-line):", "type": "textarea", "default": "id: INT PRIMARY KEY\\nname: VARCHAR(100)\\nemail: VARCHAR(255) UNIQUE\\ncreated_at: TIMESTAMP"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Schema SQL Output:", "type": "textarea"}
        ],
        "calc_js": """
            const table = document.getElementById('schema-table').value.trim();
            const colsVal = document.getElementById('schema-cols').value.trim();
            
            if (!table || !colsVal) {
                showToast("Please enter table name and column rules.", "error");
                return;
            }
            
            const lines = colsVal.split('\\n');
            let sql = `CREATE TABLE ${table} (\\n`;
            let htmlCard = `<div style="border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:15px; background:rgba(0,0,0,0.2); width:280px; margin:15px auto; text-align:left;">`;
            htmlCard += `<h4 style="border-bottom:1px solid #7C3AED; padding-bottom:5px; margin-top:0; color:#fff;">🛢️ ${table}</h4>`;
            htmlCard += `<ul style="list-style-type:none; padding:0; margin:0; font-family:monospace; font-size:0.9rem;">`;
            
            lines.forEach((line, idx) => {
                if (line.includes(':')) {
                    const parts = line.split(':');
                    const col = parts[0].trim();
                    const type = parts[1].trim();
                    sql += `  ${col} ${type}${idx === lines.length - 1 ? '' : ','}\\n`;
                    htmlCard += `<li style="padding:4px 0;"><span style="color:#EF4444;">${col}</span>: <span style="color:#ccc;">${type}</span></li>`;
                }
            });
            sql += ");";
            htmlCard += "</ul></div>";
            
            document.getElementById('text-output').value = sql;
            updateBreakdown(htmlCard);
            showToast("Visual schema loaded below.");
        """
    },
    {
        "category": "Database Tools",
        "name": "ER Diagram Generator",
        "slug": "er-diagram-generator",
        "desc": "Check entity relationships and compile visual schema connections.",
        "formula": "Primary -> Foreign Key mapping",
        "formula_desc": "Maps table relational dependencies into structured visual nodes list showing database schema connections.",
        "icon": "🌲",
        "inputs": [
            {"id": "er-relations", "label": "Enter Relationships (e.g. users.id -> profiles.user_id, line-by-line):", "type": "textarea", "default": "users.id -> posts.user_id\\nposts.id -> comments.post_id"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Mapped Connections:", "type": "textarea"}
        ],
        "calc_js": """
            const val = document.getElementById('er-relations').value.trim();
            if (!val) {
                showToast("Please enter some relationships.", "error");
                return;
            }
            const lines = val.split('\\n');
            let listHtml = "<div style='text-align:left; padding:10px; font-family:monospace; color:#ccc;'>";
            lines.forEach(line => {
                if (line.includes('->')) {
                    const parts = line.split('->');
                    listHtml += `<div style='padding:5px 0;'><span style='color:#7C3AED; font-weight:bold;'>${parts[0].trim()}</span> ───▶ <span style='color:#EF4444; font-weight:bold;'>${parts[1].trim()}</span></div>`;
                }
            });
            listHtml += "</div>";
            document.getElementById('text-output').value = val;
            updateBreakdown(listHtml);
        """
    },
    {
        "category": "Database Tools",
        "name": "Table Creator",
        "slug": "table-creator",
        "desc": "Design custom tables and output HTML, Markdown, or SQL schemas.",
        "formula": "Grid Matrix Table Rendering",
        "formula_desc": "Constructs columns and rows elements based on column configurations.",
        "icon": "📊",
        "inputs": [
            {"id": "tc-cols", "label": "Columns list (comma-separated):", "type": "text", "default": "id, name, email"},
            {"id": "tc-rows", "label": "Rows count:", "type": "number", "default": "3"}
        ],
        "outputs": [
            {"id": "text-output", "label": "HTML Table Code Output:", "type": "textarea"}
        ],
        "calc_js": """
            const colsVal = document.getElementById('tc-cols').value.trim();
            const rows = parseInt(document.getElementById('tc-rows').value) || 1;
            
            if (!colsVal) {
                showToast("Please enter column names.", "error");
                return;
            }
            
            const cols = colsVal.split(',').map(c => c.trim());
            let html = "<table>\\n  <thead>\\n    <tr>\\n";
            cols.forEach(col => {
                html += `      <th>${col}</th>\\n`;
            });
            html += "    </tr>\\n  </thead>\\n  <tbody>\\n";
            for (let i = 1; i <= rows; i++) {
                html += "    <tr>\\n";
                cols.forEach(col => {
                    html += `      <td>value</td>\\n`;
                });
                html += "    </tr>\\n";
            }
            html += "  </tbody>\\n</table>";
            
            document.getElementById('text-output').value = html;
            updateBreakdown(html);
        """
    },
    {
        "category": "Database Tools",
        "name": "Mock Database Generator",
        "slug": "mock-database-generator",
        "desc": "Generate dummy SQL database tables with insert statements containing mock usernames.",
        "formula": "Random User Generator Loop",
        "formula_desc": "Compiles SQL scripts by loops adding typical primary key integers and mock names.",
        "icon": "🛢️",
        "inputs": [
            {"id": "mb-table", "label": "Target SQL Table Name:", "type": "text", "default": "users"},
            {"id": "mb-count", "label": "Number of Records:", "type": "number", "default": "5"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Mock SQL SQL Script:", "type": "textarea"}
        ],
        "calc_js": """
            const table = document.getElementById('mb-table').value.trim();
            const count = parseInt(document.getElementById('mb-count').value) || 5;
            
            const firstNames = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah'];
            const lastNames = ['Smith', 'Doe', 'Jones', 'Miller', 'Davis', 'Wilson'];
            const roles = ['Admin', 'Editor', 'User', 'Developer'];
            
            let sql = `INSERT INTO ${table} (id, name, email, role)\\nVALUES\\n`;
            for (let i = 1; i <= count; i++) {
                const fname = firstNames[Math.floor(Math.random() * firstNames.length)];
                const lname = lastNames[Math.floor(Math.random() * lastNames.length)];
                const role = roles[Math.floor(Math.random() * roles.length)];
                const email = `${fname.toLowerCase()}.${lname.toLowerCase()}@example.com`;
                
                sql += `  (${i}, '${fname} ${lname}', '${email}', '${role}')${i === count ? ';' : ','}\\n`;
            }
            document.getElementById('text-output').value = sql;
            updateBreakdown("<p class='text-success'>Mock dataset generated successfully with " + count + " records.</p>");
        """
    },
    {
        "category": "Database Tools",
        "name": "CSV Import Generator",
        "slug": "csv-import-generator",
        "desc": "Convert CSV rows into SQL INSERT database scripts.",
        "formula": "CSV Split -> INSERT INTO SQL",
        "formula_desc": "Transforms lines into structured SQL insert statements using columns.",
        "icon": "🔄",
        "inputs": [
            {"id": "csv-table", "label": "Target Database Table Name:", "type": "text", "default": "users"},
            {"id": "csv-data", "label": "Paste CSV data (first row headers):", "type": "textarea", "default": "id,name,role\\n1,Alice,Dev\\n2,Bob,PM"}
        ],
        "outputs": [
            {"id": "text-output", "label": "Generated SQL Script:", "type": "textarea"}
        ],
        "calc_js": """
            const table = document.getElementById('csv-table').value.trim();
            const csv = document.getElementById('csv-data').value.trim();
            
            if (!table || !csv) {
                showToast("Please enter table name and CSV data.", "error");
                return;
            }
            try {
                const lines = csv.split('\\n').map(l => l.split(',').map(c => c.trim()));
                if (lines.length < 2) {
                    throw new Error("CSV requires headers and data rows.");
                }
                const headers = lines[0].join(', ');
                let sql = `INSERT INTO ${table} (${headers})\\nVALUES\\n`;
                
                for (let i = 1; i < lines.length; i++) {
                    const row = lines[i];
                    if (row.length === 1 && row[0] === '') continue;
                    let values = row.map(cell => {
                        return isNaN(cell) ? `'${cell.replace(/'/g, "''")}'` : cell;
                    }).join(', ');
                    sql += `  (${values})${i === lines.length - 1 ? ';' : ','}\\n`;
                }
                document.getElementById('text-output').value = sql;
                updateBreakdown("<p class='text-success'>CSV imported and translated to SQL statements.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                showToast("Failed importing CSV!", "error");
            }
        """
    },
    {
        "category": "Database Tools",
        "name": "SQL Export Generator",
        "slug": "sql-export-generator",
        "desc": "Translate JSON object arrays into SQL schema export files.",
        "formula": "JSON attributes loop -> CREATE TABLE + INSERT SQL",
        "formula_desc": "Analyzes JSON properties to generate CREATE TABLE schemas and matching database INSERT lines.",
        "icon": "🔄",
        "inputs": [
            {"id": "json-table", "label": "Database Table Name:", "type": "text", "default": "users"},
            {"id": "json-data", "label": "Paste JSON Array:", "type": "textarea", "default": '[\n  {"id": 1, "name": "Alice", "role": "Dev"},\n  {"id": 2, "name": "Bob", "role": "PM"}\n]'}
        ],
        "outputs": [
            {"id": "text-output", "label": "SQL Schema & Data Export:", "type": "textarea"}
        ],
        "calc_js": """
            const table = document.getElementById('json-table').value.trim();
            const jsonVal = document.getElementById('json-data').value.trim();
            
            if (!table || !jsonVal) {
                showToast("Please enter table name and JSON data.", "error");
                return;
            }
            try {
                let obj = JSON.parse(jsonVal);
                if (!Array.isArray(obj)) obj = [obj];
                
                const keys = Object.keys(obj[0]);
                let sql = `CREATE TABLE ${table} (\\n`;
                keys.forEach((key, idx) => {
                    const type = typeof obj[0][key] === 'number' ? 'INT' : 'VARCHAR(255)';
                    sql += `  ${key} ${type}${idx === keys.length - 1 ? '' : ','}\\n`;
                });
                sql += `);\\n\\nINSERT INTO ${table} (${keys.join(', ')})\\nVALUES\\n`;
                
                obj.forEach((item, iIdx) => {
                    const vals = keys.map(k => {
                        const val = item[k];
                        return typeof val === 'number' ? val : `'${String(val).replace(/'/g, "''")}'`;
                    }).join(', ');
                    sql += `  (${vals})${iIdx === obj.length - 1 ? ';' : ','}\\n`;
                });
                
                document.getElementById('text-output').value = sql;
                updateBreakdown("<p class='text-success'>SQL Export Script generated successfully.</p>");
            } catch(e) {
                document.getElementById('text-output').value = "Error: " + e.message;
                showToast("Invalid JSON data structure!", "error");
            }
        """
    }
]
