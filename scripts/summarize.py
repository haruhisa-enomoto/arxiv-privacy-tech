import os

import arxiv
from openai import OpenAI


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM = """
# 指示
- 与えられたタイトルとアブストに対して、日本語で重要なポイントを簡潔にまとめ、箇条書き(最大4個)で要約してください
- 最後の読点は不要です
- 1つ1つは短く簡潔にまとめてください

# 訳語
英単語の日本語訳として必要ならば以下を用いてください
- 連合学習
- 合成データ
- 差分プライバシー
- 準同型暗号
- 秘密計算
- ゼロ知識証明

# 出力例
*ここに論文タイトルの和訳が入る*

- fooはbarだが、bazがあり困難
- 新たにblaを提案、それによりhogeが改善
- この研究は、fugaを用いてpiyoを実現
...
"""


def get_summary(result: arxiv.Result) -> str:
    print(f"Getting summary for {result.entry_id}")
    text = f"Title: {result.title}\nAbstract: {result.summary}"

    response = openai_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text},
        ],
    )
    summary = response.choices[0].message.content
    print(summary)
    return summary
