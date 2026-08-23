# Condition

Condition represents your character's ability to withstand the physical and mental rigors of a life of adventure. Instead of relying on a simple pool of hit points, your character tracks resilience across two distinct categories: **Physical Condition** and **Mental Condition**. Physical Condition measures physical well-being against injuries, toxins, and physical exertion, determined by your **Endurance** attribute. Mental Condition measures emotional fortitude against terror, psychological trauma, and overwhelming stress, determined by your **Willpower** attribute.

Both Physical and Mental Condition are divided into three linked, sequential **Tracks** (Track I, Track II, and Track III). Whenever your character suffers damage or stress, you mark off segments starting on Track I. Once a Track becomes completely full, any subsequent damage instances naturally carry over into the next Track in the sequence. Each Track has a capacity equal to **4 + your relevant Derived Attribute** (4 + Endurance for Physical Tracks, and 4 + Willpower for Mental Tracks).

---

## Damage Types and Attribute Penalties

Harm is categorized into **Light Wounds** (standard damage) and **Aggravated Wounds** (severe trauma). When an incoming source of damage is large enough to overflow the remaining capacity of a Track, the overflow damage turns Light Wounds on that filled Track into **Aggravated Wounds**. Aggravated Wounds represent deep trauma that cannot be restored through standard Lesser Healing methods. Once a Track is completely filled, any subsequent damage instances proceed into the next Track in sequence.

Filling an individual Track inflicts physical or mental strain, resulting in specific Attribute penalties:

* **Impaired (Light Wounds):** When an individual Track becomes completely filled with Light Wounds, you select and mark one corresponding Attribute on your character sheet (a Physical Attribute for Physical Tracks, or a Mental Attribute for Mental Tracks). That Attribute becomes **Impaired** (e.g., *Impaired Strength*, *Impaired Instinct*). From that moment on, whenever a test involves an Impaired Attribute, you suffer **1 Downgrade** on that roll.
* **Crippled (Aggravated Wounds):** If an individual Track becomes completely filled with Aggravated Wounds, the marked Attribute becomes **Crippled** (e.g., *Crippled Strength*, *Crippled Instinct*). From that point forward, any test involving a Crippled Attribute suffers **2 Downgrades** instead.

---

## Healing and Recovery Across Scene Scopes

Recovery is categorized into two distinct types based on the severity of the injury. **Lesser Healing** restores standard filled segments (Light Wounds) on your Condition Tracks, but is incapable of repairing Aggravated Wounds. **Greater Healing** represents intensive treatment and deep rest capable of clearing Aggravated Wounds. Each specific healing method defines its exact segment restoration costs.

Your opportunities for recovery naturally depend on the pacing of the current scene:

* **Moment-to-Moment Pacing:** In the heat of active combat or immediate crisis, healing is restricted to rapid battlefield supplies, such as stim-packs or specialized class abilities, which function according to their specific item or trait rules.
* **Place-to-Place Pacing:** When your crew pauses to take a breath during exploration, characters gain access to Lesser Healing through a **Short Rest**. A character can make a **Success Test** using **Endurance + Willpower**. For every 2 Success Points generated (rounded down), the character heals 1 Light Wound segment on either their Physical or Mental Condition.
* **Day-to-Day Pacing:** During extended downtime, characters gain access to Greater Healing through a **Long Rest**. When resting for a significant period, a character makes a **Success Test** using **Endurance + Willpower**. Success Points generated from this test can be freely allocated across both Physical and Mental Condition to heal Light Wounds (1 Success Point per segment) or clear Aggravated Wounds (2 Success Points per segment). Characters may also visit specialized medical facilities, such as clinics or a ship's medbay, which provide additional recovery benefits.

---

## Consequences of Full Condition

Filling all three Tracks of your Physical or Mental Condition brings severe overall consequences:

* **Physical Condition Consequences:** When all three Physical Tracks are filled with any combination of Light or Aggravated Wounds, your character falls **Unconscious** and cannot act until at least one segment is cleared. If every single segment across all three Physical Tracks becomes filled entirely with **Aggravated Wounds**, your character **Dies**.
* **Mental Condition Consequences:** When all three Mental Tracks become filled, your character is mentally overwhelmed; you **cannot earn or spend Gambit Dice**, though you retain any Gambit Dice currently in your pool until at least one mental segment is cleared. If all three Mental Tracks are filled entirely with **Aggravated Wounds**, your mental resilience collapses, leaving your character **susceptible to suggestions, commands, and intimidation** from others in the exact same manner that non-player characters are susceptible to such actions from player characters.

---

## Example: Damage, Attribute Penalties, and Recovery in Action

> During a heavy firefight, Jax takes 8 physical damage from a single blast. Jax has an Endurance of 3, giving his Physical Condition three Tracks of 7 segments each (4 + 3). The first 7 points of damage fill Track I completely with Light Wounds. Jax marks his **Strength** Attribute as **Impaired**, meaning any future test involving Strength will suffer **1 Downgrade**. The 1 point of overflow damage turns 1 Light Wound on Track I into an **Aggravated Wound** (leaving Track I with 6 Light Wounds and 1 Aggravated Wound). Any subsequent damage will now proceed into Track II.
> 
> Later, during a **Long Rest**, Jax makes an **Endurance (3) + Willpower (2)** Success Test using his lower Attribute (**Willpower 2**), rolling `[4, 9]`. The `9` yields 9 base Success Points. Jax spends 2 Success Points to heal the 1 Aggravated Wound on Track I (costing 2 Success Points per segment), and spends 6 Success Points to heal the remaining 6 Light Wounds on Track I (costing 1 Success Point per segment). With Track I completely cleared and no longer full, Jax removes the **Impaired** condition from his Strength Attribute, restoring his rolls to normal.
