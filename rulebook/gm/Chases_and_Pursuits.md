# Chapter 10: Chases & Pursuits

In the cutthroat expanse of the Sphere, knowing when to pull back and run—or when to run a fleeing suspect to ground—is just as vital to a Corsair cell's survival as knowing when to draw a sidearm. Whether marshals are sprinting through the humid, neon-drenched bazaars of Port Zenith with syndicate hit squads on their heels, gunning the supercharged turbine of a patrol rover across the wind-scoured badlands to run down an outlaw convoy, or burning sub-light thrusters to the physiological limits of human endurance to evade an ambush by a pirate strike frigate, chases are intense, white-knuckle transitions where seconds translate into kilometers.

In *Corsair*, an escape is neither an automatic narrative hand-wave nor an abstract series of disconnected skill checks that stall the momentum of the game. Instead, chases function as an operational bridge between **Moment-to-Moment** tactical combat and **Place-to-Place** macro exploration. Governed by a tangible token economy, strict tactical guardrails, and severe consequences for failure, the pursuit engine ensures that every evasion attempt is a calculated gamble with life-or-death stakes.

```
+---------------------------------------------------------------------------------------------------------+
|                                      THE PURSUIT RESOLUTION CYCLE                                       |
+---------------------------------------------------------------------------------------------------------+
|  [ 1. TACTICAL COMBAT ]           --->  [ 2. VERIFY GUARDRAILS ]        --->  [ 3. COMMIT PLACE-TO-PLACE AP ]
|  Operatives position, trade fire,        Outside CQC (0 spaces);               Quarry spends 1 P2P AP;
|  and break off engagement                viable exit vector;                   Pursuers must spend 1 P2P AP
|  on the Moment-to-Moment grid.           operational locomotion online.        to give chase and contest.
|                                                                                                         |
|  [ 4. RESOLVE CONTEST ROLL ]      --->  [ 5A. CLEAN ESCAPE ]            OR    [ 5B. VIOLENT INTERCEPTION ] 
|  Quarry rolls Mode Attribute Pair;       Quarry retains >=1 Hit (8+).          All 8+ Hits eliminated. Scene 
|  Each pursuer rolls Contest pool.        Zooms to P2P Manhunt:                 zooms to Moment-to-Moment:   
|  Distance modifiers apply.               governed by Hideout & Heat.           Pursuers get 3 AP & ACT FIRST!
+---------------------------------------------------------------------------------------------------------+
```

---

## The Escape Engine

When a combat situation deteriorates or an objective shifts to extraction, a character, vehicle crew, or starship cannot simply vanish into thin air. Breaking contact requires dedicated macro-level time, physical separation, and operational focus.

### The Escape Action
To break away from an active tactical engagement, a creature or vessel must execute an **Escape Attempt**. 

* **The AP Cost:** Attempting an escape costs **1 Place-to-Place Action Point (AP)** from the fleeing character's broader operational pool. 
* **Tactical Turn Consumption:** Because the character is committing their immediate focus to breaking off tactical engagement and accelerating into macro-traversal (covering hundreds of meters or kilometers), executing an Escape Attempt immediately consumes all remaining **Moment-to-Moment AP** for that character on their current turn.
* **Vehicles and Starships:** When fleeing inside a ground vehicle or starship, **a single driver or pilot spends 1 Place-to-Place AP** to maneuver the entire vessel and its passengers out of the danger zone. Crew members not operating the primary controls pay **0 AP**, though they may use their tactical actions to assist via sensors, countermeasures, or suppressive fire.
* **Groups on Foot:** When multiple operatives flee on foot together, each character must spend **1 Place-to-Place AP** from their individual pool and resolve the flight using the rules for **Teamwork Cell Escapes** (detailed below).

---

## The Guardrails of Disengagement

A character cannot declare an Escape Attempt indiscriminately. The Game Master enforces three strict tactical prerequisites before any creature, vehicle, or vessel is permitted to spend an Action Point to flee:

```
+---------------------------------------------------------------------------------------------------------+
|                                    THE GUARDRAILS OF DISENGAGEMENT                                      |
+-------------------+-------------------------------------------------------------------------------------+
| Guardrail         | Operational Requirement                                                             |
+-------------------+-------------------------------------------------------------------------------------+
| 1. Clearance      | Outside Close Quarters Combat (CQC / 0 spaces) and unrestrained.                     |
| 2. Vector         | An unobstructed, viable egress path (unlocked bulkheads, clear alleys, open skies). |
| 3. Mobility       | Operational locomotion or propulsion (conscious, unrestrained, active engines).     |
+-------------------+-------------------------------------------------------------------------------------+
```

### 1. Tactical Clearance (Outside CQC)
The fleeing entity must have tactical clearance—meaning they cannot be engaged in **Close Quarters Combat (CQC)**, occupying the same 4x4 meter space (0 spaces) as an active hostile, nor be grappled or physically pinned.

If an operative is locked in CQC, an adversary's physical grip and point-blank engagement prevent them from initiating macro-traversal. The operative must first spend Moment-to-Moment movement or defensive actions (such as Shoving or Disengaging) to clear the shared space and establish at least 1 space of physical separation.

> **Escaping from Short Range (1–5 spaces):** Once an operative has cleared CQC and is at least 1 space away (1+ spaces / >0 meters), they meet this guardrail and are permitted to declare an Escape Attempt. However, attempting to break away within Short Range (1–5 spaces / 4–20 meters) is inherently precarious under point-blank fire: the quarry suffers **2 Downgrades** and pursuers gain **2 Upgrades** on the contest roll.
> 
> **Obscurance Does Not Waive CQC:** Environmental obscurance—such as deploying a smoke grenade, cutting facility power, or slipping behind cover—provides valuable tactical Upgrades and Downgrades, but **does not waive the CQC restriction**. An operative pinned in CQC inside a smoke cloud cannot flee until they physically push out of the same space.

### 2. Viable Egress Vector
The fleeing party must possess an accessible, physically open escape route. Attempting to escape into a dead-end alleyway, a sealed vault, an airlock cycling in lockdown, or a hangar bay with closed blast shields is impossible. The cell must first breach, slice, or unlock the barrier before attempting to flee through it.

