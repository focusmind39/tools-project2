# -*- coding: utf-8 -*-
"""
Travel and Math & Engineering Calculators Data
"""

TRAVEL_CALCS = [
    {
        "name": "Fuel Cost Calculator",
        "slug": "fuel-cost-calculator",
        "category": "Travel",
        "icon": "⛽",
        "desc": "Calculate total fuel volume and cost for road trips based on distance and fuel efficiency.",
        "formula": "Fuel Cost = (Distance / 100) * Consumption * Fuel Price",
        "formula_desc": "Multiplies trip distance by vehicle fuel consumption rate and price per liter.",
        "inputs": [
            {"id": "fc-dist", "label": "Trip Distance (km)", "type": "number", "default": "300", "min": "1", "max": "50000", "step": "10"},
            {"id": "fc-cons", "label": "Fuel Consumption (L/100km)", "type": "number", "default": "8.0", "min": "1", "max": "40", "step": "0.1"},
            {"id": "fc-price", "label": "Fuel Price ($/Liter)", "type": "number", "default": "1.45", "min": "0.1", "max": "10", "step": "0.01"}
        ],
        "outputs": [
            {"id": "out-fc-liters", "label": "Fuel Needed", "prefix": "", "suffix": " Liters"},
            {"id": "out-fc-cost", "label": "Total Fuel Cost", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('fc-dist').value);
            const cons = parseFloat(document.getElementById('fc-cons').value);
            const price = parseFloat(document.getElementById('fc-price').value);

            if (isNaN(dist) || isNaN(cons) || isNaN(price) || dist <= 0 || cons <= 0 || price <= 0) {
                showToast("Please check travel inputs.", "error");
                return;
            }

            const liters = (dist / 100) * cons;
            const cost = liters * price;

            document.getElementById('out-fc-liters').textContent = liters.toFixed(1);
            document.getElementById('out-fc-cost').textContent = cost.toFixed(2);

            updateBreakdown(`
                <p>Fuel consumption target: <strong>${liters.toFixed(1)} Liters</strong> for the trip.</p>
            `);
        """
    },
    {
        "name": "Mileage Calculator",
        "slug": "mileage-calculator",
        "category": "Travel",
        "icon": "🚗",
        "desc": "Calculate vehicle fuel efficiency (mileage) based on distance covered and fuel filled.",
        "formula": "Mileage = Distance / Fuel Consumption (km/L)",
        "formula_desc": "Divides total odometer distance differences by the fuel volume added.",
        "inputs": [
            {"id": "mil-start", "label": "Starting Odometer (km)", "type": "number", "default": "12000", "min": "0", "max": "1000000", "step": "1"},
            {"id": "mil-end", "label": "Ending Odometer (km)", "type": "number", "default": "12450", "min": "0", "max": "1000000", "step": "1"},
            {"id": "mil-fuel", "label": "Fuel Filled (Liters)", "type": "number", "default": "36.0", "min": "1", "max": "500", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-mil-kml", "label": "Mileage (km/Liter)", "prefix": "", "suffix": " km/L"},
            {"id": "out-mil-l100", "label": "Consumption (L/100km)", "prefix": "", "suffix": " L/100km"}
        ],
        "calc_js": """
            const start = parseFloat(document.getElementById('mil-start').value);
            const end = parseFloat(document.getElementById('mil-end').value);
            const fuel = parseFloat(document.getElementById('mil-fuel').value);

            if (isNaN(start) || isNaN(end) || isNaN(fuel) || start < 0 || end <= start || fuel <= 0) {
                showToast("Odometer end must be greater than start.", "error");
                return;
            }

            const dist = end - start;
            const kml = dist / fuel;
            const l100 = (fuel / dist) * 100;

            document.getElementById('out-mil-kml').textContent = kml.toFixed(2);
            document.getElementById('out-mil-l100').textContent = l100.toFixed(2);

            updateBreakdown(`
                <p>Total distance traveled: <strong>${dist} km</strong>.</p>
            `);
        """
    },
    {
        "name": "Trip Cost Calculator",
        "slug": "trip-cost-calculator",
        "category": "Travel",
        "icon": "🗺️",
        "desc": "Calculate total road trip costs, including fuel, road tolls, and food/lodging expenses.",
        "formula": "Trip Cost = Fuel Cost + Tolls + Lodging + Food & Other",
        "formula_desc": "Aggregates travel expenses, factoring in distance fuel math and static travel costs.",
        "inputs": [
            {"id": "tc-dist", "label": "Distance (km)", "type": "number", "default": "500", "min": "1", "max": "20000", "step": "10"},
            {"id": "tc-kml", "label": "Fuel Efficiency (km/L)", "type": "number", "default": "12.0", "min": "2", "max": "50", "step": "0.1"},
            {"id": "tc-price", "label": "Fuel Price ($/L)", "type": "number", "default": "1.45", "min": "0.1", "max": "10", "step": "0.01"},
            {"id": "tc-tolls", "label": "Road Tolls ($)", "type": "number", "default": "15", "min": "0", "max": "5000", "step": "5"},
            {"id": "tc-other", "label": "Other Expenses (Hotel, Food) ($)", "type": "number", "default": "150", "min": "0", "max": "100000", "step": "10"}
        ],
        "outputs": [
            {"id": "out-tc-fuel", "label": "Fuel Expenses Portion", "prefix": "$", "suffix": ""},
            {"id": "out-tc-total", "label": "Total Trip Budget", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('tc-dist').value);
            const kml = parseFloat(document.getElementById('tc-kml').value);
            const price = parseFloat(document.getElementById('tc-price').value);
            const tolls = parseFloat(document.getElementById('tc-tolls').value) || 0;
            const other = parseFloat(document.getElementById('tc-other').value) || 0;

            if (isNaN(dist) || isNaN(kml) || isNaN(price) || dist <= 0 || kml <= 0 || price <= 0) {
                showToast("Please check numeric fields.", "error");
                return;
            }

            const fuelExpenses = (dist / kml) * price;
            const total = fuelExpenses + tolls + other;

            document.getElementById('out-tc-fuel').textContent = fuelExpenses.toFixed(2);
            document.getElementById('out-tc-total').textContent = total.toFixed(2);

            updateBreakdown(`
                <p>Fuel cost portion: $${fuelExpenses.toFixed(2)}</p>
                <p>Tolls & others: $${(tolls+other).toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Flight Time Calculator",
        "slug": "flight-time-calculator",
        "category": "Travel",
        "icon": "✈️",
        "desc": "Estimate direct flight time durations between cities based on distance and speed.",
        "formula": "Time = Distance / Speed",
        "formula_desc": "Divides air distance by typical aircraft cruising speeds, adding 30 minutes for takeoff and landing.",
        "inputs": [
            {"id": "flt-dist", "label": "Flight Distance (km)", "type": "number", "default": "3500", "min": "100", "max": "20000", "step": "100"},
            {"id": "flt-speed", "label": "Cruising Speed (km/h)", "type": "number", "default": "800", "min": "200", "max": "1500", "step": "50"}
        ],
        "outputs": [
            {"id": "out-flt-hours", "label": "Estimated Duration", "prefix": "", "suffix": " hours"},
            {"id": "out-flt-text", "label": "Readable Duration", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('flt-dist').value);
            const speed = parseFloat(document.getElementById('flt-speed').value);

            if (isNaN(dist) || isNaN(speed) || dist <= 0 || speed <= 0) {
                showToast("Please check flight inputs.", "error");
                return;
            }

            // Cruise time + 30 mins (0.5 hrs) for maneuvers, taxiing, takeoff and landing
            const rawTime = (dist / speed) + 0.5;
            const hrs = Math.floor(rawTime);
            const mins = Math.round((rawTime - hrs) * 60);

            document.getElementById('out-flt-hours').textContent = rawTime.toFixed(2);
            document.getElementById('out-flt-text').textContent = hrs + "h " + mins + "m (incl. takeoff/landing)";

            updateBreakdown(`
                <p>Pure flight cruise time: ${(dist/speed).toFixed(2)} hours.</p>
            `);
        """
    },
    {
        "name": "Travel Budget Calculator",
        "slug": "travel-budget-calculator",
        "category": "Travel",
        "icon": "💵",
        "desc": "Calculate your total travel budget, accounting for flights, hotels, food, and daily allowances.",
        "formula": "Total Budget = Flights + (Hotel + Food + Activities) * Days",
        "formula_desc": "Combines fixed transit costs with daily living allowances over the vacation period.",
        "inputs": [
            {"id": "tb-days", "label": "Trip Duration (Days)", "type": "number", "default": "7", "min": "1", "max": "365", "step": "1"},
            {"id": "tb-flights", "label": "Flights & Transport ($)", "type": "number", "default": "600", "min": "0", "max": "50000", "step": "50"},
            {"id": "tb-hotel", "label": "Hotel Per Night ($)", "type": "number", "default": "120", "min": "0", "max": "10000", "step": "10"},
            {"id": "tb-food", "label": "Food & Daily Allowance ($/day)", "type": "number", "default": "60", "min": "0", "max": "5000", "step": "5"},
            {"id": "tb-activities", "label": "Total Activities/Excursions ($)", "type": "number", "default": "250", "min": "0", "max": "20000", "step": "25"}
        ],
        "outputs": [
            {"id": "out-tb-total", "label": "Total Estimated Budget", "prefix": "$", "suffix": ""},
            {"id": "out-tb-daily", "label": "Average Cost Per Day", "prefix": "$", "suffix": " /day"}
        ],
        "calc_js": """
            const days = parseFloat(document.getElementById('tb-days').value);
            const flights = parseFloat(document.getElementById('tb-flights').value) || 0;
            const hotel = parseFloat(document.getElementById('tb-hotel').value) || 0;
            const food = parseFloat(document.getElementById('tb-food').value) || 0;
            const activities = parseFloat(document.getElementById('tb-activities').value) || 0;

            if (isNaN(days) || days <= 0) {
                showToast("Please check duration days.", "error");
                return;
            }

            const total = flights + (hotel * days) + (food * days) + activities;
            const daily = total / days;

            document.getElementById('out-tb-total').textContent = total.toFixed(2);
            document.getElementById('out-tb-daily').textContent = daily.toFixed(2);

            updateBreakdown(`
                <p>Transit & Fixed: $${(flights+activities).toFixed(2)}</p>
                <p>Daily Accommodations & Meals: $${((hotel+food)*days).toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Currency Exchange Calculator",
        "slug": "currency-exchange-calculator",
        "category": "Travel",
        "icon": "💱",
        "desc": "Convert monetary sums instantly using a fixed exchange rate.",
        "formula": "Converted Amount = Source Amount * Exchange Rate",
        "formula_desc": "Multiplies input capital values by custom currency market conversion rates.",
        "inputs": [
            {"id": "cur-amt", "label": "Source Amount", "type": "number", "default": "100", "min": "0.01", "max": "100000000", "step": "1"},
            {"id": "cur-rate", "label": "Exchange Rate (1 Source = X Target)", "type": "number", "default": "1.12", "min": "0.00001", "max": "100000", "step": "0.01"}
        ],
        "outputs": [
            {"id": "out-cur-val", "label": "Converted Target Amount", "prefix": "", "suffix": ""},
            {"id": "out-cur-rev", "label": "Reverse Value (1 Target)", "prefix": "", "suffix": " Source"}
        ],
        "calc_js": """
            const amt = parseFloat(document.getElementById('cur-amt').value);
            const rate = parseFloat(document.getElementById('cur-rate').value);

            if (isNaN(amt) || isNaN(rate) || amt <= 0 || rate <= 0) {
                showToast("Please check currency inputs.", "error");
                return;
            }

            const converted = amt * rate;
            const reverse = 1 / rate;

            document.getElementById('out-cur-val').textContent = converted.toFixed(2);
            document.getElementById('out-cur-rev').textContent = reverse.toFixed(5);

            updateBreakdown(`
                <p>Exchanged sum: <strong>${converted.toFixed(2)}</strong> target currency.</p>
            `);
        """
    },
    {
        "name": "Hotel Cost Calculator",
        "slug": "hotel-cost-calculator",
        "category": "Travel",
        "icon": "🏨",
        "desc": "Calculate total lodging invoices, including daily taxes and service fee additions.",
        "formula": "Total = Nightly Rate * Nights * (1 + Tax Rate / 100) + Extra Fees",
        "formula_desc": "Multiplies nightly rates by staying cycles, applying tax percentages and service additions.",
        "inputs": [
            {"id": "htl-rate", "label": "Nightly Room Rate ($)", "type": "number", "default": "120.00", "min": "1", "max": "50000", "step": "5"},
            {"id": "htl-nights", "label": "Number of Nights", "type": "number", "default": "3", "min": "1", "max": "120", "step": "1"},
            {"id": "htl-tax", "label": "Lodging Tax (%)", "type": "number", "default": "12.5", "min": "0", "max": "45", "step": "0.1"},
            {"id": "htl-fees", "label": "Service / Resort Fees ($)", "type": "number", "default": "30.00", "min": "0", "max": "5000", "step": "5"}
        ],
        "outputs": [
            {"id": "out-htl-room", "label": "Room Subtotal", "prefix": "$", "suffix": ""},
            {"id": "out-htl-tax", "label": "Total Taxes", "prefix": "$", "suffix": ""},
            {"id": "out-htl-grand", "label": "Invoice Total", "prefix": "$", "suffix": ""}
        ],
        "calc_js": """
            const rate = parseFloat(document.getElementById('htl-rate').value);
            const nights = parseFloat(document.getElementById('htl-nights').value);
            const tax = parseFloat(document.getElementById('htl-tax').value) || 0;
            const fees = parseFloat(document.getElementById('htl-fees').value) || 0;

            if (isNaN(rate) || isNaN(nights) || rate <= 0 || nights <= 0) {
                showToast("Please enter positive rate and nights.", "error");
                return;
            }

            const sub = rate * nights;
            const taxVal = sub * (tax / 100);
            const total = sub + taxVal + fees;

            document.getElementById('out-htl-room').textContent = sub.toFixed(2);
            document.getElementById('out-htl-tax').textContent = taxVal.toFixed(2);
            document.getElementById('out-htl-grand').textContent = total.toFixed(2);

            updateBreakdown(`
                <p>Gross lodging: $${sub.toFixed(2)} | Fees: $${fees.toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Road Trip Planner Calculator",
        "slug": "road-trip-planner-calculator",
        "category": "Travel",
        "icon": "🚗",
        "desc": "Calculate total drive time and travel days required based on distance and daily driving limits.",
        "formula": "Total Drive Hours = Distance / Speed | Travel Days = Drive Hours / Daily Driving Limit",
        "formula_desc": "Solves for total travel days required using road distance, speed averages, and daily resting schedules.",
        "inputs": [
            {"id": "rtp-dist", "label": "Total Route Distance (km)", "type": "number", "default": "1200", "min": "10", "max": "50000", "step": "50"},
            {"id": "rtp-speed", "label": "Average Driving Speed (km/h)", "type": "number", "default": "90", "min": "20", "max": "180", "step": "5"},
            {"id": "rtp-limit", "label": "Daily Driving Limit (Hours)", "type": "number", "default": "6", "min": "1", "max": "16", "step": "1"}
        ],
        "outputs": [
            {"id": "out-rtp-hours", "label": "Total Driving Time", "prefix": "", "suffix": " hours"},
            {"id": "out-rtp-days", "label": "Minimum Days Needed", "prefix": "", "suffix": " days"}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('rtp-dist').value);
            const speed = parseFloat(document.getElementById('rtp-speed').value);
            const limit = parseFloat(document.getElementById('rtp-limit').value);

            if (isNaN(dist) || isNaN(speed) || isNaN(limit) || dist <= 0 || speed <= 0 || limit <= 0) {
                showToast("Please check road trip planner inputs.", "error");
                return;
            }

            const driveHours = dist / speed;
            const days = driveHours / limit;

            document.getElementById('out-rtp-hours').textContent = driveHours.toFixed(1);
            document.getElementById('out-rtp-days').textContent = Math.ceil(days);

            updateBreakdown(`
                <p>Pure wheel time: <strong>${driveHours.toFixed(1)} hours</strong>.</p>
            `);
        """
    },
    {
        "name": "Taxi Fare Calculator",
        "slug": "taxi-fare-calculator",
        "category": "Travel",
        "icon": "🚕",
        "desc": "Estimate total metered taxi fares using local transit distance rates and base fees.",
        "formula": "Fare = Base Flag Drop + (Distance * Rate per km) + Idle Time cost",
        "formula_desc": "Combines base hook charges with progressive distance mileage rates.",
        "inputs": [
            {"id": "tx-dist", "label": "Trip Distance (km)", "type": "number", "default": "12", "min": "0.1", "max": "1000", "step": "0.5"},
            {"id": "tx-base", "label": "Base Fare / Flag Drop ($)", "type": "number", "default": "3.50", "min": "0", "max": "50", "step": "0.5"},
            {"id": "tx-rate", "label": "Rate Per Kilometer ($/km)", "type": "number", "default": "1.80", "min": "0.1", "max": "20", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-tx-fare", "label": "Estimated Metered Fare", "prefix": "$", "suffix": ""},
            {"id": "out-tx-costkm", "label": "Effective Cost per km", "prefix": "$", "suffix": " /km"}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('tx-dist').value);
            const base = parseFloat(document.getElementById('tx-base').value) || 0;
            const rate = parseFloat(document.getElementById('tx-rate').value);

            if (isNaN(dist) || isNaN(rate) || dist <= 0 || rate <= 0) {
                showToast("Please check taxi fare inputs.", "error");
                return;
            }

            const fare = base + (dist * rate);
            const costPerKm = fare / dist;

            document.getElementById('out-tx-fare').textContent = fare.toFixed(2);
            document.getElementById('out-tx-costkm').textContent = costPerKm.toFixed(2);

            updateBreakdown(`
                <p>Base hook drop: $${base.toFixed(2)} | Distance charge: $${(dist*rate).toFixed(2)}</p>
            `);
        """
    },
    {
        "name": "Speed Calculator",
        "slug": "speed-calculator",
        "category": "Travel",
        "icon": "⚡",
        "desc": "Calculate average speeds based on elapsed time and traveled route distance.",
        "formula": "Speed = Distance / Time",
        "formula_desc": "Divides traveled distance by time hours to solve for velocity.",
        "inputs": [
            {"id": "spd-dist", "label": "Travel Distance (km)", "type": "number", "default": "100", "min": "0.1", "max": "100000", "step": "1"},
            {"id": "spd-hours", "label": "Time (Hours)", "type": "number", "default": "1.5", "min": "0.01", "max": "1000", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-spd-kmh", "label": "Speed (km/h)", "prefix": "", "suffix": " km/h"},
            {"id": "out-spd-mph", "label": "Speed (mph)", "prefix": "", "suffix": " mph"}
        ],
        "calc_js": """
            const dist = parseFloat(document.getElementById('spd-dist').value);
            const time = parseFloat(document.getElementById('spd-hours').value);

            if (isNaN(dist) || isNaN(time) || dist <= 0 || time <= 0) {
                showToast("Please check speed inputs.", "error");
                return;
            }

            const kmh = dist / time;
            const mph = kmh * 0.621371;

            document.getElementById('out-spd-kmh').textContent = kmh.toFixed(2);
            document.getElementById('out-spd-mph').textContent = mph.toFixed(2);

            updateBreakdown(`
                <p>Velocity resolved over ${time} hours: <strong>${kmh.toFixed(2)} km/h</strong>.</p>
            `);
        """
    }
]

MATH_CALCS = [
    {
        "name": "Area Calculator",
        "slug": "area-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate surface areas for rectangles, circles, triangles, and parallelograms.",
        "formula": "Area = Formula varies by shape selection",
        "formula_desc": "Applies geometric area formulas based on your chosen shape index.",
        "inputs": [
            {"id": "ar-shape", "label": "Select Shape", "type": "select", "options": [
                ("rectangle", "Rectangle (Length * Width)"),
                ("circle", "Circle (π * r²)"),
                ("triangle", "Triangle (0.5 * Base * Height)")
            ]},
            {"id": "ar-p1", "label": "Length / Base / Radius", "type": "number", "default": "10", "min": "0.1", "max": "100000", "step": "0.5"},
            {"id": "ar-p2", "label": "Width / Height (Not needed for circle)", "type": "number", "default": "5", "min": "0.1", "max": "100000", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-ar-val", "label": "Calculated Surface Area", "prefix": "", "suffix": " sq units"}
        ],
        "calc_js": """
            const shape = document.getElementById('ar-shape').value;
            const p1 = parseFloat(document.getElementById('ar-p1').value);
            const p2 = parseFloat(document.getElementById('ar-p2').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter a valid primary input.", "error");
                return;
            }

            let area = 0;
            if (shape === "rectangle") {
                if (isNaN(p2) || p2 <= 0) { showToast("Width is required.", "error"); return; }
                area = p1 * p2;
            } else if (shape === "circle") {
                area = Math.PI * p1 * p1;
            } else {
                if (isNaN(p2) || p2 <= 0) { showToast("Height is required.", "error"); return; }
                area = 0.5 * p1 * p2;
            }

            document.getElementById('out-ar-val').textContent = area.toFixed(4);
            updateBreakdown(`<p>Geometric area solved for <strong>${shape}</strong>: ${area.toFixed(4)}</p>`);
        """
    },
    {
        "name": "Volume Calculator",
        "slug": "volume-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate volumetric contents for boxes, cylinders, cones, and spheres.",
        "formula": "Volume = Varies by shape selection",
        "formula_desc": "Evaluates solid mathematical volume integrals for standard geometries.",
        "inputs": [
            {"id": "vol-shape", "label": "Select Geometry", "type": "select", "options": [
                ("prism", "Rectangular Prism (L * W * H)"),
                ("cylinder", "Cylinder (π * r² * H)"),
                ("sphere", "Sphere (4/3 * π * r³)")
            ]},
            {"id": "vol-p1", "label": "Length / Radius", "type": "number", "default": "6", "min": "0.1", "max": "100000", "step": "0.5"},
            {"id": "vol-p2", "label": "Width (Prism only)", "type": "number", "default": "4", "min": "0.1", "max": "100000", "step": "0.5"},
            {"id": "vol-p3", "label": "Height / depth", "type": "number", "default": "8", "min": "0.1", "max": "100000", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-vol-val", "label": "Calculated Volume", "prefix": "", "suffix": " cubic units"}
        ],
        "calc_js": """
            const shape = document.getElementById('vol-shape').value;
            const p1 = parseFloat(document.getElementById('vol-p1').value);
            const p2 = parseFloat(document.getElementById('vol-p2').value);
            const p3 = parseFloat(document.getElementById('vol-p3').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter primary input.", "error");
                return;
            }

            let volume = 0;
            if (shape === "prism") {
                if (isNaN(p2) || isNaN(p3) || p2 <= 0 || p3 <= 0) { showToast("Width and Height are required.", "error"); return; }
                volume = p1 * p2 * p3;
            } else if (shape === "cylinder") {
                if (isNaN(p3) || p3 <= 0) { showToast("Height is required for cylinders.", "error"); return; }
                volume = Math.PI * p1 * p1 * p3;
            } else {
                volume = (4/3) * Math.PI * Math.pow(p1, 3);
            }

            document.getElementById('out-vol-val').textContent = volume.toFixed(4);
            updateBreakdown(`<p>Volume: ${volume.toFixed(4)}</p>`);
        """
    },
    {
        "name": "Surface Area Calculator",
        "slug": "surface-area-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate total external surface areas for prisms, cylinders, and spheres.",
        "formula": "Surface Area = Shape dependent equations",
        "formula_desc": "Evaluates total boundary surface areas for geometric solids.",
        "inputs": [
            {"id": "sa-shape", "label": "Select Geometry", "type": "select", "options": [
                ("prism", "Rectangular Prism (2LW + 2LH + 2WH)"),
                ("cylinder", "Cylinder (2πr² + 2πrH)"),
                ("sphere", "Sphere (4πr²)")
            ]},
            {"id": "sa-p1", "label": "Length / Radius", "type": "number", "default": "5", "min": "0.1", "max": "100000", "step": "0.5"},
            {"id": "sa-p2", "label": "Width (Prism only)", "type": "number", "default": "3", "min": "0.1", "max": "100000", "step": "0.5"},
            {"id": "sa-p3", "label": "Height", "type": "number", "default": "6", "min": "0.1", "max": "100000", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-sa-val", "label": "Surface Area", "prefix": "", "suffix": " sq units"}
        ],
        "calc_js": """
            const shape = document.getElementById('sa-shape').value;
            const p1 = parseFloat(document.getElementById('sa-p1').value);
            const p2 = parseFloat(document.getElementById('sa-p2').value);
            const p3 = parseFloat(document.getElementById('sa-p3').value);

            if (isNaN(p1) || p1 <= 0) {
                showToast("Please enter primary dimensions.", "error");
                return;
            }

            let sa = 0;
            if (shape === "prism") {
                if (isNaN(p2) || isNaN(p3) || p2 <= 0 || p3 <= 0) { showToast("Width and Height are required.", "error"); return; }
                sa = 2 * (p1 * p2 + p1 * p3 + p2 * p3);
            } else if (shape === "cylinder") {
                if (isNaN(p3) || p3 <= 0) { showToast("Height is required for cylinders.", "error"); return; }
                sa = (2 * Math.PI * p1 * p1) + (2 * Math.PI * p1 * p3);
            } else {
                sa = 4 * Math.PI * p1 * p1;
            }

            document.getElementById('out-sa-val').textContent = sa.toFixed(4);
        """
    },
    {
        "name": "Triangle Calculator",
        "slug": "triangle-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate triangle area and perimeter based on base and height dimensions.",
        "formula": "Area = 0.5 * Base * Height",
        "formula_desc": "Multiplies base dimension by height to evaluate flat triangle boundaries.",
        "inputs": [
            {"id": "tri-base", "label": "Base Length", "type": "number", "default": "8", "min": "0.1", "max": "100000", "step": "0.5"},
            {"id": "tri-height", "label": "Height", "type": "number", "default": "6", "min": "0.1", "max": "100000", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-tri-area", "label": "Triangle Area", "prefix": "", "suffix": " sq units"}
        ],
        "calc_js": """
            const base = parseFloat(document.getElementById('tri-base').value);
            const height = parseFloat(document.getElementById('tri-height').value);

            if (isNaN(base) || isNaN(height) || base <= 0 || height <= 0) {
                showToast("Please check triangle inputs.", "error");
                return;
            }

            const area = 0.5 * base * height;
            document.getElementById('out-tri-area').textContent = area.toFixed(4);
        """
    },
    {
        "name": "Circle Calculator",
        "slug": "circle-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate circular area, circumference, and diameter based on radius inputs.",
        "formula": "Area = π * r² | Circumference = 2 * π * r",
        "formula_desc": "Evaluates circular boundaries based on the transcendental index pi.",
        "inputs": [
            {"id": "circ-r", "label": "Radius (r)", "type": "number", "default": "5", "min": "0.01", "max": "100000", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-circ-area", "label": "Circle Area", "prefix": "", "suffix": " sq units"},
            {"id": "out-circ-circum", "label": "Circumference", "prefix": "", "suffix": " units"},
            {"id": "out-circ-diam", "label": "Diameter", "prefix": "", "suffix": " units"}
        ],
        "calc_js": """
            const r = parseFloat(document.getElementById('circ-r').value);

            if (isNaN(r) || r <= 0) {
                showToast("Please check radius values.", "error");
                return;
            }

            const area = Math.PI * r * r;
            const circum = 2 * Math.PI * r;
            const diam = 2 * r;

            document.getElementById('out-circ-area').textContent = area.toFixed(4);
            document.getElementById('out-circ-circum').textContent = circum.toFixed(4);
            document.getElementById('out-circ-diam').textContent = diam.toFixed(4);
        """
    },
    {
        "name": "Pythagorean Theorem Calculator",
        "slug": "pythagorean-theorem-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Solve right triangle side dimensions (a, b, c) using the Pythagorean theorem.",
        "formula": "a² + b² = c²",
        "formula_desc": "Resolves unknown legs or hypotenuse lengths of right-angled triangles.",
        "inputs": [
            {"id": "pyt-a", "label": "Side Leg a", "type": "number", "default": "3", "min": "0", "max": "100000", "step": "0.5"},
            {"id": "pyt-b", "label": "Side Leg b", "type": "number", "default": "4", "min": "0", "max": "100000", "step": "0.5"},
            {"id": "pyt-c", "label": "Hypotenuse c (Leave empty if solving for c)", "type": "number", "default": "", "min": "0", "max": "100000", "step": "0.5"}
        ],
        "outputs": [
            {"id": "out-pyt-solved", "label": "Solved Value", "prefix": "", "suffix": ""},
            {"id": "out-pyt-desc", "label": "Equation Output", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('pyt-a').value) || 0;
            const b = parseFloat(document.getElementById('pyt-b').value) || 0;
            const c = parseFloat(document.getElementById('pyt-c').value) || 0;

            if (a < 0 || b < 0 || c < 0) {
                showToast("Side values cannot be negative.", "error");
                return;
            }

            let solved = 0;
            let desc = "";

            if (c === 0) {
                if (a === 0 || b === 0) { showToast("Provide both legs a and b to solve for c.", "error"); return; }
                solved = Math.sqrt(a*a + b*b);
                desc = `c = √(${a}² + ${b}²) = √(${a*a + b*b})`;
            } else if (a === 0) {
                if (c <= b) { showToast("Hypotenuse c must exceed leg b.", "error"); return; }
                solved = Math.sqrt(c*c - b*b);
                desc = `a = √(${c}² - ${b}²) = √(${c*c - b*b})`;
            } else if (b === 0) {
                if (c <= a) { showToast("Hypotenuse c must exceed leg a.", "error"); return; }
                solved = Math.sqrt(c*c - a*a);
                desc = `b = √(${c}² - ${a}²) = √(${c*c - a*a})`;
            } else {
                showToast("Leave one side empty to solve for it.", "error");
                return;
            }

            document.getElementById('out-pyt-solved').textContent = solved.toFixed(4);
            document.getElementById('out-pyt-desc').textContent = desc;
        """
    },
    {
        "name": "Quadratic Equation Calculator",
        "slug": "quadratic-equation-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate real and complex roots for quadratic equations in ax² + bx + c = 0 format.",
        "formula": "x = [ -b ± √(b² - 4ac) ] / 2a",
        "formula_desc": "Solves quadratic polynomials by applying the standard algebraic discriminant formula.",
        "inputs": [
            {"id": "quad-a", "label": "Coefficient a", "type": "number", "default": "1", "min": "-1000", "max": "1000", "step": "0.1"},
            {"id": "quad-b", "label": "Coefficient b", "type": "number", "default": "-5", "min": "-1000", "max": "1000", "step": "0.1"},
            {"id": "quad-c", "label": "Coefficient c", "type": "number", "default": "6", "min": "-1000", "max": "1000", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-quad-r1", "label": "Root x1", "prefix": "", "suffix": ""},
            {"id": "out-quad-r2", "label": "Root x2", "prefix": "", "suffix": ""},
            {"id": "out-quad-disc", "label": "Discriminant (b² - 4ac)", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('quad-a').value);
            const b = parseFloat(document.getElementById('quad-b').value);
            const c = parseFloat(document.getElementById('quad-c').value);

            if (isNaN(a) || isNaN(b) || isNaN(c)) {
                showToast("Please enter coefficients.", "error");
                return;
            }
            if (a === 0) {
                showToast("Coefficient a cannot be zero (otherwise it is a linear equation).", "error");
                return;
            }

            const disc = b*b - 4*a*c;
            document.getElementById('out-quad-disc').textContent = disc.toFixed(2);

            if (disc > 0) {
                const r1 = (-b + Math.sqrt(disc)) / (2 * a);
                const r2 = (-b - Math.sqrt(disc)) / (2 * a);
                document.getElementById('out-quad-r1').textContent = r1.toFixed(4);
                document.getElementById('out-quad-r2').textContent = r2.toFixed(4);
            } else if (disc === 0) {
                const r = -b / (2 * a);
                document.getElementById('out-quad-r1').textContent = r.toFixed(4);
                document.getElementById('out-quad-r2').textContent = r.toFixed(4) + " (double root)";
            } else {
                // Complex roots
                const real = (-b / (2*a)).toFixed(4);
                const imag = (Math.sqrt(-disc) / (2*a)).toFixed(4);
                document.getElementById('out-quad-r1').textContent = real + " + " + imag + "i";
                document.getElementById('out-quad-r2').textContent = real + " - " + imag + "i";
            }
        """
    },
    {
        "name": "Matrix Calculator",
        "slug": "matrix-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Perform addition, subtraction, and multiplication operations on 2x2 matrices.",
        "formula": "Standard 2x2 Matrix arithmetic linear operations",
        "formula_desc": "Combines matching rows and columns to output resultant matrices.",
        "inputs": [
            {"id": "mat-a11", "label": "A [1,1]", "type": "number", "default": "2", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-a12", "label": "A [1,2]", "type": "number", "default": "1", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-a21", "label": "A [2,1]", "type": "number", "default": "0", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-a22", "label": "A [2,2]", "type": "number", "default": "4", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-b11", "label": "B [1,1]", "type": "number", "default": "1", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-b12", "label": "B [1,2]", "type": "number", "default": "3", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-b21", "label": "B [2,1]", "type": "number", "default": "2", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-b22", "label": "B [2,2]", "type": "number", "default": "1", "min": "-100", "max": "100", "step": "1"},
            {"id": "mat-op", "label": "Matrix Operation", "type": "select", "options": [("add", "Addition (A + B)"), ("sub", "Subtraction (A - B)")]}
        ],
        "outputs": [
            {"id": "out-mat-r11", "label": "Result [1,1]", "prefix": "", "suffix": ""},
            {"id": "out-mat-r12", "label": "Result [1,2]", "prefix": "", "suffix": ""},
            {"id": "out-mat-r21", "label": "Result [2,1]", "prefix": "", "suffix": ""},
            {"id": "out-mat-r22", "label": "Result [2,2]", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const a11 = parseFloat(document.getElementById('mat-a11').value);
            const a12 = parseFloat(document.getElementById('mat-a12').value);
            const a21 = parseFloat(document.getElementById('mat-a21').value);
            const a22 = parseFloat(document.getElementById('mat-a22').value);
            const b11 = parseFloat(document.getElementById('mat-b11').value);
            const b12 = parseFloat(document.getElementById('mat-b12').value);
            const b21 = parseFloat(document.getElementById('mat-b21').value);
            const b22 = parseFloat(document.getElementById('mat-b22').value);
            const op = document.getElementById('mat-op').value;

            if ([a11, a12, a21, a22, b11, b12, b21, b22].some(isNaN)) {
                showToast("Please enter values in all cells.", "error");
                return;
            }

            let r11, r12, r21, r22;
            if (op === "add") {
                r11 = a11 + b11; r12 = a12 + b12;
                r21 = a21 + b21; r22 = a22 + b22;
            } else {
                r11 = a11 - b11; r12 = a12 - b12;
                r21 = a21 - b21; r22 = a22 - b22;
            }

            document.getElementById('out-mat-r11').textContent = r11;
            document.getElementById('out-mat-r12').textContent = r12;
            document.getElementById('out-mat-r21').textContent = r21;
            document.getElementById('out-mat-r22').textContent = r22;
        """
    },
    {
        "name": "Determinant Calculator",
        "slug": "determinant-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate the determinant of a standard 2x2 matrix.",
        "formula": "det(A) = ad - bc",
        "formula_desc": "Multiplies main diagonal values and subtracts the product of the cross diagonal.",
        "inputs": [
            {"id": "det-a", "label": "Cell a (1,1)", "type": "number", "default": "4", "min": "-1000", "max": "1000", "step": "1"},
            {"id": "det-b", "label": "Cell b (1,2)", "type": "number", "default": "3", "min": "-1000", "max": "1000", "step": "1"},
            {"id": "det-c", "label": "Cell c (2,1)", "type": "number", "default": "2", "min": "-1000", "max": "1000", "step": "1"},
            {"id": "det-d", "label": "Cell d (2,2)", "type": "number", "default": "5", "min": "-1000", "max": "1000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-det-val", "label": "Determinant |A|", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const a = parseFloat(document.getElementById('det-a').value);
            const b = parseFloat(document.getElementById('det-b').value);
            const c = parseFloat(document.getElementById('det-c').value);
            const d = parseFloat(document.getElementById('det-d').value);

            if ([a,b,c,d].some(isNaN)) {
                showToast("Please enter numbers.", "error");
                return;
            }

            const det = a*d - b*c;
            document.getElementById('out-det-val').textContent = det;
            updateBreakdown(`<p>det = (${a} * ${d}) - (${b} * ${c}) = <strong>${det}</strong></p>`);
        """
    },
    {
        "name": "Log Calculator",
        "slug": "log-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Calculate logarithm values for a number to any custom base or common natural log base.",
        "formula": "log_b(x) = log(x) / log(b)",
        "formula_desc": "Uses mathematical change of base formulas to solve for logarithmic scales.",
        "inputs": [
            {"id": "log-x", "label": "Number (x)", "type": "number", "default": "100", "min": "0.0001", "max": "1000000000", "step": "0.1"},
            {"id": "log-b", "label": "Log Base (b) (Use 2.71828 for Natural ln)", "type": "number", "default": "10", "min": "0.0001", "max": "1000", "step": "0.1"}
        ],
        "outputs": [
            {"id": "out-log-val", "label": "Logarithm Value", "prefix": "", "suffix": ""},
            {"id": "out-log-ln", "label": "Natural Log (ln x)", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const x = parseFloat(document.getElementById('log-x').value);
            const b = parseFloat(document.getElementById('log-b').value);

            if (isNaN(x) || isNaN(b) || x <= 0 || b <= 0 || b === 1) {
                showToast("Ensure number and base are positive and base is not 1.", "error");
                return;
            }

            const logVal = Math.log(x) / Math.log(b);
            const lnVal = Math.log(x);

            document.getElementById('out-log-val').textContent = logVal.toFixed(6);
            document.getElementById('out-log-ln').textContent = lnVal.toFixed(6);
        """
    },
    {
        "name": "Percentage Increase Calculator",
        "slug": "percentage-increase-calculator",
        "category": "Math & Engineering",
        "icon": "📈",
        "desc": "Calculate the percentage increase between two numerical values.",
        "formula": "Increase (%) = ((New - Original) / Original) * 100",
        "formula_desc": "Solves relative percentage growth ratios from starting baseline numbers.",
        "inputs": [
            {"id": "pi-orig", "label": "Original Value", "type": "number", "default": "80", "min": "0.0001", "max": "1000000000", "step": "1"},
            {"id": "pi-new", "label": "New Value", "type": "number", "default": "100", "min": "0.0001", "max": "1000000000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-pi-pct", "label": "Percentage Increase", "prefix": "", "suffix": "%"},
            {"id": "out-pi-diff", "label": "Absolute Difference", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const orig = parseFloat(document.getElementById('pi-orig').value);
            const newVal = parseFloat(document.getElementById('pi-new').value);

            if (isNaN(orig) || isNaN(newVal) || orig <= 0) {
                showToast("Original value must be greater than zero.", "error");
                return;
            }

            const diff = newVal - orig;
            const pct = (diff / orig) * 100;

            document.getElementById('out-pi-pct').textContent = pct.toFixed(2);
            document.getElementById('out-pi-diff').textContent = diff.toFixed(2);
        """
    },
    {
        "name": "Percentage Decrease Calculator",
        "slug": "percentage-decrease-calculator",
        "category": "Math & Engineering",
        "icon": "📉",
        "desc": "Calculate the percentage decrease and raw drops between two numerical values.",
        "formula": "Decrease (%) = ((Original - New) / Original) * 100",
        "formula_desc": "Solves for relative percentage drops from starting baseline numbers.",
        "inputs": [
            {"id": "pd-orig", "label": "Original Value", "type": "number", "default": "150", "min": "0.0001", "max": "1000000000", "step": "1"},
            {"id": "pd-new", "label": "New Value", "type": "number", "default": "120", "min": "0", "max": "1000000000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-pd-pct", "label": "Percentage Decrease", "prefix": "", "suffix": "%"},
            {"id": "out-pd-diff", "label": "Absolute Drop", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const orig = parseFloat(document.getElementById('pd-orig').value);
            const newVal = parseFloat(document.getElementById('pd-new').value);

            if (isNaN(orig) || isNaN(newVal) || orig <= 0) {
                showToast("Original value must be greater than zero.", "error");
                return;
            }

            const diff = orig - newVal;
            const pct = (diff / orig) * 100;

            document.getElementById('out-pd-pct').textContent = pct.toFixed(2);
            document.getElementById('out-pd-diff').textContent = diff.toFixed(2);
        """
    },
    {
        "name": "Average Calculator",
        "slug": "average-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Calculate the arithmetic average (mean) for a set of comma-separated numbers.",
        "formula": "Mean = Sum(X) / N",
        "formula_desc": "Calculates the sum value of elements divided by the total sample count.",
        "inputs": [
            {"id": "avg-vals", "label": "Values (comma separated)", "type": "text", "default": "10, 15, 20, 25, 30"}
        ],
        "outputs": [
            {"id": "out-avg-mean", "label": "Arithmetic Mean", "prefix": "", "suffix": ""},
            {"id": "out-avg-sum", "label": "Sum Total", "prefix": "", "suffix": ""},
            {"id": "out-avg-count", "label": "Count (N)", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const raw = document.getElementById('avg-vals').value;
            const nums = raw.split(',').map(x => parseFloat(x.trim())).filter(x => !isNaN(x));

            if (nums.length === 0) {
                showToast("Please enter numbers separated by commas.", "error");
                return;
            }

            const sum = nums.reduce((a,b) => a+b, 0);
            const mean = sum / nums.length;

            document.getElementById('out-avg-mean').textContent = mean.toFixed(4);
            document.getElementById('out-avg-sum').textContent = sum;
            document.getElementById('out-avg-count').textContent = nums.length;
        """
    },
    {
        "name": "Median Calculator",
        "slug": "median-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Calculate the median (middle value) of a set of comma-separated numbers.",
        "formula": "Median = Middle Value of Sorted Array",
        "formula_desc": "Sorts lists in order and identifies the center value index.",
        "inputs": [
            {"id": "med-vals", "label": "Values (comma separated)", "type": "text", "default": "5, 2, 9, 1, 7, 6"}
        ],
        "outputs": [
            {"id": "out-med-val", "label": "Median Value", "prefix": "", "suffix": ""},
            {"id": "out-med-sorted", "label": "Sorted List", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const raw = document.getElementById('med-vals').value;
            const nums = raw.split(',').map(x => parseFloat(x.trim())).filter(x => !isNaN(x));

            if (nums.length === 0) {
                showToast("Please enter valid numbers.", "error");
                return;
            }

            nums.sort((a,b) => a - b);
            
            let median = 0;
            const mid = Math.floor(nums.length / 2);
            if (nums.length % 2 === 0) {
                median = (nums[mid - 1] + nums[mid]) / 2;
            } else {
                median = nums[mid];
            }

            document.getElementById('out-med-val').textContent = median;
            document.getElementById('out-med-sorted').textContent = nums.join(', ');
        """
    },
    {
        "name": "Mode Calculator",
        "slug": "mode-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Find the mode (most frequent number) for a set of comma-separated numbers.",
        "formula": "Mode = Most Frequent Element(s)",
        "formula_desc": "Audits list frequencies to return elements that occur most often.",
        "inputs": [
            {"id": "mod-vals", "label": "Values (comma separated)", "type": "text", "default": "1, 2, 2, 3, 4, 4, 4, 5"}
        ],
        "outputs": [
            {"id": "out-mod-val", "label": "Mode(s) Solved", "prefix": "", "suffix": ""},
            {"id": "out-mod-freq", "label": "Peak Frequency Count", "prefix": "", "suffix": " times"}
        ],
        "calc_js": """
            const raw = document.getElementById('mod-vals').value;
            const nums = raw.split(',').map(x => parseFloat(x.trim())).filter(x => !isNaN(x));

            if (nums.length === 0) {
                showToast("Please enter valid numbers.", "error");
                return;
            }

            const freq = {};
            let maxCount = 0;
            nums.forEach(n => {
                freq[n] = (freq[n] || 0) + 1;
                if (freq[n] > maxCount) maxCount = freq[n];
            });

            const modes = [];
            for (let k in freq) {
                if (freq[k] === maxCount) modes.push(k);
            }

            document.getElementById('out-mod-val').textContent = modes.join(', ');
            document.getElementById('out-mod-freq').textContent = maxCount;
        """
    },
    {
        "name": "Standard Deviation Calculator",
        "slug": "standard-deviation-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Calculate standard deviation and variance for datasets.",
        "formula": "σ = √[ Sum(x - μ)² / N ]",
        "formula_desc": "Solves sample standard deviation deviations relative to the mean.",
        "inputs": [
            {"id": "sd-vals", "label": "Values (comma separated)", "type": "text", "default": "10, 12, 23, 23, 16, 23, 21, 16"},
            {"id": "sd-type", "label": "Analysis Target", "type": "select", "options": [("sample", "Sample (N - 1)"), ("population", "Population (N)")]}
        ],
        "outputs": [
            {"id": "out-sd-val", "label": "Standard Deviation (SD)", "prefix": "", "suffix": ""},
            {"id": "out-sd-var", "label": "Variance", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const raw = document.getElementById('sd-vals').value;
            const type = document.getElementById('sd-type').value;
            const nums = raw.split(',').map(x => parseFloat(x.trim())).filter(x => !isNaN(x));

            if (nums.length < 2) {
                showToast("Please enter at least 2 numbers.", "error");
                return;
            }

            const mean = nums.reduce((a,b) => a+b, 0) / nums.length;
            const sqDiffs = nums.map(x => Math.pow(x - mean, 2));
            const sumSqDiffs = sqDiffs.reduce((a,b) => a+b, 0);
            
            const denom = (type === "sample") ? nums.length - 1 : nums.length;
            const variance = sumSqDiffs / denom;
            const sd = Math.sqrt(variance);

            document.getElementById('out-sd-val').textContent = sd.toFixed(4);
            document.getElementById('out-sd-var').textContent = variance.toFixed(4);
        """
    },
    {
        "name": "Probability Calculator",
        "slug": "probability-calculator",
        "category": "Math & Engineering",
        "icon": "🎲",
        "desc": "Calculate basic probabilities based on favorable outcomes and total events.",
        "formula": "Probability = Favorable Outcomes / Total Outcomes",
        "formula_desc": "Divides potential winning selections by total sample sizes.",
        "inputs": [
            {"id": "prb-fav", "label": "Favorable Outcomes (A)", "type": "number", "default": "1", "min": "0", "max": "10000000", "step": "1"},
            {"id": "prb-tot", "label": "Total Sample Space (S)", "type": "number", "default": "6", "min": "1", "max": "10000000", "step": "1"}
        ],
        "outputs": [
            {"id": "out-prb-pct", "label": "Probability Percentage", "prefix": "", "suffix": "%"},
            {"id": "out-prb-odds", "label": "Decimals Odds value", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const fav = parseFloat(document.getElementById('prb-fav').value);
            const tot = parseFloat(document.getElementById('prb-tot').value);

            if (isNaN(fav) || isNaN(tot) || fav < 0 || tot <= 0 || fav > tot) {
                showToast("Favorable events cannot exceed sample space.", "error");
                return;
            }

            const pct = (fav / tot) * 100;
            const odds = fav / tot;

            document.getElementById('out-prb-pct').textContent = pct.toFixed(2);
            document.getElementById('out-prb-odds').textContent = odds.toFixed(5);
        """
    },
    {
        "name": "Permutation Calculator",
        "slug": "permutation-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Calculate permutations nPr - where ordering matches matters.",
        "formula": "nPr = n! / (n - r)!",
        "formula_desc": "Solves total ordering sequences for selecting subset elements from a set.",
        "inputs": [
            {"id": "perm-n", "label": "Total Elements (n)", "type": "number", "default": "8", "min": "1", "max": "150", "step": "1"},
            {"id": "perm-r", "label": "Selected Elements (r)", "type": "number", "default": "3", "min": "1", "max": "150", "step": "1"}
        ],
        "outputs": [
            {"id": "out-perm-val", "label": "Permutations nPr", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const n = parseFloat(document.getElementById('perm-n').value);
            const r = parseFloat(document.getElementById('perm-r').value);

            if (isNaN(n) || isNaN(r) || n <= 0 || r <= 0 || r > n) {
                showToast("Ensure n >= r.", "error");
                return;
            }

            const fact = (num) => {
                let f = 1;
                for (let i = 2; i <= num; i++) f *= i;
                return f;
            };

            const nPr = fact(n) / fact(n - r);
            document.getElementById('out-perm-val').textContent = nPr.toLocaleString();
        """
    },
    {
        "name": "Combination Calculator",
        "slug": "combination-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Calculate combinations nCr - where ordering does not matter.",
        "formula": "nCr = n! / (r! * (n - r)!)",
        "formula_desc": "Solves combination configurations for picking sub-elements without sequence orders.",
        "inputs": [
            {"id": "comb-n", "label": "Total Elements (n)", "type": "number", "default": "10", "min": "1", "max": "150", "step": "1"},
            {"id": "comb-r", "label": "Selected Elements (r)", "type": "number", "default": "3", "min": "1", "max": "150", "step": "1"}
        ],
        "outputs": [
            {"id": "out-comb-val", "label": "Combinations nCr", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const n = parseFloat(document.getElementById('comb-n').value);
            const r = parseFloat(document.getElementById('comb-r').value);

            if (isNaN(n) || isNaN(r) || n <= 0 || r <= 0 || r > n) {
                showToast("Ensure n >= r.", "error");
                return;
            }

            const fact = (num) => {
                let f = 1;
                for (let i = 2; i <= num; i++) f *= i;
                return f;
            };

            const nCr = fact(n) / (fact(r) * fact(n - r));
            document.getElementById('out-comb-val').textContent = nCr.toLocaleString();
        """
    },
    {
        "name": "Factorial Calculator",
        "slug": "factorial-calculator",
        "category": "Math & Engineering",
        "icon": "🔢",
        "desc": "Calculate the factorial (n!) of positive integers.",
        "formula": "n! = n * (n - 1) * ... * 1",
        "formula_desc": "Multiplies all positive integers up to input numbers.",
        "inputs": [
            {"id": "fac-n", "label": "Integer (n)", "type": "number", "default": "5", "min": "0", "max": "170", "step": "1"}
        ],
        "outputs": [
            {"id": "out-fac-val", "label": "Factorial n!", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const n = parseFloat(document.getElementById('fac-n').value);

            if (isNaN(n) || n < 0) {
                showToast("Integer must be positive.", "error");
                return;
            }

            let f = 1;
            for (let i = 2; i <= n; i++) f *= i;

            document.getElementById('out-fac-val').textContent = (f === Infinity) ? "Infinity (Exceeds double limits)" : f.toLocaleString();
        """
    },
    {
        "name": "Scientific Notation Calculator",
        "slug": "scientific-notation-calculator",
        "category": "Math & Engineering",
        "icon": "📐",
        "desc": "Convert standard decimal numbers to scientific notation format.",
        "formula": "a * 10^b",
        "formula_desc": "Normalizes numerical decimals, isolating base values from exponential powers.",
        "inputs": [
            {"id": "sn-val", "label": "Decimal Number", "type": "number", "default": "45000", "min": "-1000000000000000", "max": "1000000000000000", "step": "0.0001"}
        ],
        "outputs": [
            {"id": "out-sn-notation", "label": "Scientific Notation", "prefix": "", "suffix": ""}
        ],
        "calc_js": """
            const val = parseFloat(document.getElementById('sn-val').value);

            if (isNaN(val)) {
                showToast("Please enter a valid number.", "error");
                return;
            }

            if (val === 0) {
                document.getElementById('out-sn-notation').textContent = "0.0 x 10^0";
                return;
            }

            const notation = val.toExponential(4);
            document.getElementById('out-sn-notation').textContent = notation.replace('e', ' x 10^');
        """
    }
]
