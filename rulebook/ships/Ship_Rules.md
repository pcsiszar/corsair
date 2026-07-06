# Ships and Space Combat

Space combat is a high-stakes dance of orbital mechanics, tactical positioning, and raw physiological endurance. Battles
take place across two distinct modes of engagement: navigating the vast distances of a planetary orbit on a macro scale,
and entering tight, white-knuckle dogfights where pilots fight tooth and nail for the optimal firing vector.

Surviving these encounters requires a deep understanding of your ship’s core architecture and a crew that operates as a
single, cohesive unit.

---

## Positioning in Space

Space combat operates on a macro-level **Hex Grid** representing vast distances of open void, paired with a micro-level
**Dogfight Scale** when ships engage at close quarters.

### Macro-Movement & Momentum

Ships start out on the **Macro-Grid**, where each space constitutes a 1 km diameter sphere. Ships move on the grid using
their Engine's **Acceleration**. They roll a **Success Test** to determine how far they can move, moving 500 meters for
every Success Point, or a single space for every 2 Success Points, rounded down.

However, the G forces of heavy acceleration and deceleration take a toll on the ship's crew. If you spend more than 6
Success Points moving, you suffer G-Strain, taking one **Light Wound** and one **Light Stress** for every additional
Success Point you spend moving. This damage is not reduced by Protection.

Due to Newtonian physics and vector momentum, space travel demands forward commitment. A ship is strictly prohibited
from moving back into a space it just moved out of during its movement. This means that in order for a ship to reenter a
space it left during its movement, it first must move through two adjacent spaces on the grid.

### Entering the Dogfight (The Dogfight Scale)

When two or more ships enter the same hex on the grid, they immediately enter **Dogfight Mode**. The macro-grid movement
stops, and their relative micro-positioning is tracked on a **Dogfight Scale from 1 to 10**.

```
[ 1 — 2 — 3 ] ---------> [ 4 — 5 — 6 — 7 ] ---------> [ 8 — 9 — 10 ]
 Disadvantage                  Neutral                    Advantage
(Enemy on your Tail)       (Passing Vectors)         (You are on their Tail)

```

Every ship has a separate Dogfight Scale with every other ship sharing its space. The value is always representative of
the players' perspective.

On their turn, a character piloting the ship can use the ship's **Maneuverability** to climb the scale. With a Complex
Test using **Maneuverability + Instinct**, the pilot can climb (or drop) one position on the scale for every Success
Point scored. G-Strain also affects this maneuver if you use more than 6 Success Points to move on the scale.

* **The Interception Advantage:** The act of hunting a target grants momentum. The ship that moves into an occupied hex
  enters the scale at **Position 6** (Attacker), giving them an immediate edge. The ship that was already present in the
  hex starts at **Position 5** (Defender).


* **Breakaway:** A ship trapped in a disadvantageous position cannot simply fly away. A Pilot must successfully
  shift the Dogfight Scale back to a neutral zone (Position 4 or higher) before the ship is permitted to leave the
  dogfight hex and return to the macro-grid. The ship can use **Acceleration** to break away and climb the scale back
  to neutral, and then use the remaining Success Points to move on the macro-grid.

* **Contesting Breakaway:** When a ship tries to break away from your space, you can spend 1 AP to also roll
  Acceleration. As long as you score a higher result, you can perform a movement action on the macro-grid directly after
  the contested ship, during the opponent's turn. If you end your movement on the same hex, you keep your position on
  the Dogfight scale, and you can also climb the scale by the difference in the results. The sum of every macro and
  dogfight movement you make is subject to G-Strain.

* **Contesting Maneuvers:** When a ship in your space tries to move on the Dogfight Scale, you can spend 1 AP to also
  roll Maneuverability. Instead of negating the highest dice, you fall or climb the scale by the difference in the
  results.

---

## Anatomy of a Starship

Every starship is defined by a few universal structural characteristics. These stats determine how much punishment the
ship can take, how it moves through space, and how it is customized for war.

### 1. Hull

