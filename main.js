/* 
  Enginewheels Global Javascript
  Controls Header scroll states, Mobile burger navigation, Toast Alerts, and Quick Search Indexing
*/

// Tool Index for Client-Side Search
const ENGINYWHEELS_TOOLS = [
  {
    "name": "Word Counter",
    "url": "tools/word-counter.html",
    "category": "Text Tools",
    "desc": "Count words, characters, sentences, paragraphs, and reading time."
  },
  {
    "name": "Case Converter",
    "url": "tools/case-converter.html",
    "category": "Text Tools",
    "desc": "Convert text to UPPERCASE, lowercase, Title Case, Sentence case, and more."
  },
  {
    "name": "Password Generator",
    "url": "tools/password-generator.html",
    "category": "Security Tools",
    "desc": "Create secure custom passwords with entropy assessment."
  },
  {
    "name": "Hash Generator",
    "url": "tools/hash-generator.html",
    "category": "Security Tools",
    "desc": "Generate MD5, SHA-1, SHA-256, and SHA-512 cryptographic hashes."
  },
  {
    "name": "JSON Formatter & Validator",
    "url": "tools/json-formatter.html",
    "category": "Developer Tools",
    "desc": "Format, validate, beautify, and minify raw JSON data."
  },
  {
    "name": "URL Encoder & Decoder",
    "url": "tools/url-encoder-decoder.html",
    "category": "Developer Tools",
    "desc": "Encode or decode strings to match standard URL format."
  },
  {
    "name": "QR Code Generator",
    "url": "tools/qr-code-generator.html",
    "category": "Generators",
    "desc": "Generate and download custom QR codes for links, text, and emails."
  },
  {
    "name": "UUID Generator",
    "url": "tools/uuid-generator.html",
    "category": "Generators",
    "desc": "Generate secure version 4 UUIDs (single or bulk)."
  },
  {
    "name": "Age Calculator",
    "url": "tools/age-calculator.html",
    "category": "Calculators",
    "desc": "Calculate your exact age in years, months, days, and breakdown details."
  },
  {
    "name": "Percentage Calculator",
    "url": "tools/percentage-calculator.html",
    "category": "Calculators",
    "desc": "Perform standard percentage calculations easily."
  },
  {
    "name": "Epoch Time Converter",
    "url": "tools/epoch-converter.html",
    "category": "Time Tools",
    "desc": "Convert Unix timestamps to human-readable dates and vice-versa."
  },
  {
    "name": "Binary Converter",
    "url": "tools/binary-converter.html",
    "category": "Math & Numbers",
    "desc": "Convert numbers or text between Binary, Decimal, Hex, and Octal formats."
  },
  {
    "name": "Color Picker & Converter",
    "url": "tools/color-picker.html",
    "category": "Image Tools",
    "desc": "Translate colors between HEX, RGB, HSL, and CMYK formats."
  },
  {
    "name": "Base64 Image Encoder",
    "url": "tools/base64-image.html",
    "category": "Image Tools",
    "desc": "Convert images to Base64 data strings for inline usage."
  },
  {
    "name": "Meta Tag Generator",
    "url": "tools/meta-tag-generator.html",
    "category": "SEO & Web Tools",
    "desc": "Generate complete meta tags for SEO, OpenGraph, and Twitter."
  },
  {
    "name": "Morse Code Translator",
    "url": "tools/morse-code.html",
    "category": "Fun & Utility",
    "desc": "Translate text to Morse code and back with Web Audio playback."
  },
  {
    "name": "SIP Calculator",
    "url": "calculators/sip-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Estimate your mutual fund investment returns and wealth growth via Systematic Investment Plans."
  },
  {
    "name": "Mutual Fund Returns Calculator",
    "url": "calculators/mutual-fund-returns-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate compound returns and maturity value for mutual fund lumpsum investments."
  },
  {
    "name": "Stock Profit Calculator",
    "url": "calculators/stock-profit-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate your net profit, ROI, and total commissions for buying and selling stocks."
  },
  {
    "name": "Retirement Calculator",
    "url": "calculators/retirement-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the target savings corpus needed for a secure retirement based on standard expenses."
  },
  {
    "name": "Mortgage Calculator",
    "url": "calculators/mortgage-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate monthly home loan payments (EMI), interest totals, and amortization details."
  },
  {
    "name": "Credit Card EMI Calculator",
    "url": "calculators/credit-card-emi-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the EMI and interest payouts for turning credit card dues into monthly installments."
  },
  {
    "name": "Debt Payoff Calculator",
    "url": "calculators/debt-payoff-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Determine how fast you can pay off loans by adding extra payments to your monthly dues."
  },
  {
    "name": "GST Calculator",
    "url": "calculators/gst-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate standard GST amounts (inclusive/exclusive tax rates) for goods and services."
  },
  {
    "name": "Sales Tax Calculator",
    "url": "calculators/sales-tax-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate sales tax amounts, net retail costs, and grand totals for consumer shopping."
  },
  {
    "name": "Income Tax Calculator",
    "url": "calculators/income-tax-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Estimate taxable income brackets, net payouts, and tax obligations under basic structures."
  },
  {
    "name": "Profit Margin Calculator",
    "url": "calculators/profit-margin-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate profit margins, markups, gross earnings, and pricing metrics for retail sales."
  },
  {
    "name": "Break-even Calculator",
    "url": "calculators/break-even-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the unit sales needed to cover all business production costs."
  },
  {
    "name": "ROI Calculator",
    "url": "calculators/roi-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the Return on Investment (ROI) and annualized gains for your capital payouts."
  },
  {
    "name": "Discount Calculator",
    "url": "calculators/discount-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Determine sale pricing, raw savings, and final invoice values during promotion events."
  },
  {
    "name": "Salary Calculator",
    "url": "calculators/salary-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Convert annual salaries to monthly, bi-weekly, weekly, daily, and hourly payouts."
  },
  {
    "name": "Hourly Wage Calculator",
    "url": "calculators/hourly-wage-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate weekly and annual income based on hourly wage rates and work hours per week."
  },
  {
    "name": "Freelance Rate Calculator",
    "url": "calculators/freelance-rate-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the target hourly freelance rate needed to match salary goals after costs and time off."
  },
  {
    "name": "Net Worth Calculator",
    "url": "calculators/net-worth-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate your net worth by subtracting total liabilities from your total financial assets."
  },
  {
    "name": "Inflation Calculator",
    "url": "calculators/inflation-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the purchasing power of money over time under historical or custom inflation rates."
  },
  {
    "name": "Future Value Calculator",
    "url": "calculators/future-value-calculator.html",
    "category": "Calculators (Finance)",
    "desc": "Calculate the future value of investments compounded over time at regular intervals."
  },
  {
    "name": "Calorie Calculator",
    "url": "calculators/calorie-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your daily calorie needs to maintain, lose, or gain weight based on activity."
  },
  {
    "name": "BMR Calculator",
    "url": "calculators/bmr-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your Basal Metabolic Rate (BMR) - the energy required at rest."
  },
  {
    "name": "Body Fat Calculator",
    "url": "calculators/body-fat-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Estimate your body fat percentage using the US Navy Circumference Method."
  },
  {
    "name": "Ideal Weight Calculator",
    "url": "calculators/ideal-weight-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your ideal body weight range based on height and gender using standard formulas."
  },
  {
    "name": "Water Intake Calculator",
    "url": "calculators/water-intake-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your daily optimal water intake based on body weight and workout intensity."
  },
  {
    "name": "Pregnancy Due Date Calculator",
    "url": "calculators/pregnancy-due-date-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Estimate your pregnancy due date based on the first day of your last menstrual period."
  },
  {
    "name": "Ovulation Calculator",
    "url": "calculators/ovulation-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Estimate your most fertile window and ovulation dates for pregnancy planning."
  },
  {
    "name": "Heart Rate Calculator",
    "url": "calculators/heart-rate-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your maximum heart rate and target cardiovascular training intensity zones."
  },
  {
    "name": "Macro Calculator",
    "url": "calculators/macro-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Determine optimal carbohydrate, protein, and fat allocations for your fitness objectives."
  },
  {
    "name": "Protein Intake Calculator",
    "url": "calculators/protein-intake-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your recommended daily protein requirements based on weight and activity levels."
  },
  {
    "name": "Workout Calories Burned Calculator",
    "url": "calculators/workout-calories-burned-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Estimate total calories burned during physical training sessions using MET values."
  },
  {
    "name": "Running Pace Calculator",
    "url": "calculators/running-pace-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your running pace, total elapsed time, or distance for targeted runs."
  },
  {
    "name": "Cycling Calories Calculator",
    "url": "calculators/cycling-calories-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate calories burned while cycling based on speed, body weight, and duration."
  },
  {
    "name": "Sleep Calculator",
    "url": "calculators/sleep-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Find the best bedtime or wake up times based on natural 90-minute sleep cycles."
  },
  {
    "name": "Waist-to-Hip Ratio Calculator",
    "url": "calculators/waist-to-hip-ratio-calculator.html",
    "category": "Calculators (Health & Fitness)",
    "desc": "Calculate your waist-to-hip ratio and check your relative abdominal health indicators."
  },
  {
    "name": "GPA Calculator",
    "url": "calculators/gpa-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate your semester Grade Point Average (GPA) based on grades and course credits."
  },
  {
    "name": "CGPA Calculator",
    "url": "calculators/cgpa-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate your Cumulative Grade Point Average (CGPA) for multiple semesters."
  },
  {
    "name": "Percentage to GPA Converter",
    "url": "calculators/percentage-to-gpa-converter.html",
    "category": "Calculators (Education)",
    "desc": "Convert standard academic percentages to a standard US 4.0 GPA scale."
  },
  {
    "name": "Marks Percentage Calculator",
    "url": "calculators/marks-percentage-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate your grade percentage based on total marks obtained and maximum marks."
  },
  {
    "name": "Attendance Calculator",
    "url": "calculators/attendance-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate how many more classes you need to attend or can skip to maintain a target attendance %."
  },
  {
    "name": "Study Time Calculator",
    "url": "calculators/study-time-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate recommended study hours per week based on course credits and course difficulty."
  },
  {
    "name": "Exam Score Calculator",
    "url": "calculators/exam-score-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate the final exam score you need to achieve a target overall grade in a course."
  },
  {
    "name": "Grade Calculator",
    "url": "calculators/grade-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate weighted averages for assignments, quizzes, midterms, and final exam grades."
  },
  {
    "name": "Average Marks Calculator",
    "url": "calculators/average-marks-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate the arithmetic average score for up to 6 different subjects."
  },
  {
    "name": "Weighted Average Calculator",
    "url": "calculators/weighted-average-calculator.html",
    "category": "Calculators (Education)",
    "desc": "Calculate the weighted average of values with differing percentage or fractional weights."
  },
  {
    "name": "Invoice Calculator",
    "url": "calculators/invoice-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate subtotal, tax amounts, discount deductions, and invoice grand totals."
  },
  {
    "name": "VAT Calculator",
    "url": "calculators/vat-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate Value Added Tax (VAT) additions or removals on retail invoice pricing."
  },
  {
    "name": "Commission Calculator",
    "url": "calculators/commission-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate total commission amounts and sales payout distributions."
  },
  {
    "name": "Markup Calculator",
    "url": "calculators/markup-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Determine selling price, gross profit, and profit margin based on cost and markup rate."
  },
  {
    "name": "Inventory Turnover Calculator",
    "url": "calculators/inventory-turnover-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate how many times inventory is sold and replaced over a business cycle."
  },
  {
    "name": "Cash Flow Calculator",
    "url": "calculators/cash-flow-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate net operational cash flow balances by auditing inflows and outflows."
  },
  {
    "name": "Payback Period Calculator",
    "url": "calculators/payback-period-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Determine how many years it will take to recover the cost of a capital investment."
  },
  {
    "name": "Depreciation Calculator",
    "url": "calculators/depreciation-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate annual straight-line asset depreciation value and salvage balance."
  },
  {
    "name": "Business Loan Calculator",
    "url": "calculators/business-loan-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate monthly EMI and total interest for commercial loans."
  },
  {
    "name": "Revenue Growth Calculator",
    "url": "calculators/revenue-growth-calculator.html",
    "category": "Calculators (Business)",
    "desc": "Calculate your business year-over-year or month-over-month revenue growth rate."
  },
  {
    "name": "Concrete Calculator",
    "url": "calculators/concrete-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate the concrete volume and bag count required for slabs, columns, and foundations."
  },
  {
    "name": "Paint Calculator",
    "url": "calculators/paint-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate paint volume required based on wall surface area and number of coats."
  },
  {
    "name": "Tile Calculator",
    "url": "calculators/tile-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate total tile units and packaging boxes needed for flooring or wall surface layouts."
  },
  {
    "name": "Brick Calculator",
    "url": "calculators/brick-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate the brick count required for walls based on dimensions and brick sizes."
  },
  {
    "name": "Flooring Calculator",
    "url": "calculators/flooring-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate required floor materials (laminate, hardwood, vinyl) and total purchase costs."
  },
  {
    "name": "Roofing Calculator",
    "url": "calculators/roofing-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate roof area and total shingles bundles needed based on roof dimensions and pitch."
  },
  {
    "name": "Asphalt Calculator",
    "url": "calculators/asphalt-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate the volume and weight of asphalt required for paving driveways or roads."
  },
  {
    "name": "Sand Calculator",
    "url": "calculators/sand-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate total volume and weight of sand required for landscaping or concrete mixes."
  },
  {
    "name": "Cement Calculator",
    "url": "calculators/cement-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate standard cement bags, sand, and gravel quantities for specific concrete volumes."
  },
  {
    "name": "Land Area Calculator",
    "url": "calculators/land-area-calculator.html",
    "category": "Calculators (Construction)",
    "desc": "Calculate land area in square meters, square feet, acres, and hectares."
  },
  {
    "name": "Fuel Cost Calculator",
    "url": "calculators/fuel-cost-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate total fuel volume and cost for road trips based on distance and fuel efficiency."
  },
  {
    "name": "Mileage Calculator",
    "url": "calculators/mileage-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate vehicle fuel efficiency (mileage) based on distance covered and fuel filled."
  },
  {
    "name": "Trip Cost Calculator",
    "url": "calculators/trip-cost-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate total road trip costs, including fuel, road tolls, and food/lodging expenses."
  },
  {
    "name": "Flight Time Calculator",
    "url": "calculators/flight-time-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Estimate direct flight time durations between cities based on distance and speed."
  },
  {
    "name": "Travel Budget Calculator",
    "url": "calculators/travel-budget-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate your total travel budget, accounting for flights, hotels, food, and daily allowances."
  },
  {
    "name": "Currency Exchange Calculator",
    "url": "calculators/currency-exchange-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Convert monetary sums instantly using a fixed exchange rate."
  },
  {
    "name": "Hotel Cost Calculator",
    "url": "calculators/hotel-cost-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate total lodging invoices, including daily taxes and service fee additions."
  },
  {
    "name": "Road Trip Planner Calculator",
    "url": "calculators/road-trip-planner-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate total drive time and travel days required based on distance and daily driving limits."
  },
  {
    "name": "Taxi Fare Calculator",
    "url": "calculators/taxi-fare-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Estimate total metered taxi fares using local transit distance rates and base fees."
  },
  {
    "name": "Speed Calculator",
    "url": "calculators/speed-calculator.html",
    "category": "Calculators (Travel)",
    "desc": "Calculate average speeds based on elapsed time and traveled route distance."
  },
  {
    "name": "Area Calculator",
    "url": "calculators/area-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate surface areas for rectangles, circles, triangles, and parallelograms."
  },
  {
    "name": "Volume Calculator",
    "url": "calculators/volume-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate volumetric contents for boxes, cylinders, cones, and spheres."
  },
  {
    "name": "Surface Area Calculator",
    "url": "calculators/surface-area-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate total external surface areas for prisms, cylinders, and spheres."
  },
  {
    "name": "Triangle Calculator",
    "url": "calculators/triangle-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate triangle area and perimeter based on base and height dimensions."
  },
  {
    "name": "Circle Calculator",
    "url": "calculators/circle-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate circular area, circumference, and diameter based on radius inputs."
  },
  {
    "name": "Pythagorean Theorem Calculator",
    "url": "calculators/pythagorean-theorem-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Solve right triangle side dimensions (a, b, c) using the Pythagorean theorem."
  },
  {
    "name": "Quadratic Equation Calculator",
    "url": "calculators/quadratic-equation-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate real and complex roots for quadratic equations in ax\u00b2 + bx + c = 0 format."
  },
  {
    "name": "Matrix Calculator",
    "url": "calculators/matrix-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Perform addition, subtraction, and multiplication operations on 2x2 matrices."
  },
  {
    "name": "Determinant Calculator",
    "url": "calculators/determinant-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate the determinant of a standard 2x2 matrix."
  },
  {
    "name": "Log Calculator",
    "url": "calculators/log-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate logarithm values for a number to any custom base or common natural log base."
  },
  {
    "name": "Percentage Increase Calculator",
    "url": "calculators/percentage-increase-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate the percentage increase between two numerical values."
  },
  {
    "name": "Percentage Decrease Calculator",
    "url": "calculators/percentage-decrease-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate the percentage decrease and raw drops between two numerical values."
  },
  {
    "name": "Average Calculator",
    "url": "calculators/average-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate the arithmetic average (mean) for a set of comma-separated numbers."
  },
  {
    "name": "Median Calculator",
    "url": "calculators/median-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate the median (middle value) of a set of comma-separated numbers."
  },
  {
    "name": "Mode Calculator",
    "url": "calculators/mode-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Find the mode (most frequent number) for a set of comma-separated numbers."
  },
  {
    "name": "Standard Deviation Calculator",
    "url": "calculators/standard-deviation-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate standard deviation and variance for datasets."
  },
  {
    "name": "Probability Calculator",
    "url": "calculators/probability-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate basic probabilities based on favorable outcomes and total events."
  },
  {
    "name": "Permutation Calculator",
    "url": "calculators/permutation-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate permutations nPr - where ordering matches matters."
  },
  {
    "name": "Combination Calculator",
    "url": "calculators/combination-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate combinations nCr - where ordering does not matter."
  },
  {
    "name": "Factorial Calculator",
    "url": "calculators/factorial-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Calculate the factorial (n!) of positive integers."
  },
  {
    "name": "Scientific Notation Calculator",
    "url": "calculators/scientific-notation-calculator.html",
    "category": "Calculators (Math & Engineering)",
    "desc": "Convert standard decimal numbers to scientific notation format."
  },
  {
    "name": "Age In Days Calculator",
    "url": "calculators/age-in-days-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Calculate your exact age in days based on your birthdate."
  },
  {
    "name": "Days Between Dates Calculator",
    "url": "calculators/days-between-dates-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Calculate the total number of calendar days between two selected dates."
  },
  {
    "name": "Business Days Calculator",
    "url": "calculators/business-days-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Calculate the count of business working days (excluding weekends) between two dates."
  },
  {
    "name": "Hours Between Times Calculator",
    "url": "calculators/hours-between-times-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Calculate exact hours and minutes elapsed between two active daily time nodes."
  },
  {
    "name": "Time Duration Calculator",
    "url": "calculators/time-duration-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Add or subtract custom periods of days, hours, and minutes."
  },
  {
    "name": "Countdown Calculator",
    "url": "calculators/countdown-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Calculate time remaining (days, hours, minutes) until a target future event."
  },
  {
    "name": "Leap Year Calculator",
    "url": "calculators/leap-year-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Check if a calendar year is a leap year containing 366 days."
  },
  {
    "name": "Week Number Calculator",
    "url": "calculators/week-number-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Find the ISO-8601 week number for any selected date."
  },
  {
    "name": "Unix Timestamp Calculator",
    "url": "calculators/unix-timestamp-calculator.html",
    "category": "Calculators (Date & Time)",
    "desc": "Convert standard dates to Unix epoch timestamps."
  },
  {
    "name": "Advertising ROI Calculator",
    "url": "calculators/advertising-roi-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate Return on Ad Spend (ROAS) and ROI for digital marketing campaigns."
  },
  {
    "name": "CPC Calculator",
    "url": "calculators/cpc-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate Cost Per Click (CPC) for pay-per-click marketing campaigns."
  },
  {
    "name": "CPM Calculator",
    "url": "calculators/cpm-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate Cost Per Mille (CPM) - the advertising cost per 1,000 impressions."
  },
  {
    "name": "CTR Calculator",
    "url": "calculators/ctr-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate Click-Through Rate (CTR) for links, emails, and ads."
  },
  {
    "name": "Conversion Rate Calculator",
    "url": "calculators/conversion-rate-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate the conversion rate for sign-ups, sales, or lead generation campaigns."
  },
  {
    "name": "Email Open Rate Calculator",
    "url": "calculators/email-open-rate-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate the open rate of your email marketing campaigns."
  },
  {
    "name": "Social Media Engagement Calculator",
    "url": "calculators/social-media-engagement-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Calculate your engagement rate based on likes, comments, shares, and followers."
  },
  {
    "name": "Affiliate Earnings Calculator",
    "url": "calculators/affiliate-earnings-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Estimate affiliate marketing revenue based on referral traffic and commission rates."
  },
  {
    "name": "Influencer Rate Calculator",
    "url": "calculators/influencer-rate-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Estimate earnings per sponsored post based on follower size and engagement rates."
  },
  {
    "name": "Keyword Density Calculator",
    "url": "calculators/keyword-density-calculator.html",
    "category": "Calculators (SEO & Marketing)",
    "desc": "Find the keyword density of a specific target keyword within your article content."
  },
  {
    "name": "Love Calculator",
    "url": "calculators/love-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Estimate romantic compatibility percentages between two partner names."
  },
  {
    "name": "Compatibility Calculator",
    "url": "calculators/compatibility-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Calculate astrological compatibility percentages based on zodiac signs."
  },
  {
    "name": "Birthday Calculator",
    "url": "calculators/birthday-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Calculate days remaining until your next birthday and check your astrological profiles."
  },
  {
    "name": "Pet Age Calculator",
    "url": "calculators/pet-age-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Convert standard dog and cat ages to equivalent human years."
  },
  {
    "name": "Zodiac Calculator",
    "url": "calculators/zodiac-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Calculate your zodiac sign and elemental alignment based on birthdate."
  },
  {
    "name": "Life Path Number Calculator",
    "url": "calculators/life-path-number-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Calculate your numerology Life Path Number based on your birthdate."
  },
  {
    "name": "Daily Water Calculator",
    "url": "calculators/daily-water-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Calculate standard daily baseline drinking water requirements based on body weight."
  },
  {
    "name": "Screen Time Calculator",
    "url": "calculators/screen-time-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Calculate how much of your life is spent looking at screens (phones, computers, TV)."
  },
  {
    "name": "Carbon Footprint Calculator",
    "url": "calculators/carbon-footprint-calculator.html",
    "category": "Calculators (Lifestyle)",
    "desc": "Estimate your average carbon emissions based on home utilities and driving habits."
  },
  {
    "name": "Word Counter",
    "url": "text-tools/word-counter.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Count words, characters, sentences, paragraphs, and reading times in real-time."
  },
  {
    "name": "Character Counter",
    "url": "text-tools/character-counter.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Count total characters, letters, numbers, and symbols with or without spaces."
  },
  {
    "name": "Sentence Counter",
    "url": "text-tools/sentence-counter.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Count the total number of sentences in your writing instantly."
  },
  {
    "name": "Paragraph Counter",
    "url": "text-tools/paragraph-counter.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Calculate total paragraphs in your document, ignoring empty lines."
  },
  {
    "name": "Reading Time Calculator",
    "url": "text-tools/reading-time-calculator.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Calculate estimated reading time based on typical human WPM speeds."
  },
  {
    "name": "Speaking Time Calculator",
    "url": "text-tools/speaking-time-calculator.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Calculate speaking time for presentations, speeches, and podcasts."
  },
  {
    "name": "Text Reverser",
    "url": "text-tools/text-reverser.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Reverse your text letters, words, or sentences instantly."
  },
  {
    "name": "Line Counter",
    "url": "text-tools/line-counter.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Count total lines, empty lines, and non-empty lines in text."
  },
  {
    "name": "Whitespace Remover",
    "url": "text-tools/whitespace-remover.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Remove extra spaces, tabs, and newlines from your text strings."
  },
  {
    "name": "Duplicate Line Remover",
    "url": "text-tools/duplicate-line-remover.html",
    "category": "Text Tools (Basic Text Tools)",
    "desc": "Filter out duplicate lines of text, leaving only unique rows."
  },
  {
    "name": "Uppercase Converter",
    "url": "text-tools/uppercase-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Convert all alphabetical characters in your text to uppercase letters."
  },
  {
    "name": "Lowercase Converter",
    "url": "text-tools/lowercase-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Convert all alphabetical characters in your text to lowercase letters."
  },
  {
    "name": "Title Case Converter",
    "url": "text-tools/title-case-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Format text with capitalized principal words for book, essay, or email titles."
  },
  {
    "name": "Sentence Case Converter",
    "url": "text-tools/sentence-case-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Capitalize the first letter of each sentence, setting others to lowercase."
  },
  {
    "name": "Toggle Case Converter",
    "url": "text-tools/toggle-case-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Invert the capitalization of every single letter in your text."
  },
  {
    "name": "Capitalize Words Tool",
    "url": "text-tools/capitalize-words-tool.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Capitalize the first letter of every single word in your text."
  },
  {
    "name": "camelCase Converter",
    "url": "text-tools/camelcase-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Convert text into camelCase variable naming convention style."
  },
  {
    "name": "PascalCase Converter",
    "url": "text-tools/pascalcase-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Convert text to PascalCase format, popular for class structures in coding."
  },
  {
    "name": "snake_case Converter",
    "url": "text-tools/snake-case-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Convert text into snake_case format, commonly used in database schema names."
  },
  {
    "name": "kebab-case Converter",
    "url": "text-tools/kebab-case-converter.html",
    "category": "Text Tools (Case Converters)",
    "desc": "Convert text into kebab-case format, ideal for URL slug conventions."
  },
  {
    "name": "Text Cleaner",
    "url": "text-tools/text-cleaner.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Clean text by removing control characters, fixing bad spaces, and tidying markup symbols."
  },
  {
    "name": "Text Formatter",
    "url": "text-tools/text-formatter.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Standardize text spacing, sentence capitalization, and paragraph alignments."
  },
  {
    "name": "Text Sorter",
    "url": "text-tools/text-sorter.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Sort text lines alphabetically, numerically, by length, or in reverse."
  },
  {
    "name": "Alphabetical Sorter",
    "url": "text-tools/alphabetical-sorter.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Sort text lines in ascending alphabetical order (A to Z)."
  },
  {
    "name": "Reverse Sorter",
    "url": "text-tools/reverse-sorter.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Sort text lines in reverse alphabetical order (Z to A)."
  },
  {
    "name": "Randomize Lines",
    "url": "text-tools/randomize-lines.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Shuffle and randomize the order of lines in your text block."
  },
  {
    "name": "Remove Empty Lines",
    "url": "text-tools/remove-empty-lines.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Remove all completely blank or whitespace-only lines from text."
  },
  {
    "name": "Trim Text Tool",
    "url": "text-tools/trim-text-tool.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Remove leading, trailing, and unnecessary whitespace from text lines."
  },
  {
    "name": "Text Indenter",
    "url": "text-tools/text-indenter.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Add custom spaces or tab indentations to the beginning of each line."
  },
  {
    "name": "Text Outdenter",
    "url": "text-tools/text-outdenter.html",
    "category": "Text Tools (Text Formatters)",
    "desc": "Remove leading tab or space indentations from your text lines."
  },
  {
    "name": "Find And Replace Text",
    "url": "text-tools/find-and-replace-text.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Find occurrences of specific text strings and replace them with new content."
  },
  {
    "name": "Multi Text Replace Tool",
    "url": "text-tools/multi-text-replace-tool.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Find and replace multiple words at once using comma-separated rules."
  },
  {
    "name": "Remove Specific Words",
    "url": "text-tools/remove-specific-words.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Remove selected words or phrases from your text block entirely."
  },
  {
    "name": "Remove Numbers From Text",
    "url": "text-tools/remove-numbers-from-text.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Remove all numeric digits (0-9) from your text string."
  },
  {
    "name": "Remove Special Characters",
    "url": "text-tools/remove-special-characters.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Remove symbols, emojis, and special chars, keeping letters and numbers."
  },
  {
    "name": "Remove Punctuation Tool",
    "url": "text-tools/remove-punctuation-tool.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Strip punctuation marks like periods, commas, and question marks from text."
  },
  {
    "name": "Extract Numbers From Text",
    "url": "text-tools/extract-numbers-from-text.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Pull all numbers and integers out of a mixed text document."
  },
  {
    "name": "Extract Emails From Text",
    "url": "text-tools/extract-emails-from-text.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Extract all email addresses from a large text document or list."
  },
  {
    "name": "Extract URLs From Text",
    "url": "text-tools/extract-urls-from-text.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Scan text and extract all HTTP, HTTPS, and FTP web links."
  },
  {
    "name": "Extract Hashtags From Text",
    "url": "text-tools/extract-hashtags-from-text.html",
    "category": "Text Tools (Search & Replace Tools)",
    "desc": "Extract hashtags (#topic) from tweets, posts, or marketing copies."
  },
  {
    "name": "Keyword Density Checker",
    "url": "text-tools/keyword-density-checker.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Check keyword density percentage and word frequency in your website content."
  },
  {
    "name": "Meta Description Length Checker",
    "url": "text-tools/meta-description-length-checker.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Verify if your meta description fits the Google 120-160 character limit guidelines."
  },
  {
    "name": "Title Length Checker",
    "url": "text-tools/title-length-checker.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Check your SEO meta title length against the optimal 50-60 character limits."
  },
  {
    "name": "Word Frequency Counter",
    "url": "text-tools/word-frequency-counter.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Count the frequency of each word in your text, sorting by popularity."
  },
  {
    "name": "Text Readability Checker",
    "url": "text-tools/text-readability-checker.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Measure readability based on the Flesch-Kincaid Reading Ease formula."
  },
  {
    "name": "SEO Content Analyzer",
    "url": "text-tools/seo-content-analyzer.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Run content audits for target word limits, headings, and readability."
  },
  {
    "name": "Keyword Extractor",
    "url": "text-tools/keyword-extractor.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Extract important keywords and phrases from your text content."
  },
  {
    "name": "Keyword Position Checker",
    "url": "text-tools/keyword-position-checker.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Verify where keywords appear in your article (e.g. first 100 words)."
  },
  {
    "name": "Content Density Analyzer",
    "url": "text-tools/content-density-analyzer.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Analyze content weight parameters including sentence count ratios."
  },
  {
    "name": "N-Gram Generator",
    "url": "text-tools/n-gram-generator.html",
    "category": "Text Tools (SEO Text Tools)",
    "desc": "Generate lists of unigrams, bigrams, and trigrams from text."
  },
  {
    "name": "Article Rewriter",
    "url": "text-tools/article-rewriter.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Rewrite articles and essays by replacing words with matching synonyms."
  },
  {
    "name": "Paragraph Rewriter",
    "url": "text-tools/paragraph-rewriter.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Rewrite text paragraphs automatically to change structure and flow."
  },
  {
    "name": "Sentence Rewriter",
    "url": "text-tools/sentence-rewriter.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Rewrite sentences by swapping phrases and terms with equivalents."
  },
  {
    "name": "Headline Generator",
    "url": "text-tools/headline-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Generate high-CTR news, article, and essay headlines from topics."
  },
  {
    "name": "Blog Title Generator",
    "url": "text-tools/blog-title-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Create engaging, click-worthy blog title ideas from keywords."
  },
  {
    "name": "Meta Description Generator",
    "url": "text-tools/meta-description-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Generate custom, action-oriented SEO meta descriptions instantly."
  },
  {
    "name": "Product Description Generator",
    "url": "text-tools/product-description-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Generate catchy sales descriptions for products and services."
  },
  {
    "name": "YouTube Title Generator",
    "url": "text-tools/youtube-title-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Create catchy, click-worthy YouTube titles to increase video views."
  },
  {
    "name": "YouTube Description Generator",
    "url": "text-tools/youtube-description-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Generate SEO-optimized descriptions for your YouTube videos."
  },
  {
    "name": "Social Media Caption Generator",
    "url": "text-tools/social-media-caption-generator.html",
    "category": "Text Tools (Content Writing Tools)",
    "desc": "Create engaging social media captions with emojis and hashtags."
  },
  {
    "name": "Hashtag Generator",
    "url": "text-tools/hashtag-generator.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Generate relevant hashtags for Instagram, Twitter, and TikTok based on keywords."
  },
  {
    "name": "Instagram Caption Formatter",
    "url": "text-tools/instagram-caption-formatter.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Format Instagram captions with clean line breaks that will not collapse."
  },
  {
    "name": "Twitter Character Counter",
    "url": "text-tools/twitter-character-counter.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Track your character counts against the Twitter/X 280 character limit limit."
  },
  {
    "name": "LinkedIn Post Formatter",
    "url": "text-tools/linkedin-post-formatter.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Format LinkedIn posts with emojis, clean lists, and line spacing."
  },
  {
    "name": "Facebook Text Formatter",
    "url": "text-tools/facebook-text-formatter.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Format Facebook posts with headers and call-to-action line spacings."
  },
  {
    "name": "Emoji Text Generator",
    "url": "text-tools/emoji-text-generator.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Insert emojis between words or replace keywords with relevant emojis."
  },
  {
    "name": "Fancy Text Generator",
    "url": "text-tools/fancy-text-generator.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Convert normal text to cool fancy styles for bio descriptions."
  },
  {
    "name": "Stylish Font Generator",
    "url": "text-tools/stylish-font-generator.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Generate stylish unicode fonts for social media profiles."
  },
  {
    "name": "Unicode Text Generator",
    "url": "text-tools/unicode-text-generator.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Convert standard text to gothic, script, and serif unicode fonts."
  },
  {
    "name": "Text Decorator",
    "url": "text-tools/text-decorator.html",
    "category": "Text Tools (Social Media Tools)",
    "desc": "Decorate your text with unique border stars, arrows, and shapes."
  },
  {
    "name": "JSON Formatter",
    "url": "text-tools/json-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Validate, beautify, indent, or minify your raw JSON code."
  },
  {
    "name": "XML Formatter",
    "url": "text-tools/xml-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Beautify and format messy XML documents with indentations."
  },
  {
    "name": "SQL Formatter",
    "url": "text-tools/sql-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Beautify database queries by capitalizing SQL commands and keywords."
  },
  {
    "name": "HTML Formatter",
    "url": "text-tools/html-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Clean and format HTML code with proper tag indentations."
  },
  {
    "name": "CSS Formatter",
    "url": "text-tools/css-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Format messy CSS style blocks with clean linebreaks and tab spacings."
  },
  {
    "name": "JavaScript Formatter",
    "url": "text-tools/javascript-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Beautify JS scripts with consistent brace matching and semicolon splits."
  },
  {
    "name": "Markdown Formatter",
    "url": "text-tools/markdown-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Standardize Markdown files by fixing blank spacing under headers."
  },
  {
    "name": "YAML Formatter",
    "url": "text-tools/yaml-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Check and format YAML files, correcting indentations and key-value margins."
  },
  {
    "name": "CSV Formatter",
    "url": "text-tools/csv-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Convert raw CSV files into cleanly formatted Markdown tables."
  },
  {
    "name": "TSV Formatter",
    "url": "text-tools/tsv-formatter.html",
    "category": "Text Tools (Developer Text Tools)",
    "desc": "Convert TSV (tab-separated values) data into formatted Markdown tables."
  },
  {
    "name": "Text To Binary",
    "url": "text-tools/text-to-binary.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Convert standard text characters to binary code bytes (0s and 1s)."
  },
  {
    "name": "Binary To Text",
    "url": "text-tools/binary-to-text.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Decode binary sequences (0s and 1s) back into readable text."
  },
  {
    "name": "Text To ASCII",
    "url": "text-tools/text-to-ascii.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Convert text characters to their corresponding ASCII code numbers."
  },
  {
    "name": "ASCII To Text",
    "url": "text-tools/ascii-to-text.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Convert ASCII decimal code numbers back into readable text."
  },
  {
    "name": "Text To Hex",
    "url": "text-tools/text-to-hex.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Convert text strings to hexadecimal (base-16) representation format."
  },
  {
    "name": "Hex To Text",
    "url": "text-tools/hex-to-text.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Decode hexadecimal character strings back into readable text."
  },
  {
    "name": "Text To Base64",
    "url": "text-tools/text-to-base64.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Convert text into Base64 encoding structure for binary safe transfers."
  },
  {
    "name": "Base64 To Text",
    "url": "text-tools/base64-to-text.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Decode Base64 encoded strings back into readable text format."
  },
  {
    "name": "Text To Morse Code",
    "url": "text-tools/text-to-morse-code.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Translate plain text letters and numbers to international Morse code."
  },
  {
    "name": "Morse Code To Text",
    "url": "text-tools/morse-code-to-text.html",
    "category": "Text Tools (Text Converters)",
    "desc": "Translate international Morse code (dots and dashes) back to plain text."
  },
  {
    "name": "Text To Slug",
    "url": "text-tools/text-to-slug.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Convert text headings into clean, SEO-friendly URL slug strings."
  },
  {
    "name": "URL Slug Generator",
    "url": "text-tools/url-slug-generator.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Generate web-optimized slugs for articles, pages, or routes."
  },
  {
    "name": "URL Encoder",
    "url": "text-tools/url-encoder.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Encode text string components to standard percent-encoded URL formats."
  },
  {
    "name": "URL Decoder",
    "url": "text-tools/url-decoder.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Decode percent-encoded URL components back to standard plain text."
  },
  {
    "name": "HTML Encoder",
    "url": "text-tools/html-encoder.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Convert special HTML characters like tags into escaped HTML entities."
  },
  {
    "name": "HTML Decoder",
    "url": "text-tools/html-decoder.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Decode HTML entities (e.g. &amp;lt;) back to standard raw tags."
  },
  {
    "name": "Unicode Encoder",
    "url": "text-tools/unicode-encoder.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Encode standard text strings to unicode code point format (\\uXXXX)."
  },
  {
    "name": "Unicode Decoder",
    "url": "text-tools/unicode-decoder.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Decode unicode escaped code points (\\uXXXX) back to normal text."
  },
  {
    "name": "Escape Text Tool",
    "url": "text-tools/escape-text-tool.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Escape programming variables by adding backslashes to quotes and slashes."
  },
  {
    "name": "Unescape Text Tool",
    "url": "text-tools/unescape-text-tool.html",
    "category": "Text Tools (URL & Encoding Tools)",
    "desc": "Unescape programming strings by removing double backslashes and quotes escapes."
  },
  {
    "name": "Random Word Generator",
    "url": "text-tools/random-word-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate lists of random English words for vocabulary practice or games."
  },
  {
    "name": "Random Sentence Generator",
    "url": "text-tools/random-sentence-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate random grammatical sentences for writers and bloggers."
  },
  {
    "name": "Random Paragraph Generator",
    "url": "text-tools/random-paragraph-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate paragraphs of randomized placeholder text."
  },
  {
    "name": "Random Quote Generator",
    "url": "text-tools/random-quote-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate inspiring quotes from historical figures and famous writers."
  },
  {
    "name": "Lorem Ipsum Generator",
    "url": "text-tools/lorem-ipsum-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate classic Lorem Ipsum dummy text for layouts and mocks."
  },
  {
    "name": "Dummy Text Generator",
    "url": "text-tools/dummy-text-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate custom placeholder text in English for web development."
  },
  {
    "name": "Random Username Generator",
    "url": "text-tools/random-username-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate cool and secure random usernames for accounts and games."
  },
  {
    "name": "Random Story Prompt Generator",
    "url": "text-tools/random-story-prompt-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Get creative writing prompts and story starters to beat writer's block."
  },
  {
    "name": "Random Topic Generator",
    "url": "text-tools/random-topic-generator.html",
    "category": "Text Tools (Random Generators)",
    "desc": "Generate discussion topics and speech subjects randomly."
  },
  {
    "name": "Palindrome Checker",
    "url": "text-tools/palindrome-checker.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Check if your word, sentence, or phrase reads the same backward as forward."
  },
  {
    "name": "Anagram Generator",
    "url": "text-tools/anagram-generator.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Find and generate anagrams by rearranging letters of a word."
  },
  {
    "name": "Text Comparison Tool",
    "url": "text-tools/text-comparison-tool.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Compare two blocks of text side-by-side to highlight similarities."
  },
  {
    "name": "Diff Checker",
    "url": "text-tools/diff-checker.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Check line differences between two code or text documents."
  },
  {
    "name": "Duplicate Word Finder",
    "url": "text-tools/duplicate-word-finder.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Find and list all words that appear more than once in your text."
  },
  {
    "name": "Keyword Counter",
    "url": "text-tools/keyword-counter.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Count exact occurrences of specific keywords in your copy."
  },
  {
    "name": "Text Statistics Tool",
    "url": "text-tools/text-statistics-tool.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Generate complete structural statistics for a text document."
  },
  {
    "name": "Word Frequency Analyzer",
    "url": "text-tools/word-frequency-analyzer.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Analyze and audit how often each word is used in text block."
  },
  {
    "name": "Text Compression Tool",
    "url": "text-tools/text-compression-tool.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Simulate and test text compression sizes using simple LZW rules."
  },
  {
    "name": "Text Expansion Tool",
    "url": "text-tools/text-expansion-tool.html",
    "category": "Text Tools (Advanced Text Tools)",
    "desc": "Expand standard writing shorthand (e.g. btw) into full phrases."
  },
  {
    "name": "Grammar Checker",
    "url": "text-tools/grammar-checker.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Scan and fix common grammar issues like double spaces and bad capitalization."
  },
  {
    "name": "Spell Checker",
    "url": "text-tools/spell-checker.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Check and autocorrect common spelling mistakes in your copy."
  },
  {
    "name": "Text Summarizer",
    "url": "text-tools/text-summarizer.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Summarize long articles into a few bullet points based on key terms."
  },
  {
    "name": "Blog Outline Generator",
    "url": "text-tools/blog-outline-generator.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Generate structured blog headings (H2, H3) outline for writers."
  },
  {
    "name": "FAQ Generator",
    "url": "text-tools/faq-generator.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Create standard, search-friendly FAQ questions for your blog post."
  },
  {
    "name": "Content Idea Generator",
    "url": "text-tools/content-idea-generator.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Get multiple content and article ideas from keywords."
  },
  {
    "name": "Hook Generator",
    "url": "text-tools/hook-generator.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Generate attention-grabbing opening hooks for posts and essays."
  },
  {
    "name": "Call To Action Generator",
    "url": "text-tools/call-to-action-generator.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Generate high-converting Call To Action (CTA) phrases for marketing."
  },
  {
    "name": "Email Subject Line Generator",
    "url": "text-tools/email-subject-generator.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Generate high open-rate email subject lines from topics."
  },
  {
    "name": "Content Improver",
    "url": "text-tools/content-improver.html",
    "category": "Text Tools (AI Content Tools)",
    "desc": "Upgrade weak writing by adding strong verbs and clean sentence links."
  },
  {
    "name": "Password Generator",
    "url": "security-tools/password-generator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Generate strong, secure, and customizable passwords to protect your online accounts."
  },
  {
    "name": "Password Strength Checker",
    "url": "security-tools/password-strength-checker.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Check the strength and security level of your password against common patterns."
  },
  {
    "name": "Password Entropy Calculator",
    "url": "security-tools/password-entropy-calculator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Calculate the mathematical entropy (strength in bits) of any given password."
  },
  {
    "name": "Random Password Generator",
    "url": "security-tools/random-password-generator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Quickly generate random high-strength passwords with customizable rules."
  },
  {
    "name": "Secure Passphrase Generator",
    "url": "security-tools/secure-passphrase-generator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Generate memorable yet highly secure passphrases using Diceware-style random wordlists."
  },
  {
    "name": "Password Hash Generator",
    "url": "security-tools/password-hash-generator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Securely hash your passwords client-side using MD5, SHA-1, SHA-256, or SHA-512 algorithms."
  },
  {
    "name": "Password Leak Checker",
    "url": "security-tools/password-leak-checker.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Check if your password has been exposed in a data breach safely using HIBP k-Anonymity."
  },
  {
    "name": "Password Complexity Checker",
    "url": "security-tools/password-complexity-checker.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Check the complexity requirements of your password, evaluating character variety, length, and repeats."
  },
  {
    "name": "Password Policy Generator",
    "url": "security-tools/password-policy-generator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Create robust corporate or application password policies to ensure your users choose strong keys."
  },
  {
    "name": "Bulk Password Generator",
    "url": "security-tools/bulk-password-generator.html",
    "category": "Security Tools (Password Tools)",
    "desc": "Generate multiple secure passwords at once for servers, user migrations, or bulk creation."
  },
  {
    "name": "MD5 Hash Generator",
    "url": "security-tools/md5-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate a 128-bit MD5 checksum of any text input for data integrity checks."
  },
  {
    "name": "SHA1 Hash Generator",
    "url": "security-tools/sha1-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate a 160-bit SHA-1 cryptographic hash of your text in your browser."
  },
  {
    "name": "SHA224 Hash Generator",
    "url": "security-tools/sha224-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate a SHA-224 hash value of your text instantly."
  },
  {
    "name": "SHA256 Hash Generator",
    "url": "security-tools/sha256-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate secure 256-bit SHA-256 hashes of your text strings client-side."
  },
  {
    "name": "SHA384 Hash Generator",
    "url": "security-tools/sha384-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate secure 384-bit SHA-384 hashes of your text strings client-side."
  },
  {
    "name": "SHA512 Hash Generator",
    "url": "security-tools/sha512-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate secure 512-bit SHA-512 hashes of your text strings client-side."
  },
  {
    "name": "HMAC Generator",
    "url": "security-tools/hmac-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Calculate Hash-based Message Authentication Codes (HMAC) using standard hash ciphers."
  },
  {
    "name": "File Hash Generator",
    "url": "security-tools/file-hash-generator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Generate hashes and checksums of local files safely without uploading them to any servers."
  },
  {
    "name": "Checksum Calculator",
    "url": "security-tools/checksum-calculator.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Calculate standard CRC-32 and Adler-32 checksums of any input text block."
  },
  {
    "name": "Hash Comparison Tool",
    "url": "security-tools/hash-comparison-tool.html",
    "category": "Security Tools (Hash Generators)",
    "desc": "Compare two cryptographic hashes to check if they match (integrity verification)."
  },
  {
    "name": "Base64 Encoder",
    "url": "security-tools/base64-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Encode raw text strings into Base64 format safely in your browser."
  },
  {
    "name": "Base64 Decoder",
    "url": "security-tools/base64-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode Base64 encoded strings back to plain text format locally."
  },
  {
    "name": "URL Encoder",
    "url": "security-tools/url-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Encode text strings to make them safe for URL queries and parameters."
  },
  {
    "name": "URL Decoder",
    "url": "security-tools/url-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode URL-encoded parameters back into clear text."
  },
  {
    "name": "HTML Encoder",
    "url": "security-tools/html-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Convert special HTML characters like <, >, and & into secure HTML entity equivalents."
  },
  {
    "name": "HTML Decoder",
    "url": "security-tools/html-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode escaped HTML entities back into plain characters."
  },
  {
    "name": "Unicode Encoder",
    "url": "security-tools/unicode-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Convert text characters into unicode escape sequences (e.g., \\uXXXX) easily."
  },
  {
    "name": "Unicode Decoder",
    "url": "security-tools/unicode-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode unicode hex sequences (\\uXXXX) back to standard readable text."
  },
  {
    "name": "ASCII Encoder",
    "url": "security-tools/ascii-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Convert text strings to their decimal ASCII numerical values."
  },
  {
    "name": "ASCII Decoder",
    "url": "security-tools/ascii-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Convert decimal ASCII codes back to clear readable text characters."
  },
  {
    "name": "Binary Encoder",
    "url": "security-tools/binary-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Convert your plain text characters into standard 8-bit binary representation."
  },
  {
    "name": "Binary Decoder",
    "url": "security-tools/binary-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode base-2 binary strings (8-bit blocks) back to clear text representation."
  },
  {
    "name": "Hex Encoder",
    "url": "security-tools/hex-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Convert clear text strings into hexadecimal representation (base-16)."
  },
  {
    "name": "Hex Decoder",
    "url": "security-tools/hex-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode hexadecimal codes (base-16) back to clear plain text representation."
  },
  {
    "name": "ROT13 Encoder",
    "url": "security-tools/rot13-encoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Encode your text by shifting letters by 13 spaces along the alphabet."
  },
  {
    "name": "ROT13 Decoder",
    "url": "security-tools/rot13-decoder.html",
    "category": "Security Tools (Encoding & Decoding Tools)",
    "desc": "Decode ROT13 text back to its original readable format."
  },
  {
    "name": "UUID Generator",
    "url": "security-tools/uuid-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate cryptographically secure RFC 4122 Version 4 UUIDs instantly."
  },
  {
    "name": "UUID Validator",
    "url": "security-tools/uuid-validator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Validate UUIDs to ensure they comply with standard RFC 4122 formatting rules."
  },
  {
    "name": "Random Token Generator",
    "url": "security-tools/random-token-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate high-entropy random tokens in HEX, Base64, or Alphanumeric formats."
  },
  {
    "name": "API Key Generator",
    "url": "security-tools/api-key-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate custom API keys with configurable prefixes (e.g. ew_live_...) for your software services."
  },
  {
    "name": "Secret Key Generator",
    "url": "security-tools/secret-key-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate high-entropy random secret keys for session cookies, Django, Flask, or Node applications."
  },
  {
    "name": "Encryption Key Generator",
    "url": "security-tools/encryption-key-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate secure symmetric encryption keys from passwords using PBKDF2 key derivation."
  },
  {
    "name": "JWT Generator",
    "url": "security-tools/jwt-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate custom JSON Web Tokens (JWT) signed with HS256 (HMAC-SHA256) instantly."
  },
  {
    "name": "JWT Decoder",
    "url": "security-tools/jwt-decoder.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Decode JSON Web Tokens (JWT) client-side to inspect the header and payload properties."
  },
  {
    "name": "JWT Validator",
    "url": "security-tools/jwt-validator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Validate JSON Web Token (JWT) signatures and check their expiration properties."
  },
  {
    "name": "Session ID Generator",
    "url": "security-tools/session-id-generator.html",
    "category": "Security Tools (Token & Key Generators)",
    "desc": "Generate secure session identifiers to handle active connection logs safely."
  },
  {
    "name": "AES Encryption Tool",
    "url": "security-tools/aes-encryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Encrypt your sensitive messages client-side using the Advanced Encryption Standard (AES)."
  },
  {
    "name": "AES Decryption Tool",
    "url": "security-tools/aes-decryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Decrypt AES-encrypted ciphertext back to clear text using the secret key."
  },
  {
    "name": "DES Encryption Tool",
    "url": "security-tools/des-encryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Encrypt text using the historical Data Encryption Standard (DES) algorithm."
  },
  {
    "name": "DES Decryption Tool",
    "url": "security-tools/des-decryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Decrypt DES-encrypted ciphertext back to clear text using the secret key."
  },
  {
    "name": "Triple DES Encryption Tool",
    "url": "security-tools/triple-des-encryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Encrypt text using Triple DES (3DES) which applies DES three times for stronger security."
  },
  {
    "name": "RSA Key Pair Generator",
    "url": "security-tools/rsa-key-pair-generator.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Generate strong, secure RSA Public and Private key pairs in PEM format client-side."
  },
  {
    "name": "RSA Encrypt Tool",
    "url": "security-tools/rsa-encrypt-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Encrypt text strings with a recipient's RSA Public Key in PEM format."
  },
  {
    "name": "RSA Decrypt Tool",
    "url": "security-tools/rsa-decrypt-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Decrypt RSA-encrypted ciphertext using your RSA Private Key."
  },
  {
    "name": "Text Encryption Tool",
    "url": "security-tools/text-encryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Encrypt text strings instantly using key-based standard symmetric AES cipher."
  },
  {
    "name": "Text Decryption Tool",
    "url": "security-tools/text-decryption-tool.html",
    "category": "Security Tools (Encryption Tools)",
    "desc": "Decrypt your encrypted text block back to readable text with the correct key."
  },
  {
    "name": "Password Security Analyzer",
    "url": "security-tools/password-security-analyzer.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Perform a deep security inspection of any password, identifying entropy and security issues."
  },
  {
    "name": "Entropy Calculator",
    "url": "security-tools/entropy-calculator.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Calculate the Shannon entropy of any text block to measure its randomness or complexity."
  },
  {
    "name": "Hash Analyzer",
    "url": "security-tools/hash-analyzer.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Identify potential hash algorithms (like MD5, SHA-256, etc.) based on hash patterns."
  },
  {
    "name": "Token Inspector",
    "url": "security-tools/token-inspector.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Inspect random tokens to estimate key size, encoding format, and entropy level."
  },
  {
    "name": "JWT Inspector",
    "url": "security-tools/jwt-inspector.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Inspect JWT structures and break down payload properties safely client-side."
  },
  {
    "name": "Security Header Checker",
    "url": "security-tools/security-header-checker.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Analyze security headers pasted from your server response to verify protection status."
  },
  {
    "name": "SSL Certificate Checker",
    "url": "security-tools/ssl-certificate-checker.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Check and verify SSL certificate details of any website to audit expiration and domain names."
  },
  {
    "name": "SSL Decoder",
    "url": "security-tools/ssl-decoder.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Decode raw PEM SSL certificates to view readable domain names, validity dates, and issuer."
  },
  {
    "name": "Public Key Inspector",
    "url": "security-tools/public-key-inspector.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Inspect public key files in PEM format to verify key sizes, exponents, and validity."
  },
  {
    "name": "Certificate Viewer",
    "url": "security-tools/certificate-viewer.html",
    "category": "Security Tools (Security Analysis Tools)",
    "desc": "Load and inspect certificate files to view subject names, validity periods, and issuer information."
  },
  {
    "name": "IP Address Lookup",
    "url": "security-tools/ip-address-lookup.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Lookup your public IP address or query custom IPs to retrieve location, ISP, and ASN data."
  },
  {
    "name": "IP Address Validator",
    "url": "security-tools/ip-address-validator.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Check if an IP address string is a valid IPv4 or IPv6 address."
  },
  {
    "name": "IPv4 Validator",
    "url": "security-tools/ipv4-validator.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Check if a string matches the dot-decimal IPv4 address format (0.0.0.0 to 255.255.255.255)."
  },
  {
    "name": "IPv6 Validator",
    "url": "security-tools/ipv6-validator.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Verify if an address string is formatted correctly according to IPv6 syntax protocols."
  },
  {
    "name": "Subnet Calculator",
    "url": "security-tools/subnet-calculator.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Calculate subnets, network IPs, broadcast ranges, and mask parameters for your networks."
  },
  {
    "name": "CIDR Calculator",
    "url": "security-tools/cidr-calculator.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Calculate CIDR parameters, mask digits, and wildcard conversions."
  },
  {
    "name": "DNS Lookup",
    "url": "security-tools/dns-lookup.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Query domain DNS records (A, MX, TXT, CNAME) instantly using Cloudflare's secure DNS-over-HTTPS API."
  },
  {
    "name": "Reverse DNS Lookup",
    "url": "security-tools/reverse-dns-lookup.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Lookup hostnames linked to a public IP using Reverse DNS (PTR query)."
  },
  {
    "name": "WHOIS Lookup",
    "url": "security-tools/whois-lookup.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Check domain registration dates, name servers, and ownership details."
  },
  {
    "name": "Port Scanner Simulator",
    "url": "security-tools/port-scanner-simulator.html",
    "category": "Security Tools (Network Security Tools)",
    "desc": "Simulate and study network port scans to identify open/closed services on network nodes."
  },
  {
    "name": "CSRF Token Generator",
    "url": "security-tools/csrf-token-generator.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Generate strong, unique, cryptographically secure CSRF tokens to secure web forms against forgery attacks."
  },
  {
    "name": "CSP Header Generator",
    "url": "security-tools/csp-header-generator.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Generate Content Security Policy (CSP) headers to defend against script injection attacks."
  },
  {
    "name": "Secure Cookie Generator",
    "url": "security-tools/secure-cookie-generator.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Generate robust Set-Cookie header directives with Secure, HttpOnly, and SameSite attributes."
  },
  {
    "name": "Security Headers Generator",
    "url": "security-tools/security-headers-generator.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Compile server security headers into simple configurations for Nginx, Apache, or IIS."
  },
  {
    "name": "Robots.txt Validator",
    "url": "security-tools/robots-txt-validator.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Check robots.txt file formatting directives to verify compliance with crawler standards."
  },
  {
    "name": "Open Graph Validator",
    "url": "security-tools/open-graph-validator.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Validate Open Graph tags pasted from your site HTML headers."
  },
  {
    "name": "HTTP Header Viewer",
    "url": "security-tools/http-header-viewer.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Parse and view raw HTTP response headers in structured tabular format."
  },
  {
    "name": "HTTP Status Checker",
    "url": "security-tools/http-status-checker.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Check the HTTP status codes, meanings, and specifications for standard codes."
  },
  {
    "name": "URL Safety Checker",
    "url": "security-tools/url-safety-checker.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Check URLs client-side against safety patterns and common phishing indicators."
  },
  {
    "name": "Redirect Checker",
    "url": "security-tools/redirect-checker.html",
    "category": "Security Tools (Web Security Tools)",
    "desc": "Audit URL redirects and study status codes link jumps."
  },
  {
    "name": "OAuth Token Viewer",
    "url": "security-tools/oauth-token-viewer.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Inspect and view JWT claims, scopes, and validity information from standard OAuth 2.0 access tokens."
  },
  {
    "name": "API Request Signer",
    "url": "security-tools/api-request-signer.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Sign your API payloads with a timestamp and secret key using HMAC SHA-256 for secure integrations."
  },
  {
    "name": "Signature Generator",
    "url": "security-tools/signature-generator.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Generate cryptographic signatures of messages using HMAC or RSA key signing."
  },
  {
    "name": "Signature Verifier",
    "url": "security-tools/signature-verifier.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Verify cryptographic signatures of messages against their key and payload values."
  },
  {
    "name": "JSON Web Key Generator",
    "url": "security-tools/json-web-key-generator.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Generate JWK representations from standard PEM public key formats."
  },
  {
    "name": "PEM Formatter",
    "url": "security-tools/pem-formatter.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Format raw base64 key strings into valid 64-character column PEM key formats."
  },
  {
    "name": "PEM Decoder",
    "url": "security-tools/pem-decoder.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Decode PEM files back to their raw unformatted Base64 strings."
  },
  {
    "name": "PEM Validator",
    "url": "security-tools/pem-validator.html",
    "category": "Security Tools (Developer Security Tools)",
    "desc": "Verify if a PEM key or certificate is validly formatted and check its block tags."
  },
  {
    "name": "Metadata Remover",
    "url": "security-tools/metadata-remover.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Strip hidden metadata from your text files to prevent leaking author, time, or system details."
  },
  {
    "name": "Email Obfuscator",
    "url": "security-tools/email-obfuscator.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Obfuscate email addresses into HTML entities to prevent bots and spammers from scraping them."
  },
  {
    "name": "Phone Number Masker",
    "url": "security-tools/phone-number-masker.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Mask digits of phone numbers to hide details while retaining format."
  },
  {
    "name": "Text Redaction Tool",
    "url": "security-tools/text-redaction-tool.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Redact custom target words or phrases from text blocks automatically."
  },
  {
    "name": "PII Detector",
    "url": "security-tools/pii-detector.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Scan text blocks to locate and highlight Personally Identifiable Information (PII)."
  },
  {
    "name": "Sensitive Data Scanner",
    "url": "security-tools/sensitive-data-scanner.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Scan logs, configs, or codes to locate API keys, database credentials, or secret variables."
  },
  {
    "name": "Privacy Text Cleaner",
    "url": "security-tools/privacy-text-cleaner.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Clean IP addresses, emails, and phone numbers from logs before publishing."
  },
  {
    "name": "Secure Notes Generator",
    "url": "security-tools/secure-notes-generator.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Create encrypted notes client-side that can only be unlocked with a custom passphrase."
  },
  {
    "name": "Anonymous ID Generator",
    "url": "security-tools/anonymous-id-generator.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Generate anonymous, non-trackable UUID identifiers for databases or analytics tracking."
  },
  {
    "name": "Random Identity Generator",
    "url": "security-tools/random-identity-generator.html",
    "category": "Security Tools (Privacy Tools)",
    "desc": "Generate complete random fake identity personas (name, address, telephone) for testing layouts."
  },
  {
    "name": "Caesar Cipher Encoder",
    "url": "security-tools/caesar-cipher-encoder.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Encode messages by shifting alphabet letters using the classic Caesar Cipher."
  },
  {
    "name": "Caesar Cipher Decoder",
    "url": "security-tools/caesar-cipher-decoder.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Decode Caesar Cipher messages by shifting alphabet letters backwards."
  },
  {
    "name": "Vigenere Cipher Encoder",
    "url": "security-tools/vigenere-cipher-encoder.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Encode your text messages using the polyalphabetic Vigenere Cipher with a key phrase."
  },
  {
    "name": "Vigenere Cipher Decoder",
    "url": "security-tools/vigenere-cipher-decoder.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Decode Vigenere Cipher messages using the key phrase."
  },
  {
    "name": "Morse Code Encoder",
    "url": "security-tools/morse-code-encoder.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Translate plain text into standard Morse Code dashes and dots."
  },
  {
    "name": "Morse Code Decoder",
    "url": "security-tools/morse-code-decoder.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Translate standard Morse Code (dots and dashes) back to plain readable text."
  },
  {
    "name": "Rail Fence Cipher Tool",
    "url": "security-tools/rail-fence-cipher-tool.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Encode or decode text using the Rail Fence transposition cipher technique."
  },
  {
    "name": "Atbash Cipher Tool",
    "url": "security-tools/atbash-cipher-tool.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Encode or decode text using the Atbash substitution cipher (reversing alphabet positions)."
  },
  {
    "name": "Affine Cipher Tool",
    "url": "security-tools/affine-cipher-tool.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Encrypt or decrypt text using the mathematical Affine Cipher parameters."
  },
  {
    "name": "Playfair Cipher Tool",
    "url": "security-tools/playfair-cipher-tool.html",
    "category": "Security Tools (Cryptography Tools)",
    "desc": "Encode or decode messages using the historical Playfair double-letter diagram cipher."
  },
  {
    "name": "Image Resizer",
    "url": "image-tools/image-resizer.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Resize your images to custom dimensions (width and height) in pixels in your browser."
  },
  {
    "name": "Image Cropper",
    "url": "image-tools/image-cropper.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Crop and cut specific sections of your images by defining custom coordinates."
  },
  {
    "name": "Image Rotator",
    "url": "image-tools/image-rotator.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Rotate your images by 90, 180, or 270 degrees client-side."
  },
  {
    "name": "Image Flipper",
    "url": "image-tools/image-flipper.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Flip your images horizontally or vertically instantly."
  },
  {
    "name": "Image Compressor",
    "url": "image-tools/image-compressor.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Compress and reduce the file size of your JPEG, PNG, or WebP images client-side."
  },
  {
    "name": "Image Enhancer",
    "url": "image-tools/image-enhancer.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Enhance your photos by dynamically adjusting brightness, contrast, and saturation."
  },
  {
    "name": "Image Sharpener",
    "url": "image-tools/image-sharpener.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Sharpen details and edges in your image using canvas convolution filter matrices."
  },
  {
    "name": "Image Blur Tool",
    "url": "image-tools/image-blur-tool.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Blur your photos and images using client-side canvas filters."
  },
  {
    "name": "Image Brightness Adjuster",
    "url": "image-tools/image-brightness-adjuster.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Adjust and fine-tune image brightness levels client-side."
  },
  {
    "name": "Image Contrast Adjuster",
    "url": "image-tools/image-contrast-adjuster.html",
    "category": "Image Tools (Image Editing Tools)",
    "desc": "Increase or decrease contrast settings of your pictures in real-time."
  },
  {
    "name": "JPG to PNG Converter",
    "url": "image-tools/jpg-to-png-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert JPG and JPEG images to PNG format offline in your browser."
  },
  {
    "name": "PNG to JPG Converter",
    "url": "image-tools/png-to-jpg-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert PNG images to JPG format client-side, adjusting compression qualities."
  },
  {
    "name": "WebP to JPG Converter",
    "url": "image-tools/webp-to-jpg-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert WebP images to JPG format for wider application compatibility."
  },
  {
    "name": "JPG to WebP Converter",
    "url": "image-tools/jpg-to-webp-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert JPG photos to highly-efficient WebP images for optimal web performance."
  },
  {
    "name": "PNG to WebP Converter",
    "url": "image-tools/png-to-webp-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert lossless PNG images to WebP format client-side."
  },
  {
    "name": "WebP to PNG Converter",
    "url": "image-tools/webp-to-png-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert WebP images to lossless PNG format with transparent alpha channels."
  },
  {
    "name": "BMP to PNG Converter",
    "url": "image-tools/bmp-to-png-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert uncompressed BMP bitmaps to standard Web-friendly PNG images."
  },
  {
    "name": "TIFF to JPG Converter",
    "url": "image-tools/tiff-to-jpg-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert TIFF print graphics to standard JPG images client-side."
  },
  {
    "name": "SVG to PNG Converter",
    "url": "image-tools/svg-to-png-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Render XML-based SVG vectors into static, high-resolution PNG images."
  },
  {
    "name": "HEIC to JPG Converter",
    "url": "image-tools/heic-to-jpg-converter.html",
    "category": "Image Tools (Image Converter Tools)",
    "desc": "Convert iPhone HEIC photos to standard JPG images directly in your browser."
  },
  {
    "name": "Bulk Image Compressor",
    "url": "image-tools/bulk-image-compressor.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Compress multiple images at once client-side and download them one by one."
  },
  {
    "name": "Image Quality Reducer",
    "url": "image-tools/image-quality-reducer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Reduce image file size by scaling down the JPEG/WebP encoding quality values."
  },
  {
    "name": "Image Size Reducer",
    "url": "image-tools/image-size-reducer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Reduce the resolution and dimensions of your image to lower the storage footprint."
  },
  {
    "name": "Lossless Image Optimizer",
    "url": "image-tools/lossless-image-optimizer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Optimize images by stripping hidden metadata headers without altering pixel values."
  },
  {
    "name": "Web Image Optimizer",
    "url": "image-tools/web-image-optimizer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Optimize your image specifically for fast loading on websites."
  },
  {
    "name": "Social Media Image Optimizer",
    "url": "image-tools/social-media-image-optimizer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Optimize your images for Facebook, Instagram, and Twitter sizing parameters."
  },
  {
    "name": "SEO Image Optimizer",
    "url": "image-tools/seo-image-optimizer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Optimize images to follow Google SEO page speed and naming suggestions."
  },
  {
    "name": "Progressive JPG Generator",
    "url": "image-tools/progressive-jpg-generator.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Generate progressive JPEGs that load sequentially on web servers."
  },
  {
    "name": "WebP Optimizer",
    "url": "image-tools/webp-optimizer.html",
    "category": "Image Tools (Image Optimization Tools)",
    "desc": "Further optimize and recompress WebP images to match target size requirements."
  },
  {
    "name": "Image to Base64",
    "url": "image-tools/image-to-base64.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Convert local PNG, JPG, or SVG image files into Base64 code strings for coding."
  },
  {
    "name": "Base64 to Image",
    "url": "image-tools/base64-to-image.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Reconstruct a Base64 text string back into a downloadable image file."
  },
  {
    "name": "Image to Data URI",
    "url": "image-tools/image-to-data-uri.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Convert images into standard HTML Data URIs (data:image/...) for direct embedding."
  },
  {
    "name": "Data URI Generator",
    "url": "image-tools/data-uri-generator.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Generate custom Data URI schemes from code parameters and image bytes."
  },
  {
    "name": "Image to ASCII Art",
    "url": "image-tools/image-to-ascii-art.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Convert your photos and graphics into text-based ASCII art character maps."
  },
  {
    "name": "Image to SVG Converter",
    "url": "image-tools/image-to-svg-converter.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Wrap or trace images client-side into scalable SVG XML code templates."
  },
  {
    "name": "Image to Text (OCR)",
    "url": "image-tools/image-to-text-ocr.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Extract text lines from your images and photos locally using Tesseract OCR."
  },
  {
    "name": "Text to Image Generator",
    "url": "image-tools/text-to-image-generator.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Generate custom banners and photos with text overlays rendered onto Canvas."
  },
  {
    "name": "Image Metadata Viewer",
    "url": "image-tools/image-metadata-viewer.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "View EXIF and metadata information inside JPEG image headers client-side."
  },
  {
    "name": "Image Metadata Remover",
    "url": "image-tools/image-metadata-remover.html",
    "category": "Image Tools (Image Conversion & Encoding Tools)",
    "desc": "Strip sensitive EXIF metadata from JPEG files to protect your privacy."
  },
  {
    "name": "YouTube Thumbnail Downloader",
    "url": "image-tools/youtube-thumbnail-downloader.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Extract and download high-resolution cover thumbnails of any YouTube video."
  },
  {
    "name": "YouTube Thumbnail Creator",
    "url": "image-tools/youtube-thumbnail-creator.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Create standard 1280x720 YouTube video covers with text overlays client-side."
  },
  {
    "name": "Instagram Photo Resizer",
    "url": "image-tools/instagram-photo-resizer.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Resize your images to Instagram's standard 1080x1080 square format."
  },
  {
    "name": "Instagram Story Resizer",
    "url": "image-tools/instagram-story-resizer.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Scale and crop your images into Instagram's vertical 1080x1920 Story format."
  },
  {
    "name": "Instagram Profile Picture Downloader",
    "url": "image-tools/instagram-profile-picture-downloader.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Simulate and download profile picture assets for layouts."
  },
  {
    "name": "Facebook Cover Photo Maker",
    "url": "image-tools/facebook-cover-photo-maker.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Create Facebook Page cover banners with custom colors and titles (820x312 px)."
  },
  {
    "name": "Facebook Post Resizer",
    "url": "image-tools/facebook-post-resizer.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Resize your images to match Facebook feed post dimensions (1200x630 px)."
  },
  {
    "name": "Twitter/X Image Resizer",
    "url": "image-tools/twitter-image-resizer.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Scale and crop your graphics for Twitter/X feed displays (1200x675 px)."
  },
  {
    "name": "LinkedIn Banner Maker",
    "url": "image-tools/linkedin-banner-maker.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Design corporate LinkedIn profile headers matching the standard 1584x396 dimensions."
  },
  {
    "name": "Pinterest Pin Resizer",
    "url": "image-tools/pinterest-pin-resizer.html",
    "category": "Image Tools (Social Media Image Tools)",
    "desc": "Convert and scale your images for Pinterest Pins matching 1000x1500 px."
  },
  {
    "name": "Color Picker",
    "url": "image-tools/color-picker.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Select colors interactively and translate between HEX, RGB, HSL, and CMYK formats."
  },
  {
    "name": "Color Palette Generator",
    "url": "image-tools/color-palette-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate cohesive color palettes based on complementary or analogous color rules."
  },
  {
    "name": "Gradient Generator",
    "url": "image-tools/gradient-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate CSS gradient code lines and preview them in real-time."
  },
  {
    "name": "CSS Gradient Generator",
    "url": "image-tools/css-gradient-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate custom linear-gradient and radial-gradient rules for your style sheets."
  },
  {
    "name": "Favicon Generator",
    "url": "image-tools/favicon-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Convert local PNG images into 16x16 or 32x32 favicon formats."
  },
  {
    "name": "Logo Size Generator",
    "url": "image-tools/logo-size-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate brand logo variations in standard square and rectangular sizes."
  },
  {
    "name": "Brand Color Generator",
    "url": "image-tools/brand-color-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Create a design system from a brand color, showing primary, secondary, and neutral shades."
  },
  {
    "name": "Background Generator",
    "url": "image-tools/background-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate geometric wallpaper backgrounds on a canvas for screens."
  },
  {
    "name": "Pattern Generator",
    "url": "image-tools/pattern-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate repeating grid patterns (dots, diagonal lines) and output download files."
  },
  {
    "name": "Icon Generator",
    "url": "image-tools/icon-generator.html",
    "category": "Image Tools (Design Tools)",
    "desc": "Generate custom square app icons with text overlays and background gradients."
  },
  {
    "name": "Screenshot to Text (OCR)",
    "url": "image-tools/screenshot-to-text-ocr.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Extract printed or handwritten text from uploaded screenshots using offline client-side OCR."
  },
  {
    "name": "Screenshot Cropper",
    "url": "image-tools/screenshot-cropper.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Crop and trim your screenshots to keep only essential parts client-side."
  },
  {
    "name": "Screenshot Annotator",
    "url": "image-tools/screenshot-annotator.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Draw boxes, write text notes, or add arrows on screenshots before sharing."
  },
  {
    "name": "Image Markup Tool",
    "url": "image-tools/image-markup-tool.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Add professional markup, highlights, and border elements to screenshots."
  },
  {
    "name": "Screen Resolution Checker",
    "url": "image-tools/screen-resolution-checker.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Check your physical screen size, active monitor resolution, and pixel depth instantly."
  },
  {
    "name": "Screenshot Compressor",
    "url": "image-tools/screenshot-compressor.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Compress your heavy PNG screenshot files into compact formats client-side."
  },
  {
    "name": "Screenshot Converter",
    "url": "image-tools/screenshot-converter.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Convert screenshots between PNG, JPEG, and WebP formats instantly."
  },
  {
    "name": "Website Screenshot Tool",
    "url": "image-tools/website-screenshot-tool.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Generate mockup screenshots of websites using a premium browser shell outline."
  },
  {
    "name": "Full Page Screenshot Tool",
    "url": "image-tools/full-page-screenshot-tool.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Format and scale vertical screenshots into standard full-page website templates."
  },
  {
    "name": "Screenshot Optimizer",
    "url": "image-tools/screenshot-optimizer.html",
    "category": "Image Tools (Screenshot & Capture Tools)",
    "desc": "Optimize screenshot dimensions and formats for web sharing, emails, and bug reports."
  },
  {
    "name": "Watermark Image Tool",
    "url": "image-tools/watermark-image-tool.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Add secure text watermarks to your photographs or drawings client-side."
  },
  {
    "name": "Add Text Watermark",
    "url": "image-tools/add-text-watermark.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Stamp customizable copyright, brand, or name strings as text watermarks on images."
  },
  {
    "name": "Add Logo Watermark",
    "url": "image-tools/add-logo-watermark.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Overlay secondary branding logo images as image watermarks."
  },
  {
    "name": "Remove Watermark Area Tool",
    "url": "image-tools/remove-watermark-area-tool.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Blur or pixelate selected watermark regions to sanitize image templates."
  },
  {
    "name": "Batch Watermark Tool",
    "url": "image-tools/batch-watermark-tool.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Configure and preview text watermarks to apply to batch image collections."
  },
  {
    "name": "Copyright Watermark Generator",
    "url": "image-tools/copyright-watermark-generator.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Generate custom copyright stamps on digital images."
  },
  {
    "name": "Transparent Watermark Creator",
    "url": "image-tools/transparent-watermark-creator.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Create transparent overlay watermarks that blend smoothly with graphic assets."
  },
  {
    "name": "Signature Watermark Tool",
    "url": "image-tools/signature-watermark-tool.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Stamp stylized cursive signature lines to protect document scans and contracts."
  },
  {
    "name": "Social Media Watermark Tool",
    "url": "image-tools/social-media-watermark-tool.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Stamp your social handles (like @username) to prevent asset piracy."
  },
  {
    "name": "Custom Watermark Generator",
    "url": "image-tools/custom-watermark-generator.html",
    "category": "Image Tools (Watermark Tools)",
    "desc": "Generate custom watermarks with granular positioning, transparency, and sizes."
  },
  {
    "name": "Passport Photo Maker",
    "url": "image-tools/passport-photo-maker.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Crop and format your photographs into official 2x2 inch (600x600 px) passport sizes with standard background fills."
  },
  {
    "name": "ID Photo Maker",
    "url": "image-tools/id-photo-maker.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Scale and format portraits into standardized ID Card dimensions."
  },
  {
    "name": "Photo Collage Maker",
    "url": "image-tools/photo-collage-maker.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Combine multiple photos side-by-side or in custom grids client-side."
  },
  {
    "name": "Photo Frame Generator",
    "url": "image-tools/photo-frame-generator.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Overlay decorative wooden, gold, or modern gallery borders on photos."
  },
  {
    "name": "Photo Border Generator",
    "url": "image-tools/photo-border-generator.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Add clean borders of variable thickness and colors to photos."
  },
  {
    "name": "Photo Background Remover",
    "url": "image-tools/photo-background-remover.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Simulate and key out backgrounds from portraits using color thresholds client-side."
  },
  {
    "name": "Photo Background Changer",
    "url": "image-tools/photo-background-changer.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Change the background color of your portraits using transparency masks."
  },
  {
    "name": "Photo Size Reducer",
    "url": "image-tools/photo-size-reducer.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Scale down your photo's resolution and file size for fast uploads."
  },
  {
    "name": "Photo Enlarger",
    "url": "image-tools/photo-enlarger.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Enlarge smaller photos utilizing high-quality canvas bilinear interpolation scaling."
  },
  {
    "name": "Photo Splitter",
    "url": "image-tools/photo-splitter.html",
    "category": "Image Tools (Photo Tools)",
    "desc": "Split and slice a photo into equal grids (e.g. 2x2, 3x3) for Instagram layouts."
  },
  {
    "name": "AI Image Upscaler",
    "url": "image-tools/ai-image-upscaler.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Simulate artificial intelligence detail restoration to upscale smaller, blurry images."
  },
  {
    "name": "AI Background Remover",
    "url": "image-tools/ai-background-remover.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Simulate neural-network subject segmentation to isolate portraits and remove backgrounds."
  },
  {
    "name": "AI Object Remover",
    "url": "image-tools/ai-object-remover.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Simulate content-aware fill to remove unwanted objects or blemishes from photos."
  },
  {
    "name": "AI Image Enhancer",
    "url": "image-tools/ai-image-enhancer.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Simulate AI-driven auto-enhancement to optimize brightness, contrast, and color vibrance."
  },
  {
    "name": "AI Face Blur Tool",
    "url": "image-tools/ai-face-blur-tool.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Simulate automatic face detection to blur or pixelate human faces for privacy."
  },
  {
    "name": "AI Image Sharpen Tool",
    "url": "image-tools/ai-image-sharpen-tool.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Sharpen details and remove focus blur using mathematical high-pass filters."
  },
  {
    "name": "AI Photo Colorizer",
    "url": "image-tools/ai-photo-colorizer.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Simulate AI colorization algorithms to colorize vintage black and white photographs."
  },
  {
    "name": "AI Image Restoration Tool",
    "url": "image-tools/ai-image-restoration-tool.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Restore vintage photographs by removing dust, cleaning scratches, and balancing exposure."
  },
  {
    "name": "AI Image Caption Generator",
    "url": "image-tools/ai-image-caption-generator.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Generate descriptive labels and captions for your images automatically."
  },
  {
    "name": "AI Alt Text Generator",
    "url": "image-tools/ai-alt-text-generator.html",
    "category": "Image Tools (AI Image Utilities)",
    "desc": "Generate descriptive alt text parameters to make images accessible and SEO friendly."
  },
  {
    "name": "PDF to Image Converter",
    "url": "image-tools/pdf-to-image-converter.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Extract pages from PDF files and convert them into high-quality PNG or JPEG images."
  },
  {
    "name": "Image to PDF Converter",
    "url": "image-tools/image-to-pdf-converter.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Compile PNG or JPEG images into standard PDF documents client-side."
  },
  {
    "name": "JPG to PDF Converter",
    "url": "image-tools/jpg-to-pdf-converter.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Convert JPG photographs to standard PDF documents in your browser."
  },
  {
    "name": "PNG to PDF Converter",
    "url": "image-tools/png-to-pdf-converter.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Convert PNG graphics to PDF documents while preserving alpha channels."
  },
  {
    "name": "PDF Thumbnail Generator",
    "url": "image-tools/pdf-thumbnail-generator.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Generate custom icon thumbnails of PDF covers client-side."
  },
  {
    "name": "Multi Image to PDF",
    "url": "image-tools/multi-image-to-pdf.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Upload multiple images and compile them into a multi-page PDF document."
  },
  {
    "name": "PDF Page Extractor",
    "url": "image-tools/pdf-page-extractor.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Simulate extracting individual pages from a PDF file as standalone image assets."
  },
  {
    "name": "PDF Cover Generator",
    "url": "image-tools/pdf-cover-generator.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Generate stylish cover page images for e-books, reports, and manuals."
  },
  {
    "name": "PDF Image Extractor",
    "url": "image-tools/pdf-image-extractor.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Simulate scanning a PDF file and extracting embedded JPEG or PNG photos."
  },
  {
    "name": "PDF Preview Generator",
    "url": "image-tools/pdf-preview-generator.html",
    "category": "Image Tools (PDF & Image Tools)",
    "desc": "Create page preview grid sheets from PDF documents client-side."
  },
  {
    "name": "Alt Text Generator",
    "url": "image-tools/alt-text-generator.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Generate optimized, search-engine-readable Alt text tags to improve accessibility and image SEO."
  },
  {
    "name": "Image SEO Analyzer",
    "url": "image-tools/image-seo-analyzer.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Analyze images for SEO factors, including file size, filename structure, and alt text checks."
  },
  {
    "name": "Image File Name Generator",
    "url": "image-tools/image-file-name-generator.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Convert generic camera filenames (like IMG_0123.jpg) into optimized, SEO-friendly file names."
  },
  {
    "name": "Image Sitemap Generator",
    "url": "image-tools/image-sitemap-generator.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Generate XML sitemap codes specifically for Google Image searches."
  },
  {
    "name": "Open Graph Image Creator",
    "url": "image-tools/open-graph-image-creator.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Scale and frame your images into standard 1200x630px Open Graph covers for social media sharing."
  },
  {
    "name": "Social Sharing Image Generator",
    "url": "image-tools/social-sharing-image-generator.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Scale and format cover graphics for Twitter/X (1200x675) and Pinterest Pin (1000x1500) layout sharing."
  },
  {
    "name": "Featured Image Generator",
    "url": "image-tools/featured-image-generator.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Generate beautiful blog featured cover images with title text and brand colors."
  },
  {
    "name": "Blog Image Optimizer",
    "url": "image-tools/blog-image-optimizer.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Optimize blog images by converting them to next-gen WebP formats and scaling to standard post widths (800px)."
  },
  {
    "name": "Web Image Analyzer",
    "url": "image-tools/web-image-analyzer.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Analyze page loading speeds, layout shifts, and responsive image configurations."
  },
  {
    "name": "Image Performance Checker",
    "url": "image-tools/image-performance-checker.html",
    "category": "Image Tools (Image SEO Tools)",
    "desc": "Check layout paint times, compression ratios, and performance metrics of web assets."
  },
  {
    "name": "World Clock",
    "url": "time-tools/world-clock.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "View the current live time across major international cities including London, New York, Tokyo, Sydney, and UTC."
  },
  {
    "name": "Digital Clock",
    "url": "time-tools/digital-clock.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "A large, real-time digital clock displaying hours, minutes, seconds, current date, and active timezone details."
  },
  {
    "name": "Analog Clock",
    "url": "time-tools/analog-clock.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "A live-rendering analog clock using a detailed canvas layout and ticking second hand."
  },
  {
    "name": "Military Time Converter",
    "url": "time-tools/military-time-converter.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "Convert standard 12-hour AM/PM times into 24-hour military clock values (and vice-versa)."
  },
  {
    "name": "UTC Time Converter",
    "url": "time-tools/utc-time-converter.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "View the current Coordinated Universal Time (UTC) and convert any local timezone offset to UTC values."
  },
  {
    "name": "GMT Time Converter",
    "url": "time-tools/gmt-time-converter.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "Convert time between local offsets and Greenwich Mean Time (GMT) formats."
  },
  {
    "name": "Multi Time Zone Clock",
    "url": "time-tools/multi-time-zone-clock.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "Add and view multiple timezone dials side-by-side in real-time."
  },
  {
    "name": "Local Time Finder",
    "url": "time-tools/local-time-finder.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "Find and analyze details about your local system timezone offset, DST status, and location labels."
  },
  {
    "name": "International Time Converter",
    "url": "time-tools/international-time-converter.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "Convert clock times between international cities."
  },
  {
    "name": "Time Zone Lookup",
    "url": "time-tools/time-zone-lookup.html",
    "category": "Time Tools (Clock Tools)",
    "desc": "Lookup geographical offsets and abbreviations for international timezones."
  },
  {
    "name": "Time Duration Calculator",
    "url": "time-tools/time-duration-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Calculate the duration in days, hours, minutes, and seconds between two date-time values."
  },
  {
    "name": "Hours Between Times Calculator",
    "url": "time-tools/hours-between-times-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Calculate the exact decimal and HH:MM hours between two clock times."
  },
  {
    "name": "Minutes Between Times Calculator",
    "url": "time-tools/minutes-between-times-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Calculate the total minutes between two clock times."
  },
  {
    "name": "Time Difference Calculator",
    "url": "time-tools/time-difference-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Find the difference between two times, supporting PM-to-AM midnight boundaries."
  },
  {
    "name": "Add Time Calculator",
    "url": "time-tools/add-time-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Add hours, minutes, and seconds to a starting time index."
  },
  {
    "name": "Subtract Time Calculator",
    "url": "time-tools/subtract-time-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Subtract hours, minutes, and seconds from a starting time index."
  },
  {
    "name": "Future Time Calculator",
    "url": "time-tools/future-time-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Find the future date and time by adding days, hours, and minutes to a starting timestamp."
  },
  {
    "name": "Past Time Calculator",
    "url": "time-tools/past-time-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Find the past date and time by subtracting days, hours, and minutes from a starting timestamp."
  },
  {
    "name": "Shift Hours Calculator",
    "url": "time-tools/shift-hours-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Calculate total work shift hours and deduct lunch breaks automatically."
  },
  {
    "name": "Overtime Calculator",
    "url": "time-tools/overtime-calculator.html",
    "category": "Time Tools (Time Calculators)",
    "desc": "Calculate standard hours, overtime hours, and total salary payments based on base rate and multipliers."
  },
  {
    "name": "Date Difference Calculator",
    "url": "time-tools/date-difference-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate the exact duration between two dates in years, months, weeks, and days."
  },
  {
    "name": "Days Between Dates Calculator",
    "url": "time-tools/days-between-dates-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Determine the total number of calendar days between two dates, with option to include the start/end date."
  },
  {
    "name": "Weeks Between Dates Calculator",
    "url": "time-tools/weeks-between-dates-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate the number of weeks and remaining days between two calendar dates."
  },
  {
    "name": "Months Between Dates Calculator",
    "url": "time-tools/months-between-dates-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Find the elapsed calendar months and remaining days between two dates."
  },
  {
    "name": "Years Between Dates Calculator",
    "url": "time-tools/years-between-dates-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate the exact number of years elapsed between two historical or future calendar dates."
  },
  {
    "name": "Business Days Calculator",
    "url": "time-tools/business-days-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate the count of working business days (Monday to Friday) between two dates, excluding weekends."
  },
  {
    "name": "Working Days Calculator",
    "url": "time-tools/working-days-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate active working days using custom weekend formats (e.g. Sunday-only rest days)."
  },
  {
    "name": "School Days Calculator",
    "url": "time-tools/school-days-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate school attendance days between two dates, adjusting for weekends and institutional holidays."
  },
  {
    "name": "Holiday Calculator",
    "url": "time-tools/holiday-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Calculate calendar days and week positions of major national and international holidays for any given year."
  },
  {
    "name": "Leap Year Calculator",
    "url": "time-tools/leap-year-calculator.html",
    "category": "Time Tools (Date Calculators)",
    "desc": "Check if a specific year is a leap year (containing 366 days instead of 365)."
  },
  {
    "name": "Age Calculator",
    "url": "time-tools/age-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Calculate your exact age in years, months, and days based on your birthdate."
  },
  {
    "name": "Age In Days Calculator",
    "url": "time-tools/age-in-days-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Calculate your total age in days, hours, and minutes since your birthdate."
  },
  {
    "name": "Age In Months Calculator",
    "url": "time-tools/age-in-months-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Compute your age in months, showing total months elapsed since birth."
  },
  {
    "name": "Exact Age Calculator",
    "url": "time-tools/exact-age-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Track your exact age in real-time down to the millisecond with a live ticking display."
  },
  {
    "name": "Birthday Countdown Calculator",
    "url": "time-tools/birthday-countdown-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Check how many months, days, hours, and minutes remain until your next annual birthday celebration."
  },
  {
    "name": "Next Birthday Calculator",
    "url": "time-tools/next-birthday-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Calculate days left for your next birthday and discover what day of the week it will fall on."
  },
  {
    "name": "Pet Age Calculator",
    "url": "time-tools/pet-age-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Translate human years of dogs and cats into their biological pet age equivalent."
  },
  {
    "name": "Retirement Age Calculator",
    "url": "time-tools/retirement-age-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Calculate how many years are left until your target retirement and find out the calendar year you will retire."
  },
  {
    "name": "Zodiac Age Calculator",
    "url": "time-tools/zodiac-age-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Discover your Western Zodiac and Chinese Zodiac symbols based on your birthdate."
  },
  {
    "name": "Life Expectancy Calculator",
    "url": "time-tools/life-expectancy-calculator.html",
    "category": "Time Tools (Age Calculators)",
    "desc": "Check your estimated remaining lifespan and statistical average life expectancy based on demographic and lifestyle choices."
  },
  {
    "name": "Countdown Timer",
    "url": "time-tools/countdown-timer.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Set a custom duration in hours, minutes, and seconds, and receive an audio alert when the countdown reaches zero."
  },
  {
    "name": "Event Countdown",
    "url": "time-tools/event-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Count down to any specific calendar date and time event."
  },
  {
    "name": "Birthday Countdown",
    "url": "time-tools/birthday-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Check the precise remaining time until your next annual birthday anniversary."
  },
  {
    "name": "Wedding Countdown",
    "url": "time-tools/wedding-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Track the months, days, hours, and seconds remaining until your wedding day."
  },
  {
    "name": "Exam Countdown",
    "url": "time-tools/exam-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Check how much study time you have left before your target exam date."
  },
  {
    "name": "New Year Countdown",
    "url": "time-tools/new-year-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Track the exact time remaining until the stroke of midnight on January 1st."
  },
  {
    "name": "Holiday Countdown",
    "url": "time-tools/holiday-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Count down to major upcoming seasonal holidays and public vacation breaks."
  },
  {
    "name": "Product Launch Countdown",
    "url": "time-tools/product-launch-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Create a live countdown for launch announcements and product release goals."
  },
  {
    "name": "Anniversary Countdown",
    "url": "time-tools/anniversary-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Check remaining days until your corporate, wedding, or custom milestone anniversary."
  },
  {
    "name": "Goal Countdown",
    "url": "time-tools/goal-countdown.html",
    "category": "Time Tools (Countdown Tools)",
    "desc": "Stay motivated by counting down to your target deadline for specific achievements."
  },
  {
    "name": "Pomodoro Timer",
    "url": "time-tools/pomodoro-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "A productivity timer implementing the standard Pomodoro method: 25 minutes of focus followed by a 5-minute break."
  },
  {
    "name": "Focus Timer",
    "url": "time-tools/focus-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "A simple customizable focus timer that tracks and logs completed focus blocks."
  },
  {
    "name": "Study Timer",
    "url": "time-tools/study-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "A timer optimized for structured study blocks (e.g. 50 minutes study, 10 minutes rest)."
  },
  {
    "name": "Work Timer",
    "url": "time-tools/work-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "Track active task sprints with custom limits and rest interval notifications."
  },
  {
    "name": "Break Timer",
    "url": "time-tools/break-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "An adjustable timer for micro-breaks, lunch breaks, and stretching sessions."
  },
  {
    "name": "Deep Work Timer",
    "url": "time-tools/deep-work-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "Optimize cognitive focus with dedicated 90-minute deep work blocks."
  },
  {
    "name": "Meeting Timer",
    "url": "time-tools/meeting-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "Track and budget meeting discussions to prevent time overflow."
  },
  {
    "name": "Presentation Timer",
    "url": "time-tools/presentation-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "Track your speech time with visual and audio alerts when nearing deadline limits."
  },
  {
    "name": "Classroom Timer",
    "url": "time-tools/classroom-timer.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "A teacher's utility to budget student tests, quizzes, and classroom team activities."
  },
  {
    "name": "Productivity Tracker",
    "url": "time-tools/productivity-tracker.html",
    "category": "Time Tools (Productivity Tools)",
    "desc": "Track focused hours, log completed tasks, and calculate your daily productivity score."
  },
  {
    "name": "Online Stopwatch",
    "url": "time-tools/online-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A precise online stopwatch with start, split/lap, pause, and reset features."
  },
  {
    "name": "Lap Stopwatch",
    "url": "time-tools/lap-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A stopwatch optimized for recording and exporting multiple lap splits."
  },
  {
    "name": "Sports Stopwatch",
    "url": "time-tools/sports-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A sports-oriented coaching timer designed for outdoor training schedules."
  },
  {
    "name": "Race Timer",
    "url": "time-tools/race-timer.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A race-day lap timer designed to track speeds and interval displacements."
  },
  {
    "name": "Training Timer",
    "url": "time-tools/training-timer.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A workout timer designed for tracking split training sessions and exercise durations."
  },
  {
    "name": "Fitness Stopwatch",
    "url": "time-tools/fitness-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A stopwatch that tracks workout durations and estimates standard metabolic calorie burn metrics."
  },
  {
    "name": "Running Stopwatch",
    "url": "time-tools/running-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A stopwatch with integrated pace estimation algorithms for running workouts."
  },
  {
    "name": "Swimming Stopwatch",
    "url": "time-tools/swimming-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A swimmer's stopwatch optimized for recording pool lap splits and stroke pace intervals."
  },
  {
    "name": "Interval Stopwatch",
    "url": "time-tools/interval-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A custom training timer for configuring and tracking high-intensity interval training (HIIT) workout loops."
  },
  {
    "name": "Precision Stopwatch",
    "url": "time-tools/precision-stopwatch.html",
    "category": "Time Tools (Stopwatch Tools)",
    "desc": "A millisecond-precise stopwatch display featuring microsecond accuracy clocks."
  },
  {
    "name": "Meeting Planner",
    "url": "time-tools/meeting-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Plan and structure agenda slots for business meetings or workshop sessions."
  },
  {
    "name": "Meeting Time Finder",
    "url": "time-tools/meeting-time-finder.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Find the best common meeting slot based on team member availabilities."
  },
  {
    "name": "Time Zone Meeting Planner",
    "url": "time-tools/time-zone-meeting-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Find overlapping meeting slots for remote team members located in different time zones."
  },
  {
    "name": "Appointment Scheduler",
    "url": "time-tools/appointment-scheduler.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "A scheduling assistant to help divide your day into clean, structured appointment slots."
  },
  {
    "name": "Shift Planner",
    "url": "time-tools/shift-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Plan and allocate daily employee work shifts based on hours and roles."
  },
  {
    "name": "Work Schedule Generator",
    "url": "time-tools/work-schedule-generator.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Generate structured weekly work rosters for multiple team members."
  },
  {
    "name": "Weekly Planner",
    "url": "time-tools/weekly-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Organize tasks and distribute priorities across the days of the week."
  },
  {
    "name": "Monthly Planner",
    "url": "time-tools/monthly-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Organize key deadlines and milestones across a monthly calendar view."
  },
  {
    "name": "Daily Planner",
    "url": "time-tools/daily-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Structure your daily goals hour-by-hour to optimize personal productivity."
  },
  {
    "name": "Event Planner",
    "url": "time-tools/event-planner.html",
    "category": "Time Tools (Scheduling Tools)",
    "desc": "Schedule milestones and track agenda budgets for large social events."
  },
  {
    "name": "Time Zone Converter",
    "url": "time-tools/time-zone-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Convert standard times between multiple international time zones instantly."
  },
  {
    "name": "Unix Timestamp Converter",
    "url": "time-tools/unix-timestamp-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Translate 10-digit Unix timestamps into readable local and UTC dates."
  },
  {
    "name": "Epoch Converter",
    "url": "time-tools/epoch-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Convert standard calendar dates to seconds and milliseconds Unix Epoch timestamps."
  },
  {
    "name": "12 Hour To 24 Hour Converter",
    "url": "time-tools/12-hour-to-24-hour-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Translate standard 12-hour (AM/PM) clock time into 24-hour military values."
  },
  {
    "name": "24 Hour To 12 Hour Converter",
    "url": "time-tools/24-hour-to-12-hour-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Convert 24-hour military clock values into standard 12-hour (AM/PM) format."
  },
  {
    "name": "Seconds Converter",
    "url": "time-tools/seconds-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Convert seconds into minutes, hours, days, and fractional weeks."
  },
  {
    "name": "Minutes Converter",
    "url": "time-tools/minutes-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Convert minute values into seconds, hours, and calendar day counts."
  },
  {
    "name": "Hours Converter",
    "url": "time-tools/hours-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Translate hours into equivalent seconds, minutes, days, and calendar weeks."
  },
  {
    "name": "Days Converter",
    "url": "time-tools/days-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Convert calendar day counts into equivalent weeks, months, and hours."
  },
  {
    "name": "Date Format Converter",
    "url": "time-tools/date-format-converter.html",
    "category": "Time Tools (Conversion Tools)",
    "desc": "Translate standard calendar dates into multiple string styles (ISO-8601, RFC-2822, UNIX, DD/MM/YYYY, etc.)."
  },
  {
    "name": "Payroll Hours Calculator",
    "url": "time-tools/payroll-hours-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Calculate gross payroll earnings by combining working hours and overtime rates."
  },
  {
    "name": "Employee Time Tracker",
    "url": "time-tools/employee-time-tracker.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Track employee shifts by logging custom clock-in and clock-out hours."
  },
  {
    "name": "Timesheet Calculator",
    "url": "time-tools/timesheet-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Calculate total weekly working hours by inputting daily working shifts."
  },
  {
    "name": "Attendance Calculator",
    "url": "time-tools/attendance-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Calculate attendance rates and see the minimum classes needed to meet target percentage rules."
  },
  {
    "name": "Work Hours Calculator",
    "url": "time-tools/work-hours-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Calculate shift duration excluding custom break limits."
  },
  {
    "name": "Shift Duration Calculator",
    "url": "time-tools/shift-duration-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Calculate total duration for regular or overnight shifts."
  },
  {
    "name": "Billable Hours Calculator",
    "url": "time-tools/billable-hours-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Find total invoice values by inputting client rates and billable hour metrics."
  },
  {
    "name": "Freelancer Time Tracker",
    "url": "time-tools/freelancer-time-tracker.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "A tracking timer for freelancers to log active client tasks and estimate invoice earnings."
  },
  {
    "name": "Project Time Calculator",
    "url": "time-tools/project-time-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Aggregate multiple employee and task sprint times into a master project total."
  },
  {
    "name": "Productivity Hours Calculator",
    "url": "time-tools/productivity-hours-calculator.html",
    "category": "Time Tools (Business Time Tools)",
    "desc": "Measure the ratio of productive working hours relative to total clocked shift times."
  },
  {
    "name": "Event Countdown Timer",
    "url": "time-tools/event-countdown-timer.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "A dedicated event timer that ticks down in real-time, helping you organize announcements and announcements."
  },
  {
    "name": "Wedding Planner Timer",
    "url": "time-tools/wedding-planner-timer.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Track your wedding preparation milestones and checklist deadlines."
  },
  {
    "name": "Vacation Countdown",
    "url": "time-tools/vacation-countdown.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Check how many days, hours, and minutes remain before your upcoming vacation trip."
  },
  {
    "name": "Trip Countdown",
    "url": "time-tools/trip-countdown.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Track the exact remaining time before your next travel journey."
  },
  {
    "name": "Festival Countdown",
    "url": "time-tools/festival-countdown.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Check remaining days until major annual festivals (Christmas, Diwali, Thanksgiving, etc.)."
  },
  {
    "name": "Conference Countdown",
    "url": "time-tools/conference-countdown.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Plan and count down to major professional summits and team conferences."
  },
  {
    "name": "Webinar Timer",
    "url": "time-tools/webinar-timer.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "A specialized countdown tool for webinar speakers and digital events."
  },
  {
    "name": "Launch Timer",
    "url": "time-tools/launch-timer.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Check remaining days before brand announcement milestones."
  },
  {
    "name": "Registration Deadline Timer",
    "url": "time-tools/registration-deadline-timer.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Check days left before registration signups close."
  },
  {
    "name": "Reminder Generator",
    "url": "time-tools/reminder-generator.html",
    "category": "Time Tools (Event & Planning Tools)",
    "desc": "Create a structured plan of tasks and set calendar alarm alerts."
  },
  {
    "name": "Sunrise Calculator",
    "url": "time-tools/sunrise-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Calculate the exact sunrise time for any location based on latitude, longitude, and calendar date."
  },
  {
    "name": "Sunset Calculator",
    "url": "time-tools/sunset-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Find the precise local sunset hour for any global latitude and date coordinates."
  },
  {
    "name": "Golden Hour Calculator",
    "url": "time-tools/golden-hour-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Identify the optimal morning and evening golden hours for photography based on solar elevations."
  },
  {
    "name": "Moon Phase Calculator",
    "url": "time-tools/moon-phase-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Calculate the current phase of the moon and its illumination percentage."
  },
  {
    "name": "Day Length Calculator",
    "url": "time-tools/day-length-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Calculate total daylight photoperiod hours based on latitudinal tilt."
  },
  {
    "name": "Night Length Calculator",
    "url": "time-tools/night-length-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Calculate total night photoperiod hours based on latitudinal tilt."
  },
  {
    "name": "Solar Time Calculator",
    "url": "time-tools/solar-time-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Calculate True Solar Time (sundial time) based on Equation of Time variations."
  },
  {
    "name": "Seasonal Calculator",
    "url": "time-tools/seasonal-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Check dates of Spring Equinox, Summer Solstice, Autumn Equinox, and Winter Solstice for any given year."
  },
  {
    "name": "Equinox Calculator",
    "url": "time-tools/equinox-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Check dates of Vernal (Spring) and Autumnal equinoxes."
  },
  {
    "name": "Solstice Calculator",
    "url": "time-tools/solstice-calculator.html",
    "category": "Time Tools (Astronomy & Natural Time Tools)",
    "desc": "Calculate dates of Summer and Winter solstices."
  },
  {
    "name": "JSON Formatter",
    "url": "developer-tools/json-formatter-dev.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Format, indent, and beautify raw JSON strings into human-readable structures."
  },
  {
    "name": "JSON Validator",
    "url": "developer-tools/json-validator.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Validate JSON structures and locate exact syntax error line numbers."
  },
  {
    "name": "XML Formatter",
    "url": "developer-tools/xml-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Clean and format XML syntax tree documents with correct indentation levels."
  },
  {
    "name": "XML Validator",
    "url": "developer-tools/xml-validator.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Check XML documents for schema validity and parse error offsets."
  },
  {
    "name": "HTML Formatter",
    "url": "developer-tools/html-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Format and beautify HTML documents with nested tag indentation."
  },
  {
    "name": "HTML Minifier",
    "url": "developer-tools/html-minifier.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Compress and minify HTML markup by removing unnecessary spacing, comments, and line breaks."
  },
  {
    "name": "CSS Formatter",
    "url": "developer-tools/css-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Beautify stylesheet code with consistent blocks, property spacing, and clean indents."
  },
  {
    "name": "CSS Minifier",
    "url": "developer-tools/css-minifier.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Minify CSS rules to optimize style sheets and improve website performance."
  },
  {
    "name": "JavaScript Formatter",
    "url": "developer-tools/javascript-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Beautify raw JavaScript files, aligned braces, indent arguments, and spacing."
  },
  {
    "name": "JavaScript Minifier",
    "url": "developer-tools/javascript-minifier.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Compress and minify JavaScript source code by stripping formatting, comments, and empty lines."
  },
  {
    "name": "SQL Formatter",
    "url": "developer-tools/sql-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Format query text files by placing keywords (SELECT, FROM, WHERE) on new lines with proper casing."
  },
  {
    "name": "YAML Formatter",
    "url": "developer-tools/yaml-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Indent, format, and validate YAML layout files for clean configuration parameters."
  },
  {
    "name": "Markdown Formatter",
    "url": "developer-tools/markdown-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Beautify markdown documents by organizing headers, spacing, and table syntax layouts."
  },
  {
    "name": "CSV Formatter",
    "url": "developer-tools/csv-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Align CSV tabular datasets by spacing columns symmetrically for visual inspection."
  },
  {
    "name": "TSV Formatter",
    "url": "developer-tools/tsv-formatter.html",
    "category": "Developer Tools (Code Formatters)",
    "desc": "Align TSV files by computing max cell widths and displaying aligned grids."
  },
  {
    "name": "JSON to CSV Converter",
    "url": "developer-tools/json-to-csv-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Convert JSON array data into structured CSV spreadsheet files."
  },
  {
    "name": "CSV to JSON Converter",
    "url": "developer-tools/csv-to-json-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Translate comma-separated CSV rows into clean JSON object arrays."
  },
  {
    "name": "XML to JSON Converter",
    "url": "developer-tools/xml-to-json-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Convert XML documents into hierarchical JSON tree objects."
  },
  {
    "name": "JSON to XML Converter",
    "url": "developer-tools/json-to-xml-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Generate custom XML document strings from JSON models."
  },
  {
    "name": "HTML to Markdown Converter",
    "url": "developer-tools/html-to-markdown-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Translate HTML elements (headers, lists, links) into clean Markdown files."
  },
  {
    "name": "Markdown to HTML Converter",
    "url": "developer-tools/markdown-to-html-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Compile Markdown syntax sheets into clean HTML tags."
  },
  {
    "name": "CSV to XML Converter",
    "url": "developer-tools/csv-to-xml-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Convert tabular CSV datasets into formatted XML files."
  },
  {
    "name": "XML to CSV Converter",
    "url": "developer-tools/xml-to-csv-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Translate XML list structures into CSV sheet matrices."
  },
  {
    "name": "YAML to JSON Converter",
    "url": "developer-tools/yaml-to-json-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Translate YAML configuration text streams into parseable JSON trees."
  },
  {
    "name": "JSON to YAML Converter",
    "url": "developer-tools/json-to-yaml-converter.html",
    "category": "Developer Tools (Code Converters)",
    "desc": "Format JSON models as clean YAML indentation configs."
  },
  {
    "name": "Color Code Converter",
    "url": "developer-tools/color-code-converter.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Translate color values between HEX, RGB, and HSL formats."
  },
  {
    "name": "CSS Gradient Generator",
    "url": "developer-tools/css-gradient-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Create beautiful CSS linear or radial gradient declarations."
  },
  {
    "name": "CSS Box Shadow Generator",
    "url": "developer-tools/css-box-shadow-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Generate CSS box-shadow styles with real-time preview indicators."
  },
  {
    "name": "CSS Border Radius Generator",
    "url": "developer-tools/css-border-radius-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Adjust and generate border-radius CSS attributes with visual previews."
  },
  {
    "name": "CSS Clip Path Generator",
    "url": "developer-tools/css-clip-path-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Create CSS clip-path masks using standard shapes (polygon, circle, inset)."
  },
  {
    "name": "CSS Grid Generator",
    "url": "developer-tools/css-grid-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Design two-dimensional CSS Grid layouts and get instant structural styles."
  },
  {
    "name": "Flexbox Generator",
    "url": "developer-tools/flexbox-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Design and test one-dimensional CSS Flexbox layouts with alignment options."
  },
  {
    "name": "Open Graph Generator",
    "url": "developer-tools/open-graph-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Create meta tags for Open Graph mappings to control link previews on social platforms."
  },
  {
    "name": "Meta Tag Generator",
    "url": "developer-tools/meta-tag-generator-dev.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Generate core HTML header SEO meta tags for site indexing."
  },
  {
    "name": "Robots.txt Generator",
    "url": "developer-tools/robotstxt-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Create robots.txt configurations to guide search engine crawlers."
  },
  {
    "name": "Sitemap Generator",
    "url": "developer-tools/sitemap-generator-dev.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Generate XML sitemap file structures containing site page links."
  },
  {
    "name": "Favicon Generator",
    "url": "developer-tools/favicon-generator.html",
    "category": "Developer Tools (Web Development Tools)",
    "desc": "Draw or mock up a basic custom color block favicon asset."
  },
  {
    "name": "API Request Builder",
    "url": "developer-tools/api-request-builder.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Build and send GET, POST, PUT, or DELETE API requests directly from your browser."
  },
  {
    "name": "API Response Viewer",
    "url": "developer-tools/api-response-viewer.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Format and inspect raw API response payloads with headers validation."
  },
  {
    "name": "JSON Viewer",
    "url": "developer-tools/json-viewer.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "View, format, and syntax check raw JSON structures cleanly."
  },
  {
    "name": "JSON Tree Viewer",
    "url": "developer-tools/json-tree-viewer.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Explore JSON datasets with an interactive collapsible tree node renderer."
  },
  {
    "name": "JSON Compare Tool",
    "url": "developer-tools/json-compare-tool.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Check if two separate JSON strings are structurally identical."
  },
  {
    "name": "JSON Diff Checker",
    "url": "developer-tools/json-diff-checker.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Identify and highlight line differences between two JSON structures."
  },
  {
    "name": "XML Viewer",
    "url": "developer-tools/xml-viewer.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Check, format, and view XML documents cleanly inside browsers."
  },
  {
    "name": "XML Tree Viewer",
    "url": "developer-tools/xml-tree-viewer.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Renders collapsible tag structures of XML documents."
  },
  {
    "name": "CSV Viewer",
    "url": "developer-tools/csv-viewer.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Render raw CSV file inputs into structured HTML tables."
  },
  {
    "name": "Data Table Generator",
    "url": "developer-tools/data-table-generator.html",
    "category": "Developer Tools (API & Data Tools)",
    "desc": "Generate custom HTML table scripts dynamically with custom column metrics."
  },
  {
    "name": "Base64 Encoder",
    "url": "developer-tools/base64-encoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Encode raw text strings into secure Base64 format representations."
  },
  {
    "name": "Base64 Decoder",
    "url": "developer-tools/base64-decoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Decode Base64 strings back into human-readable text."
  },
  {
    "name": "URL Encoder",
    "url": "developer-tools/url-encoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Encode special characters into percent-escaped URL strings."
  },
  {
    "name": "URL Decoder",
    "url": "developer-tools/url-decoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Convert percent-escaped URL parameters back to original text."
  },
  {
    "name": "HTML Entity Encoder",
    "url": "developer-tools/html-encoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Convert special HTML tags into matching character entity sequences."
  },
  {
    "name": "HTML Entity Decoder",
    "url": "developer-tools/html-decoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Translate escaped HTML character entities back to normal tags."
  },
  {
    "name": "Unicode Encoder",
    "url": "developer-tools/unicode-encoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Translate characters into escaped Unicode code point sequences."
  },
  {
    "name": "Unicode Decoder",
    "url": "developer-tools/unicode-decoder.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Unescape unicode escape sequences back into readable text."
  },
  {
    "name": "ASCII Converter",
    "url": "developer-tools/ascii-converter.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Convert text into decimal or binary representation of ASCII bytes."
  },
  {
    "name": "Text Escape Tool",
    "url": "developer-tools/text-escape-tool.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Escape programming control characters in plain text."
  },
  {
    "name": "Text Unescape Tool",
    "url": "developer-tools/text-unescape-tool.html",
    "category": "Developer Tools (Text & Encoding Tools)",
    "desc": "Restore escaped sequences back into raw string text formatting."
  },
  {
    "name": "Regex Tester",
    "url": "developer-tools/regex-tester.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Test and evaluate JavaScript regular expressions against target strings."
  },
  {
    "name": "Regex Generator",
    "url": "developer-tools/regex-generator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Generate custom regular expression patterns based on simple requirements."
  },
  {
    "name": "Regex Cheat Sheet Generator",
    "url": "developer-tools/regex-cheat-sheet-generator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Check and display standard regular expression operators cheat sheets."
  },
  {
    "name": "Email Validator",
    "url": "developer-tools/email-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Check if an email address matches RFC 5322 syntax criteria."
  },
  {
    "name": "URL Validator",
    "url": "developer-tools/url-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Verify if a URL string conforms to RFC 3986 URI specifications."
  },
  {
    "name": "IPv4 Validator",
    "url": "developer-tools/ipv4-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Check if an IP address is a valid IPv4 network coordinates interface."
  },
  {
    "name": "IPv6 Validator",
    "url": "developer-tools/ipv6-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Validate IPv6 network address structures against RFC 4291 patterns."
  },
  {
    "name": "UUID Validator",
    "url": "developer-tools/uuid-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Check if a UUID / GUID string is mathematically structured."
  },
  {
    "name": "JSON Schema Validator",
    "url": "developer-tools/json-schema-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Validate JSON object data layouts against a basic JSON Schema specification."
  },
  {
    "name": "XML Schema Validator",
    "url": "developer-tools/xml-schema-validator.html",
    "category": "Developer Tools (Regex & Validation Tools)",
    "desc": "Check XML documents for presence of tags and nested tag syntax structures."
  },
  {
    "name": "SQL Query Formatter",
    "url": "developer-tools/sql-query-formatter.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Beautify and format complex SQL queries with proper keywords layout."
  },
  {
    "name": "SQL Beautifier",
    "url": "developer-tools/sql-beautifier.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Indent and align SQL database statements for improved readability."
  },
  {
    "name": "SQL Minifier",
    "url": "developer-tools/sql-minifier.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Compress and minify SQL query codes by removing spaces and comments."
  },
  {
    "name": "SQL Query Generator",
    "url": "developer-tools/sql-query-generator.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Generate custom SQL SELECT queries dynamically using form inputs."
  },
  {
    "name": "Database Schema Viewer",
    "url": "developer-tools/database-schema-viewer.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Check and display database column properties inside clean schema cards."
  },
  {
    "name": "ER Diagram Generator",
    "url": "developer-tools/er-diagram-generator.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Check entity relationships and compile visual schema connections."
  },
  {
    "name": "Table Creator",
    "url": "developer-tools/table-creator.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Design custom tables and output HTML, Markdown, or SQL schemas."
  },
  {
    "name": "Mock Database Generator",
    "url": "developer-tools/mock-database-generator.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Generate dummy SQL database tables with insert statements containing mock usernames."
  },
  {
    "name": "CSV Import Generator",
    "url": "developer-tools/csv-import-generator.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Convert CSV rows into SQL INSERT database scripts."
  },
  {
    "name": "SQL Export Generator",
    "url": "developer-tools/sql-export-generator.html",
    "category": "Developer Tools (Database Tools)",
    "desc": "Translate JSON object arrays into SQL schema export files."
  },
  {
    "name": "Unix Timestamp Converter",
    "url": "developer-tools/unix-timestamp-converter.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Convert Unix epoch timestamps to human-readable dates and vice-versa."
  },
  {
    "name": "Epoch Converter",
    "url": "developer-tools/epoch-converter-dev.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Bi-directional epoch time converter featuring a live ticking Unix clock."
  },
  {
    "name": "Date Formatter",
    "url": "developer-tools/date-formatter.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Format date elements into multiple calendar standard formats."
  },
  {
    "name": "Time Zone Converter",
    "url": "developer-tools/time-zone-converter.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Translate calendar times between major worldwide timezones."
  },
  {
    "name": "ISO Date Converter",
    "url": "developer-tools/iso-date-converter.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Convert ISO 8601 strings (e.g. YYYY-MM-DDTHH:mm:ssZ) to local formats."
  },
  {
    "name": "Date Difference Calculator",
    "url": "developer-tools/date-difference-calculator.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Calculate calendar intervals (days, weeks, months) between two dates."
  },
  {
    "name": "Cron Expression Generator",
    "url": "developer-tools/cron-expression-generator.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Build standard 5-field cron schedule strings using interactive inputs."
  },
  {
    "name": "Cron Expression Parser",
    "url": "developer-tools/cron-expression-parser.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Parse 5-field cron strings into human-readable text descriptions."
  },
  {
    "name": "Working Days Calculator",
    "url": "developer-tools/working-days-calculator-dev.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "Calculate working days (excluding weekends) between two dates."
  },
  {
    "name": "World Time Viewer",
    "url": "developer-tools/world-time-viewer.html",
    "category": "Developer Tools (Date & Time Tools)",
    "desc": "View ticking live clocks across major global timezones."
  },
  {
    "name": "IP Address Lookup",
    "url": "developer-tools/ip-address-lookup.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Retrieve geo-location, ISP, and connection metadata for your active public IP address."
  },
  {
    "name": "IP Address Validator",
    "url": "developer-tools/ip-address-validator.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Check if an IP address is a valid IPv4 or IPv6 format."
  },
  {
    "name": "DNS Lookup",
    "url": "developer-tools/dns-lookup.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Query DNS A, AAAA, MX, and TXT records using public DNS over HTTPS interfaces."
  },
  {
    "name": "Reverse DNS Lookup",
    "url": "developer-tools/reverse-dns-lookup.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Simulate reverse PTR DNS lookups to find hostnames mapped to IP addresses."
  },
  {
    "name": "HTTP Header Checker",
    "url": "developer-tools/http-header-checker.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Simulate and check standard HTTP headers sent during page requests."
  },
  {
    "name": "User Agent Parser",
    "url": "developer-tools/user-agent-parser.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Parse and identify OS, browser engine, and device brand metrics from active user-agents."
  },
  {
    "name": "MIME Type Lookup",
    "url": "developer-tools/mime-type-lookup.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Check standard MIME types associated with file extensions."
  },
  {
    "name": "Port Reference Tool",
    "url": "developer-tools/port-reference-tool.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Check standard TCP/UDP networking port numbers and descriptions."
  },
  {
    "name": "HTTP Status Code Reference",
    "url": "developer-tools/http-status-code-reference.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Check definitions for HTTP status response codes."
  },
  {
    "name": "URL Parser",
    "url": "developer-tools/url-parser.html",
    "category": "Developer Tools (Network & Internet Tools)",
    "desc": "Parse URL strings into separate hostname, protocol, search queries, and port properties."
  },
  {
    "name": "HEX to RGB Converter",
    "url": "developer-tools/hex-to-rgb-converter.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Convert hexadecimal color strings to RGB values."
  },
  {
    "name": "RGB to HEX Converter",
    "url": "developer-tools/rgb-to-hex-converter.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Translate RGB color values into hexadecimal color formats."
  },
  {
    "name": "HEX to HSL Converter",
    "url": "developer-tools/hex-to-hsl-converter.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Convert hex colors to HSL (Hue, Saturation, Lightness) styles."
  },
  {
    "name": "HSL to HEX Converter",
    "url": "developer-tools/hsl-to-hex-converter.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Translate HSL color values back into hexadecimal codes."
  },
  {
    "name": "Color Palette Generator",
    "url": "developer-tools/color-palette-generator.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Generate monochromatic, analogous, and complementary color schemes."
  },
  {
    "name": "Gradient Generator",
    "url": "developer-tools/gradient-generator.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Create CSS linear or radial gradient declarations."
  },
  {
    "name": "Color Contrast Checker",
    "url": "developer-tools/color-contrast-checker.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Check contrast ratios between foreground and background colors."
  },
  {
    "name": "Accessibility Color Checker",
    "url": "developer-tools/accessibility-color-checker.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Check color combinations for WCAG AA and AAA accessibility parameters."
  },
  {
    "name": "Brand Color Generator",
    "url": "developer-tools/brand-color-generator.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Generate brand color palettes including secondary, accent, and background options."
  },
  {
    "name": "CSS Color Generator",
    "url": "developer-tools/css-color-generator.html",
    "category": "Developer Tools (Color & Design Tools)",
    "desc": "Build CSS colors (RGBA, HSLA) using interactive sliders."
  },
  {
    "name": "Lorem Ipsum Generator",
    "url": "developer-tools/lorem-ipsum-generator.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Generate dummy placeholder text for website layout mockup designs."
  },
  {
    "name": "Dummy Data Generator",
    "url": "developer-tools/dummy-data-generator.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Create mock user databases (names, emails, phones) in JSON format."
  },
  {
    "name": "UUID Generator",
    "url": "developer-tools/uuid-generator-dev.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Generate secure Version 4 UUIDs (Universally Unique Identifiers)."
  },
  {
    "name": "Random Number Generator",
    "url": "developer-tools/random-number-generator.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Generate random integers within a custom min/max range."
  },
  {
    "name": "Random String Generator",
    "url": "developer-tools/random-string-generator.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Create secure random passwords, tokens, or keys of custom length."
  },
  {
    "name": "Slug Generator",
    "url": "developer-tools/slug-generator.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Convert text headings into clean URL-friendly slugs."
  },
  {
    "name": "Case Converter",
    "url": "developer-tools/case-converter-dev.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Convert code variables and text between camelCase, snake_case, PascalCase, and kebab-case."
  },
  {
    "name": "Text Difference Checker",
    "url": "developer-tools/text-difference-checker.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Identify differences between two plain text strings."
  },
  {
    "name": "Text Comparison Tool",
    "url": "developer-tools/text-comparison-tool.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Check if two text blocks are identical."
  },
  {
    "name": "Character Counter",
    "url": "developer-tools/character-counter-dev.html",
    "category": "Developer Tools (Productivity Tools)",
    "desc": "Display counts of characters, words, sentences, and lines in your text."
  },
  {
    "name": "Twitter Card Generator",
    "url": "developer-tools/twitter-card-generator.html",
    "category": "Developer Tools (SEO & Webmaster Tools)",
    "desc": "Generate custom Twitter Card meta tags for responsive social media previews."
  },
  {
    "name": "Canonical URL Generator",
    "url": "developer-tools/canonical-url-generator.html",
    "category": "Developer Tools (SEO & Webmaster Tools)",
    "desc": "Generate canonical link tags to resolve duplicate page indexing issues."
  },
  {
    "name": "Schema Markup Generator",
    "url": "developer-tools/schema-markup-generator.html",
    "category": "Developer Tools (SEO & Webmaster Tools)",
    "desc": "Generate structured JSON-LD schema scripts for Rich Snippets."
  },
  {
    "name": "Keyword Density Checker",
    "url": "developer-tools/keyword-density-checker.html",
    "category": "Developer Tools (SEO & Webmaster Tools)",
    "desc": "Check the occurrences and frequency percentage of keywords in your copy."
  },
  {
    "name": "Redirect Generator",
    "url": "developer-tools/redirect-generator.html",
    "category": "Developer Tools (SEO & Webmaster Tools)",
    "desc": "Generate Nginx redirects or Apache .htaccess rules."
  },
  {
    "name": "Hreflang Generator",
    "url": "developer-tools/hreflang-generator.html",
    "category": "Developer Tools (SEO & Webmaster Tools)",
    "desc": "Create alternate hreflang tags for multi-language search engine index targeting."
  },
  {
    "name": "Lorem Ipsum Generator",
    "url": "generator-tools/lorem-ipsum-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Generate classic Lorem Ipsum placeholder text for layouts and designs."
  },
  {
    "name": "Dummy Text Generator",
    "url": "generator-tools/dummy-text-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Generate custom mock sentences, pangrams, and random gibberish."
  },
  {
    "name": "Random Word Generator",
    "url": "generator-tools/random-word-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Generate lists of random verbs, nouns, adjectives, or general English words."
  },
  {
    "name": "Random Sentence Generator",
    "url": "generator-tools/random-sentence-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Generate grammatically correct random sentences for typing tests or placeholders."
  },
  {
    "name": "Random Paragraph Generator",
    "url": "generator-tools/random-paragraph-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Assemble cohesive-looking paragraphs consisting of randomized sentences."
  },
  {
    "name": "Random Story Generator",
    "url": "generator-tools/random-story-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Create fun, randomized short stories using structural mad-lib templates."
  },
  {
    "name": "Random Topic Generator",
    "url": "generator-tools/random-topic-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Generate interesting discussion prompts, debate questions, or essay topics."
  },
  {
    "name": "Quote Generator",
    "url": "generator-tools/quote-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Get classic, inspiring, and historic quotes from famous figures."
  },
  {
    "name": "Motivational Quote Generator",
    "url": "generator-tools/motivational-quote-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Get direct motivational quotes to boost your productivity and focus."
  },
  {
    "name": "Writing Prompt Generator",
    "url": "generator-tools/writing-prompt-generator.html",
    "category": "Generator Tools (Text Generators)",
    "desc": "Get random story prompts combining genre, character, conflict, and key objects."
  },
  {
    "name": "Username Generator",
    "url": "generator-tools/username-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate clean, modern, and unique usernames using word blending."
  },
  {
    "name": "Instagram Username Generator",
    "url": "generator-tools/instagram-username-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate aesthetic Instagram usernames using dots, underscores, and keyword styles."
  },
  {
    "name": "YouTube Channel Name Generator",
    "url": "generator-tools/youtube-channel-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate catching names for your YouTube channel based on category niches."
  },
  {
    "name": "Business Name Generator",
    "url": "generator-tools/business-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate catchy and brandable ideas for your company or business."
  },
  {
    "name": "Brand Name Generator",
    "url": "generator-tools/brand-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate unique, abstract, and brandable names using vowel-consonant blending."
  },
  {
    "name": "Startup Name Generator",
    "url": "generator-tools/startup-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate modern, punchy, tech-focused startup name ideas."
  },
  {
    "name": "Domain Name Generator",
    "url": "generator-tools/domain-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Check domain name availability suggestions based on your name or brand."
  },
  {
    "name": "Nickname Generator",
    "url": "generator-tools/nickname-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate cute, funny, or cool nicknames based on standard traits."
  },
  {
    "name": "Gamer Name Generator",
    "url": "generator-tools/gamer-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate epic gamer tags and multiplayer aliases."
  },
  {
    "name": "Fantasy Name Generator",
    "url": "generator-tools/fantasy-name-generator.html",
    "category": "Generator Tools (Username & Name Generators)",
    "desc": "Generate medieval, elven, or dwarven fantasy names for games and writing."
  },
  {
    "name": "Password Generator",
    "url": "generator-tools/password-generator-tool.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate custom passwords with selectable length, letters, numbers, and symbols."
  },
  {
    "name": "Secure Password Generator",
    "url": "generator-tools/secure-password-generator-tool.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate strong, cryptographically secure passwords utilizing browser-native Web Crypto API."
  },
  {
    "name": "Passphrase Generator",
    "url": "generator-tools/passphrase-generator-tool.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate easy-to-remember but hard-to-crack random passphrases."
  },
  {
    "name": "PIN Generator",
    "url": "generator-tools/pin-generator.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate numerical Personal Identification Numbers (PINs) of custom length."
  },
  {
    "name": "API Key Generator",
    "url": "generator-tools/api-key-generator.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate custom API secret tokens and access client keys."
  },
  {
    "name": "UUID Generator",
    "url": "generator-tools/uuid-generator-tool.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate RFC4122 Version 4 Universally Unique Identifiers."
  },
  {
    "name": "Random Token Generator",
    "url": "generator-tools/random-token-generator.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate random alphanumeric, hex, or base64 tokens of a custom length."
  },
  {
    "name": "Secret Key Generator",
    "url": "generator-tools/secret-key-generator.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate strong, high-entropy cryptographic secret keys for cookie or JWT signing."
  },
  {
    "name": "Session ID Generator",
    "url": "generator-tools/session-id-generator.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate standard session identifiers for cookies and database testing."
  },
  {
    "name": "Encryption Key Generator",
    "url": "generator-tools/encryption-key-generator.html",
    "category": "Generator Tools (Password & Security Generators)",
    "desc": "Generate standard 128-bit, 192-bit, or 256-bit symmetric encryption keys."
  },
  {
    "name": "YouTube Title Generator",
    "url": "generator-tools/youtube-title-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate click-worthy and optimized titles for your YouTube videos."
  },
  {
    "name": "YouTube Description Generator",
    "url": "generator-tools/youtube-description-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate complete description outlines for YouTube uploads containing chapters and links."
  },
  {
    "name": "YouTube Tag Generator",
    "url": "generator-tools/youtube-tag-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate search-optimized tags and keywords for your YouTube videos."
  },
  {
    "name": "Blog Title Generator",
    "url": "generator-tools/blog-title-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate catchy blog post headlines to attract readers."
  },
  {
    "name": "Blog Idea Generator",
    "url": "generator-tools/blog-idea-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate creative blog ideas and concept outlines."
  },
  {
    "name": "Article Idea Generator",
    "url": "generator-tools/article-idea-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate article outlines, hooks, and research directions."
  },
  {
    "name": "Headline Generator",
    "url": "generator-tools/headline-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate powerful headlines for landing pages, ads, and newsletters."
  },
  {
    "name": "Hook Generator",
    "url": "generator-tools/hook-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate attention-grabbing hooks to start your essays or videos."
  },
  {
    "name": "CTA Generator",
    "url": "generator-tools/cta-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate effective Call to Action (CTA) buttons and copy tags."
  },
  {
    "name": "Social Media Caption Generator",
    "url": "generator-tools/social-caption-generator.html",
    "category": "Generator Tools (Content Creator Generators)",
    "desc": "Generate captions for Instagram, LinkedIn, or Twitter/X posts."
  },
  {
    "name": "Meta Title Generator",
    "url": "generator-tools/meta-title-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate search-optimized page meta titles matching Google's character limit."
  },
  {
    "name": "Meta Description Generator",
    "url": "generator-tools/meta-description-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate click-worthy and search-optimized meta description tags."
  },
  {
    "name": "Schema Markup Generator",
    "url": "generator-tools/schema-markup-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate website structured JSON-LD schema tags for search engines."
  },
  {
    "name": "Sitemap Generator",
    "url": "generator-tools/sitemap-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate standard XML sitemaps for search engine indexing submissions."
  },
  {
    "name": "Robots.txt Generator",
    "url": "generator-tools/robots-txt-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate custom robots.txt directives for search crawlers."
  },
  {
    "name": "Canonical URL Generator",
    "url": "generator-tools/canonical-url-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate canonical URL tag links to prevent duplicate page indexing issues."
  },
  {
    "name": "Open Graph Generator",
    "url": "generator-tools/open-graph-generator.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate Facebook Open Graph meta tags for beautiful social sharing previews."
  },
  {
    "name": "Twitter Card Generator",
    "url": "generator-tools/twitter-card-generator.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate Twitter / X Card meta tags for rich social post attachments."
  },
  {
    "name": "FAQ Schema Generator",
    "url": "generator-tools/faq-schema-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate structured JSON-LD FAQPage schemas to qualify for Google search rich snippets."
  },
  {
    "name": "Hreflang Generator",
    "url": "generator-tools/hreflang-generator-tool.html",
    "category": "Generator Tools (SEO Generators)",
    "desc": "Generate localized hreflang link tags for international multi-language SEO sites."
  },
  {
    "name": "Hashtag Generator",
    "url": "generator-tools/hashtag-generator-tool.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate trending hashtags for Instagram, Twitter, and TikTok posts based on keywords."
  },
  {
    "name": "Instagram Bio Generator",
    "url": "generator-tools/instagram-bio-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate attractive, structured bios with emojis for your Instagram profile."
  },
  {
    "name": "TikTok Bio Generator",
    "url": "generator-tools/tiktok-bio-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate punchy and short bios matching TikTok's character limit."
  },
  {
    "name": "LinkedIn Headline Generator",
    "url": "generator-tools/linkedin-headline-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate professional headlines to attract recruiters and profile visits."
  },
  {
    "name": "Facebook Post Generator",
    "url": "generator-tools/facebook-post-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate engaging Facebook posts with headlines and calls to action."
  },
  {
    "name": "Twitter/X Post Generator",
    "url": "generator-tools/twitter-post-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate short, punchy tweets within Twitter's 280-character limit."
  },
  {
    "name": "YouTube Bio Generator",
    "url": "generator-tools/youtube-bio-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate description copy for your YouTube channel About page."
  },
  {
    "name": "Pinterest Description Generator",
    "url": "generator-tools/pinterest-description-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate search-friendly Pinterest pin descriptions with target hashtags."
  },
  {
    "name": "Social Media Username Generator",
    "url": "generator-tools/social-username-generator-tool.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate general social media handle suggestions checkable across networks."
  },
  {
    "name": "Influencer Name Generator",
    "url": "generator-tools/influencer-name-generator.html",
    "category": "Generator Tools (Social Media Generators)",
    "desc": "Generate catchy personal brand and influencer names."
  },
  {
    "name": "Email Subject Generator",
    "url": "generator-tools/email-subject-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate professional, eye-catching, and click-worthy email subject lines."
  },
  {
    "name": "Professional Email Generator",
    "url": "generator-tools/professional-email-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate complete, polished drafts for standard business communication emails."
  },
  {
    "name": "Business Slogan Generator",
    "url": "generator-tools/business-slogan-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate catchy slogans and brand taglines for your company."
  },
  {
    "name": "Business Mission Statement Generator",
    "url": "generator-tools/business-mission-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate clear, professional mission statements for your brand."
  },
  {
    "name": "Invoice Number Generator",
    "url": "generator-tools/invoice-number-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate unique invoice serial numbers based on prefix formats."
  },
  {
    "name": "Company Name Generator",
    "url": "generator-tools/company-name-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate professional corporate names for your startup or enterprise."
  },
  {
    "name": "Product Name Generator",
    "url": "generator-tools/product-name-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate catchy, modern names for your product or SaaS application."
  },
  {
    "name": "Product Description Generator",
    "url": "generator-tools/product-description-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate promotional description paragraphs for marketing listings."
  },
  {
    "name": "Business Tagline Generator",
    "url": "generator-tools/business-tagline-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate inspiring business taglines to display under your brand logo."
  },
  {
    "name": "Business Idea Generator",
    "url": "generator-tools/business-idea-generator.html",
    "category": "Generator Tools (Email & Business Generators)",
    "desc": "Generate startup and side-hustle business ideas by combining industries."
  },
  {
    "name": "Color Palette Generator",
    "url": "generator-tools/color-palette-generator-tool.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate cohesive 5-color palettes based on styling tones."
  },
  {
    "name": "Gradient Generator",
    "url": "generator-tools/gradient-generator-tool.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate CSS gradients and visual hex properties."
  },
  {
    "name": "CSS Gradient Generator",
    "url": "generator-tools/css-gradient-generator-tool.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate complete CSS background gradient property codes."
  },
  {
    "name": "Box Shadow Generator",
    "url": "generator-tools/box-shadow-generator-tool.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate CSS box-shadow properties with offset, blur, and spread selectors."
  },
  {
    "name": "Border Radius Generator",
    "url": "generator-tools/border-radius-generator-tool.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate CSS border-radius properties with four corner controls."
  },
  {
    "name": "SVG Pattern Generator",
    "url": "generator-tools/svg-pattern-generator.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate custom decorative SVG pattern styles client-side."
  },
  {
    "name": "QR Code Generator",
    "url": "generator-tools/qr-code-generator-tool.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate downloadable QR codes for links and text entirely client-side using local assets."
  },
  {
    "name": "Barcode Generator",
    "url": "generator-tools/barcode-generator.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate custom 1D barcodes client-side on a canvas element."
  },
  {
    "name": "Favicon Generator",
    "url": "generator-tools/favicon-generator.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate custom website favicons by drawing text/emojis on a canvas."
  },
  {
    "name": "Avatar Generator",
    "url": "generator-tools/avatar-generator.html",
    "category": "Generator Tools (Design Generators)",
    "desc": "Generate custom colored geometric avatars client-side."
  },
  {
    "name": "Random Number Generator",
    "url": "generator-tools/random-number-generator-tool.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Generate random integers within a custom specified minimum and maximum range."
  },
  {
    "name": "Random Letter Generator",
    "url": "generator-tools/random-letter-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Generate a random letter from the English alphabet (A-Z)."
  },
  {
    "name": "Random Color Generator",
    "url": "generator-tools/random-color-generator-tool.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Generate random HEX colors and show their values."
  },
  {
    "name": "Random Country Generator",
    "url": "generator-tools/random-country-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Get a random country name, capital, and region detail."
  },
  {
    "name": "Random City Generator",
    "url": "generator-tools/random-city-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Get a random famous global city name and its country."
  },
  {
    "name": "Random Date Generator",
    "url": "generator-tools/random-date-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Generate a random calendar date between two specified years."
  },
  {
    "name": "Random Time Generator",
    "url": "generator-tools/random-time-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Generate random clock times in 12-hour or 24-hour formatting."
  },
  {
    "name": "Random Emoji Generator",
    "url": "generator-tools/random-emoji-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Get a random emoji from common smiley, nature, and food categories."
  },
  {
    "name": "Random Fact Generator",
    "url": "generator-tools/random-fact-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Get interesting, funny, or educational random facts."
  },
  {
    "name": "Random Challenge Generator",
    "url": "generator-tools/random-challenge-generator.html",
    "category": "Generator Tools (Random Generators)",
    "desc": "Get random mini challenges for coding, fitness, or self-improvement."
  },
  {
    "name": "Fantasy Character Generator",
    "url": "generator-tools/fantasy-character-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate detailed fantasy character attributes, stats, and backstories."
  },
  {
    "name": "Superhero Name Generator",
    "url": "generator-tools/superhero-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate epic superhero aliases for comics and writing."
  },
  {
    "name": "Villain Name Generator",
    "url": "generator-tools/villain-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate dark and menacing villain name concepts."
  },
  {
    "name": "Team Name Generator",
    "url": "generator-tools/team-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate catchy team names for sports, gaming, or work projects."
  },
  {
    "name": "Clan Name Generator",
    "url": "generator-tools/clan-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate epic clan and guild names for multiplayer games."
  },
  {
    "name": "Pet Name Generator",
    "url": "generator-tools/pet-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate cute and unique names for your dog, cat, or bird."
  },
  {
    "name": "Baby Name Generator",
    "url": "generator-tools/baby-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate baby name ideas based on gender classifications."
  },
  {
    "name": "Rap Name Generator",
    "url": "generator-tools/rap-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate cool and punchy rap aliases."
  },
  {
    "name": "Band Name Generator",
    "url": "generator-tools/band-name-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate catchy rock, pop, or indie band name ideas."
  },
  {
    "name": "Movie Title Generator",
    "url": "generator-tools/movie-title-generator.html",
    "category": "Generator Tools (Fun & Entertainment Generators)",
    "desc": "Generate catch movie titles based on genres."
  },
  {
    "name": "JSON Generator",
    "url": "generator-tools/json-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate custom mock JSON objects with dynamic key-value pairs."
  },
  {
    "name": "Mock Data Generator",
    "url": "generator-tools/mock-data-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate lists of mock user names, emails, and phone numbers in CSV format."
  },
  {
    "name": "SQL Query Generator",
    "url": "generator-tools/sql-query-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate custom SQL INSERT statements for database seeding."
  },
  {
    "name": "API Response Generator",
    "url": "generator-tools/api-response-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate mock API response payloads for frontend testing."
  },
  {
    "name": "UUID Generator",
    "url": "generator-tools/uuid-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate version 4 UUID values client-side."
  },
  {
    "name": "JSON Schema Generator",
    "url": "generator-tools/json-schema-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate standard draft-07 JSON Schemas based on input JSON structures."
  },
  {
    "name": "HTML Boilerplate Generator",
    "url": "generator-tools/html-boilerplate-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate modern HTML5 index.html boilerplate codes."
  },
  {
    "name": "CSS Boilerplate Generator",
    "url": "generator-tools/css-boilerplate-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate clean CSS resets and custom variables boilerplates."
  },
  {
    "name": "Regex Generator",
    "url": "generator-tools/regex-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate regular expressions for emails, URLs, dates, or numeric values."
  },
  {
    "name": "Cron Expression Generator",
    "url": "generator-tools/cron-expression-generator-dev.html",
    "category": "Generator Tools (Developer Generators)",
    "desc": "Generate crontab expression scripts for scheduling tasks."
  },
  {
    "name": "To-Do List Generator",
    "url": "generator-tools/todo-list-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate custom, structured checklists for projects or daily tasks."
  },
  {
    "name": "Study Plan Generator",
    "url": "generator-tools/study-plan-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate study plans and calendars for learning goals."
  },
  {
    "name": "Workout Plan Generator",
    "url": "generator-tools/workout-plan-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate simple 3-day split workout routines."
  },
  {
    "name": "Daily Routine Generator",
    "url": "generator-tools/daily-routine-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate custom, productive daily routine timetables."
  },
  {
    "name": "Project Idea Generator",
    "url": "generator-tools/project-idea-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate creative ideas for coding side-projects."
  },
  {
    "name": "Startup Idea Generator",
    "url": "generator-tools/startup-idea-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate innovative tech startup ideas by crossing industries."
  },
  {
    "name": "Side Hustle Idea Generator",
    "url": "generator-tools/side-hustle-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate low-investment side hustle ideas."
  },
  {
    "name": "Marketing Plan Generator",
    "url": "generator-tools/marketing-plan-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate simple 4-step marketing plans for new product launches."
  },
  {
    "name": "Content Calendar Generator",
    "url": "generator-tools/content-calendar-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate 7-day social media content calendars."
  },
  {
    "name": "Goal Planner Generator",
    "url": "generator-tools/goal-planner-generator.html",
    "category": "Generator Tools (AI & Productivity Generators)",
    "desc": "Generate SMART goal planner worksheets."
  },
  {
    "name": "Keyword Density Checker",
    "url": "seo-web-tools/keyword-density-checker.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Analyze the keyword density and distribution of your content to prevent keyword stuffing."
  },
  {
    "name": "Keyword Position Checker",
    "url": "seo-web-tools/keyword-position-checker.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Check the occurrences and positional indices of keywords within your HTML or text content."
  },
  {
    "name": "Keyword Difficulty Estimator",
    "url": "seo-web-tools/keyword-difficulty-estimator.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Estimate search competition difficulty based on search volumes and backlink competitors."
  },
  {
    "name": "Keyword Frequency Analyzer",
    "url": "seo-web-tools/keyword-frequency-analyzer.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Analyze the frequency of single words, 2-grams, and 3-grams inside copy content."
  },
  {
    "name": "Content SEO Analyzer",
    "url": "seo-web-tools/content-seo-analyzer.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Analyze content structures including meta tags alignment, word counts, and header layouts."
  },
  {
    "name": "On-Page SEO Checker",
    "url": "seo-web-tools/on-page-seo-checker.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Check critical on-page SEO factors by analyzing raw HTML markup configurations."
  },
  {
    "name": "SEO Audit Tool",
    "url": "seo-web-tools/seo-audit-tool.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Execute a localized simulated SEO audit on your page structure and indexing settings."
  },
  {
    "name": "SEO Score Checker",
    "url": "seo-web-tools/seo-score-checker.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Calculate a percentage score evaluating the search readiness of your metadata."
  },
  {
    "name": "SEO Content Optimizer",
    "url": "seo-web-tools/seo-content-optimizer.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Optimize keyword placement and structure across content segments to maximize ranking opportunities."
  },
  {
    "name": "Search Snippet Preview Tool",
    "url": "seo-web-tools/search-snippet-preview-tool.html",
    "category": "SEO & Web Tools (SEO Analysis Tools)",
    "desc": "Visualize how your meta tag titles and descriptions display on search engine results pages."
  },
  {
    "name": "Meta Title Generator",
    "url": "seo-web-tools/meta-title-generator.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Generate optimized SEO title tag titles that align with search engine recommendations."
  },
  {
    "name": "Meta Description Generator",
    "url": "seo-web-tools/meta-description-generator-tool.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Generate search-friendly HTML description meta tags of the correct length."
  },
  {
    "name": "Meta Tags Generator",
    "url": "seo-web-tools/meta-tags-generator-tool.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Generate complete meta header tag packages including open-graph and robots configurations."
  },
  {
    "name": "Meta Tags Analyzer",
    "url": "seo-web-tools/meta-tags-analyzer.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Extract and analyze existing meta tags from a raw HTML header snippet."
  },
  {
    "name": "Open Graph Generator",
    "url": "seo-web-tools/open-graph-generator.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Create standard OpenGraph tags to customize your website's preview on platforms like Facebook and LinkedIn."
  },
  {
    "name": "Twitter Card Generator",
    "url": "seo-web-tools/twitter-card-generator.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Generate Twitter Card metadata to control how links look when shared on Twitter (X)."
  },
  {
    "name": "Canonical URL Generator",
    "url": "seo-web-tools/canonical-url-generator.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Generate canonical URL link tags to resolve duplicate content indexing issues."
  },
  {
    "name": "Robots Meta Generator",
    "url": "seo-web-tools/robots-meta-generator.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Generate meta robots tags to instruct crawlers on how to index and follow links on the page."
  },
  {
    "name": "Social Meta Preview Tool",
    "url": "seo-web-tools/social-meta-preview-tool.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Preview how shared links look on social networks like Facebook and Twitter (X)."
  },
  {
    "name": "SERP Preview Tool",
    "url": "seo-web-tools/serp-preview-tool.html",
    "category": "SEO & Web Tools (Meta Tag Tools)",
    "desc": "Simulate and preview search engine result snippets in desktop and mobile viewports."
  },
  {
    "name": "FAQ Schema Generator",
    "url": "seo-web-tools/faq-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate valid JSON-LD FAQ schema markup for your website in seconds."
  },
  {
    "name": "Article Schema Generator",
    "url": "seo-web-tools/article-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate Google-compliant Article JSON-LD schema markup to boost search appearance."
  },
  {
    "name": "Organization Schema Generator",
    "url": "seo-web-tools/organization-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate detailed Organization schema templates to establish your company credentials with search engines."
  },
  {
    "name": "Product Schema Generator",
    "url": "seo-web-tools/product-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate Product JSON-LD schemas incorporating price, reviews, and availability markers."
  },
  {
    "name": "Local Business Schema Generator",
    "url": "seo-web-tools/local-business-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate detailed LocalBusiness schemas incorporating hours, locations, and geocodes."
  },
  {
    "name": "Event Schema Generator",
    "url": "seo-web-tools/event-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate Event JSON-LD schema markup with schedules, location structures, and registration options."
  },
  {
    "name": "Breadcrumb Schema Generator",
    "url": "seo-web-tools/breadcrumb-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate BreadcrumbList JSON-LD tags to improve site navigation hierarchy in search result snippets."
  },
  {
    "name": "Website Schema Generator",
    "url": "seo-web-tools/website-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate WebSite JSON-LD tags incorporating searchbox queries to get sitelinks search boxes."
  },
  {
    "name": "Person Schema Generator",
    "url": "seo-web-tools/person-schema-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate Person JSON-LD schemas representing authors, founders, or key team members."
  },
  {
    "name": "JSON-LD Generator",
    "url": "seo-web-tools/json-ld-generator.html",
    "category": "SEO & Web Tools (Schema Markup Tools)",
    "desc": "Generate a baseline boilerplate structure for any custom JSON-LD schema type."
  },
  {
    "name": "Robots.txt Generator",
    "url": "seo-web-tools/robots-txt-generator.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Generate custom robots.txt crawl rules to direct bots safely through your site pages."
  },
  {
    "name": "Robots.txt Validator",
    "url": "seo-web-tools/robots-txt-validator.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Validate standard robots.txt formatting guidelines and index syntax patterns."
  },
  {
    "name": "XML Sitemap Generator",
    "url": "seo-web-tools/xml-sitemap-generator.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Generate XML sitemaps to index pages with crawl priorities and update dates."
  },
  {
    "name": "Sitemap Validator",
    "url": "seo-web-tools/sitemap-validator.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Check XML sitemap structures for syntactic tags validity and schema matches."
  },
  {
    "name": "Sitemap URL Extractor",
    "url": "seo-web-tools/sitemap-url-extractor.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Extract a plain-text list of page links from an XML sitemap source block."
  },
  {
    "name": "URL Inspection Tool",
    "url": "seo-web-tools/url-inspection-tool.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Inspect URLs structure safety, protocols, subdirectories depth, and query parameters."
  },
  {
    "name": "URL Analyzer",
    "url": "seo-web-tools/url-analyzer.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Check URL layout structures for SEO-friendliness, lowercase consistency, and character lengths."
  },
  {
    "name": "Redirect Generator",
    "url": "seo-web-tools/redirect-generator.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Generate Apache .htaccess or Nginx redirection config scripts."
  },
  {
    "name": "Redirect Checker",
    "url": "seo-web-tools/redirect-checker.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Check redirect paths and HTTP header responses to verify redirection rules."
  },
  {
    "name": "Canonical URL Checker",
    "url": "seo-web-tools/canonical-url-checker.html",
    "category": "SEO & Web Tools (Webmaster Tools)",
    "desc": "Extract and check if canonical links are configured correctly inside HTML files."
  },
  {
    "name": "Title Length Checker",
    "url": "seo-web-tools/title-length-checker.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Check character counts and pixel widths of title tags to ensure they fit in search results."
  },
  {
    "name": "Meta Description Length Checker",
    "url": "seo-web-tools/meta-description-length-checker.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Evaluate meta descriptions for optimal character lengths and pixel widths."
  },
  {
    "name": "Heading Structure Analyzer",
    "url": "seo-web-tools/heading-structure-analyzer.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Analyze HTML heading outlines and tag hierarchies (H1 to H6) for structural health."
  },
  {
    "name": "Readability Checker",
    "url": "seo-web-tools/readability-checker.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Calculate a Flesch Reading Ease score to optimize your content readability."
  },
  {
    "name": "Word Counter",
    "url": "seo-web-tools/word-counter-tool.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Count words, characters, sentences, and paragraphs in your content real-time."
  },
  {
    "name": "Keyword Extractor",
    "url": "seo-web-tools/keyword-extractor.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Extract high-density single and multi-word terms from your content, ignoring stop words."
  },
  {
    "name": "N-Gram Generator",
    "url": "seo-web-tools/n-gram-generator.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Generate n-gram phrases (words sequences) from your copy content."
  },
  {
    "name": "Internal Link Analyzer",
    "url": "seo-web-tools/internal-link-analyzer.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Analyze HTML contents to extract, verify, and count internal vs. external links."
  },
  {
    "name": "Content Density Checker",
    "url": "seo-web-tools/content-density-checker.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Check paragraph lengths and distribution of word densities across content segments."
  },
  {
    "name": "Content Optimization Tool",
    "url": "seo-web-tools/content-optimization-tool.html",
    "category": "SEO & Web Tools (Content SEO Tools)",
    "desc": "Optimize headings, keywords, and text distribution inside content layouts."
  },
  {
    "name": "Internal Link Generator",
    "url": "seo-web-tools/internal-link-generator.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Generate relative and absolute internal anchor link HTML tags based on keyword selections."
  },
  {
    "name": "Link Analyzer",
    "url": "seo-web-tools/link-analyzer.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Extract and inspect all anchor links, rel tags, and destinations inside an HTML segment."
  },
  {
    "name": "Anchor Text Generator",
    "url": "seo-web-tools/anchor-text-generator.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Generate click-worthy and descriptive anchor texts matching standard link guidelines."
  },
  {
    "name": "Anchor Text Analyzer",
    "url": "seo-web-tools/anchor-text-analyzer.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Analyze distributions of anchor texts (generic, brand, exact match) from a list of links."
  },
  {
    "name": "Broken Link Checker",
    "url": "seo-web-tools/broken-link-checker.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Scan HTML code blocks for broken, empty, or improperly formatted links."
  },
  {
    "name": "Link Attribute Checker",
    "url": "seo-web-tools/link-attribute-checker.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Check HTML links to verify rel attributes (nofollow, noopener, noreferrer) for external URLs."
  },
  {
    "name": "Redirect Path Checker",
    "url": "seo-web-tools/redirect-path-checker.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Check and map redirection history paths to identify redirect loops."
  },
  {
    "name": "URL Cleaner",
    "url": "seo-web-tools/url-cleaner.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Clean and remove tracking tokens and query parameters (UTM, gclid, fbclid) from URLs."
  },
  {
    "name": "URL Builder",
    "url": "seo-web-tools/url-builder.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Build formatted URLs with custom key-value query parameters."
  },
  {
    "name": "UTM Link Generator",
    "url": "seo-web-tools/utm-link-generator.html",
    "category": "SEO & Web Tools (Link Tools)",
    "desc": "Create Google Analytics UTM tracking URLs with campaign sources, mediums, and terms."
  },
  {
    "name": "Hashtag Generator",
    "url": "seo-web-tools/hashtag-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Generate relevant hashtags based on a seed keyword to expand your social media reach."
  },
  {
    "name": "Social Preview Generator",
    "url": "seo-web-tools/social-preview-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Preview how shared links appear on popular social networks like Facebook and LinkedIn."
  },
  {
    "name": "Open Graph Preview Tool",
    "url": "seo-web-tools/open-graph-preview-tool.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Check Open Graph properties and display a Facebook style social preview."
  },
  {
    "name": "Twitter Card Preview Tool",
    "url": "seo-web-tools/twitter-card-preview-tool.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Check Twitter Card tags and render a Twitter (X) post mockup preview."
  },
  {
    "name": "YouTube Tag Generator",
    "url": "seo-web-tools/youtube-tag-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Generate relevant video tags to optimize your YouTube video rankings."
  },
  {
    "name": "YouTube SEO Analyzer",
    "url": "seo-web-tools/youtube-seo-analyzer.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Analyze YouTube video titles and descriptions to verify formatting standards."
  },
  {
    "name": "Video Title Generator",
    "url": "seo-web-tools/video-title-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Generate click-worthy and viral YouTube video titles using keyword templates."
  },
  {
    "name": "Video Description Generator",
    "url": "seo-web-tools/video-description-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Generate formatted description copy blueprints for your YouTube video uploads."
  },
  {
    "name": "Social Bio Generator",
    "url": "seo-web-tools/social-bio-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Generate custom biography copy for Twitter, Instagram, or LinkedIn profiles."
  },
  {
    "name": "Social Caption Generator",
    "url": "seo-web-tools/social-caption-generator.html",
    "category": "SEO & Web Tools (Social Media SEO Tools)",
    "desc": "Generate captions with structured spacing, emojis, and hashtags for social posts."
  },
  {
    "name": "Page Size Calculator",
    "url": "seo-web-tools/page-size-calculator.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Calculate the total weight of a page based on files sizes of HTML, CSS, images, and script assets."
  },
  {
    "name": "Asset Size Analyzer",
    "url": "seo-web-tools/asset-size-analyzer.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Calculate file size reductions and compression savings (Gzip/Brotli)."
  },
  {
    "name": "Image SEO Analyzer",
    "url": "seo-web-tools/image-seo-analyzer.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Check image tag code blocks for missing alt tags, incorrect sizes, and formatting issues."
  },
  {
    "name": "CSS Minifier",
    "url": "seo-web-tools/css-minifier.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Minify CSS code by stripping spaces, comments, and line breaks to improve page load speed."
  },
  {
    "name": "JavaScript Minifier",
    "url": "seo-web-tools/javascript-minifier.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Minify JavaScript code by removing comments, spacing, and line breaks."
  },
  {
    "name": "HTML Minifier",
    "url": "seo-web-tools/html-minifier.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Minify HTML source code by removing comments and unnecessary spaces."
  },
  {
    "name": "WebP Optimization Tool",
    "url": "seo-web-tools/webp-optimization-tool.html",
    "category": "SEO & Web Tools (WebPerformance Tools)",
    "desc": "Calculate size reductions and loading speed benefits of converting files to WebP."
  },
  {
    "name": "Lazy Load Generator",
    "url": "seo-web-tools/lazy-load-generator.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Generate HTML image tags with loading=lazy attributes to improve page load speed."
  },
  {
    "name": "Core Web Vitals Guide Tool",
    "url": "seo-web-tools/core-web-vitals-guide-tool.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Rate loading performance and stability based on Core Web Vitals metric inputs."
  },
  {
    "name": "Resource Optimization Analyzer",
    "url": "seo-web-tools/resource-optimization-analyzer.html",
    "category": "SEO & Web Tools (Web Performance Tools)",
    "desc": "Generate browser resource directives (preconnect, dns-prefetch, preload) to speed up asset loading."
  },
  {
    "name": "Domain Name Generator",
    "url": "seo-web-tools/domain-name-generator-seo.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Generate search-friendly domain name ideas based on brand seed terms."
  },
  {
    "name": "URL Encoder",
    "url": "seo-web-tools/url-encoder-seo.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Encode special characters in URLs using standard escape characters."
  },
  {
    "name": "URL Decoder",
    "url": "seo-web-tools/url-decoder-seo.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Decode percent-encoded URL parameters back to standard text strings."
  },
  {
    "name": "URL Parser",
    "url": "seo-web-tools/url-parser.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Parse URL strings into hostname, pathname, port, and query parameter tokens."
  },
  {
    "name": "URL Slug Generator",
    "url": "seo-web-tools/url-slug-generator.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Convert text headlines into SEO-friendly URL slug strings."
  },
  {
    "name": "URL Rewriter",
    "url": "seo-web-tools/url-rewriter.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Generate search-friendly URL rewrite rules from parameters-heavy links."
  },
  {
    "name": "Hreflang Generator",
    "url": "seo-web-tools/hreflang-generator.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Generate hreflang link tags to declare localized versions of your pages to search engines."
  },
  {
    "name": "Hreflang Validator",
    "url": "seo-web-tools/hreflang-validator.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Check hreflang link tags for formatting structure and valid ISO codes."
  },
  {
    "name": "Domain Authority Tracker",
    "url": "seo-web-tools/domain-authority-tracker.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Estimate search authority indicators based on backlinks profiles and domain age."
  },
  {
    "name": "Domain Age Checker",
    "url": "seo-web-tools/domain-age-checker.html",
    "category": "SEO & Web Tools (Domain & URL Tools)",
    "desc": "Calculate a domain's age in years, months, and days based on its registration date."
  },
  {
    "name": "CTR Calculator",
    "url": "seo-web-tools/ctr-calculator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Calculate the Click-Through Rate (CTR) of your marketing campaigns and organic listings."
  },
  {
    "name": "CPM Calculator",
    "url": "seo-web-tools/cpm-calculator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Calculate ad campaign costs per mille (thousand impressions)."
  },
  {
    "name": "CPC Calculator",
    "url": "seo-web-tools/cpc-calculator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Calculate the average Cost Per Click (CPC) for pay-per-click ad groups."
  },
  {
    "name": "Conversion Rate Calculator",
    "url": "seo-web-tools/conversion-rate-calculator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Calculate campaign conversion rates to measure lead and sales quality."
  },
  {
    "name": "ROI Calculator",
    "url": "seo-web-tools/roi-calculator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Calculate Return on Investment (ROI) percentages for marketing and business budgets."
  },
  {
    "name": "Marketing Budget Calculator",
    "url": "seo-web-tools/marketing-budget-calculator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Calculate target budget splits across SEO, PPC, and social media channels."
  },
  {
    "name": "Ad Copy Generator",
    "url": "seo-web-tools/ad-copy-generator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Generate Google Ads style search ad headlines and descriptions matching keyword seeds."
  },
  {
    "name": "Call-To-Action Generator",
    "url": "seo-web-tools/call-to-action-generator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Generate high-converting Call-To-Action button copy and hooks."
  },
  {
    "name": "Landing Page Headline Generator",
    "url": "seo-web-tools/landing-page-headline-generator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Generate landing page headlines based on product benefits and target audiences."
  },
  {
    "name": "Campaign Name Generator",
    "url": "seo-web-tools/campaign-name-generator.html",
    "category": "SEO & Web Tools (Marketing Tools)",
    "desc": "Generate clean marketing campaign name tokens matching standard parameters."
  },
  {
    "name": "SERP Snippet Preview Tool",
    "url": "seo-web-tools/serp-snippet-preview-google.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Preview how your page titles and snippets render in Google Desktop and Mobile search indexes."
  },
  {
    "name": "Featured Snippet Optimizer",
    "url": "seo-web-tools/featured-snippet-optimizer.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Check if your definition paragraphs match featured snippet requirements."
  },
  {
    "name": "Search Intent Analyzer",
    "url": "seo-web-tools/search-intent-analyzer.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Analyze keywords to classify target user intent into informational or transactional categories."
  },
  {
    "name": "FAQ Generator",
    "url": "seo-web-tools/faq-generator-google.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Generate search-friendly Frequently Asked Questions (FAQ) sets matching seed topics."
  },
  {
    "name": "Google Title Checker",
    "url": "seo-web-tools/google-title-checker.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Verify title tag lengths against Google desktop search truncation width limits."
  },
  {
    "name": "Google Description Checker",
    "url": "seo-web-tools/google-description-checker.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Check description lengths against Google snippet display limits."
  },
  {
    "name": "Mobile SERP Preview Tool",
    "url": "seo-web-tools/mobile-serp-preview-tool.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Simulate and preview how your search snippets look on mobile devices."
  },
  {
    "name": "Desktop SERP Preview Tool",
    "url": "seo-web-tools/desktop-serp-preview-tool.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Simulate and preview search snippet outputs on desktop monitors."
  },
  {
    "name": "SEO Checklist Generator",
    "url": "seo-web-tools/seo-checklist-generator.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Generate an interactive, printable SEO checklist for website optimization."
  },
  {
    "name": "Search Appearance Preview Tool",
    "url": "seo-web-tools/search-appearance-preview-tool.html",
    "category": "SEO & Web Tools (Google SEO Tools)",
    "desc": "Check how schema enhancements like FAQ drops display in Google search results."
  },
  {
    "name": "Local SEO Audit Tool",
    "url": "seo-web-tools/local-seo-audit-tool.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Check critical local SEO ranking factors for your business coordinates."
  },
  {
    "name": "Local Business Schema Generator",
    "url": "seo-web-tools/local-business-schema-generator-seo.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Generate detailed LocalBusiness JSON-LD markup blocks for geographic listings."
  },
  {
    "name": "NAP Consistency Checker",
    "url": "seo-web-tools/nap-consistency-checker.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Verify if Name, Address, and Phone details are identical across various website and directory platforms."
  },
  {
    "name": "Google Business Description Generator",
    "url": "seo-web-tools/google-business-description-generator.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Generate optimized Google Business Profile descriptions (up to 750 characters)."
  },
  {
    "name": "Service Area Generator",
    "url": "seo-web-tools/service-area-generator.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Generate structured service area coverage lists and geo coordinates."
  },
  {
    "name": "Local Keyword Generator",
    "url": "seo-web-tools/local-keyword-generator.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Generate local keywords combining business services with target cities."
  },
  {
    "name": "Location Landing Page Generator",
    "url": "seo-web-tools/location-landing-page-generator.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Generate standard boilerplate copy layouts for geo-targeted location pages."
  },
  {
    "name": "Citation Builder",
    "url": "seo-web-tools/citation-builder.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Compile business registration citations for yelp and yellowpages directory listings."
  },
  {
    "name": "Business Category Generator",
    "url": "seo-web-tools/business-category-generator.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Suggest standard primary Google Business Profile categories based on keywords."
  },
  {
    "name": "Review Response Generator",
    "url": "seo-web-tools/review-response-generator.html",
    "category": "SEO & Web Tools (Local SEO Tools)",
    "desc": "Generate professional and positive review response templates for client feedback."
  },
  {
    "name": "Blog Title Generator",
    "url": "seo-web-tools/blog-title-generator-seo.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate catchy blog title ideas based on topic keywords."
  },
  {
    "name": "Meta Description Generator",
    "url": "seo-web-tools/meta-description-generator-seo.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate custom search-friendly meta descriptions containing target keywords."
  },
  {
    "name": "FAQ Generator",
    "url": "seo-web-tools/faq-generator-seo.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate lists of frequently asked questions to optimize content layout."
  },
  {
    "name": "Content Brief Generator",
    "url": "seo-web-tools/content-brief-generator.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate detailed content briefings containing outlines and target keywords for copywriters."
  },
  {
    "name": "Keyword Cluster Generator",
    "url": "seo-web-tools/keyword-cluster-generator.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Group related keywords into semantic thematic clusters for content planning."
  },
  {
    "name": "Blog Outline Generator",
    "url": "seo-web-tools/blog-outline-generator.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate complete blog post outlines and subheading structures based on topic keywords."
  },
  {
    "name": "SEO Content Planner",
    "url": "seo-web-tools/seo-content-planner.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate structured SEO content checklists for pages launch."
  },
  {
    "name": "Search Intent Generator",
    "url": "seo-web-tools/search-intent-generator.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate search query suggestions matching specific user intents."
  },
  {
    "name": "Topic Cluster Generator",
    "url": "seo-web-tools/topic-cluster-generator.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Map core topics to support pillar-and-cluster SEO content models."
  },
  {
    "name": "Content Calendar Generator",
    "url": "seo-web-tools/content-calendar-generator-seo.html",
    "category": "SEO & Web Tools (AI SEO & Content Tools)",
    "desc": "Generate a weekly content calendar posting schedule."
  },
  {
    "name": "Calculator",
    "url": "math-tools/calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "A clean, functional online calculator for basic arithmetic operations."
  },
  {
    "name": "Scientific Calculator",
    "url": "math-tools/scientific-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Perform advanced scientific operations like trigonometry, exponents, and logarithms."
  },
  {
    "name": "Percentage Calculator",
    "url": "math-tools/percentage-calculator-math.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Calculate basic percentage values, increases, and differences instantly."
  },
  {
    "name": "Fraction Calculator",
    "url": "math-tools/fraction-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Add, subtract, multiply, and divide fractions with simplified outputs."
  },
  {
    "name": "Decimal Calculator",
    "url": "math-tools/decimal-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Convert decimals to fractions or percentages and round them to selected decimals."
  },
  {
    "name": "Ratio Calculator",
    "url": "math-tools/ratio-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Simplify a ratio A:B, or solve ratio equations like A:B = C:D for missing terms."
  },
  {
    "name": "Proportion Calculator",
    "url": "math-tools/proportion-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Solve for missing variables in proportional values format A/B = C/D."
  },
  {
    "name": "Average Calculator",
    "url": "math-tools/average-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Find the sum, count, and average value of a series of numbers."
  },
  {
    "name": "Mean Calculator",
    "url": "math-tools/mean-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Calculate Arithmetic Mean, Geometric Mean, and Harmonic Mean of a group of numbers."
  },
  {
    "name": "Weighted Average Calculator",
    "url": "math-tools/weighted-average-calculator.html",
    "category": "Math & Numbers (Basic Math Tools)",
    "desc": "Calculate the weighted average of values associated with different weights."
  },
  {
    "name": "Prime Number Checker",
    "url": "math-tools/prime-number-checker.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Check if a number is prime and retrieve its divisor breakdown."
  },
  {
    "name": "Prime Number Generator",
    "url": "math-tools/prime-number-generator.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Generate a list of prime numbers within a specified boundary range."
  },
  {
    "name": "Even Odd Checker",
    "url": "math-tools/even-odd-checker.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Quickly verify if an integer is even or odd."
  },
  {
    "name": "Number To Words Converter",
    "url": "math-tools/number-to-words-converter.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Convert numbers to their English word representation."
  },
  {
    "name": "Words To Number Converter",
    "url": "math-tools/words-to-number-converter.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Translate written English words into numeric digits."
  },
  {
    "name": "Number Sequence Generator",
    "url": "math-tools/number-sequence-generator.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Generate custom arithmetic or geometric series progression listings."
  },
  {
    "name": "Number Pattern Generator",
    "url": "math-tools/number-pattern-generator.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Generate famous mathematical sequences like Fibonacci, square, and triangular patterns."
  },
  {
    "name": "Number Comparator",
    "url": "math-tools/number-comparator.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Compare multiple numbers to find minimum, maximum, and sort them."
  },
  {
    "name": "Number Splitter",
    "url": "math-tools/number-splitter.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Split numbers into place values or generate their prime factorization."
  },
  {
    "name": "Number Joiner",
    "url": "math-tools/number-joiner.html",
    "category": "Math & Numbers (Number Calculators)",
    "desc": "Join separate digits or comma-separated number items into a single integer using custom separators."
  },
  {
    "name": "Algebra Calculator",
    "url": "math-tools/algebra-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Evaluate linear and basic algebraic expressions step-by-step."
  },
  {
    "name": "Equation Solver",
    "url": "math-tools/equation-solver.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Solve mathematical equations of standard format ax + b = cx + d."
  },
  {
    "name": "Linear Equation Solver",
    "url": "math-tools/linear-equation-solver.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Solve systems of two linear equations in two variables: a1 x + b1 y = c1 and a2 x + b2 y = c2."
  },
  {
    "name": "Quadratic Equation Solver",
    "url": "math-tools/quadratic-equation-solver.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Solve quadratic equations of standard form ax^2 + bx + c = 0."
  },
  {
    "name": "Polynomial Calculator",
    "url": "math-tools/polynomial-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Evaluate polynomial expressions at a given point x."
  },
  {
    "name": "Factorization Calculator",
    "url": "math-tools/factorization-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Find factors and factorizations of quadratic equations or numeric values."
  },
  {
    "name": "Simplify Expression Calculator",
    "url": "math-tools/simplify-expression-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Expand and simplify standard algebraic mathematical expressions like a(bx + c) + d."
  },
  {
    "name": "Logarithm Calculator",
    "url": "math-tools/logarithm-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Calculate logarithms for any positive base value."
  },
  {
    "name": "Exponent Calculator",
    "url": "math-tools/exponent-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Raise values to any power base instantly."
  },
  {
    "name": "Root Calculator",
    "url": "math-tools/root-calculator.html",
    "category": "Math & Numbers (Algebra Tools)",
    "desc": "Calculate square root, cube root, or any custom nth root value."
  },
  {
    "name": "Area Calculator",
    "url": "math-tools/area-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate the surface area of basic geometrical shapes (Circle, Rectangle, Triangle)."
  },
  {
    "name": "Perimeter Calculator",
    "url": "math-tools/perimeter-calculator.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate perimeter boundaries for circles, rectangles, and regular polygons."
  },
  {
    "name": "Volume Calculator",
    "url": "math-tools/volume-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate volume metrics for solid geometric shapes (Cylinder, Sphere, Cube)."
  },
  {
    "name": "Surface Area Calculator",
    "url": "math-tools/surface-area-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate total boundary surface area of cylinders, spheres, and cubes."
  },
  {
    "name": "Triangle Calculator",
    "url": "math-tools/triangle-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate angles, sides, perimeter, and area parameters of triangles."
  },
  {
    "name": "Circle Calculator",
    "url": "math-tools/circle-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate circle parameters like area, circumference, diameter, and radius."
  },
  {
    "name": "Rectangle Calculator",
    "url": "math-tools/rectangle-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Compute perimeter, area, and diagonal lengths of a rectangle."
  },
  {
    "name": "Square Calculator",
    "url": "math-tools/square-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate perimeter, area, and diagonal dimensions of a square given its side."
  },
  {
    "name": "Trapezoid Calculator",
    "url": "math-tools/trapezoid-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate the area and height properties of a trapezoid shape."
  },
  {
    "name": "Polygon Calculator",
    "url": "math-tools/polygon-calculator-math.html",
    "category": "Math & Numbers (Geometry Tools)",
    "desc": "Calculate properties like interior angles and area for regular polygons."
  },
  {
    "name": "Sine Calculator",
    "url": "math-tools/sine-calculator.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Calculate the sine value of any angle in degrees or radians."
  },
  {
    "name": "Cosine Calculator",
    "url": "math-tools/cosine-calculator.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Calculate the cosine value of an angle in degrees or radians."
  },
  {
    "name": "Tangent Calculator",
    "url": "math-tools/tangent-calculator.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Calculate the tangent value of an angle in degrees or radians."
  },
  {
    "name": "Inverse Trigonometry Calculator",
    "url": "math-tools/inverse-trigonometry-calculator.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Calculate inverse trig values (arcsin, arccos, arctan) in degrees or radians."
  },
  {
    "name": "Right Triangle Solver",
    "url": "math-tools/right-triangle-solver.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Solve for missing sides and angles in a right-angled triangle."
  },
  {
    "name": "Pythagorean Theorem Calculator",
    "url": "math-tools/pythagorean-theorem-calculator-math.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Calculate missing lengths of right triangle sides using standard Pythagorean rules."
  },
  {
    "name": "Angle Converter",
    "url": "math-tools/angle-converter.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Convert angles bidirectionally between degrees, radians, gradians, and turns."
  },
  {
    "name": "Degree To Radian Converter",
    "url": "math-tools/degree-to-radian-converter.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Quickly convert angles from degrees to radians."
  },
  {
    "name": "Radian To Degree Converter",
    "url": "math-tools/radian-to-degree-converter.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Quickly convert angles from radians to degrees."
  },
  {
    "name": "Trigonometry Solver",
    "url": "math-tools/trigonometry-solver.html",
    "category": "Math & Numbers (Trigonometry Tools)",
    "desc": "Solve for basic ratios: sine, cosine, tangent, cosecant, secant, and cotangent of an angle."
  },
  {
    "name": "Mean Calculator",
    "url": "math-tools/mean-calculator-stats.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate Arithmetic Mean of a set of statistical numbers."
  },
  {
    "name": "Median Calculator",
    "url": "math-tools/median-calculator-math.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Locate the middle value element in a sorted numerical dataset."
  },
  {
    "name": "Mode Calculator",
    "url": "math-tools/mode-calculator-math.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Locate the most frequent value element(s) in a numerical series."
  },
  {
    "name": "Range Calculator",
    "url": "math-tools/range-calculator.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate the difference between the highest and lowest values in a statistical group."
  },
  {
    "name": "Standard Deviation Calculator",
    "url": "math-tools/standard-deviation-calculator-math.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate population or sample standard deviation metrics for a set of numbers."
  },
  {
    "name": "Variance Calculator",
    "url": "math-tools/variance-calculator.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate statistical variance of a list of numbers."
  },
  {
    "name": "Probability Calculator",
    "url": "math-tools/probability-calculator-math.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate single event probabilities, union, intersection, and conditional probability properties."
  },
  {
    "name": "Percentile Calculator",
    "url": "math-tools/percentile-calculator.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate the k-th percentile value of an input set of numbers."
  },
  {
    "name": "Z-Score Calculator",
    "url": "math-tools/z-score-calculator.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Calculate standard score (z-score) indicating deviations from the mean."
  },
  {
    "name": "Statistics Calculator",
    "url": "math-tools/statistics-calculator.html",
    "category": "Math & Numbers (Statistics Tools)",
    "desc": "Perform comprehensive statistical analysis on a set of numbers."
  },
  {
    "name": "Matrix Calculator",
    "url": "math-tools/matrix-calculator-math.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Add, subtract, and multiply 2x2 matrices."
  },
  {
    "name": "Matrix Determinant Calculator",
    "url": "math-tools/matrix-determinant-calculator.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Calculate the determinant of a 2x2 matrix."
  },
  {
    "name": "Matrix Inverse Calculator",
    "url": "math-tools/matrix-inverse-calculator.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Calculate the inverse of a 2x2 matrix."
  },
  {
    "name": "Vector Calculator",
    "url": "math-tools/vector-calculator.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Calculate vector addition, dot product, and cross product for two 3D vectors."
  },
  {
    "name": "Complex Number Calculator",
    "url": "math-tools/complex-number-calculator.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Add, subtract, and multiply complex numbers of format a + bi."
  },
  {
    "name": "Scientific Notation Calculator",
    "url": "math-tools/scientific-notation-calculator-math.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Multiply or divide numbers configured in scientific notations format (a * 10^b)."
  },
  {
    "name": "Binary Calculator",
    "url": "math-tools/binary-calculator-math.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Perform addition, subtraction, multiplication, and division on binary strings."
  },
  {
    "name": "Hex Calculator",
    "url": "math-tools/hex-calculator.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Perform mathematical calculations on hexadecimal (base-16) number values."
  },
  {
    "name": "Octal Calculator",
    "url": "math-tools/octal-calculator.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Perform mathematical calculations on octal (base-8) number values."
  },
  {
    "name": "Base Converter",
    "url": "math-tools/base-converter-math.html",
    "category": "Math & Numbers (Advanced Math Tools)",
    "desc": "Convert values from any base (from 2 to 36) to another base."
  },
  {
    "name": "Compound Interest Calculator",
    "url": "math-tools/compound-interest-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate standard compound interest growth schedules for investment budgets."
  },
  {
    "name": "Simple Interest Calculator",
    "url": "math-tools/simple-interest-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate simple interest values using the principal, rate, and time parameters."
  },
  {
    "name": "Loan Calculator",
    "url": "math-tools/loan-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate total payments and interest accrued over the life of a loan."
  },
  {
    "name": "EMI Calculator",
    "url": "math-tools/emi-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate Equated Monthly Installments (EMI) for home, car, or personal loans."
  },
  {
    "name": "ROI Calculator",
    "url": "math-tools/roi-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate Return on Investment percentage and gains."
  },
  {
    "name": "Discount Calculator",
    "url": "math-tools/discount-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate discount savings and final discounted price."
  },
  {
    "name": "Profit Calculator",
    "url": "math-tools/profit-calculator.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate cost margins, absolute profits, and markups."
  },
  {
    "name": "Margin Calculator",
    "url": "math-tools/margin-calculator.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate profit margins, selling prices, and markups based on cost and target margin."
  },
  {
    "name": "Break Even Calculator",
    "url": "math-tools/break-even-calculator-math.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate units count required to break even based on fixed costs and pricing."
  },
  {
    "name": "Investment Growth Calculator",
    "url": "math-tools/investment-growth-calculator.html",
    "category": "Math & Numbers (Financial Math Tools)",
    "desc": "Calculate future investment values for recurring deposits."
  },
  {
    "name": "Decimal To Binary Converter",
    "url": "math-tools/decimal-to-binary-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert standard base-10 decimal integers to base-2 binary strings."
  },
  {
    "name": "Binary To Decimal Converter",
    "url": "math-tools/binary-to-decimal-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert base-2 binary strings to base-10 decimal numbers."
  },
  {
    "name": "Decimal To Hex Converter",
    "url": "math-tools/decimal-to-hex-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert base-10 decimal integers to base-16 hexadecimal codes."
  },
  {
    "name": "Hex To Decimal Converter",
    "url": "math-tools/hex-to-decimal-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert base-16 hexadecimal codes to base-10 decimal integers."
  },
  {
    "name": "Decimal To Octal Converter",
    "url": "math-tools/decimal-to-octal-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert base-10 decimal integers to base-8 octal strings."
  },
  {
    "name": "Octal To Decimal Converter",
    "url": "math-tools/octal-to-decimal-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert base-8 octal strings to base-10 decimal integers."
  },
  {
    "name": "Roman Numeral Converter",
    "url": "math-tools/roman-numeral-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert standard numbers to Roman numerals or vice versa."
  },
  {
    "name": "Number Base Converter",
    "url": "math-tools/number-base-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Translate value representations across multiple base radix formats."
  },
  {
    "name": "Scientific Notation Converter",
    "url": "math-tools/scientific-notation-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Convert standard decimal numbers to scientific notation form."
  },
  {
    "name": "Percentage To Decimal Converter",
    "url": "math-tools/percentage-to-decimal-converter.html",
    "category": "Math & Numbers (Number Converters)",
    "desc": "Translate percentage values to their decimal equivalents."
  },
  {
    "name": "Unit Converter",
    "url": "math-tools/unit-converter-math.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Convert standard physical units between imperial and metric units."
  },
  {
    "name": "Density Calculator",
    "url": "math-tools/density-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate density, mass, or volume properties of a material."
  },
  {
    "name": "Force Calculator",
    "url": "math-tools/force-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate absolute physical force based on mass and acceleration values."
  },
  {
    "name": "Velocity Calculator",
    "url": "math-tools/velocity-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate physical velocity based on distance and travel time."
  },
  {
    "name": "Acceleration Calculator",
    "url": "math-tools/acceleration-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate average acceleration from initial and final velocity."
  },
  {
    "name": "Pressure Calculator",
    "url": "math-tools/pressure-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate pressure based on perpendicular force and surface area."
  },
  {
    "name": "Power Calculator",
    "url": "math-tools/power-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate engineering power based on work done and time interval."
  },
  {
    "name": "Energy Calculator",
    "url": "math-tools/energy-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate kinetic energy based on mass and velocity parameters."
  },
  {
    "name": "Torque Calculator",
    "url": "math-tools/torque-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Calculate physical torque based on force, radius, and application angle."
  },
  {
    "name": "Electrical Calculator",
    "url": "math-tools/electrical-calculator.html",
    "category": "Math & Numbers (Engineering Calculators)",
    "desc": "Apply Ohm's law to solve for Voltage, Current, or Resistance."
  },
  {
    "name": "GPA Calculator",
    "url": "math-tools/gpa-calculator-math.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate your grade point average (GPA) based on class grades and credit weights."
  },
  {
    "name": "CGPA Calculator",
    "url": "math-tools/cgpa-calculator-math.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate your cumulative grade point average (CGPA) from semester GPAs."
  },
  {
    "name": "Marks Percentage Calculator",
    "url": "math-tools/marks-percentage-calculator-math.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate your score percentage from obtained and maximum possible marks."
  },
  {
    "name": "Grade Calculator",
    "url": "math-tools/grade-calculator-math.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Estimate the final class grade using homework, exam, and quiz weight percentages."
  },
  {
    "name": "Attendance Calculator",
    "url": "math-tools/attendance-calculator-math.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate attendance percentage or classes needed to hit target percentage."
  },
  {
    "name": "Study Time Calculator",
    "url": "math-tools/study-time-calculator-math.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate average study time allocations required to prepare for exams."
  },
  {
    "name": "Score Calculator",
    "url": "math-tools/score-calculator.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Find your test score based on total questions and incorrect answers."
  },
  {
    "name": "Exam Percentage Calculator",
    "url": "math-tools/exam-percentage-calculator.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate the percentage weight contribution of an exam score to your final grade."
  },
  {
    "name": "Ranking Calculator",
    "url": "math-tools/ranking-calculator.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Convert a numerical rank into a percentile ranking class."
  },
  {
    "name": "Academic Average Calculator",
    "url": "math-tools/academic-average-calculator.html",
    "category": "Math & Numbers (Education Tools)",
    "desc": "Calculate average scores across multiple class semesters."
  },
  {
    "name": "Random Number Generator",
    "url": "math-tools/random-number-generator-math.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Generate custom random integers within select boundaries."
  },
  {
    "name": "Random Decimal Generator",
    "url": "math-tools/random-decimal-generator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Generate random floats/decimal numbers within a range."
  },
  {
    "name": "Random Integer Generator",
    "url": "math-tools/random-integer-generator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Generate multiple random whole integers in one execution."
  },
  {
    "name": "Lottery Number Generator",
    "url": "math-tools/lottery-number-generator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Generate custom random lottery numbers with no duplicates."
  },
  {
    "name": "Dice Roller",
    "url": "math-tools/dice-roller.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Roll virtual dice (standard D6, D20, or custom sides count) for games."
  },
  {
    "name": "Coin Flip Simulator",
    "url": "math-tools/coin-flip-simulator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Simulate random coin flips and track heads vs. tails statistics."
  },
  {
    "name": "Random Selection Generator",
    "url": "math-tools/random-selection-generator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Randomly pick item names from a custom comma-separated list."
  },
  {
    "name": "Random Sequence Generator",
    "url": "math-tools/random-sequence-generator-math.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Shuffle a sequence of numbers randomly."
  },
  {
    "name": "Random Combination Generator",
    "url": "math-tools/random-combination-generator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Generate random combinations (n choose k) from a list of values."
  },
  {
    "name": "Random Statistics Generator",
    "url": "math-tools/random-statistics-generator.html",
    "category": "Math & Numbers (Random Number Tools)",
    "desc": "Generate random normal-distributed data sets."
  },
  {
    "name": "Multiplication Table Generator",
    "url": "math-tools/multiplication-table-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate custom multiplication matrices tables for kids and worksheets."
  },
  {
    "name": "Worksheet Generator",
    "url": "math-tools/worksheet-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Create standard practice worksheet tests for mathematics arithmetic."
  },
  {
    "name": "Math Quiz Generator",
    "url": "math-tools/math-quiz-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate custom mathematics quizzes with accompanying answer sheets."
  },
  {
    "name": "Arithmetic Problem Generator",
    "url": "math-tools/arithmetic-problem-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate random practice arithmetic problems for tests."
  },
  {
    "name": "Algebra Problem Generator",
    "url": "math-tools/algebra-problem-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate basic linear equation algebra problems."
  },
  {
    "name": "Geometry Problem Generator",
    "url": "math-tools/geometry-problem-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate area/perimeter geometry questions."
  },
  {
    "name": "Fraction Problem Generator",
    "url": "math-tools/fraction-problem-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate fraction addition and subtraction questions."
  },
  {
    "name": "Equation Generator",
    "url": "math-tools/equation-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate algebraic linear and quadratic equations for testing."
  },
  {
    "name": "Number Pattern Generator",
    "url": "math-tools/number-pattern-generator-math.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate custom arithmetic or geometric number patterns."
  },
  {
    "name": "Practice Test Generator",
    "url": "math-tools/practice-test-generator.html",
    "category": "Math & Numbers (Math Generators)",
    "desc": "Generate a comprehensive practice math test."
  }
];

