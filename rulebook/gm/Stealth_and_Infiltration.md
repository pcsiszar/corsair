# Stealth & Infiltration

In *Corsair*, infiltration is never reduced to a single binary die roll that ends in either effortless invisibility or a base-wide firefight. Covert operations are dynamic tactical dilemmas governed by positioning, time management, sensory coverage, and active counter-measures. Whether operatives are creeping through the pressurized conduits of an orbital shipyard, bluffing their way past security checkpoints in forged corporate attire, or slicing surveillance relays to blind an automated kill-box, stealth operates on the same core mechanical engines as combat and social negotiations: **Action Points**, **Pacing Tiers**, **Blocker Effects**, and **Activating Actors**.

This guide provides Game Masters with a unified, comprehensive framework to run high-tension stealth operations, security breaches, and alarm escalations across the Sphere.

---

## 1. Hiding & Sneaking

Sneaking represents the deliberate act of moving unseen and unheard through hostile territory. In *Corsair*, an operative does not roll merely to "be hidden" while stationary behind cover; if a character breaks line of sight and sits motionless behind a solid bulkhead outside sensor coverage, they are inherently hidden. Tests are required when taking active risks: traversing open killzones, crossing patrolled corridors, moving quietly past acoustic sniffers, or rushing between cover points.

When an operative moves stealthily, the core assumption is that they are transitioning from one concealed position to another.

```
+-------------------------------------------------------------------------------------------------------------+
|                                           STEALTH MOVEMENT MATRIX                                           |
+-------------------+----------------------+------------------------+-----------------------------------------+
| Pacing Tier       | Test Type            | Movement Rate          | Primary Resolution Focus                |
+-------------------+----------------------+------------------------+-----------------------------------------+
| Moment to Moment  | Complex Test         | 2 SP per meter (Half)  | Action Roll ensures silence/cover (8+). |
|                   |                      | 1 SP per meter (Full)* | Success Roll allocates movement meters. |
|                   |                      | *Incurs 2 Downgrades   | Extra Hits bank Blockers or Downgrades. |
+-------------------+----------------------+------------------------+-----------------------------------------+
| Place to Place    | Simple / Contested   | Room / Sector Traverse | Overcoming patrol cycles, sweeps, and   |
|                   | Test                 | (1 AP per sector)      | transit corridors across minutes.       |
+-------------------+----------------------+------------------------+-----------------------------------------+
```

### Moment to Moment Stealth: The Complex Movement Test

During tactical **Moment-to-Moment** play (where rounds last roughly 10 to 15 seconds and each AP represents 3 to 5 seconds of physical effort), slipping between cover positions is resolved as a **Complex Test** costing **1 AP**.

The test pairs physical coordination and situational awareness, using a combination of **Finesse**, **Instinct**, and **Agility**:
* **Agility + Finesse**: Used for cautious physical creeping, dampening footfalls, controlling joint movement, and navigating narrow ventilation ducts.
* **Agility + Instinct**: Used for rapid dashes across corridors, timing sightlines, reading patrol rhythms, and darting into sensor blind spots.

#### Step 1: The Action Roll (Ensuring Concealment)
The operative rolls a number of dice equal to the **higher** Attribute in the pair.
* If the highest die is **7 or lower**, the Action Roll **fails**. The movement stalls or the operative is caught off-balance in partial cover. The spent **1 AP is lost**, and the nearest unaware sentry becomes **Alerted as an Activating Actor** for the GM's upcoming turn.
* If at least one die shows **8 or higher (a Hit)**, the Action Roll **succeeds**. The operative moves cleanly without exposing their silhouette or generating alarming noise. They immediately advance to the Success Roll.

#### Step 2: The Success Roll (Allocating Movement)
The operative gathers dice equal to the **lower** Attribute in the pair from their successful roll. The highest die among these selected dice provides their base **Success Points (SP)**, which determine how many meters the character can traverse:
* **Half Speed (Cautious Creeping):** Costs **2 Success Points per meter** moved. An operative who rolls 6 Success Points can creep up to 3 meters into new cover; 8 Success Points yields 4 meters.
* **Full Speed (Rushing):** If the operative declares they are moving at full speed (costing **1 Success Point per meter**, up to standard 4 meters per AP), the test suffers **2 Downgrades** to reflect the increased acoustic profile and exposed posture.

#### Step 3: Banking Hits for Defensive Camouflage
If the operative rolled additional Hits (dice showing 8+) beyond the initial success on their Action Roll or Success Roll, those excess Hits can be deployed strategically:
* **Banking Blocker Effects:** In strict accordance with the core rules for Blocker Effects, the operative spends **2 excess Hits per set-aside Blocker Hit** to hinder enemy search actions at their destination. Each set-aside Blocker Hit eliminates the highest die from an adversary's test attempting to spot them while they remain stationary in that spot.
* **Banking Downgrade Effects:** The operative spends **1 excess Hit per Downgrade** to impose **Downgrade Effects** on search tests targeting that position.
* **Crit Effects for Distance:** On the Success Roll, an operative can spend excess Hits on a **Crit Effect** (+2 Success Points per Hit spent) to extend their creeping distance across wider gaps.

