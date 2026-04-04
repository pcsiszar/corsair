# Class: The Conduit

## Description

The Conduit is the cell’s living battery and high-intensity shock trooper, defined by the volatile relationship between
their biology and the Aether Core implanted within their chest. This core constantly generates a specialized strain of
biotic nanomachines that flow through the user's veins like a secondary circulatory system. As these "Aether-cells"
circulate, they build up a massive internal charge that the Conduit must periodically vent through devastating physical
feats. Visually, a Conduit is a walking storm of elemental energy; the coursing ether leaves glowing, vein-like marks
across their limbs and permanently alters the color of their eyes and hair to match their specific elemental attunement.

The core utility of the Conduit lies in the management and release of this built-up pressure, manifesting as either
Lightning, Frost, or Fire. By surging the Aether-cells through their muscles, the Conduit can execute near-instant
bursts of movement that blur the vision of onlookers or trigger a state of rapid molecular reconstruction for
near-instant regeneration of lethal wounds. When the charge reaches its peak, it can be expelled in localized,
devastating blasts that can shatter armor or incinerate high-density alloys. This makes the Conduit a terrifying
presence on the battlefield—a warrior who grows more dangerous as the conflict drags on, literally glowing with the
lethal potential of the storm trapped inside their veins.

## Attributes

The Conduit's three primary attributes correspond to the elements they harness:

- **Flame**: The embodiment of destruction and aggression.
- **Frost**: The essence of preservation, control, and entropy.
- **Lightning**: The spark of speed, precision, and chain reactions.

## Mechanics

### Charge

Conduit abilities revolve around the **Charge** mechanic. The Aether Core hums, growing louder and brighter as energy
accumulates.

- **Amp Abilities**: These abilities channel energy into the Conduit's body, building up elemental Charge.
    - Using an Amp ability of the *same* element as your current Charges increases your Charge count by 1 (up to a
      maximum).
    - Using an Amp ability of a *different* element purges the old energy, resetting Charges to 0 before applying the
      new element's effect.
    - If you hold the maximum number of Charges, you cannot use an Amp ability of that same element; the vessel is full.
    - Activating an Amp ability of a specific element suppresses any active effects from other elements.

- **Burst Abilities**: These abilities vent the stored energy in a devastating release.
    - Burst abilities can only be used if you have at least 1 Charge.
    - You can only use the Burst variant corresponding to your current elemental Charge.
    - Using a Burst ability consumes *all* current Charges. The power of the ability scales with the number of Charges
      consumed ($N$).

---

## Skills

### Amp Skills

*You begin with knowledge of 2 Amp Abilities. You unlock more as you level up.*

#### Amp Body

*Elemental energy floods your muscles, pushing them beyond natural limits.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, increase the matching Physical Attribute
by 1.

- **Flame**: Your muscles bulge with heat. Increase **Strength**.
- **Frost**: Your movements become fluid and precise. Increase **Finesse**.
- **Lightning**: Your reflexes twitch with anticipation. Increase **Agility**.

#### Amp Psyche

*The hum of the core sharpens your mind, accelerating your thoughts to match the element.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, increase the matching Mental Attribute
by 1.

- **Flame**: Your presence becomes commanding and intense. Increase **Charisma**.
- **Frost**: Your mind becomes a cold, calculating fortress. Increase **Instinct**.
- **Lightning**: Information processes at the speed of light. Increase **Knowledge**.

#### Amp Projectiles

*You infuse your ammunition with elemental power, turning bullets into tracers of fire, ice, or lightning.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, your ranged attacks gain the following
benefits:

- **Flame**: Rounds burn super-hot. **+1 Damage**.
- **Frost**: Rounds sap heat on impact. Inflict 1 **Downgrade** on the target's next action.
- **Lightning**: Rounds arc electricity to nearby foes. For every 2 damage dealt to a target, deal 1 damage to a
  different target in the same space.

#### Amp Strikes

*Your weapons crackle with energy, discharging violently on impact.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, your melee attacks gain the following
benefits:

- **Flame**: Strikes sear flesh and armor. **+1 Damage**.
- **Frost**: Strikes chill the target's bones. Inflict 1 **Downgrade** on the target's next action.
- **Lightning**: Impact sends shockwaves through the group. For every 2 damage dealt to a target, deal 1 damage to a
  different target in the same space.

#### Amp Regen

*You cauterize wounds or numb pain, forcing your body to knit together through sheer will.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, you can heal standard damage on specific
track segments.

- **Flame**: Burn away the impurities. Heal 1 Physical segment.
- **Frost**: Cool the mind and numb the shock. Heal 1 Mental segment.
- **Lightning**: Jumpstart the system. Heal 2 segments (Mental or Physical), but only on the last box of a track.

#### Amp Aura

*An aura of elemental power surrounds you, visible as shimmering heat, drifting snowflakes, or static sparks.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, gain the following effect at the end of
each Player Turn (multiple instances do not stack):

- **Flame**: Radiate intense heat. Deal damage equal to your **Flame** attribute to all creatures in your space.
- **Frost**: Form a crystalline barrier. Gain a **Protection** bonus equal to half your **Frost** attribute (rounded
  down). This lasts until you take damage or until the end of the Player Turn.
- **Lightning**: The next time you land a melee attack or someone lands a melee attack on you, you can deal damage to
  them equal to your Lightning attribute.

#### Amp Detection

*Your senses expand, tuning into thermal gradients or electromagnetic fields.*
**Effect**: Make a Simple Test with the chosen Conduit Attribute. On a success, you can detect specific phenomena within
a 20-meter radius.

- **Flame** / **Frost**: Sense heat signatures, such as the body heat of living creatures or running engines.
- **Lightning**: Sense electrical currents, allowing detection of electronic devices, traps, or hidden constructs.

---

### Burst Skills

*You begin with knowledge of 1 Burst Ability. You unlock more as you level up.*

#### Motion Burst

*You explode into motion, leaving a trail of elemental residue as you dash across the battlefield.*
**Effect**: When spending an action to move, move an additional number of spaces equal to Charges consumed ($N$), in any
direction, ignoring difficult terrain.

- **Flame/Lightning**: Impact like a fireball. All creatures in the space where you end your movement take damage equal
  to $N \times$ **Flame**.
- **Frost**: Flash freeze the area. Spend points equal to $N \times$ **Frost** on **Downgrades** and **Blocker** effects
  against creatures in your destination space.
- **Lightning**: Crash like a thunder. Your next melee attack deals bonus damage equal to $N \times$ *
  *Lightning**.

#### Nova Burst

*You release a spherical detonation, turning the area into a disaster zone.*
**Effect**: Make a special Area Attack against a target space within 40 meters. Roll a number of d10s equal to your
Conduit Attribute. Damage equals the sum of the $N$ highest dice.

- **Flame**: The explosion expands. Increase the radius of the Area Attack by 1 space per Charge.
- **Frost**: A blizzard erupts. Instead of damage, you can apply up to 12 points of **Downgrade** or **Blocker** effects
  to creatures in the space.
- **Lightning**: Arcs jump to specific targets. Select 1 additional target space per Charge, provided it intersects a
  line between your space and the original target.

#### Healing Burst

*You vent excess energy to revitalize yourself and allies, the Aether Core glowing with soothing light.*
**Effect**: Make a special Success Roll using your current Conduit Attribute. Roll d8s equal to the Attribute. Heal an
amount equal to the sum of the $N$ highest dice.

- **Flame**: Warmth spreads to others. Heal $N$ additional creatures in your space.
- **Frost**: Ice reinforces your form. Gain temporary Physical track segments equal to the total rolled.
- **Lightning**: A quick jolt. Heal only the amount of the single highest die. However, you may trigger this ability
  again for free once per Player Turn, up to $N$ total times. You may target other creatures in your space.

#### Torrent Burst

*You unleash a continuous stream of destruction, sweeping across the battlefield like a hose of pure energy.*
**Effect**: Make a special Area Attack against a target space within 20 meters. Roll d12s equal to your Conduit
Attribute. Deal damage equal to the highest die. You may repeat this attack (targeting the same or adjacent space) up
to $N$ times this round.

