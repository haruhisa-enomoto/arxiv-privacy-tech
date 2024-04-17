from pathlib import Path
import json

# JSONファイルのパス
file_path = Path("_data/papers.json")

# JSONファイルを読み込む
with file_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

# 各エントリーに日本語タイトルを追加
for entry in data:
    japanese_title = entry["summary"].split("\n")[0].strip("*")
    entry["japanese_title"] = japanese_title

# ファイルに変更を書き戻す
with Path("_data/new.json").open("w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# 処理が完了したことを表示
print("Japanese titles added to all entries.")