```
+---------------------------------------------------------------------------------+
|                       EXPIRATION & CARRYOVER OF BANKED DICE                     |
+---------------------------------------------------------------------------------+
| 1. Positional Blockers Expire on Movement: Banked Blocker Effects are anchored  |
|    strictly to the physical cover and shadows of that specific location. When   |
|    the operative moves away from that hiding spot, all banked Blockers at that  |
|    position are immediately lost.                                               |
| 2. Upgrade / Downgrade Carryover: Any banked Downgrade dice on enemy perception |
|    that were not triggered or consumed before the operative moves again are      |
|    converted into Upgrades (+d12) on the operative's very next stealth action.  |
+---------------------------------------------------------------------------------+
```

---

### Adversary Behavior: Unaware vs. Alerted NPCs

The Game Master does not roll constant, repetitive perception checks for every guard on the map. Adversaries fall into two operational states:

#### 1. Unaware NPCs
Guards following standard patrol routes, monitoring screens casually, or chatting by a water recycler are **Unaware**. 
* Unaware NPCs **do not actively roll to search for characters**.
* During the GM's turn, Unaware NPCs follow their fixed patrol route, stand guard, or converse, and **pass their turn automatically**. They do not spend Action Points hunting for hidden operatives.

#### 2. Alerted NPCs
An NPC becomes **Alerted** when an operative fails a stealth test, trips an unsuppressed sensor, or generates suspicious acoustic or visual disturbances.
* Alerted NPCs actively spend their **Action Points (AP)** on their turn to locate and spot intruders.
* **Searching on the Grid:** When operating in **Moment to Moment** on a tactical grid, an Alerted NPC spends **1 AP** to perform an active search test (**Instinct + Instinct** or **Instinct + Knowledge**), designating a search zone strictly **within their Short Range (up to 12 meters)**.
* **Detection Threshold:** A **single Hit (8+)** on the search test spots one hidden character within line of sight in that designated search zone, **unless** that Hit is negated by the character's banked **Blocker Effects** or stymied by **Downgrades**.
* If the search test yields no un-negated Hits, the operative remains undetected in the shadows.

---

### Failed Stealth Tests: The Activating Actor Principle

When an operative fails a stealth test (scoring 0 Hits on their Action Roll), the GM must **never** grind the scene to a screeching halt or arbitrarily trigger an instantaneous base-wide alarm out of turn. Instead, *Corsair* enforces the **Activating Actor** principle:

1. **AP Lost:** The primary penalty is the loss of the spent **1 AP**. In tight tactical situations, losing 1 of your 3 AP is a serious operational setback.
2. **Exposed Position:** The character is caught between cover points, stumbles into a loose grating, or casts a visible shadow on a far bulkhead.
3. **Actor Activated:** The nearest Unaware sentry hears the scrape or notices the shadow and flips to **Alerted**. The GM declares: *"Your mag-boot clips an exposed conduit with a dull clang. The patrol guard at the end of the gangway jerks their helmet toward your alcove."*
4. **Turn Economy Preserved:** The sentry does not act instantly out of turn. The sentry is now an **Activated Actor for the GM's upcoming turn**. Because control only passes to the GM after the active player side spends 2 or more AP, the crew retains a crucial window of opportunity: an ally can spend an AP to create a distraction elsewhere, or the infiltrating operative can spend their remaining AP to dive into secondary cover or ready a suppressed takedown before the sentry takes their turn!

---

### Group Stealth & Teamwork

Infiltration often involves an entire cell moving together. Having every player roll individual stealth checks without support creates a statistical certainty of failure, disproportionately punishing heavily armored comrades.

To maintain fairness and reward coordination, group infiltration utilizes *Corsair's* standard **Teamwork** engine:
* **Coordination Cost:** Every operative participating in the coordinated move spends **1 AP** and declares their approach.
* **Simultaneous Rolls:** Each participant rolls their appropriate Attribute Pair (e.g., the scout rolls **Agility + Instinct**, while an armored Vanguard rolls **Agility + Finesse**).
* **Dice Swapping:** After rolling, participants in proximity can freely swap dice between their pools before finalizing results. A nimble scout who rolls multiple Hits can transfer high dice to a slower ally, effectively guiding their footfalls, timing their sprint, or muffling their gear.
* **Resolution:** 
  - Participants who retain at least one Hit (`8+`) complete their hidden movement into new cover.
  - If any operative still ends with **zero Hits** after all dice swapping is finalized, that specific operative stalls in partial cover and activates the nearest sentry as an Alerted Actor.

---

## 2. Disguises & Social Camouflage

Sneaking through shadows is not the only path into a fortified installation. In corporate complexes, orbital transit terminals, and industrial foundries, walking through the front entrance wearing a technician's jumpsuit, a security badge, or an executive courier uniform is often far more effective than crawling through air ducts.

```
+----------------------------------------------------------------------------------------------------+
|                                      DISGUISE SYSTEM OVERVIEW                                      |
+---------------------+------------------------------------------------------------------------------+
| 1. Preparation      | Simple Test (Knowledge + Finesse) during downtime or PtP planning.          |
|    Crafting Test    | Generates a Sustained Blocker rating: every 2 Hits buys 1 Sustained Blocker. |
+---------------------+------------------------------------------------------------------------------+
| 2. Authentic Props  | Stolen genuine badges, security chits, or uniforms grant +1 free Blocker.    |
|    & Tool Bonuses   | Specialized fabrication kits grant Upgrades (+d12) to the pre-crafting test. |
+---------------------+------------------------------------------------------------------------------+
| 3. MANTLE Frames    | HARD INVARIANT: MANTLE chassis CANNOT be disguised.                          |
|    Are Incompatible | Must be smuggled in separately (freight crates, shafts) and donned inside.  |
+---------------------+------------------------------------------------------------------------------+
| 4. Concealed Gear   | Concealing items under uniforms imposes Downgrades equal to their Load:      |
|    Load Penalty     | * Load 1/2 items = 0 Downgrades (stims, micro-tools, holdout blades).       |
|                     | * Load 1 items = 1 Downgrade each (sidearms, cyberdecks, scanners).          |
|                     | * Load 2 items = 2 Downgrades each (carbines, riot armor, heavy tools).      |
+---------------------+------------------------------------------------------------------------------+
| 5. Security Scrutiny| Inspectors roll an inspection test against the Sustained Blocker rating.     |
|    & Piercing       | Scrutiny does NOT wear down the disguise. An inspector must score strictly   |
|                     | MORE Hits than the Sustained Blocker rating to pierce the disguise.         |
+---------------------+------------------------------------------------------------------------------+
```