### 3. Operational Mobility
The fleeing creature or craft must possess functioning locomotion and physical freedom of movement:
* **Characters on Foot:** Must be conscious, upright, unrestrained (not pinned, handcuffed, grappled, or held in magnetic restraints), and unhampered by paralyzing neurotoxins or broken limbs that reduce speed to zero.
* **Ground Vehicles:** Must have an operational drivetrain, inflated or intact treads/tires, and a functioning power plant (not disabled at 0 HP).
* **Starships (Dogfight Breakaway Requirement):** A starship engaged in close-quarters dogfighting cannot immediately jump into an escape burn. The pilot must first execute a successful **Breakaway** maneuver (shifting the Dogfight Scale to neutral Position 4 or higher) to reach the **Macro-Grid** outside the dogfight hex before declaring an orbital escape attempt.

---

## Pursuer Commitment & Contesting

When a quarry satisfies the guardrails and declares an Escape Attempt, adversaries in the scene face an immediate operational choice: let them go, or commit resources to run them down.

### Pursuer AP Commitment
Chasing a fleeing quarry over hundreds of meters through crowded alleys, across rugged badlands, or along high-g orbital trajectories takes real operational time:

* **The Pursuer's Cost:** Any pursuer who wishes to give chase and contest the escape **must spend 1 Place-to-Place Action Point**.
* **Automatic Escape:** If pursuing adversaries have already exhausted their Place-to-Place AP for the broader round, or if the GM decides they are unwilling to abandon their current defensive post, the quarry **escapes automatically without a roll**.
* **Multiple Pursuers:** When multiple adversaries give chase, each participating pursuer must spend 1 Place-to-Place AP. **Each pursuer rolls their own separate contest pool!** Every Hit (8+) scored across all pursuers' pools eliminates the highest die from the quarry's roll (or can be strategically allocated across fleeing cell members).

```
+---------------------------------------------------------------------------------------------------------+
|                                    ESCAPE ATTEMPT CONTEST RESOLUTION                                    |
+---------------------------------------------------------------------------------------------------------+
| 1. QUARRY ACTION ROLL                                                                                   |
|    The fleeing quarry spends 1 Place-to-Place AP and rolls a Simple Test using their domain's           |
|    designated Attribute Pair (e.g., Agility + Instinct on foot).                                        |
|                                                                                                         |
| 2. PURSUER CONTEST ROLL                                                                                 |
|    Each pursuing adversary commits 1 Place-to-Place AP and rolls a Simple Test using their appropriate  |
|    chase Attribute Pair.                                                                                |
|                                                                                                         |
| 3. ELIMINATING DICE                                                                                     |
|    Each Hit (8+) scored on the Pursuer's Contest Roll eliminates the highest die from the quarry's pool.|
|                                                                                                         |
| 4. DETERMINING THE OUTCOME                                                                              |
|    * If the quarry retains at least one 8+ Hit: Clean Escape! Contact is broken.                        |
|    * If all 8+ Hits are eliminated (or zero were rolled): Interception! Pursuers run them down.        |
+---------------------------------------------------------------------------------------------------------+
```

---

## Outcomes: Clean Escape vs. Violent Interception

The contested roll yields one of two absolute outcomes: total disengagement or a catastrophic tactical interception.

### Clean Escape (Success)
If the quarry retains at least one Hit (`8+`) after the pursuers' contest dice have eliminated results, the quarry successfully shakes their pursuers on the tactical grid:

1. **Breaking Immediate Contact:** The quarry slips through perimeter alleys, ducks beneath sensor sweeps, or out-accelerates pursuers past the visual horizon. Immediate line of sight and weapon target locks are broken.
2. **Zooming Out to Place-to-Place:** The encounter immediately shifts out of Moment-to-Moment combat into **Place-to-Place exploration** (~15–30 minute rounds).
3. **Transition to the Macro Manhunt:** Breaking tactical contact is not strategic disappearance. The getaway transitions into a **Place-to-Place Manhunt** governed by **Hideout** (the Blocker Effect) and **Heat** (the ticking countdown clock), detailed in the section below.
4. **Resuming Broader Pacing:** Both the quarry and the pursuers retain whatever Place-to-Place AP they have remaining for the broader round.

### Violent Interception (Failure)
If the pursuers eliminate all `8+` dice from the quarry's roll—or if the quarry failed to roll a single Hit on their initial test—the escape attempt fails catastrophically. The pursuers close the gap, cut off the retreat, and corner the fleeing party:

1. **Zooming Back to Moment-to-Moment:** Play immediately drops back into **Moment-to-Moment tactical combat** at the physical location where the quarry was run down (e.g., a dead-end maintenance corridor, an open intersection, or a rocky bottleneck).
2. **Universal AP Refill:** Because the scene has transitioned back into Moment-to-Moment pacing, all participants refill their tactical Action Points to their maximum (**3 AP**).
3. **Pursuers Take Immediate Initiative:** The pursuers hold the operational momentum. **The pursuers act first**, taking the opening turn of the new tactical engagement.
4. **Pursuers Choose Relative Positioning:** The pursuers dictate the tactical geometry of the new confrontation. The Game Master (or players, if they are the pursuers) places their characters **anywhere relative to the quarry** on the tactical grid:
   * Surrounding the quarry from multiple angles.
   * Flanking from high ground or claiming Heavy Cover while leaving the quarry Exposed.
   * Positioning directly across the exit vector to block further retreat.
   * Closing directly into Close Quarters Combat (CQC) in the same space as the quarry.
   * *In Starship Combat:* The pursuer enters **Dogfight Mode** sharing the quarry's hex, starting at **Position 8, 9, or 10 (Advantage)** directly on the quarry's tail!
5. **Permanent AP Loss:** The 1 Place-to-Place AP spent by the quarry remains spent, permanently reducing their operational time runway for the remainder of that macro round.

---

## Modes of Pursuit

Pursuits unfold across three distinct operational environments, each defined by specific physical constraints, speed parity invariants, and attribute pairings.

