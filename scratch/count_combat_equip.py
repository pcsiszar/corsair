from pathlib import Path

files = [
    Path("rulebook/combat/Combat.md"),
    Path("rulebook/equipment/Equipment.md"),
    Path("rulebook/equipment/Firearms.md"),
    Path("rulebook/equipment/Melee.md"),
    Path("rulebook/equipment/Armor.md"),
    Path("rulebook/equipment/Gear.md"),
    Path("rulebook/equipment/Exotic_Hardware.md")
]

total = 0
for f in files:
    words = len(f.read_text(encoding="utf-8").split())
    total += words
    print(f"{f.name:20s}: {words:5d} words")

print("-" * 30)
print(f"Total: {total} words")
