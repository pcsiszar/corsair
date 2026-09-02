---
name: corsair-class-design
description: >-
  Design guidelines, architectural rules, mathematical invariants, omnirole philosophy, action economy tags, and narrative density standards for authoring, balancing, and refining Classes in Corsair.
---

# Corsair Class Design System

This skill codifies the architectural rules, mathematical invariants, omnirole philosophy, ability taxonomy, progression tables, and narrative density standards for authoring, balancing, and refining Classes in Corsair. Use this skill whenever creating a new class or reviewing and aligning existing class rulebooks and printable sheets.

---

## 1. In-Universe Chassis Identity & Ownership

In Corsair, a **Class** is not an abstract RPG profession, calling, or permanent biological destiny. Instead, it represents an advanced, proprietary **cybernetic or technological chassis**—such as subcutaneous elemental capacitor plates, a pressurized chemical delivery harness, a neurally tethered exodrone, a morphing kinetic board, or an integrated nanite reservoir.

* **Neural Implant Interface:** Every class chassis interfaces directly with the operative's central nervous system via a standardized neural implant port.
* **Single Active Chassis Limit:** Because of neural bandwidth and metabolic load, an operative can have **only one Class chassis active/equipped at a time**.
* **Chassis Ownership & Acquisition:** Operatives select their initial chassis during character creation. During downtime (day-to-day pacing), an operative can purchase additional chassis for **100,000 Credits** each and swap which chassis they have equipped.
* **Preserved Investment:** Attribute ratings, unlocked ability packages, and purchased mods belong to each specific chassis and remain intact when an operative swaps between owned chassis.

---

## 2. The Modular Omnirole Principle

Corsair rejects rigid, MMO-style holy trinity roles (e.g., dedicated healer, pure tank, or glass cannon DPS). A class must never be pigeonholed into a single operational archetype.

* **Universal Role Viability:** Every class chassis must offer viable build paths across all four core tactical pillars through its ability selections and mod choices:
  1. **Direct Damage / Offense / Burst:** Inflicting harm, penetrating armor, or clearing groups.
  2. **Protection / Defense / Tanking:** Mitigating incoming damage, shielding allies, creating cover, or contesting enemy assaults.
  3. **Restoration / Support / Buffs:** Healing light/aggravated wounds, restoring stress, granting Upgrades, or clearing debuffs.
  4. **Battlefield Control / Mobility / Utility:** Manipulating terrain, vertical/rapid movement, recon, forced repositioning, hacking, or stealth.
* **Modular Customization:** An operative's active role is defined by their chosen ability packages and mod loadouts, allowing two operatives sharing the same class to play completely differently (e.g., an offensive Pyromancer Conduit vs. a defensive/support Cryo Conduit).

---

## 3. Class Attribute Architecture & Test Resolution

Every class is defined by a signature set of **exactly three Class Attributes**.

### Character Creation Distribution
* **Base Rating:** Every Class Attribute starts at a baseline value of **1** (base `1 / 1 / 1`).
* **Creation Points:** Operatives receive **7 Class Creation Points** to distribute across their three Class Attributes.
* **Point Costs:**
  * Raising an Attribute from **1 to 4** costs **1 point** per increase.
  * Raising an Attribute from **4 to 5** costs **2 points**.
* **Starting Cap:** The maximum rating for any Class Attribute at character creation is **5**. Operatives may leave an Attribute at its starting value of 1.

### Test Engine Integration
Class Attributes seamlessly plug into Corsair's core dice resolution engine:
* **Attribute Pairs:** Class tests pair a Class Attribute with a relevant Core Attribute (`Class + Core`, e.g., *Flame + Strength* or *Create + Finesse*), or with itself / another Class Attribute (`Class + Class`, e.g., *Control + Control* or *Hazard + Hazard*).
* **Pool & Success Resolution:** As with all Corsair tests:
  * **Dice Pool:** Roll d10s equal to the **higher** Attribute in the pair.
  * **Success Pool (Complex Tests):** Select dice equal to the **lower** Attribute in the pair; the highest die among them determines **Success Points**.
  * **Hits:** Any die showing **8 or higher** is a Hit, which can be sacrificed to activate core or class-specific Effects.

---

## 4. Mathematical Invariants & Scaling Rules

Class design follows balanced mathematical invariants to prevent runaway power curves while maintaining clean table math:

* **Fractional Division Exception:** Unlike the Equipment Design system (which strictly bans division formulas), Class Design **explicitly permits fractional division formulas** (e.g., *"equal to half your [Attribute] rounded down"* or *"rounded up"*) specifically where flat integer scaling would grow too aggressive at high attribute ratings (e.g., passive Physical Protection or baseline melee attack bonuses).
* **Flat Integer Modifiers:** Where fractional scaling is not required, use flat integer bonuses (`+1`, `+2`, `+3`) or direct 1-to-1 attribute references (e.g., *"gain a damage bonus equal to your Hazard Attribute"*).
* **Stepped Threshold Scaling:** When converting Success Points into mechanical benefits, use simple integer steps (e.g., *"heal 1 Light Wound for every 2 Success Points"* or *"gain +1 Protection for every 3 Success Points"*).
* **Standard Die Steps:** Upgrade and Downgrade effects must strictly adhere to core die stepping (`d8` ↔ `d10` ↔ `d12`).

---

## 5. Unique Class Engines & Dynamic Resource Loops

Every class must be built around a distinct, dynamic mechanical engine that dictates its operational rhythm and tactical tension:

| Class | Resource Engine | Dynamic Gameplay Loop |
| :--- | :--- | :--- |
| **Conduit** | **Charges (0–3)** | Channel elemental energy via Amp abilities to gain Charges; vent all 3 Charges in massive, encounter-shifting Burst releases. |
| **Hazard** | **Pressure (0–3) & Volatile Die** | Modulate chamber pressure (`-2` to `+3`); higher pressure grants larger Volatile Dice (`d8` → `d10` → `d12`), but rolling an 8+ Hit triggers a self-damaging Rupture. |
| **Pilot** | **Battery Pool (10 max) & Avatar Stances** | Manage battery reserves; shift dynamically between Attached Mode (augmented personal stats) and Detached Mode (autonomous avatar proxy). |
| **Vanguard** | **Form Stances & Boost Dice** | Stance-dance between Shield, Glider, and Cannon; bank 8+ Hits as Boost dice to fuel momentum and explosive form transitions. |
| **Weaver** | **Reserve Pool (4 max) & Nanite Forms** | Allocate liters of physical nanites into persistent equipment/modifications or cycle them through temporary offensive/defensive commands. |

When designing or revising a class engine:
* Establish clear minimums, maximums, and recharge triggers (e.g., round start, downtime, or hit sacrifice).
* Provide a visible risk-vs-reward tension or resource pacing cycle.
* Define clear fallback states when resources are fully depleted.

---

## 6. Action Economy Standardization & Ability Tags

To eliminate table ambiguity and cleanly mesh with Corsair's **3 Action Point (AP)** economy, all class powers must be designated **Class Abilities** (never "Class Skills") and explicitly declare their action trigger tag:

* **`[Action]`**: Costs **1 AP** and requires rolling a test (Simple, Complex, or Success Test).
* **`[Rider]`**: Costs **0 additional AP**; modifies, enhances, or triggers during an existing action (such as a standard firearm attack, melee strike, or movement action).
* **`[Reaction]`**: Triggered in response to an external event (e.g., contesting an incoming attack or reacting when an enemy enters your space). Specifies whether it costs 1 AP or is free.
* **`[Free Action]`**: Instant tactical adjustment performed on your turn that requires no test and costs 0 AP.

Every ability entry must format its activation line clearly:
> **Ability Name `[Tag]`**
> * **Resource Cost:** (e.g., `+1 Pressure`, `2 Batteries`, `1 Reserve`, or `Requires 3 Charges`)
> * **Effect:** Clean, rules-precise mechanical description.

---

## 7. Ability Taxonomy & Packaging

To prevent skill bloat and maintain manageable decision-making, Class Abilities are organized into thematic packages:

