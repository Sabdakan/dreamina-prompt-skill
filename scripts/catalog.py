"""Print Dreamina's live model and voice catalog in a compact form.

Needs Dreamina's own CLI, `dreamina-canvas`, installed and signed in (`dreamina-canvas auth login`).
Runs READ-ONLY commands only: auth status, model list, voice list. It never creates a canvas,
a node or a generation, and never spends credits.

Usage:
  python "<skill folder>/scripts/catalog.py"                 all types
  python "<skill folder>/scripts/catalog.py" image|video|audio|voices
  python "<skill folder>/scripts/catalog.py" --json image    raw JSON of one list
"""
import json
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ALLOWED = (("auth", "status"), ("model", "list"), ("voice", "list"))
TAG_EN = {"男": "male", "女": "female", "英文": "English", "中文": "Chinese", "日文": "Japanese",
          "韩文": "Korean", "少年": "youth", "青年": "young adult", "中年": "middle-aged", "老年": "elderly",
          "儿童": "child", "幼儿": "toddler", "适合旁白": "narration", "适合口播": "voice-over / ads",
          "情景演绎": "acting"}


def find_cli():
    exe = shutil.which("dreamina-canvas")
    if not exe:
        home_bin = Path.home() / "bin" / ("dreamina-canvas.exe" if sys.platform == "win32" else "dreamina-canvas")
        exe = str(home_bin) if home_bin.exists() else None
    if not exe:
        sys.exit("dreamina-canvas is not installed. See Dreamina's 'Plugins & CLI' page; then run "
                 "`dreamina-canvas auth login`. Without it, read MODEL-NOTES.md instead.")
    return exe


def run(exe, *args):
    if tuple(args[:2]) not in ALLOWED:
        sys.exit(f"refused: only read-only commands are allowed, not {' '.join(args[:2])}")
    r = subprocess.run([exe, "--format", "json", "--non-interactive", *args],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    try:
        out = json.loads(r.stdout or r.stderr)
    except json.JSONDecodeError:
        sys.exit(f"unreadable reply from dreamina-canvas: {(r.stdout or r.stderr)[:300]}")
    if not out.get("ok"):
        err = out.get("error", {})
        hint = " Sign in first: dreamina-canvas auth login" if r.returncode == 11 else ""
        sys.exit(f"dreamina-canvas: {err.get('message')} {err.get('diagnostics', '')}{hint}")
    return out["data"]


def flag(f):
    name = f["flag"].lstrip("-")
    if name == "prompt":
        return f"prompt up to {f.get('maxLength')} chars" + ("" if f.get("required") else " (optional)")
    if "values" in f:
        return f"{name}: " + " ".join(str(v) for v in f["values"])
    if "min" in f or "max" in f:
        return f"{name}: {f.get('min')}-{f.get('max')}"
    return name + (" (required)" if f.get("required") else "")


def refs(r):
    if not r or not r.get("max"):
        return "no references"
    s = f"references up to {r['max']} (" + ", ".join(
        f"{t['mediaType']} {t.get('min', 0)}-{t.get('max')}" for t in r.get("types", [])) + ")"
    if r.get("mutuallyExclusiveTypes"):
        s += f"; not together: {' + '.join(r['mutuallyExclusiveTypes'])}"
    return s


def models(exe, kind):
    items = run(exe, "model", "list", "--type", kind)["items"]
    print(f"\n=== {kind.upper()}: {len(items)} models ===")
    for m in items:
        print(f"\n{m['displayName']}  ({m['model']})")
        for mode in m["modes"]:
            label = mode["name"] + (f" / {mode['scenario']}" if mode.get("scenario") else "")
            parts = [flag(f) for f in mode.get("flags", []) if f["flag"] != "--scenario"]
            line = f"  {label}: " + "; ".join(parts) + f"; {refs(mode.get('references'))}"
            if mode.get("vipResolutions"):
                line += f"; member resolutions: {' '.join(mode['vipResolutions'])}"
            for bad in mode.get("forbiddenParamCombinations", []):
                line += f"; not allowed together: {', '.join(f'{k}={list(v.values())[-1]}' for k, v in bad.items())}"
            print(line)


def voices(exe):
    data = run(exe, "voice", "list", "--count", "100")["models"]
    print("\n=== VOICES ===")
    for model, block in data.items():
        items = block["items"]
        print(f"\n{model}: {block.get('totalCount', len(items))} voices"
              + (" (first page only)" if block.get("hasMore") else ""))
        for key in ("gender", "age", "accent", "language"):
            c = Counter(TAG_EN.get(i["tags"].get(key), i["tags"].get(key)) for i in items if i["tags"].get(key))
            if c:
                print(f"  {key}: " + ", ".join(f"{k} {n}" for k, n in c.most_common()))
        print("  " + ", ".join(i["voiceName"] for i in items))


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    exe = find_cli()
    raw = "--json" in argv
    want = [a for a in argv if a in ("image", "video", "audio", "voices")] or ["image", "video", "audio", "voices"]
    status = run(exe, "auth", "status")
    if not status.get("loggedIn"):
        sys.exit("Not signed in. Run: dreamina-canvas auth login")
    for w in want:
        if raw:
            args = ("voice", "list", "--count", "100") if w == "voices" else ("model", "list", "--type", w)
            print(json.dumps(run(exe, *args), ensure_ascii=False, indent=1))
        elif w == "voices":
            voices(exe)
        else:
            models(exe, w)


if __name__ == "__main__":
    main(sys.argv[1:])
