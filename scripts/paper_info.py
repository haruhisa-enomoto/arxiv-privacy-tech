import datetime as dt
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PaperInfo:
    url: str
    authors: list[str]
    categories: list[str]
    comment: str
    summary: str
    title: str
    japanese_title: str
    topics: list[str]
    published: dt.datetime


def dump_info_list(paper_info_list: list[PaperInfo], json_file: Path):
    paper_info_json_list = [
        paper_info_to_json(paper_info) for paper_info in paper_info_list
    ]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(paper_info_json_list, f, ensure_ascii=False, indent=2)


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
        "published": paper_info.published.isoformat(),
    }


def parse_json(json_file: Path) -> list[PaperInfo]:
    with json_file.open("r", encoding="utf-8") as f:
        paper_info_json_list = json.load(f)
    return [
        PaperInfo(
            url=paper_info["url"],
            authors=paper_info["authors"],
            categories=paper_info["categories"],
            comment=paper_info["comment"],
            summary=paper_info["summary"],
            title=paper_info["title"],
            japanese_title=paper_info["japanese_title"],
            topics=paper_info["topics"],
            published=dt.datetime.fromisoformat(paper_info["published"]),
        )
        for paper_info in paper_info_json_list
    ]
