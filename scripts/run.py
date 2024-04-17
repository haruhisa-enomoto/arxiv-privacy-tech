import datetime as dt
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path

import arxiv
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

json_file = Path("_data/papers.json")
original_json_file = Path("_data/papers_original.json")

query_dict = {
    "連合学習": '(abs:"federated learning" OR abs:"VFL" OR abs:"HFL" OR abs:"FL")',
    "合成データ": '(abs:"synthetic data" OR abs:"data synthesis")',
    "SSI/DID/VC": '(abs:"decentralized identity" OR abs:"decentralised identity" OR abs:"self-sovereign identity" OR abs:"verifiable credentials")',
    "差分プライバシー": '(abs:"differential privacy")',
    "連合転移学習": '(abs:"federated transfer learning" OR abs: "FTL")',
    "準同型暗号": '(abs:"homomorphic encryption")',
    "秘密計算": '(abs:"multi-party computation" OR abs:"multiparty computation")',
    "PETs": '(abs:"privacy enhancing technologies" OR abs:"privacy-enhancing technologies" OR abs:"privacy enhancing technology" OR abs:"privacy-enhancing technology")',
}
GENRE = 'AND (cat:"cs.AI" OR cat:"cs.AR" OR cat:"cs.CC" OR cat:"cs.CE" OR cat:"cs.CG" OR cat:"cs.CL" OR cat:"cs.CR" OR cat:"cs.CV" OR cat:"cs.CY" OR cat:"cs.DB" OR cat:"cs.DC" OR cat:"cs.DL" OR cat:"cs.DM" OR cat:"cs.DS" OR cat:"cs.ET" OR cat:"cs.FL" OR cat:"cs.GL" OR cat:"cs.GR" OR cat:"cs.GT" OR cat:"cs.HC" OR cat:"cs.IR" OR cat:"cs.IT" OR cat:"cs.LG" OR cat:"cs.LO" OR cat:"cs.MA" OR cat:"cs.MM" OR cat:"cs.MS" OR cat:"cs.NA" OR cat:"cs.NE" OR cat:"cs.NI" OR cat:"cs.OH" OR cat:"cs.OS" OR cat:"cs.PF" OR cat:"cs.PL" OR cat:"cs.RO" OR cat:"cs.SC" OR cat:"cs.SD" OR cat:"cs.SE" OR cat:"cs.SI" OR cat:"cs.SY" OR cat:"stats.ML")'

N_DAYS = 5
# MAX_RESULT = 10


SYSTEM = """
# 指示
- 与えられたタイトルとアブストに対して、日本語で重要なポイントを簡潔にまとめ、箇条書き(最大4個)で要約せよ
- 最後の読点は不要
- 1つ1つは短く簡潔にまとめる
- 論文タイトル和訳は1つの*で囲む

# 訳語
英単語の日本語訳として必要ならば以下を用いること
- 連合学習
- 合成データ
- 差分プライバシー
- 準同型暗号
- 秘密計算

# 出力例
*{ここに論文タイトルの和訳が入る}*

- fooはbarだが、bazがあり困難
- 新たにblaを提案、それによりhogeが改善
- この研究は、fugaを用いてpiyoを実現
...
"""


def get_summary(result: arxiv.Result) -> str:
    # text = f"Title: {result.title}\nAbstract: {result.summary}"

    # response = openai_client.chat.completions.create(
    #     model="gpt-4-turbo",
    #     messages=[
    #         {"role": "system", "content": SYSTEM},
    #         {"role": "user", "content": text},
    #     ],
    # )
    # return response.choices[0].message.content
    with open(original_json_file, "r", encoding="utf-8") as f:
        paper_info_json_list = json.load(f)
    # Search for the paper in the original JSON file by title
    for paper_info in paper_info_json_list:
        if paper_info["title"] == result.title:
            return paper_info["summary"]
    raise ValueError(f"Paper not found in the original JSON file: {result.title}")


@dataclass(frozen=True)
class PaperInfo:
    url: str
    authors: tuple[str, ...]
    categories: tuple[str, ...]
    comment: str
    summary: str
    title: str
    japanese_title: str
    topics: tuple[str, ...]
    published: dt.datetime


def paper_info_to_json(paper_info: PaperInfo) -> dict:
    return {
        "url": paper_info.url,
        "title": paper_info.title,
        "japanese_title": paper_info.japanese_title,
        "authors": paper_info.authors,
        "categories": paper_info.categories,
        "comment": paper_info.comment,
        "summary": paper_info.summary,
        "topics": paper_info.topics,
        "published": paper_info.published.strftime("%Y-%m-%d"),
    }


def sort_and_remove_dups(paper_list: list[PaperInfo]) -> list[PaperInfo]:
    paper_list_wo_dups = list(set(paper_list))
    return sorted(paper_list_wo_dups, key=lambda x: x.published, reverse=True)


def dump_paper_info_list(result_list: list[arxiv.Result], json_file: Path):
    paper_info_list = [get_paper_info(paper) for paper in result_list]
    paper_info_list = sort_and_remove_dups(paper_info_list)
    paper_info_json_list = [
        paper_info_to_json(paper_info) for paper_info in paper_info_list
    ]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(paper_info_json_list, f, ensure_ascii=False, indent=2)


def get_paper_info(paper: arxiv.Result):
    url = re.sub(r"v\d+$", "", paper.entry_id)
    title = paper.title
    authors = [author.name for author in paper.authors]
    categories = paper.categories
    comment = paper.comment if paper.comment is not None else ""
    comment = comment.replace("\n", " ")
    published = paper.published
    print(f"Getting summary for {title}...")
    summary = get_summary(paper)
    # summary = "dummy"
    japanese_title = summary.split("\n")[0].strip("*")
    summary = "\n".join(summary.split("\n")[1:]).strip()
    topics: list[str] = []
    for key, lst in results.items():
        if paper in lst:
            topics.append(key)
    return PaperInfo(
        url=url,
        title=title,
        japanese_title=japanese_title,
        authors=tuple(authors),
        categories=tuple(categories),
        topics=tuple(topics),
        comment=comment,
        summary=summary,
        published=published,
    )


if __name__ == "__main__":
    today = dt.datetime.today()
    base_date = today - dt.timedelta(days=N_DAYS)
    results: dict[str, list[arxiv.Result]] = {}

    for key in query_dict.keys():
        query = f"{query_dict[key]} AND submittedDate:[20240401 TO 20240431] {GENRE}"

        search = arxiv.Search(
            query=query,
            # max_results=10,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        arxiv_client = arxiv.Client()
        results[key] = list(arxiv_client.results(search))

    for key in results.keys():
        for result in results[key]:
            print(result.title)

    all_results: list[arxiv.Result] = []
    for key in results.keys():
        for result in results[key]:
            if result not in all_results:
                all_results.append(result)
    dump_paper_info_list(all_results, json_file)
