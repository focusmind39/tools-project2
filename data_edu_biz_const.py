# -*- coding: utf-8 -*-
"""
Education, Business, and Construction Calculators Data
"""

EDU_CALCS = [
    {
        "name": "GPA Calculator",
        "slug": "gpa-calculator",
        "category": "Education",
        "icon": "🎓",
        "desc": "Calculate your semester Grade Point Average (GPA) based on grades and course credits.",
        "formula": "GPA = Sum(Grade Points * Credits) / Sum(Credits)",
        "formula_desc": "Multiplies course grades by credit values to find the overall weighted academic average.",
        "inputs": [
            {"id": "gpa-g1", "label": "Course 1 Grade", "type": "select", "options": [("4.0", "A (4.0)"), ("3.0", "B (3.0)"), ("2.0", "C (2.0)"), ("1.0", "D (1.0)"), ("0.0", "F (0.0)")]},
            {"id": "gpa-c1", "label": "Course 1 Credits", "type": "number", "default": "3", "min": "1", "max": "6", "step": "1"},
            {"id": "gpa-g2", "label": "Course 2 Grade", "type": "select", "options": [("4.0", "A (4.0)"), ("3.0", "B (3.0)"), ("2.0", "C (2.0)"), ("1.0", "D (1.0)"), ("0.0", "F (0.0)")]},
            {"id": "gpa-c2", "label": "Course 2 Credits", "type": "number", "default": "3", "min": "1", "max": "6", "step": "1"},
            {"id": "gpa-g3", "label": "Course 3 Grade", "type": "select", "options": [("4.0", "A (4.0)"), ("3.0", "B (3.0)"), ("2.0", "C (2.0)"), ("1.0", "D (1.0)"), ("0.0", "F (0.0)")]},
            {"id": "gpa-c3", "label": "Course 3 Credits", "type": "number", "default": "4", "min": "1", "max": "6", "step": "1"},
            {"id": "gpa-g4", "label": "Course 4 Grade", "type": "select", "options": [("4.0", "A (4.0)"), ("3.0", "B (3.0)"), ("2.0", "C (2.0)"), ("1.0", "D (1.0)"), ("0.0", "F (0.0)")]},
            {"id": "gpa-c4", "label": "Course 4 Credits", "type": "number", "default": "3", "min": "1", "max": "6", "step": "1"}
        ],
        "outputs": [
            {"id": "out-gpa-val", "label": "GPA", "prefix": "", "suffix": " / 4.00"},
            {"id": "out-gpa-credits", "label": "Total Credits", "prefix": "", "suffix": " credits"}
        ],
        "calc_js": """
            let totalPoints = 0;
            let totalCredits = 0;
            for (let i = 1; i <= 4; i++) {
                const g = parseFloat(document.getElementById('gpa-g' + i).value);
                const c = parseFloat(document.getElementById('gpa-c' + i).value);
                if (!isNaN(g) && !isNaN(c) && c > 0) {
                    totalPoints += g * c;
                    totalCredits += c;
                }
            }

            if (totalCredits === 0) {
                showToast("Please enter valid credits.", "error");
                return;
            }

            const gpa = totalPoints / totalCredits;
            document.getElementById('out-gpa-val').textContent = gpa.toFixed(2);
            document.getElementById('out-gpa-credits').textContent = totalCredits;

            updateBreakdown(`
                <p><strong>Weighted Points:</strong> ${totalPoints.toFixed(1)}</p>
                <p><strong>Total Credits:</strong> ${totalCredits}</p>
            `);
        """
    },
    {
        "name": "CGPA Calculator",
        "slug": "cgpa-calculator",
        "category": "Education",
        "icon": "🎓",
        "desc": "Calculate your Cumulative Grade Point Average (CGPA) for multiple semesters.",
        "formula": "CGPA = Sum(Semester GPA * Semester Credits) / Sum(Semester Credits)",
        "formula_desc": "Computes cumulative weighted grade averages across semesters.",
        "inputs": [
            {"id": "cgpa-s1", "label": "Semester 1 GPA", "type": "number", "default": "3.5", "min": "0", "max": "10", "step": "0.01"},
            {"id": "cgpa-c1", "label": "Semester 1 Credits", "type": "number", "default": "15", "min": "1", "max": "30", "step": "1"},
            {"id": "cgpa-s2", "label": "Semester 2 GPA", "type": "number", "default": "3.6", "min": "0", "max": "10", "step": "0.01"},
            {"id": "cgpa-c2", "label": "Semester 2 Credits", "type": "number", "default": "15", "min": "1", "max": "30", "step": "1"},
            {"id": "cgpa-s3", "label": "Semester 3 GPA", "type": "number", "default": "3.4", "min": "0", "max": "10", "step": "0.01"},
            {"id": "cgpa-c3", "label": "Semester 3 Credits", "type": "number", "default": "18", "min": "1", "max": "30", "step": "1"}
        ],
        "outputs": [
            {"id": "out-cgpa-val", "label": "CGPA", "prefix": "", "suffix": ""},
            {"id": "out-cgpa-credits", "label": "Total Credits", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            let totalPoints = 0;
            let totalCredits = 0;
            for (let i = 1; i <= 3; i++) {
                const s = parseFloat(document.getElementById('cgpa-s' + i).value);
                const c = parseFloat(document.getElementById('cgpa-c' + i).value);
                if (!isNaN(s) && !isNaN(c) && s >= 0 && c > 0) {
                    totalPoints += s * c;
                    totalCredits += c;
                }
            }

            if (totalCredits === 0) {
                showToast("Please check GPA and Credit inputs.", "error");
                return;
            }

            const cgpa = totalPoints / totalCredits;
            document.getElementById('out-cgpa-val').textContent = cgpa.toFixed(2);
            document.getElementById('out-cgpa-credits').textContent = totalCredits;

            updateBreakdown(`
                <p>Cumulative GPA: <strong>${cgpa.toFixed(3)}</strong> over ${totalCredits} total credits.</p>
            `);
        """
    },
    {
        "name": "Percentage to GPA Converter",
        "slug": "percentage-to-gpa-converter",
        "category": "Education",
        "icon": "🎓",
        "desc": "Convert standard academic percentages to a standard US 4.0 GPA scale.",
        "formula": "GPA = (Percentage / 20) - 1 (Approximate scale)",
        "formula_desc": "Maps percentage grades to standard GPA metrics (e.g. 90-100% is 3.5-4.0).",
        "inputs": [
            {"id": "pgc-pct", "label": "Academic Percentage Grade (%)", "type": "number", "default": "85", "min": "0", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-pgc-gpa", "label": "US 4.0 Scale GPA", "prefix": "", "suffix": " / 4.00"},
            {"id": "out-pgc-letter", "label": "Equivalent Letter Grade", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const pct = parseFloat(document.getElementById('pgc-pct').value);

            if (isNaN(pct) || pct < 0 || pct > 100) {
                showToast("Percentage must be between 0 and 100.", "error");
                return;
            }

            let gpa = 0;
            let letter = "F";
            if (pct >= 90) { gpa = 4.0; letter = "A"; }
            else if (pct >= 80) { gpa = 3.0 + (pct - 80) * 0.1; letter = "B"; }
            else if (pct >= 70) { gpa = 2.0 + (pct - 70) * 0.1; letter = "C"; }
            else if (pct >= 60) { gpa = 1.0 + (pct - 60) * 0.1; letter = "D"; }
            else { gpa = 0.0; letter = "F"; }

            document.getElementById('out-pgc-gpa').textContent = gpa.toFixed(2);
            document.getElementById('out-pgc-letter').textContent = letter;

            updateBreakdown(`
                <p>Percentage <strong>${pct}%</strong> corresponds to Letter Grade <strong>${letter}</strong>.</p>
            `);
        """
    },
    {
        "name": "Marks Percentage Calculator",
        "slug": "marks-percentage-calculator",
        "category": "Education",
        "icon": "📝",
        "desc": "Calculate your grade percentage based on total marks obtained and maximum marks.",
        "formula": "Percentage = (Obtained Marks / Total Marks) * 100",
        "formula_desc": "Computes standard relative ratios of correct answers or total test points.",
        "inputs": [
            {"id": "mpc-obt", "label": "Marks Obtained", "type": "number", "default": "425", "min": "0", "max": "5000", "step": "1"},
            {"id": "mpc-tot", "label": "Maximum Marks", "type": "number", "default": "500", "min": "1", "max": "5000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-mpc-pct", "label": "Percentage", "prefix": "", "suffix": "%"},
            {"id": "out-mpc-fraction", "label": "Fraction Score", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const obt = parseFloat(document.getElementById('mpc-obt').value);
            const tot = parseFloat(document.getElementById('mpc-tot').value);

            if (isNaN(obt) || isNaN(tot) || obt < 0 || tot <= 0 || obt > tot) {
                showToast("Obtained marks cannot exceed maximum marks.", "error");
                return;
            }

            const pct = (obt / tot) * 100;
            document.getElementById('out-mpc-pct').textContent = pct.toFixed(2);
            document.getElementById('out-mpc-fraction').textContent = obt + " / " + tot;

            updateBreakdown(`
                <p>Score: <strong>${pct.toFixed(2)}%</strong></p>
            `);
        """
    },
    {
        "name": "Attendance Calculator",
        "slug": "attendance-calculator",
        "category": "Education",
        "icon": "📅",
        "desc": "Calculate how many more classes you need to attend or can skip to maintain a target attendance %.",
        "formula": "Classes Required = Target % * Total - Attended",
        "formula_desc": "Evaluates attendance deficits to check compliance with standard class schedules.",
        "inputs": [
            {"id": "att-present", "label": "Classes Present", "type": "number", "default": "35", "min": "0", "max": "500", "step": "1"},
            {"id": "att-total", "label": "Total Classes Conducted", "type": "number", "default": "45", "min": "1", "max": "500", "step": "1"},
            {"id": "att-target", "label": "Target Attendance (%)", "type": "number", "default": "75", "min": "50", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-att-current", "label": "Current Attendance", "prefix": "", "suffix": "%"},
            {"id": "out-att-status", "label": "Classes Status", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const present = parseFloat(document.getElementById('att-present').value);
            const total = parseFloat(document.getElementById('att-total').value);
            const target = parseFloat(document.getElementById('att-target').value);

            if (isNaN(present) || isNaN(total) || isNaN(target) || present < 0 || total <= 0 || present > total) {
                showToast("Present classes cannot exceed total classes.", "error");
                return;
            }

            const current = (present / total) * 100;
            document.getElementById('out-att-current').textContent = current.toFixed(1);

            let statusStr = "";
            if (current >= target) {
                // How many classes can be skipped
                let skip = 0;
                let tempTotal = total;
                let tempPresent = present;
                while ((tempPresent / tempTotal) * 100 >= target) {
                    skip++;
                    tempTotal++;
                }
                skip--;
                statusStr = `You can skip next ${skip} classes.`;
            } else {
                // How many classes must be attended
                let req = 0;
                let tempTotal = total;
                let tempPresent = present;
                while ((tempPresent / tempTotal) * 100 < target) {
                    req++;
                    tempTotal++;
                    tempPresent++;
                }
                statusStr = `You must attend next ${req} classes.`;
            }

            document.getElementById('out-att-status').textContent = statusStr;
            updateBreakdown(`<p>Current status: ${current.toFixed(1)}% | Target required: ${target}%</p>`);
        """
    },
    {
        "name": "Study Time Calculator",
        "slug": "study-time-calculator",
        "category": "Education",
        "icon": "📚",
        "desc": "Calculate recommended study hours per week based on course credits and course difficulty.",
        "formula": "Study Hours = Credits * Difficulty Factor (2 for Easy, 3 for Medium, 4 for Hard)",
        "formula_desc": "Translates college credit counts to home study hours depending on target difficulty.",
        "inputs": [
            {"id": "st-credits", "label": "Total Course Credits", "type": "number", "default": "15", "min": "1", "max": "30", "step": "1"},
            {"id": "st-diff", "label": "Average Difficulty", "type": "select", "options": [
                ("2", "Easy (2 hours/credit)"),
                ("3", "Medium (3 hours/credit)"),
                ("4", "Hard (4 hours/credit)")
            ]}
        ],
        "outputs": [
            {"id": "out-st-hours", "label": "Weekly Study Target", "prefix": "", "suffix": " hours"},
            {"id": "out-st-daily", "label": "Daily Study Target", "prefix": "", "suffix": " hours"}
        ],
        "calc_js": """
            const credits = parseFloat(document.getElementById('st-credits').value);
            const diff = parseFloat(document.getElementById('st-diff').value);

            if (isNaN(credits) || credits <= 0) {
                showToast("Please check credits value.", "error");
                return;
            }

            const weekly = credits * diff;
            const daily = weekly / 7;

            document.getElementById('out-st-hours').textContent = weekly;
            document.getElementById('out-st-daily').textContent = daily.toFixed(1);

            updateBreakdown(`
                <p>We recommend studying <strong>${weekly} hours per week</strong> outside of classroom sessions.</p>
            `);
        """
    },
    {
        "name": "Exam Score Calculator",
        "slug": "exam-score-calculator",
        "category": "Education",
        "icon": "📝",
        "desc": "Calculate the final exam score you need to achieve a target overall grade in a course.",
        "formula": "Required Score = [Target - Current * (1 - Weight)] / Weight",
        "formula_desc": "Calculates required final test scores based on current grade and exam percentage weight.",
        "inputs": [
            {"id": "esc-curr", "label": "Current Grade (%)", "type": "number", "default": "82", "min": "0", "max": "100", "step": "0.1"},
            {"id": "esc-target", "label": "Target Overall Grade (%)", "type": "number", "default": "85", "min": "0", "max": "100", "step": "0.1"},
            {"id": "esc-weight", "label": "Final Exam Weight (%)", "type": "number", "default": "25", "min": "1", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-esc-req", "label": "Required Exam Score", "prefix": "", "suffix": "%"},
            {"id": "out-esc-status", "label": "Exertion Status", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const curr = parseFloat(document.getElementById('esc-curr').value);
            const target = parseFloat(document.getElementById('esc-target').value);
            const weight = parseFloat(document.getElementById('esc-weight').value) / 100;

            if (isNaN(curr) || isNaN(target) || isNaN(weight) || curr < 0 || target < 0 || weight <= 0) {
                showToast("Please check input fields.", "error");
                return;
            }

            const req = (target - (curr * (1 - weight))) / weight;
            document.getElementById('out-esc-req').textContent = req.toFixed(1);

            let status = "Possible";
            if (req > 100) {
                status = "Virtually Impossible (Needs extra credit)";
            } else if (req < 0) {
                status = "Guaranteed (You already passed)";
            } else if (req > 90) {
                status = "Extremely Challenging";
            }
            
            document.getElementById('out-esc-status').textContent = status;
            updateBreakdown(`<p>Required test score to secure ${target.toFixed(1)}% is ${req.toFixed(1)}%.</p>`);
        """
    },
    {
        "name": "Grade Calculator",
        "slug": "grade-calculator",
        "category": "Education",
        "icon": "📝",
        "desc": "Calculate weighted averages for assignments, quizzes, midterms, and final exam grades.",
        "formula": "Weighted Grade = Sum(Grade * Weight) / Sum(Weights)",
        "formula_desc": "Aggregates exam components based on specific syllabus grading weights.",
        "inputs": [
            {"id": "gc-g1", "label": "Assignments Score (%)", "type": "number", "default": "90", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-w1", "label": "Assignments Weight (%)", "type": "number", "default": "20", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-g2", "label": "Quizzes Score (%)", "type": "number", "default": "85", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-w2", "label": "Quizzes Weight (%)", "type": "number", "default": "15", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-g3", "label": "Midterm Score (%)", "type": "number", "default": "80", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-w3", "label": "Midterm Weight (%)", "type": "number", "default": "30", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-g4", "label": "Final Exam Score (%)", "type": "number", "default": "78", "min": "0", "max": "100", "step": "1"},
            {"id": "gc-w4", "label": "Final Exam Weight (%)", "type": "number", "default": "35", "min": "0", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-gc-final", "label": "Weighted Overall Grade", "prefix": "", "suffix": "%"},
            {"id": "out-gc-weight-sum", "label": "Total Weights Sum", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            let weightedSum = 0;
            let weightTotal = 0;
            for (let i = 1; i <= 4; i++) {
                const g = parseFloat(document.getElementById('gc-g' + i).value);
                const w = parseFloat(document.getElementById('gc-w' + i).value);
                if (!isNaN(g) && !isNaN(w) && w > 0) {
                    weightedSum += g * (w / 100);
                    weightTotal += w;
                }
            }

            if (weightTotal === 0) {
                showToast("Total weights must exceed 0%.", "error");
                return;
            }

            const overall = (weightedSum / (weightTotal / 100));
            document.getElementById('out-gc-final').textContent = overall.toFixed(2);
            document.getElementById('out-gc-weight-sum').textContent = weightTotal;

            updateBreakdown(`
                <p>Overall Grade: <strong>${overall.toFixed(2)}%</strong> (Weights accounted: ${weightTotal}%)</p>
            `);
        """
    },
    {
        "name": "Average Marks Calculator",
        "slug": "average-marks-calculator",
        "category": "Education",
        "icon": "📝",
        "desc": "Calculate the arithmetic average score for up to 6 different subjects.",
        "formula": "Average = Sum(Marks) / Number of Subjects",
        "formula_desc": "Divides sum score value by total subject count to evaluate overall performance.",
        "inputs": [
            {"id": "amc-m1", "label": "Subject 1 Marks", "type": "number", "default": "85", "min": "0", "max": "100", "step": "1"},
            {"id": "amc-m2", "label": "Subject 2 Marks", "type": "number", "default": "92", "min": "0", "max": "100", "step": "1"},
            {"id": "amc-m3", "label": "Subject 3 Marks", "type": "number", "default": "78", "min": "0", "max": "100", "step": "1"},
            {"id": "amc-m4", "label": "Subject 4 Marks", "type": "number", "default": "89", "min": "0", "max": "100", "step": "1"},
            {"id": "amc-m5", "label": "Subject 5 Marks", "type": "number", "default": "95", "min": "0", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-amc-avg", "label": "Average Score", "prefix": "", "suffix": "%"},
            {"id": "out-amc-total", "label": "Total Cumulative Marks", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            let sum = 0;
            let count = 0;
            for (let i = 1; i <= 5; i++) {
                const val = parseFloat(document.getElementById('amc-m' + i).value);
                if (!isNaN(val)) {
                    sum += val;
                    count++;
                }
            }

            if (count === 0) {
                showToast("Please enter marks.", "error");
                return;
            }

            const avg = sum / count;
            document.getElementById('out-amc-avg').textContent = avg.toFixed(2);
            document.getElementById('out-amc-total').textContent = sum;

            updateBreakdown(`
                <p>Arithmetic mean: <strong>${avg.toFixed(2)}</strong> over ${count} inputs.</p>
            `);
        """
    },
    {
        "name": "Weighted Average Calculator",
        "slug": "weighted-average-calculator",
        "category": "Education",
        "icon": "⚖️",
        "desc": "Calculate the weighted average of values with differing percentage or fractional weights.",
        "formula": "Weighted Average = Sum(Value * Weight) / Sum(Weights)",
        "formula_desc": "Multiplies each value by its relative weight and divides by the sum of weights.",
        "inputs": [
            {"id": "wac-v1", "label": "Value 1", "type": "number", "default": "80", "min": "0", "max": "1000000", "step": "1"},
            {"id": "wac-w1", "label": "Weight 1", "type": "number", "default": "50", "min": "0.1", "max": "1000", "step": "1"},
            {"id": "wac-v2", "label": "Value 2", "type": "number", "default": "90", "min": "0", "max": "1000000", "step": "1"},
            {"id": "wac-w2", "label": "Weight 2", "type": "number", "default": "30", "min": "0.1", "max": "1000", "step": "1"},
            {"id": "wac-v3", "label": "Value 3", "type": "number", "default": "95", "min": "0", "max": "1000000", "step": "1"},
            {"id": "wac-w3", "label": "Weight 3", "type": "number", "default": "20", "min": "0.1", "max": "1000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-wac-avg", "label": "Weighted Average", "prefix": "", "suffix": ""},
            {"id": "out-wac-wsum", "label": "Total Weights Sum", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            let weightedSum = 0;
            let weightTotal = 0;
            for (let i = 1; i <= 3; i++) {
                const v = parseFloat(document.getElementById('wac-v' + i).value);
                const w = parseFloat(document.getElementById('wac-w' + i).value);
                if (!isNaN(v) && !isNaN(w) && w > 0) {
                    weightedSum += v * w;
                    weightTotal += w;
                }
            }

            if (weightTotal === 0) {
                showToast("Total weights must exceed 0.", "error");
                return;
            }

            const avg = weightedSum / weightTotal;
            document.getElementById('out-wac-avg').textContent = avg.toFixed(2);
            document.getElementById('out-wac-wsum').textContent = weightTotal;

            updateBreakdown(`
                <p>Weighted value: <strong>${avg.toFixed(4)}</strong></p>
            `);
        """
    }
]

BUSINESS_CALCS = [
    {
        "name": "Invoice Calculator",
        "slug": "invoice-calculator",
        "category": "Business",
        "icon": "🧾",
        "desc": "Calculate subtotal, tax amounts, discount deductions, and invoice grand totals.",
        "formula": "Total = Subtotal - Discount + Tax",
        "formula_desc": "Deducts discounts and adds taxes to the product quantity subtotal.",
        "inputs": [
            {"id": "inv-price", "label": "Unit Price ($)", "type": "number", "default": "45.00", "min": "0.01", "max": "1000000", "step": "0.01"},
            {"id": "inv-qty", "label": "Quantity", "type": "number", "default": "10", "min": "1", "max": "100000", "step": "1"},
            {"id": "inv-disc", "label": "Discount Rate (%)", "type": "number", "default": "5", "min": "0", "max": "100", "step": "0.1"},
            {"id": "inv-tax", "label": "Tax Rate (%)", "type": "number", "default": "8.5", "min": "0", "max": "50", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-inv-sub", "label": "Subtotal", "prefix": "$", "suffix": ""},
            {"id": "out-inv-tax", "label": "Calculated Tax", "prefix": "$", "suffix": ""},
            {"id": "out-inv-tot", "label": "Invoice Total", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const price = parseFloat(document.getElementById('inv-price').value);
            const qty = parseFloat(document.getElementById('inv-qty').value);
            const disc = parseFloat(document.getElementById('inv-disc').value) || 0;
            const tax = parseFloat(document.getElementById('inv-tax').value) || 0;

            if (isNaN(price) || isNaN(qty) || price <= 0 || qty <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const sub = price * qty;
            const discVal = sub * (disc / 100);
            const taxable = sub - discVal;
            const taxVal = taxable * (tax / 100);
            const total = taxable + taxVal;

            document.getElementById('out-inv-sub').textContent = sub.toFixed(2);
            document.getElementById('out-inv-tax').textContent = taxVal.toFixed(2);
            document.getElementById('out-inv-tot').textContent = total.toFixed(2);

            updateBreakdown(`
                <p>Gross subtotal: $${sub.toFixed(2)}</p>
                <p>Discount applied (${disc}%): -$${discVal.toFixed(2)}</p>
                <p>Tax applied (${tax}%): +$${taxVal.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "VAT Calculator",
        "slug": "vat-calculator",
        "category": "Business",
        "icon": "🧾",
        "desc": "Calculate Value Added Tax (VAT) additions or removals on retail invoice pricing.",
        "formula": "VAT = Base * Rate (Exclusive) | VAT = Price - [Price * (100 / (100 + Rate))] (Inclusive)",
        "formula_desc": "Extracts or adds VAT values based on the tax rate index.",
        "inputs": [
            {"id": "vat-price", "label": "Amount ($)", "type": "number", "default": "500", "min": "1", "max": "10000000", "step": "1"},
            {"id": "vat-rate", "label": "VAT Rate (%)", "type": "number", "default": "20", "min": "1", "max": "45", "step": "0.1"},
            {"id": "vat-type", "label": "Tax Options", "type": "select", "options": [("exclusive", "Exclusive (Add VAT)"), ("inclusive", "Inclusive (Remove VAT)")]}
        ],
        "outputs": [
            {"id": "out-vat-base", "label": "Net Base Amount", "prefix": "$", "suffix": ""},
            {"id": "out-vat-tax", "label": "VAT Amount", "prefix": "$", "suffix": ""},
            {"id": "out-vat-total", "label": "Total Gross Amount", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const price = parseFloat(document.getElementById('vat-price').value);
            const rate = parseFloat(document.getElementById('vat-rate').value);
            const type = document.getElementById('vat-type').value;

            if (isNaN(price) || isNaN(rate) || price <= 0 || rate <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            let base, tax, total;
            if (type === "exclusive") {
                tax = price * (rate / 100);
                base = price;
                total = price + tax;
            } else {
                base = price * (100 / (100 + rate));
                tax = price - base;
                total = price;
            }

            document.getElementById('out-vat-base').textContent = base.toFixed(2);
            document.getElementById('out-vat-tax').textContent = tax.toFixed(2);
            document.getElementById('out-vat-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p>Tax mode: VAT ${type}</p>
                <p>Net price: $${base.toFixed(2)} | VAT: $${tax.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Commission Calculator",
        "slug": "commission-calculator",
        "category": "Business",
        "icon": "💸",
        "desc": "Calculate total commission amounts and sales payout distributions.",
        "formula": "Commission = Sales Amount * (Commission Rate / 100)",
        "formula_desc": "Multiplies sales revenue by broker rate to isolate commission payouts.",
        "inputs": [
            {"id": "com-sales", "label": "Total Sales Amount ($)", "type": "number", "default": "12500", "min": "10", "max": "100000000", "step": "100"},
            {"id": "com-rate", "label": "Commission Rate (%)", "type": "number", "default": "5", "min": "0.1", "max": "90", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-com-amount", "label": "Commission Amount", "prefix": "$", "suffix": ""},
            {"id": "out-com-seller", "label": "Seller Takehome Payout", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const sales = parseFloat(document.getElementById('com-sales').value);
            const rate = parseFloat(document.getElementById('com-rate').value);

            if (isNaN(sales) || isNaN(rate) || sales <= 0 || rate <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const amount = sales * (rate / 100);
            const takehome = sales - amount;

            document.getElementById('out-com-amount').textContent = amount.toFixed(2);
            document.getElementById('out-com-seller').textContent = takehome.toFixed(2);

            updateBreakdown(`
                <p>Agent commission fee: $${amount.toFixed(2)} (${rate}%)</p>
            `);
        """
    },
    {
        "name": "Markup Calculator",
        "slug": "markup-calculator",
        "category": "Business",
        "icon": "💸",
        "desc": "Determine selling price, gross profit, and profit margin based on cost and markup rate.",
        "formula": "Selling Price = Cost * (1 + Markup / 100)",
        "formula_desc": "Applies a percentage markup factor to cost to establish retail sales prices.",
        "inputs": [
            {"id": "mar-cost", "label": "Cost price ($)", "type": "number", "default": "60", "min": "0.01", "max": "1000000", "step": "1"},
            {"id": "mar-rate", "label": "Markup Rate (%)", "type": "number", "default": "40", "min": "0", "max": "1000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-mar-price", "label": "Selling Price", "prefix": "$", "suffix": ""},
            {"id": "out-mar-profit", "label": "Gross Profit Margin", "prefix": "$", "suffix": ""},
            {"id": "out-mar-margin", "label": "Equivalent Profit Margin", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('mar-cost').value);
            const rate = parseFloat(document.getElementById('mar-rate').value) || 0;

            if (isNaN(cost) || cost <= 0) {
                showToast("Please enter cost price.", "error");
                return;
            }

            const price = cost * (1 + (rate / 100));
            const profit = price - cost;
            const margin = (profit / price) * 100;

            document.getElementById('out-mar-price').textContent = price.toFixed(2);
            document.getElementById('out-mar-profit').textContent = profit.toFixed(2);
            document.getElementById('out-mar-margin').textContent = margin.toFixed(2);

            updateBreakdown(`
                <p>Retail Price set to: $${price.toFixed(2)}</p>
                <p>Gross margin: ${margin.toFixed(2)}% on sales</p>
            `);
        """
    },
    {
        "name": "Inventory Turnover Calculator",
        "slug": "inventory-turnover-calculator",
        "category": "Business",
        "icon": "📦",
        "desc": "Calculate how many times inventory is sold and replaced over a business cycle.",
        "formula": "Turnover Ratio = Cost of Goods Sold (COGS) / Average Inventory",
        "formula_desc": "Measures stock liquidity by dividing operational product cost by inventory balances.",
        "inputs": [
            {"id": "it-cogs", "label": "Cost of Goods Sold (COGS) ($)", "type": "number", "default": "120000", "min": "1", "max": "1000000000", "step": "1000"},
            {"id": "it-avg", "label": "Average Inventory Value ($)", "type": "number", "default": "30000", "min": "1", "max": "100000000", "step": "1000"}
        ],
        "outputs": [
            {"id": "out-it-ratio", "label": "Turnover Ratio", "prefix": "", "suffix": " times/yr"},
            {"id": "out-it-days", "label": "Average Days to Sell Stock", "prefix": "", "suffix": " days"}
        ],
        "calc_js": """
            const cogs = parseFloat(document.getElementById('it-cogs').value);
            const avg = parseFloat(document.getElementById('it-avg').value);

            if (isNaN(cogs) || isNaN(avg) || cogs <= 0 || avg <= 0) {
                showToast("Please check inventory inputs.", "error");
                return;
            }

            const ratio = cogs / avg;
            const days = 365 / ratio;

            document.getElementById('out-it-ratio').textContent = ratio.toFixed(2);
            document.getElementById('out-it-days').textContent = Math.round(days);

            updateBreakdown(`
                <p>Inventory turnover: <strong>${ratio.toFixed(2)} times</strong> per year.</p>
                <p>Takes approximately <strong>${Math.round(days)} days</strong> to clear inventory.</p>
            `);
        """
    },
    {
        "name": "Cash Flow Calculator",
        "slug": "cash-flow-calculator",
        "category": "Business",
        "icon": "📊",
        "desc": "Calculate net operational cash flow balances by auditing inflows and outflows.",
        "formula": "Net Cash Flow = Total Inflows - Total Outflows",
        "formula_desc": "Subtracts gross operational expenses from incoming revenues.",
        "inputs": [
            {"id": "cf-in", "label": "Total Cash Inflows ($)", "type": "number", "default": "45000", "min": "0", "max": "1000000000", "step": "100"},
            {"id": "cf-out", "label": "Total Cash Outflows ($)", "type": "number", "default": "32000", "min": "0", "max": "1000000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-cf-net", "label": "Net Cash Flow", "prefix": "$", "suffix": ""},
            {"id": "out-cf-status", "label": "Cash Flow Status", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const cashIn = parseFloat(document.getElementById('cf-in').value) || 0;
            const cashOut = parseFloat(document.getElementById('cf-out').value) || 0;

            const net = cashIn - cashOut;
            document.getElementById('out-cf-net').textContent = net.toFixed(2);

            let status = "Balanced";
            if (net > 0) {
                status = "Positive Cash Flow (Surplus)";
            } else if (net < 0) {
                status = "Negative Cash Flow (Deficit)";
            }
            
            document.getElementById('out-cf-status').textContent = status;
            updateBreakdown(`<p>Operating surplus/deficit: $${net.toFixed(2)}</p>`);
        """
    },
    {
        "name": "Payback Period Calculator",
        "slug": "payback-period-calculator",
        "category": "Business",
        "icon": "⏳",
        "desc": "Determine how many years it will take to recover the cost of a capital investment.",
        "formula": "Payback Period = Initial Investment / Annual Cash Flow",
        "formula_desc": "Divides initial purchase assets by anticipated regular annual revenue flows.",
        "inputs": [
            {"id": "pp-invest", "label": "Initial Capital Outlay ($)", "type": "number", "default": "50000", "min": "100", "max": "1000000000", "step": "1000"},
            {"id": "pp-flow", "label": "Expected Annual Cash Flow ($)", "type": "number", "default": "12500", "min": "1", "max": "100000000", "step": "500"}
        ],
        "outputs": [
            {"id": "out-pp-years", "label": "Payback Period", "prefix": "", "suffix": " Years"},
            {"id": "out-pp-roi", "label": "Annual Cash Yield Rate", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const invest = parseFloat(document.getElementById('pp-invest').value);
            const flow = parseFloat(document.getElementById('pp-flow').value);

            if (isNaN(invest) || isNaN(flow) || invest <= 0 || flow <= 0) {
                showToast("Please check investment input fields.", "error");
                return;
            }

            const years = invest / flow;
            const yieldRate = (flow / invest) * 100;

            document.getElementById('out-pp-years').textContent = years.toFixed(2);
            document.getElementById('out-pp-roi').textContent = yieldRate.toFixed(2);

            updateBreakdown(`
                <p>Estimated capital payback achieved in <strong>${years.toFixed(2)} years</strong>.</p>
            `);
        """
    },
    {
        "name": "Depreciation Calculator",
        "slug": "depreciation-calculator",
        "category": "Business",
        "icon": "⏳",
        "desc": "Calculate annual straight-line asset depreciation value and salvage balance.",
        "formula": "Annual Depreciation = (Cost - Salvage Value) / Useful Life (Years)",
        "formula_desc": "Calculates write-offs over the useful life of an asset.",
        "inputs": [
            {"id": "dep-cost", "label": "Initial Asset Cost ($)", "type": "number", "default": "20000", "min": "100", "max": "100000000", "step": "100"},
            {"id": "dep-salvage", "label": "Salvage Value ($)", "type": "number", "default": "4000", "min": "0", "max": "100000000", "step": "100"},
            {"id": "dep-life", "label": "Useful Life (Years)", "type": "number", "default": "5", "min": "1", "max": "50", "step": "1"}
        ],
        "outputs": [
            {"id": "out-dep-annual", "label": "Annual Depreciation Expense", "prefix": "$", "suffix": ""},
            {"id": "out-dep-monthly", "label": "Monthly Written-off Value", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('dep-cost').value);
            const salvage = parseFloat(document.getElementById('dep-salvage').value) || 0;
            const life = parseFloat(document.getElementById('dep-life').value);

            if (isNaN(cost) || isNaN(life) || cost <= 0 || life <= 0 || cost < salvage) {
                showToast("Cost must exceed salvage value.", "error");
                return;
            }

            const annual = (cost - salvage) / life;
            const monthly = annual / 12;

            document.getElementById('out-dep-annual').textContent = annual.toFixed(2);
            document.getElementById('out-dep-monthly').textContent = monthly.toFixed(2);

            updateBreakdown(`
                <p>Asset depreciable basis: $${(cost - salvage).toFixed(2)}</p>
                <p>Total write-off rate: $${annual.toFixed(2)} per year.</p>
            `);
        """
    },
    {
        "name": "Business Loan Calculator",
        "slug": "business-loan-calculator",
        "category": "Business",
        "icon": "🏦",
        "desc": "Calculate monthly EMI and total interest for commercial loans.",
        "formula": "EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]",
        "formula_desc": "Applies interest compound amortizations to calculate monthly installment amounts.",
        "inputs": [
            {"id": "bl-principal", "label": "Loan Amount ($)", "type": "number", "default": "50000", "min": "1000", "max": "100000000", "step": "1000"},
            {"id": "bl-rate", "label": "Annual Interest Rate (%)", "type": "number", "default": "7.5", "min": "0.1", "max": "35", "step": "0.1"},
            {"id": "bl-term", "label": "Tenure (Months)", "type": "number", "default": "36", "min": "3", "max": "120", "step": "3"}
        ],
        "outputs": [
            {"id": "out-bl-emi", "label": "Monthly EMI", "prefix": "$", "suffix": ""},
            {"id": "out-bl-interest", "label": "Total Interest Payable", "prefix": "$", "suffix": ""},
            {"id": "out-bl-total", "label": "Total Payment (P + I)", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('bl-principal').value);
            const r = parseFloat(document.getElementById('bl-rate').value);
            const n = parseFloat(document.getElementById('bl-term').value);

            if (isNaN(p) || isNaN(r) || isNaN(n) || p <= 0 || r <= 0 || n <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const monthlyRate = (r / 100) / 12;
            const emi = p * (monthlyRate * Math.pow(1 + monthlyRate, n)) / (Math.pow(1 + monthlyRate, n) - 1);
            const total = emi * n;
            const interest = total - p;

            document.getElementById('out-bl-emi').textContent = emi.toFixed(2);
            document.getElementById('out-bl-interest').textContent = interest.toFixed(2);
            document.getElementById('out-bl-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p>Monthly payment target: $${emi.toFixed(2)}</p>
                <p>Commercial loan interest: $${interest.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Revenue Growth Calculator",
        "slug": "revenue-growth-calculator",
        "category": "Business",
        "icon": "📈",
        "desc": "Calculate your business year-over-year or month-over-month revenue growth rate.",
        "formula": "Growth Rate (%) = ((Current Revenue - Previous Revenue) / Previous Revenue) * 100",
        "formula_desc": "Solves percentage difference between two calendar revenue metrics.",
        "inputs": [
            {"id": "rg-prev", "label": "Previous Period Revenue ($)", "type": "number", "default": "80000", "min": "1", "max": "1000000000", "step": "1000"},
            {"id": "rg-curr", "label": "Current Period Revenue ($)", "type": "number", "default": "96000", "min": "1", "max": "1000000000", "step": "1000"}
        ],
        "outputs": [
            {"id": "out-rg-rate", "label": "Growth Rate", "prefix": "", "suffix": "%"},
            {"id": "out-rg-diff", "label": "Revenue Increase", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const prev = parseFloat(document.getElementById('rg-prev').value);
            const curr = parseFloat(document.getElementById('rg-curr').value);

            if (isNaN(prev) || isNaN(curr) || prev <= 0 || curr < 0) {
                showToast("Previous revenue must be greater than zero.", "error");
                return;
            }

            const diff = curr - prev;
            const rate = (diff / prev) * 100;

            document.getElementById('out-rg-rate').textContent = rate.toFixed(2);
            document.getElementById('out-rg-diff').textContent = diff.toFixed(2);

            updateBreakdown(`
                <p>Net earnings increase: $${diff.toFixed(2)} (${rate.toFixed(2)}% growth)</p>
            `);
        """
    }
]

CONST_CALCS = [
    {
        "name": "Concrete Calculator",
        "slug": "concrete-calculator",
        "category": "Construction",
        "icon": "🧱",
        "desc": "Calculate the concrete volume and bag count required for slabs, columns, and foundations.",
        "formula": "Volume = Length * Width * Depth",
        "formula_desc": "Multiplies dimension variables to isolate total solid volume, converting to concrete bag counts.",
        "inputs": [
            {"id": "con-length", "label": "Length (meters)", "type": "number", "default": "5.0", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "con-width", "label": "Width (meters)", "type": "number", "default": "4.0", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "con-depth", "label": "Depth/Thickness (meters)", "type": "number", "default": "0.1", "min": "0.01", "max": "10", "step": "0.01"},
            {"id": "con-bagsize", "label": "Concrete Bag Size", "type": "select", "options": [("40", "40 kg (approx 0.02 m³)"), ("20", "20 kg (approx 0.01 m³)")]}
        ],
        "outputs": [
            {"id": "out-con-vol", "label": "Required Volume", "prefix": "", "suffix": " m³"},
            {"id": "out-con-bags", "label": "Estimated Bags Count", "prefix": "", "suffix": " bags"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('con-length').value);
            const w = parseFloat(document.getElementById('con-width').value);
            const d = parseFloat(document.getElementById('con-depth').value);
            const bag = parseFloat(document.getElementById('con-bagsize').value);

            if (isNaN(l) || isNaN(w) || isNaN(d) || l <= 0 || w <= 0 || d <= 0) {
                showToast("Please check input dimensions.", "error");
                return;
            }

            const vol = l * w * d;
            
            // 40kg concrete yields roughly 0.02 cubic meters of wet volume
            // 20kg yields 0.01 cubic meters
            const yieldVol = (bag === 40) ? 0.02 : 0.01;
            const bagsCount = vol / yieldVol;

            document.getElementById('out-con-vol').textContent = vol.toFixed(3);
            document.getElementById('out-con-bags').textContent = Math.ceil(bagsCount);

            updateBreakdown(`
                <p>Volume calculation: ${l}m x ${w}m x ${d}m = <strong>${vol.toFixed(3)} cubic meters</strong>.</p>
                <p>Assumed bag size: ${bag} kg.</p>
            `);
        """
    },
    {
        "name": "Paint Calculator",
        "slug": "paint-calculator",
        "category": "Construction",
        "icon": "🎨",
        "desc": "Calculate paint volume required based on wall surface area and number of coats.",
        "formula": "Paint Volume (Liters) = (Wall Area / Coverage) * Coats",
        "formula_desc": "Divides wall area by standard coverage rates (e.g. 10m² per liter) multiplied by coating passes.",
        "inputs": [
            {"id": "pnt-area", "label": "Total Wall Area (sq meters)", "type": "number", "default": "45", "min": "1", "max": "5000", "step": "1"},
            {"id": "pnt-coats", "label": "Number of Coats", "type": "number", "default": "2", "min": "1", "max": "5", "step": "1"},
            {"id": "pnt-coverage", "label": "Paint Coverage Rate (m²/L)", "type": "number", "default": "10", "min": "5", "max": "20", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-pnt-liters", "label": "Required Paint", "prefix": "", "suffix": " Liters"},
            {"id": "out-pnt-gallons", "label": "Required Paint (US Gallons)", "prefix": "", "suffix": " Gallons"}
        ],
        "calc_js": """
            const area = parseFloat(document.getElementById('pnt-area').value);
            const coats = parseFloat(document.getElementById('pnt-coats').value);
            const coverage = parseFloat(document.getElementById('pnt-coverage').value);

            if (isNaN(area) || isNaN(coats) || isNaN(coverage) || area <= 0 || coats <= 0 || coverage <= 0) {
                showToast("Please check numeric fields.", "error");
                return;
            }

            const liters = (area / coverage) * coats;
            const gallons = liters * 0.264172;

            document.getElementById('out-pnt-liters').textContent = liters.toFixed(1);
            document.getElementById('out-pnt-gallons').textContent = gallons.toFixed(2);

            updateBreakdown(`
                <p>Surface to cover: ${area} m² x ${coats} coats = <strong>${area*coats} m² total</strong>.</p>
            `);
        """
    },
    {
        "name": "Tile Calculator",
        "slug": "tile-calculator",
        "category": "Construction",
        "icon": "🧱",
        "desc": "Calculate total tile units and packaging boxes needed for flooring or wall surface layouts.",
        "formula": "Tiles Needed = Room Area / Tile Area * (1 + Waste %)",
        "formula_desc": "Divides floor area by individual tile size, factoring in a wastage margin (usually 10%).",
        "inputs": [
            {"id": "tile-rl", "label": "Room Length (meters)", "type": "number", "default": "5.0", "min": "0.5", "max": "200", "step": "0.1"},
            {"id": "tile-rw", "label": "Room Width (meters)", "type": "number", "default": "4.0", "min": "0.5", "max": "200", "step": "0.1"},
            {"id": "tile-ts", "label": "Individual Tile Size", "type": "select", "options": [
                ("0.09", "30x30 cm (0.09 m²)"),
                ("0.36", "60x60 cm (0.36 m²)"),
                ("0.18", "30x60 cm (0.18 m³)")
            ]},
            {"id": "tile-waste", "label": "Waste Margin (%)", "type": "number", "default": "10", "min": "0", "max": "30", "step": "1"}
        ],
        "outputs": [
            {"id": "out-tile-count", "label": "Tiles Required", "prefix": "", "suffix": " tiles"},
            {"id": "out-tile-area", "label": "Flooring Area", "prefix": "", "suffix": " m²"}
        ],
        "calc_js": """
            const rl = parseFloat(document.getElementById('tile-rl').value);
            const rw = parseFloat(document.getElementById('tile-rw').value);
            const tArea = parseFloat(document.getElementById('tile-ts').value);
            const waste = parseFloat(document.getElementById('tile-waste').value) || 0;

            if (isNaN(rl) || isNaN(rw) || rl <= 0 || rw <= 0) {
                showToast("Please check room dimensions.", "error");
                return;
            }

            const area = rl * rw;
            const baseTiles = area / tArea;
            const totalTiles = baseTiles * (1 + (waste / 100));

            document.getElementById('out-tile-count').textContent = Math.ceil(totalTiles);
            document.getElementById('out-tile-area').textContent = area.toFixed(2);

            updateBreakdown(`
                <p>Base floor surface: ${area.toFixed(2)} m².</p>
                <p>Estimated wastage overhead: +${waste}%.</p>
            `);
        """
    },
    {
        "name": "Brick Calculator",
        "slug": "brick-calculator",
        "category": "Construction",
        "icon": "🧱",
        "desc": "Calculate the brick count required for walls based on dimensions and brick sizes.",
        "formula": "Bricks Required = Wall Area / Brick Area (including mortar joints)",
        "formula_desc": "Solves for brick volume layouts against wall surface areas factoring in mortar lines (typically 10mm).",
        "inputs": [
            {"id": "brk-wl", "label": "Wall Length (meters)", "type": "number", "default": "6.0", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "brk-wh", "label": "Wall Height (meters)", "type": "number", "default": "2.4", "min": "0.1", "max": "100", "step": "0.1"},
            {"id": "brk-type", "label": "Brick Size (Standard)", "type": "select", "options": [
                ("0.0215", "Standard UK (215 x 102.5 x 65 mm)"),
                ("0.019", "US Modular (194 x 92 x 57 mm)")
            ]},
            {"id": "brk-waste", "label": "Waste Margin (%)", "type": "number", "default": "5", "min": "0", "max": "20", "step": "1"}
        ],
        "outputs": [
            {"id": "out-brk-count", "label": "Bricks Required", "prefix": "", "suffix": " bricks"},
            {"id": "out-brk-area", "label": "Wall Surface Area", "prefix": "", "suffix": " m²"}
        ],
        "calc_js": """
            const wl = parseFloat(document.getElementById('brk-wl').value);
            const wh = parseFloat(document.getElementById('brk-wh').value);
            const bArea = parseFloat(document.getElementById('brk-type').value);
            const waste = parseFloat(document.getElementById('brk-waste').value) || 0;

            if (isNaN(wl) || isNaN(wh) || wl <= 0 || wh <= 0) {
                showToast("Please check wall input dimensions.", "error");
                return;
            }

            const area = wl * wh;
            
            // Factor in 10mm mortar joints
            // Standard uk size face area is 0.215 x 0.065 = 0.013975 m2
            // With 10mm joint: 0.225 x 0.075 = 0.016875 m2
            // For simplicity, we adjust the input area values by adding ~15% for joints in calculation
            const jointAdjustment = 1.20;
            const bricksNeeded = (area / (bArea * jointAdjustment)) * (1 + (waste / 100));

            document.getElementById('out-brk-count').textContent = Math.ceil(bricksNeeded);
            document.getElementById('out-brk-area').textContent = area.toFixed(2);

            updateBreakdown(`
                <p>Wall area: <strong>${area.toFixed(2)} m²</strong>.</p>
            `);
        """
    },
    {
        "name": "Flooring Calculator",
        "slug": "flooring-calculator",
        "category": "Construction",
        "icon": "🪵",
        "desc": "Calculate required floor materials (laminate, hardwood, vinyl) and total purchase costs.",
        "formula": "Flooring Area = Length * Width | Total Cost = Area * Cost per Unit",
        "formula_desc": "Multiplies dimension variables, adds a waste factor (10%), and multiplies by material prices.",
        "inputs": [
            {"id": "fl-length", "label": "Room Length (meters)", "type": "number", "default": "4.5", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "fl-width", "label": "Room Width (meters)", "type": "number", "default": "3.5", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "fl-price", "label": "Material Cost ($/m²)", "type": "number", "default": "25.00", "min": "0.1", "max": "1000", "step": "0.5"},
            {"id": "fl-waste", "label": "Waste Margin (%)", "type": "number", "default": "10", "min": "0", "max": "30", "step": "1"}
        ],
        "outputs": [
            {"id": "out-fl-area", "label": "Flooring Area (with waste)", "prefix": "", "suffix": " m²"},
            {"id": "out-fl-cost", "label": "Total Material Cost", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('fl-length').value);
            const w = parseFloat(document.getElementById('fl-width').value);
            const p = parseFloat(document.getElementById('fl-price').value);
            const waste = parseFloat(document.getElementById('fl-waste').value) || 0;

            if (isNaN(l) || isNaN(w) || isNaN(p) || l <= 0 || w <= 0 || p <= 0) {
                showToast("Please check floor inputs.", "error");
                return;
            }

            const baseArea = l * w;
            const areaWithWaste = baseArea * (1 + (waste / 100));
            const cost = areaWithWaste * p;

            document.getElementById('out-fl-area').textContent = areaWithWaste.toFixed(2);
            document.getElementById('out-fl-cost').textContent = cost.toFixed(2);

            updateBreakdown(`
                <p>Base floor surface: ${baseArea.toFixed(2)} m².</p>
                <p>Material cost basis: $${p.toFixed(2)} /m²</p>
            `);
        """
    },
    {
        "name": "Roofing Calculator",
        "slug": "roofing-calculator",
        "category": "Construction",
        "icon": "🏠",
        "desc": "Calculate roof area and total shingles bundles needed based on roof dimensions and pitch.",
        "formula": "Roof Area = Flat Area * Pitch Factor",
        "formula_desc": "Multiplies flat roof dimensions by the pitch factor to determine overall sloped surface area.",
        "inputs": [
            {"id": "rf-length", "label": "House Length (meters)", "type": "number", "default": "12.0", "min": "1", "max": "500", "step": "0.1"},
            {"id": "rf-width", "label": "House Width (meters)", "type": "number", "default": "8.0", "min": "1", "max": "500", "step": "0.1"},
            {"id": "rf-pitch", "label": "Roof Pitch (rise/12)", "type": "select", "options": [
                ("1.0", "Flat / Low (0-2/12)"),
                ("1.08", "Medium Pitch (4/12)"),
                ("1.20", "Standard Pitch (8/12)"),
                ("1.41", "Steep Pitch (12/12)")
            ]}
        ],
        "outputs": [
            {"id": "out-rf-area", "label": "Sloped Roof Area", "prefix": "", "suffix": " m²"},
            {"id": "out-rf-bundles", "label": "Shingles Bundles Needed", "prefix": "", "suffix": " bundles"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('rf-length').value);
            const w = parseFloat(document.getElementById('rf-width').value);
            const factor = parseFloat(document.getElementById('rf-pitch').value);

            if (isNaN(l) || isNaN(w) || l <= 0 || w <= 0) {
                showToast("Please check dimension values.", "error");
                return;
            }

            // Flat area with 0.3m overhang (eaves) extension on all sides
            const flatArea = (l + 0.6) * (w + 0.6);
            const slopedArea = flatArea * factor;
            
            // Standard bundle of shingles covers approx 3.1 m² (33.3 sq ft)
            const bundles = slopedArea / 3.1;

            document.getElementById('out-rf-area').textContent = slopedArea.toFixed(1);
            document.getElementById('out-rf-bundles').textContent = Math.ceil(bundles);

            updateBreakdown(`
                <p>Total flat base (including overhangs): ${flatArea.toFixed(1)} m².</p>
                <p>Pitch multiplier applied: x${factor}</p>
            `);
        """
    },
    {
        "name": "Asphalt Calculator",
        "slug": "asphalt-calculator",
        "category": "Construction",
        "icon": "🛣️",
        "desc": "Calculate the volume and weight of asphalt required for paving driveways or roads.",
        "formula": "Tons of Asphalt = Volume * Density (approx 2.4 tons per m³)",
        "formula_desc": "Multiplies paving volume by the empirical density factor of hot-mix asphalt (approx 2,400 kg/m³).",
        "inputs": [
            {"id": "asp-length", "label": "Paving Length (meters)", "type": "number", "default": "15.0", "min": "0.1", "max": "10000", "step": "0.1"},
            {"id": "asp-width", "label": "Paving Width (meters)", "type": "number", "default": "3.0", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "asp-depth", "label": "Thickness (cm)", "type": "number", "default": "5.0", "min": "1.0", "max": "50", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-asp-vol", "label": "Required Volume", "prefix": "", "suffix": " m³"},
            {"id": "out-asp-tons", "label": "Weight Required (Tons)", "prefix": "", "suffix": " tons"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('asp-length').value);
            const w = parseFloat(document.getElementById('asp-width').value);
            const d = parseFloat(document.getElementById('asp-depth').value) / 100; // cm to m

            if (isNaN(l) || isNaN(w) || isNaN(d) || l <= 0 || w <= 0 || d <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const vol = l * w * d;
            // Hot mix asphalt density is approximately 2.4 metric tons per cubic meter
            const tons = vol * 2.4;

            document.getElementById('out-asp-vol').textContent = vol.toFixed(2);
            document.getElementById('out-asp-tons').textContent = tons.toFixed(2);

            updateBreakdown(`
                <p>Volume: ${l}m x ${w}m x ${(d*100).toFixed(1)}cm = ${vol.toFixed(2)} m³</p>
                <p>Density multiplier: 2.4 tons per m³</p>
            `);
        """
    },
    {
        "name": "Sand Calculator",
        "slug": "sand-calculator",
        "category": "Construction",
        "icon": "⏳",
        "desc": "Calculate total volume and weight of sand required for landscaping or concrete mixes.",
        "formula": "Weight of Sand = Volume * Density (approx 1.6 tons per m³)",
        "formula_desc": "Projects sand requirements using the average bulk density of dry sand (approx 1.6 tons/m³).",
        "inputs": [
            {"id": "snd-length", "label": "Length (meters)", "type": "number", "default": "4.0", "min": "0.1", "max": "1000", "step": "0.1"},
            {"id": "snd-width", "label": "Width (meters)", "type": "number", "default": "3.0", "min": "0.1", "max": "500", "step": "0.1"},
            {"id": "snd-depth", "label": "Depth (cm)", "type": "number", "default": "10.0", "min": "0.5", "max": "200", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-snd-vol", "label": "Required Volume", "prefix": "", "suffix": " m³"},
            {"id": "out-snd-tons", "label": "Weight Required", "prefix": "", "suffix": " tons"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('snd-length').value);
            const w = parseFloat(document.getElementById('snd-width').value);
            const d = parseFloat(document.getElementById('snd-depth').value) / 100; // cm to m

            if (isNaN(l) || isNaN(w) || isNaN(d) || l <= 0 || w <= 0 || d <= 0) {
                showToast("Please check sand dimensions.", "error");
                return;
            }

            const vol = l * w * d;
            // Dry bulk sand is approximately 1.6 tons per m³
            const tons = vol * 1.6;

            document.getElementById('out-snd-vol').textContent = vol.toFixed(3);
            document.getElementById('out-snd-tons').textContent = tons.toFixed(2);

            updateBreakdown(`
                <p>Volume: ${vol.toFixed(3)} m³ | Weight basis: 1.6 metric tons/m³</p>
            `);
        """
    },
    {
        "name": "Cement Calculator",
        "slug": "cement-calculator",
        "category": "Construction",
        "icon": "🧱",
        "desc": "Calculate standard cement bags, sand, and gravel quantities for specific concrete volumes.",
        "formula": "Ratio: 1 Part Cement, 2 Parts Sand, 4 Parts Gravel (standard mix)",
        "formula_desc": "Applies standard concrete mixing volumes (e.g. 1:2:4 ratio) to determine weight balances.",
        "inputs": [
            {"id": "cem-vol", "label": "Concrete Volume (cubic meters)", "type": "number", "default": "2.0", "min": "0.1", "max": "1000", "step": "0.1"},
            {"id": "cem-ratio", "label": "Concrete Mix Proportion", "type": "select", "options": [
                ("1:2:4", "M15 grade - 1:2:4 (General construction)"),
                ("1:1.5:3", "M20 grade - 1:1.5:3 (Reinforced concrete)"),
                ("1:3:6", "M10 grade - 1:3:6 (Foundations)")
            ]}
        ],
        "outputs": [
            {"id": "out-cem-bags", "label": "Cement Bags (50kg)", "prefix": "", "suffix": " bags"},
            {"id": "out-cem-sand", "label": "Sand Required", "prefix": "", "suffix": " tons"},
            {"id": "out-cem-gravel", "label": "Gravel Required", "prefix": "", "suffix": " tons"}
        ],
        "calc_js": """
            const vol = parseFloat(document.getElementById('cem-vol').value);
            const ratio = document.getElementById('cem-ratio').value;

            if (isNaN(vol) || vol <= 0) {
                showToast("Please check concrete volume.", "error");
                return;
            }

            // Dry volume of concrete is assumed to be 1.54 times the wet volume due to shrinkage/waste
            const dryVol = vol * 1.54;

            let cParts, sParts, gParts;
            if (ratio === "1:2:4") {
                cParts = 1; sParts = 2; gParts = 4;
            } else if (ratio === "1:1.5:3") {
                cParts = 1; sParts = 1.5; gParts = 3;
            } else {
                cParts = 1; sParts = 3; gParts = 6;
            }

            const totalParts = cParts + sParts + gParts;
            
            const cementVol = (cParts / totalParts) * dryVol;
            const sandVol = (sParts / totalParts) * dryVol;
            const gravelVol = (gParts / totalParts) * dryVol;

            // Density: Cement = 1440 kg/m3, 50kg bag = 0.0347 m3
            const bags = cementVol / 0.0347;
            
            // Weight: Sand = 1.6 tons/m3, Gravel = 1.6 tons/m3
            const sandTons = sandVol * 1.6;
            const gravelTons = gravelVol * 1.6;

            document.getElementById('out-cem-bags').textContent = Math.ceil(bags);
            document.getElementById('out-cem-sand').textContent = sandTons.toFixed(2);
            document.getElementById('out-cem-gravel').textContent = gravelTons.toFixed(2);

            updateBreakdown(`
                <p>Wet Concrete: ${vol} m³ | Dry Mix Requirement: ${dryVol.toFixed(2)} m³</p>
            `);
        """
    },
    {
        "name": "Land Area Calculator",
        "slug": "land-area-calculator",
        "category": "Construction",
        "icon": "🗺️",
        "desc": "Calculate land area in square meters, square feet, acres, and hectares.",
        "formula": "Area = Length * Width",
        "formula_desc": "Multiplies plot dimensions, converting output to multiple land measurement indexes.",
        "inputs": [
            {"id": "la-length", "label": "Plot Length (meters)", "type": "number", "default": "30.0", "min": "1", "max": "50000", "step": "1"},
            {"id": "la-width", "label": "Plot Width (meters)", "type": "number", "default": "20.0", "min": "1", "max": "50000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-la-sqm", "label": "Area (Sq Meters)", "prefix": "", "suffix": " m²"},
            {"id": "out-la-sqft", "label": "Area (Sq Feet)", "prefix": "", "suffix": " sq ft"},
            {"id": "out-la-acres", "label": "Area (Acres)", "prefix": "", "suffix": " acres"},
            {"id": "out-la-hectares", "label": "Area (Hectares)", "prefix": "", "suffix": " ha"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('la-length').value);
            const w = parseFloat(document.getElementById('la-width').value);

            if (isNaN(l) || isNaN(w) || l <= 0 || w <= 0) {
                showToast("Please check dimension values.", "error");
                return;
            }

            const sqm = l * w;
            const sqft = sqm * 10.7639;
            const acres = sqm * 0.000247105;
            const hectares = sqm * 0.0001;

            document.getElementById('out-la-sqm').textContent = sqm.toFixed(2);
            document.getElementById('out-la-sqft').textContent = sqft.toFixed(2);
            document.getElementById('out-la-acres').textContent = acres.toFixed(4);
            document.getElementById('out-la-hectares').textContent = hectares.toFixed(4);

            updateBreakdown(`
                <p>Plot dimension: ${l}m x ${w}m = <strong>${sqm.toFixed(2)} square meters</strong>.</p>
            `);
        """
    }
]
