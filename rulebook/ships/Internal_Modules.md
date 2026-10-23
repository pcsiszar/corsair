# Starship Internal Modules

Internal modules are specialized systems installed within a ship's hull to enhance its operational capabilities, crew safety, or tactical flexibility. Unlike hardpoints, which are reserved for external weaponry, internal modules represent the ship's infrastructure, avionics cores, automated drone hives, and specialized equipment bays.

A vessel has a limited capacity for **Module Slots** based on its structural size tier:

* **Small Vessels:** 4 Module Slots
* **Medium Vessels:** 8 Module Slots
* **Large Capital Ships:** 12 Module Slots

Each internal module has a **Slot Cost** (typically 1 to 3 slots) that counts against this total capacity.

---

## Master Internal Modules Table

| Module Name | Operational Description | Mechanical Effect | Slots | Cost (Credits) |
|:---|:---|:---|:---:|:---:|
| **Injector Seats** | High-G inertial dampening crew cradles. | Take half damage from G-Strain (round down). | 1 | 0 |
| **Extra Ammo Storage** | Expanded magazine drums and battery banks. | Double the ammo capacity of all weapons. | 1 | 350,000 |
| **Reinforced Bulkheads** | Titanium-composite cross-braces and plating. | Increase Hull Rating by +2 across all tracks. | 1 | 650,000 |
| **Auto-Loaders** | Rapid-feed hydraulic ammunition handling rams. | Increase Rate of Fire (RoF) by +1 (where applicable). | 1 | 850,000 |
| **Basic MedBay** | Compact single-bunk automated triage berth. | Recovery tests on the ship receive 1 Upgrade. | 1 | 450,000 |
| **Advanced MedBay** | Automated trauma suite with surgical drones. | Recovery tests on the ship receive 2 Upgrades. | 2 | 1,200,000 |
| **Intensive Trauma Suite** | Full clinical biosculpting and surgical gantry. | Recovery tests on the ship receive 3 Upgrades. | 3 | 2,500,000 |
| **Signal Scrambler** | Broad-spectrum electronic countermeasure array. | +2 Upgrades to Sensor Jam / Radar Jammer actions. | 1 | 1,500,000 |
| **Fire-Control Computer** | Predictive ballistic and orbital tracking core. | +2 Upgrades to Target Lock actions. | 1 | 1,800,000 |
| **Advanced Repair Drones** | Smart-autonomous zero-g nanite swarm. | +2 Upgrades to in-combat Repair actions. | 1 | 2,000,000 |
| **Enhanced Sensor Suite** | High-fidelity cryogenic sensor arrays. | Increase base Target Lock and Sensor Range by +2 km. | 1 | 2,500,000 |
| **Hangar Bay** | Pressurized launch deck and recovery bay. | Houses 2 Drone-fighters or 1 Shuttle craft. | 3 | 4,000,000 |
| **Extra Hardpoint** | Structural reinforcement for an additional mount. | Add one Hardpoint of a size already present on ship. | 2 | 5,000,000 |

---

## Detailed Module Profiles

### 1. Injector Seats
*Standard equipment for high-performance interceptors. Uses hydrostatic liquid-immersion cradles and automated cardio-vasoconstrictor drug injectors to prevent cerebral blood pooling during crushing maneuvers.*
* **Mechanical Effect:** Whenever crew members suffer **G-Strain** (usually during high-Acceleration burns or violent Combat Maneuvers), total damage taken (both Light Wounds and Light Stress) is halved, rounded down.
* **Slot Cost:** 1 Slot
* **Cost:** 0 Credits (Standard equipment on high-G combat craft)

### 2. Extra Ammo Storage
*High-density armored ammunition drums and conveyor elevators tucked into cargo voids and structural keels.*
* **Mechanical Effect:** Doubles the **Ammunition** capacity of all kinetic slugthrowers, railguns, and missile/torpedo pods installed on the ship. Has no effect on reactor-powered lasers or particle beams.
* **Slot Cost:** 1 Slot
* **Cost:** 350,000 Credits

### 3. Reinforced Bulkheads
*Titanium-foam composite cross-braces and ceramic arrestor plates welded along internal keels and structural frames.*
* **Mechanical Effect:** Permanently increases the ship's **Hull Rating by +2**. This expands every individual track segment across the vessel's Hull Condition Track (e.g., a Hull Rating 10 with 4 tracks of 10 becomes 4 tracks of 12).
* **Slot Cost:** 1 Slot
* **Cost:** 650,000 Credits

