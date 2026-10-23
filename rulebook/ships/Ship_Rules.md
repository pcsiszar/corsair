# Ships and Space Combat

In the airless void of the Sphere, your ship is more than transportation—it is your life support, your operational sanctuary, and your most lethal instrument of survival. Space combat in *Corsair* is an unforgiving dance of orbital mechanics, Newtonian momentum, and physiological endurance. The setting obeys strict hard science fiction constraints: there is no artificial gravity, no faster-than-light transit, and no deflector shielding. Every maneuver burns precious reaction mass, every high-G vector turn crushes human ribs against acceleration couches, and every penetrating round strikes pressurized titanium-composite bulkheads directly.

Surviving these encounters requires a deep understanding of your ship’s core architecture and a crew that operates as a single, cohesive unit.

---

## Dual-Scale Engagement

Naval engagements unfold across two synchronized modes of tactical resolution. When closing distance across interplanetary trajectories or planetary orbits, combat is tracked on the **Macro-Grid**, where commanders manage vector commitments, long-range sensor locks, and relativistic railgun strikes across vast orbital distances. When hostile vessels close within knife-fighting range, the engagement shifts into **Dogfight Mode**, resolving micro-positioning on an abstract tactical scale from 1 to 10 as pilots fight tooth and nail for the optimal firing cone.

---

## The Macro-Grid & Vacuum Transit

On the Macro-Grid, tactical space is mapped using a hexagonal grid where each hex represents a **1-kilometer diameter spherical volume** of open void. Ships maneuver across this grid utilizing their Engine's **Acceleration** rating.

To move on the Macro-Grid, the ship's Pilot performs a **Success Test** using the vessel's **Acceleration**. The craft traverses **500 meters for every Success Point** scored, translating to exactly **one hex space for every 2 Success Points**, rounded down. An Acceleration roll yielding 5 Success Points allows a vessel to traverse 2 hex spaces (2,000 meters), while a roll of 8 Success Points propels the craft 4 hex spaces (4,000 meters) along its flight path.

### Newtonian Momentum & Vector Inertia

Because vacuum transit is governed by pure inertia, starships cannot halt on a dime or reverse course without expending massive counter-thrust. A ship is **strictly prohibited from moving back into a space it just vacated** during its current movement action.

To reverse vector or re-enter a hex it has recently departed, the vessel must first traverse through at least **two adjacent intervening spaces** on the grid, burning thrusters to bleed lateral momentum and swing its nose around. This requirement models realistic orbital mechanics and ensures that positioning, approach angles, and intercept corridors require deliberate tactical planning.

### G-Strain & Crew Physiology

While a ship's reinforced titanium keel can survive immense structural strain, the fragile organic crew strapped inside its bridge cannot. Sustained burns and violent evasive maneuvers exert crushing gravitational forces (G-forces) that pull blood away from cerebral tissues and crack ribs against flight harness mounts.

If a pilot spends **more than 6 Success Points** on movement in a single turn, the crew suffers **G-Strain**. For every additional Success Point spent beyond 6, every crew member on board immediately suffers:

* **1 Light Wound** from internal capillary tearing, blunt harness impact, and extreme hydrostatic blood pressure.
* **1 Light Stress** from tunnel vision, sensory deprivation, and physiological shock under sustained G-forces.

Damage sustained from G-Strain represents direct physiological trauma and is **completely unmitigated by personal Armor or ship Protection**. Spacers who push their engines beyond safe operating parameters risk blacking out or rupturing internal organs before ever entering firing range.

---

## Entering the Dogfight (The Dogfight Scale)

When two or more hostile vessels enter the **same 1 km hex space** on the Macro-Grid, macro-movement immediately suspends. The encounter transitions into **Dogfight Mode**, tracking close-range spatial orientation, relative closing angles, and weapon engagement cones on the micro-level **Dogfight Scale from 1 to 10**.

The Dogfight Scale is tracked independently for every pair of opposing vessels sharing the hex, always measured from the **players' perspective**:

