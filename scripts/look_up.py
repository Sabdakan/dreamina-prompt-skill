"""Search the ui-ux-pro-max skill's style, palette and font tables for prompt vocabulary.

Usage: python "<skill folder>/scripts/look_up.py" "<words>" [--table styles|colors|fonts|all] [--max N]
Every word must appear somewhere in a row (case-insensitive) for the row to match.

The ui-ux-pro-max skill must be installed beside this skill: a sibling folder named
ui-ux-pro-max in the same skills directory, with its CSV tables in its data folder.
"""
import argparse
import csv
import sys
from pathlib import Path

# <skills dir>/dreamina-prompt/scripts/look_up.py -> <skills dir>/ui-ux-pro-max/data
SKILLS_DIR = Path(__file__).resolve().parent.parent.parent
DATA = SKILLS_DIR / "ui-ux-pro-max" / "data"

TABLES = {
    "styles": ("styles.csv", ["Style Category", "Keywords", "AI Prompt Keywords",
                              "Primary Colors", "Secondary Colors", "Best For", "Do Not Use For"]),
    "colors": ("colors.csv", ["Product Type", "Primary", "Secondary", "Accent",
                              "Background", "Foreground", "Muted", "Notes"]),
    "fonts": ("typography.csv", ["Font Pairing Name", "Heading Font", "Body Font",
                                 "Mood/Style Keywords", "Best For"]),
}


def search(table, words, limit):
    name, cols = TABLES[table]
    path = DATA / name
    if not path.exists():
        print(f"[{table}] missing: {path}")
        return 0
    found = 0
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("Status") or "").strip().lower() in {"deprecated", "retired"}:
                continue
            text = " ".join(v for v in row.values() if v).lower()
            if all(w in text for w in words):
                found += 1
                print(f"[{table}] " + " | ".join(f"{c}: {row.get(c, '').strip()}" for c in cols if row.get(c)))
                if found >= limit:
                    break
    return found


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    p.add_argument("query")
    p.add_argument("--table", default="all", choices=["styles", "colors", "fonts", "all"])
    p.add_argument("--max", type=int, default=5)
    a = p.parse_args()
    if not DATA.is_dir():
        sys.exit(
            "The ui-ux-pro-max skill was not found.\n"
            f"Looked for its data folder at: {DATA}\n"
            "Install ui-ux-pro-max as a sibling of this skill (the same skills directory), "
            "or write the style words and palette by hand from the project's art docs."
        )
    words = a.query.lower().split()
    tables = list(TABLES) if a.table == "all" else [a.table]
    total = sum(search(t, words, a.max) for t in tables)
    if total == 0:
        print("No match. Try one broader word (e.g. 'game', 'dark', 'retro', 'organic').")


if __name__ == "__main__":
    main()
