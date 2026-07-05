# Starship Internal Modules

Internal modules are specialized systems installed within a ship's hull to enhance its operational capabilities, crew
safety, or tactical flexibility. Unlike hardpoints, which are reserved for weaponry, internal modules represent the
ship's infrastructure and specialized equipment bays.

## Internal Modules Table

| Module Name                | Description                                     | Special Effect                                       | Slots | Cost (Credits) |
|:---------------------------|:------------------------------------------------|:-----------------------------------------------------|:------|:---------------|
| **Injector Seats**         | High-G inertial dampening crew cradles.         | Take half damage from G-Strain (round down).         | 1     | 0              |
| **Extra Ammo Storage**     | Expanded magazine and battery banks.            | Double the ammo capacity of all weapons.             | 1     | 350,000        |
| **Reinforced Bulkheads**   | Internal structural plating and bracing.        | Increase Hull Rating by +2.                          | 1     | 650,000        |
| **Auto-Loaders**           | Rapid-feed ammunition handling systems.         | Increase Rate of Fire (RoF) by 1 (where applicable). | 1     | 850,000        |
| **Medical Facilities**     | Fully automated med-bays and trauma suites.     | Recovery tests on the ship receive 2 Upgrades.       | 2     | 1,200,000      |
| **Signal Scrambler**       | Broad-spectrum electronic countermeasure array. | +2 Upgrades to Sensor Jam actions.                   | 1     | 1,500,000      |
| **Fire-Control Computer**  | Advanced ballistic and orbital tracking core.   | +2 Upgrades to Target Lock actions.                  | 1     | 1,800,000      |
| **Advanced Repair Drones** | Smart-autonomous maintenance nanobot swarm.     | +2 Upgrades to Repair actions.                       | 1     | 2,000,000      |
| **Enhanced Sensor Suite**  | High-fidelity cryogenic sensor arrays.          | Increase Target Lock range by 2 km.                  | 1     | 2,500,000      |
| **Hangar Bay**             | Launch and recovery racks for small craft.      | Can house 2 Drone-fighters or 1 Shuttle.             | 3     | 4,000,000      |
| **Extra Hardpoint**        | Structural reinforcement for additional mounts. | Add one Hardpoint of a size already present on ship. | 2     | 5,000,000      |

---

## Module Profiles

### 1. Injector Seats

*Standard equipment for high-performance interceptors, these seats use liquid-immersion and rapid-response inertial
dampeners to protect the crew during extreme maneuvers.*

* **Effect**: Whenever the crew or ship takes damage from **G-Strain** (usually during high-Acceleration or
  high-Maneuverability maneuvers), the total damage is halved, rounding down.
* **Slot Cost**: 1
* **Cost**: 0 Credits

### 2. Extra Ammo Storage

*A simple but essential upgrade for long-range missions, consisting of pressurized ammunition drums and high-density
battery arrays tucked into every available corner of the ship's frame.*

* **Effect**: Doubles the **Ammunition** capacity of all weapons installed on the ship. For weapons with "Unlimited"
  ammunition, this has no effect.
* **Slot Cost**: 1
* **Cost**: 350,000 Credits

### 3. Reinforced Bulkheads

*Layers of high-tensile steel and ceramic composites added to the ship's internal support structures to improve overall
survivability.*

* **Effect**: Increases the ship's **Hull Rating** by +2.
* **Slot Cost**: 1
* **Cost**: 650,000 Credits

### 4. Auto-Loaders

*Hydraulic ammunition feeds and smart-sorting magazines that significantly reduce the cycle time between shots for
kinetic and missile weaponry.*

* **Effect**: Increases the **Rate of Fire (RoF)** of all Unguided kinetic weapons and all Guided missile/torpedo
  weapons by +1 per turn/round. This does not apply to laser systems or weapons with "Unlimited" RoF.
* **Slot Cost**: 1
* **Cost**: 850,000 Credits

### 5. Medical Facilities

*A dedicated compartment equipped with stasis pods, surgical drones, and a comprehensive pharmacopeia for treating
combat injuries and vacuum exposure.*

* **Effect**: Any **Recovery** tests (for healing crew or stabilizing critical systems) performed while on board the
  ship receive 2 **Upgrades** to the dice pool.
* **Slot Cost**: 2
* **Cost**: 1,200,000 Credits

### 6. Signal Scrambler

*A suite of active jamming emitters and decoys designed to mask the ship's signature and confuse enemy targeting
systems.*

* **Effect**: Grants 2 **Upgrades** to all **Sensor Jam** actions performed by the crew.
* **Slot Cost**: 1
* **Cost**: 1,500,000 Credits

### 7. Fire-Control Computer

*A dedicated processing unit that integrates sensor data and predictive algorithms to assist gunners in achieving a
solid target lock.*

* **Effect**: Grants 2 **Upgrades** to all **Target Lock** actions performed by the crew.
* **Slot Cost**: 1
* **Cost**: 1,800,000 Credits

### 8. Advanced Repair Drones

*A swarm of semi-autonomous nanobots and spider-drones capable of performing complex repairs in zero-G environments
without crew intervention.*

* **Effect**: Grants 2 **Upgrades** to all **Repair** actions performed by the crew or the ship's automated systems.
* **Slot Cost**: 1
* **Cost**: 2,000,000 Credits

### 9. Enhanced Sensor Suite

*Combining infrared, lidar, and passive radar with a dedicated processing core, this suite allows a ship to see further
and lock on faster.*

* **Effect**: Increases the ship's base **Sensor Range** by +2 km. This bonus also applies to the maximum distance at
  which a **Target Lock** can be established on both the Dogfight and Macro-Grid scales.
* **Slot Cost**: 1
* **Cost**: 2,500,000 Credits

### 10. Hangar Bay

*Internal space repurposed into a small flight deck with launch rails and fueling stations for support craft.*

* **Effect**: The ship can house and deploy up to 2 **Drone-fighters** or 1 **Shuttle** internally.
* **Slot Cost**: 3
* **Cost**: 4,000,000 Credits

### 11. Extra Hardpoint

*A significant engineering feat involving the rerouting of power conduits and the reinforcement of the ship's internal
frame to support an additional external weapon mount.*

* **Effect**: Grants the ship one additional **Hardpoint**. The size of the new hardpoint (Small, Medium, or Large) must
  match a hardpoint size that the ship already possesses in its base configuration. A ship can only benefit from this
  module once.
* **Slot Cost**: 2
* **Cost**: 5,000,000 Credits
