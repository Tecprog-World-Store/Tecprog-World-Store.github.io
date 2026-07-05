#!/usr/bin/env python3
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.links = {}

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            key = data.get("property") or data.get("name")
            if key:
                self.meta[key] = data.get("content", "")
        if tag == "link" and data.get("rel") == "canonical":
            self.links["canonical"] = data.get("href", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def parse_local(path: Path) -> MetaParser:
    parser = MetaParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def validate_image(path: str) -> tuple[bool, str]:
    local = ROOT / path.lstrip("/")
    if local.exists():
        return True, f"OK local {local.stat().st_size} bytes"
    if path.startswith("https://"):
        with urlopen(path, timeout=10) as response:
            return response.status == 200, f"HTTP {response.status} {response.headers.get('Content-Type', '')}"
    return False, "No existe localmente y no es HTTPS"


def main() -> None:
    courses = json.loads((ROOT / "data" / "cursos_tw_educa.json").read_text(encoding="utf-8"))
    failures = []
    for course in courses:
        page = ROOT / course["url_publica"] / "index.html"
        parser = parse_local(page)
        required = {
            "canonical": parser.links.get("canonical"),
            "og:title": parser.meta.get("og:title"),
            "og:description": parser.meta.get("og:description"),
            "og:image": parser.meta.get("og:image"),
            "og:url": parser.meta.get("og:url"),
            "twitter:image": parser.meta.get("twitter:image"),
        }
        missing = [key for key, value in required.items() if not value]
        image = parser.meta.get("og:image", "")
        image_path = image.replace("https://tecprog-world-store.github.io/", "")
        image_ok, image_status = validate_image(image_path)
        if missing or not image_ok:
            failures.append((course["id"], missing, image_status))
        print(f"OK {course['id']} {course['url_publica']} image={image_status}")
    if failures:
        raise SystemExit(f"Fallos Open Graph: {failures}")


if __name__ == "__main__":
    main()