```
+---------------------------------------------------------------------------------------------------------+
|                                        PURSUIT MODES COMPARISON                                         |
+-----------------+-----------------------+-----------------------+---------------------------------------+
| Mode            | Quarry Attribute Pair | Pursuer Attribute Pair| Invariants & Special Rules            |
+-----------------+-----------------------+-----------------------+---------------------------------------+
| Foot Pursuits   | Agility + Instinct    | Agility + Instinct    | Mobility Gear (jetpacks, grapples)    |
|                 |                       |                       | pairs item's Mobility attribute.      |
+-----------------+-----------------------+-----------------------+---------------------------------------+
| Ground Vehicles | Acceleration + Accel. | Acceleration + Accel. | Cannot be contested on foot!          |
|                 | (Open Terrain)        | (Open Terrain)        | Speed tier differences grant Upgrades;|
|                 | Maneuvering + Instinct| Maneuvering + Instinct| collision damage on brutal turns.     |
|                 | (Crowded / Canyons)   | (Crowded / Canyons)   |                                       |
+-----------------+-----------------------+-----------------------+---------------------------------------+
| Space Combat    | Acceleration + Accel. | Acceleration + Accel. | Must break out of Dogfight Mode first;|
|                 | (Open Void)           | (Open Void)           | G-Strain: 2 LW per Hit on burns;      |
|                 | Maneuvering + Instinct| Maneuvering + Instinct| pursuer intercepts at Dogfight Pos 8+.|
|                 | (Debris / Asteroids)  | (Debris / Asteroids)  | Cannot be contested by non-spacecraft.|
+-----------------+-----------------------+-----------------------+---------------------------------------+
```

---

### Foot Pursuits
Foot pursuits represent desperate dashes through crowded civilian terminals, industrial catwalks, zero-g transit tubes, and narrow maintenance tunnels.

* **Standard Attribute Pair:** **Agility + Instinct**. Fleeing on foot is a balance of raw sprinting speed (**Agility**) and snap situational navigation (**Instinct**)—spotting opening doors, ducking beneath low pipes, and vaulting obstacles.
* **Mobility Gear Integration:** When characters activate specialized mobility hardware (see [Gear](../equipment/Gear.md)), the equipment's dedicated **Mobility** attribute pairs with a character physical attribute:
  * **Jump-Packs & Jetpacks:** Uses **Mobility + Agility** (Light Jump-Pack, Tactical Jetpack, Heavy Jump-Rig) to fly over obstacles, clear chasms, and ignore difficult ground terrain.
  * **Grapple Launchers & Gecko Climbing Kits:** Uses **Mobility + Strength** (Standard Grapple Launcher, Tactical Grapple Launcher, Gecko Climbing Kit) to rapidly haul oneself up vertical elevator shafts, gantry cranes, or metallic hulls.

---

### Ground & Atmospheric Vehicles
High-speed vehicular chases occur across planetary surfaces, subterranean highways, mining badlands, and suspended cloud platforms.

* **Standard Attribute Pairs:**
  * **Open Terrain / Straightaways:** **Acceleration + Acceleration**. On wide salt flats, paved highways, or open tundra, the chase comes down to raw horsepower, torque, and turbine thrust. The vehicle's Acceleration rating forms the test pool.
  * **Crowded Corridors / Canyon Runs / Urban Streets:** **Maneuvering + Instinct**. When weaving through civilian traffic, dodging falling rock pillars, or taking ninety-degree turns around industrial bulkheads, raw speed gives way to vehicle handling (**Maneuvering**) and the driver's reflexive reaction time (**Instinct**).
* **The Foot-to-Vehicle Invariant:** **Motorized vehicles cannot be contested on foot!** If a quarry boards an operational ground vehicle (such as a hover-skimmer, combat rover, or speeder bike) and satisfies the clearance guardrails, pursuers on foot cannot spend Place-to-Place AP to chase them down. The vehicle escapes automatically unless the pursuers have their own vehicles, orbital gunships, or readied anti-vehicle heavy weaponry.
* **Speed Tier Differentials:** When vehicles of vastly different performance classes engage in a pursuit, the faster craft gains **1 Upgrade** per speed tier advantage over its rival (e.g., a lightweight military hover-interceptor chasing a lumbering six-wheel mining hauler gains 2 Upgrades).

---

### Space Combat & Orbital Intercepts
Starship pursuits take place in the cold vacuum of orbital space, asteroid belts, and planetary upper atmospheres under Newtonian momentum.

* **Dogfight Breakaway Prerequisite:** Space combat operates on two scales: the close-quarters **Dogfight Scale (1–10)** and the orbital **Macro-Grid (1 km hexes)**. A starship cannot declare an orbital Escape Attempt while locked in Dogfight Mode. The pilot must first spend tactical actions to execute a **Breakaway** (shifting the scale to neutral Position 4+) and move onto the Macro-Grid outside the opponent's hex before declaring an escape burn.
* **Standard Attribute Pairs:**
  * **Open Void Escape Burns:** **Acceleration + Acceleration**. High-thrust brachistochrone escape trajectories rely purely on engine burn capability. Both quarry and pursuer roll their ship's **Acceleration** rating.
  * **Debris Fields / Dense Asteroids / Station Superstructures:** **Maneuvering + Instinct**. Weaving through orbital shipyards or dense ring systems pairs the ship's **Maneuvering** rating with the pilot's **Instinct**.
* **Physiological G-Strain:** Spacecraft in *Corsair* do not possess inertial dampeners. When pilots push sub-light drives to emergency burn levels, the crushing acceleration takes a severe physical toll on living bodies. In pursuit burns, **each Hit (8+) scored on the roll triggers 2 Light Wounds (2 LW) of G-Strain** across everyone aboard the vessel. This damage cannot be reduced by personal armor Protection (though shipboard internal modules such as Injector Seats halve it). Pilots must therefore balance the tactical necessity of scoring high Hits against the risk of inflicting massive physical trauma on their own crew.
* **The Non-Spacecraft Invariant:** Starships executing an orbital burn cannot be contested by surface vehicles or infantry.
* **Interception Consequence:** If an orbital pursuer wins the contest, they immediately intercept the quarry on the Macro-Grid, pulling directly into **Dogfight Mode** at **Position 8, 9, or 10 (Advantage)** on the quarry's tail!

---

## Distance & Tactical Modifiers

