import re
from pathlib import Path

# Load markdown source files
combat_md = Path("rulebook/combat/Combat.md").read_text(encoding="utf-8")
equip_md = Path("rulebook/equipment/Equipment.md").read_text(encoding="utf-8")
firearms_md = Path("rulebook/equipment/Firearms.md").read_text(encoding="utf-8")
melee_md = Path("rulebook/equipment/Melee.md").read_text(encoding="utf-8")
armor_md = Path("rulebook/equipment/Armor.md").read_text(encoding="utf-8")
gear_md = Path("rulebook/equipment/Gear.md").read_text(encoding="utf-8")
exotic_md = Path("rulebook/equipment/Exotic_Hardware.md").read_text(encoding="utf-8")

print("Loaded all 7 source files successfully.")