### 4. Auto-Loaders
*High-speed hydraulic rams and smart-sorting magazines that rapidly cycle heavy rounds and missile racks.*
* **Mechanical Effect:** Increases the **Rate of Fire (RoF)** of all Unguided kinetic weapons and all Guided missile/torpedo weapons by **+1 per turn/round**. Does not apply to continuous-wave lasers or weapons that already possess an "Unlimited" RoF.
* **Slot Cost:** 1 Slot
* **Cost:** 850,000 Credits

### 5. MedBay Installations (Basic, Advanced, Intensive)
*Dedicated medical compartments ranging from compact auto-doc berths to full clinical surgical gantries, equipped with diagnostic scanners, synthetic tissue knitters, and emergency life support.*
* **Basic MedBay (1 Slot • 450,000 CR):** A compact single-bunk automated triage station. Any **Recovery** tests (including Long Rest) performed while on board the ship receive **1 Upgrade**.
* **Advanced MedBay (2 Slots • 1,200,000 CR):** A multi-bed automated trauma suite with surgical drones. Any **Recovery** tests performed on board receive **2 Upgrades**.
* **Intensive Trauma Suite (3 Slots • 2,500,000 CR):** A full clinical hospital bay with cryogenic pods and organ synthesizers. Any **Recovery** tests performed on board receive **3 Upgrades**.

### 6. Signal Scrambler
*A suite of active jamming emitters, noise transmitters, and false ladar repeaters designed to shatter hostile sensor locks.*
* **Mechanical Effect:** Grants **+2 Upgrades** to all **Sensor Jam** actions and Engineer *Radar Jammer* tests performed by the crew.
* **Slot Cost:** 1 Slot
* **Cost:** 1,500,000 Credits

### 7. Fire-Control Computer
*A dedicated processing mainframe integrating optical lead solvers and predictive orbital algorithms to assist gunners.*
* **Mechanical Effect:** Grants **+2 Upgrades** to all **Target Lock** actions performed by the Gunner.
* **Slot Cost:** 1 Slot
* **Cost:** 1,800,000 Credits

### 8. Advanced Repair Drones
*Smart-autonomous maintenance nanobot swarms and zero-G repair crawlers that deploy through internal conduits into vacuum.*
* **Mechanical Effect:** Grants **+2 Upgrades** to all in-combat **Repair** actions performed by the Engineer.
* **Slot Cost:** 1 Slot
* **Cost:** 2,000,000 Credits

### 9. Enhanced Sensor Suite
*High-fidelity cryogenic sensors, cooled infrared arrays, and wide-aperture ladar receivers.*
* **Mechanical Effect:** Increases the vessel's base **Sensor Range by +2 km** beyond its standard rating (2x Systems + 2 km).
* **Slot Cost:** 1 Slot
* **Cost:** 2,500,000 Credits

### 10. Hangar Bay
*Pressurized launch decks, magnetic recovery winches, and rapid-refueling umbilicals installed inside large internal cavities.*
* **Mechanical Effect:** Can house and service either **2 Drone-fighters** or **1 Personnel Shuttle**. Craft inside can be launched or recovered during combat.
* **Slot Cost:** 3 Slots
* **Cost:** 4,000,000 Credits

### 11. Extra Hardpoint
*Structural keelson reinforcement, dedicated power bus tapping, and external mounting collars allowing an additional weapon installation.*
* **Mechanical Effect:** Adds **one Hardpoint** of a size (Small, Medium, or Large) already present on the ship. A ship can only install this module once.
* **Slot Cost:** 2 Slots
* **Cost:** 5,000,000 Credits

---

## Modular Retrofitting & Shipyard Logistics

Installing or replacing internal modules requires docking at an authorized orbital drydock, naval station, or asteroid shipyard. Shipwrights charge standard installation labor fees equal to **10% of the module's purchase price**. Fitting a 1-slot module takes roughly **24 to 48 hours**, while major structural overhauls (such as installing a Hangar Bay or Extra Hardpoint) require **1 to 2 weeks of orbital berth time**.
