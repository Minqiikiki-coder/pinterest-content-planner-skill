#!/usr/bin/env python3
"""Validate a Pinterest Content Planner plan file against the skill's
mechanical rules (see SKILL.md, "Validation checklist").

Usage:
    python3 tests/validate_plan.py examples/wabisabi-7day-plan.md
    python3 tests/validate_plan.py plan.md --keywords "indoor plants,plant shelf"
    python3 tests/validate_plan.py plan.md --expect-split 10,6,5

Checks per pin block ("### Day X — Pin N" sections with Title / Board /
Subject / Description / Image brief fields):
  * title <= 100 characters and in "Keyword | Vibe" format
  * description is exactly 2 sentences (disclosure line excluded)
  * description contains >= 2 niche keywords
  * description contains a save prompt ("Save this ...")
  * AI disclosure line present ("Image created with AI")
  * no duplicate titles or subjects across the plan
Optionally checks the board split against --expect-split.
Exits 0 and prints ALL CHECKS PASSED when everything holds.
"""

import argparse
import re
import sys
from collections import Counter

DEFAULT_KEYWORDS = [
    "wabi-sabi", "japandi interior", "minimalist home decor",
    "neutral aesthetic", "calm interior", "slow living",
    "stoneware ceramics", "linen textures", "cozy reading corner",
    "cafe interior design", "matcha ritual", "slow morning",
]

BLOCK_RE = re.compile(r"^### Day .+? — Pin \d+\s*$", re.M)


def field(block: str, name: str, stop_names: list[str]) -> str:
    """Extract a '- Name: ...' field, up to the next field line."""
    pattern = rf"^- {name}: (.*?)(?=^- (?:{'|'.join(stop_names)}): |\Z)"
    m = re.search(pattern, block, re.M | re.S)
    return m.group(1).strip() if m else ""


def count_sentences(text: str) -> int:
    return len(re.findall(r"[.!?](?:\s|$)", text))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--keywords", help="comma-separated niche keywords")
    ap.add_argument("--expect-split", help="expected board counts, e.g. 10,6,5")
    args = ap.parse_args()

    keywords = (
        [k.strip().lower() for k in args.keywords.split(",") if k.strip()]
        if args.keywords else DEFAULT_KEYWORDS
    )

    text = open(args.plan, encoding="utf-8").read()
    starts = [m.start() for m in BLOCK_RE.finditer(text)]
    if not starts:
        print("FAIL: no pin blocks found (expected '### Day X — Pin N' sections)")
        return 1
    blocks = []
    for i, s in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else text.find("\n## ", s)
        blocks.append(text[s:end if end != -1 else len(text)])

    failures: list[str] = []
    titles: Counter[str] = Counter()
    subjects: Counter[str] = Counter()
    boards: Counter[str] = Counter()

    for i, block in enumerate(blocks, 1):
        title = field(block, "Title", ["Board", "Subject", "Description", "Image brief"])
        board = field(block, "Board", ["Title", "Subject", "Description", "Image brief"])
        subject = field(block, "Subject", ["Title", "Board", "Description", "Image brief"])
        raw_desc = field(block, "Description", ["Title", "Board", "Subject", "Image brief"])

        label = f"Pin {i} ({title[:40] or 'untitled'})"
        if not title:
            failures.append(f"{label}: missing Title")
            continue
        if len(title) > 100:
            failures.append(f"{label}: title is {len(title)} chars (> 100)")
        if "|" not in title:
            failures.append(f"{label}: title lacks 'Keyword | Vibe' separator")

        has_disclosure = "Image created with AI" in raw_desc
        desc = raw_desc.replace("Image created with AI", "").strip()
        if count_sentences(desc) != 2:
            failures.append(f"{label}: description has {count_sentences(desc)} sentences (expected 2)")
        if "Save this" not in desc:
            failures.append(f"{label}: description lacks a save prompt")
        hits = [k for k in keywords if k in desc.lower()]
        if len(hits) < 2:
            failures.append(f"{label}: only {len(hits)} niche keywords in description (expected >= 2)")
        if not has_disclosure:
            failures.append(f"{label}: missing 'Image created with AI' disclosure")

        titles[title.lower()] += 1
        subjects[subject.lower()] += 1
        boards[board] += 1

    for t, n in titles.items():
        if n > 1:
            failures.append(f"Duplicate title x{n}: {t}")
    for s, n in subjects.items():
        if n > 1:
            failures.append(f"Duplicate subject x{n}: {s}")

    print(f"Pins checked: {len(blocks)}")
    print("Board split: " + ", ".join(f"{b} = {n}" for b, n in boards.most_common()))
    if args.expect_split:
        expected = sorted(int(x) for x in args.expect_split.split(","))
        actual = sorted(boards.values())
        if actual != expected:
            failures.append(f"Board split {actual} != expected {expected}")

    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print(" -", f)
        return 1
    print(f"ALL CHECKS PASSED ({len(blocks)} pins)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
