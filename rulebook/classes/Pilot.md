# Class: The Pilot

*You can download and print the [Pilot Printable Sheet](../character/Pilot_Sheet.html) for play.*

## Description

The Pilot is defined by a total neural integration with the Exodrone, a bio-mechanical frame that functions as a
high-performance exoskeleton. This link is facilitated by a sophisticated implant embedded directly into the user’s
motor cortex, manifesting as subtle data-ports along the neck and temples that allow the Pilot to treat the machine as a
direct extension of their own nervous system. Visually, a Pilot is a heavily armored figure, as their role allows them
to wear traditional combat plating or specialized gear beneath the Exodrone’s shifting frame. The Exodrone itself is a
masterpiece of interlocking plates and hissing hydraulics that hums in a rhythmic pulse synchronized with the Pilot’s
own heart, often appearing as a set of dormant, metallic wings when folded against the Pilot's spine.

The Exodrone serves as the Pilot’s primary instrument of enforcement, capable of snapping onto the spinal interface at a
moment's notice to augment the user’s natural power, speed, and precision. In this integrated state, the Pilot can
sprint through heavy fire or punch through reinforced bulkheads with ease. The true tactical depth of the class is
revealed when the Exodrone detaches to act as an independent, remote-controlled avatar. Governed by the Pilot's
thoughts, the detached drone can reconfigure its physical geometry into a heavy weapons platform, a nimble battlefield
medic, a blade-heavy duelist for silent engagements, or a walking tank that generates a localized energy shield to
protect the entire cell.

## Attributes

The Exodrone possesses its own set of physical Attributes that mirror your own:

* **Power**: Corresponds to **Strength**.

* **Speed**: Corresponds to **Agility**.

* **Precision**: Corresponds to **Finesse**.

## Exodrone Modes

The Exodrone has two distinct modes: Attached and Detached.

* **Attached Mode:** While wearing the Exodrone, you can rely on it to do the heavy lifting for you.
  When you make a test involving **Strength**, **Agility**, or **Finesse**, the owner may choose to substitute their own
  Attribute with the Exodrone's corresponding Attribute (Power, Speed, or Precision).

* **Detached Mode:** While the Exodrone is detached from you, you can command it at will. It can take actions using
  its own Attributes. It can gain Action Points via skills, but can always use the Action Points of the Pilot.

## Exo-Skills

A Pilot customizes and trains with their Exodrone extensively, allowing them to use skills that require proper mastery
of the drone. These skills are unlocked via installable Modules, and you start out with a Basic Module, plus a module of
your choice.

You can activate an Exo-Skill at any time.

If a skill refers to the Exodrone without mentioning Attached or Detached Mode, if the Pilot is in Attached Mode, the
Pilot is effectively considered as the Exodrone, from the skill's perspective, except that the skill will always use the
Exodrone's Attributes, and not the Pilot's.

### Batteries

The Exodrone's power source is its batteries carried on the back. They can contain up to a total number of 10 Batteries.
Exo-Skills require you to spend these Batteries to power your abilities.

Each skill will tell you how much it consumes. Some skills increase their cost the more they are used in the same
Round (denoted with an $X$ in the cost, where $X$ is the number of times you used that skill in the round before). If it
is the first time using a skill in a round, $X$ is 0.

You recharge two Batteries at the beginning of the Round if the Exodrone is attached to you.
If you are in place-to-place or day-to-day pacing, you recharge your full Battery instead.

When your Exodrone would take damage, it instead loses a Battery for every 3 points of damage, rounded down.
If it runs out of Batteries, it stops all functions until it recharges a Battery and cannot be used until it recharges
at least one Battery.

## Skills

You start with the Basic Module of Exo-Skills, and you unlock additional Modules as you progress in the class.

#### Basic Module

| Name   | Battery Cost | Description                                              |
|:-------|:-------------|:---------------------------------------------------------|
| Detach | $0$          | Detach the Exodrone.                                     |
| Pilot  | $4$          | Grant 1 AP to the Exodrone while it is in Detached Mode. |
| Attach | $0$          | Attach the Exodrone while it is in the same space.       |

#### Wingman Module

| Name        | Battery Cost | Description                                                                                                                 |
|:------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------|
| Boost       | $2 + X$      | The Exodrone gains +1 **Upgrade** to any one of its Exodrone Attributes until the beginning of the next Player Turn.        |
| Double Move | $2 + 2X$     | When yout take a Movement Action during the current turn, the Exodrone also takes a Movement Action for free.               |
| Tag Team    | $3$          | While detached, the Exodrone participates in your action using **Teamwork** for free, as long as in the same space as  you. |

#### Warden Module

| Name      | Battery Cost | Description                                                                                                                                                                                                                         |
|:----------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Armadillo | $1 + X$      | Gain +1 Protection until the end of the Round while in Attached Mode.                                                                                                                                                               |
| Guardian  | $2 + X$      | When the Exodrone would contest an attack, they can do so for free.                                                                                                                                                                 |
| Barricade | $1 + X$      | While detached, the Exodrone reconfigures itself as deployable mobile cover until the end of the turn, increasing the Cover Rating of its current space by +1. The only action it can take is revert to its standard mode for free. |

#### Duelist Module

| Name          | Battery Cost | Description                                                                                                                                                                                                                                                                                                               |
|:--------------|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shadow Strike | $4$          | After successfully landing a melee attack, you can have the Exodrone land a follow-up attack, adding bonus damage to your attack equal to the corresponding Exodrone Attribute of any of your own Physical Attribute that you used when making the attack, as long as it is in Attached Mode or in the same space as you. |
| Ripple Blades | $2$          | The Exodrone gains access to two wrist-mounted energy blades until the end of the round with the following profile: `Dmg: +3, Reach: 2`.                                                                                                                                                                                  |
| Plasma Glaive | $3$          | The Exodrone gains access to a two-handed energy polearm until the end of the round with the following profile: `Dmg: +6, Reach: 4`.                                                                                                                                                                                      |