```
[ 1 — 2 — 3 ] ---------> [ 4 — 5 — 6 — 7 ] ---------> [ 8 — 9 — 10 ]
 Disadvantage                  Neutral                    Advantage
(Enemy on your Tail)       (Passing Vectors)         (You are on their Tail)
```

### Relative Vector Geometry

Each zone of the Dogfight Scale models specific relative spatial orientations in three-dimensional vacuum:

* **Disadvantage (Positions 1–3):** The enemy is on your tail. Hostile craft match your evasive vector and train their forward spinal batteries or primary missile pods directly into your vulnerable main engine thrusters.
* **Neutral (Positions 4–7):** Passing vectors and broadside slashing runs. Vessels maneuver aggressively with cold-gas Reaction Control System (RCS) thrusters, exchanging snapshot autocannon bursts, flak screens, and turreted laser fire across crossing arcs.
* **Advantage (Positions 8–10):** You have gained the enemy's tail. You match their maneuvers while holding your forward weapon cones aligned with their unarmored engine bells, dictating range and denying them return fire from fixed forward mounts.

### Dogfight Maneuver Mechanics

On their turn, a Pilot can adjust spatial positioning by executing a **Combat Maneuver**. The Pilot makes a Complex Test combining the vessel's **Maneuverability + Instinct**:
1. **Action Roll:** Roll d10s equal to the higher Attribute. If at least one die shows 8+, the maneuver succeeds.
2. **Success Roll:** Take dice equal to the lower Attribute from the successful roll. The highest single die value among these is your **Success Points**.
3. **Scale Adjustment:** The craft climbs or drops **one position on the Dogfight Scale for every Success Point spent**.

If a pilot expends more than 6 Success Points on dogfight maneuvering within a single turn, the crew suffers **G-Strain** for each additional Success Point, exactly as with Macro-Grid movement.

* **The Interception Advantage:** The act of aggressively hunting and closing on a target grants immediate tactical momentum. A vessel that initiates combat by moving into an occupied hex enters the Dogfight Scale at **Position 6 (Attacker Edge)**. The vessel that was already occupying the hex begins at **Position 5 (Defender Neutral)**.
* **Breakaway Burns:** A ship trapped in a disadvantageous position cannot simply fly away. A Pilot must successfully shift the Dogfight Scale back to neutral territory (**Position 4 or higher**) before the ship is permitted to leave the dogfight hex and return to the Macro-Grid. The Pilot makes a Success Test using **Acceleration**, spending Success Points first to climb the scale back to neutral (Position 4+), and then using any remaining Success Points to traverse hexes on the Macro-Grid (500 meters per SP, or 1 hex per 2 SPs).
* **Contesting Breakaways:** When a hostile ship attempts to break away from your dogfight space, an opposing Pilot in the same hex can spend **1 AP** to contest the action by rolling a Simple Test with the ship's **Acceleration**. Each Hit (`8+`) rolled on the contest eliminates one of the highest dice from the fleeing pilot's Acceleration roll. If all `8+` dice are eliminated, the contest succeeds: the fleeing ship scores 0 Success Points and is stopped in its tracks, unable to shift its position or leave the dogfight hex this turn.
* **Contesting Maneuvers:** When an opposing ship attempts a Combat Maneuver to climb or drop positions on the Dogfight Scale, a Pilot in the same hex can spend **1 AP** to contest the action by rolling a Simple Test with the ship's **Maneuverability**. Each Hit (`8+`) rolled on the contest eliminates one of the highest dice from the active pilot's Action Roll. If all `8+` dice are eliminated, the Action Roll fails and the scale does not shift.

### Disengaging from Space Combat

To completely disengage and end space combat, a ship must establish a separation distance of at least **5 hexes (5 km)** from all hostile vessels on the Macro-Grid and successfully evade all active Target Locks. Once beyond 5 kilometers, the encounter concludes and normal orbital transit time resumes.

---

## Anatomy of a Starship

Every starship is defined by universal structural characteristics that determine how much punishment the hull can sustain, how it maneuvers through vacuum, and how it is outfitted for naval warfare.