document.addEventListener("DOMContentLoaded", () => {
  // Sticky Header Scroll Effect
  const header = document.querySelector(".site-header");
  if (header) {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }
    };
    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Run once in case page loads scrolled
  }

  // Mobile Menu Burger Toggle
  const burgerMenu = document.querySelector(".burger-menu");
  const navMenu = document.querySelector(".nav-menu");
  if (burgerMenu && navMenu) {
    burgerMenu.addEventListener("click", () => {
      burgerMenu.classList.toggle("active");
      navMenu.classList.toggle("active");
    });
  }

  // Mobile Menu Categories Toggle (Accordion feel in mobile list)
  const categoriesNav = document.querySelector(".categories-nav");
  if (categoriesNav) {
    categoriesNav.addEventListener("click", (e) => {
      if (window.innerWidth <= 768) {
        // Only trigger if clicking the nav link itself, not the items in the dropdown
        if (e.target.classList.contains("nav-link")) {
          e.preventDefault();
          categoriesNav.classList.toggle("active");
        }
      }
    });
  }

  // Search Functionality
  const searchInput = document.querySelector(".search-input");
  const searchOverlay = document.querySelector(".search-results-overlay");
  
  if (searchInput && searchOverlay) {
    searchInput.addEventListener("input", (e) => {
      const query = e.target.value.toLowerCase().trim();
      
      if (query.length < 1) {
        searchOverlay.innerHTML = "";
        searchOverlay.classList.remove("active");
        return;
      }

      const results = ENGINYWHEELS_TOOLS.filter(tool => 
        tool.name.toLowerCase().includes(query) || 
        tool.category.toLowerCase().includes(query) ||
        tool.desc.toLowerCase().includes(query)
      );

      if (results.length === 0) {
        searchOverlay.innerHTML = `
          <div style="padding: 16px 20px; color: var(--text-muted); font-size: 0.9rem;">
            No tools found matching "${e.target.value}"
          </div>
        `;
      } else {
        const prefix = (window.location.pathname.includes('/tools/') || window.location.pathname.includes('/category/') || window.location.pathname.includes('/calculators/') || window.location.pathname.includes('/text-tools/') || window.location.pathname.includes('/security-tools/') || window.location.pathname.includes('/image-tools/') || window.location.pathname.includes('/time-tools/') || window.location.pathname.includes('/developer-tools/') || window.location.pathname.includes('/generator-tools/') || window.location.pathname.includes('/seo-web-tools/') || window.location.pathname.includes('/math-tools/')) ? '../' : '';
        searchOverlay.innerHTML = results.map(tool => `
          <div class="search-result-item">
            <a href="${prefix}${tool.url}">
              <span class="search-result-title">${tool.name}</span>
              <span class="search-result-cat">${tool.category}</span>
            </a>
          </div>
        `).join("");
      }
      
      searchOverlay.classList.add("active");
    });

    // Close search overlay on click outside
    document.addEventListener("click", (e) => {
      if (!searchInput.contains(e.target) && !searchOverlay.contains(e.target)) {
        searchOverlay.classList.remove("active");
      }
    });
  }

  // Dynamic Year in footer copyright
  const footerYear = document.getElementById("footer-year");
  if (footerYear) {
    footerYear.textContent = new Date().getFullYear();
  }
});