In any pursuit, separation distance is the primary, objective arbiter of whether a quarry escapes or gets intercepted. While being outside CQC (at least 1 space of separation) is the mandatory baseline guardrail to attempt an escape, physical separation dictates the relative advantage between quarry and pursuers.

### Hard and Fast Distance Modifiers
The physical distance separating quarry and pursuers at the moment the escape is declared dictates the baseline Upgrades and Downgrades applied to the contested test:

```
+---------------------------------------------------------------------------------------------------------+
|                                       DISTANCE PURSUIT MODIFIERS                                        |
+-------------------+--------------------+------------------------+---------------------------------------+
| Range Band        | Distance on Grid   | Quarry Modifier        | Pursuer Modifier                      |
+-------------------+--------------------+------------------------+---------------------------------------+
| CQC (Same Space)  | 0 spaces (0m)      | CANNOT ESCAPE          | Guardrail 1 violated (must clear CQC).|
+-------------------+--------------------+------------------------+---------------------------------------+
| Short Range       | 1–5 spaces (4–20m) | 2 Downgrades           | +2 Upgrades                           |
+-------------------+--------------------+------------------------+---------------------------------------+
| Medium Range      | 6–12 spaces (24–48m)| No Modifiers          | No Modifiers (baseline threshold).   |
+-------------------+--------------------+------------------------+---------------------------------------+
| Long Range        | 13–20 spaces (52–80m)| +2 Upgrades          | 2 Downgrades                          |
+-------------------+--------------------+------------------------+---------------------------------------+
| Extreme Range     | 20+ spaces (80+m)  | AUTOMATIC ESCAPE       | Contact broken; no roll required.     |
+-------------------+--------------------+------------------------+---------------------------------------+
```

* **CQC (0 spaces / same space):** Violates Guardrail 1. An operative cannot turn and run while physically grappling or sharing a space with an armed combatant.
* **Short Range (1–5 spaces / ~4–20 meters):** Breaking away under point-blank rifle fire and immediate pursuit is exceedingly difficult. The fleeing quarry suffers **2 Downgrades**, and pursuers gain **2 Upgrades** on their contest rolls.
* **Medium Range (6–12 spaces / ~24–48 meters):** The standard tactical baseline. Neither side receives distance modifiers.
* **Long Range (13–20 spaces / ~52–80 meters):** Symmetrically rewards the quarry for establishing a head start. The fleeing quarry gains **2 Upgrades**, and pursuing chasers suffer **2 Downgrades** on their contest rolls.
* **Extreme Range (20+ spaces / 80+ meters):** The quarry has opened up decisive separation across open runways, multi-level gantries, or distant city avenues. Visual and operational contact is effectively broken on the tactical scale. The escape is an **automatic success**—no test is rolled!

### Situational Modifiers (GM Adjudication)
Beyond distance, the Game Master has complete flexibility to award situational Upgrades or Downgrades based on creative player tactics, deployed gear, and environmental conditions. Rather than consulting a rigid index, the GM evaluates the scene narratively:
* **Concealment & Obscurance:** Deploying a smoke canister, cutting station lighting, or vanishing into heavy steam can impose 1 or 2 Downgrades on pursuers lacking thermal sensors.
* **Physical Barriers:** Slamming a hydraulic blast door, scattering caltrops, or dropping cargo crates can impose a Blocker Effect or force pursuers to overcome a Shroud before they can follow.
* **Class Features:** Operatives leveraging signature features—such as a Hazard's chemical screen, a Shadow's optical cloak, or a Pilot's emergency thrust injection—should be rewarded with Upgrades, Downgrades, or Blocker Effects fitting the scale of their action.
* **Terrain:** Labyrinthine back-alleys or dense civilian markets might grant the quarry an Upgrade if they know the layout, while wide, brightly lit concourses might grant an Upgrade to pursuers with clear lines of sight.

---

## Teamwork & Cell Escapes

When an entire Corsair cell flees on foot, they sink or swim together. Corsair's core **Teamwork** rules govern group flights:

```
+---------------------------------------------------------------------------------------------------------+
|                                    TEAMWORK CELL ESCAPE RESOLUTION                                      |
+---------------------------------------------------------------------------------------------------------+
| 1. AP COMMITMENT                                                                                        |
|    Each fleeing operative in the cell spends 1 Place-to-Place AP.                                       |
|                                                                                                         |
| 2. SIMULTANEOUS ACTION ROLLS                                                                            |
|    Every operative rolls their designated Attribute Pair (e.g., Silas rolls Agility + Instinct;        |
|    Jax rolls Agility + Strength; Tessa rolls Mobility + Agility with her jetpack).                      |
|                                                                                                         |
| 3. TEAMWORK DICE SWAP                                                                                   |
|    Before pursuers roll, the operatives can swap any number of dice between their pools. A swift runner |
|    can pass high dice to a heavier, slower teammate, ensuring the entire crew maintains pace.           |
|                                                                                                         |
| 4. PURSUER CONTEST & HIT ELIMINATION                                                                    |
|    Each pursuer who spends 1 Place-to-Place AP rolls their own separate contest pool! Each Hit (8+)     |
|    scored by each pursuer eliminates the highest die from the quarry's roll (or can be targeted         |
|    against a specific fleeing cell member).                                                             |
|                                                                                                         |
| 5. SEPARATION OR COLLECTIVE STAND                                                                       |
|    If an operative has all their 8+ dice eliminated, they are caught! The remaining cell members must   |
|    decide: leave their comrade behind, or turn back and enter the intercepted Moment-to-Moment combat   |
|    alongside them!                                                                                      |
+---------------------------------------------------------------------------------------------------------+
```

---

## Macro Pursuits: The Place-to-Place Manhunt (Hideout & Heat)

In the hard-vacuum realism of the Sphere, breaking immediate visual contact or ducking into an asteroid's radar shadow does not mean a fugitive has vanished from the cosmos. Sensor telemetry persists, surveillance archives record transit corridors, transponder pings echo across orbital beacons, and station marshals seal sector bulkheads. A successful getaway in Moment-to-Moment tactical combat represents **tactical disengagement**, not **strategic disappearance**. 