```
+-------------------------------------------------------------------------------+
|                       PRIMARY HULL INTEGRITY TRACK                            |
|                                                                               |
|  [Track 1: 10 Wounds] -> [Track 2: 10 Wounds] -> [Track 3: 10] -> [Track 4: 10] |
|   (Superficial Hits)      (Decompression Risk)    (System Failure) (Hull Rupture) |
+-------------------------------------------------------------------------------+
```

### 1. Hull Rating & Condition Tracks

The Hull Rating represents the physical integrity and structural endurance of the ship's reinforced titanium keel and composite spaceframe. Because hard sci-fi spacecraft lack deflector shielding, any incoming projectile or thermal beam that penetrates point-defense grids strikes the hull directly.

A ship's Hull Condition Track is divided into smaller sequential tracks, each possessing a segment capacity equal to the ship's **Hull Rating** (always an even number):

* **Small Craft:** 4 tracks of 6 to 10 segments each.
* **Medium Craft:** 4 tracks of 10 to 12 segments each.
* **Large Capital Ships:** 4 to 6 tracks of 12 to 16 segments each.

Hull Condition Tracks sustain damage in the exact same manner as personal Health Tracks. When a single track fills completely with Light Wounds, damage does not immediately bleed into the next track; instead, subsequent hits begin converting existing Light Wounds on that track into **Aggravated Wounds** (critical structural breaches and frame warping).

* **System Shutdown:** When a ship's final Condition Track fills completely with Light Wounds, the vessel suffers complete electrical grid failure, loses main propulsion, and drifts dead in space.
* **Catastrophic Rupture:** When the final Condition Track fills with Aggravated Wounds, the ship's reactor containment fails, tearing the hull apart in a silent orbital fireball.

### 2. Armor (Protection)

Armor represents dense ceramic-composite plates, Whipple shields, and depleted-uranium hull tiling. Armor functions as the ship's **Protection Rating**: each point of Armor reduces incoming weapon damage by a flat **1 point per hit**. High-velocity kinetic rounds or laser beams must overcome this threshold before marking wounds on the Hull Condition Track.

### 3. Engines (Acceleration & Maneuverability)

Starship propulsion is governed by two complementary engine performance ratings:

* **Acceleration:** Governs main fusion drive thrust and longitudinal vector speed. Used exclusively for **Macro-Grid Movement** and high-thrust Breakaway burns.
* **Maneuverability:** Governs cold-gas Reaction Control System (RCS) attitude thrusters, gyroscopic flywheels, and vernier clusters. Used exclusively for **Dogfight Scale Movement** and defensive vector jinking.

### 4. Systems

The Systems attribute measures the computational power of the ship's fire-control mainframes, cryogenic sensor arrays, EWAR suites, and automated maintenance networks:

* **Sensor Range:** The maximum distance at which the ship can establish Target Locks and detect low-observable craft on the Macro-Grid. Calculated as **2 kilometers per point of Systems** (a ship with Systems 4 possesses an 8 km Sensor Range).
* **Power Distribution:** The Engineer can reroute reactor output to supercharge internal systems. By rolling a Simple Test with **Systems**, each Hit scored can be allocated as **1 Upgrade** to either *Weapons* (Accuracy and Tracking), *Engines* (Acceleration and Maneuverability), or *Systems* (EWAR and Sensors) until the end of the combat round, up to a maximum of 3 Upgrades.
* **Repair Drones:** Governs automated damage-control nanite hives and mobile maintenance crawlers that deploy to patch breached bulkheads mid-fight.

### 5. Internal Module Slots

Internal modules represent mission-specific infrastructure, avionics upgrades, and life support enhancements installed within the pressurized hull envelope. A ship possesses a fixed number of **Module Slots** determined by its structural size tier:

* **Small Vessels:** 4 Module Slots
* **Medium Vessels:** 8 Module Slots
* **Large Capital Ships:** 12 Module Slots

Each internal module has an installation cost of 1 to 3 slots.

