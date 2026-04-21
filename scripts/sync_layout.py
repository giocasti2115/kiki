import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "index.html"

try:
    index_html = INDEX_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    sys.exit("index.html not found; run from project root")

HEADER_START = "<!-- header section start -->"
HEADER_END = "<!-- sidebar section end -->"
FOOTER_START = "<!-- footer section start -->"

if HEADER_START not in index_html or HEADER_END not in index_html:
    sys.exit("Could not locate header markers in index.html")
if FOOTER_START not in index_html:
    sys.exit("Could not locate footer marker in index.html")

header_start_idx = index_html.index(HEADER_START)
header_end_idx = index_html.index(HEADER_END) + len(HEADER_END)
HEADER_BLOCK = index_html[header_start_idx:header_end_idx].rstrip() + "\n\n"

footer_start_idx = index_html.index(FOOTER_START)
TAIL_BLOCK = index_html[footer_start_idx:].strip() + "\n"

TARGET_FILES = sorted(path for path in ROOT.glob("*.html") if path.name != "index.html")

anchor_snippet = "    <span id=\"hero\" class=\"page-anchor\"></span>\n\n"

updated_files = []
skipped_files = []

for html_path in TARGET_FILES:
    content = html_path.read_text(encoding="utf-8")
    if HEADER_START not in content or HEADER_END not in content:
        skipped_files.append((html_path.name, "header markers missing"))
        continue
    if FOOTER_START not in content:
        skipped_files.append((html_path.name, "footer marker missing"))
        continue

    head_start_idx = content.index(HEADER_START)
    head_end_idx = content.index(HEADER_END) + len(HEADER_END)
    new_content = content[:head_start_idx] + HEADER_BLOCK + content[head_end_idx:]

    if "id=\"hero\"" not in new_content:
        insert_idx = new_content.index(HEADER_END) + len(HEADER_END)
        new_content = new_content[:insert_idx] + "\n" + anchor_snippet + new_content[insert_idx:]

    footer_start_idx = new_content.index(FOOTER_START)
    new_content = new_content[:footer_start_idx] + TAIL_BLOCK

    html_path.write_text(new_content, encoding="utf-8")
    updated_files.append(html_path.name)

print(f"Updated {len(updated_files)} files.")
if updated_files:
    print("Files:")
    for name in updated_files:
        print(f" - {name}")
if skipped_files:
    print("Skipped files:")
    for name, reason in skipped_files:
        print(f" - {name}: {reason}")
