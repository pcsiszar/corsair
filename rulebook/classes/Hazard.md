# Class: The Hazard

*You can download and print the [Hazard Printable Sheet](../character/Hazard_Sheet.html) for play.*

## Description

The Hazard is a rogue-alchemist and combat chemist, defined by a compact, high-pressure Catalyst Chamber and a slick
network of reinforced tubing that traces the anatomy of their limbs. Often seen wearing a low-profile breather mask to
navigate their own volatile workspace, the Hazard uses an integrated conduit system to pump pressurized reagents
directly to their hands or weapon systems. Their presence is marked by the sharp scent of ozone and the subtle, rhythmic
pulse of fluids moving through their sleeves as they tap into their stored reserves.

The Hazard's utility relies on three distinct chemical reservoirs housed within the ChemPack:

The first reservoir contains distilled corrosive acids and debilitating toxins. These substances are designed to
penetrate biological systems and compromise them from within — withering an opponent's effectiveness long after
contact. The second reservoir holds explosive and volatile compounds: fast-acting agents that react on contact with air
or impact, delivering immediate, catastrophic force in a radius the Hazard controls. Finally, a third tank stores
concentrated restorative serums and cognitive stimulants; by dosing allies or themselves, the Hazard can sharpen
reflexes, accelerate healing, and push their cell to peak performance even in the most lethal environments.

## Attributes

* **Venom**: The ability to synthesize and deploy toxic, acidic, and debilitating substances. Venoms work their way
  into a target's biology, degrading the target from the inside out.

* **Hazard**: The ability to synthesize and detonate explosive and volatile compounds. Hazard reagents act immediately
  and violently on contact, dealing direct damage.

* **Serum**: The ability to synthesize and administer restorative and enhancing serums. Serums work within a
  creature's biology to improve their performance.

At character creation, you can distribute 5 points among your Venom, Hazard, and Serum Attributes. The
maximum value for any single Attribute at creation is 4. You can leave an Attribute at 0.

## Basic Mechanics

### Pressure

The Hazard has a Pressure meter that indicates the conditions of the Catalyst Chamber. More Pressure means more potent
brews, but also a greater chance of things going wrong. The Pressure Levels of the Catalyst Chamber go from 0 to 3.

Every Hazard Skill either makes the Pressure go up or down by a set amount. If a Skill use would make the Pressure
exceed its upper or lower bound, it cannot be used.

### Volatile Die

The Hazard has access to a special die called the Volatile Die. Its size corresponds to the Pressure Level: you don't
get one at Pressure 0, it is a d8 at Pressure 1, a d10 at Pressure 2, and a d12 at Pressure 3. The Volatile Die cannot
be upgraded or downgraded by any other means.

You can add the Volatile Die to any test you roll with Hazard Attributes and any other test your skills would allow you
to. When the Volatile Die rolls a **Hit**, you cause a rupture, taking 2 damage, and rolling the Volatile Die again to
determine your new Pressure Level:

- 1, 2, 3: Pressure 3
- 4, 5, 6: Pressure 2
- 7, 8, 9: Pressure 1
- 10, 11, 12: Pressure 0

### Basic Attribute Uses

Each Attribute has a baseline use that does not require any skill:

**Venom — Apply Downgrade.** As an action, you can dose a creature in your space with a debilitating substance.
You can make a melee attack against a creature with Venom, and use any **Hits** generated to create **Downgrade**
Effects. This
**Downgrade** is permanent until removed, and a single creature can only be affected by one Venom effect from you at
a time. You can have a maximum number of active Venom effects equal to your Venom Attribute's value.

**Hazard — Melee Attack.** As an action, you can hurl or detonate a volatile compound against a target in your
space. Make a melee attack using your Hazard Attribute. This attack can only target creatures or objects in the
same space as you.

**Serum — Apply Upgrade.** As an action, you can dose yourself or a willing creature in your space with an
enhancing serum. Roll a **Success Test** with Serum. The resulting Success Points establish an **Upgrade** effect on
that
creature. This **Upgrade** is permanent until removed, and a single creature can only benefit from one Serum effect
from you at a time. You can have a maximum number of active Serum effects equal to your Serum Attribute's value.

### Hazard Skills

You can further expand your arsenal with class-specific skills you unlock as you progress with the class. These skills
are grouped into themed **Kits**, each containing three distinct abilities.

## Skills

### Medic Kit

* **First Aid**
    * *Pressure Change*: `-1 Pressure`
    * *Effect*: Choose a creature in your space and make a **Success Test** with **Serum**. For every 2 Success Points,
      heal
      1 light wound on the target plus an additional amount of light wounds equal to your Pressure.

