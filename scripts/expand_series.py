"""Expand one prompt frame and a list of subjects into a ready-to-copy prompt sheet.

Usage: python "<skill folder>/scripts/expand_series.py" <frame.txt> <items.csv> <out.md> [--force]
  frame.txt  the fixed prompt with {subject} where the slot goes
  items.csv  columns: id,name,subject  (UTF-8, header row)
  out.md     the sheet, usually <project folder>/docs/dreamina/series-<name>.md;
             refused if it exists and holds ticked boxes, unless --force
All paths come from the command line; the script has none built in.
"""
import argparse
import csv
import sys
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("frame")
    p.add_argument("items")
    p.add_argument("out")
    p.add_argument("--force", action="store_true", help="overwrite a sheet that has ticked boxes")
    a = p.parse_args()

    frame = Path(a.frame).read_text(encoding="utf-8").strip()
    if "{subject}" not in frame:
        sys.exit("frame has no {subject} slot")

    with Path(a.items).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    missing = {"id", "name", "subject"} - set(rows[0].keys() if rows else [])
    if missing:
        sys.exit(f"items.csv lacks columns: {', '.join(sorted(missing))}")

    seen, problems = set(), []
    for n, r in enumerate(rows, start=2):
        rid = (r["id"] or "").strip()
        if not rid or not (r["subject"] or "").strip():
            problems.append(f"line {n}: empty id or subject")
        if rid in seen:
            problems.append(f"line {n}: duplicate id {rid}")
        seen.add(rid)
    if problems:
        sys.exit("\n".join(problems))

    out = Path(a.out)
    if out.exists() and "- [x]" in out.read_text(encoding="utf-8") and not a.force:
        sys.exit(f"{out} has ticked boxes; pass --force to overwrite it")

    parts = [f"# Prompt sheet: {out.stem}", "",
             f"{len(rows)} pictures. Frame: `{Path(a.frame).name}` · Items: `{Path(a.items).name}`.",
             "Upload the anchor picture as the style reference for every item, or mention its Style Element with @. "
             "Tick a box when its picture is approved.", ""]
    for r in rows:
        parts += [f"## {r['id'].strip()} - {r['name'].strip()}", "",
                  f"- [ ] approved -> `{r['id'].strip()}.png`", "",
                  "```", frame.replace("{subject}", r["subject"].strip()), "```", ""]
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {out} ({len(rows)} prompts)")


if __name__ == "__main__":
    main()