Once an escapee breaks tactical contact, the pursuit transitions into a **Place-to-Place Manhunt**. Operating in Place-to-Place pacing (where each round spans **15 to 30 minutes** and each Action Point represents roughly **5 to 10 minutes** of macro legwork), the chase shifts from raw athletic reflexes to operational tradecraft, surveillance, and forensic legwork.

Every Place-to-Place manhunt is governed symmetrically by two unified mechanics: **Hideout** (the Blocker Effect) and **Heat** (the ticking countdown clock).

```
+---------------------------------------------------------------------------------------------------------+
|                                      THE PLACE-TO-PLACE MANHUNT ENGINE                                  |
+------------------------------------+--------------------------------------------------------------------+
| 1. HIDEOUT (The Blocker Effect)    | 2. HEAT (The Countdown Track)                                      |
|    "How deep is the cover?"        |    "How long before the trail goes cold?"                          |
+------------------------------------+--------------------------------------------------------------------+
| Symmetrical Blocker pool (0–3+).   | Symmetrical Countdown Track (1–3 Rounds).                          |
| Hits Required = Hideout + 1.       | Decreases by 1 at the End of each Place-to-Place Round.             |
| Pursuers spend AP to strip it;     | Quarry spends AP to burn it (accelerate extraction);               |
| Quarry spends AP to fortify it.    | Pursuers spend AP to freeze it (deploy cordons & lock down gates). |
+------------------------------------+--------------------------------------------------------------------+
```

---

### 1. The Hideout Engine (The Blocker)

Mechanically, **Hideout** functions as a persistent **Blocker Effect** anchored to the fleeing quarry's physical sanctuary, digital anonymity, and social camouflage. Exactly like an NPC's **Determination** in [Social Negotiations](Social_Interactions.md) or **Lockdown** in [Investigation](Investigation_and_Exploration.md), pursuers cannot corner a suspect with a casual glance:

$$\text{Hits Required to Locate \& Corner} = \text{Hideout Rating} + 1$$

Pursuers must strip away every point of Hideout on a 1-for-1 basis using Hits (`8+`) rolled on investigative actions. Once the Hideout pool is reduced to zero, the very next Hit scored—whether rolled as an excess Hit on that same test or achieved on a subsequent action—cracks the quarry's sanctuary and pinpoints their location!

#### Seeding Hideout from a Tactical Escape
When a manhunt begins immediately following a successful tactical getaway, the quarry's initial **Hideout Rating** is directly seeded by the **net surviving Hits (`8+`)** from their escape roll:

* **Hideout 1 (Shallow Cover / Hot Trail):** The quarry retained **1 surviving Hit**. A frantic, messy escape under fire. The quarry ducked around a corner, took an obvious elevator, or left a faint thermal plume. Pursuers know the rough direction of flight or caught a partial transponder chirp. Requires **2 total Hits** to crack.
* **Hideout 2 (Firm Cover / Standard Safehouse):** The quarry retained **2 surviving Hits**. A disciplined, textbook breakaway. The quarry melted into dense marketplace crowds, slipped through pressurized maintenance shafts, or cut their vehicle lights down a canyon run. Pursuers know the general sector but have lost direct telemetry. Requires **3 total Hits** to crack.
* **Hideout 3+ (Deep Bunker / Ghosted):** The quarry retained **3 or more surviving Hits**. An extraordinary, flawless vanishing act. The quarry scrubbed their transponder mid-flight, deployed thermal baffles into an asteroid crevasse, or reached a fortified, pre-staged bolt-hole. Requires **4 or more total Hits** to crack.

#### Setting Hideout In Situ (Cold Manhunts)
When an investigation or manhunt begins without an immediate preceding chase (such as tracking down a suspect who skipped bail yesterday or hunting an infiltrator through a sprawling corporate facility), the Game Master calibrates Hideout based on the quarry's tradecraft and resources:

* **Hideout 0 (Amateur / In Plain Sight):** A panicked corporate clerk or drunk mercenary stumbling through open plazas. Requires a standard **Simple Test (1 Hit)** to run down.
* **Hideout 1 (Improvising Runner):** A low-level smuggler diving into back alleys and paying off dockworkers on the fly. Requires **2 total Hits** to locate.
* **Hideout 2 (Professional Operative — Standard Baseline):** A trained syndicate courier, bounty hunter, or covert agent with pre-planned fallback routes, burner communicators, and local sympathizers. Requires **3 total Hits** to locate.
* **Hideout 3+ (Ghost / Master Infiltrator):** A deep-cover intelligence officer, Shadow specialist, or corporate phantom utilizing biometric scramblers, encrypted dummy servers, and air-gapped safehouses. Requires **4+ total Hits** to crack.

---

### 2. The Heat Engine (The Countdown Clock)

While Hideout measures the depth of the quarry's concealment, **Heat** measures the operational lifespan, resource commitment, and urgency of the pursuit. In accordance with *Corsair's* [Time Management rules](Time_Management.md), encounter countdown tracks made up on the fly are calibrated to **1, 2, or at most 3 rounds** in Place-to-Place pacing (~15–30 minutes per round):

* **Heat 1 (Immediate Flash Window / 1 Round, ~15–20 minutes):** Local gang enforcers with no regional reach, private security guards unwilling to pursue off corporate property, or an escapee whose extraction shuttle is idling on the launch pad and launches at the end of the round.
* **Heat 2 (The Tactical Standard / 2 Rounds, ~30–45 minutes):** Standard station precinct marshals, corporate strike teams, or syndicate hit squads deploying coordinated sweeps, camera audits, and sector checkpoints. This is the baseline duration for most dramatic manhunts.
* **Heat 3 (Extended Dragnet / 3 Rounds, ~60–90 minutes):** A planetary authority dragnet, naval sector interdiction, or station-wide lockdown complete with aerial scanner drones, sealed transit lines, and armed perimeter cordons.

#### The Universal End-of-Round Pulse
At the **End of each Place-to-Place Round**, time moves forward, and **Heat decreases by 1 segment** (`[2]` &rarr; `[1]` &rarr; `[0]`).

#### When Heat Reaches Zero
If Heat reaches `[0]` before pursuers eliminate all Hideout points and land the final locating Hit:
* **When PCs are the Quarry:** **The Heat Dies Down!** The perimeter cordon collapses, security shifts rotate out, or the crew boards their extraction craft and clears the sector. The quarry achieves a clean, permanent macro escape.
* **When PCs are the Pursuers:** **The Trail Goes Cold!** The target boards a scheduled commercial transport, burns sub-light out of station sensor range, or melts into the millions of nameless laborers in the deep sprawl. The immediate opportunity to corner the suspect is lost.

