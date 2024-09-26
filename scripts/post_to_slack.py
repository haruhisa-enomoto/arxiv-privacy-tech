import os
import re
import time

from paper_info import PaperInfo
from slack_sdk import WebClient


def make_slack_message(paper: PaperInfo) -> str:
    # TODO: Refactor
    if paper.comment:
        message = f"""<{paper.url}|*{paper.title.replace("*", "")}*>
*{paper.japanese_title.replace("*", "")}*
{", ".join(paper.authors)}

{re.sub(r"^- ", "• ", paper.summary, flags=re.MULTILINE)}

*Comment:* {paper.comment}
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


def post_paper_to_slack(paper: PaperInfo, max_retries=5):
    print("Sleeping 1 sec...")
    time.sleep(1)
    print(f"Posting {paper.url} to Slack...")
    SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
    SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")
    assert SLACK_TOKEN is not None
    assert SLACK_CHANNEL_ID is not None

    slack_client = WebClient(token=SLACK_TOKEN)

    retries = 0
    while retries < max_retries:
        try:
            slack_client.chat_postMessage(
                channel=SLACK_CHANNEL_ID,
                text=make_slack_message(paper),
                unfurl_links=False
            )
            print(f"Posted {paper.url} to Slack successfully.")
            break  # 成功したらループを抜ける
        except SlackApiError as e:
            if e.response["error"] == "ratelimited":
                retries += 1
                retry_after = int(e.response.headers.get("Retry-After", 1))
                print(f"Rate limit hit. Retrying in {retry_after} seconds...")
                time.sleep(retry_after)
            else:
                # その他のエラーの場合は例外をそのまま投げる
                print(f"Failed to post {paper.url} to Slack. Error: {e}")
                raise
        except Exception as e:
            # SlackApiError以外の予期しないエラーが発生した場合
            print(f"Unexpected error: {e}")
            raise

    if retries == max_retries:
        print(f"Failed to post {paper.url} after {max_retries} retries.")
