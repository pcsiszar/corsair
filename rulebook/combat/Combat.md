# Chapter 8: Combat

In the world of Corsair, conflict is inevitable. Whether facing down a squad of corporate enforcers, battling a
monstrous alien in the depths of a derelict ship, or engaging in a desperate dogfight in the void of space, combat is a
thrilling and dangerous part of your adventures.

When a conflict turns violent and every action matters, the game shifts into **Moment to Moment** pacing. The following
rules govern combat encounters. While you can resolve combat using "theatre of the mind," using a grid-based battle
map is highly recommended to add tactical depth and clarity to character and enemy positioning.

### Movement

Navigating the battlefield is crucial for survival. Positioning can determine cover, line of sight, and your ability to
engage or evade foes.

In combat, you can spend **1 Action Point** to move. When you move, you perform a Success Test, typically with Agility,
then move a number of meters equal to the result, plus your base speed, by default, 4 meters.

The Success Test is typically made with your **Agility** attribute, representing your ability to run, climb, and vault
across the terrain. The GM may call for a different attribute based on the situation (e.g., Strength for climbing a
sheer cliff).

#### Movement on a Grid

For ease of play, it is recommended to use a grid with squares or hexes representing an **4 meter diameter circle**.
When using a grid, your movement is calculated as follows:

* Your base speed of 4 meters translates to **1 space**.
* Your Success Test adds additional movement. You divide the number of meters rolled on your test by four, rounding up
  and move an additional number of spaces equal to the result.

This means a single move action can cover a maximum of 16 meters (4 spaces). Since a player can spend multiple Action
Points on movement, the potential distances can be significant.

#### Verticality

Since the world is not a 2D plane, you can move up and down as well as left and right. When the situation introduces
verticality, you can model this by adding more layers of flat horizontal grids on top of each other. These layers are
separated by 2 meters, and moving up and down between layers is always considered difficult terrain, unless of course,
you fall. When you fall, more than 2 meters, you take damage equal to three times the number of meters you fell, and the
damage is not reduced by Protection. Stories in a building while not exactly 2 meters high, roughly correspond to
layers.

#### Flying

Flying is a type of movement that allows you to use your movement to move in the air, as if on solid ground.
Ascending costs double; this means to ascend 2 meters, you need to use 4 meters of your movement. Moving downwards
or horizontally while flying uses your movement as if you were on solid ground. You ignore Difficult Terrain while
flying.

During the turn you lose flight, you can remain in the space you occupy in the air until the end of the turn, and you
fall to the ground at the end of the turn, taking falling damage if you fell more than 2 meters.

#### Contesting Movement

Movement is not always unopposed. A character can attempt to block or trip a creature moving through a space they
occupy. This is resolved by contesting the moving creature's movement Success Test.

When a creature's movement path takes them through a space occupied by a hostile character, that character can choose to
contest the movement. The contest follows the standard rules for Contesting a Test:

1. **The Contester Narrates:** The contesting character describes how they are impeding the movement (e.g., tripping
   them, grabbing them, blocking their path).
2. **The GM Chooses an Attribute:** The GM selects a relevant Attribute for the contest, such as **Strength** to grab or
   **Agility** to trip.
3. **The Contest Roll:** The contester rolls a number of d10s equal to their chosen Attribute.
4. **Eliminating Dice:** For each success (8+) on the contest roll, the contester eliminates one of the highest dice
   from the moving creature's movement Success Test roll. If at the end of it the contested Success Test has no dice
   with 8+, the contested creature is stuck in the same space as the contesting one.

##### Contesting Movement Example

**The Scenario:** Jax is attempting to run past a burly corporate enforcer to reach a control panel. Jax's player spends
1 Action Point for a move action and makes an **Agility** Success Test to determine the total distance. Jax has an
Agility of 4 and rolls `[9, 7, 5, 2]`. The highest die is a 9, so he can move his base 3 spaces + 2 extra spaces (from
the 9, which is 8m, so 2 spaces), for a total of 5 spaces.

The enforcer is standing in a space along Jax's path. As Jax enters the enforcer's space, the GM declares the enforcer
will contest the movement.

**1. The Contest Roll:** The enforcer has a **Strength** of 5. The GM narrates that the enforcer is attempting to grab
Jax as he runs by. The enforcer rolls 5d10 for the contest.

**2. The Result:** The enforcer's roll is `[10, 8, 6, 4, 1]`. Two successes (10 and 8).

**3. Eliminating Dice:** The two successes eliminate the two highest dice from Jax's movement roll. Jax's roll was
`[9, 7, 5, 2]`. The 9 and 7 are eliminated.

**4. Final Outcome:** Jax's movement roll is now `[5, 2]`. The highest die is a 5. Since there are no dice with a result
of 8 or higher, the contest is successful. Jax's movement ends immediately in the enforcer's space. He is stopped in his
tracks, unable to reach the control panel this turn.

#### Difficult Terrain