---

### 3. Place-to-Place Operational Actions (3 AP Pool)

In Place-to-Place pacing, every operative and pursuer manages their standard pool of **3 Action Points** per round (~5–10 minutes of concentrated activity per AP). This creates a dynamic, high-stakes duel between the hunters and the hunted.

```
+---------------------------------------------------------------------------------------------------------+
|                                    PLACE-TO-PLACE MANHUNT ACTIONS (3 AP)                                |
+-------------------+-----------------------------------+-------------------------------------------------+
| Actor             | Operational Action (1 PtP AP)     | Mechanical Resolution & Impact                  |
+-------------------+-----------------------------------+-------------------------------------------------+
| PURSUERS          | Forensic Audit & Camera Slicing   | Simple Test (Knowledge + Instinct or Hacking):  |
| (Hunting)         | (Reviewing CCTV, biometric logs)  | Each Hit strips 1 point of Hideout.             |
|                   +-----------------------------------+-------------------------------------------------+
|                   | Street Canvassing & Interrogation | Simple Test (Presence + Instinct or Presence):  |
|                   | (Shaking down dockers, informants)| Each Hit strips 1 point of Hideout.             |
|                   +-----------------------------------+-------------------------------------------------+
|                   | Drone & Sensor Sweeps             | Simple Test (Knowledge + Finesse or Instinct):  |
|                   | (Acoustic hounds, infrared scans) | Each Hit strips 1 point of Hideout.             |
|                   +-----------------------------------+-------------------------------------------------+
|                   | Deploy Cordon / Lockdown Gates    | Simple Test (Presence + Knowledge or Hacking):  |
|                   | (Sealing transit lines, bulkheads)| 1 Hit FREEZES Heat (does not drop this round)!  |
+-------------------+-----------------------------------+-------------------------------------------------+
| QUARRY            | Electronic Spoofing & Scrubbing   | Simple Test (Knowledge + Finesse or Hacking):   |
| (Fleeing)         | (Purging feeds, false beacons)    | Each Hit adds +1 to Hideout.                    |
|                   +-----------------------------------+-------------------------------------------------+
|                   | Social Camouflage & Disguises     | Simple Test (Presence + Finesse or Knowledge):  |
|                   | (Forged passes, worker overalls)  | Each Hit adds +1 to Hideout.                    |
|                   +-----------------------------------+-------------------------------------------------+
|                   | Convoluted Routes & False Leads   | Simple Test (Instinct + Agility or Finesse):    |
|                   | (Steam conduits, jumping lines)   | Each Hit adds +1 to Hideout.                    |
|                   +-----------------------------------+-------------------------------------------------+
|                   | Accelerate Extraction             | Simple Test (Presence + Presence or Knowledge): |
|                   | (Bribing pilot for emergency burn)| 1 Hit BURNS 1 Heat immediately off the clock!   |
+-------------------+-----------------------------------+-------------------------------------------------+
```

#### Modulating the Clock: Freezing vs. Burning Heat
While Heat ticks down naturally at the End of the Round, disciplined actions allow both sides to manipulate the timeline:
* **Burning Heat (Quarry Fast-Track):** Rather than hunkering down to build Hideout, a fleeing quarry can commit an AP to rush their departure—bribing a freighter pilot for an immediate un-docking burn, overriding an automated monorail express line, or firing emergency thrusters. Scoring a Hit on this test **immediately burns 1 point of Heat off the clock**, drastically tightening the window before pursuers can sweep their sector!
* **Freezing Heat (Pursuer Cordon):** Pursuers can spend an AP coordinating with station authorities, broadcasting Flotilla warrants, or hacking transit relays to seal sector blast doors and ground civilian transports. Scoring a Hit on this test **freezes the Heat Clock**, preventing it from dropping at the End of that Round and granting the hunters vital extra time to comb the district.

---

### 4. Resolving Interception: The Safehouse Raid

If the pursuing party successfully clears all points of the quarry's Hideout and lands the final locating Hit before Heat reaches zero, the quarry is cornered:

1. **Zooming In to Moment-to-Moment:** Play immediately drops back into **Moment-to-Moment tactical combat** at the quarry's physical hiding place (e.g., an industrial chop-shop, a back-alley safehouse, a cargo freighter's airlock waiting room, or a maintenance conduit).
2. **Universal AP Refill:** All participants refill their tactical Action Points to their maximum (**3 AP**).
3. **Pursuers Take Immediate Initiative:** The pursuers hold the operational momentum. **The pursuers act first**, taking the opening turn of the new tactical engagement.
4. **Pursuers Dictate Tactical Geometry:** Having run the quarry to ground through disciplined investigation, the pursuers control the battlefield layout:
   * Breaching the safehouse from multiple entry doors or cutting torches through ceiling vents.
   * Establishing a fortified containment perimeter outside the only exit vector.
   * Claiming Heavy Cover while leaving the surprised quarry trapped in the room.

---

## Complete Narrative Walkthrough: The Zenith Warrant

To see how all the pieces of the pursuit engine fit together in live play, follow this complete step-by-step example featuring **Silas**, **Tessa**, and **Jax**—a commissioned Corsair cell executing a high-stakes Flotilla warrant across Port Zenith.

### The Situation
Acting under an inter-jurisdictional seizure warrant issued by the Flotilla Admiralty, the Corsairs have raided an unregistered warehouse depot in the industrial underbelly of Port Zenith run by the "Iron Fang" syndicate, an illegal Precursor weapons-trafficking ring. The cell breaches the facility, secures a stolen military-grade Precursor focusing coil, and corners the syndicate's chief courier, **Kaelen**.

Before they can slap magnetic binders on Kaelen, the syndicate's heavy mercenary strike team breaches the lobby with military-grade auto-sluggers. Outnumbered and facing heavy suppression fire, the Corsairs must conduct an orderly tactical withdrawal through the concourse to reach their patrol rover.

---

