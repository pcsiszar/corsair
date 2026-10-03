---
name: corsair-exotic-equipment-design
description: >-
  Design guidelines, balancing invariants, hard sci-fi constraints, 4-tier rarity ladder, and catalog organization for authoring Exotic Hardware (D&D-style high-tier 'magic items') in Corsair.
---

# Corsair Exotic Hardware Design System

This skill documents the design principles, mathematical invariants, physical grounding constraints, economic tiering, and structural rules for authoring **Exotic Hardware** in *Corsair*.

Exotic Hardware serves as the *Corsair* equivalent of D&D's Magic Items, Wondrous Items, and Artifacts. It exists to provide exciting, creative, game-altering gear options with distinctive mechanics for mid-to-late campaign play, while being explicitly segregated from basic equipment to keep character creation and early-game choices approachable for novice players.

---

## 1. Core Philosophy: The D&D Parallel in Hard Sci-Fi

In traditional fantasy RPGs, magic items break the baseline laws of reality—granting teleportation, invisibility, or elemental bursts. In *Corsair*, the setting adheres strictly to **hard science fiction**:
* **No Space Magic:** There are no enchantments, psionics, or arcane energies.
* **No Hand-Waving Buzzwords:** Never throw around empty jargon like *"phase-emitter"*, *"tachyon field"*, or *"quantum resonance matrix"*.
* **Tangible Grounded Mechanisms:** Every exotic piece of hardware must explicitly explain **what it physically is**, **what it mechanically does**, and **how it actually operates** using grounded physics, thermodynamics, or the established Layer-3 cosmic truth of the setting (non-baryonic dark matter catalytic transducers created by the Precursor Singularity).

---

## 2. Hard Sci-Fi Grounding Principles

When authoring any piece of Exotic Hardware, anchor its description in real-world or setting-established physical principles:

1. **Thermodynamics & Heat Management:** High-energy devices generate massive waste heat. Active systems rely on pressurized cryo-coolant canisters, endothermic chemical sinks, or directional thermoelectric radiators.
2. **Kinetic & Material Science:** Armor and melee weapons utilize shear-thickening non-Newtonian fluids, piezoelectric shock transducers, ultrasonic harmonic motors, or carbon-nanotube monofilaments.
3. **Optics & Electromagnetic Spectrum:** Invisibility is achieved through active electrochromic metamaterial weaves, photonic refraction arrays, or directional microwave scattering.
4. **Precursor Technology (Solid-State Dark Matter Transduction):** As canonized in Layer 3 lore, the Precursors mastered the reversible conversion of dark matter into direct energy ($E \leftrightarrow m_{dm}$). The Sphere's halo provides a diffuse dark matter bath. Precursor relics do not generate energy from nothing—they are solid-state lattices that catalyze ambient dark matter into electricity, localized gravitational shearing, or inertial dampening.

---

## 3. Balancing Invariants: Load, AP & Round-Based Cooldowns

Unlike D&D, which relies on a flat "3 Attunement Slots" rule, *Corsair* balances Exotic Hardware through **Load Encumbrance**, **Action Economy**, and **Round-Based Cooldown Pacing**:

1. **Load Taxation Over Arbitrary Caps:**
   * Exotic Hardware carries substantial Load (typically **Load 2 to Load 5** for weapons and rigs; **Load 3 to Load 6** for heavy carapaces).
   * Because an operative's maximum carrying capacity is strictly capped at **$12 + (\text{Strength} \times 2)$**, equipping multiple exotic systems forces meaningful tactical tradeoffs—sacrificing extra ammo rigs, heavy sidearms, or auxiliary toolkits.
2. **Action Point (AP) Economy:**
   * Activating an active exotic function costs **1 AP** (or acts as an enhancement to an existing 1-AP test).
   * Passive systems provide situational bonuses (Upgrades, flat Protection, or specialized contest pools) that activate conditionally rather than granting unconditional power spikes.
3. **Pacing Cooldowns Across Round Scales:**
   * Bleeding-edge prototypes push capacitors and cooling loops to their limits. Cooldowns are calibrated to *Corsair's* three narrative round tiers:
     * **1 Moment-to-Moment Round (~5–10 seconds):** Recharges at the start of the operative's next combat turn. Used for micro-capacitor discharges and reaction pulses (e.g., pulsed electromagnetic deflector coils).
     * **1 Place-to-Place Round (~1 hour):** Recharges after completing the current tactical breach or short transit, allowing thermal loops to flush and coolant reservoirs to settle (e.g., thermal flash-vent carapaces, harmonic disruption heads, neuro-chemical stim shunts).
     * **1 Day-to-Day Round (24 hours):** Recharges after a full downtime cycle and complete shipboard overhaul (e.g., emergency gravitational rebirth warplate).
