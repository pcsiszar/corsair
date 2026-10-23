import re
from pathlib import Path

files = [
    '00_Front_Matter.html',
    '01_Core_Mechanics.html',
    '01b_Interlude_27th_Hour.html',
    '02_Character_Creation.html',
    '03_Classes.html',
    '03b_Interlude_Post_War.html'
]

for f in files:
    p = Path('html') / f
    if not p.exists():
        continue
    content = p.read_text(encoding='utf-8')
    nums = re.findall(r'<span class="page-num">(\d+)</span>', content)
    if nums:
        print(f"{f:30s}: count={len(nums):2d}, range={nums[0]} to {nums[-1]}")
    else:
        # maybe front matter has no page numbers or roman numerals
        pages = len(re.findall(r'class="book-page', content))
        print(f"{f:30s}: {pages} pages (no arabic page-num)")