---

## Bridge Roles & Command Seats

Every starship bridge or flight deck is equipped with dedicated physical workstations. While any spacer can monitor auxiliary telemetry or trigger basic thruster bursts from an auxiliary terminal, sitting strapped into a **dedicated command seat** connects the operator directly into high-speed fire-control buses, pneumatic flight yokes, and reactor shunts.

If a crew member is incapacitated by G-Strain or tactical priorities shift mid-battle, a character may spend **1 Action Point (AP)** to unstrap, pull through zero-G handrails, and swap into an unmanned seat.

### Basic Ship Actions (Any Station)

Any crew member at an operational terminal can perform the following baseline maneuvers:

* **Full Throttle:** A Success Test using the ship's **Acceleration**. Used to maneuver on the Macro-Grid or initiate a dogfight Breakaway burn.
* **Combat Maneuver:** A Complex Test combining **Maneuverability + Instinct**. Used to climb or drop positions along the Dogfight Scale.
* **Weapons Hot:** Trigger and discharge an operational weapon mounted to any available hardpoint, provided its rate of fire has not been expended.

### The Three Core Bridge Seats

To unleash a vessel's true combat potential, crew members take their places across three primary command stations:

#### The Pilot Seat
The pilot interfaces directly with primary propulsion and attitude thrusters, reading vector trajectories through the main canopy or synthetic wrap-around displays.
* **Enhanced Controls:** Sitting strapped in the Pilot seat grants **1 Upgrade** to all *Full Throttle* and *Combat Maneuver* tests.
* **Evasive Maneuvers:** When the ship is targeted by incoming weapon fire, the Pilot can spend 1 AP to **contest attacks using Instinct**.
* **Stay on Target:** When an enemy tries to disengage or alter vector, the Pilot can spend 1 AP to **contest Breakaways and Maneuvers** using the ship's Acceleration or Maneuverability.

#### The Gunner Seat
The gunner commands weapons feeds, optical lead calculators, and point-defense interception grids to track and destroy incoming threats.
* **Enhanced Targeting:** Sitting in the Gunner seat grants **1 Upgrade** to all attack tests using weapon *Accuracy* and *Tracking*.
* **Target Lock:** The Gunner can roll a Simple Test with **Systems** to acquire a Target Lock on a vessel within Sensor Range for each hit sacrificed. Each level of Target Lock provides 1 Upgrade to guided weapons.
* **Point Defense:** The Gunner can spend 1 AP to **contest guided weapon attacks** using a Point-Defense Cannon's (PDC) Accuracy. Firing with multiple active PDCs grants **1 Upgrade per additional PDC**.

#### The Engineer Seat
The engineer manages the ship's reactor core, cooling loops, EWAR jammers, and automated maintenance drones.
* **Enhanced Interface:** Sitting in the Engineer seat grants **1 Upgrade** to all tests made using *Systems*.
* **Repair Drones:** Perform a Complex Test using **Knowledge + Systems** to deploy automated repair drones and patch damaged hull segments or restore offline modules mid-battle.
* **Radar Jammer:** Perform a Complex Test using **Knowledge + Systems** to emit broad-spectrum electronic counter-measures, breaking enemy Target Locks held on your ship.
* **Power Distribution:** Roll a Simple Test with **Systems** to shunt surplus reactor output, granting up to 3 Upgrades to Weapons, Engines, or Systems until the end of the round.

### Tactical Comms & Sensor Warfare

Combat operations demand strict voice discipline under high acceleration ("Ladar hard on bearing two-seven, salvo away"). Concurrently, electronic warfare (EWAR) stations monitor passive radio frequencies and drive thermals, executing *Passive Surveillance* to track hostile signatures without radiating active ladar.

### Damage Control Teams & Combat Depressurization

When penetrating hits buckle outer bulkheads, damage control teams don magnetic boots to seal compartments, dog down emergency hatches, and flood burning bays with halon gas (granting +1 Upgrade to Engineer repair tests). Prior to engagement, veteran crews execute combat depressurization, pumping cabin air back into reserve tanks to eliminate explosive decompression and flash fires when bulkheads are breached.