- **Flame**: The ground burns. Creatures entering the targeted space for the first time this round take 1d12 damage.
- **Frost**: Glaciers rise. Create **Light Corner**, increase Cover Level by 1, or create **Difficult Terrain** in the
  targeted space.
- **Lightning**: The storm spreads. You can target an additional adjacent space with each attack.

#### Supercharge Burst

*You push the Aether Core to its limit, overflowing with power that enhances every action.*
**Effect**: Trigger at any time during the Player Turn. Consumes all Charges ($N$). For the rest of the Round, gain an
amount of **Upgrades** to tests using specific Attributes equal to your corresponding Conduit Attribute. Ongoing Amp
abilities remain active until the end of the round.

- **Flame**: **Strength** or **Charisma**
- **Frost**: **Finesse** or **Instinct**
- **Lightning**: **Agility** or **Knowledge**

#### Reactive Burst

*Your energy flares instinctively to negate incoming harm, a shield of pure element springing to life.*
**Effect**: Trigger when you take damage. Consume all charges ($N$).

- **Flame**: Vaporize projectiles. Reduce ranged damage taken by $N \times$ **Flame**.
- **Frost**: Harden your skin against blows. Reduce melee damage taken by $N \times$ **Frost**.
- **Lightning**: Disperse energy. Reduce Area Attack damage taken by $N \times$ **Lightning**.

#### Displacer Burst

*You strike with kinetic force, sending foes flying with an explosion of contact.*
**Effect**: Trigger when making a melee attack. Deal $N$ bonus damage. You may push the target $N$ spaces.

- **Flame**: Explosive force. Select $N$ additional targets in your space. They take $N \times$ **Flame** damage and are
  pushed the same distance.
- **Frost**: Encase in ice. Spend Success Points equal to $N \times$ **Frost** to buy **Blocker** effects.
- **Lightning**: Thunderclap. Deal damage to all creatures in the target's landing space equal to $N \times$ **Lightning
  **.

---

## Class Mods

You unlock class mods slots at certain progression levels. You can buy Class Mods for 25,000 Credits each. You can
replace your current mod with a different on you own during your day-to-day.

### Duality

**Effect**: You can hold Charges of two different elements simultaneously. The maximum number of Charges you can hold
remains the same (shared between both elements). When you use a Burst Ability, you consume all charges, but only charges
of the element corresponding to the Burst Ability contribute to the corresponding effect ($N$). When you Amp an
elemental charge that you hold, but you are at maximum capacity, you override the charge of the other element. When you
Amp an elemental charge that you don't hold, and you already hold two different elemental charges, you decide which type
of charges you lose.

### Chain Burst

**Effect**: When using a Burst Skill, you can choose to retain some of your Charges instead of spending them on the
skill, but any Charge you have left are lost at the end of the Player Turn.

### Jump Start

**Effect**: When you use an Amp Skill and have Zero Charges (in any element), you generate 2 Charges instead of 1.

### Overflow

**Effect**: Increase your maximum Charges to 4.

### ReCycle

**Effect**: When you cycle between elemental charges, you keep the ongoing effects of the cycled out element until the
end of the Player Turn.

---

## Progression

## Conduit Progression

At character creation, distribute 5 points among Flame, Frost, and Lightning (max 4). The Aether Core can be upgraded by
spending Credits.

| Level | Benefit                                                                      | Credit Cost |
|:------|:-----------------------------------------------------------------------------|:------------|
| 1     | 5 Attribute Points, Max Attribute Cap: 4, Max Charges: 3, Unlock 3 Abilities | 50,000*     |
| 2     | +1 Attribute Point, +1 Mod Slot, Unlock 1 Ability                            | 10,000      |
| 3     | +1 Attribute Point, Max Attribute Cap becomes 5, Unlock 1 Ability            | 20,000      |
| 4     | +1 Attribute Point, +1 Mod Slot, Unlock 1 Ability                            | 40,000      |
| 5     | +1 Attribute Point, Max Attribute Cap becomes 6, Unlock 1 Ability            | 70,000      |
| 6     | +1 Attribute Point, +1 Mod Slot, Unlock 1 Ability                            | 110,000     |

* This cost is only applicable if the Conduit class was not gained with your starting class.