* **Regenerator**
    * *Pressure Change*: `+2 Pressure`
    * *Effect*: Roll a **Simple Test** with **Serum**. For every **Hit** you sacrifice, you can apply the following
      effect to a
      creature in your space: the next time that creature takes physical damage, they then immediately heal an amount of
      light wounds equal to your Serum Attribute. A creature can have multiple applications of this effect at the same
      time.

* **Defibrillator**: You use an electrical discharge to jolt a creature back to consciousness and heal their wounds, or
  shock an enemy.
    * *Pressure Change*: `+1 Pressure`
    * *Effect*: Choose a creature in your space. If it is unconscious, make a **Success Test** with **Serum** and for
      every 2
      Success Points, heal 1 light wound on the target and an amount of aggravated damage equal to your Pressure. If
      it is conscious, make a melee attack with **Hazard** and gain a damage bonus equal to your Pressure.

### Booster Kit

* **Micro-Booster**
    * *Pressure Change*: `+1 Pressure`
    * *Effect*: Whenever you or a creature in your space takes an action, you can add your Volatile Die to all
      rolls involved in the test.

* **Maximum Effort**:
    * *Pressure Change*: `-2 Pressure`
    * *Effect*: Roll a **Simple Test** with **Serum**. For every **Hit** you sacrifice, you can apply the following
      effect to a
      creature in your space: You gain +1 **Upgrade** to all tests using at least 1 until the end of the round.

* **Adrenaline Rush**:
    * *Pressure Change*: `-3 Pressure`
    * *Effect*: Roll a **Simple Test** with **Serum**. For every **Hit** you sacrifice, you can temporarily grant 1 AP
      to a
      creature in your space, which is lost at the beginning of the next Player Turn.

### Poison Kit

* **Envenom**: Coat your weapon with deadly poison.
    * *Pressure Change*: `+1 Pressure`
    * *Effect*: Make a melee attack. You can use your **Venom** Attribute for the
      **Success Roll**, and gain +1 damage to the attack per Pressure level. You can add any **Downgrade** using this
      skill that
      you could normally add using **Venom**.

* **Decay**: Activate the toxins you embedded to cause direct harm.
    * *Pressure Change*: `-3 Pressure`
    * *Effect*: Make a **Success Test** with Venom. Deal damage equal
      to the result to all creatures affected by your Venom **Downgrades**, which are then consumed.

* **Cloudkill**: Lob a grenade full of pressurized toxic gas.
    * *Pressure Change*: `+3 Pressure`
    * *Effect*: Choose a space within Short Range and make a **Success Test**
      using **Venom**. For every **Hit** you sacrifice, you can apply 1 level of a Venom **Downgrade** to all creatures
      within
      a 4-meter radius of the target space. Creatures in the affected area cannot see outside, and creatures outside the
      area cannot see into or through the cloud.

### Pyro Kit

* **Firebolt**
    * *Pressure Change*: `+1 Pressure`
    * *Effect*: Make a ranged attack in Short Range using **Hazard**. You gain +1 damage to the attack per Pressure
      level.

* **Flamestrike**
    * *Pressure Change*: `+2 Pressure`
    * *Effect*: Choose a space within Short Range and make a **Success Test** using **Hazard**. All creatures in the
      space
      take damage equal to the result. You gain +1 damage to the attack per Pressure level.

* **Flame Ward**:
    * *Pressure Change*: `-3 Pressure`
    * *Effect*: Contest an attack using Hazard without paying any AP. The attacker also takes damage equal to the
      highest remaining die you rolled, if they are in the same space.

### Caustic Kit

* **Corrosive Spray**
    * *Pressure Change*: `+2 Pressure`
    * *Effect*: Make a melee attack with Venom. For each **Hit** you sacrifice from the **Success Roll**, you can
      decrease the
      Physical Protection of the target by 1.

* **Caustic Bullets**:
    * *Pressure Change*: `+1 Pressure`
    * *Effect*: Make a ranged attack using a Firearm. The weapon loses any Damage Bonus it would normally provide, but
      it ignores the target's Physical Protection entirely.

* **Acid Trail**:
    * *Pressure Change*: `-2 Pressure`
    * *Effect*: Make a movement action. You can deal damage to all creatures in the spaces you move through equal to
      your Hazard Attribute. In addition, every time you enter a space, you can decrease the Cover Rating of that space
      by 1.

### Ooze Kit

* **Rubberband**
    * *Pressure Change*: `+2 Pressure`
    * *Effect*: Choose a creature within short range and make a **Simple Test** using Serum. For each **Hit** you
      sacrifice, you
      can move the creature 4 meters closer to you, if it's large or smaller, or move yourself 4 meters closer to it. If
      you end up in the same space, you can make a **Success Roll** with Serum without paying any AP and deal damage to
      the
      target equal to the result.