* **Packaging Typologies:** Packages are tailored to the thematic identity of the chassis:
  * **Kits** (e.g., Hazard's Medic Kit, Pyro Kit — 3 abilities per kit).
  * **Modules** (e.g., Pilot's Warden Module, Arsenal Module — 3 abilities per module).
  * **Weaves** (e.g., Weaver's HardWeave, LifeWeave — 3 tripartite aspects: Create, Modify, Control).
  * **Form Triads** (e.g., Vanguard's grouped Shield, Glider, and Cannon abilities).
  * **Amp & Burst Pairs** (e.g., Conduit's paired charge-builder and charge-spender abilities).
* **Progression Pacing:** Every class awards new ability packages at a standardized cadence:
  * **Level 1:** Starting package (+ baseline module/touch abilities).
  * **Level 2:** +1 Package.
  * **Level 3:** +1 Package.
  * **Level 4:** +1 Package.

---

## 8. Class Mods Architecture

Class Mods represent hardware overclocks, precision calibrations, and firmware alterations to the operative's chassis.

* **Fixed Pool Size:** Exactly **5 distinct Class Mods** are designed for each class.
* **Universal Pricing:** Each Class Mod costs **25,000 Credits**.
* **Socket Slots:**
  * **Slot 1:** Unlocked at **Level 2**.
  * **Slot 2:** Unlocked at **Level 4**.
  * An operative can install a maximum of **2 Class Mods** at a time per chassis.
* **Downtime Swapping:** Operatives may swap installed mods among those they own during day-to-day pacing.
* **Design Philosophy (Lateral Rule-Bending):** Mods should **not** provide boring numerical stat bumps (`+1 Attribute`). Instead, they must offer playstyle-defining lateral changes that bend the class engine's hard rules, such as:
  * Expanding resource capacity or multi-resource banking (e.g., holding two elements/boosts).
  * Altering delivery mechanisms (e.g., delivering touch/melee abilities at ranged distances).
  * Establishing safety valves (e.g., dampening self-damage on rupture).
  * Granting alternative resource-generation vectors (e.g., recharging reserves by sacrificing test Hits).

---

## 9. Standardized Class Progression Table

All classes follow a strictly standardized credit-funded upgrade progression from Level 1 to Level 5:

| Level | Benefits Unlocked | Credit Cost |
| :---: | :--- | :---: |
| **Level 1** | Base Chassis, 7 Attribute Points (base 1/1/1, cap 5), Starting Package, Class Engine | **100,000 Credits\*** |
| **Level 2** | +1 Attribute Point, +1 Class Mod Slot (Slot 1), +1 Ability Package | **20,000 Credits** |
| **Level 3** | +1 Attribute Point, Max Attribute Cap becomes 6, +1 Ability Package | **40,000 Credits** |
| **Level 4** | +1 Attribute Point, +1 Class Mod Slot (Slot 2), +1 Ability Package | **75,000 Credits** |
| **Level 5** | +1 Attribute Point, Max Attribute Cap becomes 7 | **150,000 Credits** |

*\*The 100,000 Credit cost for Level 1 applies only when purchasing an additional class chassis after character creation; an operative's starting class is free.*

---

## 10. Narrative Density & Hard Sci-Fi Guidelines

Class documents must strike a balance between evocative sci-fi atmosphere and scannable technical precision, calibrated to a 10th–12th grade reading level:

### Section-by-Section Density Standards
1. **Class Overview (`## Description`):** Exactly **2 to 3 well-developed paragraphs**:
   * *Paragraph 1 (Visual Silhouette & Hardware):* Describe the physical appearance, visible implants, ports, tubing, plating, or material manifestations on the operative's body.
   * *Paragraph 2 (Technical Mechanism & Combat Reality):* Explain how the technology functions internally under hard sci-fi principles and how it feels on the battlefield.
   * *Paragraph 3 (Tactical Flexibility & Cell Role):* Highlight the modular versatility of the chassis in cooperative team operations.
2. **Attributes (`## Attributes`):** Exactly **1 concise, evocative sentence** per attribute defining both its physical/in-universe nature and mechanical domain.
3. **Basic Mechanics (`## Basic Mechanics`):** Explain the unique resource engine in grounded technological terms (e.g., capacitor discharge, hydraulic pressure lines, servo draws, nanite fluid volume) before stating the exact rules.
4. **Class Abilities (`## Class Abilities`):** Exactly **1 short sentence of flavor description** introducing the technique, followed immediately by clean mechanical bullet points.
5. **Class Mods (`## Class Mods`):** 1 brief in-universe technical summary explaining what physical component or firmware is being modified, followed by the exact rule modification.

### Strict Hard Sci-Fi Constraints
In alignment with [`corsair-writing-style`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-writing-style/SKILL.md):
* **No Science Fantasy / Psionics:** Do not use terms like "magic", "spells", "mana", "auras", or "psychic powers".
* **No Soft Sci-Fi Force Fields or Pure Energy Weapons:** Defensive shields are kinetic dispersion barriers, physical deployables, reactive hydro-gels, or magnetic deflector mesh. Offensive energy is grounded in high-voltage static discharge, thermal ignition, cryogenic fluid cooling, or kinetic acceleration.
* **Biotechnology & Hardware Grounding:** Frame all effects in plausible engineering: micro-servos, subdermal conduits, capacitor cells, pneumatic solenoids, pressurized canisters, and neuro-synaptic interfaces.

---

## 11. Accompanying Printable Sheets & Document Architecture

Every class rulebook file must maintain strict parity with its corresponding printable A4 HTML sheet:

* **Markdown Document Path:** `rulebook/classes/[ClassName].md`
* **Printable Sheet Path:** `rulebook/classes/[ClassName]_Sheet.html`
* **Single-Page A4 Guarantee:** Every class sheet must strictly adhere to [`corsair-printable-sheets`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-printable-sheets/SKILL.md), utilizing Barlow typography, tokenized CSS variables, print media queries, and dense multi-column card layouts guaranteed to fit entirely on a single printed A4 page without spilling onto a second page.
