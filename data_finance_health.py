# -*- coding: utf-8 -*-
"""
Finance and Health & Fitness Calculators Data
"""

FINANCE_CALCS = [
    {
        "name": "SIP Calculator",
        "slug": "sip-calculator",
        "category": "Finance",
        "icon": "📈",
        "desc": "Estimate your mutual fund investment returns and wealth growth via Systematic Investment Plans.",
        "formula": "M = P * [((1 + i)^n - 1) / i] * (1 + i)",
        "formula_desc": "Calculates the future value of a series of monthly investments (SIP) compounded regularly.",
        "inputs": [
            {"id": "sip-p", "label": "Monthly Investment ($)", "type": "number", "default": "100", "min": "1", "max": "1000000", "step": "10"},
            {"id": "sip-r", "label": "Expected Return Rate (% p.a.)", "type": "number", "default": "12", "min": "1", "max": "50", "step": "0.1"},
            {"id": "sip-t", "label": "Time Period (Years)", "type": "number", "default": "10", "min": "1", "max": "40", "step": "1"}
        ],
        "outputs": [
            {"id": "out-sip-invested", "label": "Invested Amount", "prefix": "$", "suffix": ""},
            {"id": "out-sip-returns", "label": "Estimated Returns", "prefix": "$", "suffix": ""},
            {"id": "out-sip-total", "label": "Total Value", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('sip-p').value);
            const r = parseFloat(document.getElementById('sip-r').value);
            const t = parseFloat(document.getElementById('sip-t').value);
            if (isNaN(p) || isNaN(r) || isNaN(t) || p <= 0 || r <= 0 || t <= 0) {
                showToast("Please enter valid positive numbers.", "error");
                return;
            }
            const i = (r / 100) / 12;
            const n = t * 12;
            const total = p * ((Math.pow(1 + i, n) - 1) / i) * (1 + i);
            const invested = p * n;
            const returns = total - invested;

            document.getElementById('out-sip-invested').textContent = invested.toFixed(2);
            document.getElementById('out-sip-returns').textContent = returns.toFixed(2);
            document.getElementById('out-sip-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Monthly savings (P):</strong> $${p.toFixed(2)}</p>
                <p><strong>Total months (n):</strong> ${n}</p>
                <p><strong>Monthly rate (i):</strong> ${(i*100).toFixed(4)}%</p>
                <p><strong>Compound maturity:</strong> $${total.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Mutual Fund Returns Calculator",
        "slug": "mutual-fund-returns-calculator",
        "category": "Finance",
        "icon": "📊",
        "desc": "Calculate compound returns and maturity value for mutual fund lumpsum investments.",
        "formula": "A = P * (1 + r)^t",
        "formula_desc": "Calculates the future value of a lumpsum investment compounding annually.",
        "inputs": [
            {"id": "mf-p", "label": "Lumpsum Investment ($)", "type": "number", "default": "5000", "min": "1", "max": "10000000", "step": "100"},
            {"id": "mf-r", "label": "Expected Return Rate (% p.a.)", "type": "number", "default": "12", "min": "1", "max": "50", "step": "0.1"},
            {"id": "mf-t", "label": "Time Period (Years)", "type": "number", "default": "10", "min": "1", "max": "40", "step": "1"}
        ],
        "outputs": [
            {"id": "out-mf-invested", "label": "Invested Amount", "prefix": "$", "suffix": ""},
            {"id": "out-mf-returns", "label": "Estimated Returns", "prefix": "$", "suffix": ""},
            {"id": "out-mf-total", "label": "Total Value", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('mf-p').value);
            const r = parseFloat(document.getElementById('mf-r').value);
            const t = parseFloat(document.getElementById('mf-t').value);
            if (isNaN(p) || isNaN(r) || isNaN(t) || p <= 0 || r <= 0 || t <= 0) {
                showToast("Please enter valid positive numbers.", "error");
                return;
            }
            const total = p * Math.pow(1 + (r / 100), t);
            const returns = total - p;

            document.getElementById('out-mf-invested').textContent = p.toFixed(2);
            document.getElementById('out-mf-returns').textContent = returns.toFixed(2);
            document.getElementById('out-mf-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Principal (P):</strong> $${p.toFixed(2)}</p>
                <p><strong>Compounding rate:</strong> ${r}% per year</p>
                <p><strong>Duration:</strong> ${t} years</p>
                <p><strong>Total wealth generated:</strong> $${total.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Stock Profit Calculator",
        "slug": "stock-profit-calculator",
        "category": "Finance",
        "icon": "📈",
        "desc": "Calculate your net profit, ROI, and total commissions for buying and selling stocks.",
        "formula": "Net Profit = (Sell Price * Shares) - (Buy Price * Shares) - Buy Commission - Sell Commission",
        "formula_desc": "Subtracts buy costs and sell commissions from the total sale revenue to find stock returns.",
        "inputs": [
            {"id": "st-buy", "label": "Buy Price per Share ($)", "type": "number", "default": "50", "min": "0.01", "max": "1000000", "step": "0.1"},
            {"id": "st-sell", "label": "Sell Price per Share ($)", "type": "number", "default": "65", "min": "0.01", "max": "1000000", "step": "0.1"},
            {"id": "st-shares", "label": "Number of Shares", "type": "number", "default": "100", "min": "1", "max": "10000000", "step": "1"},
            {"id": "st-buy-comm", "label": "Buy Commission ($)", "type": "number", "default": "5", "min": "0", "max": "5000", "step": "1"},
            {"id": "st-sell-comm", "label": "Sell Commission ($)", "type": "number", "default": "5", "min": "0", "max": "5000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-st-cost", "label": "Total Buying Cost", "prefix": "$", "suffix": ""},
            {"id": "out-st-rev", "label": "Total Selling Revenue", "prefix": "$", "suffix": ""},
            {"id": "out-st-profit", "label": "Net Profit", "prefix": "$", "suffix": ""},
            {"id": "out-st-roi", "label": "Return on Investment (ROI)", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const buy = parseFloat(document.getElementById('st-buy').value);
            const sell = parseFloat(document.getElementById('st-sell').value);
            const shares = parseFloat(document.getElementById('st-shares').value);
            const buyComm = parseFloat(document.getElementById('st-buy-comm').value) || 0;
            const sellComm = parseFloat(document.getElementById('st-sell-comm').value) || 0;

            if (isNaN(buy) || isNaN(sell) || isNaN(shares) || buy <= 0 || sell <= 0 || shares <= 0) {
                showToast("Please check share price inputs.", "error");
                return;
            }

            const cost = (buy * shares) + buyComm;
            const revenue = (sell * shares) - sellComm;
            const profit = revenue - cost;
            const roi = (profit / cost) * 100;

            document.getElementById('out-st-cost').textContent = cost.toFixed(2);
            document.getElementById('out-st-rev').textContent = revenue.toFixed(2);
            document.getElementById('out-st-profit').textContent = profit.toFixed(2);
            document.getElementById('out-st-roi').textContent = roi.toFixed(2);

            updateBreakdown(`
                <p><strong>Shares:</strong> ${shares} | <strong>Total commissions:</strong> $${(buyComm+sellComm).toFixed(2)}</p>
                <p><strong>Net investment:</strong> $${cost.toFixed(2)}</p>
                <p><strong>Net returns:</strong> $${profit.toFixed(2)} (${roi.toFixed(2)}% profit)</p>
            `);
        """
    },
    {
        "name": "Retirement Calculator",
        "slug": "retirement-calculator",
        "category": "Finance",
        "icon": "⏳",
        "desc": "Calculate the target savings corpus needed for a secure retirement based on standard expenses.",
        "formula": "Retirement Corpus = Annual Expense * Life Expectancy Years (inflation-adjusted)",
        "formula_desc": "Determines total target savings needed to sustain life expenses post-retirement adjusted for inflation.",
        "inputs": [
            {"id": "ret-age", "label": "Current Age", "type": "number", "default": "30", "min": "15", "max": "80", "step": "1"},
            {"id": "ret-target", "label": "Target Retirement Age", "type": "number", "default": "60", "min": "40", "max": "90", "step": "1"},
            {"id": "ret-exp", "label": "Monthly Expense Now ($)", "type": "number", "default": "3000", "min": "100", "max": "1000000", "step": "100"},
            {"id": "ret-inf", "label": "Expected Inflation Rate (%)", "type": "number", "default": "6", "min": "0", "max": "20", "step": "0.1"},
            {"id": "ret-life", "label": "Life Expectancy (Age)", "type": "number", "default": "85", "min": "60", "max": "120", "step": "1"}
        ],
        "outputs": [
            {"id": "out-ret-years", "label": "Years to Retire", "prefix": "", "suffix": " years"},
            {"id": "out-ret-fut-exp", "label": "Fut. Monthly Expense", "prefix": "$", "suffix": ""},
            {"id": "out-ret-corpus", "label": "Total Corpus Needed", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const age = parseFloat(document.getElementById('ret-age').value);
            const target = parseFloat(document.getElementById('ret-target').value);
            const exp = parseFloat(document.getElementById('ret-exp').value);
            const inf = parseFloat(document.getElementById('ret-inf').value) || 0;
            const life = parseFloat(document.getElementById('ret-life').value);

            if (isNaN(age) || isNaN(target) || isNaN(exp) || isNaN(life) || age >= target || target >= life) {
                showToast("Please ensure Current Age < Retirement Age < Life Expectancy.", "error");
                return;
            }

            const yearsToRetire = target - age;
            const futMonthlyExp = exp * Math.pow(1 + (inf / 100), yearsToRetire);
            const retirementYears = life - target;
            const corpus = futMonthlyExp * 12 * retirementYears;

            document.getElementById('out-ret-years').textContent = yearsToRetire;
            document.getElementById('out-ret-fut-exp').textContent = futMonthlyExp.toFixed(2);
            document.getElementById('out-ret-corpus').textContent = corpus.toFixed(2);

            updateBreakdown(`
                <p><strong>Years to retire:</strong> ${yearsToRetire} years</p>
                <p><strong>Post-retirement life span:</strong> ${retirementYears} years</p>
                <p><strong>Maturity Expense (inflation adjusted):</strong> $${(futMonthlyExp*12).toFixed(2)}/yr</p>
                <p><strong>Corpus Target:</strong> $${corpus.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Mortgage Calculator",
        "slug": "mortgage-calculator",
        "category": "Finance",
        "icon": "🏠",
        "desc": "Calculate monthly home loan payments (EMI), interest totals, and amortization details.",
        "formula": "M = P * [ r * (1 + r)^n ] / [ (1 + r)^n - 1 ]",
        "formula_desc": "Computes monthly amortized payments based on loan principal, rate, and tenure.",
        "inputs": [
            {"id": "mort-p", "label": "Home Loan Principal ($)", "type": "number", "default": "250000", "min": "1000", "max": "100000000", "step": "1000"},
            {"id": "mort-r", "label": "Annual Interest Rate (%)", "type": "number", "default": "4.5", "min": "0.1", "max": "30", "step": "0.05"},
            {"id": "mort-t", "label": "Loan Tenure (Years)", "type": "number", "default": "30", "min": "1", "max": "50", "step": "1"}
        ],
        "outputs": [
            {"id": "out-mort-emi", "label": "Monthly EMI Payment", "prefix": "$", "suffix": ""},
            {"id": "out-mort-interest", "label": "Total Interest Payable", "prefix": "$", "suffix": ""},
            {"id": "out-mort-total", "label": "Total Payment (P + I)", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('mort-p').value);
            const r = parseFloat(document.getElementById('mort-r').value);
            const t = parseFloat(document.getElementById('mort-t').value);

            if (isNaN(p) || isNaN(r) || isNaN(t) || p <= 0 || r <= 0 || t <= 0) {
                showToast("Please check mortgage inputs.", "error");
                return;
            }

            const monthlyRate = (r / 100) / 12;
            const monthsCount = t * 12;
            const emi = p * (monthlyRate * Math.pow(1 + monthlyRate, monthsCount)) / (Math.pow(1 + monthlyRate, monthsCount) - 1);
            const total = emi * monthsCount;
            const interest = total - p;

            document.getElementById('out-mort-emi').textContent = emi.toFixed(2);
            document.getElementById('out-mort-interest').textContent = interest.toFixed(2);
            document.getElementById('out-mort-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Principal:</strong> $${p.toFixed(2)} | <strong>Term:</strong> ${monthsCount} months</p>
                <p><strong>Monthly rate:</strong> ${(monthlyRate*100).toFixed(4)}%</p>
                <p><strong>Interest portion:</strong> $${interest.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Credit Card EMI Calculator",
        "slug": "credit-card-emi-calculator",
        "category": "Finance",
        "icon": "💳",
        "desc": "Calculate the EMI and interest payouts for turning credit card dues into monthly installments.",
        "formula": "EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]",
        "formula_desc": "Computes installment values for converting credit card debt balances to fixed monthly loans.",
        "inputs": [
            {"id": "cc-debt", "label": "Credit Card Dues ($)", "type": "number", "default": "5000", "min": "100", "max": "1000000", "step": "100"},
            {"id": "cc-rate", "label": "EMI Annual Interest (%)", "type": "number", "default": "16", "min": "1", "max": "45", "step": "0.5"},
            {"id": "cc-tenure", "label": "Tenure (Months)", "type": "number", "default": "12", "min": "3", "max": "60", "step": "3"}
        ],
        "outputs": [
            {"id": "out-cc-emi", "label": "Monthly EMI", "prefix": "$", "suffix": ""},
            {"id": "out-cc-interest", "label": "Total Interest Dues", "prefix": "$", "suffix": ""},
            {"id": "out-cc-total", "label": "Total Debt Payback", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('cc-debt').value);
            const r = parseFloat(document.getElementById('cc-rate').value);
            const n = parseFloat(document.getElementById('cc-tenure').value);

            if (isNaN(p) || isNaN(r) || isNaN(n) || p <= 0 || r <= 0 || n <= 0) {
                showToast("Check input fields for numbers.", "error");
                return;
            }

            const monthlyRate = (r / 100) / 12;
            const emi = p * (monthlyRate * Math.pow(1 + monthlyRate, n)) / (Math.pow(1 + monthlyRate, n) - 1);
            const total = emi * n;
            const interest = total - p;

            document.getElementById('out-cc-emi').textContent = emi.toFixed(2);
            document.getElementById('out-cc-interest').textContent = interest.toFixed(2);
            document.getElementById('out-cc-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Dues amount:</strong> $${p.toFixed(2)}</p>
                <p><strong>Interest over ${n} months:</strong> $${interest.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Debt Payoff Calculator",
        "slug": "debt-payoff-calculator",
        "category": "Finance",
        "icon": "⚖️",
        "desc": "Determine how fast you can pay off loans by adding extra payments to your monthly dues.",
        "formula": "Months = -log(1 - (P * r) / PMT) / log(1 + r)",
        "formula_desc": "Solves for standard loan repayment cycles when monthly payments exceed minimum EMI.",
        "inputs": [
            {"id": "dp-p", "label": "Debt Balance ($)", "type": "number", "default": "15000", "min": "100", "max": "10000000", "step": "100"},
            {"id": "dp-r", "label": "Annual Interest Rate (%)", "type": "number", "default": "8", "min": "0.1", "max": "50", "step": "0.1"},
            {"id": "dp-pmt", "label": "Planned Monthly Payment ($)", "type": "number", "default": "500", "min": "10", "max": "100000", "step": "10"}
        ],
        "outputs": [
            {"id": "out-dp-months", "label": "Months to Pay Off", "prefix": "", "suffix": " months"},
            {"id": "out-dp-interest", "label": "Total Interest Accrued", "prefix": "$", "suffix": ""},
            {"id": "out-dp-total", "label": "Total Amount Paid", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('dp-p').value);
            const r = parseFloat(document.getElementById('dp-r').value);
            const pmt = parseFloat(document.getElementById('dp-pmt').value);

            if (isNaN(p) || isNaN(r) || isNaN(pmt) || p <= 0 || r <= 0 || pmt <= 0) {
                showToast("Please enter positive values.", "error");
                return;
            }

            const monthlyRate = (r / 100) / 12;
            if (pmt <= p * monthlyRate) {
                showToast("Monthly payment must be greater than monthly interest accrual ($" + (p * monthlyRate).toFixed(2) + ").", "error");
                return;
            }

            const months = -Math.log(1 - (p * monthlyRate) / pmt) / Math.log(1 + monthlyRate);
            const total = pmt * months;
            const interest = total - p;

            document.getElementById('out-dp-months').textContent = Math.ceil(months);
            document.getElementById('out-dp-interest').textContent = interest.toFixed(2);
            document.getElementById('out-dp-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Years:</strong> ${(months/12).toFixed(2)} years</p>
                <p><strong>Total interest:</strong> $${interest.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "GST Calculator",
        "slug": "gst-calculator",
        "category": "Finance",
        "icon": "⚖️",
        "desc": "Calculate standard GST amounts (inclusive/exclusive tax rates) for goods and services.",
        "formula": "GST = Base Price * TaxRate / 100 (Exclusive) | GST = Price - [Price * (100 / (100 + TaxRate))] (Inclusive)",
        "formula_desc": "Computes tax additions or deductions based on chosen index values.",
        "inputs": [
            {"id": "gst-price", "label": "Amount ($)", "type": "number", "default": "1000", "min": "1", "max": "100000000", "step": "10"},
            {"id": "gst-rate", "label": "GST Rate (%)", "type": "number", "default": "18", "min": "1", "max": "50", "step": "1"},
            {"id": "gst-type", "label": "Calculation Type", "type": "select", "options": [("exclusive", "Exclusive (Add GST)"), ("inclusive", "Inclusive (Remove GST)")]}
        ],
        "outputs": [
            {"id": "out-gst-base", "label": "Net Base Amount", "prefix": "$", "suffix": ""},
            {"id": "out-gst-tax", "label": "GST Amount", "prefix": "$", "suffix": ""},
            {"id": "out-gst-total", "label": "Total Gross Amount", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const price = parseFloat(document.getElementById('gst-price').value);
            const rate = parseFloat(document.getElementById('gst-rate').value);
            const type = document.getElementById('gst-type').value;

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

            document.getElementById('out-gst-base').textContent = base.toFixed(2);
            document.getElementById('out-gst-tax').textContent = tax.toFixed(2);
            document.getElementById('out-gst-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Calculation type:</strong> GST ${type}</p>
                <p><strong>GST Amount (${rate}%):</strong> $${tax.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Sales Tax Calculator",
        "slug": "sales-tax-calculator",
        "category": "Finance",
        "icon": "🛍️",
        "desc": "Calculate sales tax amounts, net retail costs, and grand totals for consumer shopping.",
        "formula": "Sales Tax = Before-Tax Price * (Tax Rate / 100)",
        "formula_desc": "Multiplies base value by tax rate to compute total retail invoice price additions.",
        "inputs": [
            {"id": "stx-price", "label": "Before-Tax Price ($)", "type": "number", "default": "150", "min": "0.01", "max": "10000000", "step": "1"},
            {"id": "stx-rate", "label": "Tax Rate (%)", "type": "number", "default": "8.25", "min": "0", "max": "40", "step": "0.01"}
        ],
        "outputs": [
            {"id": "out-stx-tax", "label": "Tax Amount", "prefix": "$", "suffix": ""},
            {"id": "out-stx-total", "label": "Total Price (After-Tax)", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const price = parseFloat(document.getElementById('stx-price').value);
            const rate = parseFloat(document.getElementById('stx-rate').value) || 0;

            if (isNaN(price) || price <= 0) {
                showToast("Please enter a valid price.", "error");
                return;
            }

            const tax = price * (rate / 100);
            const total = price + tax;

            document.getElementById('out-stx-tax').textContent = tax.toFixed(2);
            document.getElementById('out-stx-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p><strong>Base Cost:</strong> $${price.toFixed(2)}</p>
                <p><strong>Sales Tax (${rate}%):</strong> $${tax.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Income Tax Calculator",
        "slug": "income-tax-calculator",
        "category": "Finance",
        "icon": "💵",
        "desc": "Estimate taxable income brackets, net payouts, and tax obligations under basic structures.",
        "formula": "Tax = Income * Bracket rate (progressive)",
        "formula_desc": "Applies tax percentages to progressive income bracket limits.",
        "inputs": [
            {"id": "it-inc", "label": "Gross Annual Income ($)", "type": "number", "default": "75000", "min": "1000", "max": "100000000", "step": "1000"},
            {"id": "it-ded", "label": "Total Deductions ($)", "type": "number", "default": "12000", "min": "0", "max": "5000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-it-net-taxable", "label": "Net Taxable Income", "prefix": "$", "suffix": ""},
            {"id": "out-it-tax", "label": "Estimated Tax Due", "prefix": "$", "suffix": ""},
            {"id": "out-it-takehome", "label": "Effective Take-Home Pay", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const inc = parseFloat(document.getElementById('it-inc').value);
            const ded = parseFloat(document.getElementById('it-ded').value) || 0;

            if (isNaN(inc) || inc <= 0) {
                showToast("Check input income values.", "error");
                return;
            }

            const taxable = Math.max(0, inc - ded);
            let tax = 0;
            if (taxable <= 10000) {
                tax = taxable * 0.1;
            } else if (taxable <= 40000) {
                tax = (10000 * 0.1) + ((taxable - 10000) * 0.15);
            } else if (taxable <= 85000) {
                tax = (10000 * 0.1) + (30000 * 0.15) + ((taxable - 40000) * 0.25);
            } else {
                tax = (10000 * 0.1) + (30000 * 0.15) + (45000 * 0.25) + ((taxable - 85000) * 0.35);
            }

            const takehome = inc - tax;

            document.getElementById('out-it-net-taxable').textContent = taxable.toFixed(2);
            document.getElementById('out-it-tax').textContent = tax.toFixed(2);
            document.getElementById('out-it-takehome').textContent = takehome.toFixed(2);

            updateBreakdown(`
                <p><strong>Gross income:</strong> $${inc.toFixed(2)} | <strong>Deductions:</strong> $${ded.toFixed(2)}</p>
                <p><strong>Tax owed:</strong> $${tax.toFixed(2)} (Effective rate: ${((tax/inc)*100).toFixed(2)}%)</p>
            `);
        """
    },
    {
        "name": "Profit Margin Calculator",
        "slug": "profit-margin-calculator",
        "category": "Finance",
        "icon": "💸",
        "desc": "Calculate profit margins, markups, gross earnings, and pricing metrics for retail sales.",
        "formula": "Profit Margin = (Revenue - Cost) / Revenue * 100",
        "formula_desc": "Determines the percentage profit on sales by checking revenue margins against product cost.",
        "inputs": [
            {"id": "pm-cost", "label": "Product Cost Price ($)", "type": "number", "default": "40", "min": "0.01", "max": "1000000", "step": "0.1"},
            {"id": "pm-rev", "label": "Selling Price / Revenue ($)", "type": "number", "default": "60", "min": "0.01", "max": "1000000", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-pm-profit", "label": "Gross Profit", "prefix": "$", "suffix": ""},
            {"id": "out-pm-margin", "label": "Profit Margin", "prefix": "", "suffix": "%"},
            {"id": "out-pm-markup", "label": "Percentage Markup", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('pm-cost').value);
            const rev = parseFloat(document.getElementById('pm-rev').value);

            if (isNaN(cost) || isNaN(rev) || cost <= 0 || rev <= 0 || rev < cost) {
                showToast("Selling price must exceed product cost.", "error");
                return;
            }

            const profit = rev - cost;
            const margin = (profit / rev) * 100;
            const markup = (profit / cost) * 100;

            document.getElementById('out-pm-profit').textContent = profit.toFixed(2);
            document.getElementById('out-pm-margin').textContent = margin.toFixed(2);
            document.getElementById('out-pm-markup').textContent = markup.toFixed(2);

            updateBreakdown(`
                <p><strong>Cost:</strong> $${cost.toFixed(2)} | <strong>Sale:</strong> $${rev.toFixed(2)}</p>
                <p><strong>Markup applied:</strong> ${markup.toFixed(2)}% on cost</p>
            `);
        """
    },
    {
        "name": "Break-even Calculator",
        "slug": "break-even-calculator",
        "category": "Finance",
        "icon": "⚖️",
        "desc": "Calculate the unit sales needed to cover all business production costs.",
        "formula": "Break-even units = Fixed Costs / (Price - Variable Cost)",
        "formula_desc": "Solves for the point where business revenues equal total costs.",
        "inputs": [
            {"id": "be-fixed", "label": "Total Fixed Costs ($)", "type": "number", "default": "5000", "min": "1", "max": "10000000", "step": "100"},
            {"id": "be-price", "label": "Selling Price per Unit ($)", "type": "number", "default": "25", "min": "0.1", "max": "100000", "step": "1"},
            {"id": "be-var", "label": "Variable Cost per Unit ($)", "type": "number", "default": "15", "min": "0", "max": "100000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-be-units", "label": "Break-even Units Needed", "prefix": "", "suffix": " units"},
            {"id": "out-be-revenue", "label": "Break-even Sales Revenue", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const fixed = parseFloat(document.getElementById('be-fixed').value);
            const price = parseFloat(document.getElementById('be-price').value);
            const variable = parseFloat(document.getElementById('be-var').value) || 0;

            if (isNaN(fixed) || isNaN(price) || isNaN(variable) || fixed <= 0 || price <= 0 || price <= variable) {
                showToast("Price must be greater than variable unit cost.", "error");
                return;
            }

            const margin = price - variable;
            const units = fixed / margin;
            const revenue = units * price;

            document.getElementById('out-be-units').textContent = Math.ceil(units);
            document.getElementById('out-be-revenue').textContent = revenue.toFixed(2);

            updateBreakdown(`
                <p><strong>Fixed overheads:</strong> $${fixed.toFixed(2)}</p>
                <p><strong>Marginal gain per unit:</strong> $${margin.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "ROI Calculator",
        "slug": "roi-calculator",
        "category": "Finance",
        "icon": "💸",
        "desc": "Calculate the Return on Investment (ROI) and annualized gains for your capital payouts.",
        "formula": "ROI = (Net Return / Cost of Investment) * 100",
        "formula_desc": "Evaluates investment efficiency by dividing profits by initial asset purchase costs.",
        "inputs": [
            {"id": "roi-cost", "label": "Initial Investment ($)", "type": "number", "default": "10000", "min": "1", "max": "100000000", "step": "100"},
            {"id": "roi-value", "label": "Final Value ($)", "type": "number", "default": "13500", "min": "0", "max": "100000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-roi-gain", "label": "Total Net Profit", "prefix": "$", "suffix": ""},
            {"id": "out-roi-rate", "label": "Return on Investment (ROI)", "prefix": "", "suffix": "%"}
        ],
        "calc_js": """
            const cost = parseFloat(document.getElementById('roi-cost').value);
            const value = parseFloat(document.getElementById('roi-value').value);

            if (isNaN(cost) || isNaN(value) || cost <= 0 || value < 0) {
                showToast("Check input fields for numerical values.", "error");
                return;
            }

            const gain = value - cost;
            const rate = (gain / cost) * 100;

            document.getElementById('out-roi-gain').textContent = gain.toFixed(2);
            document.getElementById('out-roi-rate').textContent = rate.toFixed(2);

            updateBreakdown(`
                <p><strong>Invested:</strong> $${cost.toFixed(2)} | <strong>Returned:</strong> $${value.toFixed(2)}</p>
                <p><strong>ROI Percentage:</strong> ${rate.toFixed(2)}%</p>
            `);
        """
    },
    {
        "name": "Discount Calculator",
        "slug": "discount-calculator",
        "category": "Finance",
        "icon": "🛍️",
        "desc": "Determine sale pricing, raw savings, and final invoice values during promotion events.",
        "formula": "Saved = Price * (Discount / 100)",
        "formula_desc": "Deducts coupon percentages from primary values to check actual shopping discount costs.",
        "inputs": [
            {"id": "disc-price", "label": "Original Price ($)", "type": "number", "default": "80", "min": "0.1", "max": "1000000", "step": "1"},
            {"id": "disc-rate", "label": "Discount Rate (%)", "type": "number", "default": "25", "min": "0", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-disc-saved", "label": "Amount Saved", "prefix": "$", "suffix": ""},
            {"id": "out-disc-final", "label": "Final Sale Price", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const price = parseFloat(document.getElementById('disc-price').value);
            const rate = parseFloat(document.getElementById('disc-rate').value) || 0;

            if (isNaN(price) || price <= 0 || rate < 0 || rate > 100) {
                showToast("Please check price and discount values (0-100%).", "error");
                return;
            }

            const saved = price * (rate / 100);
            const finalPrice = price - saved;

            document.getElementById('out-disc-saved').textContent = saved.toFixed(2);
            document.getElementById('out-disc-final').textContent = finalPrice.toFixed(2);

            updateBreakdown(`
                <p><strong>Before discount:</strong> $${price.toFixed(2)}</p>
                <p><strong>Discount value (${rate}%):</strong> -$${saved.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Salary Calculator",
        "slug": "salary-calculator",
        "category": "Finance",
        "icon": "💵",
        "desc": "Convert annual salaries to monthly, bi-weekly, weekly, daily, and hourly payouts.",
        "formula": "Monthly = Annual / 12 | Weekly = Annual / 52",
        "formula_desc": "Divides gross wage packages by standard calendar periods.",
        "inputs": [
            {"id": "sal-annual", "label": "Gross Annual Salary ($)", "type": "number", "default": "60000", "min": "100", "max": "100000000", "step": "1000"}
        ],
        "outputs": [
            {"id": "out-sal-monthly", "label": "Monthly Payout", "prefix": "$", "suffix": ""},
            {"id": "out-sal-weekly", "label": "Weekly Wage", "prefix": "$", "suffix": ""},
            {"id": "out-sal-hourly", "label": "Hourly Equivalent (40h/wk)", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const annual = parseFloat(document.getElementById('sal-annual').value);

            if (isNaN(annual) || annual <= 0) {
                showToast("Please check salary values.", "error");
                return;
            }

            const monthly = annual / 12;
            const weekly = annual / 52;
            const hourly = weekly / 40;

            document.getElementById('out-sal-monthly').textContent = monthly.toFixed(2);
            document.getElementById('out-sal-weekly').textContent = weekly.toFixed(2);
            document.getElementById('out-sal-hourly').textContent = hourly.toFixed(2);

            updateBreakdown(`
                <p><strong>Yearly total:</strong> $${annual.toFixed(2)}</p>
                <p><strong>Daily (assuming 260 workdays):</strong> $${(annual/260).toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Hourly Wage Calculator",
        "slug": "hourly-wage-calculator",
        "category": "Finance",
        "icon": "💵",
        "desc": "Calculate weekly and annual income based on hourly wage rates and work hours per week.",
        "formula": "Weekly = Wage * Hours | Annual = Weekly * 52",
        "formula_desc": "Multiplies hourly rate by weekly hours to find overall annual earnings.",
        "inputs": [
            {"id": "hw-rate", "label": "Hourly Rate ($)", "type": "number", "default": "25", "min": "0.1", "max": "5000", "step": "0.5"},
            {"id": "hw-hours", "label": "Hours per Week", "type": "number", "default": "40", "min": "1", "max": "168", "step": "1"}
        ],
        "outputs": [
            {"id": "out-hw-weekly", "label": "Weekly Earnings", "prefix": "$", "suffix": ""},
            {"id": "out-hw-monthly", "label": "Monthly Earnings", "prefix": "$", "suffix": ""},
            {"id": "out-hw-annual", "label": "Annual Gross Earnings", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const rate = parseFloat(document.getElementById('hw-rate').value);
            const hours = parseFloat(document.getElementById('hw-hours').value);

            if (isNaN(rate) || isNaN(hours) || rate <= 0 || hours <= 0) {
                showToast("Please check hourly inputs.", "error");
                return;
            }

            const weekly = rate * hours;
            const annual = weekly * 52;
            const monthly = annual / 12;

            document.getElementById('out-hw-weekly').textContent = weekly.toFixed(2);
            document.getElementById('out-hw-monthly').textContent = monthly.toFixed(2);
            document.getElementById('out-hw-annual').textContent = annual.toFixed(2);

            updateBreakdown(`
                <p><strong>Earnings per hour:</strong> $${rate.toFixed(2)} x ${hours} hours</p>
                <p><strong>Approximate Monthly:</strong> $${monthly.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Freelance Rate Calculator",
        "slug": "freelance-rate-calculator",
        "category": "Finance",
        "icon": "💻",
        "desc": "Calculate the target hourly freelance rate needed to match salary goals after costs and time off.",
        "formula": "Rate = (Salary Goal + Expenses) / (Billable Hours)",
        "formula_desc": "Factors in annual business expenses and non-billable hours to isolate gross freelance service costs.",
        "inputs": [
            {"id": "fr-salary", "label": "Target Net Income ($/year)", "type": "number", "default": "70000", "min": "1000", "max": "10000000", "step": "1000"},
            {"id": "fr-exp", "label": "Annual Business Costs ($)", "type": "number", "default": "10000", "min": "0", "max": "1000000", "step": "500"},
            {"id": "fr-hours", "label": "Billable Hours per Week", "type": "number", "default": "25", "min": "1", "max": "80", "step": "1"},
            {"id": "fr-weeks", "label": "Working Weeks per Year", "type": "number", "default": "48", "min": "10", "max": "52", "step": "1"}
        ],
        "outputs": [
            {"id": "out-fr-total", "label": "Required Gross Revenue", "prefix": "$", "suffix": ""},
            {"id": "out-fr-hours-yr", "label": "Total Billable Hours/year", "prefix": "", "suffix": " hours"},
            {"id": "out-fr-rate", "label": "Target Hourly Rate", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const salary = parseFloat(document.getElementById('fr-salary').value);
            const exp = parseFloat(document.getElementById('fr-exp').value) || 0;
            const hours = parseFloat(document.getElementById('fr-hours').value);
            const weeks = parseFloat(document.getElementById('fr-weeks').value);

            if (isNaN(salary) || isNaN(hours) || isNaN(weeks) || salary <= 0 || hours <= 0 || weeks <= 0) {
                showToast("Please check numeric fields.", "error");
                return;
            }

            const totalRevenue = salary + exp;
            const totalHours = hours * weeks;
            const targetRate = totalRevenue / totalHours;

            document.getElementById('out-fr-total').textContent = totalRevenue.toFixed(2);
            document.getElementById('out-fr-hours-yr').textContent = totalHours;
            document.getElementById('out-fr-rate').textContent = targetRate.toFixed(2);

            updateBreakdown(`
                <p><strong>Gross revenue goal:</strong> $${totalRevenue.toFixed(2)}</p>
                <p><strong>Billable time:</strong> ${totalHours} hours total</p>
            `);
        """
    },
    {
        "name": "Net Worth Calculator",
        "slug": "net-worth-calculator",
        "category": "Finance",
        "icon": "💎",
        "desc": "Calculate your net worth by subtracting total liabilities from your total financial assets.",
        "formula": "Net Worth = Total Assets - Total Liabilities",
        "formula_desc": "Subtracts debt balances from overall personal holdings and investments.",
        "inputs": [
            {"id": "nw-assets-liquid", "label": "Liquid Assets (Cash, Bank) ($)", "type": "number", "default": "15000", "min": "0", "max": "100000000", "step": "500"},
            {"id": "nw-assets-prop", "label": "Property & Real Estate ($)", "type": "number", "default": "250000", "min": "0", "max": "100000000", "step": "1000"},
            {"id": "nw-assets-inv", "label": "Stocks & Investments ($)", "type": "number", "default": "35000", "min": "0", "max": "100000000", "step": "500"},
            {"id": "nw-liab-loans", "label": "Loans & Mortgages ($)", "type": "number", "default": "180000", "min": "0", "max": "100000000", "step": "1000"},
            {"id": "nw-liab-cards", "label": "Credit Card & Short Dues ($)", "type": "number", "default": "2500", "min": "0", "max": "10000000", "step": "100"}
        ],
        "outputs": [
            {"id": "out-nw-assets", "label": "Total Assets", "prefix": "$", "suffix": ""},
            {"id": "out-nw-liab", "label": "Total Liabilities", "prefix": "$", "suffix": ""},
            {"id": "out-nw-net", "label": "Calculated Net Worth", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const liq = parseFloat(document.getElementById('nw-assets-liquid').value) || 0;
            const prop = parseFloat(document.getElementById('nw-assets-prop').value) || 0;
            const inv = parseFloat(document.getElementById('nw-assets-inv').value) || 0;
            const loan = parseFloat(document.getElementById('nw-liab-loans').value) || 0;
            const card = parseFloat(document.getElementById('nw-liab-cards').value) || 0;

            const assets = liq + prop + inv;
            const liabilities = loan + card;
            const netWorth = assets - liabilities;

            document.getElementById('out-nw-assets').textContent = assets.toFixed(2);
            document.getElementById('out-nw-liab').textContent = liabilities.toFixed(2);
            document.getElementById('out-nw-net').textContent = netWorth.toFixed(2);

            updateBreakdown(`
                <p><strong>Total assets:</strong> $${assets.toFixed(2)}</p>
                <p><strong>Total liabilities:</strong> $${liabilities.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Inflation Calculator",
        "slug": "inflation-calculator",
        "category": "Finance",
        "icon": "💸",
        "desc": "Calculate the purchasing power of money over time under historical or custom inflation rates.",
        "formula": "Future Value = Present Value * (1 + Inflation Rate)^Years",
        "formula_desc": "Projects price increases over years using a compound inflation percentage rate.",
        "inputs": [
            {"id": "inf-p", "label": "Current Value ($)", "type": "number", "default": "1000", "min": "1", "max": "100000000", "step": "10"},
            {"id": "inf-r", "label": "Annual Inflation Rate (%)", "type": "number", "default": "3", "min": "-5", "max": "50", "step": "0.1"},
            {"id": "inf-t", "label": "Years in Future", "type": "number", "default": "10", "min": "1", "max": "100", "step": "1"}
        ],
        "outputs": [
            {"id": "out-inf-fut", "label": "Equivalent Future Value", "prefix": "$", "suffix": ""},
            {"id": "out-inf-loss", "label": "Lost Purchasing Power", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const p = parseFloat(document.getElementById('inf-p').value);
            const r = parseFloat(document.getElementById('inf-r').value);
            const t = parseFloat(document.getElementById('inf-t').value);

            if (isNaN(p) || isNaN(r) || isNaN(t) || p <= 0 || t <= 0) {
                showToast("Please check inflation inputs.", "error");
                return;
            }

            const fut = p * Math.pow(1 + (r / 100), t);
            const loss = fut - p;

            document.getElementById('out-inf-fut').textContent = fut.toFixed(2);
            document.getElementById('out-inf-loss').textContent = loss.toFixed(2);

            updateBreakdown(`
                <p><strong>Starting buying power:</strong> $${p.toFixed(2)}</p>
                <p><strong>Required sum in ${t} years:</strong> $${fut.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Future Value Calculator",
        "slug": "future-value-calculator",
        "category": "Finance",
        "icon": "⏳",
        "desc": "Calculate the future value of investments compounded over time at regular intervals.",
        "formula": "FV = PV * (1 + r/n)^(n*t)",
        "formula_desc": "Multiplies current value by compound growth factors to project financial maturity.",
        "inputs": [
            {"id": "fv-pv", "label": "Present Value (PV) ($)", "type": "number", "default": "1000", "min": "1", "max": "100000000", "step": "10"},
            {"id": "fv-rate", "label": "Annual Interest Rate (%)", "type": "number", "default": "8", "min": "0.1", "max": "50", "step": "0.1"},
            {"id": "fv-years", "label": "Time Period (Years)", "type": "number", "default": "5", "min": "1", "max": "50", "step": "1"},
            {"id": "fv-comp", "label": "Compounding Frequency", "type": "select", "options": [("12", "Monthly"), ("4", "Quarterly"), ("1", "Annually")]}
        ],
        "outputs": [
            {"id": "out-fv-tot", "label": "Future Value (FV)", "prefix": "$", "suffix": ""},
            {"id": "out-fv-gain", "label": "Total Growth Earned", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const pv = parseFloat(document.getElementById('fv-pv').value);
            const r = parseFloat(document.getElementById('fv-rate').value);
            const t = parseFloat(document.getElementById('fv-years').value);
            const comp = parseFloat(document.getElementById('fv-comp').value);

            if (isNaN(pv) || isNaN(r) || isNaN(t) || pv <= 0 || t <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const compoundRate = (r / 100) / comp;
            const periods = t * comp;
            const fv = pv * Math.pow(1 + compoundRate, periods);
            const gain = fv - pv;

            document.getElementById('out-fv-tot').textContent = fv.toFixed(2);
            document.getElementById('out-fv-gain').textContent = gain.toFixed(2);

            updateBreakdown(`
                <p><strong>Principal:</strong> $${pv.toFixed(2)} | <strong>Growth rate:</strong> ${r}%</p>
                <p><strong>Total compound periods:</strong> ${periods} (${comp} times/yr)</p>
            `);
        """
    }
]

HEALTH_CALCS = [
    {
        "name": "Calorie Calculator",
        "slug": "calorie-calculator",
        "category": "Health & Fitness",
        "icon": "🍎",
        "desc": "Calculate your daily calorie needs to maintain, lose, or gain weight based on activity.",
        "formula": "Total Calorie Needs = BMR * Activity Factor",
        "formula_desc": "Uses the Mifflin-St Jeor equation to compute Basal Metabolic Rate, scaled by lifestyle activity.",
        "inputs": [
            {"id": "cal-age", "label": "Age (Years)", "type": "number", "default": "25", "min": "15", "max": "80", "step": "1"},
            {"id": "cal-gender", "label": "Gender", "type": "select", "options": [("male", "Male"), ("female", "Female")]},
            {"id": "cal-height", "label": "Height (cm)", "type": "number", "default": "170", "min": "100", "max": "250", "step": "1"},
            {"id": "cal-weight", "label": "Weight (kg)", "type": "number", "default": "70", "min": "30", "max": "300", "step": "0.5"},
            {"id": "cal-act", "label": "Activity Level", "type": "select", "options": [
                ("1.2", "Sedentary (Little/no exercise)"),
                ("1.375", "Light (Exercise 1-3 days/wk)"),
                ("1.55", "Moderate (Exercise 3-5 days/wk)"),
                ("1.725", "Active (Exercise 6-7 days/wk)"),
                ("1.9", "Very Active (Physical work/heavy exercise)")
            ]}
        ],
        "outputs": [
            {"id": "out-cal-maintain", "label": "Maintain Weight", "prefix": "", "suffix": " kcal/day"},
            {"id": "out-cal-lose", "label": "Weight Loss (-0.5kg/wk)", "prefix": "", "suffix": " kcal/day"},
            {"id": "out-cal-gain", "label": "Weight Gain (+0.5kg/wk)", "prefix": "", "suffix": " kcal/day"}
        ],
        "calc_js": """
            const age = parseFloat(document.getElementById('cal-age').value);
            const gender = document.getElementById('cal-gender').value;
            const h = parseFloat(document.getElementById('cal-height').value);
            const w = parseFloat(document.getElementById('cal-weight').value);
            const act = parseFloat(document.getElementById('cal-act').value);

            if (isNaN(age) || isNaN(h) || isNaN(w) || age <= 0 || h <= 0 || w <= 0) {
                showToast("Please enter valid positive values.", "error");
                return;
            }

            let bmr = 10 * w + 6.25 * h - 5 * age;
            if (gender === "male") {
                bmr += 5;
            } else {
                bmr -= 161;
            }

            const maintain = bmr * act;
            const lose = maintain - 500;
            const gain = maintain + 500;

            document.getElementById('out-cal-maintain').textContent = Math.round(maintain);
            document.getElementById('out-cal-lose').textContent = Math.round(lose);
            document.getElementById('out-cal-gain').textContent = Math.round(gain);

            updateBreakdown(`
                <p><strong>Basal Metabolic Rate (BMR):</strong> ${Math.round(bmr)} calories</p>
                <p><strong>Activity multiplier:</strong> x${act}</p>
                <p><strong>Daily Caloric Balance:</strong> ${Math.round(maintain)} kcal</p>
            `);
        """
    },
    {
        "name": "BMR Calculator",
        "slug": "bmr-calculator",
        "category": "Health & Fitness",
        "icon": "⚡",
        "desc": "Calculate your Basal Metabolic Rate (BMR) - the energy required at rest.",
        "formula": "BMR = 10*Weight(kg) + 6.25*Height(cm) - 5*Age(y) + s (s=+5 for men, s=-161 for women)",
        "formula_desc": "Uses the Mifflin-St Jeor equation, the most accurate formula for predicting metabolic rates.",
        "inputs": [
            {"id": "bmr-age", "label": "Age (Years)", "type": "number", "default": "25", "min": "10", "max": "100", "step": "1"},
            {"id": "bmr-gender", "label": "Gender", "type": "select", "options": [("male", "Male"), ("female", "Female")]},
            {"id": "bmr-height", "label": "Height (cm)", "type": "number", "default": "170", "min": "80", "max": "250", "step": "1"},
            {"id": "bmr-weight", "label": "Weight (kg)", "type": "number", "default": "70", "min": "20", "max": "400", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-bmr-kcal", "label": "Basal Metabolic Rate", "prefix": "", "suffix": " kcal/day"},
            {"id": "out-bmr-hourly", "label": "Hourly Energy Expenditure", "prefix": "", "suffix": " kcal/hour"}
        ],
        "calc_js": """
            const age = parseFloat(document.getElementById('bmr-age').value);
            const gender = document.getElementById('bmr-gender').value;
            const h = parseFloat(document.getElementById('bmr-height').value);
            const w = parseFloat(document.getElementById('bmr-weight').value);

            if (isNaN(age) || isNaN(h) || isNaN(w) || age <= 0 || h <= 0 || w <= 0) {
                showToast("Please check numeric fields.", "error");
                return;
            }

            let bmr = 10 * w + 6.25 * h - 5 * age;
            if (gender === "male") {
                bmr += 5;
            } else {
                bmr -= 161;
            }

            document.getElementById('out-bmr-kcal').textContent = Math.round(bmr);
            document.getElementById('out-bmr-hourly').textContent = (bmr / 24).toFixed(1);

            updateBreakdown(`
                <p>Your BMR is the energy your body needs to function at complete rest. Under Mifflin-St Jeor: BMR = ${Math.round(bmr)} kcal/day.</p>
            `);
        """
    },
    {
        "name": "Body Fat Calculator",
        "slug": "body-fat-calculator",
        "category": "Health & Fitness",
        "icon": "⚖️",
        "desc": "Estimate your body fat percentage using the US Navy Circumference Method.",
        "formula": "Body Fat % = US Navy Circumference Equations",
        "formula_desc": "Solves body volume ratios using height, waist, neck, and hip (for women) measurements.",
        "inputs": [
            {"id": "bf-gender", "label": "Gender", "type": "select", "options": [("male", "Male"), ("female", "Female")]},
            {"id": "bf-height", "label": "Height (cm)", "type": "number", "default": "175", "min": "100", "max": "250", "step": "1"},
            {"id": "bf-neck", "label": "Neck Circumference (cm)", "type": "number", "default": "38", "min": "20", "max": "80", "step": "0.1"},
            {"id": "bf-waist", "label": "Waist Circumference (cm)", "type": "number", "default": "86", "min": "40", "max": "200", "step": "0.1"},
            {"id": "bf-hip", "label": "Hip Circumference (cm) (Women)", "type": "number", "default": "90", "min": "40", "max": "200", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-bf-pct", "label": "Body Fat Percentage", "prefix": "", "suffix": "%"},
            {"id": "out-bf-mass", "label": "Fat Mass", "prefix": "", "suffix": " kg"},
            {"id": "out-bf-lean", "label": "Lean Body Mass", "prefix": "", "suffix": " kg"}
        ],
        "calc_js": """
            const gender = document.getElementById('bf-gender').value;
            const h = parseFloat(document.getElementById('bf-height').value);
            const neck = parseFloat(document.getElementById('bf-neck').value);
            const waist = parseFloat(document.getElementById('bf-waist').value);
            const hip = parseFloat(document.getElementById('bf-hip').value) || 0;

            if (isNaN(h) || isNaN(neck) || isNaN(waist) || h <= 0 || neck <= 0 || waist <= 0) {
                showToast("Please enter positive numbers.", "error");
                return;
            }

            let bf = 0;
            if (gender === "male") {
                if (waist <= neck) {
                    showToast("Waist must be larger than neck.", "error");
                    return;
                }
                bf = 86.010 * Math.log10(waist - neck) - 70.041 * Math.log10(h) + 36.76;
            } else {
                if (hip <= 0) {
                    showToast("Please enter hip circumference for females.", "error");
                    return;
                }
                if (waist + hip <= neck) {
                    showToast("Waist + hip must be larger than neck.", "error");
                    return;
                }
                bf = 163.205 * Math.log10(waist + hip - neck) - 97.684 * Math.log10(h) - 78.387;
            }

            if (bf < 2) bf = 2; // Min limit

            document.getElementById('out-bf-pct').textContent = bf.toFixed(1);
            document.getElementById('out-bf-mass').textContent = "-";
            document.getElementById('out-bf-lean').textContent = "-";

            updateBreakdown(`
                <p><strong>Body Fat:</strong> ${bf.toFixed(1)}%</p>
                <p>US Navy method is an empirical estimation formula based on body measurements.</p>
            `);
        """
    },
    {
        "name": "Ideal Weight Calculator",
        "slug": "ideal-weight-calculator",
        "category": "Health & Fitness",
        "icon": "⚖️",
        "desc": "Calculate your ideal body weight range based on height and gender using standard formulas.",
        "formula": "Ideal Weight (Devine) = 50.0 + 2.3 kg per inch over 5 feet (Men) | 45.5 + 2.3 kg per inch (Women)",
        "formula_desc": "Computes ideal body mass indexes based on historical biological models (Devine, Robinson, Miller).",
        "inputs": [
            {"id": "iw-gender", "label": "Gender", "type": "select", "options": [("male", "Male"), ("female", "Female")]},
            {"id": "iw-height", "label": "Height (cm)", "type": "number", "default": "175", "min": "120", "max": "240", "step": "1"}
        ],
        "outputs": [
            {"id": "out-iw-devine", "label": "Devine Formula", "prefix": "", "suffix": " kg"},
            {"id": "out-iw-robinson", "label": "Robinson Formula", "prefix": "", "suffix": " kg"},
            {"id": "out-iw-range", "label": "Healthy BMI Weight Range", "prefix": "", "suffix": " kg"}
        ],
        "calc_js": """
            const gender = document.getElementById('iw-gender').value;
            const h = parseFloat(document.getElementById('iw-height').value);

            if (isNaN(h) || h <= 0) {
                showToast("Please check height inputs.", "error");
                return;
            }

            const inchesOver5Ft = Math.max(0, (h / 2.54) - 60);
            
            let devine = 0;
            let robinson = 0;
            if (gender === "male") {
                devine = 50.0 + 2.3 * inchesOver5Ft;
                robinson = 52.0 + 1.9 * inchesOver5Ft;
            } else {
                devine = 45.5 + 2.3 * inchesOver5Ft;
                robinson = 49.0 + 1.7 * inchesOver5Ft;
            }

            const minBMI = 18.5 * Math.pow(h / 100, 2);
            const maxBMI = 24.9 * Math.pow(h / 100, 2);

            document.getElementById('out-iw-devine').textContent = devine.toFixed(1);
            document.getElementById('out-iw-robinson').textContent = robinson.toFixed(1);
            document.getElementById('out-iw-range').textContent = minBMI.toFixed(1) + " - " + maxBMI.toFixed(1);

            updateBreakdown(`
                <p>Healthy weight range based on standard body mass index is <strong>${minBMI.toFixed(1)} kg to ${maxBMI.toFixed(1)} kg</strong>.</p>
            `);
        """
    },
    {
        "name": "Water Intake Calculator",
        "slug": "water-intake-calculator",
        "category": "Health & Fitness",
        "icon": "💧",
        "desc": "Calculate your daily optimal water intake based on body weight and workout intensity.",
        "formula": "Water Intake (ml) = Weight (kg) * 35 + (Exercise Minutes * 12)",
        "formula_desc": "Combines baseline biological hydration requirements with extra fluids lost during training.",
        "inputs": [
            {"id": "wi-weight", "label": "Weight (kg)", "type": "number", "default": "70", "min": "20", "max": "250", "step": "1"},
            {"id": "wi-exercise", "label": "Daily Exercise (Minutes)", "type": "number", "default": "30", "min": "0", "max": "360", "step": "10"}
        ],
        "outputs": [
            {"id": "out-wi-ml", "label": "Daily Target (ml)", "prefix": "", "suffix": " ml"},
            {"id": "out-wi-liters", "label": "Daily Target (Liters)", "prefix": "", "suffix": " Liters"},
            {"id": "out-wi-glasses", "label": "Glasses (250ml each)", "prefix": "", "suffix": " glasses"}
        ],
        "calc_js": """
            const w = parseFloat(document.getElementById('wi-weight').value);
            const ex = parseFloat(document.getElementById('wi-exercise').value) || 0;

            if (isNaN(w) || w <= 0 || ex < 0) {
                showToast("Please enter valid weight and exercise inputs.", "error");
                return;
            }

            const ml = (w * 35) + (ex * 12);
            const liters = ml / 1000;
            const glasses = ml / 250;

            document.getElementById('out-wi-ml').textContent = Math.round(ml);
            document.getElementById('out-wi-liters').textContent = liters.toFixed(2);
            document.getElementById('out-wi-glasses').textContent = glasses.toFixed(1);

            updateBreakdown(`
                <p>Your baseline water target: <strong>${Math.round(w * 35)} ml</strong>.</p>
                <p>Additional hydration for ${ex} minutes exercise: <strong>${Math.round(ex * 12)} ml</strong>.</p>
            `);
        """
    },
    {
        "name": "Pregnancy Due Date Calculator",
        "slug": "pregnancy-due-date-calculator",
        "category": "Health & Fitness",
        "icon": "🤰",
        "desc": "Estimate your pregnancy due date based on the first day of your last menstrual period.",
        "formula": "Due Date = Last Menstrual Period Date + 280 Days",
        "formula_desc": "Calculates the standard human gestational period of 40 weeks (280 days) from the last period.",
        "inputs": [
            {"id": "pd-lmp", "label": "Last Period Start Date", "type": "date", "default": ""},
            {"id": "pd-cycle", "label": "Average Cycle Length (Days)", "type": "number", "default": "28", "min": "20", "max": "45", "step": "1"}
        ],
        "outputs": [
            {"id": "out-pd-date", "label": "Estimated Due Date", "prefix": "", "suffix": ""},
            {"id": "out-pd-weeks", "label": "Current Gestational Age", "prefix": "", "suffix": " weeks"},
            {"id": "out-pd-rem", "label": "Days Remaining", "prefix": "", "suffix": " days"}
        ],
        "calc_js": """
            const lmpStr = document.getElementById('pd-lmp').value;
            const cycle = parseFloat(document.getElementById('pd-cycle').value);

            if (!lmpStr) {
                showToast("Please select a date.", "error");
                return;
            }

            const lmp = new Date(lmpStr);
            if (isNaN(lmp.getTime())) {
                showToast("Please enter a valid date.", "error");
                return;
            }

            // Adjust standard 280 days for cycle deviations
            const adjustment = cycle - 28;
            const dueDays = 280 + adjustment;
            
            const due = new Date(lmp.getTime() + (dueDays * 24 * 60 * 60 * 1000));
            const today = new Date();
            
            const diffTime = today - lmp;
            const diffDays = Math.max(0, Math.floor(diffTime / (1000 * 60 * 60 * 24)));
            const currentWeeks = (diffDays / 7).toFixed(1);
            
            const remTime = due - today;
            const remDays = Math.max(0, Math.ceil(remTime / (1000 * 60 * 60 * 24)));

            document.getElementById('out-pd-date').textContent = due.toDateString();
            document.getElementById('out-pd-weeks').textContent = currentWeeks;
            document.getElementById('out-pd-rem').textContent = remDays;

            updateBreakdown(`
                <p><strong>First day of last period:</strong> ${lmp.toDateString()}</p>
                <p>Your gestation period adjusted to a ${cycle} day cycle: ${dueDays} days.</p>
            `);
        """
    },
    {
        "name": "Ovulation Calculator",
        "slug": "ovulation-calculator",
        "category": "Health & Fitness",
        "icon": "🤰",
        "desc": "Estimate your most fertile window and ovulation dates for pregnancy planning.",
        "formula": "Ovulation Day = LMP + Cycle Length - 14 Days",
        "formula_desc": "Identifies the ovulation event based on the luteal phase occurring 14 days before the next cycle.",
        "inputs": [
            {"id": "ov-lmp", "label": "Last Period Start Date", "type": "date", "default": ""},
            {"id": "ov-cycle", "label": "Average Cycle Length (Days)", "type": "number", "default": "28", "min": "20", "max": "45", "step": "1"}
        ],
        "outputs": [
            {"id": "out-ov-date", "label": "Ovulation Date", "prefix": "", "suffix": ""},
            {"id": "out-ov-window", "label": "Fertile Window Target", "prefix": "", "suffix": ""},
            {"id": "out-ov-next", "label": "Next Period Start Date", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const lmpStr = document.getElementById('ov-lmp').value;
            const cycle = parseFloat(document.getElementById('ov-cycle').value);

            if (!lmpStr) {
                showToast("Please select a date.", "error");
                return;
            }

            const lmp = new Date(lmpStr);
            if (isNaN(lmp.getTime())) {
                showToast("Please enter a valid date.", "error");
                return;
            }

            const nextPeriod = new Date(lmp.getTime() + (cycle * 24 * 60 * 60 * 1000));
            const ovulation = new Date(nextPeriod.getTime() - (14 * 24 * 60 * 60 * 1000));
            
            const windowStart = new Date(ovulation.getTime() - (5 * 24 * 60 * 60 * 1000));
            const windowEnd = new Date(ovulation.getTime() + (1 * 24 * 60 * 60 * 1000));

            const formatDate = (d) => d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

            document.getElementById('out-ov-date').textContent = formatDate(ovulation);
            document.getElementById('out-ov-window').textContent = formatDate(windowStart) + " to " + formatDate(windowEnd);
            document.getElementById('out-ov-next').textContent = formatDate(nextPeriod);

            updateBreakdown(`
                <p>Fertile window spans 5 days before ovulation plus ovulation day itself.</p>
            `);
        """
    },
    {
        "name": "Heart Rate Calculator",
        "slug": "heart-rate-calculator",
        "category": "Health & Fitness",
        "icon": "❤️",
        "desc": "Calculate your maximum heart rate and target cardiovascular training intensity zones.",
        "formula": "Max HR = 220 - Age | Target HR = (Max HR - Resting HR) * Intensity % + Resting HR (Karvonen method)",
        "formula_desc": "Estimates max heart rates and progressive exertion thresholds for safe cardiac workouts.",
        "inputs": [
            {"id": "hr-age", "label": "Age (Years)", "type": "number", "default": "30", "min": "10", "max": "99", "step": "1"},
            {"id": "hr-resting", "label": "Resting Heart Rate (bpm)", "type": "number", "default": "65", "min": "30", "max": "120", "step": "1"}
        ],
        "outputs": [
            {"id": "out-hr-max", "label": "Estimated Max HR", "prefix": "", "suffix": " bpm"},
            {"id": "out-hr-fatburn", "label": "Fat Burn Zone (50%-70%)", "prefix": "", "suffix": " bpm"},
            {"id": "out-hr-cardio", "label": "Cardio Aerobic Zone (70%-85%)", "prefix": "", "suffix": " bpm"}
        ],
        "calc_js": """
            const age = parseFloat(document.getElementById('hr-age').value);
            const resting = parseFloat(document.getElementById('hr-resting').value);

            if (isNaN(age) || isNaN(resting) || age <= 0 || resting <= 0) {
                showToast("Please fill all numeric fields.", "error");
                return;
            }

            const maxHR = 220 - age;
            const hrr = maxHR - resting; // Heart Rate Reserve

            const fbMin = Math.round(hrr * 0.50 + resting);
            const fbMax = Math.round(hrr * 0.70 + resting);
            
            const cardMin = Math.round(hrr * 0.70 + resting);
            const cardMax = Math.round(hrr * 0.85 + resting);

            document.getElementById('out-hr-max').textContent = maxHR;
            document.getElementById('out-hr-fatburn').textContent = fbMin + " - " + fbMax;
            document.getElementById('out-hr-cardio').textContent = cardMin + " - " + cardMax;

            updateBreakdown(`
                <p>Uses the Karvonen formula which incorporates resting heart rate to establish relative training margins.</p>
            `);
        """
    },
    {
        "name": "Macro Calculator",
        "slug": "macro-calculator",
        "category": "Health & Fitness",
        "icon": "🥩",
        "desc": "Determine optimal carbohydrate, protein, and fat allocations for your fitness objectives.",
        "formula": "Carbs (4 kcal/g) | Protein (4 kcal/g) | Fat (9 kcal/g)",
        "formula_desc": "Divides total caloric targets into macronutrient weight splits based on fitness goals.",
        "inputs": [
            {"id": "mac-cal", "label": "Target Daily Calories (kcal)", "type": "number", "default": "2000", "min": "1000", "max": "8000", "step": "50"},
            {"id": "mac-goal", "label": "Fitness Goal", "type": "select", "options": [
                ("balance", "Balanced Diet (40% Carbs, 30% Protein, 30% Fat)"),
                ("cut", "Low Carb / Cutting (25% Carbs, 40% Protein, 35% Fat)"),
                ("bulk", "High Carb / Bulking (50% Carbs, 25% Protein, 25% Fat)")
            ]}
        ],
        "outputs": [
            {"id": "out-mac-carbs", "label": "Carbohydrates Target", "prefix": "", "suffix": " g/day"},
            {"id": "out-mac-protein", "label": "Protein Target", "prefix": "", "suffix": " g/day"},
            {"id": "out-mac-fat", "label": "Fat Target", "prefix": "", "suffix": " g/day"}
        ],
        "calc_js": """
            const cal = parseFloat(document.getElementById('mac-cal').value);
            const goal = document.getElementById('mac-goal').value;

            if (isNaN(cal) || cal <= 0) {
                showToast("Please check input target calories.", "error");
                return;
            }

            let cPct, pPct, fPct;
            if (goal === "balance") {
                cPct = 0.40; pPct = 0.30; fPct = 0.30;
            } else if (goal === "cut") {
                cPct = 0.25; pPct = 0.40; fPct = 0.35;
            } else {
                cPct = 0.50; pPct = 0.25; fPct = 0.25;
            }

            const carbsG = (cal * cPct) / 4;
            const proteinG = (cal * pPct) / 4;
            const fatG = (cal * fPct) / 9;

            document.getElementById('out-mac-carbs').textContent = Math.round(carbsG);
            document.getElementById('out-mac-protein').textContent = Math.round(proteinG);
            document.getElementById('out-mac-fat').textContent = Math.round(fatG);

            updateBreakdown(`
                <p><strong>Calories distribution:</strong></p>
                <p>Carbohydrates: ${Math.round(cal * cPct)} kcal | Protein: ${Math.round(cal * pPct)} kcal | Fat: ${Math.round(cal * fPct)} kcal</p>
            `);
        """
    },
    {
        "name": "Protein Intake Calculator",
        "slug": "protein-intake-calculator",
        "category": "Health & Fitness",
        "icon": "🥩",
        "desc": "Calculate your recommended daily protein requirements based on weight and activity levels.",
        "formula": "Protein Target = Weight (kg) * Activity Multiplier",
        "formula_desc": "Applies RDA and sports science multipliers (0.8g for sedentary up to 2.0g for athletes) to body weight.",
        "inputs": [
            {"id": "pro-weight", "label": "Weight (kg)", "type": "number", "default": "70", "min": "30", "max": "250", "step": "1"},
            {"id": "pro-activity", "label": "Training Activity Profile", "type": "select", "options": [
                ("0.8", "Sedentary (No regular sport)"),
                ("1.2", "Light Activity (Active / jogger)"),
                ("1.6", "Moderate Training (Gym workout / resistance)"),
                ("2.0", "Athletic / Heavy Lifting (Elite training)")
            ]}
        ],
        "outputs": [
            {"id": "out-pro-target", "label": "Recommended Daily Protein", "prefix": "", "suffix": " grams"},
            {"id": "out-pro-min", "label": "RDA Minimum Target", "prefix": "", "suffix": " grams"}
        ],
        "calc_js": """
            const w = parseFloat(document.getElementById('pro-weight').value);
            const act = parseFloat(document.getElementById('pro-activity').value);

            if (isNaN(w) || w <= 0) {
                showToast("Please enter positive weight values.", "error");
                return;
            }

            const target = w * act;
            const rda = w * 0.8;

            document.getElementById('out-pro-target').textContent = Math.round(target);
            document.getElementById('out-pro-min').textContent = Math.round(rda);

            updateBreakdown(`
                <p>Recommended target using factor <strong>${act} g/kg</strong>: ${Math.round(target)} grams.</p>
                <p>Daily minimum RDA required to prevent deficiency is ${Math.round(rda)} grams.</p>
            `);
        """
    },
    {
        "name": "Workout Calories Burned Calculator",
        "slug": "workout-calories-burned-calculator",
        "category": "Health & Fitness",
        "icon": "🔥",
        "desc": "Estimate total calories burned during physical training sessions using MET values.",
        "formula": "Calories Burned = MET * 3.5 * Weight (kg) / 200 * Duration (Minutes)",
        "formula_desc": "Uses metabolic equivalents (MET) associated with training actions to calculate relative calorie burn.",
        "inputs": [
            {"id": "wcb-weight", "label": "Weight (kg)", "type": "number", "default": "70", "min": "30", "max": "250", "step": "1"},
            {"id": "wcb-duration", "label": "Workout Duration (Minutes)", "type": "number", "default": "45", "min": "1", "max": "480", "step": "5"},
            {"id": "wcb-met", "label": "Training Activity Type", "type": "select", "options": [
                ("3.5", "Walking (Moderate pace)"),
                ("8.0", "Running / Jogging"),
                ("6.0", "Resistance Training / Weight Lifting"),
                ("7.0", "Swimming (Moderate pace)"),
                ("8.5", "Cycling (Fast pace)"),
                ("10.0", "HIIT / Intense Circuit")
            ]}
        ],
        "outputs": [
            {"id": "out-wcb-burned", "label": "Estimated Calories Burned", "prefix": "", "suffix": " kcal"},
            {"id": "out-wcb-rate", "label": "Rate of Calories Burned", "prefix": "", "suffix": " kcal/min"}
        ],
        "calc_js": """
            const w = parseFloat(document.getElementById('wcb-weight').value);
            const d = parseFloat(document.getElementById('wcb-duration').value);
            const met = parseFloat(document.getElementById('wcb-met').value);

            if (isNaN(w) || isNaN(d) || w <= 0 || d <= 0) {
                showToast("Please check numeric fields.", "error");
                return;
            }

            const burned = met * 3.5 * w / 200 * d;
            const rate = burned / d;

            document.getElementById('out-wcb-burned').textContent = Math.round(burned);
            document.getElementById('out-wcb-rate').textContent = rate.toFixed(1);

            updateBreakdown(`
                <p>Activity MET value: <strong>${met}</strong>.</p>
                <p>Approximate metabolic rate during workout: ${rate.toFixed(1)} kcal per minute.</p>
            `);
        """
    },
    {
        "name": "Running Pace Calculator",
        "slug": "running-pace-calculator",
        "category": "Health & Fitness",
        "icon": "🏃",
        "desc": "Calculate your running pace, total elapsed time, or distance for targeted runs.",
        "formula": "Pace = Time / Distance",
        "formula_desc": "Divides total time duration by travel distance to isolate exact minute-per-kilometer ratios.",
        "inputs": [
            {"id": "rp-dist", "label": "Distance (km)", "type": "number", "default": "5", "min": "0.1", "max": "1000", "step": "0.1"},
            {"id": "rp-hours", "label": "Hours", "type": "number", "default": "0", "min": "0", "max": "99", "step": "1"},
            {"id": "rp-minutes", "label": "Minutes", "type": "number", "default": "25", "min": "0", "max": "59", "step": "1"},
            {"id": "rp-seconds", "label": "Seconds", "type": "number", "default": "0", "min": "0", "max": "59", "step": "1"}
        ],
        "outputs": [
            {"id": "out-rp-pace", "label": "Pace", "prefix": "", "suffix": " /km"},
            {"id": "out-rp-speed", "label": "Speed", "prefix": "", "suffix": " km/h"},
            {"id": "out-rp-mile", "label": "Pace Per Mile", "prefix": "", "suffix": " /mile"}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('rp-dist').value);
            const hrs = parseFloat(document.getElementById('rp-hours').value) || 0;
            const mins = parseFloat(document.getElementById('rp-minutes').value) || 0;
            const secs = parseFloat(document.getElementById('rp-seconds').value) || 0;

            if (isNaN(dist) || dist <= 0) {
                showToast("Please enter a valid distance.", "error");
                return;
            }

            const totalSeconds = (hrs * 3600) + (mins * 60) + secs;
            if (totalSeconds <= 0) {
                showToast("Please enter a non-zero time duration.", "error");
                return;
            }

            const paceSecsPerKm = totalSeconds / dist;
            const paceMin = Math.floor(paceSecsPerKm / 60);
            const paceSec = Math.round(paceSecsPerKm % 60);
            const paceStr = paceMin + ":" + (paceSec < 10 ? "0" + paceSec : paceSec);

            const speedKmh = dist / (totalSeconds / 3600);
            
            const paceSecsPerMile = paceSecsPerKm * 1.60934;
            const mileMin = Math.floor(paceSecsPerMile / 60);
            const mileSec = Math.round(paceSecsPerMile % 60);
            const mileStr = mileMin + ":" + (mileSec < 10 ? "0" + mileSec : mileSec);

            document.getElementById('out-rp-pace').textContent = paceStr + " min";
            document.getElementById('out-rp-speed').textContent = speedKmh.toFixed(2);
            document.getElementById('out-rp-mile').textContent = mileStr + " min";

            updateBreakdown(`
                <p>Speed equivalent: <strong>${speedKmh.toFixed(2)} km/h</strong>.</p>
            `);
        """
    },
    {
        "name": "Cycling Calories Calculator",
        "slug": "cycling-calories-calculator",
        "category": "Health & Fitness",
        "icon": "🚴",
        "desc": "Calculate calories burned while cycling based on speed, body weight, and duration.",
        "formula": "Calories Burned = MET * 3.5 * Weight (kg) / 200 * Duration (Minutes)",
        "formula_desc": "Estimates MET indices based on speed intervals (15 km/h to 30+ km/h) to compute energy expenditure.",
        "inputs": [
            {"id": "cy-weight", "label": "Weight (kg)", "type": "number", "default": "70", "min": "30", "max": "250", "step": "1"},
            {"id": "cy-duration", "label": "Duration (Minutes)", "type": "number", "default": "60", "min": "1", "max": "480", "step": "5"},
            {"id": "cy-speed", "label": "Cycling Average Speed", "type": "select", "options": [
                ("4.0", "Leisurely / Light (approx. 14 km/h)"),
                ("6.0", "Moderate pace (approx. 17 km/h)"),
                ("8.0", "Vigorous / Fast (approx. 20 km/h)"),
                ("10.0", "Very Vigorous (approx. 25 km/h)"),
                ("12.0", "Racing / Elite (approx. 30+ km/h)")
            ]}
        ],
        "outputs": [
            {"id": "out-cy-burned", "label": "Total Calories Burned", "prefix": "", "suffix": " kcal"},
            {"id": "out-cy-hourly", "label": "Burn Rate (kcal/hour)", "prefix": "", "suffix": " kcal/h"}
        ],
        "calc_js": """
            const w = parseFloat(document.getElementById('cy-weight').value);
            const d = parseFloat(document.getElementById('cy-duration').value);
            const met = parseFloat(document.getElementById('cy-speed').value);

            if (isNaN(w) || isNaN(d) || w <= 0 || d <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const burned = met * 3.5 * w / 200 * d;
            const hourly = burned / (d / 60);

            document.getElementById('out-cy-burned').textContent = Math.round(burned);
            document.getElementById('out-cy-hourly').textContent = Math.round(hourly);

            updateBreakdown(`
                <p>Estimated MET multiplier: <strong>${met}</strong>.</p>
            `);
        """
    },
    {
        "name": "Sleep Calculator",
        "slug": "sleep-calculator",
        "category": "Health & Fitness",
        "icon": "😴",
        "desc": "Find the best bedtime or wake up times based on natural 90-minute sleep cycles.",
        "formula": "Sleep Cycles = 90 Minutes",
        "formula_desc": "Calculates optimal waking thresholds by compounding 90-minute sleep intervals, adding 15 minutes to fall asleep.",
        "inputs": [
            {"id": "sl-time", "label": "Time Target", "type": "select", "options": [
                ("06:00", "06:00 AM"),
                ("06:30", "06:30 AM"),
                ("07:00", "07:00 AM"),
                ("07:30", "07:30 AM"),
                ("08:00", "08:00 AM"),
                ("08:30", "08:30 AM"),
                ("22:00", "10:00 PM"),
                ("22:30", "10:30 PM"),
                ("23:00", "11:00 PM"),
                ("23:30", "11:30 PM")
            ]},
            {"id": "sl-mode", "label": "Calculation Goal", "type": "select", "options": [
                ("wake", "I want to wake up at this time (Show bedtimes)"),
                ("sleep", "I want to go to bed at this time (Show wake times)")
            ]}
        ],
        "outputs": [
            {"id": "out-sl-opt1", "label": "Option 1 (6 Cycles - 9h)", "prefix": "", "suffix": ""},
            {"id": "out-sl-opt2", "label": "Option 2 (5 Cycles - 7.5h)", "prefix": "", "suffix": ""},
            {"id": "out-sl-opt3", "label": "Option 3 (4 Cycles - 6h)", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const timeVal = document.getElementById('sl-time').value;
            const mode = document.getElementById('sl-mode').value;

            const [hr, min] = timeVal.split(":").map(Number);
            const targetDate = new Date();
            targetDate.setHours(hr, min, 0, 0);

            const options = [];
            const fallAsleepMin = 15;

            if (mode === "wake") {
                // Subtract sleep cycles to find bedtime
                // Option 1: 6 cycles (540 mins) + 15 mins = 555 mins
                const date1 = new Date(targetDate.getTime() - (555 * 60 * 1000));
                // Option 2: 5 cycles (450 mins) + 15 mins = 465 mins
                const date2 = new Date(targetDate.getTime() - (465 * 60 * 1000));
                // Option 3: 4 cycles (360 mins) + 15 mins = 375 mins
                const date3 = new Date(targetDate.getTime() - (375 * 60 * 1000));

                options.push(date1, date2, date3);
            } else {
                // Add sleep cycles to find wake time
                // Option 1: 6 cycles (540 mins) + 15 mins = 555 mins
                const date1 = new Date(targetDate.getTime() + (555 * 60 * 1000));
                // Option 2: 5 cycles (450 mins) + 15 mins = 465 mins
                const date2 = new Date(targetDate.getTime() + (465 * 60 * 1000));
                // Option 3: 4 cycles (360 mins) + 15 mins = 375 mins
                const date3 = new Date(targetDate.getTime() + (375 * 60 * 1000));

                options.push(date1, date2, date3);
            }

            const formatTime = (d) => d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

            document.getElementById('out-sl-opt1').textContent = formatTime(options[0]);
            document.getElementById('out-sl-opt2').textContent = formatTime(options[1]);
            document.getElementById('out-sl-opt3').textContent = formatTime(options[2]);

            updateBreakdown(`
                <p>Calculated assuming it takes about 15 minutes to fall asleep.</p>
            `);
        """
    },
    {
        "name": "Waist-to-Hip Ratio Calculator",
        "slug": "waist-to-hip-ratio-calculator",
        "category": "Health & Fitness",
        "icon": "⚖️",
        "desc": "Calculate your waist-to-hip ratio and check your relative abdominal health indicators.",
        "formula": "WHR = Waist Circumference / Hip Circumference",
        "formula_desc": "Divides waist circumference by hip circumference to assess fat distribution profiles.",
        "inputs": [
            {"id": "whr-gender", "label": "Gender", "type": "select", "options": [("male", "Male"), ("female", "Female")]},
            {"id": "whr-waist", "label": "Waist Circumference (cm)", "type": "number", "default": "80", "min": "40", "max": "200", "step": "0.5"},
            {"id": "whr-hip", "label": "Hip Circumference (cm)", "type": "number", "default": "95", "min": "40", "max": "200", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-whr-ratio", "label": "Waist-to-Hip Ratio", "prefix": "", "suffix": ""},
            {"id": "out-whr-risk", "label": "Health Risk Category", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const gender = document.getElementById('whr-gender').value;
            const w = parseFloat(document.getElementById('whr-waist').value);
            const h = parseFloat(document.getElementById('whr-hip').value);

            if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const ratio = w / h;
            let risk = "Low Risk";
            
            if (gender === "male") {
                if (ratio >= 0.90 && ratio < 1.0) risk = "Moderate Risk";
                else if (ratio >= 1.0) risk = "High Risk";
            } else {
                if (ratio >= 0.80 && ratio < 0.85) risk = "Moderate Risk";
                else if (ratio >= 0.85) risk = "High Risk";
            }

            document.getElementById('out-whr-ratio').textContent = ratio.toFixed(2);
            document.getElementById('out-whr-risk').textContent = risk;

            updateBreakdown(`
                <p>Ratio: <strong>${ratio.toFixed(2)}</strong> (${risk}).</p>
                <p>WHO guidelines indicate a WHR above 0.90 for men and 0.85 for women increases metabolic health risks.</p>
            `);
        """
    }
]