// Clipboard Copy Helper function with Toast notification
function copyToClipboard(text, successMsg = "Copied to clipboard!") {
  if (!navigator.clipboard) {
    // Fallback for older browsers
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed"; // Avoid scrolling to bottom
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand("copy");
      showToast(successMsg);
    } catch (err) {
      showToast("Could not copy text.", "error");
    }
    document.body.removeChild(textArea);
    return;
  }
  
  navigator.clipboard.writeText(text)
    .then(() => {
      showToast(successMsg);
    })
    .catch(() => {
      showToast("Could not copy text.", "error");
    });
}

// Global Toast System
function showToast(message, type = "success") {
  // Check if a toast container already exists, or create one
  let toast = document.querySelector(".toast-notification");
  if (!toast) {
    toast = document.createElement("div");
    toast.className = "toast-notification";
    document.body.appendChild(toast);
  }

  // Configure style and message
  toast.className = "toast-notification";
  if (type === "error") {
    toast.classList.add("toast-error");
    toast.innerHTML = `
      <svg style="width:20px;height:20px" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
      </svg>
      <span>${message}</span>
    `;
  } else {
    toast.innerHTML = `
      <svg style="width:20px;height:20px" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
      </svg>
      <span>${message}</span>
    `;
  }

  // Animate active
  setTimeout(() => {
    toast.classList.add("active");
  }, 10);

  // Auto hide after 3 seconds
  if (window.toastTimeout) {
    clearTimeout(window.toastTimeout);
  }
  window.toastTimeout = setTimeout(() => {
    toast.classList.remove("active");
  }, 3000);
}
