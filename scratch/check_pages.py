from pathlib import Path
import re

for fname in ["00_Front_Matter.html", "01_Core_Mechanics.html", "01b_Interlude_27th_Hour.html", 
              "02_Character_Creation.html", "02b_Interlude_Great_Tithe.html", 
              "03_Classes.html", "03b_Interlude_Post_War.html", 
              "04_Armory_and_Gear.html", "05_Starships.html"]:
    fpath = Path("html") / fname
    if fpath.exists():
        txt = fpath.read_text(encoding="utf-8")
        nums = re.findall(r'<span class="page-num">(\d+)</span>', txt)
        print(f"{fname:30s}: {len(nums):2d} pages | Start: {nums[0] if nums else '?'} -> End: {nums[-1] if nums else '?'}")
