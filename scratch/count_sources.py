from pathlib import Path

files = [
    "rulebook/combat/Combat.md",
    "rulebook/equipment/Equipment.md",
    "rulebook/equipment/Firearms.md",
    "rulebook/equipment/Melee.md",
    "rulebook/equipment/Armor.md",
    "rulebook/equipment/Gear.md",
    "rulebook/equipment/Exotic_Hardware.md"
]

total = 0
for fpath in files:
    p = Path(fpath)
    text = p.read_text(encoding="utf-8")
    words = len(text.split())
    total += words
    print(f"{p.name:25s}: {words:5d} words")
print("-" * 35)
print(f"{'Total Source Words':25s}: {total:5d} words")
