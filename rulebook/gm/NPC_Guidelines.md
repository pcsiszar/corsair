# NPC Guidelines

Designing and running non-player characters (NPCs) in Corsair should be efficient for the Game Master while remaining
tactically engaging for the players. These guidelines provide a framework for creating enemies that range from
disposable grunts to formidable bosses.

## NPC Philosophy: Simplicity and Scale

To keep the game moving, NPCs are built with less granularity than Player Characters. The goal is to allow the GM to
handle dozens of enemies without getting bogged down in individual stat blocks.

### 1. Grunts and Minions

Most "cannon fodder"—corporate guards, street thugs, or basic alien drones—use **Uniform Attributes**. The GM can quickly assemble these using the **Tier** baselines. Unique mechanical traits for more complex enemies are defined as **Properties**.

* **Physical Attribute:** A single value used for all Strength, Agility, and Finesse tests.
* **Mental Attribute:** A single value used for all Knowledge, Presence, and Instinct tests.
* **Health (HP):** Unlike players, most NPCs use a flat Health value instead of multiple Condition Tracks. When HP
  reaches 0, the NPC is defeated or incapacitated.

### 2. Squads and Mobs (Mass Action)

When NPCs outnumber players, they should act in **Squads**. A squad should typically be around the same size as the
**Corsair Cell** (the player group) to keep the action economy balanced and the turn order clean.

* **Movement:** A squad moves as a single unit on the same initiative/turn.
* **Teamwork:** Squad members prioritize the **Teamwork** action. Instead of 4-5 guards making individual attacks, have one leader make the attack while the others "sacrifice" their Action Points to provide **Upgrades** to the leader. Some elite units have properties that further enhance this (e.g., **Squad Tactics**).
* **Outnumbering:** Use the **Outnumbering** rules from Chapter 8 to give squads a natural advantage in melee without
  needing complex math.

### 3. Categories: Standard, Elite, and Boss

The enemy's role determines their resilience and action economy, regardless of their Tier.

* **Standard:** The baseline for most enemies. 3 AP, flat HP.
* **Elite:** Toughened specialists. 3 AP, higher flat HP, and usually better protection.
* **Boss:** Faction leaders or major threats. 4-6 AP, massive flat HP. Bosses can spend AP to act outside their turn.

---

## NPC Tiers

Tiers represent the raw power and quality of training/equipment of an NPC. Use the table below to set baseline stats,
then apply the **Category** modifiers.

### Baseline Stats by Tier

| Tier  | Phys | Ment | Move | DMG Bonus | Protection | Hit Points |
|:------|:-----|:-----|:-----|:----------|:-----------|:-----------|
| **1** | 2    | 2    | 4m   | +0        | 0          | 9          |
| **2** | 3    | 3    | 4m   | +1        | 1          | 12         |
| **3** | 5    | 5    | 4m   | +2        | 3          | 15         |
| **4** | 6+   | 6+   | 4m   | +3        | 5          | 18         |

* **Accuracy:** By default, NPC weapon Accuracy is equal to their **Physical** attribute.
* **Accuracy Array:** For ranged combat, the GM should assign accuracy values for **Short**, **Medium**, **Long**, and **Extreme** ranges based on the NPC's role and equipment.
* **Movement:** The base distance an NPC can move with a single Action Point. The standard for all Tiers is **4m**. Exceptional cases (e.g., predatory wildlife, high-tech drones) may deviate from this baseline.
* **Damage Bonus:** Added to the final result of successful attacks.
* **Protection:** Reduces incoming damage.

### NPC Properties

Rather than generic tactics, unique NPC behaviors should be codified as **Properties**. These are passive or active abilities that define how the NPC interacts with the environment and the Corsairs. 

* **Standard Properties:** Most NPCs have 0-1 properties.
* **Elite/Boss Properties:** May have 2+ properties.
* **Cost:** Significant properties might increase the NPC's point cost (refer to the Tier/Category table for guidance).

### Category Modifiers (HP, AP, & Protection)

Apply these to the Tier baselines to finalize the NPC.

| Category     | Health (HP)     | Action Points (AP) | Protection |
|:-------------|:----------------|:-------------------|:-----------|
| **Standard** | 6 + (Tier x 3)  | 3 AP               | +0         |
| **Elite**    | 12 + (Tier x 4) | 3 AP               | +1         |
| **Boss**     | 20 + (Tier x 8) | 4-6 AP             | +2         |

* **Standard Range:** 9 HP (Tier 1) to 18 HP (Tier 4).
* **Elite Range:** 16 HP (Tier 1) to 28 HP (Tier 4).
* **Boss Range:** 28 HP (Tier 1) to 52 HP (Tier 4).

*Example: A **Tier 2 Elite** has Phys 3, Ment 3, 20 HP, 3 AP, and 2 Protection (1 Baseline + 1 Category).*

---

## Encounter Building (The Point System)

To balance an encounter, Game Masters use a **Point Budget** based on the number of players and the desired difficulty.
You "spend" this budget on NPCs by their Tier and Category.

### 1. NPC Costs

Every NPC has a base cost determined by their Tier. You then pay an additional cost if they are an **Elite** or a **Boss
**.

| Tier  | Base Cost (Standard) | Elite Upgrade | Boss Upgrade |
|:------|:---------------------|:--------------|:-------------|
| **1** | 1 Point              | +2 Points     | +6 Points    |
| **2** | 2 Points             | +2 Points     | +6 Points    |
| **3** | 4 Points             | +2 Points     | +6 Points    |
| **4** | 6 Points             | +2 Points     | +6 Points    |

* **Squad Cost:** Since a squad is typically the same size as the Corsair Cell (4 players), a **Tier 1 Standard Squad**
  costs 4 Points, while a **Tier 2 Standard Squad** costs 8 Points.

### 2. Encounter Budget

Calculate the total budget by multiplying the **Difficulty Value** by the number of players in the Corsair Cell.

| Difficulty   | Points per Player | Total Budget (4 Players) |
|:-------------|:------------------|:-------------------------|
| **Easy**     | 2 Points          | 8 Points                 |
| **Moderate** | 4 Points          | 16 Points                |
| **Hard**     | 6 Points          | 24 Points                |
| **Perilous** | 8+ Points         | 32+ Points               |

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
is charging its railgun" or a "Siren is gathering psionic energy" gives players a vital turn to dive for cover or use a
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
