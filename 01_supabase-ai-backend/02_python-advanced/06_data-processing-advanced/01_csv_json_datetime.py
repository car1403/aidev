"""CSV, JSON, datetime, pathlib 예제입니다."""

import csv
import json
from datetime import datetime
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

rows = [
    {"name": "Jean", "score": "95"},
    {"name": "Alex", "score": "88"},
]

csv_path = data_dir / "scores.csv"
with csv_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)

json_path = data_dir / "summary.json"
summary = {
    "created_at": datetime.now().isoformat(timespec="seconds"),
    "count": len(rows),
}
json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

print("CSV:", csv_path)
print("JSON:", json_path)