### Auxiliary Stations & Skeleton Crews

Larger starships carry multiple Gunner and Engineer consoles for simultaneous PDC interception and damage control. Shorthanded vessels operating with a skeleton crew suffer severe limits: without a dedicated Gunner, PDCs cannot execute reaction intercepts; without an Engineer, power cannot be redistributed mid-flight.

---

## Combat Walkthrough: The Skirmish at Vesta Void

To illustrate how orbital vector mechanics, bridge command actions, point-defense screens, and G-Strain interact under *Corsair's* core rules, observe the following encounter between the player crew's **RF "Kestrel"** (corvette) and an aggressive pirate-operated **GVI "Rusty Hook"** in the debris belt of Vesta.

### The Combatants

* **RF "Kestrel" (Players):** Hull Rating 10 (4 tracks of 10), Armor 2, Acceleration 3, Maneuverability 4, Systems 3 (Sensor Range 6 km). Hardpoints: 1x PA "Sentinel" Rotary PDC (S), 1x GVI "Stinger" Light Missile (S), 1x CQV "Solarflare" Laser Array (M). Modules: Injector Seats, Fire-Control Computer.
  * **Crew (3 AP each at start of round):** **Jax** (Pilot: Instinct 3, Agility 3), **Sarah** (Engineer: Knowledge 4, Systems 3), **Miller** (Gunner: Finesse 3, Systems 3).
* **GVI "Rusty Hook" (Pirates):** Hull Rating 10 (4 tracks of 10), Armor 2, Acceleration 2, Maneuverability 4, Systems 2 (Sensor Range 4 km). Weapons: PA "Sentinel" Rotary PDC (S), PA "Caltrop" Mine Dispenser (S), KSK "Harpoon" Kinetic Missile (S: Guided, Tracking 4, Damage +1).
  * **Crew (3 AP each at start of round):** Pirate Pilot (Instinct 3, Acceleration 2, Maneuverability 4), Pirate Gunner (Systems 2, Tracking 4), Pirate Engineer (Systems 2).

The encounter takes place during **Round 1**. Control alternates between the players and the GM whenever an active side spends **2 or more Action Points (AP)**.

---

### Player Turn 1 (2 AP Spent — Approach & Interception)

The *Kestrel* detects the pirate *Rusty Hook* closing across an asteroid corridor at a distance of 2 hex spaces (2 km) on the Macro-Grid.

* **Sarah (1 AP):** Sitting in the Engineer seat, Sarah opens the engagement by shunting surplus reactor power to propulsion. She makes a Simple Test with **Systems (3)**. Sitting in the Engineer seat grants **1 Upgrade** (stepping one d10 up to a d12, so 1d12 + 2d10). Sarah rolls `[9]` on the d12 and `[8, 4]` on the d10s. Two Hits (`9` and `8`)! She allocates both hits as Upgrades to *Engines* (Acceleration and Maneuverability) until the end of the round. *(Sarah: 2 AP remaining)*
* **Jax (1 AP):** Jax sits strapped in the Pilot seat and executes Full Throttle to close the distance. He makes a Success Test with **Acceleration (3)** + 1 Upgrade (Pilot Seat) + 2 Upgrades (Reactor Shunt) = 3 Upgrades total (3d12). Jax rolls `[11, 8, 7]`. The highest die is `11`. Jax spends 4 Success Points to propel the *Kestrel* 2 hex spaces (2,000 meters) straight into the pirate's hex! Because he spends only 4 SPs (below the 6 SP threshold), the crew suffers zero G-Strain. *(Jax: 2 AP remaining)*
* **Transition to Dogfight Mode:** Because the *Kestrel* moved into the pirate's hex, Jax claims the **Interception Advantage**! The *Kestrel* begins at **Position 6 (Attacker Edge)**, while the defending pirate begins at **Position 5 (Defender Neutral)**.

*Having spent 2 Action Points collectively (Sarah 1, Jax 1), control swaps to the GM.*

