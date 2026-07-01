import json
import os

transcript_path = r"C:\Users\Manorama Salunkhe\.gemini\antigravity\brain\bf99aba9-7141-4828-8702-e3a84bb5ab0a\.system_generated\logs\transcript.jsonl"

if not os.path.exists(transcript_path):
    print("Transcript not found at", transcript_path)
    exit(1)

with open(transcript_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        try:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                content = data.get("content", "")
                if "CALCULATOR" in content or "Calculators" in content or "sip-calculator" in content:
                    print(f"--- Line {line_num} ---")
                    print(content[:2000])  # print first 2000 chars of matching user input
                    print("\n" + "="*50 + "\n")
        except Exception as e:
            print(f"Error parsing line {line_num}: {e}")
