import json
from datetime import datetime, timedelta
from pathlib import Path

# JSONデータを読み込む
data_path = Path("_data/papers.json")
with data_path.open("r", encoding="utf-8") as file:
    papers = json.load(file)


topic_ja_to_en = {
    "連合学習": "fl",
    "連合転移学習": "ftl",
    "差分プライバシー": "dp",
    "合成データ": "sd",
    "準同型暗号": "he",
    "秘密計算": "mpc",
    "PETs": "pets",
    "SSI/DID/VC": "ssi",
    "全て": "all",
}
topic_en_to_ja = {v: k for k, v in topic_ja_to_en.items()}


# 週の初めを金曜日に設定して、投稿日を週ごとに分類
def get_week_start(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    start_of_week = date - timedelta(days=(date.weekday() + 3) % 7)
    return start_of_week


# 週ごとのデータをトピックごとに保持する辞書
weekly_papers = {topic_en: {} for topic_en in topic_en_to_ja.keys()}
weekly_papers["all"] = {}  # "all"カテゴリも含める

for paper in papers:
    week_start = get_week_start(paper["published"]).date()
    for topic_ja in paper["topics"]:
        folder = topic_ja_to_en.get(topic_ja)
        if folder:
            if week_start not in weekly_papers[folder]:
                weekly_papers[folder][week_start] = []
            weekly_papers[folder][week_start].append(paper)
    # 全てのトピックに対して同じことをする
    if week_start not in weekly_papers["all"]:
        weekly_papers["all"][week_start] = []
    weekly_papers["all"][week_start].append(paper)

# 週ごとにトピックごとのファイルを出力
for topic_en, data in weekly_papers.items():
    output_dir = Path(f"_{topic_en}/")
    output_dir.mkdir(parents=True, exist_ok=True)
    topic_ja = topic_en_to_ja[topic_en]
    print(f"Processing {topic_ja}...")

    for week_start, papers in data.items():
        week_end = week_start + timedelta(days=6)  # 週の終わりを計算
        file_name = week_start.strftime("%Y-%m-%d") + ".md"
        print(topic_ja)
        md_output = [
            "---",
            f"title: {topic_ja} ({week_start} ~ {week_end})",
            f"date: {week_start}",
            "---\n",
            (
                f"{topic_ja}に関する論文まとめ ({week_start} ~ {week_end})"
                if topic_ja != "all"
                else "論文まとめ"
            ),
            "",
        ]
        for paper in papers:
            md_output.append(f"### [{paper['title']}]({paper['url']})")
            md_output.append(f"**{paper['japanese_title']}**\n")
            md_output.append(f"{', '.join(paper['authors'])}\n")
            md_output.append(f"{paper['summary']}\n")
            if paper["comment"]:
                md_output.append(f"**Comment:** {paper['comment']}\n")
            topic_links = [
                f"[{topic}](../../{topic_ja_to_en[topic]})" for topic in paper["topics"]
            ]
            md_output.append(
                f"**トピック:** {', '.join(topic_links)}, **投稿日:** {paper['published']}\n"
            )
            md_output.append("---")

        output_file = output_dir / file_name
        with output_file.open("w", encoding="utf-8") as file:
            file.write("\n".join(md_output))
