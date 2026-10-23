# -*- coding: utf-8 -*-
"""
Generate verbatim, continuous-flow html/04_Armory_and_Gear.html.
18 pages (9 complete two-page spreads: Pages 68 to 85).
Preserves 100% of markdown source text from:
- rulebook/combat/Combat.md
- rulebook/equipment/Equipment.md
- rulebook/equipment/Firearms.md
- rulebook/equipment/Melee.md
- rulebook/equipment/Armor.md
- rulebook/equipment/Gear.md
- rulebook/equipment/Exotic_Hardware.md
"""

from pathlib import Path

def build_full_fidelity_ch04():
    pages = []

    # =========================================================================
    # SPREAD 1 (Pages 68-69): COMBAT MOVEMENT, VERTICALITY, FLYING & CONTESTING
    # =========================================================================

    p68 = """    <!-- =========================================================================
         PAGE 68 (Spread 1 Left) — CHAPTER 04 OPENER: COMBAT & TACTICAL MOVEMENT
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="combat-movement">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Movement</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Combat &amp; The Armory</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the world of Corsair, conflict is inevitable. Whether facing down a squad of corporate enforcers, battling a monstrous alien in the depths of a derelict ship, or engaging in a desperate firefight across depressurized docking gantries, combat is a thrilling and dangerous reality of high-frontier survival. When conflict turns violent and every action matters, the game shifts into <strong>Moment to Moment</strong> pacing. While you can resolve combat using "theater of the mind," employing a grid-based battle map adds tactical depth and clarity to character and enemy positioning.
            </p>

            <h3 style="margin-top: 1mm;">Movement</h3>
            <p>
                Navigating the battlefield is crucial for survival. Positioning determines cover, line of sight, and your ability to engage or evade foes. In combat, you can spend <strong>1 Action Point (AP)</strong> to move. When you move, you perform a <strong>Success Test</strong>, typically with <strong>Agility</strong>, then move a number of meters equal to the result, plus your base speed (by default, <strong>4 meters</strong>).
            </p>
            <p>
                The Success Test is typically made with your Agility attribute, representing your ability to run, climb, and vault across terrain. The GM may call for a different attribute based on the situation (e.g., Strength for climbing a sheer cliff).
            </p>

            <h3>Movement on a Grid</h3>
            <p>
                For ease of play, use a battle grid with squares or hexes representing a <strong>4 meter diameter circle</strong>. On a grid, movement is calculated as follows:
            </p>
            <ul>
                <li>Your base speed of 4 meters translates to <strong>1 space</strong>.</li>
                <li>Your Success Test adds additional movement: divide the number of meters rolled on your test by four, rounding up, and move an additional number of spaces equal to the result.</li>
            </ul>
            <p>
                A single move action covers a maximum of 16 meters (4 spaces). Because a player can spend multiple Action Points on movement, the potential distances can be significant.
            </p>

            <h3>Verticality</h3>
            <p>
                Since the world is not a 2D plane, you can move up and down as well as left and right. When the situation introduces verticality, you can model this by adding more layers of flat horizontal grids on top of each other. These layers are separated by <strong>2 meters</strong>, and moving up and down between layers is always considered difficult terrain, unless of course, you fall.
            </p>
            <p>
                When you fall more than 2 meters, you take damage equal to <strong>three times the number of meters you fell</strong>, and the damage is completely <strong>unmitigated by Protection</strong>. Stories in a building, while not exactly 2 meters high, roughly correspond to tactical layers.
            </p>

            <h3>Flying</h3>
            <p>
                Flying is a type of movement that allows you to use your movement to move in the air, as if on solid ground. Ascending costs double; this means to ascend 2 meters, you need to use 4 meters of your movement. Moving downwards or horizontally while flying uses your movement as if you were on solid ground. You ignore Difficult Terrain while flying.
            </p>
            <p>
                During the turn you lose flight, you can remain in the space you occupy in the air until the end of the turn, and you fall to the ground at the end of the turn, taking falling damage if you fell more than 2 meters.
            </p>

            <h3>Difficult Terrain</h3>
            <p>
                Not all battlefields are open fields. Movement can be hindered by obstacles, hazardous ground, or changes in elevation. This is represented by <strong>Difficult Terrain</strong>. When you move through difficult terrain, every 1 meter of progress costs you 2 meters of your speed. On a grid, this means that moving into a space containing difficult terrain (such as mud, dense rubble, or thick vegetation) costs <strong>8 meters</strong> of your movement instead of the usual 4 meters.
            </p>
            <p>
                This rule also applies if the <em>boundary</em> between two otherwise clear spaces is difficult, such as when you are climbing up to a higher ledge or vaulting over a barricade.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">68</span>
        </div>
    </div>"""
    pages.append(p68)

    p69 = """    <!-- =========================================================================
         PAGE 69 (Spread 1 Right) — CONTESTING MOVEMENT, SPACE & OCCUPANCY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="contesting-movement">
        <div class="page-running-header">
            <span>Chapter 04: Tactical Movement</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Contesting Movement</h3>
            <p>
                Movement is not always unopposed. A character can attempt to block or trip a creature moving through a space they occupy. This is resolved by contesting the moving creature's movement Success Test.
            </p>
            <p>
                When a creature's movement path takes them through a space occupied by a hostile character, that character can choose to contest the movement. The contest follows the standard rules for Contesting a Test:
            </p>
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 2mm;">
                <li><strong>The Contester Narrates:</strong> The contesting character describes how they are impeding the movement (e.g., tripping them, grabbing them, blocking their path).</li>
                <li><strong>The GM Chooses an Attribute:</strong> The GM selects a relevant Attribute for the contest, such as <strong>Strength</strong> to grab or <strong>Agility</strong> to trip.</li>
                <li><strong>The Contest Roll:</strong> The contester rolls a number of d10s equal to their chosen Attribute.</li>
                <li><strong>Eliminating Dice:</strong> For each success (8+) on the contest roll, the contester eliminates one of the highest dice from the moving creature's movement Success Test roll. If at the end of it the contested Success Test has no dice with 8+, the contested creature is stuck in the same space as the contesting one.</li>
            </ol>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 2.5mm 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: Contesting Jax's Movement</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>The Scenario:</strong> Jax is attempting to run past a burly corporate enforcer to reach a control panel. Jax spends 1 Action Point for a move action and makes an <strong>Agility</strong> Success Test to determine the total distance. Jax has Agility 4 and rolls <code>[9, 7, 5, 2]</code>. The highest die is a 9, so he can move his base 1 space (4m) plus 2 extra spaces (from the 9, which is 8m, rounded up to 2 spaces), for a total of 3 spaces.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    The enforcer stands along Jax's path. As Jax enters the enforcer's space, the GM declares the enforcer will contest the movement using <strong>Strength 5</strong> to grab him.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. The Contest Roll:</strong> The enforcer rolls 5d10: <code>[10, 8, 6, 4, 1]</code>—generating two successes (10 and 8).
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>2. Eliminating Dice:</strong> The two successes eliminate the two highest dice from Jax's movement roll (<code>[9, 7, 5, 2]</code>). The 9 and 7 are eliminated.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    <strong>3. Final Outcome:</strong> Jax's remaining pool is <code>[5, 2]</code>. Since there are no dice showing 8 or higher, the contest succeeds. Jax's movement ends immediately in the enforcer's space, stopped dead in his tracks.
                </p>
            </div>

            <h3>Space and Occupancy</h3>
            <p>
                In Corsair, combat is dynamic and often close-quartered. A single space on the battle map is not limited to one character. Understanding how multiple characters occupy and interact within a single space is key to tactical success. A single 4x4 meter space can comfortably house up to <strong>4 standard-sized creatures</strong>. Many actions, especially melee attacks and certain Teamwork maneuvers, require you to be in the same space as your target or ally.
            </p>

            <h4>Outnumbering</h4>
            <p>
                Ganging up on a foe is a valid and effective tactic. When you and your allies outnumber your opponents within a single space, you gain a significant advantage in melee combat. You receive a number of <strong>Upgrades</strong> on your melee attack tests equal to the difference between the number of allied creatures and hostile creatures in that space. For example, if 3 allies are in a space with 1 enemy, all allies receive <strong>2 Upgrades</strong> (3 &minus; 1 = 2) on their melee attacks against that enemy.
            </p>

            <h4>Melee Positioning</h4>
            <p>
                You can attack a creature in the same space as you, or an adjacent space. Melee attacks must use any combination of two separate Physical Attributes. For example, Jax might combine <strong>Strength + Agility</strong> to drive a heavy blade through a pirate's defense, or pair <strong>Agility + Finesse</strong> when aiming a swift, precise knife strike at a weak point in armor.
            </p>
            <p>
                When you attack a creature in an adjacent space, you move into it, provided it holds less than 4 creatures. If it does hold 4, you perform the attack from your current space, but as if you and all your allies in your space were in the target's space for outnumbering purposes.
            </p>

            <h4>Creature Size</h4>
            <p>
                Not all beings are the same size as a typical humanoid. The capacity of a space is affected by the size of the creatures within it:
            </p>
            <ul>
                <li><strong>Large</strong> creatures (like a hulking alien brute) take up the space of <strong>2</strong> standard creatures.</li>
                <li><strong>Huge</strong> creatures (like a small vehicle or monstrous beast) take up the space of <strong>4</strong> standard creatures.</li>
            </ul>
            <p>
                Truly massive creatures may occupy multiple spaces at once, counting as a Large or Huge entity in each space for capacity and targeting.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">69</span>
        </div>
    </div>"""
    pages.append(p69)

    # =========================================================================
    # SPREAD 2 (Pages 70-71): CQC, COVER, DESTROYING COVER & THE ARMORY INTRO
    # =========================================================================

    p70 = """    <!-- =========================================================================
         PAGE 70 (Spread 2 Left) — CLOSE QUARTERS COMBAT & COVER TACTICS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="cqc-and-cover">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Cover &amp; Close Quarters</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Close Quarters Combat (CQC)</h3>
            <p>
                Combat in Corsair often gets personal. When you are in the same space as a hostile creature, you are considered to be in <strong>Close Quarters Combat (CQC)</strong>. This state has significant implications for ranged weaponry:
            </p>
            <ul>
                <li><strong>Firing in CQC:</strong> If you attempt to fire a ranged weapon while you are in CQC (i.e., there is an enemy in your space), you suffer <strong>2 Downgrades</strong> to your attack test. Wielding long guns or aiming precision optics while parrying bayonets or dodging claws is intensely difficult.</li>
                <li><strong>Firing into CQC:</strong> If you are outside of a melee but fire into a space where allies and enemies are engaged in CQC, you suffer <strong>1 Downgrade</strong> to your attack test. The chaotic swirl of close-quarters combat makes it hazardous to get a clean shot without endangering friends.</li>
            </ul>

            <h3>Cover</h3>
            <p>
                Taking cover is a fundamental tactic for surviving a firefight. Many objects and environmental features can provide cover, offering protection from incoming attacks. When a character is in a space that contains a source of cover (like a large crate, a sturdy pillar, or a low wall), they can use it to gain a bonus to their Protection.
            </p>
            <p>
                This bonus stacks with Protection from armor and shields, providing a flat reduction to incoming damage. This bonus only applies against attacks originating from <em>outside</em> of the character's current space.
            </p>
            <p>
                There are three standard levels of cover:
            </p>
            <ul>
                <li><strong>Light Cover:</strong> (<strong>+1 Protection</strong>) A small object that offers partial concealment, like a thin pipe, light furniture, or a small fuel drum.</li>
                <li><strong>Medium Cover:</strong> (<strong>+2 Protection</strong>) A solid object that can hide a significant portion of your body, like a large engine block, reinforced crate, or thick metal bulkhead.</li>
                <li><strong>Heavy Cover:</strong> (<strong>+3 Protection</strong>) A large, highly durable fortification that can almost completely conceal you, like a fortified bunker wall, blast gantry, or armored vehicle chassis.</li>
            </ul>

            <h3>Destroying Cover</h3>
            <p>
                Cover is not indestructible. Light, Medium, and Heavy Cover have <strong>12, 24, and 36 health segments</strong> and an innate Protection of <strong>4, 8, and 12</strong> respectively when directly targeted. Attacking cover is a <strong>Success Test</strong> instead of a Complex one.
            </p>
            <p>
                For every 12 damage the cover absorbs, its provided Protection benefit is reduced by 1. Specialized breaching charges, anti-materiel weapons, and demolition explosives specifically ignore cover's innate Protection, shredding barricades in seconds.
            </p>

            <h3>Cover Facing</h3>
            <p>
                Using cover effectively is about more than just crouching in a space; it requires angling yourself against incoming lines of fire. The first time you take an attack where you would benefit from cover, draw a line from the attacker to your center: whichever side of your space the line crosses becomes your <strong>covering side</strong>. This represents which side of the physical barrier you are currently sheltering behind.
            </p>
            <p>
                When the line of attack crosses a corner of your space, both adjacent sides become covering sides.
            </p>
            <p>
                On any subsequent attacks during the combat round:
            </p>
            <ul>
                <li><strong>Full Bonus:</strong> If the line of attack crosses the covering side, you receive the full Protection bonus from the cover.</li>
                <li><strong>Reduced Bonus:</strong> If the line of attack crosses one of the two sides <em>adjacent</em> to the covering side, the Protection bonus is reduced by 1 on a hex grid, and by 2 on a square grid.</li>
                <li><strong>No Bonus (Exposed):</strong> If the line of attack crosses the side <em>not</em> adjacent to the covering side, you gain no benefit from the cover against that attack. You are outflanked and completely exposed.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""
    pages.append(p70)

    p71 = """    <!-- =========================================================================
         PAGE 71 (Spread 2 Right) — THE ARMORY & EQUIPMENT INVARIANTS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armory-and-equipment">
        <div class="page-running-header">
            <span>Chapter 04: The Armory &amp; Equipment</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">The Armory &amp; Equipment</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                Not every item a character carries has a significant mechanical impact on the game. Everyday objects like personal commlinks, apartment keys, or sentimental trinkets are assumed to be part of a character's belongings without needing specific rules. However, items that provide a distinct tactical advantage—from weapons and armor to specialized tools—are classified as <strong>Equipment</strong>. These items are governed by the <strong>Load</strong> system.
            </p>

            <h3>The Load Invariant</h3>
            <p>
                Every piece of mechanically significant equipment has a <strong>Load</strong> value, representing its weight, physical bulk, and cumbersomeness. A character's ability to carry this equipment is strictly limited by their physical conditioning:
            </p>
            <div class="callout callout-tactical keep-together" style="margin: 2mm 0; padding: 2.2mm 2.8mm; text-align: center;">
                <div style="font-family: var(--font-heading); font-size: 11pt; font-weight: 700; color: var(--color-gold);">
                    Maximum Load Capacity = 12 + (Strength &times; 2)
                </div>
            </div>
            <p>
                This limit is absolute; a character cannot carry items with a total Load value exceeding this capacity under any circumstances. It is often a wise tactical decision to leave some of your Load capacity unused. An open slot might be exactly what you need to carry a vital piece of salvage or a mission-critical objective discovered during an operation.
            </p>

            <h3>Equipment Categories</h3>
            <p>
                Equipment across the settled systems is divided into three major categories:
            </p>
            <ul>
                <li><strong>Weapons:</strong> Hardware engineered to inflict physical harm. Divided into Firearms and Melee Weapons.</li>
                <li><strong>Armor:</strong> Protective gear worn to reduce or negate incoming kinetic and thermal damage.</li>
                <li><strong>Exotic Hardware:</strong> Classified prototypes, black-budget skunkworks gear, and salvaged Precursor relics with extraordinary tactical properties.</li>
            </ul>

            <h3>Weapons &amp; The Damage Bonus</h3>
            <p>
                While Firearms and Melee Weapons function differently, all weapons share a common foundational statistic: the <strong>Damage Bonus</strong>.
            </p>
            <p>
                The Damage Bonus is a flat numerical value added directly to the total success points you generate on a successful attack roll. However, these bonus points can only be used to increase the damage dealt and cannot be spent to activate other effects (such as Upgrades, Crits, or Teamwork maneuvers). Heavier weapons chambered in larger calibers or forged with dense cutting heads possess substantially larger flat Damage Bonuses.
            </p>

            <h3>Equipment Damage &amp; Field Repairs</h3>
            <p>
                Deployable gear, fortifications, vehicles, and technological hardware possess structure ratings measured in <strong>Health Points (HP)</strong>. When an item takes damage from enemy fire, detonations, or environmental hazards, its HP is reduced accordingly. If an item is reduced to 0 HP, it is disabled and ceases to function until repaired.
            </p>
            <p>
                An operator carrying a toolkit with the <strong>Tinkering</strong> attribute can perform field maintenance to restore damaged hardware:
            </p>
            <ul>
                <li><strong>Repairing Equipment:</strong> Restoring HP to damaged equipment costs <strong>1 AP</strong> (in structured combat) or standard narrative time (in downtime) and requires a <strong>Success Test</strong> using <strong>Tinkering + Knowledge</strong>.</li>
                <li><strong>HP Restored:</strong> The item immediately recovers <strong>1 HP per Success Point</strong> generated on the test, up to its maximum HP rating. Repairing completely destroyed or vaporized equipment requires dedicated workshop facilities and spare components at the GM's discretion.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">71</span>
        </div>
    </div>"""
    pages.append(p71)

    # =========================================================================
    # SPREAD 3 (Pages 72-73): FIREARMS STATS, MANUFACTURERS & HANDGUNS/SMGS
    # =========================================================================

    p72 = """    <!-- =========================================================================
         PAGE 72 (Spread 3 Left) — FIREARMS STATISTICS & CONGLOMERATES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-overview">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms &amp; Munitions</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Firearms</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the cold vacuum of space, across contested orbital platforms, and inside pressurized ship corridors, firearms are the ultimate arbiters of ranged combat. Ranging from rugged chemical-propellant slugthrowers to electro-thermal chemical (ETC) rifles and high-velocity magnetic rail drivers, firearms give Corsairs the range, stopping power, and suppression capability necessary to overwhelm hostile forces before they close the distance.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <p>
                Every firearm is defined by mechanical attributes dictating its performance across engagement distances and how it pairs with combat attributes:
            </p>
            <ul>
                <li><strong>Accuracy (Short / Medium / Long / Extreme):</strong> Calibrated operational distances. Accuracy provides four numerical ratings corresponding to the four standard combat Range Bands. Ranged attack tests are always resolved using <strong>Accuracy + Finesse</strong>, pairing the weapon's Accuracy at the target's range with the character's Finesse:
                    <ul>
                        <li><strong>Short Range (S):</strong> 0–5 spaces (~0–20 meters). Tight corridors, cabin breeches, point-blank skirmishes.</li>
                        <li><strong>Medium Range (M):</strong> 6–12 spaces (~20–40 meters). Standard cargo bays, hangar decks, station concourses.</li>
                        <li><strong>Long Range (L):</strong> 13–20 spaces (~40–80 meters). Maintenance tunnels, hull gantries, open terrain.</li>
                        <li><strong>Extreme Range (E):</strong> 20+ spaces (~80+ meters). Perimeter defense, open surfaces, sniper perches. A dash (<code>&minus;</code>) indicates the weapon cannot engage at that distance.</li>
                    </ul>
                </li>
                <li><strong>Rate of Fire (RoF):</strong> Cyclic rate and burst control. RoF sets a strict upper limit on the total number of <strong>Crit Effects</strong> and <strong>Chain Effects</strong> activated on a single attack roll:
                    <ul>
                        <li><strong>Heavy-Hitters (RoF 0):</strong> Single-shot rifles, heavy revolvers, slug guns. Deliver massive single impacts; cannot trigger RoF-based Crits or Chain onto secondary targets.</li>
                        <li><strong>Precision &amp; Semi-Auto (RoF 1):</strong> Duty pistols, marksman rifles, tactical shotguns (up to 1 Crit or Chain effect).</li>
                        <li><strong>Burst &amp; Automatic (RoF 2):</strong> Assault carbines, combat shotguns, compact SMGs (up to 2 Crit/Chain effects).</li>
                        <li><strong>Rapid Suppression &amp; Rotary (RoF 3–4):</strong> Automatic rifles, squad automatic weapons, heavy machine guns, rotary autocannons built for wide-angle saturation (up to 3–4 Crit/Chain effects).</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to success points on a successful hit. Heavier calibers feature substantially larger flat Damage Bonuses.</li>
                <li><strong>Hands:</strong> Sidearm designed for one hand (<strong>1H</strong>) or shoulder-fired platform requiring two hands (<strong>2H</strong>).</li>
                <li><strong>Load &amp; Cost:</strong> Mass in the Load system and galactic market price in Credits.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p>
                While the catalog lists universal functional archetypes, individual models found across the cosmos are produced by major conglomerates:
            </p>
            <ul>
                <li><strong>Panthera Arms:</strong> Sleek, high-tolerance carbines and designated marksman rifles favored by corporate strike teams.</li>
                <li><strong>Vandal's Workshop:</strong> Rugged, stamped-sheet firearms and high-RoF submachine guns built to cycle reliably in dirt, sand, and vacuum.</li>
                <li><strong>Caldera Foundry:</strong> Devastating heavy-bore rifles and trench shotguns designed for brutal close-quarters boarding defense.</li>
                <li><strong>Ker'Satz Korp:</strong> Precision magnetic-assisted rail drivers and heavy revolvers engineered for maximum armor penetration and stopping power.</li>
                <li><strong>Chidori-Qwei Combatwear:</strong> Lightweight polymer sidearms, integrated smart-linked machine pistols, and rapid-response tactical weapons.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">72</span>
        </div>
    </div>"""
    pages.append(p72)

    p73 = """    <!-- =========================================================================
         PAGE 73 (Spread 3 Right) — HANDGUNS, SUBMACHINE GUNS & SHOTGUNS CATALOG
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-catalog-short">
        <div class="page-running-header">
            <span>Chapter 04: Firearms Catalog</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Firearms Catalog</h3>
            <h4>Handguns</h4>
            <p>
                Compact sidearms designed for personal defense, emergency boarding backup, and rapid close-quarters deployment.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Handguns Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Weapon Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.2mm 1.2mm;">RoF</th>
                            <th style="padding: 1.2mm 1.2mm;">H</th>
                            <th style="padding: 1.2mm 1.2mm;">Dmg</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Holdout Pistol</td>
                            <td>2 / 1 / &minus; / &minus;</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>300</td>
                            <td>Ultra-compact concealable polymer pistol designed for covert carry and last-ditch defense.</td>
                        </tr>
                        <tr>
                            <td class="bold">Service Pistol</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>800</td>
                            <td>Standard-issue semi-automatic sidearm offering reliable cycling and balanced handling.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Revolver</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>1,200</td>
                            <td>Large-frame cylinder handgun firing high-grain magnum cartridges with punishing recoil.</td>
                        </tr>
                        <tr>
                            <td class="bold">Machine Pistol</td>
                            <td>3 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1</td>
                            <td>1,500</td>
                            <td>Compact automatic handgun capable of dumping high-volume bursts in point-blank skirmishes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hand Cannon</td>
                            <td>2 / 3 / 2 / 0</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>2,200</td>
                            <td>Massive reinforced handgun chambered in anti-armor kinetic rounds for devastating single shots.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Submachine Guns &amp; Shotguns</h4>
            <p>
                Close-quarters primary weapons engineered for boarding operations, clearing tight ship bulkheads, and dominating short-range firefights.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Submachine Guns &amp; Shotguns Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Weapon Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.2mm 1.2mm;">RoF</th>
                            <th style="padding: 1.2mm 1.2mm;">H</th>
                            <th style="padding: 1.2mm 1.2mm;">Dmg</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Compact SMG</td>
                            <td>4 / 3 / 1 / &minus;</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+1</td>
                            <td>2</td>
                            <td>2,000</td>
                            <td>Lightweight collapsible submachine gun designed for vehicle crews and shipboard boarding teams.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical SMG</td>
                            <td>3 / 4 / 2 / 0</td>
                            <td>3</td>
                            <td>2H</td>
                            <td>+1</td>
                            <td>2</td>
                            <td>2,800</td>
                            <td>Balanced automatic platform featuring integral recoil compensators and high cyclic fire rates.</td>
                        </tr>
                        <tr>
                            <td class="bold">Trench Shotgun</td>
                            <td>5 / 2 / &minus; / &minus;</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>2</td>
                            <td>2,400</td>
                            <td>Heavy pump-action smoothbore scattergun delivering catastrophic kinetic spread at point-blank range.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Shotgun</td>
                            <td>4 / 3 / 0 / &minus;</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>3,500</td>
                            <td>Semi-automatic magazine-fed shotgun engineered for rapid room clearing and breaching operations.</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Scattergun</td>
                            <td>4 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,000</td>
                            <td>Fully automatic drum-fed scattergun delivering overwhelming short-range projectile swarms.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.30; color: var(--text-muted); margin-top: 1mm;">
                <em>Corridor Ballistics:</em> In pressurized habitats, pump-action shotguns and low-velocity submachine guns are preferred by boarding crews because heavy kinetic pellets flatten against reinforced bulkheads rather than puncturing environmental seals or fuel lines.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">73</span>
        </div>
    </div>"""
    pages.append(p73)

    # =========================================================================
    # SPREAD 4 (Pages 74-75): RIFLES, HEAVY SUPPORT, DUAL WIELDING & WALKTHROUGH
    # =========================================================================

    p74 = """    <!-- =========================================================================
         PAGE 74 (Spread 4 Left) — RIFLES & HEAVY SUPPORT WEAPONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-rifles-heavy">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Rifles &amp; Heavy Weapons</span>
        </div>

        <div class="page-body two-columns">
            <h4 style="margin-top: 0;">Rifles</h4>
            <p>
                Versatile long guns that balance effective range, stopping power, and tactical flexibility across ship corridors and planetary battlegrounds.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Rifles Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Weapon Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.2mm 1.2mm;">RoF</th>
                            <th style="padding: 1.2mm 1.2mm;">H</th>
                            <th style="padding: 1.2mm 1.2mm;">Dmg</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Assault Carbine</td>
                            <td>3 / 3 / 2 / 1</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>3,800</td>
                            <td>Short-barreled rifle optimized for high mobility, fast target acquisition, and medium-range skirmishes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Rifle</td>
                            <td>2 / 4 / 3 / 1</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,800</td>
                            <td>Standard military battle rifle delivering disciplined burst fire and balanced accuracy across combat zones.</td>
                        </tr>
                        <tr>
                            <td class="bold">Battle Rifle</td>
                            <td>2 / 3 / 4 / 2</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>3</td>
                            <td>5,500</td>
                            <td>Heavy-caliber semi-automatic rifle engineered for hard-hitting, armor-cracking kinetic penetration.</td>
                        </tr>
                        <tr>
                            <td class="bold">DMR</td>
                            <td>1 / 3 / 5 / 3</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>7,000</td>
                            <td>Designated marksman rifle equipped with high-magnification optics for mid-to-long range fire.</td>
                        </tr>
                        <tr>
                            <td class="bold">Sniper Rifle</td>
                            <td>0 / 2 / 5 / 4</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+5</td>
                            <td>4</td>
                            <td>9,500</td>
                            <td>Long-range bolt-action rifle delivering extreme terminal ballistics at standoff engagement distances.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Heavy Support Weapons</h4>
            <p>
                Crew-served and reinforced heavy weapons requiring substantial physical leverage to operate, delivering unmatched suppressive fire and anti-armor kinetic energy.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Heavy Support Weapons Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Weapon Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.2mm 1.2mm;">RoF</th>
                            <th style="padding: 1.2mm 1.2mm;">H</th>
                            <th style="padding: 1.2mm 1.2mm;">Dmg</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Squad Auto (SAW)</td>
                            <td>3 / 4 / 3 / 1</td>
                            <td>3</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>4</td>
                            <td>8,500</td>
                            <td>Belt-fed light machine gun designed to pin down enemy squads with continuous, sustained automatic fire.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Machine Gun</td>
                            <td>3 / 5 / 4 / 2</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>5</td>
                            <td>12,000</td>
                            <td>Massive large-caliber machine gun capable of shredding light vehicle plating and reinforced barricades.</td>
                        </tr>
                        <tr>
                            <td class="bold">Rotary Autocannon</td>
                            <td>5 / 4 / 2 / 1</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>5</td>
                            <td>16,000</td>
                            <td>Multi-barrel motorized cannon delivering devastating saturation fire at extreme cyclic rates.</td>
                        </tr>
                        <tr>
                            <td class="bold">Anti-Materiel (AMR)</td>
                            <td>0 / 2 / 5 / 5</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+7</td>
                            <td>5</td>
                            <td>15,000</td>
                            <td>High-caliber magnetic-assisted anti-tank rifle designed to disable light vehicles and penetrate bulkheads.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.30; color: var(--text-muted); margin-top: 1mm;">
                <em>Suppression Doctrine:</em> Heavy weapons firing at RoF 3 or 4 saturate wide arcs of space. While their ammunition consumption and Load are severe, their ability to trigger multiple Chain and Crit Effects can break enemy defensive lines in a single burst.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">74</span>
        </div>
    </div>"""
    pages.append(p74)

    p75 = """    <!-- =========================================================================
         PAGE 75 (Spread 4 Right) — DUAL WIELDING, UPGRADES & RANGED WALKTHROUGH
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-customization-action">
        <div class="page-running-header">
            <span>Chapter 04: Firearms Customization</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Dual Wielding Firearms</h3>
            <p>
                A combatant can choose to wield a one-handed firearm in each hand, laying down intense suppressive fire or engaging multiple targets simultaneously:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield firearms with the <strong>1H</strong> designation (holding one sidearm in each hand).</li>
                <li><strong>Combined Firepower (Damage &amp; RoF):</strong> When making a ranged attack while dual wielding two 1H firearms, you combine the offensive output of both weapons, adding together both the flat <strong>Damage Bonus</strong> and the <strong>Rate of Fire (RoF)</strong> of the two firearms.</li>
                <li><strong>Worse Accuracy:</strong> Discharging two weapons simultaneously compromises sight alignment and recoil control. When resolving the attack test, you must use the <strong>worse (lower) Accuracy rating</strong> at the target's current range band between the two wielded firearms.</li>
            </ul>

            <h3>Firearm Upgrade Kits</h3>
            <p>
                Stock firearms can be customized into mastercrafted instruments through high-tolerance machining, carbon-fiber skeletonization, match-grade barrels, tuned gas pistons, and custom optics. Because each subsequent modification requires increasingly complex gunsmithing, upgrade kits escalate in cost with every installation:
            </p>
            <ul>
                <li><strong>Upgrade Limit:</strong> A single firearm can benefit from a maximum of <strong>3 Upgrade Kits</strong> in total, while one-handed (1H) sidearms are limited to a maximum of <strong>2 Upgrade Kits</strong>.</li>
                <li><strong>Tiered Cost Structure:</strong> 1st Upgrade: <strong>10,000 Credits</strong> &middot; 2nd Upgrade: <strong>25,000 Credits</strong> &middot; 3rd Upgrade: <strong>50,000 Credits</strong>.</li>
                <li><strong>Upgrade Choices:</strong> Each time an Upgrade Kit is applied, choose one permanent modification:
                    <ul>
                        <li><strong>Lightweight Chassis:</strong> Precision skeletonization reduces weapon <strong>Load by 1</strong> (minimum 1/2 Load).</li>
                        <li><strong>Lethal Tuning:</strong> Match-grade barrel rifling increases flat <strong>Damage Bonus by +1</strong>.</li>
                        <li><strong>Recoil Dampening:</strong> Hydraulic buffer tubes increase <strong>Rate of Fire (RoF) by 1</strong>.</li>
                        <li><strong>Optic Calibration:</strong> Holographic or thermal optics increase <strong>Accuracy by +1</strong> at one designated range band (e.g., Medium Range Accuracy +1).</li>
                    </ul>
                </li>
            </ul>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: The Hangar Deck Firefight</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax advances down an industrial catwalk overlooking a contested cargo hangar. Positioned <strong>8 spaces (~26 meters)</strong> away behind low freight containers, an armed mercenary returns fire. The distance places the mercenary squarely at <strong>Medium Range</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax is armed with an <strong>Assault Rifle</strong> (Accuracy <code>2 / 4 / 3 / 1</code>, RoF 2, 2H, Load 3, flat <strong>+2 Damage Bonus</strong>). Jax's character sheet shows <strong>Finesse 5</strong>, <strong>Instinct 3</strong>, and <strong>Strength 4</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. Determining the Test Pool:</strong> Jax declares an <strong>Accuracy + Finesse</strong> Complex Test. At Medium Range, the Assault Rifle has Accuracy 4. Pairing Jax's Finesse 5 with Accuracy 4, the higher attribute is Finesse 5 and the lower is Accuracy 4.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>2. Action Roll (Finesse 5):</strong> Jax rolls 5d10: <code>[2, 5, 8, 8, 9]</code>—scoring three Hits (8, 8, 9). The Action Roll succeeds. Jax spends one extra Hit (8) to activate an <strong>Upgrade Effect</strong>, stepping up one die in his upcoming Success Roll from a d10 to a <strong>d12</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>3. Success Roll (Accuracy 4):</strong> With the Upgrade applied, Jax rolls 3d10 and 1d12: rolling <code>[4, 7, 8]</code> on the d10s and a <strong>10</strong> on the upgraded d12.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>4. Activating Effects &amp; RoF Limits:</strong> The Success Roll produced two Hits (8 and 10). Jax spends both Hits on <strong>Crit Effects</strong> (+2 Success Points per Crit). Because the Assault Rifle has <strong>RoF 2</strong>, it perfectly accommodates spending 2 Hits on Crits.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    <strong>5. Calculating Total Damage:</strong> Highest non-spent die: <strong>7 SP</strong> + Two Crit Effects (+2 each): <strong>+4 SP</strong> + Rifle Flat Damage Bonus: <strong>+2</strong> = <strong>13 points of damage</strong>, punching cleanly through the container seam!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">75</span>
        </div>
    </div>"""
    pages.append(p75)

    # =========================================================================
    # SPREAD 5 (Pages 76-77): MELEE STATS, 15-WEAPON CATALOG, SHIELDS & STRIKE
    # =========================================================================

    p76 = """    <!-- =========================================================================
         PAGE 76 (Spread 5 Left) — MELEE WEAPONS & THE COMPLETE CATALOG
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-fundamentals-catalog">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Weapons</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the tight corridors of starships, depressurized maintenance shafts, and claustrophobic orbital stations, discharging a firearm risks puncturing critical hull plating or ricocheting in zero-gravity. In these confined environments, a dependable melee weapon is an indispensable tool for survival. Whether utilizing precision combat knives, weighted riot clubs, or heavy two-handed mauls, close-quarters combat demands physical prowess, tactical positioning, and mastery over your weapon's mechanical profile.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <p>
                Every melee weapon is defined by mechanical attributes that dictate its performance and tactical synergies:
            </p>
            <ul>
                <li><strong>Damage Type &amp; Favored Attribute Pair:</strong> Melee weapons inflict damage through one of three distinct physical methods, each paired with a favored Attribute Pair that maximizes leverage:
                    <ul>
                        <li><strong>Piercing (Agility + Finesse):</strong> Swift, pinpoint thrusts directed at structural seams, visor slits, and armor joints.</li>
                        <li><strong>Slashing (Agility + Strength):</strong> Wide, sweeping kinetic cuts that combine dynamic movement with heavy cutting force.</li>
                        <li><strong>Striking (Strength + Finesse):</strong> Controlled, bone-shattering impacts delivered with precise leverage and disciplined body mechanics.</li>
                    </ul>
                </li>
                <li><strong>Favored Pair Damage Bonus:</strong> When you make an attack test using the weapon's favored Attribute Pair, you gain a damage bonus equal to the <strong>lower attribute</strong> in that pair. While a character is free to attack using any two physical attributes, choosing the favored pair unlocks this substantial damage boost.</li>
                <li><strong>Minimum Strength (Min STR):</strong> Weapons require physical leverage to control effectively:
                    <ul>
                        <li><strong>One-Handed (1H):</strong> If Strength is lower than Min STR, you cannot wield the weapon in one hand; you must wield it with <strong>two hands</strong> to attack with it.</li>
                        <li><strong>Two-Handed (2H):</strong> If Strength is lower than Min STR, the weapon is too cumbersome to wield, and you <strong>cannot attack</strong> with it under any circumstances.</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to success points on a hit. Heavier weapons with higher Min STR feature significantly larger flat Damage Bonuses.</li>
                <li><strong>Hands, Load &amp; Cost:</strong> Standard inventory mass and market credits.</li>
            </ul>

            <h3 style="margin-top: 1mm;">Melee Weapons Catalog</h3>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Melee Weapons Catalog</div>
                <table class="rules-table" style="font-size: 7.3pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 1.0mm;">Weapon Name</th>
                            <th style="padding: 1.0mm 1.0mm;">Type</th>
                            <th style="padding: 1.0mm 1.0mm;">STR</th>
                            <th style="padding: 1.0mm 1.0mm;">H</th>
                            <th style="padding: 1.0mm 1.0mm;">Dmg</th>
                            <th style="padding: 1.0mm 1.0mm;">Load</th>
                            <th style="padding: 1.0mm 1.0mm;">Cost</th>
                            <th style="padding: 1.0mm 1.0mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Shiv / Stiletto</td>
                            <td>Piercing</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>150</td>
                            <td>Compact concealable thrusting blade for unarmored seams.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Knife</td>
                            <td>Slashing</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>200</td>
                            <td>Standard utility and combat knife with single-edged blade.</td>
                        </tr>
                        <tr>
                            <td class="bold">Knuckleduster</td>
                            <td>Striking</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>100</td>
                            <td>Fitted fist reinforcement concentrating punching force.</td>
                        </tr>
                        <tr>
                            <td class="bold">Dagger</td>
                            <td>Piercing</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>400</td>
                            <td>Double-edged tactical dagger for penetrating thrusts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hatchet / Machete</td>
                            <td>Slashing</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>500</td>
                            <td>Forward-weighted chopping blade for utility and combat.</td>
                        </tr>
                        <tr>
                            <td class="bold">Baton / Club</td>
                            <td>Striking</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>300</td>
                            <td>Weighted polymer or steel rod delivering blunt trauma.</td>
                        </tr>
                        <tr>
                            <td class="bold">Shortsword</td>
                            <td>Piercing</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,200</td>
                            <td>Straight rigid blade optimized for high-mobility lunges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Boarding Axe</td>
                            <td>Slashing</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,500</td>
                            <td>Sturdy single-handed axe for breaching doors and armor.</td>
                        </tr>
                        <tr>
                            <td class="bold">Mace / Crowbar</td>
                            <td>Striking</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Flanged bludgeon or prybar cracking bone through plating.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spear</td>
                            <td>Piercing</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,200</td>
                            <td>Two-handed hafted spear delivering deep thrusts with reach.</td>
                        </tr>
                        <tr>
                            <td class="bold">Longsword</td>
                            <td>Slashing</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,800</td>
                            <td>Versatile tempered blade generating fluid cutting arcs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Warhammer</td>
                            <td>Striking</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,400</td>
                            <td>Reinforced hammerhead built to crumple armor plating.</td>
                        </tr>
                        <tr>
                            <td class="bold">Halberd / Poleaxe</td>
                            <td>Piercing</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,500</td>
                            <td>Long polearm capped with piercing spike and axe head.</td>
                        </tr>
                        <tr>
                            <td class="bold">Greatsword</td>
                            <td>Slashing</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>5,000</td>
                            <td>Massive two-handed blade leveraging full body rotation.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Maul</td>
                            <td>Striking</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,800</td>
                            <td>Enormous sledgehammer delivering armor-pulverizing force.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">76</span>
        </div>
    </div>"""
    pages.append(p76)

    p77 = """    <!-- =========================================================================
         PAGE 77 (Spread 5 Right) — DUAL WIELDING, UPGRADES, SHIELDS & MELEE ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-customization-action">
        <div class="page-running-header">
            <span>Chapter 04: Melee &amp; Shields</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Dual Wielding Melee Weapons</h3>
            <p>
                A combatant can choose to hold and fight with a weapon in each hand, creating an aggressive combat style that overwhelms opponents with combined offensive pressure:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield weapons with the <strong>1H</strong> designation. You must meet the Minimum Strength requirement of each weapon individually to wield them simultaneously in separate hands.</li>
                <li><strong>Combined Damage Bonus:</strong> When you make a melee attack while dual wielding two 1H weapons, you gain the flat <strong>Damage Bonus of both weapons</strong> added to your total outcome.</li>
                <li><strong>Attack Resolution:</strong> When attacking, you designate which of your two weapons is leading the strike to determine the attack's <strong>Damage Type</strong> (Piercing, Slashing, or Striking) and its corresponding favored Attribute Pair. If your declared action utilizes that favored pair, you also add the lower attribute of the test to the combined damage.</li>
            </ul>

            <h3>Melee Upgrade Kits</h3>
            <p>
                Standard melee weapons can be customized into mastercrafted instruments through aerospace machining, monomolecular edge-honing, ergonomic carbon-fiber balancing, or high-frequency vibration emitters. Because each modification requires precision engineering, upgrade kits escalate in cost:
            </p>
            <ul>
                <li><strong>Upgrade Limit:</strong> Two-handed (2H) melee weapons can benefit from a maximum of <strong>3 Upgrade Kits</strong>, while one-handed (1H) weapons are limited to a maximum of <strong>2 Upgrade Kits</strong>.</li>
                <li><strong>Tiered Cost Structure:</strong> 1st Upgrade: <strong>10,000 Credits</strong> &middot; 2nd Upgrade: <strong>25,000 Credits</strong> &middot; 3rd Upgrade: <strong>50,000 Credits</strong>.</li>
                <li><strong>Upgrade Choices:</strong> Each time an Upgrade Kit is applied, choose one permanent modification:
                    <ul>
                        <li><strong>Lightweight Tuning:</strong> Skeletal milling reduces weapon <strong>Load by 1</strong> (minimum 1/2 Load).</li>
                        <li><strong>Lethal Edge / Weighted Core:</strong> High-frequency vibration motors or carbide weights increase flat <strong>Damage Bonus by +1</strong>.</li>
                    </ul>
                </li>
            </ul>

            <h3>Shields</h3>
            <p>
                Shields are rigid defensive barriers constructed from ballistic polymers, layered ceramics, or titanium alloys. Wielded in the off-hand, they provide vital protection during tactical breaches and close-quarters engagements:
            </p>
            <ul>
                <li><strong>One Free Hand Required:</strong> Wielding a shield requires <strong>one hand (1H)</strong>. You cannot wield a two-handed weapon or perform two-handed tasks while actively holding a shield.</li>
                <li><strong>Physical Protection Bonus:</strong> While held, a shield grants a flat bonus to your <strong>Physical Protection</strong> (+1 to +3). This bonus stacks directly with worn armor, reducing incoming damage before it affects health.</li>
                <li><strong>No Dual Wielding Shields:</strong> A character cannot wield two shields simultaneously, nor benefit from more than one shield bonus at a time.</li>
                <li><strong>Minimum Strength:</strong> If Strength is lower than a shield's Min STR, you cannot wield the shield.</li>
            </ul>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Tactical Shields Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Shield Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Protection</th>
                            <th style="padding: 1.2mm 1.2mm;">STR</th>
                            <th style="padding: 1.2mm 1.2mm;">H</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Buckler</td>
                            <td>+1 Prot</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>1</td>
                            <td>800</td>
                            <td>Compact arm-mounted composite disc parrying blades and shrapnel.</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Shield</td>
                            <td>+2 Prot</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>2</td>
                            <td>2,500</td>
                            <td>Reinforced polycarbonate barrier providing solid torso and limb coverage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Ballistic Shield</td>
                            <td>+3 Prot</td>
                            <td>6</td>
                            <td>1H</td>
                            <td>4</td>
                            <td>6,500</td>
                            <td>Heavy ceramic-composite assault pavise built to withstand rifle fire.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: The Boarding Action Strike</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax enters a contested airlock space occupied by a hostile pirate enforcer. Armed with a <strong>Boarding Axe</strong> (Slashing, Min STR 3, 1H, Load 2, flat <strong>+2 Damage Bonus</strong>), Jax initiates a melee strike. Jax has <strong>Strength 5</strong>, <strong>Agility 4</strong>, and <strong>Finesse 3</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Because the Boarding Axe is Slashing, its favored pair is <strong>Agility + Strength</strong>. Jax's Strength 5 easily satisfies Min STR 3, allowing single-handed wielding.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. Action Roll (Strength 5):</strong> Jax rolls 5d10: <code>[3, 5, 7, 8, 9]</code>. Both 8 and 9 are Hits. The Action Roll succeeds. Jax spends one Hit (8) to activate an <strong>Upgrade Effect</strong>, stepping up one die in his Success Roll from a d10 to a <strong>d12</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>2. Success Roll (Agility 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 6, 7]</code> on the d10s and a <strong>9</strong> on the upgraded d12. The highest single die is <strong>9 SP</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    <strong>3. Calculating Damage:</strong> Base Success Points: <strong>9</strong> + Favored Pair Bonus (lower attribute = Agility 4): <strong>+4</strong> + Axe Damage Bonus: <strong>+2</strong> = <strong>15 points of damage</strong>, cleaving through the pirate's defenses!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">77</span>
        </div>
    </div>"""
    pages.append(p77)

    # =========================================================================
    # SPREAD 6 (Pages 78-79): ARMOR STATS, PROPERTIES, CATALOG & WALKTHROUGH
    # =========================================================================

    p78 = """    <!-- =========================================================================
         PAGE 78 (Spread 6 Left) — ARMOR MECHANICS, PROPERTIES & UPGRADES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-mechanics-upgrades">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Armor</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the perilous expanses of the settled systems, a dependable suit of armor is often the only barrier between a Corsair and lethal trauma. Whether weathering rifle fire in a depressurized corridor, deflecting shrapnel from an explosive hull breach, or absorbing punishing melee impacts during a boarding skirmish, protective gear preserves an operative's capability in the deadliest environments.
            </p>

            <h3>Armor Statistics Explained</h3>
            <p>
                Every suit of armor is defined by mechanical attributes governing its resilience and encumbrance:
            </p>
            <ul>
                <li><strong>Protection:</strong> Flat integer value of physical and kinetic damage reduced from each incoming attack before it affects health. When struck, subtract armor Protection directly from incoming damage:
                    <ul>
                        <li><strong>Stacking Rules:</strong> Armor Protection stacks directly with defensive bonuses provided by <strong>Shields</strong> (e.g., Riot Shield +2 Prot) and <strong>Cover</strong> (e.g., Medium Cover +2 Prot). However, an operative can only wear <strong>one suit of armor</strong> at a time; separate suits do not stack.</li>
                    </ul>
                </li>
                <li><strong>Load &amp; No Minimum Strength:</strong> Armor counts against maximum Load limit (<code>12 + Strength &times; 2</code>). Unlike weapons, armor does not enforce a binary Minimum Strength requirement; any operative can wear any armor if they have sufficient Load capacity. However, heavier suits carry the <strong>Cumbersome (X)</strong> property.</li>
                <li><strong>Armor Properties:</strong> Specialized engineering features providing tactical benefits or physical trade-offs:
                    <ul>
                        <li><strong>Cumbersome (X):</strong> Mass and rigid plates restrict sudden articulation. While wearing this armor, you suffer <strong>X Downgrades on all tests involving Agility</strong> (including movement tests, acrobatics, athletics, stealth, and agility attack/contest rolls).</li>
                        <li><strong>Hardened:</strong> Layered boron-carbide strike faces diffuse concentrated penetrators. When an attacker scores a <strong>Crit Effect</strong> against you, bonus SP gained per Hit spent is reduced by 1 (granting <strong>+1 SP per Hit</strong> instead of +2).</li>
                        <li><strong>Blast-Dampened:</strong> Concussive baffles dissipate explosive shockwaves. You gain <strong>+2 additional Protection against Area Attacks and Explosives</strong>.</li>
                        <li><strong>Tactical Harness (X):</strong> Features reinforced webbing providing <strong>X dedicated Load slots for any equipment</strong>. Stowed items do not count against standard Load capacity, up to X Load.</li>
                        <li><strong>Muffled:</strong> Acoustic-dampening micro-weaves suppress gear rattle, granting <strong>+1 Upgrade on Stealth tests</strong>.</li>
                    </ul>
                </li>
                <li><strong>Cost:</strong> Standard galactic market price in Credits.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p>
                Protective gear is manufactured by major aerospace conglomerates:
            </p>
            <ul>
                <li><strong>Chidori-Qwei Combatwear:</strong> Sleek flexible polymers and smart-fiber flightsuits tailored for urban covert security.</li>
                <li><strong>Panthera Arms:</strong> Precision composite armor and modular plate carriers favored by corporate security strike teams.</li>
                <li><strong>Vandal's Workshop:</strong> Stamped-sheet alloy armor and rugged industrial hazard suits built for frontline abuse.</li>
                <li><strong>Caldera Foundry:</strong> Heavy cast ceramic-titanium battleplate and carapace suits engineered for zero-compromise kinetic resistance.</li>
                <li><strong>Ker'Satz Korp:</strong> Industrial siege rigs built to withstand catastrophic structural punishment.</li>
            </ul>

            <h3>Armor Upgrade Kits</h3>
            <p>
                Stock armor can be customized through armorer machining, composite substitution, liquid-gel trauma dampeners, or high-density ceramic strike faces:
            </p>
            <ul>
                <li><strong>Upgrade Limit:</strong> A suit of armor can benefit from a maximum of <strong>3 Upgrade Kits</strong> in total.</li>
                <li><strong>Tiered Cost Structure:</strong> 1st Upgrade: <strong>50,000 Credits</strong> &middot; 2nd Upgrade: <strong>100,000 Credits</strong> &middot; 3rd Upgrade: <strong>180,000 Credits</strong>.</li>
                <li><strong>Upgrade Choices:</strong> Each kit provides one permanent modification:
                    <ul>
                        <li><strong>Reinforced Plating:</strong> Micro-layered titanium inserts increase <strong>Protection by +1</strong> (maximum +3 Protection across all kits).</li>
                        <li><strong>Lightweight Composites:</strong> Aerogels reduce <strong>Load by 1</strong> (minimum 1 Load).</li>
                        <li><strong>Specialized Modification:</strong> Installs one property: <strong>Hardened</strong>, <strong>Blast-Dampened</strong>, <strong>Tactical Harness (1)</strong>, or <strong>Muffled</strong>.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">78</span>
        </div>
    </div>"""
    pages.append(p78)

    p79 = """    <!-- =========================================================================
         PAGE 79 (Spread 6 Right) — COMPLETE ARMOR CATALOG & PROTECTION WALKTHROUGH
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-catalog-full">
        <div class="page-running-header">
            <span>Chapter 04: Armor Catalog</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Armor Catalog</h3>
            <h4>Light Armor (No Agility Penalties &middot; Load 1–3 &middot; Prot 2–4)</h4>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Light Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Armor Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Prot</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Padded Flightsuit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>&mdash;</td>
                            <td>1,200</td>
                            <td>Standard pressurized spacer flight jumpsuit; unencumbering.</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltration Suit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>Muffled</td>
                            <td>3,500</td>
                            <td>Sleek acoustic-dampening bodysuit favored by covert agents.</td>
                        </tr>
                        <tr>
                            <td class="bold">Armored Jacket</td>
                            <td>3</td>
                            <td>2</td>
                            <td>&mdash;</td>
                            <td>3,000</td>
                            <td>Rugged everyday utility jacket lined with ballistic aramid inserts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hardened Vest</td>
                            <td>3</td>
                            <td>2</td>
                            <td>Hardened</td>
                            <td>5,500</td>
                            <td>Reinforced security vest fitted with ceramic strike faces.</td>
                        </tr>
                        <tr>
                            <td class="bold">Light Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>&mdash;</td>
                            <td>10,000</td>
                            <td>Mil-spec tactical plate carrier balancing defense with mobility.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spec-Ops Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>Hardened</td>
                            <td>18,000</td>
                            <td>Elite plate carrier featuring boron-carbide inserts for peak defense.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Medium Armor (Frontline Assault &middot; Load 4–5 &middot; Prot 5–6)</h4>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Medium Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Armor Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Prot</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>&mdash;</td>
                            <td>30,000</td>
                            <td>Full-torso ceramic-carbide plate carrier; maximum unencumbered defense.</td>
                        </tr>
                        <tr>
                            <td class="bold">Flak Combat Rig</td>
                            <td>5</td>
                            <td>4</td>
                            <td>Blast-Dampened</td>
                            <td>38,000</td>
                            <td>Shrapnel-lined assault vest designed for surviving grenade blasts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Vanguard Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>Hardened, Tac Harness (1)</td>
                            <td>45,000</td>
                            <td>Squad-leader vest with trauma plates and quick-access utility webbing.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Carapace Armor</td>
                            <td>6</td>
                            <td>5</td>
                            <td>Cumbersome (1)</td>
                            <td>65,000</td>
                            <td>Full-body interlocking alloy carapace; exceptional stopping power.</td>
                        </tr>
                        <tr>
                            <td class="bold">Bastion Carapace</td>
                            <td>6</td>
                            <td>5</td>
                            <td>Cumbersome (1), Hardened, Tac (1)</td>
                            <td>85,000</td>
                            <td>Fortified trench carapace engineered to weather sniper and auto fire.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Heavy Armor (Walking Fortresses &middot; Load 6–7 &middot; Prot 7–8)</h4>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Heavy Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Armor Name</th>
                            <th style="padding: 1.2mm 1.2mm;">Prot</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Breacher Carapace</td>
                            <td>7</td>
                            <td>6</td>
                            <td>Cumbersome (1), Blast, Tac (1)</td>
                            <td>140,000</td>
                            <td>Heavy blast apron and limb plating built for point-men kicking airlocks.</td>
                        </tr>
                        <tr>
                            <td class="bold">Juggernaut Armor</td>
                            <td>7</td>
                            <td>6</td>
                            <td>Cumbersome (1), Hardened</td>
                            <td>160,000</td>
                            <td>Shock-absorbing fortress armor that shrugs off critical hits and slugs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Titan Rig</td>
                            <td>8</td>
                            <td>7</td>
                            <td>Cumbersome (2), Hard, Blast, Tac (2)</td>
                            <td>280,000</td>
                            <td>Massive unpowered siege carapace; absolute pinnacle of personal protection.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: Weathering the Boarding Barrage</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    During a violent breach of a station cargo bay, Jax is caught in the open when a pirate gunner opens fire with a <strong>Battle Rifle</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax is equipped with <strong>Tactical Battleplate</strong> (Protection 5, Load 4) and carries a <strong>Riot Shield</strong> (+2 Protection, Min STR 4, 1H, Load 2). Because Tactical Battleplate carries no Cumbersome penalty, his Agility rolls remain unhindered.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. Incoming Attack:</strong> The pirate scores a Hit, spending 1 Hit on a Crit Effect (+2 damage) alongside the Battle Rifle's flat +4 Damage Bonus, generating <strong>14 points of physical damage</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>2. Total Protection:</strong> Tactical Battleplate Base (5) + Riot Shield (+2) = <strong>7 Combined Protection</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    <strong>3. Damage Reduction:</strong> 14 Incoming Damage &minus; 7 Protection = <strong>7 net damage</strong>, absorbed cleanly within Track I of Jax's Physical Condition.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">79</span>
        </div>
    </div>"""
    pages.append(p79)

    # =========================================================================
    # SPREAD 7 (Pages 80-81): GEAR RULES, MOBILITY, FORTIFICATION & EXPLOSIVES
    # =========================================================================

    p80 = """    <!-- =========================================================================
         PAGE 80 (Spread 7 Left) — TACTICAL GEAR RULES & MOBILITY HARDWARE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-rules-mobility">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Gear</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                Gear encompasses the broad spectrum of mission-critical tactical equipment, specialized toolkits, refillable field rigs, and survival hardware utilized by operators in the Corsair universe. While weapons and armor govern basic combat survival, gear provides the technical leverage, mobility, intelligence, and utility needed to complete dangerous boarding operations and wilderness expeditions.
            </p>

            <h3>Gear Rules &amp; Resolution</h3>
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 2mm;">
                <li><strong>Dedicated Attributes &amp; Test Pairs:</strong> Gear categories provide dedicated item attributes (such as <em>Mobility</em>, <em>Medicine</em>, <em>Sensors</em>, <em>Tinkering</em>, <em>Locksmith</em>, <em>Disguise</em>, <em>Forgery</em>, <em>Interfacing</em>, <em>Hacking</em>, or <em>Ordnance</em>). When activated, the item's attribute pairs with a core attribute to form the dice pool.</li>
                <li><strong>Action Point Costs:</strong> Deploying, activating, or utilizing any piece of gear requires <strong>1 Action Point (AP)</strong>, unless explicitly noted otherwise. Passive items that require no roll (such as deploying Cover) still cost 1 AP.</li>
                <li><strong>Capacity &amp; Automatic Refill:</strong> Items with expendable charges have an innate <strong>Capacity (Cap X)</strong>. Activating the item expends 1 charge. All expended charges <strong>automatically refill to maximum</strong> whenever visiting an eligible supply hub (starship, clinic, armory, colony depot) during place-to-place or day-to-day pacing, without spending Credits or tracking individual stock.</li>
                <li><strong>Stand-Alone Explosive Rolls:</strong> Explosives do not pair with a character attribute; grenades and charges resolve as Area Attack Success Tests rolling pure <strong>Ordnance</strong> pools.</li>
                <li><strong>Upgrade Compatibility:</strong> Gear and electronic devices can be enhanced with up to 3 standard Upgrade Kits to reduce Load by 1 or increase their primary attribute by +1.</li>
            </ol>

            <h3>1. Mobility Gear</h3>
            <p>
                Mobility hardware overcomes zero-gravity, vertical terrain, and planetary gravity wells. All mobility equipment shares the unified <strong>Mobility</strong> item attribute.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Mobility Gear Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Light Jump-Pack</td>
                            <td>Jetpack (8m), Mobility 3</td>
                            <td>3</td>
                            <td>35,000</td>
                            <td>Compact personal thruster pack for short tactical bounds.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Jetpack</td>
                            <td>Jetpack (12m), Mobility 4</td>
                            <td>4</td>
                            <td>72,000</td>
                            <td>Standard mil-spec jump rig with balanced fuel capacity.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Jump-Rig</td>
                            <td>Jetpack (16m), Mobility 5</td>
                            <td>5</td>
                            <td>120,000</td>
                            <td>High-output vector thruster chassis for high-altitude assaults.</td>
                        </tr>
                        <tr>
                            <td class="bold">Gecko Climbing Kit</td>
                            <td>Mobility 3, Surface Adhesion</td>
                            <td>1</td>
                            <td>15,000</td>
                            <td>Magnetic gloves and boots for scaling metallic ship hulls.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Zipline (40m)</td>
                            <td>Zipline (40m), 24 HP</td>
                            <td>3</td>
                            <td>15,000</td>
                            <td>Pneumatic launcher deploying high-tensile motorized cables.</td>
                        </tr>
                        <tr>
                            <td class="bold">Standard Grapple</td>
                            <td>Grapple (8m), Mobility 3, Cap 3</td>
                            <td>2</td>
                            <td>5,000</td>
                            <td>Gas-tether launcher for rapid ascent and target displacement.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Grapple</td>
                            <td>Grapple (16m), Mobility 4, Cap 4</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>Reinforced magnetic winch rig with extended range and pull.</td>
                        </tr>
                        <tr>
                            <td class="bold">High-Tensile Rope (40m)</td>
                            <td>Utility Cordage</td>
                            <td>1</td>
                            <td>100</td>
                            <td>Synthetic braided line rated for extreme loads and rappelling.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Mobility Special Properties</h4>
            <ul>
                <li><strong>Jetpack (Xm):</strong> Activating costs <strong>1 AP</strong>; Success Test using <strong>Mobility + Agility</strong>. Movement equals base speed (Xm) plus 1m per SP. Fly in 3D, hover, ignore difficult terrain. Ignore falling damage while wearing active jetpack.
                    <ul>
                        <li><strong>Vector Boost (Crit Effect):</strong> Spending a Hit grants <strong>+4m movement</strong> per Hit instead of +2 SP.</li>
                        <li><strong>Charging:</strong> Spend <strong>1 AP</strong> to fly base speed in a straight line and execute a Melee Attack at the end.</li>
                    </ul>
                </li>
                <li><strong>Surface Adhesion:</strong> Scaling sheer surfaces costs <strong>1 AP</strong>; Success Test using <strong>Mobility + Strength</strong>. Base climb speed 8m plus 1m per SP.</li>
                <li><strong>Zipline (40m):</strong> Launching cable costs <strong>1 AP</strong>. Any creature can traverse cable as part of standard Move Action. Reeling in costs 1 AP.</li>
                <li><strong>Grapple (Xm) &amp; Target Displacement:</strong> Firing costs <strong>1 AP</strong> and 1 charge. Inanimate targets succeed automatically, pulling user directly to anchor. Hostile creatures resolve as Complex Test using <strong>Mobility + Strength</strong>:
                    <ul>
                        <li><strong>Tether Pull (Push Effect):</strong> Each Hit spent pulls target 1 space (2m) towards user. User can advance along line up to target's space. Optional Tearing Damage deals SP as damage.</li>
                    </ul>
                </li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">80</span>
        </div>
    </div>"""
    pages.append(p80)

    p81 = """    <!-- =========================================================================
         PAGE 81 (Spread 7 Right) — FORTIFICATION GEAR & EXPLOSIVES RIGS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortification-explosives">
        <div class="page-running-header">
            <span>Chapter 04: Fortifications &amp; Explosives</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">2. Fortification Gear</h3>
            <p>
                Deployable fortifications provide instant cover, automated defense, and remote weapon platforms.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Fortification Gear Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Deployable Cover (Light)</td>
                            <td>Light Cover (+1), 12 HP, Innate Prot 4</td>
                            <td>2</td>
                            <td>5,000</td>
                            <td>Rapid ballistic fabric barrier for quick ambushes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Medium)</td>
                            <td>Medium Cover (+2), 24 HP, Innate Prot 8</td>
                            <td>3</td>
                            <td>8,000</td>
                            <td>Telescoping ceramic-composite barricade with spikes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Heavy)</td>
                            <td>Heavy Cover (+3), 36 HP, Innate Prot 12</td>
                            <td>4</td>
                            <td>12,000</td>
                            <td>Alloy blast shield designed to withstand sustained assault.</td>
                        </tr>
                        <tr>
                            <td class="bold">APS Beacon</td>
                            <td>Intercept 5, Area-Defense Reaction, 24 HP</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Automated Active Protection System firing counter-munitions.</td>
                        </tr>
                        <tr>
                            <td class="bold">Smartpod Remote Mount</td>
                            <td>Automount 3, 12 HP</td>
                            <td>3</td>
                            <td>36,000</td>
                            <td>Motorized gyro-stabilized turret for mounted ranged weapons.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Fortification Special Properties</h4>
            <ul>
                <li><strong>Deployable Cover:</strong> Deploying or packing up costs <strong>1 AP</strong>. Occupies one space, granting Cover Protection (+1 to +3) with listed Cover HP and Innate Protection. Recover for 1 AP.</li>
                <li><strong>Intercept (X) &amp; Area-Defense Reaction:</strong> Once deployed (1 AP), monitors its space and all adjacent spaces. Gains <strong>1 Free Reaction AP per round</strong> to contest incoming Area Attacks and Ordnance explosions. Resolves contest rolling pure <strong>Intercept (X)</strong>. If no dice 8+ remain, incoming explosive munition is destroyed mid-flight and completely negated.</li>
                <li><strong>Automount (X):</strong> Deploying with mounted ranged weapon costs <strong>1 AP</strong>. Operator or linked ally spends <strong>1 AP</strong> to fire remotely, rolling <strong>Automount (X) + Finesse</strong> (or pure Automount if automated).</li>
            </ul>

            <h3>3. Explosives &amp; Launchers</h3>
            <p>
                Explosives deliver high-yield area destruction. Rather than tracking loose throwables, combatants carry refillable <strong>Grenade Rigs</strong> allowing on-the-fly point-of-use selection.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Explosives &amp; Launchers Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Grenade Rig</td>
                            <td>Capacity 3, Refillable, Choice</td>
                            <td>2</td>
                            <td>4,000</td>
                            <td>Bandolier holding 3 charges; choose Frag, Flash, Smoke, HE.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Grenade Rig</td>
                            <td>Capacity 5, Refillable, Choice</td>
                            <td>3</td>
                            <td>10,000</td>
                            <td>Heavy combat rig holding 5 refillable charges with instant choice.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Demolitions Rig</td>
                            <td>Capacity 2, Refillable, Choice</td>
                            <td>3</td>
                            <td>8,000</td>
                            <td>Breaching rig holding 2 heavy demolition or high-explosive charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Siege Demolitions Rig</td>
                            <td>Capacity 4, Refillable, Choice</td>
                            <td>4</td>
                            <td>16,000</td>
                            <td>Military harness carrying 4 breaching charges and structural cutters.</td>
                        </tr>
                        <tr>
                            <td class="bold">Grenade Launcher Rig</td>
                            <td>Delivery (Medium Range)</td>
                            <td>2</td>
                            <td>6,000</td>
                            <td>Shoulder-fired tubular launcher firing Ordnance to Medium Range.</td>
                        </tr>
                        <tr>
                            <td class="bold">Rocket Launcher Rig</td>
                            <td>Delivery (Long Range)</td>
                            <td>4</td>
                            <td>22,000</td>
                            <td>Tube-launched unguided rocket system firing to Long Range.</td>
                        </tr>
                        <tr>
                            <td class="bold">Missile Guidance System</td>
                            <td>Delivery (Extreme Range)</td>
                            <td>6</td>
                            <td>60,000</td>
                            <td>Heavy laser-guided missile tube firing Ordnance to Extreme Range.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Munition Profiles &amp; Explosives Properties</h4>
            <ul>
                <li><strong>Frag Munition:</strong> Ordnance 4, Blast 3, 8m Radius. Anti-personnel fragmentation casing.</li>
                <li><strong>Flashbang Munition:</strong> Ordnance 5, Area Stun, 4m Radius. Discards highest die on next roll for hostiles.</li>
                <li><strong>Smoke Canister:</strong> Area Obscurance, 8m Radius. Dense aerosol blocking line of sight without rolling.</li>
                <li><strong>HE Munition:</strong> Ordnance 5, Blast 5, 4m Radius. High-explosive concussion charge.</li>
                <li><strong>Remote Demolition Charge:</strong> Ordnance 7, Blast 5, 12m Radius, Remote radio detonator (Heavy Rig only).</li>
                <li><strong>Ordnance (X) Area Attack:</strong> Hand-thrown grenades target Short Range (0–5 spaces). Pure Ordnance Success Test. <strong>Blast (X)</strong> adds +X damage per Hit spent on Crits.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">81</span>
        </div>
    </div>"""
    pages.append(p81)

    # =========================================================================
    # SPREAD 8 (Pages 82-83): MEDICAL, TECH KITS, SURVEILLANCE & UTILITY
    # =========================================================================

    p82 = """    <!-- =========================================================================
         PAGE 82 (Spread 8 Left) — MEDICAL RIGS, TRIAGE & COMBAT STIMULANTS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-medical-consumables">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Medical &amp; Consumables</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">4. Medical &amp; Consumables</h3>
            <p>
                Medical kits and performance stimulant injectors provide emergency field triage and biochemical enhancement. All medical gear operates on durable, refillable casings.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Medical &amp; Consumables Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Field Medi-Kit</td>
                            <td>Medicine 3, Cap 3, Lesser Phys (1/2)</td>
                            <td>1</td>
                            <td>2,500</td>
                            <td>Auto-sutures, dermal staplers, coagulant spray.</td>
                        </tr>
                        <tr>
                            <td class="bold">Trauma Rig</td>
                            <td>Medicine 4, Cap 4, Lesser Phys (1/1)</td>
                            <td>2</td>
                            <td>7,500</td>
                            <td>Rapid tissue welders and synthetic blood applicator.</td>
                        </tr>
                        <tr>
                            <td class="bold">Phoenix Reconstructor</td>
                            <td>Medicine 4, Cap 2, Greater Phys (1/1)</td>
                            <td>2</td>
                            <td>15,000</td>
                            <td>Stabilizes critical trauma and clears Aggravated damage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Stabilizer Inhaler</td>
                            <td>Medicine 3, Cap 3, Lesser Mental (1/2)</td>
                            <td>1</td>
                            <td>2,000</td>
                            <td>Pressurized mist dispenser countering stress and panic.</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Stabilizer Rig</td>
                            <td>Medicine 4, Cap 4, Lesser Mental (1/1)</td>
                            <td>2</td>
                            <td>6,000</td>
                            <td>Cranial auto-injector delivering potent cognitive restoratives.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Stim Injector</td>
                            <td>Capacity 3, Refillable, Choice</td>
                            <td>1</td>
                            <td>5,000</td>
                            <td>Transdermal auto-injector unit delivering 3 stimulant doses.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Chem-Rig</td>
                            <td>Capacity 5, Refillable, Choice</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>High-capacity injector harness carrying 5 stimulant doses.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Medical Properties &amp; Triage</h4>
            <ul>
                <li><strong>Medicine (X) Triage:</strong> Applying to self or adjacent ally costs <strong>1 AP</strong>, 1 charge; Success Test using <strong>Medicine + Knowledge</strong>.</li>
                <li><strong>Lesser Healing (1/X, Track):</strong> Restores 1 segment on designated track per X SPs. Cannot repair Aggravated damage.</li>
                <li><strong>Greater Healing (1/X, Track):</strong> Restores normal damage (1 seg / X SPs) and clears <strong>Aggravated damage</strong> at double cost (2X SPs per locked segment).</li>
            </ul>

            <h4>Combat Stimulant Formulas</h4>
            <p>
                When activating a Stim Injector or Chem-Rig (1 AP, 1 charge), choose one chemical formula:
            </p>
            <ul>
                <li><strong>Roid (Strength):</strong> <strong>+1 Strength.</strong> High-grade anabolic surge providing raw muscular leverage (Volatile 2, Fleeting).</li>
                <li><strong>Nitro (Agility):</strong> <strong>+1 Agility.</strong> Adrenaline booster accelerating muscle twitch response and sprint speed (Volatile 2, Fleeting).</li>
                <li><strong>Edgedance (Finesse):</strong> <strong>+1 Finesse.</strong> Fine-motor neural enhancer for micrometric hand-eye precision (Volatile 2, Fleeting).</li>
                <li><strong>SharpX (Instinct):</strong> <strong>+1 Instinct.</strong> Sensory cortex stimulant accelerating peripheral awareness and reactions (Volatile 2, Fleeting).</li>
                <li><strong>Cognita (Knowledge):</strong> <strong>+1 Knowledge.</strong> Nootropic neuro-accelerator boosting tactical calculation and memory (Volatile 2, Fleeting).</li>
                <li><strong>Rizz (Presence):</strong> <strong>+1 Presence.</strong> Vocal and pheromonal cocktail projecting commanding authority (Volatile 2, Fleeting).</li>
                <li><strong>Volatile (X):</strong> When administered, user immediately suffers <strong>X unmitigated damage</strong>. Consuming a stimulant while already under Volatile effects causes additional damage equal to the total number of active Volatile substances in your system.</li>
                <li><strong>Fleeting:</strong> Stimulant surge lasts until end of current combat round, or end of Player Turn in day-to-day scenes.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">82</span>
        </div>
    </div>"""
    pages.append(p82)

    p83 = """    <!-- =========================================================================
         PAGE 83 (Spread 8 Right) — INFILTRATION KITS, SURVEILLANCE & SURVIVAL
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-tech-surveillance-survival">
        <div class="page-running-header">
            <span>Chapter 04: Tech, Sensors &amp; Utility</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">5. Infiltration &amp; Tech Kits</h3>
            <p>
                Specialized toolkits and electronic rigs used to bypass physical security, falsify credentials, and penetrate secure data networks.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Infiltration &amp; Tech Kits Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Mechanic's Kit</td>
                            <td>Tinkering 2, Locksmith 2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Standard bypass picks, tension wrenches, diagnostic drivers.</td>
                        </tr>
                        <tr>
                            <td class="bold">Engineer's Kit</td>
                            <td>Tinkering 4, Locksmith 4</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>Precision ultrasonic picks and electronic bypass shunts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Maker's Kit</td>
                            <td>Tinkering 6, Locksmith 6</td>
                            <td>2</td>
                            <td>25,000</td>
                            <td>Mil-spec quantum lock decoders and micro-plasma cutters.</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltrator Kit</td>
                            <td>Disguise 2, Forgery 2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Cosmetic prosthetics, seal replicators, pass laminators.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spy Kit</td>
                            <td>Disguise 4, Forgery 4</td>
                            <td>3</td>
                            <td>12,000</td>
                            <td>Holographic identity cloners and biometric stamp mimics.</td>
                        </tr>
                        <tr>
                            <td class="bold">Chameleon Kit</td>
                            <td>Disguise 6, Forgery 6</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Neural-adaptive latex mesh and encrypted identity fakers.</td>
                        </tr>
                        <tr>
                            <td class="bold">"Spider" Cyberdeck</td>
                            <td>Interfacing 3, Hacking 2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Portable deck with standard optical transceiver.</td>
                        </tr>
                        <tr>
                            <td class="bold">"Mantis" Cyberdeck</td>
                            <td>Interfacing 5, Hacking 4</td>
                            <td>3</td>
                            <td>12,000</td>
                            <td>Tactical deck with dedicated intrusion coprocessors.</td>
                        </tr>
                        <tr>
                            <td class="bold">"Scorpion" Cyberdeck</td>
                            <td>Interfacing 7, Hacking 6</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Black-market military cyberdeck built to shred ICE.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Tech Properties (1 AP Costs)</h4>
            <ul>
                <li><strong>Tinkering (X):</strong> Disabling traps, sabotaging machinery, repairing hardware (Tinkering + Knowledge).</li>
                <li><strong>Locksmith (X):</strong> Picking locks or bypassing latches (Locksmith + Finesse).</li>
                <li><strong>Disguise (X):</strong> Creating convincing physical personas (Disguise + Knowledge).</li>
                <li><strong>Forgery (X):</strong> Counterfeiting security passes and manifests (Forgery + Finesse).</li>
                <li><strong>Interfacing (X):</strong> Establishing network links, executing system commands (Interfacing + Knowledge).</li>
                <li><strong>Hacking (X):</strong> Breaching firewalls, disabling ICE, seizing network nodes (Hacking + Knowledge).</li>
            </ul>

            <h3>6. Detection &amp; Surveillance Gear</h3>
            <p>
                Sensors and autonomous drones reveal hidden hostiles, scan environments, and secure perimeters.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Detection &amp; Surveillance Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Proximity Sensor</td>
                            <td>Scouting 4m, Alert, Remote</td>
                            <td>1/2</td>
                            <td>1,000</td>
                            <td>Magnetic trip-sensor broadcasting automated alerts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Proximity Radar</td>
                            <td>Scouting 20m, 360-Sweep</td>
                            <td>2</td>
                            <td>25,000</td>
                            <td>Ground-penetrating radar mapping motion and structural voids.</td>
                        </tr>
                        <tr>
                            <td class="bold">Recon Drone</td>
                            <td>Fly 20m, Sensors 2, Remote</td>
                            <td>2</td>
                            <td>35,000</td>
                            <td>Micro-quadcopter equipped with night-vision optical sensors.</td>
                        </tr>
                        <tr>
                            <td class="bold">Forensic Sensor</td>
                            <td>Sensors 4, Chemical Scan</td>
                            <td>3</td>
                            <td>20,000</td>
                            <td>Handheld spectrometer for analyzing field ballistic evidence.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>7. Survival &amp; Field Utility</h4>
            <div class="table-container keep-together" style="margin: 1.5mm 0 2mm 0;">
                <div class="table-header">Survival &amp; Utility Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm;">Item</th>
                            <th style="padding: 1.2mm 1.2mm;">Properties</th>
                            <th style="padding: 1.2mm 1.2mm;">Load</th>
                            <th style="padding: 1.2mm 1.2mm;">Cost (Cr)</th>
                            <th style="padding: 1.2mm 1.2mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Vacuum / Hazard Suit</td>
                            <td>Environmental Immunity</td>
                            <td>1</td>
                            <td>5,000</td>
                            <td>Pressurized suit protecting against vacuum, heat, toxins.</td>
                        </tr>
                        <tr>
                            <td class="bold">Field Rations (1 Wk)</td>
                            <td>Sustenance</td>
                            <td>1</td>
                            <td>50</td>
                            <td>Nutrient-dense self-heating meal packs for expeditions.</td>
                        </tr>
                        <tr>
                            <td class="bold">Wilderness Camp</td>
                            <td>Squad Shelter</td>
                            <td>4</td>
                            <td>500</td>
                            <td>Pressurized pop-up tent and water cycler for 4 operators.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Commlink</td>
                            <td>Interfacing 2, Long-Range</td>
                            <td>0</td>
                            <td>1,000</td>
                            <td>Ear-piece transceiver with encrypted frequency hopping.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">83</span>
        </div>
    </div>"""
    pages.append(p83)

    # =========================================================================
    # SPREAD 9 (Pages 84-85): EXOTIC HARDWARE RULES & 4-TIER RARITY LADDER
    # =========================================================================

    p84 = """    <!-- =========================================================================
         PAGE 84 (Spread 9 Left) — EXOTIC HARDWARE LORE & OPERATIONAL RULES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-hardware-rules">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Exotic Hardware</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Exotic Hardware</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the commercial bazaars and scrap-alleys of the Sphere, money can buy you a great many things. A modest stack of Flotilla Credits will purchase a dependable pump shotgun that smells faintly of machine oil, a suit of reinforced ballistic weave that might keep your ribs inside your chest when an Ork marine kicks you through a bulkhead, or a pair of magnetic boots that only fail three percent of the time. These are the workhorse tools of Newcomer civilization: mass-produced, thoroughly documented, and priced so that a greenhorn Corsair cell doesn't bankrupt their sponsor on week two.
            </p>
            <p>
                And then there is the other stuff.
            </p>
            <p>
                <strong>Exotic Hardware</strong> refers to the narrow, intoxicating, and thoroughly lethal category of equipment that exists far beyond standard military procurement. These are the crown jewels of black-budget corporate skunkworks, the un-cataloged prototypes liberated from clandestine research labs on Nimbus, and the terrifying, cold-glass relics dragged kicking and screaming from subterranean Precursor vaults. In the lexicon of ancient fantasy tabletop games, they are the "magic items" of <em>Corsair</em>—objects possessing properties that seem to bend the rules of engagement.
            </p>
            <p>
                Yet in accordance with the fundamental laws of the Sphere, there is no magic here. Every prototype operates on bleeding-edge physics, extreme thermal shunting, and precision mechanical engineering. Every Precursor relic is a solid-state transducer tapping into the diffuse dark matter halo engineered by the Singularity. They are rare, exorbitantly expensive, and carried only by veterans who have both the coin to afford them and the physical constitution to carry their crushing weight.
            </p>

            <h3>The Rules of Exotic Hardware</h3>
            <p>
                Exotic Hardware functions under distinct operational constraints designed to reward tactical mastery without trivializing the hard-scrabble realities of combat:
            </p>
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 2mm;">
                <li><strong>Load Taxation Over Arbitrary Limits:</strong> There is no mystical "attunement" ceiling in <em>Corsair</em>. An operative is free to carry as many pieces of Exotic Hardware as their spine can endure. However, exotic hardware is dense, power-hungry, and heavily shielded. Weapons, power units, and field rigs carry substantial <strong>Load</strong> (typically Load 2 to 5), while exotic carapaces represent a massive encumbrance investment. Because every operative is bound by the absolute carrying capacity of <strong>12 + (Strength &times; 2)</strong>, packing multiple exotic systems forces agonizing compromises: you cannot wear a kinetic dissipation carapace, carry a dark-transducer carbine, and haul a seismic resonance rig without leaving your spare medical kits and sidearms back on the ship.</li>
                <li><strong>Action Point Economy:</strong> Activating an active exotic hardware function costs <strong>1 Action Point (AP)</strong>, or acts as an integrated enhancement to an existing 1-AP combat action. Passive defenses, sensory suites, and permanent material enhancements apply continuously, but active bursts always demand dedicated tactical focus.</li>
                <li><strong>Pacing Cooldowns &amp; Thermal Cycles:</strong> Bleeding-edge prototypes generate severe thermal spikes and power drains. Instead of abstract cooldown counters, exotic cooling cycles are measured directly in Corsair's narrative pacing rounds:
                    <ul>
                        <li><strong>Moment-to-Moment Cooldowns:</strong> Recover after <strong>1 moment-to-moment round</strong> (~5–10 seconds), resetting cleanly at the start of the operative's next combat turn.</li>
                        <li><strong>Place-to-Place Cooldowns:</strong> Recover after <strong>1 place-to-place round</strong> (~1 hour). The operative must complete their short transit or tactical breach, flush cryo-coolant loops, or vent residual capacitor heat into a starship heat sink before the system can fire again.</li>
                        <li><strong>Day-to-Day Cooldowns:</strong> Recover after <strong>1 day-to-day round</strong> (a full 24-hour downtime cycle), resetting after a proper shift of sleep, workshop calibration, and trickle-charging.</li>
                    </ul>
                </li>
            </ol>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">84</span>
        </div>
    </div>"""
    pages.append(p84)

    p85 = """    <!-- =========================================================================
         PAGE 85 (Spread 9 Right) — EXOTIC MAINTENANCE & 4-TIER RARITY LADDER
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-rarity-ladder">
        <div class="page-running-header">
            <span>Chapter 04: Exotic Hardware Ladder</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <ol start="4" style="margin-left: 3.5mm; padding-left: 0; margin-top: 0; margin-bottom: 2mm;">
                <li><strong>Irreplaceable Maintenance:</strong> When a piece of Exotic Hardware suffers structural damage and is reduced to 0 HP, it cannot be patched up with a generic soldering iron and a roll of thermal tape. Repairing a classified prototype requires an operative with a dedicated workshop and a successful <strong>Tinkering + Knowledge</strong> test against a Difficulty set by the item's Tier. Damaged Precursor relics cannot be repaired by mortal hands at all, unless the cell acquires rare molecular salvage or secures the favor of an Ancestral artisan or the scholar dragon Stormdrinker.</li>
                <li><strong>Non-Customizable Architecture (No Upgrade Kits):</strong> Exotic weapons, protective carapaces, and tactical hardware are precision-calibrated skunkworks trials or alien crystalline lattices whose tolerances operate at the atomic level. Because of this, <strong>Exotic Hardware cannot be customized or modified with standard Upgrade Kits</strong> (such as mastercrafted +1 Damage enhancements, Weight Reduction kits, or aftermarket weapon attachments). Attempting to drill, file, or bolt third-party components onto an exotic weapon short-circuits its induction coils, shatters non-baryonic barrel sleeves, or completely ruins its harmonic calibration. Their statistics, properties, and Load values are permanently fixed as written.</li>
            </ol>

            <h3>The 4-Tier Rarity &amp; Economic Ladder</h3>
            <p>
                To prevent market confusion and establish clear campaign progression, Exotic Hardware is organized into four distinct tiers of rarity, cost, and availability:
            </p>

            <div class="table-container keep-together" style="margin: 2mm 0 2.5mm 0;">
                <div class="table-header">Exotic Hardware Rarity &amp; Acquisition Ladder</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm; width: 12%;">Tier</th>
                            <th style="padding: 1.4mm 1.5mm; width: 22%;">Classification</th>
                            <th style="padding: 1.4mm 1.5mm; width: 22%;">Typical Cost (Credits)</th>
                            <th style="padding: 1.4mm 1.5mm; width: 44%;">Market Reality &amp; Acquisition</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tier 1</td>
                            <td class="bold" style="color: var(--color-gold);">Mil-Spec Skunkworks</td>
                            <td>15,000 &ndash; 30,000 CR</td>
                            <td>Limited-run military trials, skunkworks modifications, and high-spec aerospace machining from premier foundries (Caldera Foundry, Port Zenith Engineering, Panthera Arms). Available through high-end corporate fixers, retired veteran armories, or wealthy colonial sponsors.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 2</td>
                            <td class="bold" style="color: var(--color-gold);">Classified Prototypes</td>
                            <td>40,000 &ndash; 80,000 CR</td>
                            <td>Bleeding-edge corporate espionage targets, hybrid reverse-engineered alien polymers, and experimental cybernetic field rigs. Heavily guarded by corporate strike teams; acquired through corporate black-site heists, black-market auctions, or high-threat unsanctioned contracts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 3</td>
                            <td class="bold" style="color: var(--color-gold);">Precursor Relics</td>
                            <td>100,000 &ndash; 250,000 CR</td>
                            <td>Intact alien artifacts, non-baryonic catalytic lattices, and self-repairing alloys recovered from deep Vault excavations or the Evergaol crash site. Strictly illegal contraband under the Covenant Accords; traded only in deep-underworld circles (the Jailers, Iron Fang, or Scav warlords).</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 4</td>
                            <td class="bold" style="color: var(--color-gold);">Singularities &amp; Unique Wonders</td>
                            <td><strong>Priceless</strong> (Not for Sale)</td>
                            <td>Mythic, one-of-a-kind artifacts of campaign-defining significance (e.g., an intact dreadnought catalytic core, an uncorrupted Shard memory lattice, or an intact Precursor null-beam projector). Found exclusively as major campaign milestones or climactic salvage objectives.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Campaign Integration</h3>
            <p>
                Game Masters are encouraged to introduce Exotic Hardware as tangible milestones rather than routine loot drops. A Tier 1 prototype in the hands of an elite rival gives players an immediate preview of high-tier capabilities, while recovering a Tier 3 Precursor relic from an irradiated ruin should trigger attention from corporate retrieval squads, Covenant inquisitors, and pirate cartels alike.
            </p>
            <p>
                Because exotic hardware cannot be upgraded, finding a new tier of prototype represents a qualitative leap in operational doctrine, shifting how a Corsair approaches close-quarters combat, orbital insertions, and electronic warfare.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">85</span>
        </div>
    </div>"""
    pages.append(p85)

    # Assemble HTML
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corsair TTRPG — Chapter 04: Combat &amp; The Armory</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700;1,800&family=Barlow:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    
    <!-- Shared Modular Stylesheets -->
    <link rel="stylesheet" href="../assets/css/corsair-variables.css">
    <link rel="stylesheet" href="../assets/css/corsair-typography.css">
    <link rel="stylesheet" href="../assets/css/corsair-components.css">
    <link rel="stylesheet" href="../assets/css/corsair-layout.css">
    <link rel="stylesheet" href="../assets/css/corsair-print.css">
</head>
<body class="book-screen-canvas">

{"".join(pages)}

</body>
</html>
"""

    out_path = Path("html/04_Armory_and_Gear.html")
    out_path.write_text(html_template, encoding="utf-8")
    print(f"Successfully generated {out_path} with {len(pages)} pages (Pages 68 to {67 + len(pages)}).")

if __name__ == "__main__":
    build_full_fidelity_ch04()
