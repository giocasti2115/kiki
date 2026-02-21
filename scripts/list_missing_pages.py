from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
existing = {p.name for p in root.glob('*.html')}
refs = set()
pattern = re.compile(r'href="([^"?#]+\.html)"')

for html_file in root.glob('*.html'):
    text = html_file.read_text(encoding='utf-8', errors='ignore')
    for match in pattern.findall(text):
        if match.startswith('http'):
            continue
        refs.add(Path(match).name)

missing = sorted(refs - existing)
print('\n'.join(missing))