* **Slimeball**:
    * *Pressure Change*: `-2 Pressure`
    * *Effect*: Make a ranged attack using Venom. Instead of dealing damage, you can sacrifice **Hits** on the **Success
      Roll** to generate a blocker effect that prevents the target from using their legs, or a blocker effect that
      prevents them from using their hands.

* **Trailblazer**:
    * *Pressure Change*: `-1 Pressure`
    * *Effect*: Make a movement action using **Serum**. Until the start of your next turn, all spaces you move through
      are treated as difficult terrain.

### Smoke Kit

* **Smoke Screen**
    * *Pressure Change*: `+2 Pressure`
    * *Effect*: Make a **Simple Test** with **Hazard**. For each **Hit** you sacrifice, you can choose a space within
      short
      range to deploy a smoke screen in. Creatures in the smoke cannot see out of it, and creatures outside the smoke
      cannot see into or through it. Every creature in the smoke also receives 2 **Downgrades** for any test requiring
      sight. The
      smoke screen lasts until the end of the round.

* **Gas Canister**:
    * *Pressure Change*: `+2 Pressure`
    * *Effect*: Choose a space within short range, then roll with either **Venom** or **Serum** to apply the appropriate
      **Upgrade** or **Downgrade** effect to any creatures in the space. Sacrificing one **Hit** applies the effect to
      only one
      creature of your choice, not all of them.

* **Ninja Vanish**:
    * *Pressure Change*: `-2 Pressure`
    * *Effect*: Contest an attack using **Hazard**, then drop a smoke screen in your current space. Creatures in the
      smoke cannot see out of it, and creatures outside the smoke cannot see into or through it. The smoke screen lasts
      until the end of the round.

### Psychedelic Kit

* **Ear Bug**
    * *Pressure Change*: `+1 Pressure`
    * *Effect*: Take a social action against a creature or creatures in short range. You can add your Volatile Die to
      the roll and receive **Upgrades** equal to the highest level of your Venom **Downgrade** active on any one
      creature you
      speak to.

* **Lullaby**:
    * *Pressure Change*: `-1 Pressure`
    * *Effect*: Make a **Success Test** using **Serum**. For every 2 Success Points, you can heal 1 light stress on a
      creature in the same space.

* **Rampage**:
    * *Pressure Change*: `+3 Pressure`
    * *Effect*: Make a **Simple Test** using **Venom**. For each **Hit** you sacrifice, you can turn each level of a
      Venom
      **Downgrade** into a Rampage Effect. A rampaging creature will always try to attack the nearest creature in Short
      Range, friend or foe. If no other creature is within range, it will pass its turn. After the end of the GM Turn,
      clear one level of Rampage Effect.

## Class Mods

* **Reagent Extension**
    * *Effect*: When you activate a skill that can target one or more creatures in your space, you can also target
      creatures that have an active **Upgrade** or **Downgrade** effect created by your **Serums** or **Venoms**.

* **Burst Dampener**
    * *Effect*: You take only 1 damage when you Rupture.

* **Redline Engine**
    * *Effect*: You can exceed the maximum Pressure level, but you rupture immediately when you do and take 2 damage for
      each level you exceed the max by.

* **Dart Launcher**
    * *Effect*: Skills requiring a melee attack can use a ranged attack in short range instead.

* **Deadly Cocktail**
    * *Effect*: You activate the basic effects of your **Venom** and **Hazard** Attributes, by combining the two in a
      melee attack.

## Progression

The ChemPack can be upgraded by spending Credits. Each level of upgrade provides a significant boost to the ChemPack's
capabilities.

At character creation, distribute 5 points among Venom, Hazard, and Serum (max 4). You start out with 1 Kit of your
choice.

| Level | Benefit                                                          | Credit Cost |
|:------|:-----------------------------------------------------------------|:------------|
| 1     | 7 Attribute Points, Max Attribute Cap: 4, Max Pressure: 3, 1 Kit | 100,000*    |
| 2     | +1 Attribute Point, +1 Class Mod Slot, +1 Kit                    | 20,000      |
| 3     | +1 Attribute Point, Max Attribute Cap becomes 5, +1 Kit          | 40,000      |
| 4     | +1 Attribute Point, +1 Class Mod Slot, +1 Kit                    | 75,000      |
| 5     | +1 Attribute Point, Max Attribute Cap becomes 6                  | 150,000     |

* This cost is only applicable if the Hazard class was not gained with your starting class.
