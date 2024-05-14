import os

import arxiv
from openai import OpenAI


SYSTEM = """
これから英語でプライバシー技術の論文のタイトルとアブストラクトを入力します。最初にタイトルの和訳を「*」で囲んで出力し空行を挿入し、その後にアブストラクトの要約を日本語の箇条書きでまとめてください。
項目数は4つで各項目100文字程度とし、日本語で短く簡潔にまとめてください。出力の最後に、空行を挿入し、2文程度の「おもしろそうなポイント」などの感想を簡潔に添えてください。
その際、箇条書きの部分は「です・ます調」ではなく「だ・である体」で出力し、感想の部分は未来志向で仲良しな高校3年の同級生の女の子風に書いてください。
箇条書きの点は"- "とし、結果のみを出力してください。また、決して論文と矛盾した情報が含まれないよう注意してください 。

英単語の訳として必要ならば以下を用いてください：連合学習、合成データ、差分プライバシー、準同型暗号、秘密計算、ゼロ知識証明

# 出力例
*ここに論文タイトルの和訳が入る*

- fooはbarだが、bazがあり困難
- 新たにblaを提案、それによりhogeが改善
- この研究は、fugaを用いてpiyoを実現
- quxの効果がcorgeでありwaldoが期待される

ここに感想が入る
"""


def get_summary(result: arxiv.Result) -> str:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

    print(f"Getting summary for {result.entry_id}")
    text = f"Title: {result.title}\nAbstract: {result.summary}"

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text},
        ],
    )
    summary = response.choices[0].message.content
    print(summary)
    return summary
