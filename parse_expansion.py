import json

with open("full_calculator_list.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Find the section between CALCULATOR CATEGORY EXPANSION and CATEGORY PAGE OPTIMIZATION
start_marker = "CALCULATOR CATEGORY EXPANSION"
end_marker = "CATEGORY PAGE OPTIMIZATION"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

section_text = text[start_idx + len(start_marker):end_idx]

# Parse categories and items
categories = {}
current_cat = None

for line in section_text.split("\n"):
    line = line.strip()
    if not line:
        continue
    if line.startswith("===") or line.startswith("Create a dedicated tool page"):
        continue
    if line.startswith("- "):
        item = line[2:].strip()
        if current_cat and item:
            categories[current_cat].append(item)
    elif "CALCULATORS" in line:
        current_cat = line.title()
        categories[current_cat] = []

# Output the categories and items in a clean format
print(f"Parsed {len(categories)} categories:")
total_items = 0
for cat, items in categories.items():
    print(f"{cat} ({len(items)} items):")
    for item in items:
         print(f"  - {item}")
    total_items += len(items)

print(f"\nTotal calculators: {total_items}")

with open("calculators_list.json", "w", encoding="utf-8") as out:
    json.dump(categories, out, indent=4)