### Crafting a Disguise: The Preparation Test

A disguise is assembled prior to infiltration during **Place to Place** preparation or **Day to Day** downtime. The operative makes a **Simple Test** combining technical forgery, garment tailoring, and credential spoofing using **Knowledge + Finesse**:
* **Purchasing Sustained Blockers (2 Hits per Blocker):** In strict accordance with the core rules for **Blocker Effects** and **Persistent Blocker Effects**, Blockers cost **2 Hits per set-aside Blocker Hit** and are never derived from Success Points. For every two Hits (dice showing 8+) scored on the crafting roll, the operative purchases **1 Sustained Blocker** for the disguise (e.g., 2 Hits = 1 Sustained Blocker, 4 Hits = 2 Sustained Blockers).
* **Sustained Protection:** Mechanically, this functions as a **Persistent Blocker Effect**: security guards and automated terminals are merely observing, scanning, or inspecting credentials, so repeated routine scrutiny **does not wear down or degrade the disguise**. The disguise provides its full Blocker rating against every inspection test encountered.
* **Authentic Credentials:** Stealing genuine security badges, biometric identity chits, or official uniforms grants **+1 free Sustained Blocker** directly added to the disguise's rating.
* **Specialized Tools:** Using a dedicated *Disguise & Forgery Kit* or *Cyberdeck Credential Slicer* grants **Upgrades (+d12)** to the crafting test pool, maximizing the chance of rolling 8+ Hits.

### The MANTLE Chassis Invariant

Under the hard sci-fi constraints of *Corsair*, **MANTLE combat chassis cannot be disguised**. 

A MANTLE (*Modular Adaptive Neural Transmission Linked Equipment*) is a full-body, high-output neuro-cybernetic exoskeleton laced with external hydraulic cabling, thermal heat sinks, and reinforced armor plating. There is no trench coat, coverall, or medical smock in the Sphere capable of concealing a powered combat frame without arousing immediate alarm.

Operatives who rely on MANTLE chassis must solve this logistical puzzle tactically:
* The cell must smuggle their inert MANTLE frames into the facility through secondary freight channels, industrial garbage chutes, pressurized cargo crates, or exterior service conduits.
* Operatives infiltrate in civilian or maintenance disguises to secure the staging area, disable local perimeter sensors, and rendezvous with their smuggled chassis.
* Donning a MANTLE chassis requires securing an isolated compartment and spending operational time hooking up the spinal neuro-shunt before engaging in heavy combat.

### Concealing Weapons, Armor, and Gear

Concealing military-grade equipment beneath tailored coveralls or uniforms is exceptionally difficult. Every piece of equipment carried beneath a disguise adds bulk, printing, and unnatural weight, imposing **Downgrades to the disguise pre-crafting test equal to the item's Load**:
* **Load 1/2 Items:** Small items—such as holdout knives, micro-communicators, neuro-stims, or lock-bypass shims—are compact enough to slip into pockets and boot seams without penalty (**0 Downgrades**).
* **Load 1 Items:** Standard sidearms, electronic cyberdecks, magnetic grapples, and folding tools impose **1 Downgrade** each.
* **Load 2+ Items:** Submachine guns, long-barreled carbines, ballistic vests, and heavy toolkits impose **2 Downgrades** each.

Operatives must make hard tactical compromises: either carry minimal concealed gear to ensure an airtight disguise, or smuggle heavier armaments inside sealed maintenance toolboxes and rolling equipment bins.

---

### Security Scrutiny & Piercing the Disguise

