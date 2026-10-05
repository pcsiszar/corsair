# NPC Guidelines

Designing and running non-player characters (NPCs) in Corsair should be efficient for the Game Master while remaining
tactically engaging for the players. These guidelines provide a framework for creating enemies that range from
disposable grunts to formidable bosses. For a complete catalog of ready-to-run stat blocks utilizing this framework, see the [Bestiary](Bestiary.md).

## NPC Philosophy: Simplicity and Scale

To keep the game moving, NPCs are built with less granularity than Player Characters. The goal is to allow the GM to
handle dozens of enemies without getting bogged down in individual stat blocks.

### 1. Grunts and Minions

Most "cannon fodder"—corporate guards, street thugs, or basic alien drones—use **Uniform Attributes**. The GM can quickly assemble these using the **Tier** baselines. Unique mechanical traits for more complex enemies are defined as **Properties**.

* **Physical Attribute:** A single value used for all Strength, Agility, and Finesse tests.
* **Mental Attribute:** A single value used for all Knowledge, Presence, and Instinct tests.
* **Health (HP):** Unlike players, most NPCs use a flat Health value instead of multiple Condition Tracks. When HP
  reaches 0, the NPC is defeated or incapacitated.
* **Customizing Attributes:** While uniform attributes are ideal for fast GM bookkeeping, you can freely break away from uniform arrays whenever a character concept, enemy archetype, or tactical role demands it. For example, a nimble scout or sniper might have Agility 5 and Strength 2 instead of a uniform Physical 4, or an interrogator might possess Presence 5 and Knowledge 2. Customize individual attributes as needed while using the Tier baselines as your benchmark.

### 2. Squads and Mobs (Mass Action)

When NPCs outnumber players, they operate in **Squads**. Rather than relying on bespoke mob stat blocks or complex tracking, a squad is simply **a group of up to 4 enemies who occupy the same space and act exclusively through standard [Teamwork](../core/Teamwork.md)**.