#### Arsenal Module

| Name           | Battery Cost | Description                                                                                                                                         |
|:---------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| Laser Rifle    | $3$          | The Exodrone gains access to a wrist-mounted plasma rifle until the end of the round with the following profile: `Acc: [3/2/1/-], Dmg: +2, RoF: 2`. |
| Ion Cannon     | $3$          | The Exodrone can fire a single shot from a shoulder-mounted laser with the following profile: `Acc: [1/4/3/2], Dmg: +5, RoF: 0`.                    |
| Plasma Grenade | $3$          | The Exodrone can lob a powerful grenade with the following profile: `Area Attack, Ordnance 4, 4m Radius`.                                           |

Assault Module

| Name          | Battery Cost | Description                                                                                                                                                                                                                                                                                                                                                            |
|:--------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Full Throttle | $3$          | Until the end of the Player Turn, you can declare a melee attack against a creature 12 meters away from you and move into that creature's space as part of the attack.                                                                                                                                                                                                 |
| Spider Climb  | $1$          | Until the end of the round, the Exodrone can stick to and move on any surface as if it were regular terrain.                                                                                                                                                                                                                                                           |
| Jump Pack     | $3$          | On your next movement until the end of the Player Turn, the Exodrone gain a Thrusters Attribute equal to your highest Exodrone Attribute. When you use your Thrusters to move, your base movement speed is 8 meters, you double the number of meters rolled in your movement action, and you can fly for your entire movement. You fall at the end of the Player Turn. |

Recon Module

| Name           | Battery Cost | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|:---------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sensor Suite   | $3$          | Until the end of the round, the Exodrone gains a fourth Exodrone Attribute called Sensors, which corresponds to Instinct. Its value is equal to the highest Exodrone Attribute out of Power, Speed, and Precision.                                                                                                                                                                                           |
| Proximity Scan | $1$          | The Exodrone scans a 20-meter radius for either living creatures or electronic devices. You learn their approximate position and size, but nothing else.                                                                                                                                                                                                                                                     |
| Omni Tool      | $3$          | While detached, the Exodrone reconfigures itself as an interfacing device. It attaches to a device, mechanical or electronic, and can force it to take actions that the device could otherwise take, including malfunctioning behavior. The Exodrone uses its highest Attribute for any tests to manipulate the device. The only other action the Exodrone can take is revert to its standard mode for free. |

### Seraph Module

| Name         | Battery Cost | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| First Aid    | $1 + X$      | While the Exodrone is attached, it can heal 2 light wounds for the wearer for every Battery Charge spent. While detached, it can instead heal 2 light wounds for any creatures in the same space.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Healer Darts | 2            | The Exodrone gains access to a wrist-mounted dartgun until the end of the round with the following profile: `Acc: [3/2/1/-], Dmg: 0, RoF: 0`. When these Darts hit their target, they heal 1 light wound for every 2 Success Points instead of dealing damage.                                                                                                                                                                                                                                                                                                                                                   |
| Phoenix Egg  | 7            | While detached, the Exodrone reconfigures itself as a medical device. It attaches to a creature and can perform a special healing action, taking a Success Test using its highest Attribute and healing 1 light wound for every 2 Success Points or 1 aggravated wound for every 4 Success Points. Any damage the creature would take is instead taken by the Exodrone. This healing can also revive creatures that died during the current round. The only action the Exodrone can take is revert to its standard mode for free, and the creature cannot take any action while the Exodrone is attached at all. |

## Class Mods

You unlock class mod slots at certain progression levels. You can buy Class Mods for 25,000 Credits each. You can
replace your current mod with a different one you own during your day-to-day.

### Extra Battery

**Effect**: The max number of Batteries you can hold is increased to 12.

### Remote Charging

**Effect**: The Exodrone loses one Battery for every 4 points of damage it receives instead of 3 and can gaine Batteries
even in detached mode.

### Biomechanical Dynamo

**Effect**: While in Attached Mode, you may sacrifice **Hits** on any test that uses your own Physical Attributes to
increase your Battery by 1 for each **Hit** you sacrifice.

### Turbo Boost

**Effect**: After using an Exodrone Skill, any test using a chosen Exodrone Attribute gains +1 Upgrade until the end of
the Player Turn.

### Charger Mode

**Effect**: If you didn't use a skill that requires a Battery and didn't use the Exodrone's Attributes on any
test, you regain two more Batteries at the end of the Round.

## Progression

The Exodrone can be upgraded by spending Credits. Each level of upgrade provides a significant boost to the Exodrone's
capabilities.

| Level | Benefit                                                           | Credit Cost |
|:------|:------------------------------------------------------------------|:------------|
| 1     | 7 Attribute Points, Basic Module, +1 Module, Max Attribute Cap: 4 | 100,000*    |
| 2     | +1 Attribute Point, +1 Module, +1 Mod Slot                        | 20,000      |
| 3     | +1 Attribute Point, +1 Module, Max Attribute Cap +1               | 40,000      |
| 4     | +1 Attribute Point, +1 Mod Slot, +1 Module                        | 75,000      |
| 5     | +1 Attribute Point, Max Attribute Cap +1                          | 150,000     |

* This cost is only applicable if the Exodrone Pilot class was not gained with your starting class.
