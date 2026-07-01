import json
import os

transcript_path = r"C:\Users\Manorama Salunkhe\.gemini\antigravity\brain\bf99aba9-7141-4828-8702-e3a84bb5ab0a\.system_generated\logs\transcript_full.jsonl"

if not os.path.exists(transcript_path):
    print("Transcript not found at", transcript_path)
    exit(1)

with open(transcript_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if idx == 467:
            data = json.loads(line)
            content = data.get("content", "")
            print(f"Read line 467, length of content: {len(content)}")
            # Save it to a file in the workspace
            with open("full_calculator_list.txt", "w", encoding="utf-8") as out:
                out.write(content)
            print("Successfully wrote full list to full_calculator_list.txt")
            break