### Phase 1: Disengagement on Foot (Tactical Withdrawal Under Fire)

> **1. Establishing Clearance & Guardrails:**
> Facing overwhelming automatic fire, Silas provides cover with his marksman rifle, Tessa secures the evidence lockbox, and Jax readies his boarding axe.
> * On their turns in Moment-to-Moment combat, Jax uses **1 AP** to shove an aggressive syndicate mercenary back, clearing CQC.
> * Tessa spends **1 AP** to ignite a **Smoke Canister** from her utility rig, blanketing the corridor in dense chemical aerosol.
> * Silas, Tessa, and Jax spend their remaining Moment-to-Moment AP sprinting down the corridor into an adjoining transit concourse, putting **7 spaces (28 meters)** of distance between themselves and the mercenaries.
> * The GM checks the Guardrails of Disengagement:
>   * *Tactical Clearance:* 7 spaces (Outside CQC / same space; positioned at Medium Range). **Satisfied.**
>   * *Vector:* Concourse blast doors are open to the civilian transit terminal. **Satisfied.**
>   * *Mobility:* All three operatives are upright, unrestrained, and mobile. **Satisfied.**

> **2. Committing Place-to-Place AP:**
> Silas calls over the comms, *"Fall back to the transit gate! Don't let them pin us down!"*
> * Silas, Tessa, and Jax each spend **1 Place-to-Place AP** from their broader operational pools to initiate a **Teamwork Cell Escape**.
> * Two syndicate mercenaries charge through the smoke, spending **1 Place-to-Place AP each** to give chase.

> **3. The Contested Foot Roll & Teamwork Swap:**
> * Silas rolls **Agility (3) + Instinct (4)** = 4d10: `[3, 5, 8, 9]`. (Two Hits: 8, 9).
> * Tessa rolls **Agility (4) + Instinct (3)** = 4d10: `[4, 6, 7, 7]`. (Zero Hits!).
> * Jax rolls **Agility (3) + Strength (5)** = 5d10: `[2, 4, 8, 8, 10]`. (Three Hits: 8, 8, 10).
> * Because Tessa rolled zero Hits while shielding the evidence lockbox, she is lagging behind. The Corsairs utilize **Teamwork Dice Swapping**! Jax passes one of his `8`s to Tessa, and Silas passes his `8` to Tessa, taking her unneeded `7`s.
> * Final Cell Pools: Silas `[3, 5, 7, 9]`, Tessa `[4, 6, 8, 8]`, Jax `[2, 4, 7, 8, 10]`. Every operative now holds at least one Hit!

> **4. The Pursuers' Contest:**
> Because Tessa deployed a smoke canister across the threshold, the GM rules that the syndicate pursuers suffer **1 Downgrade** to their contest rolls, stepping one d10 down to a d8.
> Both mercenaries have **Agility (4) + Instinct (3)** = 4d10 base pool. With the Downgrade, each rolls 3d10 and 1d8:
> * **Mercenary A** rolls: `[2, 5, 8]` on the d10s and `3` on the d8. That is **one Hit (8)**.
> * **Mercenary B** rolls: `[4, 6, 7]` on the d10s and `5` on the d8. That is **zero Hits**.
> * With one total Hit scored across both pursuers, the mercenaries eliminate the highest die from Silas's pool (the `9`).
> * Silas still retains an un-eliminated `7`, while Tessa retains `[8, 8]` and Jax retains `[8, 10]`.
> * Jax hauls Silas through the transit security gate as Tessa triggers the emergency override, slamming the armored turnstiles shut behind them and severing the mercenaries' visual pursuit! **Clean Escape on Foot!**
> * **Transitioning to Place-to-Place (Hideout & Heat):** With four net Hits surviving across the cell (`8, 8, 8, 10`), the Corsairs establish a formidable **Hideout 3** buffer against the street mercenaries. Furthermore, because these are localized warehouse thugs lacking station-wide authority, the GM assigns the pursuit **Heat 1 (~20 minutes)**. The Corsairs spend their next Place-to-Place AP riding the high-speed transit line down to the lower freight yard, cleanly outlasting the Heat before the syndicate can organize a search!

---

### Phase 2: Vehicular Pursuit of the Syndicate Courier (Corsairs as Pursuers!)

The transit car drops the cell at the lower freight yard where their customized patrol rover is stationed. But as they exit the terminal, they spot **Kaelen**, the syndicate courier, peeling out of an industrial garage in a high-speed combat buggy laden with the rest of the smuggled weapons cache!

> **1. The Vehicular Escape Declaration:**
> Kaelen attempts an escape across the wide asphalt freight yard, starting 10 spaces away (Medium Range).
> * Kaelen (the criminal quarry) spends **1 Place-to-Place AP** to gun his buggy's supercharged turbine.
> * Tessa leaps behind the wheel of the Corsairs' patrol rover and spends **1 Place-to-Place AP** to give chase! Silas and Jax pay **0 AP**, boarding the passenger seats with firearms readied.
> * Because both sides are in motorized vehicles, the Foot-to-Vehicle invariant is satisfied.

> **2. The Test Across Crowded Freight Yards:**
> The chase barrels through dense shipping container stacks. Because the yard is narrow and labyrinthine, the GM calls for **Maneuvering + Instinct**.
> * Kaelen rolls **Maneuvering 3 + Instinct 3** = 3d10: `[5, 7, 9]`. One Hit (the `9`).
> * Tessa rolls **Maneuvering 3 + Instinct 3** = 3d10 base pool.
> * Silas leans out the rover's passenger window and fires a burst of precision suppressive fire into the buggy's rear tires, successfully activating an **Upgrade Effect** to assist Tessa's driving.
> * Tessa rolls 2d10 and 1d12 (upgraded): `[5, 7]` on the d10s and an `11` on the upgraded d12! A decisive Hit!

> **3. The Corsairs Intercept the Courier:**
> As the pursuing party, the Corsairs' Hits eliminate the quarry's dice:
> * Tessa's `11` eliminates Kaelen's highest die (the `9`).
> * Kaelen has no remaining 8+ dice! **The criminal courier's escape attempt fails!**