While wearing a valid disguise, operatives move freely through matching facility sectors without rolling tests. However, when an operative passes through a biometric checkpoint, encounters a supervisor, or attempts to access a restricted sector, security personnel or automated identity terminals conduct an **Inspection Test**:
* The inspector rolls an appropriate test (typically **Instinct + Knowledge** for a suspicious guard, or a flat dice pool based on the terminal's security tier).
* **Sustained Absorption:** The disguise's **Sustained Blocker Rating** automatically eliminates incoming inspector Hits on a 1-for-1 basis. Because observers are merely scrutinizing the uniform and credentials, this Blocker rating does **not** degrade from encounter to encounter; it resets to its full value for every new inspection.
* **Clean Passage:** If the inspector's roll yields Hits equal to or fewer than the disguise's Sustained Blocker rating, all incoming Hits are eliminated. The inspector detects nothing amiss, waving the operative through or receiving a green confirmation light.
* **Piercing the Disguise:** An inspector only pierces the disguise if they roll **strictly more Hits than the disguise's Sustained Blocker rating in a single inspection**. For example, against a disguise with a Sustained Blocker rating of 2, an inspector who rolls 2 Hits is blocked completely; an inspector who rolls 3 Hits scores 1 net Hit, piercing the cover (e.g., the scanner displays a red mismatch, or the guard notices an expired authorization code).

#### What Happens When Cover Is Blown?
When an inspector pierces the disguise, that NPC immediately becomes an **Active Actor for the GM's upcoming turn**.

Rather than immediately opening fire or sounding a base-wide klaxon, the NPC acts according to their role, orders, and temperament:
* **The Social Interrogation:** In the vast majority of commercial and corporate settings, guards do not immediately assume an intruder is a lethal assassin. The guard steps forward with a hand on their holster: *"Hold on, technician. Your authorization chit expired two cycles ago. Put that tool case down and step over to the console."*
* **The Interrogation Engine:** The scene immediately zooms into a high-stakes **Social Interaction** (as detailed in Chapter 10: *Social Interactions & Negotiations*). The GM sets the guard's **Patience** clock (typically 1 to 2 rounds). Operatives have an immediate window to spend AP delivering convincing lies (**Presence + Knowledge**), offering bribes, showing fabricated emergency work orders, or executing a silent takedown before the guard's patience expires and an alarm is raised.
* **Hostile Sectors:** In black-ops research labs or active military red-zones, an alert sentry may skip social questioning entirely, spending their AP to draw a sidearm or trigger an alarm switch.

---

## 3. Security Measures: Locks, Traps & Sensors

Facilities across the Sphere protect their assets with layered physical and electronic obstacles. To prevent arbitrary rulings, *Corsair* categorizes all security measures into three distinct mechanical archetypes: **Passive Security**, **Active Security**, and **Sensory Equipment**.

```
+-------------------------------------------------------------------------------------------------------------+
|                                           SECURITY MEASURES MATRIX                                          |
+-------------------+--------------------+------------------------+-------------------------------------------+
| Security Type     | Mechanical Engine  | Example Obstacles      | How Operatives Interact & Bypass          |
+-------------------+--------------------+------------------------+-------------------------------------------+
| Passive Security  | Lockdown Rating    | Electronic deadbolts,  | Simple Test using Finesse + Locksmith or  |
|                   | (Blocker Effect)   | encrypted terminals,   | Knowledge + Hacking. Must score Hits      |
|                   |                    | reinforced bulkheads   | equal to Lockdown Rating + 1.             |
+-------------------+--------------------+------------------------+-------------------------------------------+
| Active Security   | Activating Actors  | Laser tripwires,       | Disarmed via Finesse + Tinkering before   |
|                   | (Triggered AP)     | automated turrets,     | triggering. Triggering activates the trap |
|                   |                    | electrified floor grids| to spend its AP on its preset action.     |
+-------------------+--------------------+------------------------+-------------------------------------------+
| Sensory Equipment | Stacking Stealth   | Optical cameras,       | Blinded or spliced via Knowledge + Hacking|
|                   | Downgrades         | thermal sniffers,      | or Finesse + Tinkering. Stacks Downgrades |
|                   |                    | acoustic microphones   | on all stealth tests in monitored zone.   |
+-------------------+--------------------+------------------------+-------------------------------------------+
```

### 1. Passive Security: The Lockdown Rating

Passive security consists of stationary, unthinking barriers designed to deny physical or electronic entry: mechanical tumbler locks, magnetic door clamps, digital credential pads, encrypted databanks, and reinforced blast doors.

Passive security measures possess a **Lockdown Rating** that functions exactly like an NPC's **Determination** in social encounters:
* **Lockdown 0 (Standard Commercial):** Basic access doors, residential locks, and public terminals. Requires a standard **Simple Test** scoring **1 Hit** to bypass.
* **Lockdown 1 (Restricted / Professional):** Corporate office doors, secure storage lockers, and maintenance hubs. Possesses 1 point of Lockdown, requiring **2 total Hits** to bypass.
* **Lockdown 2 (High Security / Military):** Armory vaults, research lab bulkheads, and server core gateways. Possesses 2 points of Lockdown, requiring **3 total Hits** to bypass.
* **Lockdown 3+ (Precursor Vault / Black Site):** Deep-vault blast doors, quantum-encrypted terminal nodes. Requires **4 or more total Hits** to crack.

#### Bypassing Passive Security
Operatives spend **1 AP** to interface with the lock:
* **Physical & Mechanical Locks:** Bypassed using **Finesse + Locksmith** (using lock-picks, tension wrenches, or acoustic stethoscopes from a *Mechanic's Kit*).
* **Electronic & Digital Locks:** Bypassed using **Knowledge + Hacking** (using a *Cyberdeck*, electronic bypass shims, or terminal splicers).

Each Hit (`8+`) scored on the bypass test strips away 1 point of the lock's Lockdown rating. The final Hit unlocks the door or decrypts the terminal. If the operative's initial roll scores multiple Hits, the excess Hits immediately clear the remaining Lockdown and open the mechanism on that same action.

---

### 2. Active Security: Traps & Automated Defenses

Active security measures are reactive hazards engineered to incapacitate or kill unauthorized personnel: infrared laser tripwires, pressure-sensitive landmines, automated ceiling defense turrets, and high-voltage electrified floor plates.

Active security measures do not make continuous rolls; they function as **Activating Actors triggered by specific conditions**:
* **The Trigger:** Crossing an invisible laser line, stepping on a concealed floor plate, or cutting the wrong wire on a maintenance junction.
* **Execution:** The instant the trigger condition is met, the security measure becomes an **Active Actor**. On its activation, it spends its available Action Points strictly on its single, pre-determined action:
  - *Laser Tripwire:* Triggers a local alarm relay and drops emergency fire curtains (1 AP).
  - *Proximity Frag Mine:* Detonates an explosive blast dealing heavy shrapnel damage across a 4-meter radius (1 AP).
  - *Automated Ceiling Turret:* Deploys from its housing, acquires the triggering intruder, and fires a kinetic burst dealing weapon damage (1 AP).
  - *Electrified Floor Grid:* Charges the deck plates, dealing electrical shock damage and inflicting the **Stunned** condition (1 AP).

#### Spotting Active Security
Operatives do not need to stumble blindly into traps:
* **Instinctive Awareness:** An operative who pauses to survey a hallway can spend **1 AP** to make an **Instinct + Instinct** (raw perception) or **Knowledge + Instinct** (spotting standard defensive layouts) Simple Test. A single Hit reveals all concealed tripwires, floor sensors, and ceiling turret mounts in that room.
* **Player Inquiry:** If a player actively declares: *"Before stepping into the corridor, I check the floor seams for pressure plates and shine my flashlight along the door frame for wires,"* the Game Master provides the information freely without requiring a roll. Attentive roleplay is always rewarded.

#### Disarming Active Security
Once spotted, an active hazard can be disarmed or bypassed before it triggers:
* An operative spends **1 AP** to cut wires, shim detonators, or ground electrical circuits using **Finesse + Tinkering** or **Knowledge + Hacking** against the trap's Lockdown rating.
* If the disarm test **succeeds**, the trap is safely rendered inert.
* If the disarm test **fails (0 Hits)**, the operative's tool slips or triggers the anti-tamper circuit, immediately activating the trap as an Active Actor!

---

### 3. Sensory Equipment: The Stacking Downgrade Engine

Sensory equipment does not walk the halls or shoot weapons; it observes, records, and relays telemetry to security consoles. Sensory suites include optical video cameras, infrared thermal sniffers, acoustic microphones, and biometric pressure sensors.

Mechanically, active sensors impose **Downgrades to all Stealth tests** attempted within their monitored zone:
* **Basic Sensor (Optical Camera / Audio Mic):** Imposes **1 Downgrade** to stealth tests moving through its viewing cone.
* **Advanced Sensor (Thermal Imager / Motion Sweeper):** Imposes **2 Downgrades** to stealth tests, detecting body heat and micro-vibrations through smoke or darkness.
* **Military / Multi-Spectrum Suite:** Imposes **3 Downgrades**, combining optical zoom, thermal detection, and hull magnetic resonance.

#### Stacking Sensor Downgrades
If a high-security corridor is covered by both a ceiling optical camera and a wall-mounted thermal scanner, their penalties **stack cumulatively**. An operative attempting to sneak through that corridor suffers **3 Downgrades** (1 from the camera + 2 from the thermal scanner), stepping down three of their d10 dice to d8s!

```
+---------------------------------------------------------------------------------+
|                    DIRECT INTERFACE VS. REMOTE SENSOR HACKING                   |
+---------------------------------------------------------------------------------+
| Operatives can eliminate sensor Downgrades by disabling or looping them:        |
|                                                                                 |
| 1. Remote Slicing (From an Access Terminal): An operative connects their        |
|    Cyberdeck to a corridor junction box or local terminal, rolling Knowledge +  |
|    Hacking to loop camera feeds. While safe from physical sight, their roll     |
|    suffers the full stacked Downgrades of all sensors monitoring that network.  |
|                                                                                 |
| 2. Direct Physical Tampering: An operative crawls directly beneath a camera or  |
|    splices its physical wire loom. When interacting with a sensor directly,    |
|    the operative ONLY suffers the Downgrade of that specific device, completely |
|    ignoring the stacked Downgrades of all other sensors in the room!             |
+---------------------------------------------------------------------------------+
```

---

## 4. Sentries & Alerts: When Infiltrations Go Hot

When a guard spots an unmasked intruder, an operative botches a door breach, or a tripwire detonates, the facility does not remain passive. However, alarms do not instantaneously teleport the entire station's garrison into the room. Security response is governed by deliberate **Sentry Actions** and a **Three-Stage Facility Alert Track**.

```
+-------------------------------------------------------------------------------------------------------------+
|                                           FACILITY ALERT STATES                                             |
+-------------------+-----------------------+-----------------------------------------------------------------+
| State             | Security Awareness    | Operational Impact on Infiltration                              |
+-------------------+-----------------------+-----------------------------------------------------------------+
| 1. Unaware        | Zero knowledge of     | Sentries follow fixed routes and pass GM turns automatically.   |
|                   | intruders.            | Cameras record passively. Standard patrols.                     |
+-------------------+-----------------------+-----------------------------------------------------------------+
| 2. Alert          | Facility knows        | Every encountered guard is an Active Actor. Guards actively     |
|                   | intruders are inside, | spend AP searching every GM turn. Cameras enter active sweep.   |
|                   | but NOT where.        | Security gates seal between major sectors.                      |
+-------------------+-----------------------+-----------------------------------------------------------------+
| 3. Lockdown       | Facility knows the    | Full sirens, red klaxons, blast doors seal room exits.          |
|                   | exact location of     | REINFORCEMENTS ARRIVE EVERY ROUND at the End of the Round       |
|                   | the intruders!        | until all active enemies are dead OR PCs dispatch the wave,     |
|                   |                       | retain AP, and successfully Hide (resetting back to Alert).     |
+-------------------+-----------------------+-----------------------------------------------------------------+
```

### Raising the Alarm: The Sentry's Success Test

A sentry who discovers an intruder or stumbles across a compromised terminal cannot instantly transmit an alert through telepathy. Raising the alarm is an active, physical endeavor that costs **1 AP** on the sentry's turn and is resolved as a **Success Test**:

* **Radio Call / Voice Shouting:** The sentry unclips their comm-link or shouts into a tactical throat mic, rolling **Presence + Instinct**.
* **Physical Alarm Switch:** The sentry sprints to a wall-mounted red alarm console or hits a panic button on their terminal, rolling **Finesse + Agility**.

#### Contesting the Alarm
If a player character is in position (within melee range or maintaining a readied ranged weapon covering the sentry), the player can **reactively spend 1 AP to Contest the test**:
* The player rolls an appropriate Simple Test (e.g., tackling the sentry, shooting the radio out of their hand, or jamming their arm against the wall).
* Each Hit (`8+`) rolled on the Contest Roll **eliminates one die** from the sentry's incoming Success Test pool, exactly adhering to *Corsair's* core rules for Contesting a Test.
* If all of the sentry's `8+` dice are eliminated, the sentry fails to transmit the alert!

#### Environmental & Electronic Interference
Clever preparation directly hinders sentry communications:
* **Electronic Jamming:** Deploying an RF comm-jammer or EMP charge imposes **2 Downgrades** on radio-based alarm tests.
* **Severed Physical Lines:** Slicing the corridor's external comms conduit imposes a **Blocker Effect** on physical wall switches, requiring the sentry to score 2 Hits to reach the central network.

#### Escalating the Alarm Level
If the sentry's Success Test yields un-negated Hits, **each Hit rolled advances the facility's Alert Track by 1 stage**:
* Rolling **1 Hit** elevates an **Unaware** facility to **Alert**.
* Rolling **2 Hits** elevates an **Unaware** facility straight to **Lockdown** (or elevates an **Alert** facility to **Lockdown**)!

---

### The Three Facility States in Detail

#### State 1: Unaware (Green)
The baseline operational status of a secure facility. Guards follow their routine shifts, maintenance workers focus on repairs, and surveillance monitors cycle on pre-set loops. 
* Unaware sentries **pass their turn automatically** during the GM's phase.
* Operatives move through shadows, slip past blind spots, or leverage disguises with minimal friction.

#### State 2: Alert (Yellow)
Triggered when an un-silenced gunshot echoes down a shaft, a patrol fails to check in on schedule, a severed power line trips automated network diagnostics, or a sentry gets off a partial radio call: *"Command, we have an unconfirmed contact in Sector 4!"*
* **Active Hunting:** Security forces know intruders are somewhere inside the facility, but **they do not know where**.
* **Every Guard Is Active:** Every security guard, guard drone, or supervisor the characters encounter is immediately an **Activated Actor**.
* **Mandatory Search Turns:** On every GM turn, every sentry within sensory range spends their AP actively rolling search tests (**Instinct + Instinct**) to inspect shadows, lockers, and ceiling grates.
* **Sector Containment:** Secondary security gates between sectors close, requiring operatives to bypass Lockdown 1 doors to navigate deeper into the installation.

#### State 3: Lockdown (Red)
Triggered when security confirms visual identification of the intruders, a sentry successfully sounds the alarm console, or an active firefight erupts.
* **Location Compromised:** Red emergency strobes flash, klaxons blare, and the central public address system announces: *"Intruders confirmed in Level 2 Turbine Bay. Containment protocol active."*
* **Reinforcements Arrive Every Round:** In Lockdown, the facility unleashes its rapid response forces. At the **End of every Round**, a fresh wave of reinforcements (typically a 3- to 4-man tactical security team or combat drones) arrives via elevators, service stairwells, or exterior blast doors!
* **Breaking the Lockdown:** Operatives cannot survive an infinite attrition battle against a station's entire garrison. To survive, the cell must break line of sight and re-establish stealth:
  1. The crew must neutralize, stun, or kill **all active enemies currently in their immediate encounter space**.
  2. The operatives must have **Action Points remaining** in that round after the last active enemy falls.
  3. Every operative must spend an AP to make a successful stealth move into deep cover, ventilation ducts, or maintenance sub-floors before the End of the Round strikes.
  4. If all operatives are successfully hidden when the End of the Round arrives, the incoming reinforcement wave breaches the room to find it empty! Security loses active visual telemetry, and the facility drops from **Lockdown back to Alert**, giving the crew a second chance to evade capture.

---

## 5. Practical Example: The Pelagia Sub-Aquatic Breach

The following comprehensive narrative example demonstrates how all four pillars—stealth movement, disguise bluffing, sensory downgrades, and alert escalation—interact seamlessly at the table.

> ### The Contract
> Jax (Vanguard), Silas (Weaver), and Tessa (Pilot) have accepted a black-market freelance contract on the oceanic moon of Pelagia. Their objective is to infiltrate the **Nereus Deep-Sea Aquaculture Research Complex**, locate a secure genetics vault on Sub-Level 3, and extract an encrypted canister of Precursor-derived aquatic algae without triggering an automated facility purge.
>
> The GM sets the scene in **Place-to-Place pacing** for the infiltration approach.

---

### Phase 1: Preparation & Disguise Crafting (Place to Place)

The crew knows that walking into Nereus in full combat gear is suicide. During their 30-minute preparation round outside the sea-lock, the operatives coordinate their infiltration plan:

```
+-----------------------------------------------------------------------------------------+
|                                NEREUS INFILTRATION PREP                                 |
+-----------+--------+--------------------------------------------------------------------+
| Character | AP Cost| Preparation Action                                                 |
+-----------+--------+--------------------------------------------------------------------+
| Silas     | 1 AP   | Knowledge + Finesse Simple Test: Crafts Maintenance Disguises      |
|           | 1 AP   | Interfacing via Cyberdeck: Downloads internal plumbing blue-prints |
|           | 1 AP   | Forfeited / Holds in reserve                                       |
+-----------+--------+--------------------------------------------------------------------+
| Jax       | 1 AP   | Dismounts Vanguard MANTLE; stows frame in hydraulic cargo crate    |
|           | 1 AP   | Conceals heavy Boarding Axe inside maintenance toolbox (Load 2)    |
|           | 1 AP   | Forfeited / Holds in reserve                                       |
+-----------+--------+--------------------------------------------------------------------+
| Tessa     | 1 AP   | Piloting test: Docks submersible cleanly into external waste chute |
|           | 1 AP   | Arms concealed EMP Breaching Charge on primary power conduit       |
|           | 1 AP   | Forfeited / Holds in reserve                                       |
+-----------+--------+--------------------------------------------------------------------+
```

1. **Crafting the Cover (Silas):** Silas spends **1 AP** fabricating forged maintenance contractor credentials using his disguise kit and miniature thermal-printer. He makes a **Knowledge (4) + Finesse (3)** Simple Test. His specialized Disguise Kit grants **2 Upgrades**, stepping up two d10s to d12s. Rolling 2d10 and 2d12, Silas scores `[4, 8]` on the d10s and `[9, 11]` on the d12s—yielding **three Hits (`8`, `9`, and `11`)**! Following the core rule for Blocker Effects (**2 Hits per Blocker**), Silas spends 2 of his Hits to purchase **1 Sustained Blocker**.
2. **Authentic Badges (Tessa):** Tessa spent downtime procuring an authentic sanitation foreman badge from a bribed dockhand, adding **+1 free Sustained Blocker** directly to the disguise! This establishes a base **Sustained Blocker Rating of 2**.
3. **The MANTLE Hard Invariant & Concealed Gear (Jax):** Jax knows his heavy Vanguard MANTLE cannot be disguised. He spends **1 AP** uncoupling his cranial shunt and packing the powered frame into a heavy wheeled industrial tool container. Jax also packs his heavy Boarding Axe (**Load 2**) into the false bottom of the crate. Because Load 2 gear imposes **2 Downgrades** to concealment, Silas works carefully to reinforce the disguise's paperwork and credential seals so Jax's bulk does not arouse immediate suspicion.

---

### Phase 2: The Security Checkpoint & The Social Interrogation

The trio wheels their heavy cargo crate through the pressurized airlock into the Sub-Level 1 reception checkpoint. The facility is currently **Unaware**.

At the security desk, a corporate guard scans their identity chits on a wall terminal:
* The GM rolls an **Inspection Test** for the terminal (**Instinct 3 + Knowledge 3**), rolling 3d10: `[3, 7, 8]`—scoring a **single Hit (`8`)**.
* Silas's disguise has a **Sustained Blocker Rating of 2**. The 2 Sustained Blockers completely eliminate the terminal's 1 Hit. Because the disguise functions as a Sustained Blocker, this inspection does not degrade its rating—the disguise remains at full 2 protection for future checkpoints. (To pierce this cover, an inspector would have to score strictly more than 2 Hits—3 or more Hits—in a single test). The terminal chimes green: *"Contractor ID Verified. Sub-Level 3 access granted for drainage repair."*
* The guard waves them toward the service elevator without looking up from his datapad.

---

### Phase 3: The Sensor-Laced Vault Hallway (Moment to Moment)

Reaching Sub-Level 3, the crew steps out of the elevator into a gleaming white corridor leading to the genetics vault. The vault door is sealed behind **Passive Security (Lockdown 2)**. 

Worse, the corridor is protected by **Sensory Equipment**:
* A ceiling **Optical Camera** covers the central 8 meters (imposing **1 Downgrade**).
* An **Acoustic Sniffer** mounted above the vault door detects metallic vibrations (imposing **1 Downgrade**).
* Any character attempting to sneak down the central corridor suffers **2 stacking Downgrades**!

The GM calls for **Zooming In to Moment-to-Moment pacing**. The crew receives **3 Moment-to-Moment AP** each.

```
+-----------------------------------------------------------------------------------------+
|                               VAULT CORRIDOR SNEAK & SLICE                              |
+-------+-----------+--------+------------------------------------------------------------+
| Round | Character | AP Cost| Tactical Infiltration Action                               |
+-------+-----------+--------+------------------------------------------------------------+
| R1    | Silas     | 1 AP   | Direct Interface: Slices camera junction (Knowledge + Hack)|
|       | Jax       | 1 AP   | Creeps 3m along pipe shadows (Agility + Finesse Complex)   |
|       | Jax       | 1 AP   | Fails second creep; botches footstep on loose grate        |
+-------+-----------+--------+------------------------------------------------------------+
```

1. **Direct Physical Tampering (Silas):** Silas spots the camera's external wiring conduit along the ceiling. Instead of hacking the camera remotely from the far elevator terminal (which would suffer both Downgrades), Silas creeps along the ceiling maintenance gantry directly above the camera. Reaching the unit directly, **he only suffers the single Downgrade from that camera**. Silas spends **1 AP** rolling **Knowledge (4) + Hacking (3)** with 1 Downgrade (3d10 and 1d8), scoring `[8, 10]`. Silas loops the video feed, completely neutralizing the camera's Downgrade for the room!
2. **Cautious Creeping (Jax):** With the camera looped, Jax creeps along the wall shadows toward the vault door, facing only the acoustic sniffer's **1 Downgrade**. Jax spends **1 AP** making an **Agility (3) + Finesse (3)** Complex Test to creep forward at half speed (2 SP per meter). Rolling 2d10 and 1d8, Jax rolls `[8, 8]` on the d10s and a `6` on the d8!
   * *Action Roll:* The `8` is a Hit, completing the stealth move cleanly.
   * *Success Roll:* Jax takes his lower attribute (3 dice): the highest die is `6`, yielding **6 Success Points**. At half speed (2 SP/meter), Jax creeps **3 meters forward** into the shadow of a coolant tank.
   * *Banking:* Jax spends his second Hit (`8`) from the Action Roll on a **Downgrade Effect** (costing 1 Hit), imposing 1 Downgrade on any guard perception test searching his position!
3. **The Botched Move (Jax):** Jax attempts to cross the final 3 meters to the vault console. He spends **1 AP** making a second **Agility + Finesse** Complex Test with 1 Downgrade. Jax rolls: `[3, 5, 7]`—**zero Hits!**
   * The Action Roll fails. Jax loses his spent 1 AP.
   * Jax's boot slips on a wet deck grating, kicking an industrial wrench against the metal wall with a sharp ringing echo.
   * **The Activating Actor:** A patrol guard in the adjacent monitoring station hears the clang. The GM announces: *"The guard at the monitoring console stands up, draws his stun-baton, and steps through the doorway. He is now an Alerted Activating Actor for my upcoming turn!"*

---

### Phase 4: Contesting the Alarm & Facility Lockdown

Because Jax has now spent 2 AP this turn (and completed his action), control passes to the GM:

1. **The Guard's Turn (Active Actor):**
   * The guard steps into the corridor and spots Jax crouching half-exposed behind the coolant tank.
   * Seeing an intruder in a maintenance jumpsuit next to an open weapons crate, the guard spends **1 AP** to hit his tactical radio and sound the alarm.
   * The guard initiates a **Success Test** rolling **Presence (3) + Instinct (3)**.
2. **Contesting the Alarm (Tessa):**
   * Tessa, still standing by the elevator with her suppressed sidearm, **reactively spends 1 AP to Contest the guard's test**!
   * Tessa rolls an **Agility (4) + Finesse (3)** Simple Test, rolling 4d10: `[4, 7, 8, 9]`—scoring **two Hits (`8` and `9`)**!
   * Each Hit eliminates the highest die from the guard's Success Test pool. The guard's roll of `[6, 8, 9]` loses the `9` and the `8`, leaving only a `6`.
   * With zero Hits remaining, the guard's radio call is cut off as Tessa's suppressed shot shatters his comm-unit!
3. **Escalation (The Physical Switch):**
   * Frantic, the guard spends his second **1 AP** lunging toward the wall-mounted red alarm pull. He rolls **Finesse (3) + Agility (3)**, scoring a single Hit (`8`).
   * The un-eliminated Hit trips the central system. The facility shifts from **Alert to Lockdown**!
   * Red klaxons blare through the sub-level. Heavy hydraulic blast doors begin sliding shut across the corridor exits.

---

### Phase 5: Breaking the Lockdown

With the klaxons screaming, the GM announces that a heavily armed 4-man corporate tactical team is en route, scheduled to arrive via the service elevator at the **End of Round 1**.

The operatives must act decisively to crack the vault and break the lockdown:
1. **Neutralizing the Witness (Jax):** Jax spends his final **1 AP**, surging from the coolant tank to strike the guard with a concussive melee blow, instantly incapacitating the sentry before he can take cover.
2. **Cracking the Vault (Silas):** Silas sprints to the vault door. The door has **Lockdown 2** (requiring 3 Hits to open). Silas plugs his cyberdeck into the bypass port, spending **1 AP** to roll **Knowledge (4) + Hacking (3)**. Silas spends a banked **Gambit die**, rolling 5d10: `[4, 8, 9, 10]`—an incredible three Hits! All 3 Hits clear the door's Lockdown rating in a single burst, and the heavy titanium door hiss-swings open.
3. **Grabbing the Prize & Hiding:** Tessa dashes into the vault, scoops the algae canister into her pack (1 AP), while Jax and Silas haul the unconscious guard inside and pull the vault door almost shut, slipping into the dark maintenance crawlspace beneath the floor plates.
4. **The End of the Round:**
   * The world clock strikes the End of the Round. The elevator doors chime open, and four armored tactical guards pour into the hallway with assault carbines raised.
   * However, every operative is inside the vault, out of line of sight, and has successfully established cover. There are no active hostiles left standing in the corridor.
   * Finding only an empty hallway and severed camera wires, the tactical team reports: *"Intruders are not at the vault. Sweep the upper corridors!"*
   * Security loses active visual tracking. The facility drops from **Lockdown back to Alert**, giving Jax, Silas, and Tessa the vital window they need to don Jax's Vanguard MANTLE and execute their extraction to the waiting submarine!