* **Occupancy & Scale:** A squad consists of **2 to 4 members** sharing a single 4m space (matching the maximum capacity of a standard grid space). Members retain their individual flat HP (e.g., 9 HP for Tier 1).
* **Squad Firing (Coordinated Volley):** All active members in the space spend **1 AP** to fire at the same target. They roll their combined pools simultaneously (e.g., 4 grunts with Phys 2 roll $4 \times 2 = 8\text{ dice total}$) and swap dice between their pools under standard Teamwork rules to distribute Hits (`8+`). The target player may spend 1 AP to make an Evasion Contest (benefiting from **Defender's Advantage** to eliminate high dice). Each surviving attacker with an `8+` makes an individual Success Roll for damage.
* **Squad Movement (Coordinated Advance):** All active members spend **1 AP** to move. Each makes a Movement Success Test (*Agility/Phys*), and they swap dice. Under the universal Teamwork movement rule, **the entire squad moves as far as the furthest member could move**.
* **The Turn Pacing Trigger:** Because spending 1 AP per member on a coordinated squad action totals 4 AP (exceeding the active side's **2 AP per turn limit**), **executing a squad action immediately concludes the GM's turn and passes control back to the players!** The GM never takes an endless sequence of individual actions.
* **Casualties & Counter-Play:** When players attack the squad, damage reduces individual members. Players rolling excess Hits on their Action Roll can activate the **Chain Effect** to mow down multiple squad members in the same space in a single attack. As members fall, the squad's dice pool naturally shrinks (4 members = 8 dice, 3 members = 6 dice, 2 members = 4 dice).
* **Morale & Disband:** When a squad is reduced to **1 surviving member**, the squad disbands. The lone survivor loses coordinated Teamwork benefits and either retreats, dives for heavy cover, or surrenders.
* **Squad Movement & Tactical Pacing:** To keep combat fluid and prevent hordes from functioning as static gun turrets, squads should typically spend **1 AP on Squad Advance** (maneuvering or taking cover) and **1–2 AP on firing** per round. This models authentic squad movement-to-contact and creates natural dynamic firefights.

### 3. Categories: Standard, Elite, and Boss

The enemy's role determines their resilience and action economy, regardless of their Tier.

* **Standard:** The baseline for most enemies. 3 AP, flat HP.
* **Elite:** Toughened specialists, field lieutenants, and champions. 3 AP, higher flat HP, and reinforced protection.
* **Boss:** Faction leaders, heavily armored mechs, or apex alien monstrosities. Solitary bosses face the entire player group's combined action economy (12+ AP). To prevent a Boss from being neutralized by focus fire, they possess two mechanical advantages:
  * **Action Economy (6 AP Baseline):** Standard Bosses start each round with **6 AP** (Apex Tier 4 Bosses receive **7–8 AP**), providing enough stamina to engage across multiple turn cycles.
  * **Legendary Reactions (Free Contests):** A Boss gains **2 Free Reactions per round** used exclusively for **Contest Rolls** (Evasion or Parries). These allow the Boss to defend against concentrated player fire without depleting their offensive Action Point pool.

---

## NPC Tiers

Tiers represent the raw power, training, and equipment quality of an NPC. Use the table below to set baseline stats, then apply the **Category** modifiers.

### Baseline Stats by Tier

| Tier  | Phys | Ment | Move | DMG Bonus | Protection | Hit Points |
|:------|:-----|:-----|:-----|:----------|:-----------|:-----------|
| **1** | 2    | 2    | 4m   | +0        | 0          | 9          |
| **2** | 3    | 3    | 4m   | +1        | 1          | 12         |
| **3** | 4    | 4    | 4m   | +2        | 2          | 15         |
| **4** | 5    | 5    | 4m   | +3        | 4          | 18         |

* **Accuracy:** By default, NPC weapon Accuracy is equal to their **Physical** attribute.
* **Accuracy Array:** For ranged combat, the GM should assign accuracy values for **Short**, **Medium**, **Long**, and **Extreme** ranges based on the NPC's role and equipment.
* **Movement:** The base distance an NPC can move with a single Action Point. The standard for all Tiers is **4m**. Exceptional cases (e.g., predatory wildlife, high-speed skimmers) may deviate from this baseline.
* **Damage Bonus:** Added to the final result of successful attacks.
* **Protection:** Reduces incoming damage. **Protection Ceiling:** Personal armor for humanoid NPCs is capped at **4** (representing military ceramic strike plates or heavy ballistic carapace). Protection ratings of **5 or higher** are reserved strictly for mechanized walkers, armored vehicles, fortified gun emplacements, or massive armored alien fauna, which require anti-materiel weapons or heavy demolition ordnance to penetrate.

### NPC Properties

Rather than generic tactics, unique NPC behaviors should be codified as **Properties**. These are passive or active abilities that define how the NPC interacts with the environment and the Corsairs. 

* **Standard Properties:** Most NPCs have 0-1 properties.
* **Elite/Boss Properties:** May have 2+ properties.
* **Cost:** Significant properties might increase the NPC's point cost (refer to the Tier/Category table for guidance).

### Category Modifiers (HP, AP, & Protection)

Apply these to the Tier baselines to finalize the NPC.

| Category     | Health (HP)     | Action Points (AP)              | Protection |
|:-------------|:----------------|:--------------------------------|:-----------|
| **Standard** | 6 + (Tier x 3)  | 3 AP                            | +0         |
| **Elite**    | 12 + (Tier x 4) | 3 AP                            | +1 (Max 4 for infantry) |
| **Boss**     | 20 + (Tier x 8) | 6 AP (7-8 AP for Apex Tier 4)   | +1 (Max 5 for personal gear) |

* **Standard Range:** 9 HP (Tier 1) to 18 HP (Tier 4).
* **Elite Range:** 16 HP (Tier 1) to 28 HP (Tier 4).
* **Boss Range:** 28 HP (Tier 1) to 52 HP (Tier 4).

*Example: A **Tier 2 Elite** has Phys 3, Ment 3, 20 HP, 3 AP, and 2 Protection (1 Baseline + 1 Category).*

---

## Encounter Building (The Point System)

To balance an encounter, Game Masters use a **Point Budget** based on the number of players and the desired difficulty. You "spend" this budget on NPCs by their Tier and Category.

### 1. NPC Costs

Every NPC has a base cost determined by their Tier. You then pay an additional cost if they are an **Elite** or a **Boss**.

| Tier  | Base Cost (Standard) | Elite Upgrade | Boss Upgrade |
|:------|:---------------------|:--------------|:-------------|
| **1** | 1 Point              | +2 Points     | +4 Points    |
| **2** | 2 Points             | +2 Points     | +6 Points    |
| **3** | 4 Points             | +2 Points     | +6 Points    |
| **4** | 6 Points             | +2 Points     | +6 Points    |

* **Squad Costs:** 
  * A **Tier 1 Standard Squad** (4 grunts) costs **4 Points**.
  * A **Tier 2 Fireteam** (2 guards) costs **4 Points**, while a full **Tier 2 Squad** (4 guards) costs **8 Points**.
  * A **Tier 3 Veteran Pair** (2 operatives) costs **8 Points**.

### 2. Encounter Budget

Calculate the total budget by multiplying the **Difficulty Value** by the number of players in the Corsair Cell. Each step up in difficulty provides enough additional points to add one tactical squad, fireteam, or specialist operative to the field.

| Difficulty   | Points per Player | Total Budget (4 Players) | Expected Experience |
|:-------------|:------------------|:-------------------------|:--------------------|
| **Easy**     | 2 Points          | 8 Points                 | Low risk, routine patrol or light skirmish. |
| **Moderate** | 3 Points          | 12 Points                | Balanced challenge; 1 PC likely wounded or dropped. |
| **Hard**     | 4 Points          | 16 Points                | High lethality; requires cover, focus fire, and tactical coordination. |
| **Perilous** | 5+ Points         | 20+ Points               | Desperate survival; high risk of casualties without objectives or retreat. |

---

## Running Encounters

Once the math is settled, consider the narrative and tactical context of the fight.

### 1. Objective-Based Combat

Combat is more engaging when the goal is not just "clear the room." Players might be trying to activate a terminal,
escape with data, or hold a position until a ship arrives. The combat ends when the objective is met, regardless of how
many enemies remain. This encourages players to focus on movement and utility rather than just raw damage.

### 2. Reinforcements and Waves

Instead of placing all enemies on the map at once, have them enter in waves. Every round, new units can arrive from
elevators, airlocks, or drop pods. This keeps the tactical situation fluid and forces players to adapt to new threats
from unexpected angles.

### 3. Escalation & De-escalation

If an encounter feels too trivial, call in reinforcements. If it's too perilous, have the enemies pivot to a non-lethal
objective, like capturing a player or securing cargo. This allows the GM to modulate the challenge in real-time without
breaking the narrative.

### 4. Telegraphing Threats

For Bosses and powerful Elites, telegraph their most devastating moves one turn in advance. Describing how a "Heavy Mech
is charging its railgun" or a "combat drone is spooling its capacitor coils" gives players a vital turn to dive for cover or use a
defensive ability. This makes high-damage attacks feel like a tactical challenge rather than a random punishment.

### 5. Environmental Interaction

The battlefield should be more than just a grid. Use explosive canisters, venting steam pipes, or unstable platforms to
change the environment. Allow players (and NPCs) to interact with these—shooting a steam pipe to create a smoke screen
or hacking a bridge to trap an enemy.

### 6. Morale and Surrender

NPCs are people (or at least sentient entities) with their own survival instincts. Professional mercenaries might
surrender if their leader falls, and corporate security might retreat to call for backup if they take heavy casualties.
Offering a chance for enemies to surrender or flee can lead to interesting social scenes and moral dilemmas for the
Corsair Cell.