The Hull represents the ship's physical integrity and structural health—its primary hit point bar. Because hard sci-fi
vessels lack energy shields, any weapon hit that penetrates point-defense grids strikes the hull directly.

Your ship's Hull Condition Track is split into smaller tracks whose size is equal to the Ship's Hull Rating. The Hull
Rating is always an even number.
The number of smaller tracks is dependent on the ship's size, usually ranging from 3 to 6. A typical Corsair ship has
four tracks, with length ranging between 8 and 12 segments.

Your Hull Condition Track takes damage exactly like a character's Health Track. When a single track is filled, it
doesn't spill over to the next one but starts turning the Light Wounds into Aggravated Wounds. When a ship's Condition
Track is filled with Light Wounds, it shuts down and becomes unusable. When it fills with Aggravated Wounds,
it is completely destroyed.

### 2. Armor

Armor is the ship's Protection, meaning that each point of Armor reduces the damage a ship takes by 1.

### 3. Engines

A starship engine has two primary Attributes:

* **Acceleration:** Used exclusively for **Macro-Grid Movement**. This rating dictates the raw forward thrust of the
  main engines.
* **Maneuverability:** Used exclusively for **Dogfight Movement**. This rating dictates the ship's agility, lateral
  thruster power, and attitude control.

### 3. Weapons

A ship's weapon systems consist of the actual weapons and the hardpoints where they are mounted.

Hardpoints are the designated structural mounting zones on a ship's hull where weapons and specialized deployment
systems are installed. Hardpoints come in three distinct sizes, restricting the types of equipment a ship can carry:

* **Small Hardpoints:** Designed for agile, rapid-tracking systems like Point-Defense Cannons (PDCs) or light sensor
  packages.
* **Medium Hardpoints:** Accommodate standard offensive ordnance, such as missile salvos, torpedo tubes, or standard
  laser arrays.
* **Large Hardpoints:** Reserved for massive, devastating weapon systems like spinal-mount coilguns or high-yield heavy
  railguns that often require the ship to align its entire chassis to aim.

The actual weapons themselves are installed in the hardpoints. Most weapons fall into two separate categories, Guided or
Unguided. Unguided weapons can be fired at any time, Guided weapons require Target Lock on the target ship. Unguided
weapons are fired using a Complex Test with **Finesse** + **Accuracy**. Guided weapons are fired using a Complex Test
with **Tracking** + **Tracking** and their Target Locks are acquired by a Complex Test with **System + Knowledge**.

Ship Weapons have the following characteristics:

* **Size:** The size of the weapon dictates what hardpoints it can be mounted on. They come in Small, Medium, and Large
  categories, each of which can be mounted on the corresponding Hardpoints.

* **Accuracy:** The measure of how accurate an unguided weapon is. Accuracy is an array that covers every scale of the
  Dogfight Scale as well as distance on the Macro-Grid. Most weapons cannot only be fired on a few positions on the
  Dogfight Scale, like spinal-mount coilguns. Most unguided weapons can be fired on the Macro grid, but the accuracy
  decreases as the distance increases.

* **Tracking:** The measure of how reliable a guided weapon is. To use a guided weapon, the firing ship must
  have a Target Lock on the target ship. Each level of Target Lock provides one Upgrade when firing the guided weapon.

* **Damage Bonus:** The additional flat damage that a weapon deals when it lands.

* **Rate of Fire:** The number of shots that the weapon can fire. Some weapons can fire without restrictions, like PDCs,
  some weapons can fire only once per turn, and some weapons can fire only a limited number of times per round, and only
  once per turn.

* **Ammunition:** The number of times the weapon can be fired, total. Most weapons don't require ammo, but heavier
  weapons have a limited amount of ammo and once it's depleted, it must be resupplied.

### 4. Systems

Systems represent the capabilities of the ship's core internal devices like its sensors, power grids, and automated
repair drones and navigation. This is a core ship Attribute and is used for a number of purposes, such as:

* **Sensor Range:** The range at which a ship can acquire Target Locks. It's a number of kilometers equal to twice the
  ship's System Attribute.

