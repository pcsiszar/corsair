from pathlib import Path
import re

files = [
    Path("rulebook/combat/Combat.md"),
    Path("rulebook/equipment/Equipment.md"),
    Path("rulebook/equipment/Firearms.md"),
    Path("rulebook/equipment/Melee.md"),
    Path("rulebook/equipment/Armor.md"),
    Path("rulebook/equipment/Gear.md"),
    Path("rulebook/equipment/Exotic_Hardware.md")
]

for f in files:
    content = f.read_text(encoding="utf-8")
    print("=" * 60)
    print(f"FILE: {f.name} ({len(content.split())} words)")
    print("=" * 60)
    for line in content.splitlines():
        if re.match(r"^#{1,4}\s", line):
            print("  " + line)
