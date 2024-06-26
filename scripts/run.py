import datetime as dt
import json
import re
from pathlib import Path

import arxiv
from paper_info import PaperInfo, dump_info_list, parse_json
from post_to_slack import post_paper_to_slack
from summarize import get_summary

json_file = Path("_data/papers.json")
latest_json_file = Path("_data/latest_papers.json")

query_dict = {
    "連合学習": '(abs:"federated learning" OR abs:"VFL" OR abs:"HFL" OR abs:"FL")',
    "合成データ": '(abs:"synthetic data" OR abs:"data synthesis")',
    "SSI/DID/VC": '(abs:"decentralized identity" OR abs:"decentralised identity" OR abs:"self-sovereign identity" OR abs:"verifiable credentials")',
    "差分プライバシー": '(abs:"differential privacy")',
    "連合転移学習": '(abs:"federated transfer learning" OR abs: "FTL")',
    "準同型暗号": '(abs:"homomorphic encryption")',
    "秘密計算": '(abs:"multi-party computation" OR abs:"multiparty computation")',
    "PETs": '(abs:"privacy enhancing technologies" OR abs:"privacy-enhancing technologies" OR abs:"privacy enhancing technology" OR abs:"privacy-enhancing technology")',
    "ゼロ知識証明": '(abs:"zero-knowledge" OR abs:"zero knowledge")',
    "TEE": '(abs:"TEE" OR abs:"trusted execution environment" OR abs:"SGX" OR abs:"software guard extensions" OR abs:"TDX" OR abs:"trust domain extensions" OR abs:"SEV" OR abs:"secure encrypted virtualization")',
}

GENRE = 'AND (cat:"cs.AI" OR cat:"cs.AR" OR cat:"cs.CC" OR cat:"cs.CE" OR cat:"cs.CG" OR cat:"cs.CL" OR cat:"cs.CR" OR cat:"cs.CV" OR cat:"cs.CY" OR cat:"cs.DB" OR cat:"cs.DC" OR cat:"cs.DL" OR cat:"cs.DM" OR cat:"cs.DS" OR cat:"cs.ET" OR cat:"cs.FL" OR cat:"cs.GL" OR cat:"cs.GR" OR cat:"cs.GT" OR cat:"cs.HC" OR cat:"cs.IR" OR cat:"cs.IT" OR cat:"cs.LG" OR cat:"cs.LO" OR cat:"cs.MA" OR cat:"cs.MM" OR cat:"cs.MS" OR cat:"cs.NA" OR cat:"cs.NE" OR cat:"cs.NI" OR cat:"cs.OH" OR cat:"cs.OS" OR cat:"cs.PF" OR cat:"cs.PL" OR cat:"cs.RO" OR cat:"cs.SC" OR cat:"cs.SD" OR cat:"cs.SE" OR cat:"cs.SI" OR cat:"cs.SY" OR cat:"stats.ML")'

N_DAYS = 7


def get_paper_info(paper: arxiv.Result):
    url = re.sub(r"v\d+$", "", paper.entry_id)
    title = re.sub(r"\$.*?\$", "", paper.title)
    authors = [author.name for author in paper.authors]
    categories = paper.categories
    comment = paper.comment if paper.comment is not None else ""
    comment = comment.replace("\n", " ")
    published = paper.published
    summary = get_summary(paper)
    japanese_title = summary.split("\n")[0].strip("*")
    summary = "\n".join(summary.split("\n")[1:]).strip()
    topics: list[str] = []
    for key, lst in new_results_dict.items():
        if paper in lst:
            topics.append(key)
    return PaperInfo(
        url=url,
        title=title,
        japanese_title=japanese_title,
        authors=authors,
        categories=categories,
        topics=topics,
        comment=comment,
        summary=summary,
        published=published,
    )


if __name__ == "__main__":
    current_info_list = parse_json(json_file)
    current_urls = {result.url for result in current_info_list}

    today = dt.datetime.today()
    base_date = today - dt.timedelta(days=N_DAYS)
    new_results_dict: dict[str, list[arxiv.Result]] = {}

    for key in query_dict.keys():
        query = f"{query_dict[key]} AND submittedDate:[{base_date.strftime('%Y%m%d')} TO {today.strftime('%Y%m%d')}] {GENRE}"
        search = arxiv.Search(
            query=query,
            # max_results=10,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        arxiv_client = arxiv.Client()
        fetch_results = list(arxiv_client.results(search))
        # Append only new papers (look at the URL)
        new_results_dict[key] = [
            result
            for result in fetch_results
            if re.sub(r"v\d+$", "", result.entry_id) not in current_urls
        ]
        old_results = [
            result
            for result in fetch_results
            if re.sub(r"v\d+$", "", result.entry_id) in current_urls
        ]
        print(f"Found {len(new_results_dict[key])} new papers for {key}")

    new_results: list[arxiv.Result] = []
    for key in new_results_dict.keys():
        for result in new_results_dict[key]:
            if result not in new_results:
                new_results.append(result)

    print(f"Found {len(new_results)} new papers in total")
    if not new_results:
        print("No new papers to summarize.")
        exit()

    new_info_list = [get_paper_info(result) for result in new_results]
    paper_info_list = current_info_list + new_info_list
    paper_info_list.sort(key=lambda x: x.published, reverse=True)
    new_info_list.sort(key=lambda x: x.published, reverse=True)
    dump_info_list(paper_info_list, json_file)
    dump_info_list(new_info_list, latest_json_file)
    print("Posting to Slack...")
    for paper in new_info_list:
        post_paper_to_slack(paper)
    print("Done")
