# Corsair Development Roadmap & TODOs

This document tracks upcoming design tasks, mechanical balances, lore expansions, and chapter overhauls across the *Corsair* rulebook and GM toolkit.

---

## 1. Class Gear Lore & Origins: MANTLEs [COMPLETED]
* **Summary:** Codified the full origin, lore, neuro-cybernetics, and 518 AA reality of **MANTLEs** (*Modular Adaptive Neural Transmission Linked Equipment*) and the permanent **Neural Control Chip (NCC)** across the rulebook, class manuals, character creation, and core skills.
  * **Origins & Discovery:** Developed during the Scavenger Incursions (315–320 AA) by Chief Fleet-Engineer Kira Abe and Commander Velen Redmane at the Port Zenith Orbital Engineering Yards, reverse-engineering inert Precursor Vault neural conduits into a closed-loop combat harness to counter Scav bio-reaction speeds. Evolved over two centuries incorporating dragon biology research, vault technologies, and iterative military engineering.
  * **Neuro-Cybernetics & Invariants:** Operatives undergo surgical installation of a permanent cranial/spinal Neural Control Chip (NCC) and shunt. Established the hard sci-fi **Synaptic Bandwidth Saturation** rule: an operative's nervous system can only sustain one active telemetry mapping at a time without risking catastrophic **Synaptic Burnout**, mechanically enforcing the single active chassis limit. Swapping chassis costs 100,000 Credits during downtime for hardware, licensing/jailbreaks, and neuro-pod recalibration.
  * **518 AA Distribution & The Freelancer Network:** Classified as Tier-1 Restricted Military Hardware by the Flotilla. Commissioned Corsairs have frames underwritten by official sponsors; uncommissioned Freelancers acquire starting rigs via Sponsor Candidate training pipelines, veteran hand-me-downs from the underground **Freelancer Network**, or refurbished battlefield salvage.
  * **Bespoke Frames:** Standardized NCC bus, but five fully bespoke full-body frames (Conduit, Hazard, Pilot, Vanguard, Weaver).
* **Updated Files:**
  * [rulebook/classes/Classes.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/classes/Classes.md) *(New Master Chapter)*
  * [rulebook/classes/Conduit.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/classes/Conduit.md)
  * [rulebook/classes/Hazard.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/classes/Hazard.md)
  * [rulebook/classes/Pilot.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/classes/Pilot.md)
  * [rulebook/classes/Vanguard.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/classes/Vanguard.md)
  * [rulebook/classes/Weaver.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/classes/Weaver.md)
  * [rulebook/Rulebook.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/Rulebook.md)
  * [rulebook/character/Creation.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Creation.md)
  * [rulebook/character/Player_Characters.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Player_Characters.md)
  * [.agents/skills/corsair-class-design/SKILL.md](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-class-design/SKILL.md)
  * [.agents/skills/corsair-core-lore/SKILL.md](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-core-lore/SKILL.md)

---

## 2. Feats / Traits System Rework: Removing Unlock Requirements [COMPLETED]
* **Summary:** Streamlined the Trait progression model. Removed all unlock requirements, challenge gates, and prerequisite trees. Traits are now categorized into operational areas and purchased directly with flat XP (costs 2–8 XP) during character creation or downtime training.
* **Character Creation XP Integration:** Replaced isolated "Skill Points" with flat Experience Points (6 XP baseline; +4 XP for Humans [10 total], +2 XP for Human-mixed races [8 total]). Starting XP can be spent freely on Skills (2 XP per level) or Traits.
* **Updated Files:**
  * [rulebook/character/Traits.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Traits.md)
  * [rulebook/character/Creation.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Creation.md)
  * [rulebook/character/Advancement.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Advancement.md)
  * [rulebook/character/Player_Characters.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Player_Characters.md)
  * [rulebook/character/Character_Sheet.html](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/character/Character_Sheet.html)

---

## 3. GM Guide: Stealth & Infiltration [COMPLETED]
* **Summary:** Codified a comprehensive Game Master reference chapter detailing stealth mechanics, disguises, security architecture, sensory downgrade networks, and tiered alarm states across the core rules.
  * **Hiding & Sneaking:** In Moment-to-Moment pacing, sneaking is a Complex Test costing 1 AP. The Action Roll (8+) ensures silent/concealed movement (failure wastes 1 AP and flips the nearest sentry to Alerted as an Activating Actor). The Success Roll determines distance moved: half speed costs 2 SP/meter, while full speed costs 1 SP/meter and incurs 2 Downgrades. Excess Hits can be banked into Blocker Effects or Downgrade Effects (lost upon moving away, but unused Upgrade/Downgrade dice carry forward). Group infiltration uses standard Teamwork with dice swapping.
  * **Disguises & Social Camouflage:** Pre-crafted via preparation Simple Tests (Knowledge + Finesse) where every 2 Hits buys 1 Sustained Blocker (following the core rule that Blockers cost 2 Hits, not derived from Success Points). Sustained Blockers do not degrade from repeated scrutiny; an inspector must score strictly more Hits than the rating in a single check to pierce it. Established the hard sci-fi invariant: MANTLE frames cannot be disguised and must be smuggled in separately. Smuggled gear imposes Downgrades equal to Load (Load 1/2 = 0 Downgrades). Authentic badges add +1 free Blocker. Piercing a disguise activates the inspector as an Active Actor, triggering high-tension Social Interrogations governed by Patience clocks.
  * **Security Measures:** Passive security (locks, encryptions, blast doors) uses a Lockdown rating (functioning like Determination). Active security (traps, tripwires, turrets) function as Activating Actors on triggers. Sensory equipment (optical, thermal, acoustic) imposes stacking Downgrades on stealth tests; direct physical tampering avoids room-wide stacked Downgrades.
  * **Sentries & Facility Alerts:** Sentries spend 1 AP on their turn to roll an alarm Success Test (Presence + Instinct for radio/shout; Finesse + Agility for wall panels), which can be reactively contested by players in position. Un-negated hits advance the Three Facility States: **Unaware** (guards idle and pass turns), **Alert** (guards know intruders are present, actively search every GM turn), and **Lockdown** (intruder location known, reinforcement waves deploy at the End of every Round until eliminated or the cell breaks visual tracking and re-establishes stealth).
* **Updated Files:**
  * [rulebook/gm/Stealth_and_Infiltration.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/gm/Stealth_and_Infiltration.md) *(New Chapter)*
  * [rulebook/gm/Running_the_Game.md](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/gm/Running_the_Game.md)

