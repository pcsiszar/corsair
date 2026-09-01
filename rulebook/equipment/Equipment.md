# Chapter 6: Equipment

Not every item a character carries has a significant mechanical impact on the game. Everyday objects like personal commlinks, apartment keys, or sentimental trinkets are assumed to be part of a character's belongings without needing specific rules. However, items that provide a distinct advantage in challenging situations—from weapons and armor to specialized tools—are classified as Equipment. These items are governed by the **Load** system.

## Load

Every piece of mechanically significant equipment has a **Load** value, which represents its weight, size, and cumbersomeness. A character's ability to carry this equipment is limited by their physical strength.

Your character's maximum Load capacity is **12 + (Strength x 2)**.

This limit is absolute; a character cannot carry items with a total Load value exceeding this capacity under any circumstances. It is often a wise tactical decision to leave some of your Load capacity unused. An open slot might be exactly what you need to carry a vital piece of salvage or a mission-critical objective you discover on the job.

## Equipment Categories

Equipment is divided into three major categories:

* **Weapons:** Anything designed to inflict physical harm, from vibro-knives and plasma pistols to heavy repeating blasters. See [Firearms](Firearms.md) and [Melee Weapons](Melee.md).
* **Armor:** Protective gear worn to reduce or negate incoming damage. See [Armor](Armor.md).
* **Gear:** A broad category that includes everything else of mechanical importance. See [Gear](Gear.md).

### Weapons

Weapons are divided into two main types: Melee and Ranged. While they function differently, all weapons share a common statistic: the Damage Bonus.

**Damage Bonus**

The Damage Bonus is a flat value added to the success points you generate on a successful attack roll. However, these bonus points can only be used to increase the damage dealt and cannot be used for any other purpose.

---

#### Melee Weapons

Melee weapons are engineered for brutal close-quarters combat. Each weapon deals a specific damage type—**Piercing**, **Slashing**, or **Striking**—which aligns with a favored physical Attribute Pair. Attacking with a weapon's favored pair grants a damage bonus equal to the lower attribute of the test, in addition to the weapon's flat Damage Bonus. For the full catalog of close-quarters weaponry, minimum strength requirements, and combat mechanics, see [Melee Weapons](Melee.md).

---

#### Ranged Weapons

Ranged weapons are defined by their Accuracy, Rate of Fire, Damage Bonus, and Minimum Strength.

* **Accuracy:** Ranged attacks always pair the weapon's Accuracy at the target's distance with the character's **Finesse** attribute (**Accuracy + Finesse**). Accuracy is listed as an array of four values corresponding to the four standard combat range bands:
  * **Short Range:** 0–5 spaces (~0–20m)
  * **Medium Range:** 6–12 spaces (~20–40m)
  * **Long Range:** 13–20 spaces (~40–80m)
  * **Extreme Range:** 20+ spaces (~80m+)
* **Rate of Fire (RoF):** Represents cyclic fire capability and burst control. RoF sets the maximum limit on the total number of **Crit Effects** and **Chain Effects** that can be activated on an attack roll.
* **Damage Bonus:** A flat integer bonus added directly to the total success points of a successful attack.

For the full catalog of handguns, submachine guns, shotguns, rifles, heavy support weapons, and weapon upgrade kits, see [Firearms](Firearms.md).

### Armor

Armor is protective gear worn by a character to reduce incoming physical and kinetic damage. Every suit of armor is defined by its **Protection**, **Minimum Strength (Min STR)**, **Load**, and **Cost**.

* **Protection:** A flat integer reduction applied directly to incoming damage before it affects your health. Armor Protection stacks with bonuses from **Shields** and **Cover**, but a character can only benefit from one worn suit of armor at a time.
* **Minimum Strength (Min STR):** Armor requires physical conditioning to articulate properly. If your Strength is lower than the armor's Min STR, the suit is too heavy and cumbersome to move in, and **cannot be worn or donned**.
* **Load:** The mass and physical bulk of the armor, which counts toward your maximum Load capacity.

For the full catalog of armor archetypes, defense mechanics, and armor upgrade kits, see [Armor](Armor.md).

### Gear

Gear is a broad category encompassing all other mission-critical tactical equipment, specialized toolkits, field consumables, and survival hardware that don't fall under Weapons or Armor. Gear is organized into seven tactical categories:

* **Mobility Gear:** Jump-packs, climbing gear, and motorized ziplines for vertical traversal and zero-g mobility.
* **Fortification Gear:** Deployable cover barricades, active protection defense beacons, and remote weapon mounts.
* **Explosives & Launchers:** Grenades, demolition charges, and launcher platforms executing high-yield area attacks.
* **Medical & Consumables:** Trauma kits, neuro-stabilizers, and combat stimulants providing field recovery and biochemical boosts.
* **Infiltration & Tech Kits:** Mechanic, infiltrator, and hacker toolkits providing dedicated attributes for physical and electronic intrusion.
* **Detection & Surveillance:** Passive sensors, reconnaissance drones, and forensic spectrometers for gathering situational intelligence.
* **Survival & Field Utility:** Pressurized environmental suits, encrypted commlinks, and expedition provisions.

Most gear items provide dedicated **Item Attributes** (such as *Thrust*, *Medicine*, *Sensors*, or *Hacking*) that pair with a character's core attributes for tests costing **1 Action Point (AP)**.

For the full catalog of gear items, category attributes, and special properties, see [Gear](Gear.md).

---

## Equipment Damage & Repairs

Deployable gear, fortifications, vehicles, and technological hardware possess structure ratings measured in **Health Points (HP)**. When an item takes damage from enemy fire, detonations, or environmental hazards, its HP is reduced accordingly. If an item is reduced to 0 HP, it is disabled and ceases to function until repaired.

An operator carrying a toolkit with the **Tinkering** attribute can perform field maintenance to restore damaged hardware:

* **Repairing Equipment:** Restoring HP to damaged equipment costs **1 AP** (in structured combat) or standard narrative time (in downtime) and requires a **Success Test** using **Tinkering + Knowledge**.
* **HP Restored:** The item immediately recovers **1 HP per Success Point** generated on the test, up to its maximum HP rating. Repairing completely destroyed or vaporized equipment may require dedicated workshop facilities and spare components at the GM's discretion.

