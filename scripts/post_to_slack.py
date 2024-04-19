import os
import re

from paper_info import PaperInfo
from slack_sdk import WebClient


def make_slack_message(paper: PaperInfo) -> str:
    # TODO: Refactor
    if paper.comment:
        message = f"""<{paper.url}|*{paper.title.replace("*", "")}*>
*{paper.japanese_title.replace("*", "")}*
{", ".join(paper.authors)}

{re.sub(r"^- ", "• ", paper.summary, flags=re.MULTILINE)}

*Comment:* {paper.comment}"
*トピック*: {", ".join(paper.topics)}, *カテゴリ*: {", ".join(paper.categories)}, *公開日時*: {paper.published.strftime("%Y-%m-%d")}
"""
    else:
        message = f"""<{paper.url}|*{paper.title.replace("*", "")}*>
*{paper.japanese_title.replace("*", "")}*
{", ".join(paper.authors)}

{re.sub(r"^- ", "• ", paper.summary, flags=re.MULTILINE)}

*トピック*: {", ".join(paper.topics)}, *カテゴリ*: {", ".join(paper.categories)}, *公開日時*: {paper.published.strftime("%Y-%m-%d")}
"""
    return message


def post_paper_to_slack(paper: PaperInfo):
    print(f"Posting {paper.url} to Slack...")
    SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
    SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")
    assert SLACK_TOKEN is not None
    assert SLACK_CHANNEL_ID is not None

    slack_client = WebClient(token=SLACK_TOKEN)
    slack_client.chat_postMessage(
        channel=SLACK_CHANNEL_ID, text=make_slack_message(paper), unfurl_links=False
    )
