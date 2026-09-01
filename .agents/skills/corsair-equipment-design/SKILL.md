---
name: corsair-equipment-design
description: >-
  Design guidelines, mathematical invariants, naming conventions, load tiering, and upgrade economics for designing or overhauling Equipment (Melee, Firearms, Armor, Gear) in Corsair.
---

# Corsair Equipment Design System

This skill documents the design principles, mathematical rules, naming conventions, and economic frameworks for authoring and balancing equipment in Corsair. Use this skill whenever designing or revising items in **Melee**, **Firearms**, **Armor**, and **Gear**.

---

## 1. Mathematical Invariants: Zero-Division Rule

* **No Division Formulas:** Never use mathematical division (e.g., `STR/2`, `STR/3`, or `(Agility / 3) + 1`).
* **Flat Integer Scaling:** All weapon bonuses, armor protections, and stat requirements must use flat integer additions (`+1`, `+2`, `+3`, etc.) or direct attribute references (e.g., *"equal to the lower attribute of the test"*).
* **Threshold Requirements:** Physical scaling should use minimum attribute thresholds (e.g., **Min STR 4**) with clear binary handling rules (e.g., 1H weapons require two hands if below Min STR; 2H weapons cannot be wielded).

---

## 2. Naming Conventions: D&D-Style Functional Archetypes

* **Clear Archetypes Over Model Numbers:** Primary equipment tables must use recognizable, functional archetype names (e.g., *Combat Knife, Boarding Axe, Shotgun, Assault Rifle, Heavy Armor, Riot Shield*) rather than cluttered in-universe make/model strings (*"KSK Sharkfin"*, *"VWS Scrapper"*).
* **Separation of Lore and Mechanics:** In-universe manufacturer lore (Panthera Arms, Vandal's Workshop, Caldera Foundry, Ker'Satz Korp, Chidori-Qwei) belongs in introductory text or flavor descriptions, keeping catalog tables clean and easy to scan during play.

---

## 3. Load Tiering & Weight Class Guidelines

* **Structured Load Progression:** Organize equipment across flexible Load tiers (e.g., `Load 1/2`, `1`, `2`, `3`, `4+`) to reflect increasing bulk, power, and character investment.
* **Symmetry Across Types:** Within each load tier of a weapon category, provide balanced options across different damage types, delivery methods, or tactical roles.
* **Proportional Scaling:** Higher Load and attribute requirements should correlate with greater flat damage bonuses, protection values, or tactical utility.

---

## 4. Escalating Upgrade Kit Economics (+1 Equivalent)

Mastercrafted equipment upgrades represent high-end precision aerospace machining and custom armorer tuning.

* **Hard Cap:** A single piece of equipment can benefit from a maximum of **3 Upgrade Kits**.
* **Tiered Escalating Pricing:**
  * **Weapons (Melee & Firearms):**
    * **1st Upgrade:** `10,000 Credits`
    * **2nd Upgrade:** `25,000 Credits`
    * **3rd Upgrade:** `50,000 Credits`
  * **Armor (Premium Mil-Spec Chassis):**
    * **1st Upgrade:** `25,000 Credits`
    * **2nd Upgrade:** `60,000 Credits`
    * **3rd Upgrade:** `120,000 Credits`
* **Permanent Choice Per Kit Applied:**
  * **Weight Reduction / Optimization:** Reduces the item's **Load by 1** (to a minimum of 1/2 Load for weapons, minimum of 1 Load for armor).
  * **Performance Enhancement:** Increases the item's primary flat bonus by **+1** (e.g., +1 Flat Damage Bonus for weapons, +1 Physical Protection for armor).

---

## 5. Rulebook Architecture & Document Hierarchy

* **`Equipment.md` as High-Level Hub:** Define universal concepts (e.g., Load capacity calculation `12 + (Strength × 2)`, general categories) in [Equipment.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/equipment/Equipment.md) and use direct markdown links to dedicated sub-chapter files.
* **Dedicated Sub-Chapter Files:** Detail specific mechanics, tables, and narrative examples in dedicated files:
  * [Melee.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/equipment/Melee.md)
  * [Firearms.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/equipment/Firearms.md)
  * [Armor.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/equipment/Armor.md)
  * [Gear.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/equipment/Gear.md)
* **Accompanying Printable Handouts:** Every major equipment category should maintain an A4 print-ready HTML reference sheet generated via the [`corsair-printable-sheets`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-printable-sheets/SKILL.md) skill.
