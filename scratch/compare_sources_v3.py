from pathlib import Path

source_files = {
    "Combat": "rulebook/combat/Combat.md",
    "Equipment": "rulebook/equipment/Equipment.md",
    "Firearms": "rulebook/equipment/Firearms.md",
    "Melee": "rulebook/equipment/Melee.md",
    "Armor": "rulebook/equipment/Armor.md",
    "Gear": "rulebook/equipment/Gear.md",
    "Exotic": "rulebook/equipment/Exotic_Hardware.md"
}

v3_text = Path("scratch/generate_ch04_v3.py").read_text(encoding="utf-8")

print(f"{'Source File':15s} | {'Source Words':12s} | {'Present in v3?'}")
print("-" * 50)
for name, path in source_files.items():
    stext = Path(path).read_text(encoding="utf-8")
    swords = len(stext.split())
    # Take a few sample phrases from the source file
    paragraphs = [p.strip() for p in stext.split("\n\n") if len(p.strip()) > 50]
    found = 0
    for p in paragraphs:
        # clean markdown headers/bullets
        cleaned = " ".join(p.replace("#", "").replace("*", "").replace(">", "").split()[:6])
        if cleaned in v3_text:
            found += 1
    pct = (found / len(paragraphs) * 100) if paragraphs else 0
    print(f"{name:15s} | {swords:12d} | {found}/{len(paragraphs)} paragraphs ({pct:.1f}%)")