---

### GM Turn 1 (2 AP Spent — Guided Missile Salvo)

With both ships now swirling inside the same 1 km hex space, the pirate gunner scrambles to seize the initiative.

* **Pirate Gunner (1 AP):** The pirate gunner attempts to acquire Target Lock on the *Kestrel* at Position 5. Making a Simple Test with **Systems (2)**, the pirate rolls 2d10: `[8, 3]`. That `8` is a Hit! The pirate sacrifices the Hit to establish **1 level of Target Lock** on the *Kestrel*. *(Pirate Gunner: 2 AP remaining)*
* **Pirate Gunner (1 AP):** The pirate gunner launches their **KSK "Harpoon" Kinetic Missile** (Guided, Tracking 4, Damage +1). Guided attacks are a Complex Test using **Tracking + Tracking (4 dice)**. The Target Lock grants **1 Upgrade** (1d12 + 3d10).
  * **Action Roll:** The pirate rolls `[10]` on the d12, and `[8, 5, 2]` on the d10s. Two `8+` dice (`10` and `8`)—the missile locks onto the Kestrel's drive plume!
* **Miller (Reaction — 1 AP):** Observing the missile launch on his radar scope, Miller reacts from the Gunner seat with **Point Defense**, spending 1 AP to intercept using the **PA "Sentinel" Rotary PDC** (Point-Defense 5). Sitting in the Gunner seat grants **1 Upgrade**. Miller rolls a Simple Test of 5 dice (1d12 + 4d10) for PDC Accuracy: `[9]` on the d12, `[8, 7, 6, 2]` on the d10s. Two Hits (`9` and `8`)!
* **Contest Resolution:** Following the standard rule for contesting a test, each contest Hit eliminates one of the highest dice from the incoming attack roll. Miller's two Hits eliminate the pirate's `10` and `8`! With no `8+` dice remaining, the missile attack is completely resisted—the Sentinel's rotary flak curtain shreds the Harpoon kinetic dart in mid-vacuum 200 meters out! *(Miller: 2 AP remaining)*

*Having spent 2 Action Points on their turn (Gunner 2), control swaps back to the players.*

---

### Player Turn 2 (2 AP Spent — Tail Position & Laser Strike)

With the missile destroyed, the player crew seizes the opening to press their tactical advantage.

* **Jax (1 AP):** Jax declares a **Combat Maneuver** to climb the Dogfight Scale and gain the pirate's tail. This is a Complex Test combining **Maneuverability (4) + Instinct (3)**. Higher attribute is 4, lower is 3. Jax benefits from 1 Upgrade (Pilot Seat) + 2 Upgrades (Reactor Shunt) = 3 Upgrades total (3d12 + 1d10).
  * **Action Roll:** Jax rolls: `[11, 9, 8]` on the d12s, and `[6]` on the d10. Three Hits (`11, 9, 8`)!
* **Pirate Pilot (Reaction — 1 AP):** The pirate pilot spends 1 AP to contest the maneuver using **Maneuverability (4)**. The pirate rolls a Simple Test with 4d10: `[8, 5, 3, 2]`. One Hit (`8`).
* **Contest Resolution:** The pirate's single Hit eliminates the highest die (`11`) from Jax's pool. The remaining dice are `[9, 8, 6]`. Because two `8+` dice remain, the Action Roll still succeeds!
  * **Success Roll:** Jax takes dice equal to the lower attribute (Instinct 3) from the successful roll: `[9, 8, 6]`. The highest single die is a **9**! Jax spends 3 Success Points to advance the *Kestrel* from Position 6 to **Position 9 (Advantage: On their Tail!)**, suffering zero G-Strain. *(Jax: 1 AP remaining, Pirate Pilot: 2 AP remaining)*
