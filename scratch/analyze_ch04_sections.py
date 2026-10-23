from pathlib import Path
import re

files = [
    ("Combat", Path("rulebook/combat/Combat.md")),
    ("Equipment", Path("rulebook/equipment/Equipment.md")),
    ("Firearms", Path("rulebook/equipment/Firearms.md")),
    ("Melee", Path("rulebook/equipment/Melee.md")),
    ("Armor", Path("rulebook/equipment/Armor.md")),
    ("Gear", Path("rulebook/equipment/Gear.md")),
    ("Exotic Hardware", Path("rulebook/equipment/Exotic_Hardware.md")),
]

for title, path in files:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    print("=" * 60)
    print(f"{title.upper()} - {len(content.split())} words, {len(lines)} lines")
    print("=" * 60)
    cur_sec = "Intro"
    cur_words = 0
    for line in lines:
        if line.startswith("#"):
            if cur_words > 0:
                print(f"  {cur_sec:45s}: {cur_words:4d} words")
            cur_sec = line.strip()
            cur_words = 0
        else:
            cur_words += len(line.split())
    if cur_words > 0:
        print(f"  {cur_sec:45s}: {cur_words:4d} words")