> **4. Resolving the Violent Interception:**
> Tessa surges alongside the buggy and executes a textbook PIT maneuver, clipping the rear quarter-panel and spinning Kaelen's buggy violently into a reinforced cargo bulkhead.
> * **Moment-to-Moment Resumes:** The scene immediately drops back into Moment-to-Moment tactical combat around the crashed buggy.
> * **AP Refill:** Silas, Tessa, Jax, and Kaelen all refill their tactical AP to maximum (**3 AP**).
> * **Pursuers Take Immediate Initiative:** **The Corsairs act first!**
> * **Pursuers Place Themselves:** As the successful pursuers, the Corsairs dictate the tactical geometry! Tessa angles the armored rover across the alley mouth, completely blocking Kaelen's exit vector. Jax dismounts into Heavy Cover with his boarding axe, and Silas claims high ground on an adjacent container with his rifle trained directly on the smoking buggy cockpit, shouting: *"Flotilla Corsairs! Cut the ignition and step out with your hands up!"*
> * Cornered and facing superior tactical positioning, Kaelen surrenders. The Corsairs secure the suspect in magnetic cuffs and impound the contraband ordnance!

---

### Phase 3: The Orbital Intercept Burn

With Kaelen in custody and the seized Precursor coil locked in the rover's vault, the Corsairs reach Port Zenith's outer launch pad and board their light frigate, the *Kestrel*, to transport the prisoner and evidence to the Flotilla battlecruiser *Iron Bastion*.

As the *Kestrel* clears station space into low orbit, the syndicate's offshore pirate gunship—the *Viper's Talon*—drops out of high orbit to ambush the *Kestrel* and eliminate Kaelen before he can testify!

> **1. Macro-Grid Positioning:**
> The *Kestrel* clears the station envelope onto the **Macro-Grid (1 km hexes)** outside Dogfight Mode, starting 2 hexes away from the pirate gunship. All clearance guardrails are met.
> * Tessa, at the helm, declares an orbital escape burn toward the Flotilla battlecruiser's patrol lane, spending the ship's **1 Place-to-Place AP**.
> * The pirate gunship commits **1 Place-to-Place AP** to pursue and interdict.

> **2. The Escape Burn Roll & G-Strain:**
> In the open void, the test uses **Acceleration + Acceleration**.
> * The *Kestrel* has an **Acceleration of 7**. Tessa pushes the fusion drive to emergency military thrust!
> * Tessa rolls 7d10: `[1, 3, 5, 8, 8, 9, 10]`. That is **four Hits** (`8`, `8`, `9`, and `10`)!
> * **G-Strain in Pursuit:** Because each Hit scored on an orbital burn inflicts **2 Light Wounds (2 LW)** of G-Strain, the extreme multi-g acceleration inflicts **8 Light Wounds** (4 Hits × 2 LW) on everyone aboard. Silas, Tessa, Jax, and their prisoner in the holding cell are pinned helplessly into their crash couches, blood pooling in their extremities under brutal G-forces!

> **3. The Pirate Gunship Contests:**
> The pirate gunship has an **Acceleration of 6**. Its pilot rolls 6d10: `[2, 4, 6, 7, 8, 9]`. Two Hits (`8` and `9`).
> * The pirate gunship's two hits eliminate the *Kestrel*'s `10` and `9`.
> * The *Kestrel* still retains two un-eliminated Hits (`8` and `8`)!
> * **Clean Orbital Escape!** The *Kestrel*'s fusion plume blazes against the black, breaking past the pirate's missile tracking envelope and leaping into the protective patrol line of the Flotilla fleet. The prisoner and contraband are delivered safely into custody, and the Corsairs have successfully executed their mandate!

---

## Chapter Summary & Quick Reference

* **The Escape Action:** Costs **1 Place-to-Place AP** and ends your current tactical turn. In vehicles and ships, 1 pilot pays for the entire vessel. On foot, groups coordinate via **Teamwork Cell Escapes**.
* **The Guardrails:** (1) Tactical Clearance (outside CQC / 0 spaces and unrestrained); (2) Open egress vector; (3) Operational mobility (conscious, unrestrained; starships must break out of Dogfight Mode onto the Macro-Grid first).
* **Pursuer Commitment:** Pursuers must spend **1 Place-to-Place AP** to give chase and contest; each pursuer rolls their own separate contest pool. If pursuers cannot or will not give chase, the quarry escapes automatically.
* **Distance Modifiers:** CQC (cannot escape); Short Range (quarry 2 Downgrades / pursuers 2 Upgrades); Medium Range (no mod); Long Range (quarry 2 Upgrades / pursuers 2 Downgrades); Extreme Range (automatic escape).
* **Failure Penalty:** Scene drops to Moment-to-Moment combat with full AP refills. Pursuers take **immediate initiative** and **place themselves anywhere** relative to the quarry (in starships, pursuers enter Dogfight Mode at Advantage Position 8–10).
* **Modes of Pursuit:** Foot uses **Agility + Instinct** (or gear **Mobility**); Vehicles use **Acceleration** (open) or **Maneuvering + Instinct** (crowded) and cannot be chased on foot; Starships use **Acceleration** or **Maneuvering + Instinct** with G-Strain inflicting 2 LW per Hit scored on orbital burns.
* **The Place-to-Place Manhunt:** Clean escapes transition to a macro manhunt governed by **Hideout** (the Blocker) and **Heat** (the ticking clock), where characters spend **3 Place-to-Place AP** per round.
* **Hideout (The Blocker):** $\text{Hits Required to Intercept} = \text{Hideout Rating} + 1$. Seeded dynamically by surviving escape hits (1–3+) or set by the GM (0–3+). Stripped by pursuer search tests (1 Hit = -1 Hideout); fortified by quarry tradecraft tests (1 Hit = +1 Hideout).
* **Heat (The Clock):** A countdown track of **1 to 3 Place-to-Place rounds** (2 rounds is standard). Decreases by 1 at the End of each Round. Reaching 0 means Heat dies down / the trail goes cold (clean macro escape). The quarry can spend AP to burn Heat; pursuers can spend AP to freeze Heat.
* **Safehouse Raid (Interception):** If pursuers clear all Hideout points and land the final locating Hit before Heat reaches 0, the scene zooms into Moment-to-Moment combat (Raid/Ambush) with pursuers acting first and choosing battlefield layout.
