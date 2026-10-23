import re
from pathlib import Path

for f in sorted(Path("html").glob("*.html")):
    text = f.read_text(encoding="utf-8")
    footers = re.findall(r'<div class="page-running-footer">(.*?)</div>', text, re.DOTALL)
    print(f"{f.name:32s}: {len(footers)} footers")
    if footers:
        f_clean = re.sub(r'\s+', ' ', footers[0]).strip()
        l_clean = re.sub(r'\s+', ' ', footers[-1]).strip()
        print(f"   First: {f_clean[:80]}")
        print(f"   Last:  {l_clean[:80]}")
