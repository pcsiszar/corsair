import re
from pathlib import Path

html = Path("html/03b_Interlude_Post_War.html").read_text(encoding="utf-8")
pages = re.findall(r'<div class="book-page[^"]*" id="([^"]+)">(.*?)(?=<div class="page-running-footer">)', html, re.DOTALL)
print(f"Total pages found: {len(pages)}")
for pid, body in pages:
    text = re.sub(r'<[^>]+>', ' ', body)
    words = len(text.split())
    print(f"  {pid}: {words} words")
