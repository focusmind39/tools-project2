with open("full_calculator_list.txt", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "Create a dedicated tool page for each calculator below:"
end_marker = "CATEGORY PAGE OPTIMIZATION"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    subtext = text[start_idx + len(start_marker):end_idx]
    print(subtext)
    with open("clean_list.txt", "w", encoding="utf-8") as out:
        out.write(subtext)
else:
    print("Markers not found!")
    print("start_idx:", start_idx, "end_idx:", end_idx)
