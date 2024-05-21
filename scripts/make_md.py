from datetime import date, datetime, timedelta
from pathlib import Path

from run import PaperInfo, parse_json

# JSONデータを読み込む
json_path = Path("_data/papers.json")
papers = parse_json(json_path)

latest_json_path = Path("_data/latest_papers.json")
latest_papers = parse_json(latest_json_path)


def make_md_segment(paper: PaperInfo, on_home: bool = False) -> str:
    if on_home:
        topic_str = ", ".join(
            [f"[{topic}]({topic_ja_to_en[topic]})" for topic in paper.topics]
        )
    else:
        topic_str = ", ".join(
            [f"[{topic}](../../{topic_ja_to_en[topic]})" for topic in paper.topics]
        )
    return f"""
- - -

### [{paper.title}]({paper.url})

**{paper.japanese_title}**

{', '.join(paper.authors)}

{paper.summary}

{f"**Comment:** {paper.comment}" if paper.comment else ""}

**トピック:** {topic_str}, **カテゴリ:** {', '.join(paper.categories)}, **投稿日時:** {paper.published.strftime('%Y-%m-%d %H:%M')}
"""


topic_ja_to_en = {
    "連合学習": "fl",
    "連合転移学習": "ftl",
    "差分プライバシー": "dp",
    "合成データ": "sd",
    "準同型暗号": "he",
    "秘密計算": "mpc",
    "PETs": "pets",
    "SSI/DID/VC": "ssi",
    "ゼロ知識証明": "zkp",
    "TEE": "tee",
    "全て": "all",
}
topic_en_to_ja = {v: k for k, v in topic_ja_to_en.items()}


# 週の初めを金曜日に設定して、投稿日を週ごとに分類
def get_week_start(date: datetime) -> datetime:
    # date.weekday() が返すのは月曜日が 0、金曜日が 4
    adjustment = (date.weekday() - 4) % 7
    start_of_week = date - timedelta(days=adjustment)
    return start_of_week


# 週ごとのデータをトピックごとに保持する辞書
weekly_papers: dict[str, dict[date, list[PaperInfo]]] = {
    topic_en: {} for topic_en in topic_en_to_ja.keys()
}
weekly_papers["all"] = {}  # "all"カテゴリも含める

for paper in papers:
    week_start = get_week_start(paper.published).date()
    for topic_ja in paper.topics:
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

    for week_start, papers in data.items():
        week_end = week_start + timedelta(days=6)  # 週の終わりを計算
        file_name = week_start.strftime("%Y-%m-%d") + ".md"
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
            md_output.append(make_md_segment(paper))
        output_file = output_dir / file_name
        with output_file.open("w", encoding="utf-8") as file:
            file.write("\n".join(md_output))


if not latest_papers:
    print("No new papers to summarize.")
    exit()

index_md = f"""---
layout: single
classes: wide
title: トップページ
permalink: /
author_profile: false
---

プライバシーテック全般に関するarXiv論文まとめです。自動更新（される予定）です。

- [全てのトピック](all/)

- [秘密計算 (Multi-Party Computation)](mpc/)
- [合成データ (Synthetic Data)](sd/)
- [連合学習 (Federated Learning)](fl/)
- [差分プライバシー (Differential Privacy)](dp/)
- [準同型暗号 (Homomorphic Encryption)](he/)
- [ゼロ知識証明 (Zero-Knowledge Proof)](zkp/)
- [PETs (Privacy Enhancing Technologies)](pets/)
- [SSI/DID/VC](ssi/)
- [連合転移学習 (Federated Transfer Learning)](ftl/)


## 方法

[このPythonスクリプト](https://github.com/haruhisa-enomoto/arxiv-privacy-tech/tree/main/scripts)を[GitHub Actions](https://github.com/haruhisa-enomoto/arxiv-privacy-tech/blob/main/.github/workflows/update.yaml)で毎時日本時間13時に動かしています。

## 最新更新分

更新: {datetime.now().isoformat()}
"""


for paper in latest_papers:
    index_md += make_md_segment(paper, on_home=True)

index_file = Path("index.md")

with index_file.open("w", encoding="utf-8") as file:
    file.write(index_md)