* **Miller (1 AP):** Holding Position 9 (Advantage), Miller trains the Medium Hardpoint **CQV "Solarflare" Laser Array** (Damage +2). At Advantage, the Solarflare has an Accuracy bonus of 2 dice. Unguided attacks are a Complex Test using **Finesse (3) + Accuracy (2)**. Higher is Finesse 3, lower is Accuracy 2. Sitting in the Gunner seat grants **1 Upgrade** (1d12 + 2d10).
  * **Action Roll:** Miller rolls: `[10]` on the d12, `[8, 5]` on the d10s. Two Hits (`10` and `8`)—the beam locks onto the pirate's drive casing! Pinned at Disadvantage (Position 2 from their view), the pirate cannot contest with Evasive Maneuvers.
  * **Success Roll:** Miller selects 2 dice (lower attribute) from the roll: `[10, 8]`. The highest die is **10 Success Points**!
  * **Damage Resolution:** Total Damage = Success Points (10) + Damage Bonus (+2) = **12 damage**! The *Rusty Hook* has **Armor 2 (Protection)**, reducing the damage by 2. The remaining **10 damage** strikes the hull directly!
  * **Condition Track:** The *Rusty Hook* has a Hull Rating of 10. The 10 penetrating damage completely fills the pirate's **First Hull Track** (`[10/10 Light Wounds]`). Titanium armor boils away and toxic ozone floods the pirate flight deck! *(Miller: 1 AP remaining)*

*Having spent 2 Action Points (Jax 1, Miller 1), control swaps back to the GM.*

---

### GM Turn 2 (2 AP Spent — Failed Breakaway & Surrender)

With their first hull track shattered and sirens screaming, the pirates make a desperate bid to break contact.

* **Pirate Pilot (1 AP):** Pinned at Position 2 from their perspective, the pirate pilot executes a desperate **Breakaway Burn** to escape back to neutral territory. This is a Success Test using **Acceleration (2)**. The pirate rolls 2d10: `[9, 5]`. The highest die is `9` (9 Success Points).
* **Jax (Reaction — 1 AP):** Sitting in the Pilot seat, Jax uses his *Stay on Target* benefit, spending his final 1 AP to contest the Breakaway using **Acceleration (3)**. The Pilot seat grants **1 Upgrade** (1d12 + 2d10). Jax rolls: `[10]` on the d12, `[8, 4]` on the d10s. Two Hits (`10` and `8`)!
* **Contest Resolution:** Following the standard rule for contesting a Success Test, each contest Hit eliminates one of the highest dice from the contested roll. Jax's two Hits eliminate both the `9` and the `5` from the pirate's roll! With all `8+` dice eliminated, the contest succeeds completely: the Breakaway yields **0 Success Points**! The pirate vessel fails to alter vector and remains pinned at Position 2 with the *Kestrel* glued to its engine exhaust. *(Jax: 0 AP remaining, Pirate Pilot: 1 AP remaining)*
* **Pirate Pilot (1 AP):** Out of options and staring into the charged sapphire optics of the Solarflare laser array, the pirate captain spends their final AP to cut reactor power, vent thrust manifolds, and transmit an emergency surrender broadcast over open comms: *"Cease fire, Kestrel! We're dead in the water! Don't breach our reactor core—we surrender!"*

---

### Encounter Debrief: Core Rule Invariants

1. **2 AP Turn Switch:** Control alternated between the player crew and the GM as Action Points were spent (Player Turn 1: 2 AP $\rightarrow$ GM Turn 1: 2 AP $\rightarrow$ Player Turn 2: 2 AP $\rightarrow$ GM Turn 2: 2 AP), preserving dynamic tactical momentum within a single Round.
2. **Standard Contesting Rule:** When Miller contested the missile with Point Defense and Jax contested the Breakaway with Stay on Target, each contest Hit (`8+`) eliminated one of the highest dice from the contested roll. Eliminating all `8+` dice caused the incoming attack to miss and the Breakaway Success Test to yield 0 Success Points.
3. **Seat Synergies:** The Pilot seat's free Upgrades and Stay on Target reaction, the Gunner seat's Point Defense reaction, and the Engineer seat's Power Distribution test allowed a coordinated 3-person crew to neutralize threats and dictate the engagement.