* **Power Distribution:** The ship can use its Power Grid to power to distribute excess power to either its weapons, its
  engines, or its systems. After choosing either *Weapons*, *Systems*, or *Engines*, a player can roll a Simple Test
  with **System** to then use any hits generated to grant an Upgrade to any test using the corresponding Attributes
  until the end of the round, up to a maximum of 3.
    * *Weapons* – **Accuracy** and **Tracking**
    * *Systems* – **Systems**
    * *Engines* – **Acceleration** and **Maneuverability**.

* **Repair Drones:** The ship can use its Repair Drones to repair itself and its systems.

### 5. Internal Modules

Internal modules are specialized systems installed within a ship's hull to enhance its operational capabilities. A ship
has a limited capacity for **Module Slots** based on its size class:

* **Small**: 4 Module Slots
* **Medium**: 8 Module Slots
* **Large**: 12 Module Slots

Each internal module has a **Slot Cost** (usually 1 or 2) that counts against this total. See
the [Internal Modules](file:///c:/Users/csisz/IdeaProjects/corsair/rulebook/ships/Internal_Modules.md) list for
available upgrades, their costs, and slot requirements.

---

## Roles and Seats

Every starship bridge or command center is configured with a set number of physical seats. While any crew member can
access basic ship functions from any terminal, sitting in a dedicated seat grants access to advanced systems and
critical defensive reactions.

If a crew member is knocked unconscious or needs to pivot strategies, characters may spend an Action Point to swap
seats or move to an empty seat.

### Basic Ship Actions

These are the actions available to all crew members sitting in any seat.

* **Full Throttle:** A Success Test using the ship's **Acceleration**. Used to Break Away from a dogfight or to move
  through the Macro-Grid.
* **Combat Maneuver:** A Complex Test combining the ship's **Maneuverability + Instinct**. Used to climb the Dogfight
  Scale.
* **Weapons Hot:** Fire a weapon mounted to an available hardpoint.

### The Three Core Seat Types

These are the actions and benefits available to each of the three core seats.

* **The Pilot Seat:**
    * **Enhanced Controls:** Sitting in the Pilot seat grants an Upgrade to Full Throttle and Combat Maneuver tests.
    * **Evasive Maneuvers:** While sitting in the Pilot seat, you can contest attacks against the ship using Instinct.
    * **Stay on Target:** While sitting in the Pilot seat, you can contest Breakaways and Maneuvers using the
      appropriate Attribute.
* **The Gunner Seat:**
    * **Enhanced Targeting:** Sitting in the Gunner seat grants an Upgrade to tests using Accuracy and Tracking.
    * **Target Lock:** While sitting in the Gunner seat, you can roll a Simple Test with Systems to acquire a Target
      Lock on a ship within Sensor Range for each Hit you sacrifice
    * **Point Defense:** While sitting in the Gunner seat, you can contest a Guided weapon attack using your Point
      Defense Cannon's Accuracy. Firing with multiple PDCs grants one Upgrade per additional PDC.
* **The Engineer Seat:**
    * **Enhanced Interface:** Sitting in the Engineer seat grants an Upgrade to any test using Systems.
    * **Repair Drones:** While sitting in the Engineer seat, you can use the Repair Drones to repair the ship and its
      systems using a Complex Test with **Knowledge** + **Systems**.
    * **Radar Jammer:** While sitting in the Engineer seat, you can use your EWAR suite break Target Lock on your ship
      using a Complex Test with **Knowledge** + **Systems**.
    * **Power Distribution:** While sitting in the Engineer seat, you can distribute excess power to either its
      weapons,
      its engines, or its systems. After choosing either *Weapons*, *Systems*, or *Engines*, a player can roll a
      Simple
      Test with **System** to then use any hits generated to grant an Upgrade to any test using the corresponding
      Attributes until the end of the round, up to a maximum of 3.
        * *Weapons* – **Accuracy** and **Tracking**
        * *Systems* – **Systems**
        * *Engines* – **Acceleration** and **Maneuverability**.



