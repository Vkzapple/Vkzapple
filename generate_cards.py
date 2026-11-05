import os
from collections import Counter
from html import escape

import requests

USER = os.getenv("GH_USER", "Vkzapple")
TOKEN = os.getenv("GH_TOKEN")
# NOTE: kartu di-refresh tiap kali file ini berubah (triggers update-cards workflow)
MODE = os.getenv("LANG_MODE", "repo")
OUT = "assets"
FONT = "'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif"

HEADERS = {"Accept": "application/vnd.github+json"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178C6", "JavaScript": "#F1E05A",
    "Rust": "#DEA584", "Kotlin": "#A97BFF", "PHP": "#4F5D95", "C#": "#178600",
    "HTML": "#E34C26", "CSS": "#563D7C", "Jupyter Notebook": "#DA5B0B",
    "C++": "#F34B7D", "C": "#555555", "Blade": "#F7523F", "Dart": "#00B4AB",
    "Java": "#B07219", "Shell": "#89E051", "Other": "#8B949E",
}
FALLBACK = ["#ea6161", "#ffc64d", "#52fa5a", "#4dfcff", "#c64dff", "#ff8fab"]


def api(url, **params):
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_repos():
    repos, page = [], 1
    while True:
        data = api(f"https://api.github.com/users/{USER}/repos",
                   per_page=100, page=page, type="owner")
        if not data:
            return [r for r in repos if not r["fork"]]
        repos += data
        page += 1


def total_commits():
    try:
        return api("https://api.github.com/search/commits",
                   q=f"author:{USER}", per_page=1)["total_count"]
    except Exception:
        return None


def color_for(lang, i):
    return LANG_COLORS.get(lang, FALLBACK[i % len(FALLBACK)])


def gradient(gid, colors):
    n = len(colors) - 1 or 1
    stops = "".join(
        f'<stop offset="{i / n:.2f}" stop-color="{c}"/>' for i, c in enumerate(colors))
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
            f"{stops}</linearGradient></defs>")


def stats_svg(rows, w=360, h=137):
    lines = "".join(
        f'<text x="20" y="{34 + i * 24}" font-size="14" fill="#000" '
        f'font-family="{FONT}">{escape(label)}</text>'
        f'<text x="{w - 20}" y="{34 + i * 24}" font-size="14" font-weight="700" '
        f'fill="#000" text-anchor="end" font-family="{FONT}">{escape(str(val))}</text>'
        for i, (label, val) in enumerate(rows))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">'
            f'{gradient("g", ["#ea6161", "#ffc64d", "#fffc4d", "#52fa5a"])}'
            f'<rect width="{w}" height="{h}" rx="6" fill="url(#g)"/>{lines}</svg>')


def langs_svg(items, w=300, h=137, limit=10):
    items = items[:limit]
    total = sum(v for _, v in items) or 1
    bar, x = "", 20
    bar_w = w - 40
    for i, (lang, v) in enumerate(items):
        seg = bar_w * v / total
        bar += (f'<rect x="{x:.1f}" y="18" width="{seg:.1f}" height="8" '
                f'fill="{color_for(lang, i)}"/>')
        x += seg
    legend = ""
    for i, (lang, v) in enumerate(items):
        col, row = i % 2, i // 2
        lx, ly = 20 + col * 135, 48 + row * 19
        legend += (f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4" fill="{color_for(lang, i)}"/>'
                   f'<text x="{lx + 14}" y="{ly}" font-size="11" fill="#000" '
                   f'font-family="{FONT}">{escape(lang)} {v / total:.1%}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">'
            f'{gradient("g2", ["#52fa5a", "#4dfcff", "#c64dff"])}'
            f'<rect width="{w}" height="{h}" rx="6" fill="url(#g2)"/>'
            f'<clipPath id="c"><rect x="20" y="18" width="{w - 40}" height="8" rx="4"/></clipPath>'
            f'<g clip-path="url(#c)">{bar}</g>{legend}</svg>')


def main():
    repos = fetch_repos()
    user = api(f"https://api.github.com/users/{USER}")

    commits = total_commits()
    rows = [
        ("Total Stars", sum(r["stargazers_count"] for r in repos)),
        ("Total Commits", f"{commits:,}" if commits is not None else "-"),
        ("Public Repos", len(repos)),
        ("Followers", user["followers"]),
    ]

    if MODE == "bytes":
        counter = Counter()
        for r in repos:
            counter.update(api(r["languages_url"]))
    else:
        counter = Counter(r["language"] or "Other" for r in repos)

    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/stats.svg", "w", encoding="utf-8") as f:
        f.write(stats_svg(rows))
    with open(f"{OUT}/top-langs.svg", "w", encoding="utf-8") as f:
        f.write(langs_svg(counter.most_common()))
    print("Kartu dibuat di", OUT)


if __name__ == "__main__":
    main()