4. **Zero-Division Math & Flat Integer Bonuses:**
   * Adhere strictly to the Zero-Division Rule: never use formulas with division (no $\text{STR}/2$ or $\text{Knowledge}/3$).
   * Bonuses must be flat integers ($+1$, $+2$, $+3$) or direct Attribute references (e.g., *"equal to the lower attribute of the test"*).
   * Upgrades/Downgrades must respect the system hard cap of **6 net Upgrades or Downgrades**.
   * *Note: Keep mathematical design rules in this skill document; do not clutter the player-facing equipment book with authoring invariants.*
5. **Non-Customizable Architecture (No Upgrade Kits):**
   * Exotic weapons, protective carapaces, and systems **cannot accept standard mastercrafted Upgrade Kits** (no +1 Damage, no Weight Reduction, no aftermarket modular attachments).
   * Rationale: Exotic items already incorporate extreme, bespoke physics mechanics (e.g., armor-bypassing, cryo flash-freeze, continuous dark-matter arcs, or molecular severance). Allowing standard upgrade kits (+1 to +3 damage, -1 Load) would cause runaway mathematical inflation and break combat balance.
   * Their statistics, Damage Bonuses, and Load values are permanently fixed as written.

---

## 4. The 4-Tier Rarity & Economic Ladder

To ensure clear campaign pacing, Exotic Hardware is strictly tiered by rarity, cost, and availability:

| Tier | Classification | Typical Cost (Credits) | In-Universe Origin & Market Availability |
| :---: | :--- | :---: | :--- |
| **1** | **Mil-Spec Skunkworks** | $15,000 – 30,000 \text{ CR}$ | High-tier black-budget military modifications, experimental field-trial hardware from Flotilla foundries (Caldera Foundry, Port Zenith Engineering, Panthera Arms). Rare, but obtainable through high-end corporate fixers or Tier-1/Tier-2 contract payouts. |
| **2** | **Classified Prototypes** | $40,000 – 80,000 \text{ CR}$ | Bleeding-edge corporate skunkworks tech, hybrid reverse-engineered alien alloys, bespoke cybernetic/neural telemetry gear. Heavily guarded by corporate security; acquired via corporate espionage, black-site raids, or Tier-2/Tier-3 unsanctioned contracts. |
| **3** | **Precursor Relics** | $100,000 – 250,000 \text{ CR}$ | Intact alien artifacts, non-baryonic catalytic lattices, and self-repairing alloys recovered from deep Vault excavations or the Evergaol crash site. Strictly illegal contraband under the Covenant Accords; traded only in deep-underworld circles (the Jailers, Iron Fang, or Scav warlords). |
| **4** | **Singularities & Unique Wonders** | **Priceless** (Not for Sale) | Mythic, one-of-a-kind artifacts of campaign-defining significance (e.g., an intact dreadnought catalytic core, an uncorrupted Shard memory lattice, or an intact Precursor null-beam projector). Found exclusively as major campaign milestones or climactic salvage objectives. |

---

## 5. Catalog Organization: Ascending Price & Self-Contained Entries

To provide an intuitive browsing experience and prevent fragmentation:

1. **Ascending Order by Market Price:**
   * Present all Exotic Hardware in strict ascending order of cost, starting from consumable entry points (e.g., 3,500 Credits) up through classified prototypes (40,000–80,000 Credits) to priceless campaign wonders.
2. **Self-Contained Rules (No Extracted Property Glossaries):**
   * Unlike standard equipment catalogs that reference broad property glossaries at the bottom of the page, **each Exotic Hardware entry must contain its entire mechanical resolution, AP costs, test pairs, and cooldown rules directly inside its own stat block**.
   * Because exotic gear possesses bespoke, physics-altering capabilities, self-contained descriptions ensure players and GMs never have to cross-reference multiple appendices during high-stakes scenes.
3. **Master Catalog Index Table:**
   * Precede the detailed catalog entries with a scannable Master Catalog Table providing Item, Tier, Classification, Load, Cost, and a 1-sentence tactical summary.

---

## 6. Authoring Checklist for New Exotic Items

When creating a new piece of Exotic Hardware, ensure every entry satisfies the following:

- [ ] **Functional Name:** Clear, evocative archetype (e.g., *Disruption Maul* or *Arc Carbine*, not *"Model 42-X Hyper-Hammer"*).
- [ ] **Physical Explanation:** Explicitly describes the physical materials, power source, and working mechanism.
- [ ] **Rarity Tier & Price Placement:** Assigned to Tier 1, 2, 3, or 4 with corresponding credit valuation, positioned in proper ascending price order.
- [ ] **Load Encumbrance:** Appropriately heavy Load (typically 2 to 5, or 1/2 for single-use items) to enforce equipment tradeoffs.
- [ ] **Action Economy & Cooldown:** Clear AP cost, test pair (if rolling), and round-based cooldown (1 moment-to-moment, 1 place-to-place, or 1 day-to-day round).
- [ ] **Self-Contained Rules:** All mechanical triggers, bonuses, and effects are completely explained within the item entry.
- [ ] **Zero-Division Compliance:** Flat integer math only (+1, +2, etc.); no division formulas.
- [ ] **Tone Alignment:** Narrative flavor text emulating Terry Pratchett's dry wit and grounded *Expanse*/*Cowboy Bebop* realism.
