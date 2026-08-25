# Lean Core Rules Reference (Knowledge Base)

This document serves as a lean reference for the core mechanics of Corsair. It covers only Attributes, Simple Tests, Complex Tests, Success Tests, Action Points, and Effects.

---

## 1. Attributes

An **Attribute** is a numerical value (typically rated 1 to 10 for characters) representing a capability or characteristic of a person, creature, item, or vessel. Higher Attribute ratings grant larger dice pools and greater chances of success.

### Core Attributes
Characters are defined by six Core Attributes:

* **Physical Attributes**:
  * **Strength**: Physical power, muscular force, lifting, forcing, and grappling.
  * **Agility**: Speed, reflexes, physical coordination, dodging, and acrobatics.
  * **Finesse**: Precision, fine motor skills, lockpicking, surgery, and aiming.
* **Mental Attributes**:
  * **Knowledge**: Education, technical capability, hacking, repairs, and memory recall.
  * **Presence**: Force of personality, charisma, negotiation, intimidation, and inspiration.
  * **Instinct**: Intuition, awareness, detecting traps, sensing lies, and snap reactions.

### Derived Attributes
* **Endurance**: Equal to the value of your second-highest Physical Attribute (Strength, Agility, Finesse). Represents physical resilience.
* **Willpower**: Equal to the value of your second-highest Mental Attribute (Knowledge, Presence, Instinct). Represents mental fortitude.

### Attribute Pairs
When performing an action requiring a test, the GM pairs the two most relevant Attributes (e.g., **Accuracy + Finesse** or **Strength + Strength**) to form the foundation of the test pool.

---

## 2. Simple Tests

Used when an action has a binary outcome: **complete success or complete failure**.

* **Dice Pool**: Take a number of d10s equal to the **higher** Attribute in the pair.
* **Resolution**: Roll the pool. If at least one die shows **8 or higher** (a Hit), the test **succeeds**. If no die shows 8+, the test **fails**.

---

## 3. Complex Tests

Used when an action requires determining both **if it succeeds** and **how well it succeeds** (e.g., combat attacks).

1. **Action Roll**: Roll d10s equal to the **higher** Attribute in the pair.
   * If the highest die is **7 or lower**, the action **fails**.
   * If at least one die is **8 or higher**, the action **succeeds**, and you proceed to the Success Roll.
2. **Success Roll**: Take a number of dice from the successful roll equal to the **lower** Attribute in the pair.
   * The highest single die value among these selected dice represents your **Success Points**.

---

## 4. Success Tests

Used when an action is **guaranteed to succeed**, but the **degree or quality of success** varies based on available time or effort.

* **Dice Pool**: Roll d10s equal to the **higher** Attribute in the pair.
* **Resolution**: The highest single die value in the pool becomes your **Success Points** measuring how effectively the action was performed.

---

## 5. Upgrades and Downgrades

Situational factors modify test dice pools through **Upgrades** (advantages) and **Downgrades** (disadvantages).

* **Cancellation & Limits**: Upgrades and Downgrades cancel each other 1-to-1. The net result is capped at a maximum of **6 Upgrades** or **6 Downgrades**.
* **Upgrades**:
  * Step up one d10 in your pool to a **d12** per net Upgrade.
  * If all dice in the pool are already d12s, each additional Upgrade adds a new **d10** to the pool.
* **Downgrades**:
  * Step down one d10 in your pool to a **d8** per net Downgrade.
  * If all dice in the pool are already d8s, each additional Downgrade removes a **d8** from the pool.
  * If all dice are removed, roll **2d8 and take the lower result**.

---

## 6. Action Points

Action Points (AP) represent the currency spent to perform actions during play.

* **Maximum**: Every character and creature has a maximum of **3 Action Points**.
* **Cost**: Every test (Simple, Success, or Complex) costs **1 AP**. Non-test narrative actions (e.g., moving between major locations) may also cost 1 AP at the GM's discretion.
* **Refill**: At the start of every Round, Action Points refill to maximum.
* **Turn Pacing**: In structured scenes, control swaps between players and GM after the active side spends **2 or more AP** and completes their active action.

---

## 7. Effects

Effects allow characters to create tactical advantages, narrative twists, or environmental changes by sacrificing **Hits** (dice showing 8+) rolled during a test.

### Activating Effects
To activate an effect, sacrifice Hits from an Action Roll or Success Roll as indicated by the effect type. The effect must align logically with your declared narration and Attribute Pair.

### Action Effects (Activated on Action Roll)
* **Chain Effect**: Spend 1 Hit per additional target eligible for the same test. (For Complex Tests, make one Success Roll and apply the highest result to all targets. Cannot chain actions that already affect multiple targets; resource costs must be paid per target).
* **Push Effect**: Spend Hits to push a target 4 meters. You may move along with them.
* **Upgrade/Downgrade Effect**: Spend Hits to upgrade or downgrade a die on subsequent rolls related to the advantage/disadvantage created (can apply immediately to the current Complex Test's Success Roll).
* **Blocker Effect**: Spend 2 Hits per set-aside Hit to hinder a future action. Each set-aside Hit negates the highest die on an opponent's test attempting that action.
* **Persistent Blocker Effect**: A Blocker Effect (costing 2 Hits per set-aside Hit) where the set-aside Hit pool resets after each blocked action. Ends when an action succeeds despite the blocker or conditions no longer apply.

### Success Effects (Activated on Success Roll)
* **Crit Effect**: Spend Hits on a Success Roll to increase total Success Points by **+2 per Hit spent**.

### Trigger Effects
* **Trigger Effect**: Spend 1 AP and declare a trigger condition and intended action. When triggered, roll the test immediately. Requires concentration (lost if taking another test or taking damage/interrupted). AP counts towards turn limit when spent.
* **Persistent Trigger Effect**: A Trigger Effect requiring no concentration (used primarily for deployed items, traps, etc.).

### Removing Effects
A creature in a position to remove an ongoing effect can spend an action and make a **Simple Test** to eliminate 1 Hit set aside for that effect.
