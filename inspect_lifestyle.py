import json

with open("calculators_list.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lifestyle_items = data.get("Lifestyle Calculators", [])
print("Lifestyle items:")
for idx, item in enumerate(lifestyle_items, 1):
    print(f"{idx}: {item}")
