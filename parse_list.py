with open("full_calculator_list.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Find all lines starting with "- " or category titles (all caps followed by "CALCULATORS")
lines = text.split("\n")
current_category = "General"
categories = {}

for line in lines:
    line = line.strip()
    if not line:
        continue
    # Check if category header
    if "CALCULATORS" in line and not line.startswith("-") and not line.startswith("="):
        current_category = line
        categories[current_category] = []
    elif line.startswith("- "):
        calc_name = line[2:].strip()
        # Some lines might be other descriptions, but under category headers, these are calculator names
        if current_category not in categories:
            categories[current_category] = []
        categories[current_category].append(calc_name)

# Print categories and count of items
total = 0
for cat, items in categories.items():
    print(f"{cat} ({len(items)}):")
    for item in items:
        print(f"  - {item}")
    total += len(items)

print(f"\nTotal calculators parsed: {total}")