Not all battlefields are open fields. Movement can be hindered by obstacles, hazardous ground, or changes in
elevation. This is represented by **Difficult Terrain**.

When you move through difficult terrain, every 1 meter of progress costs you 2 meters of your speed.

On a grid, this means that moving into a space containing difficult terrain (such as mud, dense rubble, or thick
vegetation) costs **8 meters** of your movement instead of the usual 4 meters. This rule also applies if the *boundary*
between two otherwise clear spaces is difficult, such as when you are climbing up to a higher ledge or vaulting over a
barricade.

### Space and Occupancy

In Corsair, combat is dynamic and often close-quartered. A single space on the battle map is not limited to one
character. Understanding how multiple characters occupy and interact within a single space is key to tactical success.

A single 4x4 meter space can comfortably house up to **4** standard-sized creatures. The absolute maximum capacity of a
single space is **8** standard-sized creatures. Many actions, especially melee attacks and certain Teamwork maneuvers,
will require you to be in the same space as your target or ally.

#### Outnumbering

Ganging up on a foe is a valid and effective tactic. When you and your allies outnumber your opponents within a single
space, you gain a significant advantage in melee combat.

You receive a number of **Upgrades** on your melee attack tests equal to the difference between the number of allied
creatures and hostile creatures in that space. For example, if 3 allies are in a space with 1 enemy, all allies would
receive 2 Upgrades (3 - 1 = 2) on their melee attacks against that enemy.

#### Melee

You can attack a creature in the same space as you, or an adjacent space. When you attack a creature in an adjacent
space, you move into it, provided it holds less than 4 creatures. If it does, you simply perform the attack from your
current space, but as if you, and all your allies in your space were in the space of the creature you attacked (for
outnumbering purposes).

#### Creature Size

Not all beings are the same size as a typical humanoid. The capacity of a space is affected by the size of the
creatures within it.

* **Large** creatures (like a hulking alien brute) take up the space of **2** standard creatures.
* **Huge** creatures (like a small vehicle or monstrous beast) take up the space of **4** standard creatures.

Some truly massive creatures may be so large that they occupy multiple spaces at once. In these cases, different parts
of the creature (like a giant limb or a tail) might extend into adjacent spaces, counting as a Large or Huge entity in
each of those spaces for the purposes of capacity and targeting.

### Close Quarters Combat (CQC)

Combat in Corsair often gets personal. When you are in the same space as a hostile creature, you are considered to be in
**Close Quarters Combat (CQC)**. This state has significant implications for ranged weaponry.

* **Firing in CQC:** If you attempt to fire a ranged weapon while you are in CQC (i.e., there is an enemy in your
  space), you suffer **3 Downgrades** to your attack test. It is extremely difficult to aim a gun when someone is trying
  to hit you with a sword.
* **Firing into CQC:** If you are outside of a melee but fire into a space where allies and enemies are engaged in CQC,
  you suffer **2 Downgrades** to your attack test. The chaotic swirl of melee combat makes it hard to get a clean shot
  without hitting a friend.

### Cover

Taking cover is a fundamental tactic for surviving a firefight. Many objects and environmental features can provide
cover, offering protection from incoming attacks. When a character is in a space that contains a source of cover (like a
large crate, a sturdy pillar, or a low wall), they can use it to gain a bonus to their Protection. This bonus stacks
with Protection from armor and provides a flat reduction to incoming damage. This bonus only applies against attacks
originating from *outside* of the character's current space.

There are three levels of cover:

* **Light Cover:** (+1 Protection) A small object that offers partial concealment, like a thin pipe or a small barrel.
* **Medium Cover:** (+2 Protection) A solid object that can hide a significant portion of your body, like a large
  engine block or a thick metal bulkhead.
* **Heavy Cover:** (+3 Protection) A large, highly durable object that can almost completely conceal you, like a
  fortified bunker wall or the corner of a building.

#### Destroying Cover

Cover can be destroyed. Light, Medium, and Heavy Cover have 4, 8, and 12 health segments and a Protection of 4, 8, and
12 respectively. Attacking cover is a Success Test instead of a Complex one. For every 4 damage the cover takes, its
provided Protection benefit is reduced by 1.

#### Cover Facing

Using cover effectively is about more than just standing behind something; it's about angling yourself against incoming
fire. The first time you take an attack where you'd benefit from the bonus, you draw a line from the attacker and
whichever side of your space it crosses becomes side that grants you the bonus. This represents which side of the
physical cover in your space you are on.

When the line of attack crosses a corner, both adjecent sides become covering sides.

On any subsequent attacks during the turn:

* **Full Bonus:** If the line of attack crosses the covering side, you receive the full Protection bonus from the cover.
* **Reduced Bonus:** If the line of attack crosses one of the two sides *adjacent* to the covering side, the
  Protection bonus is reduced by 1 on a hex grid, and by 2 on a square grid.
* **No Bonus:** If the line of attack crosses the side *not* adjacent to the covering side, you gain no benefit from the
  cover against that attack. You are considered exposed.
