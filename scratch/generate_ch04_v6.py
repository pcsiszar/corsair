# -*- coding: utf-8 -*-
"""
Generate verbatim, continuous-flow, space-efficient html/04_Armory_and_Gear.html.
16 pages (8 complete two-page spreads: Pages 68 to 83).
Preserves 100% of markdown source text from:
- rulebook/combat/Combat.md
- rulebook/equipment/Equipment.md
- rulebook/equipment/Firearms.md
- rulebook/equipment/Melee.md
- rulebook/equipment/Armor.md
- rulebook/equipment/Gear.md
- rulebook/equipment/Exotic_Hardware.md

Invariants:
- Zero bottom voids (fill% ~80%-90%, bottom gaps ~15mm-35mm)
- Zero Column 3 horizontal overflow (scrollWidth == clientWidth == 688px)
- Zero <a> tags
- Zero made-up sci-fi telemetry tags
"""

from pathlib import Path

def build_perfect_ch04():
    pages = []

    # =========================================================================
    # SPREAD 1 (Pages 68-69): COMBAT MOVEMENT, VERTICALITY, FLYING & CONTESTS
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
                Not all battlefields are open fields. Movement can be hindered by obstacles, hazardous ground, or changes in elevation. This is represented by <strong>Difficult Terrain</strong>. When you move through difficult terrain, every 1 meter of progress costs you 2 meters of your speed. On a grid, moving into a space containing difficult terrain (such as mud, dense rubble, or thick vegetation) costs <strong>8 meters</strong> of movement instead of the usual 4 meters. This also applies if the <em>boundary</em> between two otherwise clear spaces is difficult (e.g., vaulting a barricade).
            </p>

            <h3>Contesting Movement</h3>
            <p>
                Movement is not always unopposed. A character can attempt to block or trip a creature moving through a space they occupy by contesting the moving creature's movement Success Test:
            </p>
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 0;">
                <li><strong>The Contester Narrates:</strong> Describe how you impede movement (tripping, grabbing, blocking).</li>
                <li><strong>The GM Chooses an Attribute:</strong> Relevant Attribute (e.g., Strength to grab, Agility to trip).</li>
                <li><strong>The Contest Roll:</strong> Roll d10s equal to the chosen Attribute.</li>
                <li><strong>Eliminating Dice:</strong> Each success (8+) eliminates one highest die from the movement roll. If no dice 8+ remain, the moving creature is stopped in the contester's space.</li>
            </ol>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">68</span>
        </div>
    </div>"""
    pages.append(p68)

    p69 = """    <!-- =========================================================================
         PAGE 69 (Spread 1 Right) — CONTESTING JAX, OCCUPANCY & CQC
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="contesting-occupancy-cqc">
        <div class="page-running-header">
            <span>Chapter 04: Tactical Movement</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <div class="callout callout-tactical keep-together" style="margin: 0 0 2.5mm 0; padding: 2.2mm 2.8mm;">
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

            <h3 style="margin-top: 1mm;">Space and Occupancy</h3>
            <p>
                In Corsair, combat is dynamic and often close-quartered. A single space on the battle map is not limited to one character. Understanding how multiple characters occupy and interact within a single space is key to tactical success. A single 4x4 meter space can comfortably house up to <strong>4 standard-sized creatures</strong>. Many actions, especially melee attacks and certain Teamwork maneuvers, require you to be in the same space as your target or ally.
            </p>

            <h4>Outnumbering</h4>
            <p>
                Ganging up on a foe is a valid and effective tactic. When you and your allies outnumber your opponents within a single space, you gain a significant advantage in melee combat. You receive a number of <strong>Upgrades</strong> on your melee attack tests equal to the difference between the number of allied creatures and hostile creatures in that space. For example, if 3 allies are in a space with 1 enemy, all allies receive <strong>2 Upgrades</strong> (3 &minus; 1 = 2) on their melee attacks against that enemy.
            </p>

            <h4>Melee Positioning</h4>
            <p>
                You can attack a creature in the same space as you, or an adjacent space. Melee attacks must use any combination of two separate Physical Attributes. When you attack a creature in an adjacent space, you move into it, provided it holds less than 4 creatures. If it already holds 4, you perform the attack from your current space, but count as if you and all allies in your space were in the target's space for outnumbering.
            </p>

            <h4>Creature Size</h4>
            <p>
                The capacity of a space is affected by the size of creatures within it: <strong>Large</strong> creatures take up the space of <strong>2</strong> standard creatures; <strong>Huge</strong> creatures take up the space of <strong>4</strong> standard creatures. Truly massive creatures may occupy multiple spaces at once, counting as a Large or Huge entity in each space for capacity and targeting.
            </p>

            <h3>Close Quarters Combat (CQC)</h3>
            <p>
                When you are in the same space as a hostile creature, you are in <strong>Close Quarters Combat (CQC)</strong>. This impacts ranged weaponry:
            </p>
            <ul>
                <li><strong>Firing in CQC:</strong> Firing a ranged weapon while in CQC inflicts <strong>2 Downgrades</strong> to your attack test.</li>
                <li><strong>Firing into CQC:</strong> Firing from outside into a space where allies and enemies are engaged in CQC inflicts <strong>1 Downgrade</strong> to your attack test.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">69</span>
        </div>
    </div>"""
    pages.append(p69)

    # =========================================================================
    # SPREAD 2 (Pages 70-71): COVER, THE ARMORY INVARIANTS & HANDGUNS
    # =========================================================================

    p70 = """    <!-- =========================================================================
         PAGE 70 (Spread 2 Left) — COVER TACTICS & THE ARMORY INVARIANTS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="cover-and-armory-invariants">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Cover &amp; The Armory</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Cover</h3>
            <p>
                Taking cover is a fundamental tactic for surviving a firefight. When a character is in a space that contains a source of cover (like a large crate, a sturdy pillar, or a low wall), they gain a flat bonus to their Protection against attacks originating from <em>outside</em> of their space. This bonus stacks directly with Protection from armor and shields:
            </p>
            <ul>
                <li><strong>Light Cover:</strong> (<strong>+1 Protection</strong>) A small object offering partial concealment, like a thin pipe, light furniture, or a small fuel drum.</li>
                <li><strong>Medium Cover:</strong> (<strong>+2 Protection</strong>) A solid object hiding a significant portion of your body, like a large engine block or thick metal bulkhead.</li>
                <li><strong>Heavy Cover:</strong> (<strong>+3 Protection</strong>) A large durable fortification, like a reinforced bunker wall, blast gantry, or armored vehicle chassis.</li>
            </ul>

            <h3>Destroying Cover</h3>
            <p>
                Light, Medium, and Heavy Cover have <strong>12, 24, and 36 health segments</strong> and an innate Protection of <strong>4, 8, and 12</strong> respectively when directly targeted. Attacking cover is a <strong>Success Test</strong> instead of a Complex one. For every 12 damage the cover absorbs, its provided Protection benefit is reduced by 1. Specialized breaching charges, anti-materiel weapons, and demolition explosives specifically ignore cover's innate Protection.
            </p>

            <h3>Cover Facing</h3>
            <p>
                Using cover effectively is about angling yourself against incoming fire. The first time you take an attack benefiting from cover, draw a line from the attacker to your center: whichever side of your space the line crosses becomes your <strong>covering side</strong>. When the line crosses a corner, both adjacent sides become covering sides. On subsequent attacks:
            </p>
            <ul>
                <li><strong>Full Bonus:</strong> Crossing the covering side grants full Protection bonus.</li>
                <li><strong>Reduced Bonus:</strong> Crossing an adjacent side reduces bonus by 1 on hex, and by 2 on square grids.</li>
                <li><strong>No Bonus (Exposed):</strong> Crossing the non-adjacent side grants no benefit.</li>
            </ul>

            <h2 style="margin-top: 2mm;">The Armory &amp; Equipment</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Not every item carried has a significant mechanical impact. Everyday objects like commlinks, keys, or sentimental trinkets are part of a character's belongings without needing rules. Items providing a distinct tactical advantage—weapons, armor, tools—are classified as <strong>Equipment</strong>, governed by the <strong>Load</strong> system.
            </p>

            <h3>The Load Invariant</h3>
            <p>
                Every piece of equipment has a <strong>Load</strong> value representing its weight, size, and cumbersomeness. A character's maximum Load capacity is:
            </p>
            <div class="callout callout-tactical keep-together" style="margin: 1.5mm 0; padding: 1.8mm 2.5mm; text-align: center;">
                <div style="font-family: var(--font-heading); font-size: 10.5pt; font-weight: 700; color: var(--color-gold);">
                    Maximum Load Capacity = 12 + (Strength &times; 2)
                </div>
            </div>
            <p>
                This limit is absolute; a character cannot exceed this capacity under any circumstances. Leaving capacity open is wise for carrying field salvage or mission objectives.
            </p>

            <h3>Equipment Categories &amp; Damage Bonus</h3>
            <p>
                Equipment is divided into Weapons, Armor, and Exotic Hardware. All weapons share the <strong>Damage Bonus</strong>: a flat value added directly to success points generated on a successful attack roll, strictly increasing damage dealt.
            </p>

            <h3>Equipment Damage &amp; Field Repairs</h3>
            <p>
                Deployable gear, fortifications, vehicles, and hardware have <strong>HP</strong> and are disabled at 0 HP. An operator carrying a toolkit with <strong>Tinkering</strong> can spend <strong>1 AP</strong> to make a <strong>Tinkering + Knowledge</strong> Success Test, recovering <strong>1 HP per Success Point</strong> up to maximum.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""
    pages.append(p70)

    p71 = """    <!-- =========================================================================
         PAGE 71 (Spread 2 Right) — FIREARMS MECHANICS & HANDGUNS CATALOG
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-and-handguns">
        <div class="page-running-header">
            <span>Chapter 04: Firearms &amp; Handguns</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Firearms</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the cold vacuum of space, across contested orbital platforms, and inside pressurized ship corridors, firearms are the ultimate arbiters of ranged combat. Ranging from rugged chemical slugthrowers to electro-thermal chemical (ETC) rifles and high-velocity magnetic rail drivers, firearms give Corsairs the range, stopping power, and suppression capability necessary to overwhelm hostile forces before they close the distance.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 1.5mm;">
                Every firearm is defined by mechanical attributes dictating tactical performance:
            </p>
            <ul style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 2mm;">
                <li><strong>Accuracy (Short / Medium / Long / Extreme):</strong> Ranged attacks always pair weapon Accuracy at the target's distance with <strong>Finesse</strong> (<strong>Accuracy + Finesse</strong>):
                    <ul>
                        <li><strong>Short (S):</strong> 0–5 spaces (~0–20m). Corridors, breaches, point-blank skirmishes.</li>
                        <li><strong>Medium (M):</strong> 6–12 spaces (~20–40m). Cargo bays, hangar decks, station concourses.</li>
                        <li><strong>Long (L):</strong> 13–20 spaces (~40–80m). Maintenance tunnels, gantries, open terrain.</li>
                        <li><strong>Extreme (E):</strong> 20+ spaces (~80m+). Standoff defense, sniper perches. Dash (<code>&minus;</code>) = out of range.</li>
                    </ul>
                </li>
                <li><strong>Rate of Fire (RoF):</strong> Strict upper limit on total <strong>Crit Effects</strong> and <strong>Chain Effects</strong> on an attack roll:
                    <ul>
                        <li><strong>RoF 0 (Heavy-Hitters):</strong> Single-shot rifles, heavy revolvers. No burst Crits/Chain.</li>
                        <li><strong>RoF 1 (Precision):</strong> Duty pistols, marksman rifles (up to 1 Crit/Chain).</li>
                        <li><strong>RoF 2 (Burst/Auto):</strong> Assault carbines, combat shotguns (up to 2 Crits/Chain).</li>
                        <li><strong>RoF 3–4 (Suppression):</strong> Squad automatics, heavy machine guns, rotary cannons (up to 3–4 Crits/Chain).</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to success points on a hit.</li>
                <li><strong>Hands:</strong> 1H sidearm vs 2H shoulder-fired platform. &middot; <strong>Load &amp; Cost:</strong> Mass in Load system; Credits.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 2mm;">
                <strong>Panthera Arms:</strong> Sleek high-tolerance carbines and marksman rifles. &middot; <strong>Vandal's Workshop:</strong> Stamped-sheet high-RoF submachine guns cycling in vacuum. &middot; <strong>Caldera Foundry:</strong> Heavy-bore rifles and trench shotguns for boarding defense. &middot; <strong>Ker'Satz Korp:</strong> Magnetic rail drivers and magnum revolvers. &middot; <strong>Chidori-Qwei:</strong> Lightweight polymer smart-linked sidearms.
            </p>

            <h3 style="margin-top: 1mm;">Handguns Catalog</h3>
            <div class="table-container keep-together" style="margin: 1.5mm 0 0 0;">
                <div class="table-header">Handguns Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 1.0mm;">Weapon Name</th>
                            <th style="padding: 1.0mm 1.0mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.0mm 1.0mm;">RoF</th>
                            <th style="padding: 1.0mm 1.0mm;">H</th>
                            <th style="padding: 1.0mm 1.0mm;">Dmg</th>
                            <th style="padding: 1.0mm 1.0mm;">Load</th>
                            <th style="padding: 1.0mm 1.0mm;">Cost</th>
                            <th style="padding: 1.0mm 1.0mm;">Description</th>
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
                            <td>Concealable polymer pistol for covert carry.</td>
                        </tr>
                        <tr>
                            <td class="bold">Service Pistol</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>800</td>
                            <td>Standard-issue semi-auto duty sidearm.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Revolver</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>1,200</td>
                            <td>Magnum cylinder gun with punishing recoil.</td>
                        </tr>
                        <tr>
                            <td class="bold">Machine Pistol</td>
                            <td>3 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1</td>
                            <td>1,500</td>
                            <td>Compact automatic handgun for point-blank bursts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hand Cannon</td>
                            <td>2 / 3 / 2 / 0</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>2,200</td>
                            <td>Anti-armor kinetic handgun for devastating shots.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">71</span>
        </div>
    </div>"""
    pages.append(p71)

    # =========================================================================
    # SPREAD 3 (Pages 72-73): SMGS, SHOTGUNS, RIFLES, HEAVY SUPPORT & FIREFIGHT
    # =========================================================================

    p72 = """    <!-- =========================================================================
         PAGE 72 (Spread 3 Left) — SMGS, SHOTGUNS & COMBAT RIFLES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-smgs-rifles">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Long Guns &amp; Shotguns</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Submachine Guns &amp; Shotguns</h3>
            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 1.2mm;">
                Close-quarters primary weapons engineered for boarding operations, clearing tight ship bulkheads, and dominating short-range firefights across station corridors.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1.5mm 0;">
                <div class="table-header">Submachine Guns &amp; Shotguns Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Weapon Name</th>
                            <th style="padding: 0.9mm 0.9mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 0.9mm 0.9mm;">RoF</th>
                            <th style="padding: 0.9mm 0.9mm;">H</th>
                            <th style="padding: 0.9mm 0.9mm;">Dmg</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
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
                            <td>Collapsible submachine gun for vehicle crews and boarding.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical SMG</td>
                            <td>3 / 4 / 2 / 0</td>
                            <td>3</td>
                            <td>2H</td>
                            <td>+1</td>
                            <td>2</td>
                            <td>2,800</td>
                            <td>Automatic platform with recoil compensators and high cyclic rate.</td>
                        </tr>
                        <tr>
                            <td class="bold">Trench Shotgun</td>
                            <td>5 / 2 / &minus; / &minus;</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>2</td>
                            <td>2,400</td>
                            <td>Heavy pump scattergun delivering catastrophic kinetic spread.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Shotgun</td>
                            <td>4 / 3 / 0 / &minus;</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>3,500</td>
                            <td>Semi-automatic magazine-fed shotgun for breaching operations.</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Scattergun</td>
                            <td>4 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,000</td>
                            <td>Drum-fed scattergun delivering high-volume projectile swarms.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1.5mm;">Rifles</h3>
            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 1.2mm;">
                Versatile long guns balancing effective range, stopping power, and tactical flexibility across ship corridors and planetary battlegrounds.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1mm 0;">
                <div class="table-header">Rifles Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Weapon Name</th>
                            <th style="padding: 0.9mm 0.9mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 0.9mm 0.9mm;">RoF</th>
                            <th style="padding: 0.9mm 0.9mm;">H</th>
                            <th style="padding: 0.9mm 0.9mm;">Dmg</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
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
                            <td>Short-barreled rifle for fast target acquisition and mobility.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Rifle</td>
                            <td>2 / 4 / 3 / 1</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,800</td>
                            <td>Standard military battle rifle delivering disciplined burst fire.</td>
                        </tr>
                        <tr>
                            <td class="bold">Battle Rifle</td>
                            <td>2 / 3 / 4 / 2</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>3</td>
                            <td>5,500</td>
                            <td>Heavy-caliber rifle engineered for armor-cracking penetration.</td>
                        </tr>
                        <tr>
                            <td class="bold">DMR</td>
                            <td>1 / 3 / 5 / 3</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>7,000</td>
                            <td>Designated marksman rifle with high-magnification optics.</td>
                        </tr>
                        <tr>
                            <td class="bold">Sniper Rifle</td>
                            <td>0 / 2 / 5 / 4</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+5</td>
                            <td>4</td>
                            <td>9,500</td>
                            <td>Bolt-action rifle delivering extreme terminal ballistics at standoff.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 7.9pt; line-height: 1.28; color: var(--text-muted); margin-top: 1mm;">
                <em>Corridor Ballistics:</em> In pressurized habitats, smoothbore scatterguns and low-velocity carbines are preferred by boarding crews because kinetic pellets flatten against bulkheads rather than puncturing environmental seals or coolant loops.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">72</span>
        </div>
    </div>"""
    pages.append(p72)

    p73 = """    <!-- =========================================================================
         PAGE 73 (Spread 3 Right) — HEAVY SUPPORT, DUAL WIELDING & FIREFIGHT
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-heavy-customization-action">
        <div class="page-running-header">
            <span>Chapter 04: Heavy Support &amp; Ranged Combat</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Heavy Support Weapons</h3>
            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 1.2mm;">
                Crew-served and reinforced heavy platforms requiring substantial physical leverage to operate, delivering unmatched suppressive fire and anti-armor kinetic energy.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1.5mm 0;">
                <div class="table-header">Heavy Support Weapons Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Weapon Name</th>
                            <th style="padding: 0.9mm 0.9mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 0.9mm 0.9mm;">RoF</th>
                            <th style="padding: 0.9mm 0.9mm;">H</th>
                            <th style="padding: 0.9mm 0.9mm;">Dmg</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
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
                            <td>Belt-fed light machine gun for continuous squad suppression.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Machine Gun</td>
                            <td>3 / 5 / 4 / 2</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>5</td>
                            <td>12,000</td>
                            <td>Large-caliber gun shredding light vehicles and barricades.</td>
                        </tr>
                        <tr>
                            <td class="bold">Rotary Autocannon</td>
                            <td>5 / 4 / 2 / 1</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>5</td>
                            <td>16,000</td>
                            <td>Multi-barrel motorized cannon delivering devastating saturation.</td>
                        </tr>
                        <tr>
                            <td class="bold">Anti-Materiel (AMR)</td>
                            <td>0 / 2 / 5 / 5</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+7</td>
                            <td>5</td>
                            <td>15,000</td>
                            <td>Magnetic rail rifle disabling light vehicles and bulkheads.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Dual Wielding Firearms</h3>
            <p>
                A combatant can choose to wield a one-handed firearm in each hand, laying down intense suppressive fire:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield firearms with the <strong>1H</strong> designation (holding one sidearm in each hand).</li>
                <li><strong>Combined Firepower:</strong> Add together both the flat <strong>Damage Bonus</strong> and the <strong>Rate of Fire (RoF)</strong> of the two firearms.</li>
                <li><strong>Worse Accuracy:</strong> Discharging two weapons compromises sight alignment and recoil control: use the <strong>worse (lower) Accuracy rating</strong> at the target's current range band.</li>
            </ul>

            <h3>Firearm Upgrade Kits</h3>
            <p>
                Stock firearms can be customized into mastercrafted weapons through aerospace machining. Limit: <strong>3 Upgrade Kits</strong> (2H) or <strong>2 Upgrade Kits</strong> (1H sidearms). Costs: 1st: <strong>10,000 Cr</strong> &middot; 2nd: <strong>25,000 Cr</strong> &middot; 3rd: <strong>50,000 Cr</strong>. Choices:
            </p>
            <ul>
                <li><strong>Lightweight Chassis:</strong> Precision skeletonization reduces <strong>Load by 1</strong> (min 1/2).</li>
                <li><strong>Lethal Tuning:</strong> Match-grade rifling increases flat <strong>Damage Bonus by +1</strong>.</li>
                <li><strong>Recoil Dampening:</strong> Hydraulic buffer tubes increase <strong>Rate of Fire (RoF) by 1</strong>.</li>
                <li><strong>Optic Calibration:</strong> Thermal optics increase <strong>Accuracy by +1</strong> at one range band.</li>
            </ul>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: The Hangar Deck Firefight</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax targets an armed mercenary <strong>8 spaces (~26m)</strong> away at <strong>Medium Range</strong> behind freight containers. Jax is armed with an <strong>Assault Rifle</strong> (Accuracy <code>2 / 4 / 3 / 1</code>, RoF 2, 2H, Load 3, <strong>+2 Damage Bonus</strong>). Jax has <strong>Finesse 5</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. Action Roll (Finesse 5):</strong> Jax rolls 5d10: <code>[2, 5, 8, 8, 9]</code>—scoring three Hits. The roll succeeds; Jax spends one Hit (8) on an <strong>Upgrade Effect</strong>, stepping up one Success die to a <strong>d12</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>2. Success Roll (Accuracy 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 7, 8]</code> and a <strong>10</strong> on the d12. Both 8 and 10 are Hits.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>3. Effects &amp; RoF:</strong> Jax spends both Hits on <strong>Crit Effects</strong> (+2 SP each). The Assault Rifle's <strong>RoF 2</strong> perfectly accommodates 2 Crits.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    <strong>4. Total Damage:</strong> 7 SP (highest non-spent die) + 4 SP (2 Crits) + 2 (Rifle Bonus) = <strong>13 points of damage</strong>, punching cleanly through the container seam!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">73</span>
        </div>
    </div>"""
    pages.append(p73)

    # =========================================================================
    # SPREAD 4 (Pages 74-75): MELEE WEAPONS, SHIELDS & BOARDING ACTION
    # =========================================================================

    p74 = """    <!-- =========================================================================
         PAGE 74 (Spread 4 Left) — MELEE WEAPONS RULES, DUAL WIELDING & SHIELDS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-weapons-fundamentals">
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
            <ul>
                <li><strong>Damage Type &amp; Favored Pair:</strong> Melee weapons inflict damage through one of three physical methods, each paired with a favored Attribute Pair that maximizes leverage:
                    <ul>
                        <li><strong>Piercing (Agility + Finesse):</strong> Pinpoint thrusts directed at structural seams, visor slits, and armor joints.</li>
                        <li><strong>Slashing (Agility + Strength):</strong> Sweeping kinetic cuts combining dynamic movement with heavy cutting force.</li>
                        <li><strong>Striking (Strength + Finesse):</strong> Controlled bone-shattering impacts delivered with precise leverage.</li>
                    </ul>
                </li>
                <li><strong>Favored Pair Damage Bonus:</strong> Attacking with a weapon's favored Attribute Pair adds the <strong>lower attribute</strong> directly to damage, unlocking a substantial damage boost.</li>
                <li><strong>Minimum Strength (Min STR):</strong> Weapons require physical leverage. For 1H weapons, if Strength &lt; Min STR, you must wield it with <strong>two hands</strong>. For 2H weapons, if Strength &lt; Min STR, you <strong>cannot attack</strong> with it under any circumstances.</li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to success points on a hit. Heavier weapons feature significantly larger flat Damage Bonuses.</li>
                <li><strong>Hands, Load &amp; Cost:</strong> Mass in the Load system and galactic market price in Credits.</li>
            </ul>

            <h3>Dual Wielding Melee Weapons</h3>
            <p>
                You can dual wield weapons with the <strong>1H</strong> designation, provided you meet each weapon's Minimum Strength individually. When attacking, combine the flat <strong>Damage Bonus of both weapons</strong>. You designate which weapon leads the strike to determine <strong>Damage Type</strong> (Piercing, Slashing, Striking) and favored pair. Attacking with that favored pair adds the lower attribute to the combined total.
            </p>

            <h3>Melee Upgrade Kits</h3>
            <p>
                Melee weapons accept up to <strong>3 Upgrade Kits</strong> (2H) or <strong>2 Upgrade Kits</strong> (1H). Costs: 1st: <strong>10k Cr</strong> &middot; 2nd: <strong>25k Cr</strong> &middot; 3rd: <strong>50k Cr</strong>. Choices: <em>Lightweight Tuning</em> (&minus;1 Load, min 1/2), <em>Lethal Edge / Weighted Core</em> (+1 Damage Bonus).
            </p>

            <h3>Shields</h3>
            <p>
                Shields are rigid barriers constructed from ballistic polymers, ceramics, or titanium. Held in the off-hand (1H), they grant a flat bonus to <strong>Physical Protection</strong> that stacks directly with worn armor. You cannot dual wield shields nor benefit from more than one shield at a time. If Strength &lt; Min STR, you cannot wield the shield.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0 0 0;">
                <div class="table-header">Tactical Shields Catalog</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 1.0mm;">Shield Name</th>
                            <th style="padding: 1.0mm 1.0mm;">Protection</th>
                            <th style="padding: 1.0mm 1.0mm;">STR</th>
                            <th style="padding: 1.0mm 1.0mm;">H</th>
                            <th style="padding: 1.0mm 1.0mm;">Load</th>
                            <th style="padding: 1.0mm 1.0mm;">Cost</th>
                            <th style="padding: 1.0mm 1.0mm;">Description</th>
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
                            <td>Arm-mounted composite disc parrying blades.</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Shield</td>
                            <td>+2 Prot</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>2</td>
                            <td>2,500</td>
                            <td>Polycarbonate barrier providing solid coverage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Ballistic Shield</td>
                            <td>+3 Prot</td>
                            <td>6</td>
                            <td>1H</td>
                            <td>4</td>
                            <td>6,500</td>
                            <td>Ceramic-composite pavise withstanding rifle fire.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">74</span>
        </div>
    </div>"""
    pages.append(p74)

    p75 = """    <!-- =========================================================================
         PAGE 75 (Spread 4 Right) — COMPLETE 15-WEAPON MELEE CATALOG & WALKTHROUGH
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-catalog-and-action">
        <div class="page-running-header">
            <span>Chapter 04: Melee Catalog &amp; Combat</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Melee Weapons Catalog</h3>
            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 1.2mm;">
                The table below outlines standard melee weapon archetypes across all weight classes and damage types.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 2mm 0;">
                <div class="table-header">Melee Weapons Catalog</div>
                <table class="rules-table" style="font-size: 7.2pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.8mm 0.8mm;">Weapon Name</th>
                            <th style="padding: 0.8mm 0.8mm;">Type</th>
                            <th style="padding: 0.8mm 0.8mm;">STR</th>
                            <th style="padding: 0.8mm 0.8mm;">H</th>
                            <th style="padding: 0.8mm 0.8mm;">Dmg</th>
                            <th style="padding: 0.8mm 0.8mm;">Load</th>
                            <th style="padding: 0.8mm 0.8mm;">Cost</th>
                            <th style="padding: 0.8mm 0.8mm;">Description</th>
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
                            <td>Concealable thrusting blade for unarmored seams.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Knife</td>
                            <td>Slashing</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>200</td>
                            <td>Balanced single-edged utility and combat knife.</td>
                        </tr>
                        <tr>
                            <td class="bold">Knuckleduster</td>
                            <td>Striking</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>100</td>
                            <td>Fitted metal fist reinforcement concentrating force.</td>
                        </tr>
                        <tr>
                            <td class="bold">Dagger</td>
                            <td>Piercing</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>400</td>
                            <td>Double-edged dagger for penetrating thrusts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hatchet / Machete</td>
                            <td>Slashing</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>500</td>
                            <td>Forward-weighted blade for clearing and combat.</td>
                        </tr>
                        <tr>
                            <td class="bold">Baton / Club</td>
                            <td>Striking</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>300</td>
                            <td>Weighted polymer or steel rod for blunt trauma.</td>
                        </tr>
                        <tr>
                            <td class="bold">Shortsword</td>
                            <td>Piercing</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,200</td>
                            <td>Straight rigid blade optimized for mobility lunges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Boarding Axe</td>
                            <td>Slashing</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,500</td>
                            <td>Sturdy single-handed axe for doors and armor.</td>
                        </tr>
                        <tr>
                            <td class="bold">Mace / Crowbar</td>
                            <td>Striking</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Flanged iron bludgeon cracking bone through plating.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spear</td>
                            <td>Piercing</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,200</td>
                            <td>Two-handed hafted spear delivering deep thrusts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Longsword</td>
                            <td>Slashing</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,800</td>
                            <td>Versatile tempered blade generating cutting arcs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Warhammer</td>
                            <td>Striking</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,400</td>
                            <td>Reinforced hammerhead built to crumple armor.</td>
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
                            <td>Massive two-handed blade for devastating cleaves.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Maul</td>
                            <td>Striking</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,800</td>
                            <td>Enormous sledgehammer delivering pulverizing force.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: The Boarding Action Strike</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax enters a contested airlock space occupied by a hostile pirate enforcer. Armed with a <strong>Boarding Axe</strong> (Slashing, Min STR 3, 1H, Load 2, <strong>+2 Damage Bonus</strong>), Jax initiates a melee strike. Jax has <strong>Strength 5</strong>, <strong>Agility 4</strong>, and <strong>Finesse 3</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Because the Boarding Axe is Slashing, its favored pair is <strong>Agility + Strength</strong>. Jax's Strength 5 easily satisfies Min STR 3, allowing single-handed wielding.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. Action Roll (Strength 5):</strong> Jax rolls 5d10: <code>[3, 5, 7, 8, 9]</code>. Both 8 and 9 are Hits. The Action Roll succeeds. Jax spends one Hit (8) to activate an <strong>Upgrade Effect</strong>, stepping up one Success die to a <strong>d12</strong>.
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
            <span class="page-num">75</span>
        </div>
    </div>"""
    pages.append(p75)

    # =========================================================================
    # SPREAD 5 (Pages 76-77): ARMOR STATS, PROPERTIES, FULL CATALOG & BARRAGE
    # =========================================================================

    p76 = """    <!-- =========================================================================
         PAGE 76 (Spread 5 Left) — ARMOR MECHANICS, PROPERTIES & LIGHT ARMOR
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-mechanics-light">
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
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.5mm;">
                <li><strong>Protection:</strong> Flat integer subtracted directly from incoming damage before it affects health. Stacks with <strong>Shields</strong> and <strong>Cover</strong>. An operative can only wear <strong>one suit of armor</strong> at a time.</li>
                <li><strong>Load &amp; No Minimum Strength:</strong> Armor counts against Load capacity (<code>12 + Strength &times; 2</code>). Any operative can wear any suit of armor if they have sufficient Load capacity. However, heavier suits feature <strong>Cumbersome (X)</strong>.</li>
                <li><strong>Armor Properties:</strong> Specialized engineering features:
                    <ul>
                        <li><strong>Cumbersome (X):</strong> Mass restricts articulation. Suffer <strong>X Downgrades on all tests involving Agility</strong> (movement, athletics, stealth, agility attack/contest rolls).</li>
                        <li><strong>Hardened:</strong> Ceramic strike faces diffuse penetrators. An attacker's <strong>Crit Effect</strong> grants only <strong>+1 SP per Hit spent</strong> (instead of +2).</li>
                        <li><strong>Blast-Dampened:</strong> Concussive baffles dissipate shockwaves, granting <strong>+2 additional Protection against Area Attacks and Explosives</strong>.</li>
                        <li><strong>Tactical Harness (X):</strong> Features <strong>X dedicated Load slots for any equipment</strong> (items stowed do not count against standard Load capacity, up to X).</li>
                        <li><strong>Muffled:</strong> Acoustic dampeners suppress gear rattle, granting <strong>+1 Upgrade on Stealth tests</strong>.</li>
                    </ul>
                </li>
            </ul>

            <h3>Armor Upgrade Kits</h3>
            <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.5mm;">
                Armor accepts up to <strong>3 Upgrade Kits</strong>. Costs: 1st: <strong>50k Cr</strong> &middot; 2nd: <strong>100k Cr</strong> &middot; 3rd: <strong>180k Cr</strong>. Choices: <em>Reinforced Plating</em> (+1 Protection, max +3), <em>Lightweight Composites</em> (&minus;1 Load, min 1), <em>Specialized Modification</em> (Hardened, Blast-Dampened, Tactical Harness +1, or Muffled).
            </p>

            <h3 style="margin-top: 1mm;">Light Armor (Load 1–3 &middot; Prot 2–4 &middot; No Agility Penalties)</h3>
            <div class="table-container keep-together" style="margin: 1mm 0 0 0;">
                <div class="table-header">Light Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Armor Name</th>
                            <th style="padding: 0.9mm 0.9mm;">Prot</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Properties</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost (Cr)</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Padded Flightsuit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>&mdash;</td>
                            <td>1,200</td>
                            <td>Pressurized spacer flight jumpsuit; unencumbering.</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltration Suit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>Muffled</td>
                            <td>3,500</td>
                            <td>Acoustic-dampening bodysuit favored by covert agents.</td>
                        </tr>
                        <tr>
                            <td class="bold">Armored Jacket</td>
                            <td>3</td>
                            <td>2</td>
                            <td>&mdash;</td>
                            <td>3,000</td>
                            <td>Everyday utility jacket lined with ballistic aramid.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hardened Vest</td>
                            <td>3</td>
                            <td>2</td>
                            <td>Hardened</td>
                            <td>5,500</td>
                            <td>Security vest fitted with ceramic strike faces.</td>
                        </tr>
                        <tr>
                            <td class="bold">Light Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>&mdash;</td>
                            <td>10,000</td>
                            <td>Mil-spec tactical plate carrier balancing defense and mobility.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spec-Ops Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>Hardened</td>
                            <td>18,000</td>
                            <td>Plate carrier featuring boron-carbide inserts for peak light defense.</td>
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
         PAGE 77 (Spread 5 Right) — MEDIUM & HEAVY ARMOR & PROTECTION WALKTHROUGH
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-medium-heavy-barrage">
        <div class="page-running-header">
            <span>Chapter 04: Medium &amp; Heavy Armor</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Medium Armor (Frontline Assault &middot; Load 4–5 &middot; Prot 5–6)</h3>

            <div class="table-container keep-together" style="margin: 1mm 0 1.5mm 0;">
                <div class="table-header">Medium Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Armor Name</th>
                            <th style="padding: 0.9mm 0.9mm;">Prot</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Properties</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost (Cr)</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>&mdash;</td>
                            <td>30,000</td>
                            <td>Ceramic-carbide carrier; peak unencumbered protection.</td>
                        </tr>
                        <tr>
                            <td class="bold">Flak Combat Rig</td>
                            <td>5</td>
                            <td>4</td>
                            <td>Blast-Dampened</td>
                            <td>38,000</td>
                            <td>Shrapnel-lined assault vest designed for grenade blasts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Vanguard Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>Hardened, Tac (1)</td>
                            <td>45,000</td>
                            <td>Squad-leader vest with trauma plates and utility webbing.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Carapace Armor</td>
                            <td>6</td>
                            <td>5</td>
                            <td>Cumbersome (1)</td>
                            <td>65,000</td>
                            <td>Full-body interlocking alloy carapace; stopping power.</td>
                        </tr>
                        <tr>
                            <td class="bold">Bastion Carapace</td>
                            <td>6</td>
                            <td>5</td>
                            <td>Cumbersome (1), Hard, Tac (1)</td>
                            <td>85,000</td>
                            <td>Fortified trench carapace weathering sustained fire.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1.5mm;">Heavy Armor (Walking Fortresses &middot; Load 6–7 &middot; Prot 7–8)</h3>

            <div class="table-container keep-together" style="margin: 1mm 0 1.5mm 0;">
                <div class="table-header">Heavy Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Armor Name</th>
                            <th style="padding: 0.9mm 0.9mm;">Prot</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Properties</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost (Cr)</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Breacher Carapace</td>
                            <td>7</td>
                            <td>6</td>
                            <td>Cumbersome (1), Blast, Tac (1)</td>
                            <td>140,000</td>
                            <td>Heavy blast apron and limb plating for airlock point-men.</td>
                        </tr>
                        <tr>
                            <td class="bold">Juggernaut Armor</td>
                            <td>7</td>
                            <td>6</td>
                            <td>Cumbersome (1), Hardened</td>
                            <td>160,000</td>
                            <td>Dense fortress armor shrugging off critical hits and slugs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Titan Rig</td>
                            <td>8</td>
                            <td>7</td>
                            <td>Cumbersome (2), Hard, Blast, Tac (2)</td>
                            <td>280,000</td>
                            <td>Massive mechanized siege carapace; pinnacle of protection.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together" style="margin: 1.5mm 0 0 0; padding: 2.2mm 2.8mm;">
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
            <span class="page-num">77</span>
        </div>
    </div>"""
    pages.append(p77)

    # =========================================================================
    # SPREAD 6 (Pages 78-79): GEAR RULES, MOBILITY, FORTIFICATIONS & EXPLOSIVES
    # =========================================================================

    p78 = """    <!-- =========================================================================
         PAGE 78 (Spread 6 Left) — TACTICAL GEAR RULES & MOBILITY HARDWARE
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
                <li><strong>Dedicated Attributes &amp; Test Pairs:</strong> Gear provides dedicated item attributes (such as <em>Mobility</em>, <em>Medicine</em>, <em>Sensors</em>, <em>Tinkering</em>, <em>Locksmith</em>, <em>Disguise</em>, <em>Forgery</em>, <em>Interfacing</em>, <em>Hacking</em>, <em>Ordnance</em>). The item's attribute pairs with a core attribute to form the dice pool.</li>
                <li><strong>Action Point Costs:</strong> Activating gear requires <strong>1 Action Point (AP)</strong>, unless explicitly noted otherwise. Passive items (deploying Cover) still cost 1 AP.</li>
                <li><strong>Capacity &amp; Automatic Refill:</strong> Expendable gear has an innate <strong>Capacity (Cap X)</strong>. Charges <strong>automatically refill to maximum</strong> whenever visiting an eligible supply hub (starship, clinic, armory, depot) during place-to-place or day-to-day pacing, without spending Credits.</li>
                <li><strong>Stand-Alone Explosive Rolls:</strong> Explosives resolve as Area Attack Success Tests rolling pure <strong>Ordnance</strong> pools without pairing with an attribute.</li>
                <li><strong>Upgrade Compatibility:</strong> Gear can be enhanced with up to 3 standard Upgrade Kits to reduce Load by 1 or increase primary attribute by +1.</li>
            </ol>

            <h3>1. Mobility Gear</h3>
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
                            <td>Compact thruster pack for short bounds.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Jetpack</td>
                            <td>Jetpack (12m), Mobility 4</td>
                            <td>4</td>
                            <td>72,000</td>
                            <td>Mil-spec jump rig with balanced fuel.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Jump-Rig</td>
                            <td>Jetpack (16m), Mobility 5</td>
                            <td>5</td>
                            <td>120,000</td>
                            <td>High-output vector thruster chassis.</td>
                        </tr>
                        <tr>
                            <td class="bold">Gecko Climbing Kit</td>
                            <td>Mobility 3, Adhesion</td>
                            <td>1</td>
                            <td>15,000</td>
                            <td>Magnetic gloves and boots for scaling hulls.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Zipline (40m)</td>
                            <td>Zipline (40m), 24 HP</td>
                            <td>3</td>
                            <td>15,000</td>
                            <td>Pneumatic launcher deploying motorized cables.</td>
                        </tr>
                        <tr>
                            <td class="bold">Standard Grapple</td>
                            <td>Grapple (8m), Mob 3, Cap 3</td>
                            <td>2</td>
                            <td>5,000</td>
                            <td>Gas-tether launcher for rapid ascent.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Grapple</td>
                            <td>Grapple (16m), Mob 4, Cap 4</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>Reinforced winch rig with extended pull.</td>
                        </tr>
                        <tr>
                            <td class="bold">High-Tensile Rope</td>
                            <td>Utility Cordage (40m)</td>
                            <td>1</td>
                            <td>100</td>
                            <td>Synthetic braided line for rappelling.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Mobility Properties</h4>
            <ul>
                <li><strong>Jetpack (Xm):</strong> Activating costs <strong>1 AP</strong>; Success Test using <strong>Mobility + Agility</strong>. Move Xm plus 1m per SP. Fly 3D, hover, ignore difficult terrain and falling damage. Vector Boost: Crit grants +4m movement per Hit. Charging: Spend 1 AP to fly base speed and execute a Melee Attack.</li>
                <li><strong>Surface Adhesion:</strong> 1 AP; Success Test using <strong>Mobility + Strength</strong>. Climb speed 8m plus 1m per SP.</li>
                <li><strong>Zipline (40m):</strong> 1 AP to launch cable; traverse as standard move.</li>
                <li><strong>Grapple (Xm):</strong> 1 AP; auto-pull to terrain. Hostiles: Complex Test using <strong>Mobility + Strength</strong>; Hits trigger Tether Pull (Push 1 space) or Tearing Damage.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">78</span>
        </div>
    </div>"""
    pages.append(p78)

    p79 = """    <!-- =========================================================================
         PAGE 79 (Spread 6 Right) — FORTIFICATION GEAR & EXPLOSIVES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortifications-explosives">
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
                            <td>Rapid ballistic barrier for ambushes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Med)</td>
                            <td>Medium Cover (+2), 24 HP, Innate Prot 8</td>
                            <td>3</td>
                            <td>8,000</td>
                            <td>Ceramic barricade with ground spikes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Hvy)</td>
                            <td>Heavy Cover (+3), 36 HP, Innate Prot 12</td>
                            <td>4</td>
                            <td>12,000</td>
                            <td>Alloy blast shield withstanding assault.</td>
                        </tr>
                        <tr>
                            <td class="bold">APS Beacon</td>
                            <td>Intercept 5, Reaction, 24 HP</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Automated Active Protection System.</td>
                        </tr>
                        <tr>
                            <td class="bold">Smartpod Remote Mount</td>
                            <td>Automount 3, 12 HP</td>
                            <td>3</td>
                            <td>36,000</td>
                            <td>Motorized turret for mounted ranged weapons.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 2mm;">
                <strong>Fortification Properties:</strong> Deploying barricades costs 1 AP. Barricades provide listed Protection and possess Cover HP and Innate Protection. Recover for 1 AP. &middot; <strong>Intercept (5):</strong> Deployed APS beacon gains 1 Free Reaction AP per round to contest incoming Ordnance (pure Intercept 5 roll; negates explosive if no 8+ remain). &middot; <strong>Automount (3):</strong> Operator or ally spends 1 AP to fire mounted weapon remotely using Automount 3 + Finesse.
            </p>

            <h3>3. Explosives &amp; Launchers</h3>
            <p>
                Explosives deliver high-yield area destruction. Combatants carry refillable <strong>Grenade Rigs</strong> allowing on-the-fly point-of-use munition selection.
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
                            <td>Bandolier holding 3 charges; choose at use.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Grenade Rig</td>
                            <td>Capacity 5, Refillable, Choice</td>
                            <td>3</td>
                            <td>10,000</td>
                            <td>Heavy combat rig holding 5 refillable charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Demolitions Rig</td>
                            <td>Capacity 2, Refillable, Choice</td>
                            <td>3</td>
                            <td>8,000</td>
                            <td>Breaching rig holding 2 heavy demo charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Siege Demolitions Rig</td>
                            <td>Capacity 4, Refillable, Choice</td>
                            <td>4</td>
                            <td>16,000</td>
                            <td>Military harness carrying 4 breaching charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Grenade Launcher Rig</td>
                            <td>Delivery (Medium Range)</td>
                            <td>2</td>
                            <td>6,000</td>
                            <td>Shoulder launcher firing to Medium Range.</td>
                        </tr>
                        <tr>
                            <td class="bold">Rocket Launcher Rig</td>
                            <td>Delivery (Long Range)</td>
                            <td>4</td>
                            <td>22,000</td>
                            <td>Tube-launched rocket system to Long Range.</td>
                        </tr>
                        <tr>
                            <td class="bold">Missile Guidance System</td>
                            <td>Delivery (Extreme Range)</td>
                            <td>6</td>
                            <td>60,000</td>
                            <td>Guided missile tube firing to Extreme Range.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Munition Profiles &amp; Explosives Properties</h4>
            <ul>
                <li><strong>Frag Munition:</strong> Ordnance 4, Blast 3, 8m Radius. Shrapnel anti-personnel bomb.</li>
                <li><strong>Flashbang Munition:</strong> Ordnance 5, Area Stun, 4m Radius. Blinds targets (discards highest die on next roll).</li>
                <li><strong>Smoke Canister:</strong> Area Obscurance, 8m Radius. Fills area with thermal smoke blocking sight without rolling.</li>
                <li><strong>HE Munition:</strong> Ordnance 5, Blast 5, 4m Radius. High-explosive concussion charge.</li>
                <li><strong>Remote Demolition:</strong> Ordnance 7, Blast 5, 12m Radius, Remote detonator (Heavy Rig only).</li>
                <li><strong>Ordnance (X) Area Attack:</strong> Thrown to Short Range (or launcher range). Pure Ordnance Success Test. <strong>Blast (X)</strong> adds +X damage per Hit spent on Crits.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">79</span>
        </div>
    </div>"""
    pages.append(p79)

    # =========================================================================
    # SPREAD 7 (Pages 80-81): MEDICAL, TECH KITS, SURVEILLANCE & UTILITY
    # =========================================================================

    p80 = """    <!-- =========================================================================
         PAGE 80 (Spread 7 Left) — MEDICAL RIGS, TRIAGE & COMBAT STIMULANTS
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
                            <td>Tissue welders and synthetic blood applicator.</td>
                        </tr>
                        <tr>
                            <td class="bold">Phoenix Reconstructor</td>
                            <td>Medicine 4, Cap 2, Greater Phys (1/1)</td>
                            <td>2</td>
                            <td>15,000</td>
                            <td>Stabilizes trauma and clears Aggravated damage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Stabilizer Inhaler</td>
                            <td>Medicine 3, Cap 3, Lesser Mental (1/2)</td>
                            <td>1</td>
                            <td>2,000</td>
                            <td>Pressurized mist dispenser countering panic.</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Stabilizer Rig</td>
                            <td>Medicine 4, Cap 4, Lesser Mental (1/1)</td>
                            <td>2</td>
                            <td>6,000</td>
                            <td>Auto-injector delivering potent restoratives.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Stim Injector</td>
                            <td>Capacity 3, Refillable, Choice</td>
                            <td>1</td>
                            <td>5,000</td>
                            <td>Auto-injector delivering 3 stimulant doses.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Chem-Rig</td>
                            <td>Capacity 5, Refillable, Choice</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>High-capacity harness carrying 5 doses.</td>
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
                <li><strong>Roid (Strength):</strong> <strong>+1 Strength.</strong> High-grade anabolic surge providing raw muscular leverage and kinetic force (Volatile 2, Fleeting).</li>
                <li><strong>Nitro (Agility):</strong> <strong>+1 Agility.</strong> Adrenaline booster accelerating muscle twitch response, sprint speed, and evasive bounds (Volatile 2, Fleeting).</li>
                <li><strong>Edgedance (Finesse):</strong> <strong>+1 Finesse.</strong> Fine-motor neural enhancer for micrometric hand-eye precision and weapon alignment (Volatile 2, Fleeting).</li>
                <li><strong>SharpX (Instinct):</strong> <strong>+1 Instinct.</strong> Sensory cortex stimulant accelerating peripheral awareness, reaction speed, and battlefield read (Volatile 2, Fleeting).</li>
                <li><strong>Cognita (Knowledge):</strong> <strong>+1 Knowledge.</strong> Nootropic neuro-accelerator boosting tactical calculation, memory access, and technical recall (Volatile 2, Fleeting).</li>
                <li><strong>Rizz (Presence):</strong> <strong>+1 Presence.</strong> Vocal and pheromonal enhancement cocktail projecting commanding authority and poise under duress (Volatile 2, Fleeting).</li>
                <li><strong>Volatile (X):</strong> When administered, user immediately suffers <strong>X unmitigated damage</strong>. Consuming a stimulant while already under Volatile effects causes additional damage equal to the total number of active Volatile substances in your system.</li>
                <li><strong>Fleeting:</strong> Stimulant surge lasts until end of current combat round, or end of Player Turn in day-to-day scenes.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">80</span>
        </div>
    </div>"""
    pages.append(p80)

    p81 = """    <!-- =========================================================================
         PAGE 81 (Spread 7 Right) — INFILTRATION, DETECTION & SURVIVAL
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
                            <td>Standard bypass picks, diagnostic drivers.</td>
                        </tr>
                        <tr>
                            <td class="bold">Engineer's Kit</td>
                            <td>Tinkering 4, Locksmith 4</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>Precision ultrasonic picks and bypass shunts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Maker's Kit</td>
                            <td>Tinkering 6, Locksmith 6</td>
                            <td>2</td>
                            <td>25,000</td>
                            <td>Mil-spec quantum decoders and plasma cutters.</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltrator Kit</td>
                            <td>Disguise 2, Forgery 2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Cosmetic prosthetics, seal replicators.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spy Kit</td>
                            <td>Disguise 4, Forgery 4</td>
                            <td>3</td>
                            <td>12,000</td>
                            <td>Holographic cloners and biometric stamp mimics.</td>
                        </tr>
                        <tr>
                            <td class="bold">Chameleon Kit</td>
                            <td>Disguise 6, Forgery 6</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Neural-adaptive latex mesh and identity fakers.</td>
                        </tr>
                        <tr>
                            <td class="bold">"Spider" Cyberdeck</td>
                            <td>Interfacing 3, Hacking 2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Portable deck with optical transceiver.</td>
                        </tr>
                        <tr>
                            <td class="bold">"Mantis" Cyberdeck</td>
                            <td>Interfacing 5, Hacking 4</td>
                            <td>3</td>
                            <td>12,000</td>
                            <td>Tactical deck with intrusion coprocessors.</td>
                        </tr>
                        <tr>
                            <td class="bold">"Scorpion" Cyberdeck</td>
                            <td>Interfacing 7, Hacking 6</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Black-market military deck built to shred ICE.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>Tech Properties (1 AP Costs)</h4>
            <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 2mm;">
                <strong>Tinkering (X):</strong> Traps, sabotage, repairs (Tinkering + Knowledge). &middot; <strong>Locksmith (X):</strong> Picking locks/latches (Locksmith + Finesse). &middot; <strong>Disguise (X):</strong> Creating physical personas (Disguise + Knowledge). &middot; <strong>Forgery (X):</strong> Security passes and manifests (Forgery + Finesse). &middot; <strong>Interfacing (X):</strong> Network nodes and commands (Interfacing + Knowledge). &middot; <strong>Hacking (X):</strong> Breaching firewalls, disabling ICE (Hacking + Knowledge).
            </p>

            <h3>6. Detection &amp; Surveillance Gear</h3>
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
                            <td>Ground-penetrating radar mapping motion and voids.</td>
                        </tr>
                        <tr>
                            <td class="bold">Recon Drone</td>
                            <td>Fly 20m, Sensors 2, Remote</td>
                            <td>2</td>
                            <td>35,000</td>
                            <td>Micro-quadcopter with optical night-vision sensors.</td>
                        </tr>
                        <tr>
                            <td class="bold">Forensic Sensor</td>
                            <td>Sensors 4, Chemical Scan</td>
                            <td>3</td>
                            <td>20,000</td>
                            <td>Handheld spectrometer for analyzing field evidence.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4>7. Survival &amp; Field Utility</h4>
            <div class="table-container keep-together" style="margin: 1.5mm 0 0 0;">
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
                            <td>Pressurized suit protecting against vacuum, toxins.</td>
                        </tr>
                        <tr>
                            <td class="bold">Field Rations (1 Wk)</td>
                            <td>Sustenance</td>
                            <td>1</td>
                            <td>50</td>
                            <td>Nutrient-dense self-heating meal packs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Wilderness Camp</td>
                            <td>Squad Shelter</td>
                            <td>4</td>
                            <td>500</td>
                            <td>Pressurized pop-up tent and water cycler for 4.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Commlink</td>
                            <td>Interfacing 2, Long-Range</td>
                            <td>0</td>
                            <td>1,000</td>
                            <td>Transceiver with encrypted frequency hopping.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">81</span>
        </div>
    </div>"""
    pages.append(p81)

    # =========================================================================
    # SPREAD 8 (Pages 82-83): EXOTIC HARDWARE RULES & 4-TIER RARITY LADDER
    # =========================================================================

    p82 = """    <!-- =========================================================================
         PAGE 82 (Spread 8 Left) — EXOTIC HARDWARE LORE & ALL 5 OPERATIONAL RULES
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
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 0;">
                <li><strong>Load Taxation Over Arbitrary Limits:</strong> There is no mystical "attunement" ceiling in <em>Corsair</em>. An operative is free to carry as many pieces of Exotic Hardware as their spine can endure. However, exotic hardware is dense, power-hungry, and heavily shielded. Weapons, power units, and field rigs carry substantial <strong>Load</strong> (typically Load 2 to 5), while exotic carapaces represent a massive encumbrance investment. Because every operative is bound by the absolute carrying capacity of <strong>12 + (Strength &times; 2)</strong>, packing multiple exotic systems forces agonizing compromises: you cannot wear a kinetic dissipation carapace, carry a dark-transducer carbine, and haul a seismic resonance rig without leaving your spare medical kits and sidearms back on the ship.</li>
                <li><strong>Action Point Economy:</strong> Activating an active exotic hardware function costs <strong>1 Action Point (AP)</strong>, or acts as an integrated enhancement to an existing 1-AP combat action. Passive defenses, sensory suites, and permanent material enhancements apply continuously, but active bursts always demand dedicated tactical focus.</li>
                <li><strong>Pacing Cooldowns &amp; Thermal Cycles:</strong> Bleeding-edge prototypes generate severe thermal spikes and power drains. Instead of abstract cooldown counters, exotic cooling cycles are measured directly in Corsair's narrative pacing rounds:
                    <ul>
                        <li><strong>Moment-to-Moment Cooldowns:</strong> Recover after <strong>1 moment-to-moment round</strong> (~5–10 seconds), resetting cleanly at the start of the operative's next combat turn.</li>
                        <li><strong>Place-to-Place Cooldowns:</strong> Recover after <strong>1 place-to-place round</strong> (~1 hour). The operative must complete their short transit or tactical breach, flush cryo-coolant loops, or vent residual capacitor heat into a starship heat sink before the system can fire again.</li>
                        <li><strong>Day-to-Day Cooldowns:</strong> Recover after <strong>1 day-to-day round</strong> (a full 24-hour downtime cycle), resetting after a proper shift of sleep, workshop calibration, and trickle-charging.</li>
                    </ul>
                </li>
                <li><strong>Irreplaceable Maintenance:</strong> When a piece of Exotic Hardware suffers structural damage and is reduced to 0 HP, it cannot be patched up with a generic soldering iron and a roll of thermal tape. Repairing a classified prototype requires an operative with a dedicated workshop and a successful <strong>Tinkering + Knowledge</strong> test against a Difficulty set by the item's Tier. Damaged Precursor relics cannot be repaired by mortal hands at all, unless the cell acquires rare molecular salvage or secures the favor of an Ancestral artisan or the scholar dragon Stormdrinker.</li>
                <li><strong>Non-Customizable Architecture (No Upgrade Kits):</strong> Exotic weapons, protective carapaces, and tactical hardware are precision-calibrated skunkworks trials or alien crystalline lattices whose tolerances operate at the atomic level. Because of this, <strong>Exotic Hardware cannot be customized or modified with standard Upgrade Kits</strong> (such as mastercrafted +1 Damage enhancements, Weight Reduction kits, or aftermarket weapon attachments). Attempting to drill, file, or bolt third-party components onto an exotic weapon short-circuits its induction coils, shatters non-baryonic barrel sleeves, or completely ruins its harmonic calibration. Their statistics, properties, and Load values are permanently fixed as written.</li>
            </ol>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">82</span>
        </div>
    </div>"""
    pages.append(p82)

    p83 = """    <!-- =========================================================================
         PAGE 83 (Spread 8 Right) — 4-TIER RARITY LADDER & CAMPAIGN INTEGRATION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-rarity-ladder">
        <div class="page-running-header">
            <span>Chapter 04: Exotic Hardware Ladder</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">The 4-Tier Rarity &amp; Economic Ladder</h3>
            <p>
                To prevent market confusion and establish clear campaign progression, Exotic Hardware is organized into four distinct tiers of rarity, cost, and availability:
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 2mm 0 3mm 0;">
                <div class="table-header">Exotic Hardware Rarity &amp; Acquisition Ladder</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.2mm; width: 10%;">Tier</th>
                            <th style="padding: 1.2mm 1.2mm; width: 22%;">Classification</th>
                            <th style="padding: 1.2mm 1.2mm; width: 22%;">Typical Cost (Credits)</th>
                            <th style="padding: 1.2mm 1.2mm; width: 46%;">Market Reality &amp; Acquisition</th>
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
            <p>
                When operatives secure an intact Precursor artifact, its energy signatures may inadvertently activate dormant defensive subroutines in nearby Vaults or draw the curiosity of Void entities. Owning priceless hardware carries operational consequences that ripple through an entire campaign arc.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">83</span>
        </div>
    </div>"""
    pages.append(p83)

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
    build_perfect_ch04()
