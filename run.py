import datetime as dt
import os

import arxiv
from openai import OpenAI


# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# openai_client = OpenAI(api_key=OPENAI_API_KEY)

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
today = dt.datetime.today()
base_date = today - dt.timedelta(days=N_DAYS)
results: dict[str, list[arxiv.Result]] = {}

for key in query_dict.keys():
    query = (
        f"{query_dict[key]} AND submittedDate:{base_date.strftime('%Y%m%d')}* {GENRE}"
    )

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

print(len(all_results))

SYSTEM = """
# 指示
- 与えられたタイトルとアブストに対して、日本語で重要なポイントを簡潔にまとめ、箇条書き(3個から5個程度)で要約せよ
- 最後の読点は不要
- 1つ1つは短く簡潔にまとめる
- 論文タイトル和訳は1つの*で囲む

# 訳語
単語の日本語訳として必要ならば以下を用いること
- 連合学習
- 合成データ
- 自己主権ID
- 差分プライバシー

# 出力例
*{ここに論文タイトルの和訳が入る}*

- fooはbarだが、bazがあり困難
- 新たにblaを提案、それによりhogeが改善
- この研究は、fugaを用いてpiyoを実現
...
"""


def get_summary(result: arxiv.Result):
    text = f"Title: {result.title}\nAbstract: {result.summary}"

    # response = openai_client.chat.completions.create(
    #     model="gpt-4-turbo",
    #     messages=[
    #         {"role": "system", "content": SYSTEM},
    #         {"role": "user", "content": text},
    #     ],
    # )
    # return response


def get_header(paper: arxiv.Result):
    title = paper.title
    author_list = [author.name for author in paper.authors]
    if len(author_list) > 3:
        author_list = author_list[:3]
        author_list.append("et al")
    authors = ", ".join(author_list)
    categories = ", ".join(paper.categories)
    comment = f"コメント: {paper.comment}. " if paper.comment else ""

    # Find keywords which query_dict contains
    keywords: list[str] = []
    for key, lst in results.items():
        if paper in lst:
            keywords.append(key)
    key_str = ", ".join(keywords)
    header = f"<{paper.entry_id}|{title}>\nトピック: {key_str}. {comment}分類: {categories}. 著者: {authors}. {paper.published.strftime('%Y-%m-%d')}."
    return header


text_file = open("output.txt", "w", encoding="utf-8")
for paper in all_results:
    header = get_header(paper)
    # response = get_summary(paper)
    # message = f"{header}\n{response.choices[0].message.content}"
    # message = message.replace("- ", "• ")
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"{header}\n")
