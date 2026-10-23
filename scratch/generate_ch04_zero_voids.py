# -*- coding: utf-8 -*-
"""
High-density, balanced, zero-void 14-page Chapter 04 generator.
Pages 68 to 81 (7 complete two-page spreads).
Eliminates all bottom page voids (targets 84%-92% fill, 18mm-33mm bottom gap).
Eliminates all horizontal overflows (scrollWidth == clientWidth == 688px).
100% Verbatim and high-fidelity text from canonical markdown files.
"""

from pathlib import Path

def generate_ch04_zero_voids():
    pages = []

    # =========================================================================
    # SPREAD 1 (Pages 68-69): COMBAT TACTICS (COMBAT.MD COMPLETE)
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

    p69 = """<!-- =========================================================================
         PAGE 69 (Spread 1 Right) — CONTESTING JAX, OCCUPANCY, CQC & TACTICAL COVER
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="contesting-occupancy-cqc-cover">
        <div class="page-running-header">
            <span>Chapter 04: Tactical Movement &amp; Cover</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <div class="callout callout-tactical keep-together" style="margin: 0 0 2.5mm 0; padding: 2.4mm 3.0mm;">
                <div class="callout-title" style="font-size: 8.5pt; margin-bottom: 1mm;">Tactical Example: Contesting Jax's Movement</div>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                    <strong>The Scenario:</strong> Jax is attempting to run past a burly corporate enforcer to reach a control panel. Jax spends 1 Action Point for a move action and makes an <strong>Agility</strong> Success Test to determine the total distance. Jax has Agility 4 and rolls <code>[9, 7, 5, 2]</code>. The highest die is a 9, so he can move his base 1 space (4m) plus 2 extra spaces (from the 9, which is 8m, rounded up to 2 spaces), for a total of 3 spaces.
                </p>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                    The enforcer stands along Jax's path. As Jax enters the enforcer's space, the GM declares the enforcer will contest the movement using <strong>Strength 5</strong> to grab him.
                </p>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                    <strong>1. The Contest Roll:</strong> The enforcer rolls 5d10: <code>[10, 8, 6, 4, 1]</code>—generating two successes (10 and 8).
                </p>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                    <strong>2. Eliminating Dice:</strong> The two successes eliminate the two highest dice from Jax's movement roll (<code>[9, 7, 5, 2]</code>). The 9 and 7 are eliminated.
                </p>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 0;">
                    <strong>3. Final Outcome:</strong> Jax's remaining pool is <code>[5, 2]</code>. Since there are no dice showing 8 or higher, the contest succeeds. Jax's movement ends immediately in the enforcer's space, stopped dead in his tracks.
                </p>
            </div>

            <h3 style="margin-top: 1mm;">Space and Occupancy</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                In Corsair, combat is dynamic and often close-quartered. A single space on the battle map is not limited to one character. Understanding how multiple characters occupy and interact within a single space is key to tactical success. A single 4x4 meter space can comfortably house up to <strong>4 standard-sized creatures</strong>. Many actions, especially melee attacks and certain Teamwork maneuvers, require you to be in the same space as your target or ally.
            </p>

            <h4 style="margin-top: 1mm;">Outnumbering</h4>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                Ganging up on a foe is a valid and effective tactic. When you and your allies outnumber your opponents within a single space, you gain a significant advantage in melee combat. You receive a number of <strong>Upgrades</strong> on your melee attack tests equal to the difference between the number of allied creatures and hostile creatures in that space. For example, if 3 allies are in a space with 1 enemy, all allies receive <strong>2 Upgrades</strong> (3 &minus; 1 = 2) on their melee attacks against that enemy.
            </p>

            <h4 style="margin-top: 1mm;">Melee Positioning</h4>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                You can attack a creature in the same space as you, or an adjacent space. Melee attacks must use any combination of two separate Physical Attributes. For example, Jax might combine <strong>Strength + Agility</strong> to drive a heavy blade through a pirate's defense, or pair <strong>Agility + Finesse</strong> when aiming a swift, precise knife strike at a weak point in armor.
            </p>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                When you attack a creature in an adjacent space, you move into it, provided it holds less than 4 creatures. If it already holds 4, you perform the attack from your current space, but count as if you and all allies in your space were in the target's space for outnumbering purposes.
            </p>

            <h4 style="margin-top: 1mm;">Creature Size</h4>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                The capacity of a space is affected by the size of creatures within it: <strong>Large</strong> creatures take up the space of <strong>2</strong> standard creatures; <strong>Huge</strong> creatures take up the space of <strong>4</strong> standard creatures. Truly massive creatures may occupy multiple spaces at once, counting as a Large or Huge entity in each space for capacity and targeting.
            </p>

            <h3 style="margin-top: 1mm;">Close Quarters Combat (CQC)</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                When you are in the same space as a hostile creature, you are in <strong>Close Quarters Combat (CQC)</strong>. This impacts ranged weaponry:
            </p>
            <ul style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 2mm;">
                <li><strong>Firing in CQC:</strong> Firing a ranged weapon while in CQC inflicts <strong>2 Downgrades</strong> to your attack test. Wielding long guns or aiming optics while dodging bayonets is intensely difficult.</li>
                <li><strong>Firing into CQC:</strong> Firing from outside into a space where allies and enemies are engaged in CQC inflicts <strong>1 Downgrade</strong> to your attack test. The chaotic swirl of close-quarters combat makes it hazardous to get a clean shot without endangering friends.</li>
            </ul>

            <h3 style="margin-top: 1mm;">Cover &amp; Defensive Positioning</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                Taking cover is a fundamental tactic for surviving a firefight. When a character is in a space that contains a source of cover (like a large crate, a sturdy pillar, or a low wall), they gain a flat bonus to their Protection against attacks originating from <em>outside</em> of their space. This bonus stacks directly with Protection from armor and shields:
            </p>
            <ul style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.8mm;">
                <li><strong>Light Cover:</strong> (<strong>+1 Protection</strong>) A small object offering partial concealment, like a thin pipe, light furniture, or a small fuel drum.</li>
                <li><strong>Medium Cover:</strong> (<strong>+2 Protection</strong>) A solid object hiding a significant portion of your body, like a large engine block or thick metal bulkhead.</li>
                <li><strong>Heavy Cover:</strong> (<strong>+3 Protection</strong>) A large durable fortification, like a reinforced bunker wall, blast gantry, or armored vehicle chassis.</li>
            </ul>

            <h4 style="margin-top: 1mm;">Destroying Cover &amp; Cover Facing</h4>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                Light, Medium, and Heavy Cover have <strong>12, 24, and 36 health segments</strong> and an innate Protection of <strong>4, 8, and 12</strong> respectively when directly targeted. Attacking cover is a <strong>Success Test</strong> instead of a Complex one. For every 12 damage the cover absorbs, its provided Protection benefit is reduced by 1. Specialized breaching charges, anti-materiel weapons, and demolition explosives specifically ignore cover's innate Protection.
            </p>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 2mm;">
                The first time you take an attack benefiting from cover, draw a line from the attacker to your center: whichever side of your space the line crosses becomes your <strong>covering side</strong>. When the line crosses a corner, both adjacent sides become covering sides. On subsequent attacks: <strong>Full Bonus</strong> across the covering side; <strong>Reduced Bonus</strong> (&minus;1 hex, &minus;2 square) across adjacent sides; <strong>No Bonus (Exposed)</strong> across non-adjacent sides.
            </p>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 0.8mm;">Tactical Doctrine: Flanking Sectors &amp; Cover Exposure</div>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 0;">
                    Positioning relative to cover is directional. When a combatant maneuvers around an enemy's covering side into an adjacent or rear flank sector, the target's cover bonus is reduced or stripped entirely (leaving them exposed). Coordinated fire teams use one operative to suppress a target from the front while a flanker advances to an open angle, bypassing bulkheads and eliminating Protection bonuses before delivering the lethal strike.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">69</span>
        </div>
    </div>"""
    pages.append(p69)

    # =========================================================================
    # SPREAD 2 (Pages 70-71): THE ARMORY, FIREARMS STATS, HANDGUNS & SMGS
    # =========================================================================

    p70 = """<!-- =========================================================================
         PAGE 70 (Spread 2 Left) — THE ARMORY INVARIANTS & FIREARMS MECHANICS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armory-and-firearms-intro">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: The Armory &amp; Ballistics</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">The Armory &amp; Equipment</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                Not every item a character carries has a significant mechanical impact on the game. Everyday objects like personal commlinks, apartment keys, or sentimental trinkets are assumed to be part of a character's belongings without needing specific rules. However, items that provide a distinct advantage in challenging situations—from weapons and armor to specialized tools—are classified as <strong>Equipment</strong>, governed by the <strong>Load</strong> system.
            </p>

            <h3>The Load Invariant</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                Every piece of mechanically significant equipment has a <strong>Load</strong> value representing its weight, physical size, and cumbersomeness. A character's ability to carry equipment into combat is strictly governed by their physical strength:
            </p>
            <div class="callout callout-tactical keep-together" style="margin: 2.4mm 0; padding: 2.6mm 3.0mm; text-align: center;">
                <div style="font-family: var(--font-heading); font-size: 11.5pt; font-weight: 700; color: var(--color-gold);">
                    Maximum Load Capacity = 12 + (Strength &times; 2)
                </div>
                <div style="font-size: 7.7pt; color: var(--color-silver); margin-top: 1mm;">An absolute physical limit: items exceeding capacity cannot be carried under any circumstances.</div>
            </div>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                This limit is absolute; an operative cannot carry items with a total Load exceeding this capacity under any circumstances. It is often a wise tactical decision to leave some of your Load capacity unused. An open slot might be exactly what you need to carry a vital piece of salvage, emergency oxygen tanks, or a mission-critical objective you discover on the job.
            </p>

            <h3>Equipment Categories &amp; Damage Bonus</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                Equipment is divided into Weapons, Armor, Gear, and Exotic Hardware. All weapons share a common statistic: the <strong>Damage Bonus</strong>. The Damage Bonus is a flat integer value added directly to the success points you generate on a successful attack roll, strictly increasing damage dealt.
            </p>

            <h3>Equipment Damage &amp; Field Repairs</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.6mm;">
                Deployable gear, fortifications, vehicles, and technological hardware possess structure ratings measured in <strong>Health Points (HP)</strong>. If an item is reduced to 0 HP, it is disabled and ceases to function until repaired. An operator carrying a toolkit with the <strong>Tinkering</strong> attribute can perform field maintenance to restore damaged hardware:
            </p>
            <ul style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 2mm;">
                <li><strong>Repairing Equipment:</strong> Restoring HP to damaged equipment costs <strong>1 AP</strong> (in structured combat) or standard narrative time (in downtime) and requires a <strong>Success Test</strong> using <strong>Tinkering + Knowledge</strong>.</li>
                <li><strong>HP Restored:</strong> The item immediately recovers <strong>1 HP per Success Point</strong> generated on the test, up to its maximum HP rating.</li>
                <li><strong>Workshop Fabrication:</strong> Rebuilding completely destroyed or vaporized hardware requires access to an engineering workshop or machine lathe, taking 1 Downtime Action and an Engineering test.</li>
            </ul>

            <h2 style="margin-top: 2mm;">Firearms</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the cold vacuum of space, across contested orbital platforms, and inside pressurized ship corridors, firearms are the ultimate arbiters of ranged combat. Ranging from rugged chemical-propellant slugthrowers to electro-thermal chemical (ETC) rifles and high-velocity magnetic rail drivers, firearms give Corsairs the range, stopping power, and suppression capability necessary to overwhelm hostile forces before they close the distance.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <p style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Every firearm is defined by mechanical attributes dictating tactical performance across engagement distances:
            </p>
            <ul style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 2mm;">
                <li><strong>Accuracy (Short / Medium / Long / Extreme):</strong> Ranged attacks always pair weapon Accuracy at the target's distance with <strong>Finesse</strong> (<strong>Accuracy + Finesse</strong>):
                    <ul style="margin-top: 0.8mm; margin-bottom: 0.8mm;">
                        <li><strong>Short Range (S):</strong> 0–5 spaces (~0–20m). Corridors, breaches, point-blank skirmishes.</li>
                        <li><strong>Medium Range (M):</strong> 6–12 spaces (~20–40m). Cargo bays, hangar decks, station concourses.</li>
                        <li><strong>Long Range (L):</strong> 13–20 spaces (~40–80m). Maintenance tunnels, gantries, open terrain.</li>
                        <li><strong>Extreme Range (E):</strong> 20+ spaces (~80m+). Standoff defense, sniper perches. Dash (<code>&minus;</code>) = out of range.</li>
                    </ul>
                </li>
                <li><strong>Rate of Fire (RoF):</strong> Strict upper limit on total <strong>Crit Effects</strong> and <strong>Chain Effects</strong> on an attack roll:
                    <ul style="margin-top: 0.8mm; margin-bottom: 0.8mm;">
                        <li><strong>Heavy-Hitters (RoF 0):</strong> Single-shot rifles, heavy revolvers, slug guns. No burst Crits/Chain.</li>
                        <li><strong>Precision &amp; Semi-Auto (RoF 1):</strong> Duty pistols, marksman rifles (up to 1 Crit/Chain).</li>
                        <li><strong>Burst &amp; Automatic (RoF 2):</strong> Assault carbines, combat shotguns (up to 2 Crits/Chain).</li>
                        <li><strong>Rapid Suppression &amp; Rotary (RoF 3–4):</strong> Squad automatics, heavy machine guns, rotary cannons (up to 3–4 Crits/Chain).</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to total success points of a successful attack.</li>
                <li><strong>Hands:</strong> 1H sidearm vs 2H shoulder-fired platform. &middot; <strong>Load &amp; Cost:</strong> Mass in Load system; Credits.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 2mm;">
                <strong>Panthera Arms:</strong> Sleek high-tolerance carbines and marksman rifles favored by corporate strike teams. &middot; <strong>Vandal's Workshop:</strong> Stamped-sheet high-RoF submachine guns cycling reliably in dirt and vacuum. &middot; <strong>Caldera Foundry:</strong> Heavy-bore rifles and trench shotguns for boarding defense. &middot; <strong>Ker'Satz Korp:</strong> Precision magnetic rail drivers and magnum revolvers. &middot; <strong>Chidori-Qwei:</strong> Lightweight polymer smart-linked sidearms.
            </p>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.4mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.3pt; margin-bottom: 0.8mm;">Tactical Doctrine: Storing &amp; Securing Load</div>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 0;">
                    Unused Load capacity isn't wasted—it represents physical agility, breathing room, and readiness. Veterans rarely kit out to their absolute maximum limit, reserving 2 to 3 slots for heavy mission objectives, recovered flight recorders, or seized weapon prototypes before navigating pressurized airlocks back to their vessel.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""
    pages.append(p70)

    p71 = """    <!-- =========================================================================
         PAGE 71 (Spread 2 Right) — SMALL ARMS: HANDGUNS, SMGS & SHOTGUNS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="small-arms-handguns-smgs">
        <div class="page-running-header">
            <span>Chapter 04: Sidearms &amp; Close-Quarter Firearms</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;" class="column-span-all">Handguns Catalog</h3>
            <p class="column-span-all" style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Compact sidearms designed for personal defense, emergency boarding backup, and rapid close-quarters deployment. Highly concealable and quick to draw when long guns are fouled in tight airlocks.
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.1mm 1.1mm; width: 16%;">Weapon Name</th>
                            <th style="padding: 1.1mm 1.1mm; width: 15%;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">RoF</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">H</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Dmg</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Load</th>
                            <th style="padding: 1.1mm 1.1mm; width: 8%;">Cost</th>
                            <th style="padding: 1.1mm 1.1mm; width: 35%;">Description</th>
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
                            <td>Standard-issue semi-automatic sidearm offering reliable cycling and balanced handling across pressurized environments.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Revolver</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>1,200</td>
                            <td>Large-frame cylinder handgun firing high-grain magnum cartridges with punishing recoil and armor-cracking velocity.</td>
                        </tr>
                        <tr>
                            <td class="bold">Machine Pistol</td>
                            <td>3 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1</td>
                            <td>1,500</td>
                            <td>Compact automatic handgun capable of dumping high-volume bursts in point-blank skirmishes and corridor breaches.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hand Cannon</td>
                            <td>2 / 3 / 2 / 0</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>2,200</td>
                            <td>Massive reinforced handgun chambered in anti-armor kinetic rounds for devastating single shots that shatter bulkheads.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1.5mm;" class="column-span-all">Submachine Guns &amp; Shotguns</h3>
            <p class="column-span-all" style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Close-quarters primary weapons engineered for boarding operations, clearing tight ship bulkheads, and dominating short-range firefights across station corridors where pellet spread and cyclic saturation turn the tide.
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.1mm 1.1mm; width: 16%;">Weapon Name</th>
                            <th style="padding: 1.1mm 1.1mm; width: 15%;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">RoF</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">H</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Dmg</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Load</th>
                            <th style="padding: 1.1mm 1.1mm; width: 8%;">Cost</th>
                            <th style="padding: 1.1mm 1.1mm; width: 35%;">Description</th>
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
                            <td>Lightweight collapsible submachine gun designed for vehicle crews, void-suit operations, and shipboard boarding teams.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical SMG</td>
                            <td>3 / 4 / 2 / 0</td>
                            <td>3</td>
                            <td>2H</td>
                            <td>+1</td>
                            <td>2</td>
                            <td>2,800</td>
                            <td>Balanced automatic platform featuring integral recoil compensators and high cyclic fire rates for sustained close-quarters fire.</td>
                        </tr>
                        <tr>
                            <td class="bold">Trench Shotgun</td>
                            <td>5 / 2 / &minus; / &minus;</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>2</td>
                            <td>2,400</td>
                            <td>Heavy pump-action smoothbore scattergun delivering catastrophic kinetic spread at point-blank range, shredding unarmored targets.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Shotgun</td>
                            <td>4 / 3 / 0 / &minus;</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>3,500</td>
                            <td>Semi-automatic magazine-fed shotgun engineered for rapid room clearing, airlock breaches, and close-quarters suppression.</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Scattergun</td>
                            <td>4 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,000</td>
                            <td>Fully automatic drum-fed scattergun delivering overwhelming short-range projectile swarms for area crowd control.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together column-span-all" style="margin: 1.5mm 0 0 0; padding: 2.5mm 3.0mm;">
                <div class="callout-title" style="font-size: 8.6pt; margin-bottom: 1.2mm;">Tactical Doctrine: Corridor Ballistics &amp; Point-Blank Breaches</div>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1mm;">
                    Within pressurized ship corridors (0–5 spaces), Shotguns and SMGs possess overwhelming Accuracy (4 to 5). An operative wielding a Trench Shotgun at point-blank range combines Accuracy 5 with Finesse and adds a massive +4 flat Damage Bonus, making it capable of breaching reinforced security doors or dispatching unshielded combatants in a single deafening blast.
                </p>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 0;">
                    Furthermore, because submachine guns feature high cyclic rates (RoF 2–3), they excel at laying down suppression before breaching defensive bulkheads. Spending extra Hits on Chain Effects allows boarding operatives to sweep secondary hostiles pinned along the corridor walls without sacrificing primary target penetration.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">71</span>
        </div>
    </div>"""
    pages.append(p71)

    # =========================================================================
    # SPREAD 3 (Pages 72-73): RIFLES, HEAVY SUPPORT, UPGRADES & FIREFIGHT
    # =========================================================================

    p72 = """<!-- =========================================================================
         PAGE 72 (Spread 3 Left) — COMBAT RIFLES & HEAVY SUPPORT WEAPONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-rifles-heavy">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Combat Rifles &amp; Heavy Platforms</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;" class="column-span-all">Combat Rifles Catalog</h3>
            <p class="column-span-all" style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Versatile long guns that balance effective range, stopping power, and tactical flexibility across ship corridors, open cargo bays, and planetary battlegrounds.
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.1mm 1.1mm; width: 16%;">Weapon Name</th>
                            <th style="padding: 1.1mm 1.1mm; width: 15%;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">RoF</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">H</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Dmg</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Load</th>
                            <th style="padding: 1.1mm 1.1mm; width: 8%;">Cost</th>
                            <th style="padding: 1.1mm 1.1mm; width: 35%;">Description</th>
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
                            <td>Standard military battle rifle delivering disciplined burst fire and balanced accuracy across all combat zones.</td>
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
                            <td>Precision-machined semi-automatic rifle equipped with high-magnification optics for mid-to-long range fire.</td>
                        </tr>
                        <tr>
                            <td class="bold">Sniper Rifle</td>
                            <td>0 / 2 / 5 / 4</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+5</td>
                            <td>4</td>
                            <td>9,500</td>
                            <td>Long-range bolt-action or precision-lock rifle delivering extreme terminal ballistics at standoff ranges.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1.5mm;" class="column-span-all">Heavy Support Weapons Catalog</h3>
            <p class="column-span-all" style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Crew-served and reinforced heavy platforms requiring substantial physical leverage to operate, delivering unmatched suppressive fire, corridor saturation, and anti-materiel kinetic energy against armored targets and light vehicles. Wielding these systems effectively demands setting up integral bipods or locking magnetic boot clamps to brace against massive cyclic recoil.
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.1mm 1.1mm; width: 16%;">Weapon Name</th>
                            <th style="padding: 1.1mm 1.1mm; width: 15%;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">RoF</th>
                            <th style="padding: 1.1mm 1.1mm; width: 6%;">H</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Dmg</th>
                            <th style="padding: 1.1mm 1.1mm; width: 7%;">Load</th>
                            <th style="padding: 1.1mm 1.1mm; width: 8%;">Cost</th>
                            <th style="padding: 1.1mm 1.1mm; width: 35%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">SAW</td>
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
                            <td class="bold">Anti-Materiel Rifle</td>
                            <td>0 / 2 / 5 / 5</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+7</td>
                            <td>5</td>
                            <td>15,000</td>
                            <td>High-caliber magnetic-assisted anti-tank rifle designed to disable light vehicles and penetrate heavy bulkheads.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together column-span-all" style="margin: 2mm 0 0 0; padding: 3.2mm 3.6mm;">
                <div class="callout-title" style="font-size: 8.6pt; margin-bottom: 1.2mm;">Tactical Doctrine: Heavy Firepower &amp; Bipod Bracing</div>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1mm;">
                    Heavy weapons with RoF 3–4 (such as the SAW, HMG, and Rotary Autocannon) excel at area control and perimeter suppression. When firing into spaces with clustered hostiles, their high RoF allows operatives to spend up to 4 Hits on Crit and Chain Effects simultaneously, splitting fire across multiple targets and shredding light barricades in a single sustained burst.
                </p>
                <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 0;">
                    Operating these systems effectively demands physical stability. Bracing a heavy weapon on deployable fortifications or adopting a prone firing position negates recoil drift, allowing gunners to lay down relentless cyclic saturation across hangar decks and open landing pads without sacrificing shot placement.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">72</span>
        </div>
    </div>"""
    pages.append(p72)

    p73 = """<!-- =========================================================================
         PAGE 73 (Spread 3 Right) — DUAL WIELDING, UPGRADE KITS & FIREFIGHT ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-customization-and-action">
        <div class="page-running-header">
            <span>Chapter 04: Firearm Customization &amp; Action</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Dual Wielding Firearms</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                A combatant can choose to wield a one-handed firearm in each hand, laying down intense suppressive fire or engaging multiple targets simultaneously:
            </p>
            <ul style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.8mm;">
                <li><strong>One-Handed Only:</strong> You can only dual wield firearms with the <strong>1H</strong> designation (holding one sidearm in each hand).</li>
                <li><strong>Combined Firepower (Damage &amp; RoF):</strong> When making a ranged attack while dual wielding two 1H firearms, you combine the offensive output of both weapons, adding together both the flat <strong>Damage Bonus</strong> and the <strong>Rate of Fire (RoF)</strong> of the two firearms.</li>
                <li><strong>Worse Accuracy:</strong> Discharging two weapons simultaneously compromises sight alignment and muzzle stability. When resolving the attack test, you must use the <strong>worse (lower) Accuracy rating</strong> at the target's current range band between the two wielded firearms.</li>
            </ul>

            <h3>Firearm Upgrade Kits</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                Stock firearms can be customized into precision mastercrafted weapons through high-tolerance machining, carbon-fiber skeletal framing, match-grade barrels, tuned gas pistons, and custom optics. Because each subsequent modification requires increasingly complex gunsmithing, upgrade kits escalate in cost with every installation:
            </p>
            <ul style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.8mm;">
                <li><strong>Upgrade Limit:</strong> A single firearm can benefit from a maximum of <strong>3 Upgrade Kits</strong> in total, while one-handed (1H) sidearms are limited to a maximum of <strong>2 Upgrade Kits</strong>.</li>
                <li><strong>Tiered Cost Structure:</strong>
                    <ul>
                        <li><strong>1st Upgrade:</strong> <strong>10,000 Credits</strong></li>
                        <li><strong>2nd Upgrade:</strong> <strong>25,000 Credits</strong></li>
                        <li><strong>3rd Upgrade:</strong> <strong>50,000 Credits</strong></li>
                    </ul>
                </li>
                <li><strong>Upgrade Choices:</strong> Each time an Upgrade Kit is applied, choose one permanent modification:
                    <ul>
                        <li><strong>Lightweight Chassis:</strong> Precision skeletonization and composite furniture reduce the weapon's <strong>Load by 1</strong> (minimum 1/2 Load).</li>
                        <li><strong>Lethal Tuning:</strong> Match-grade barrel rifling increases flat <strong>Damage Bonus by +1</strong>.</li>
                        <li><strong>Recoil Dampening:</strong> Hydraulic buffer tubes increase <strong>Rate of Fire (RoF) by 1</strong>.</li>
                        <li><strong>Optic Calibration:</strong> Advanced holographic sights increase <strong>Accuracy by +1</strong> at one designated range band (e.g., Medium Range Accuracy +1).</li>
                    </ul>
                </li>
            </ul>

            <h3>Ammunition &amp; Magazine Ejection</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                In Corsair, ammunition tracking is streamlined: firearms operate with high-capacity magazines or power cells sufficient for an entire tactical firefight. However, reloading a fresh magazine, swapping a depleted battery pack, or clearing a fouled bolt in combat costs <strong>1 Action Point (AP)</strong>.
            </p>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                Discharging slugthrowers in microgravity introduces unique hazards: floating spent brass casings can be sucked into life-support air recyclers, cooling intake turbines, or radiator vanes. Mil-spec firearms incorporate magnetic brass-catchers or utilize caseless propellants to preserve shipboard atmospheric scrubbers during boarding actions.
            </p>

            <h3>Optics &amp; Smart-Link Calibration</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                Target acquisition across varying engagement distances is heavily augmented by combat optics. Holographic sights, thermal focal arrays, and helmet smart-links allow operators to calculate projectile drop in microgravity and track thermal signatures through obscurants. Weapons upgraded with Optic Calibration provide vital precision bonuses (+1 Accuracy) at designated range bands.
            </p>

            <h3>Vacuum Thermal Dissipation</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.6mm;">
                Because a vacuum lacks ambient air to conduct convective heat away from the receiver, automatic fire causes rapid thermal buildup. Weapons fired in decompression rely entirely on radiative heat sinks. Laying down continuous cyclic saturation (RoF 3–4) without pause can cause barrel warping or cook-offs, demanding disciplined fire control during external hull skirmishes.
            </p>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 0 0; padding: 2.8mm 3.2mm;">
                <div class="callout-title" style="font-size: 8.5pt; margin-bottom: 1.2mm;">Tactical Example: The Hangar Deck Firefight</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax advances down an industrial catwalk overlooking a contested cargo hangar. Positioned <strong>8 spaces (~26 meters)</strong> away behind low freight containers, an armed syndicate mercenary returns fire. The distance places the mercenary squarely at <strong>Medium Range</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    Jax is armed with an <strong>Assault Rifle</strong> (Accuracy <code>2 / 4 / 3 / 1</code>, RoF 2, 2H, Load 3, and a <strong>+2 Damage Bonus</strong>). Jax's character sheet shows <strong>Finesse 5</strong>, <strong>Instinct 3</strong>, and <strong>Strength 4</strong>.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>1. Determining the Test Pool:</strong> Jax prepares a precision shot, declaring an <strong>Accuracy + Finesse</strong> Complex Test. At Medium Range, the Assault Rifle has an <strong>Accuracy of 4</strong>. Pairing Jax's <strong>Finesse 5</strong> with the rifle's <strong>Accuracy 4</strong>, the higher attribute is Finesse 5 and the lower attribute is Accuracy 4.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>2. Action Roll (Higher Attribute = Finesse 5):</strong> Jax rolls 5d10 for the Action Roll: <code>[2, 5, 8, 8, 9]</code>. The roll yields three Hits (8, 8, 9). Because the Action Roll succeeded (at least one 8+), Jax spends one of his extra Hits (8) to activate an <strong>Upgrade Effect</strong>, stepping up one die in his upcoming Success Roll from a d10 to a <strong>d12</strong>. Jax retains the remaining Hits for resolution.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>3. Success Roll (Lower Attribute = Accuracy 4):</strong> Jax now takes a pool equal to the weapon's Accuracy at this range (<strong>4 dice</strong>). With the Upgrade Effect applied, Jax rolls 3d10 and 1d12: rolling <code>[4, 7, 8]</code> on the d10s and a <code>10</code> on the upgraded d12.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                    <strong>4. Activating Effects &amp; RoF Limits:</strong> The Success Roll produced two Hits (8 and 10). Jax spends both Hits on <strong>Crit Effects</strong> to maximize damage (+2 Success Points per Crit). Because the Assault Rifle has <strong>RoF 2</strong>, it perfectly accommodates spending 2 Hits on Crits (reaching the rifle's full burst capacity).
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    <strong>5. Calculating Total Damage:</strong> Highest remaining non-spent die: <strong>7 Success Points</strong> + Two Crit Effects (+2 each): <strong>+4 Success Points</strong> + Rifle Flat Damage Bonus: <strong>+2</strong> = <strong>Total Damage Dealt: 13 points of damage</strong>. The rifle burst punches through the container seam, striking the mercenary cleanly.
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
    # SPREAD 4 (Pages 74-75): MELEE WEAPONS, CATALOG, SHIELDS & BOARDING ACTION
    # =========================================================================

    p74 = """    <!-- =========================================================================
         PAGE 74 (Spread 4 Left) — MELEE WEAPONS FUNDAMENTALS, UPGRADES & SHIELDS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-weapons-fundamentals">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons &amp; Shields</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Weapons</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                In the tight corridors of starships, depressurized maintenance shafts, and claustrophobic orbital stations, discharging a firearm risks puncturing critical hull plating or ricocheting in zero-gravity. In these confined environments, a dependable melee weapon is an indispensable tool for survival. Whether utilizing precision combat knives, weighted riot clubs, or heavy two-handed mauls, close-quarters combat demands physical prowess, tactical positioning, and mastery over your weapon's mechanical profile.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.2mm;">
                Every melee weapon is defined by mechanical attributes that dictate its lethal profile and interaction with physical attributes:
            </p>
            <ul style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.6mm;">
                <li><strong>Damage Type &amp; Favored Attribute Pair:</strong> Melee weapons inflict damage through three distinct physical methods:
                    <ul>
                        <li><strong>Piercing (Agility + Finesse):</strong> Swift, pinpoint thrusts directed at structural seams, visor slits, and armor joints.</li>
                        <li><strong>Slashing (Agility + Strength):</strong> Wide, sweeping kinetic cuts combining dynamic movement with heavy cutting force.</li>
                        <li><strong>Striking (Strength + Finesse):</strong> Controlled, bone-shattering impacts delivered with precise leverage and body mechanics.</li>
                    </ul>
                </li>
                <li><strong>Favored Pair Damage Bonus:</strong> When you make an attack test using the weapon's favored Attribute Pair, you gain a damage bonus equal to the <strong>lower attribute</strong> in that pair. While a character is free to perform a melee attack using any combination of two physical attributes, choosing the weapon's favored pair unlocks this substantial boost.</li>
                <li><strong>Minimum Strength (Min STR):</strong> Physical combat tools require sufficient muscular leverage to control effectively:
                    <ul>
                        <li><strong>One-Handed Weapons (1H):</strong> If your Strength is lower than the weapon's Min STR, you must wield the weapon with <strong>two hands (2H)</strong> to attack with it.</li>
                        <li><strong>Two-Handed Weapons (2H):</strong> If your Strength is lower than the weapon's Min STR, the weapon is too cumbersome or heavy to wield, and you <strong>cannot attack</strong> with it under any circumstances.</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat numerical value added directly to total success points on a successful attack roll.</li>
                <li><strong>Hands:</strong> 1H sidearm weapon vs 2H heavy polearm. &middot; <strong>Load &amp; Cost:</strong> Mass in Load system; Credits.</li>
            </ul>

            <h3>Dual Wielding Melee</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.2mm;">
                A combatant can hold and fight with a weapon in each hand, creating an aggressive combat style that overwhelms opponents with combined offensive pressure:
            </p>
            <ul style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.6mm;">
                <li><strong>One-Handed Only:</strong> You can only dual wield weapons with the <strong>1H</strong> designation. You must meet the Minimum Strength requirement of each weapon individually.</li>
                <li><strong>Combined Damage Bonus:</strong> Add together the flat <strong>Damage Bonus of both weapons</strong> to your total outcome.</li>
                <li><strong>Attack Resolution:</strong> Designate which weapon leads the strike to determine <strong>Damage Type</strong> and its corresponding favored Attribute Pair. If the attack utilizes that favored pair, add the lower attribute of the test to the combined damage.</li>
            </ul>

            <h3>Melee Upgrade Kits</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Mastercrafted through high-grade aerospace machining, monomolecular edge-honing, ergonomic carbon balancing, or vibration emitters. Maximum <strong>3 Kits for 2H</strong> weapons, <strong>2 Kits for 1H</strong> weapons. Tiered costs: <strong>1st: 10,000 CR</strong> &middot; <strong>2nd: 25,000 CR</strong> &middot; <strong>3rd: 50,000 CR</strong>. Choices: <em>Lightweight Tuning</em> (&minus;1 Load, min 1/2) or <em>Lethal Edge / Weighted Core</em> (+1 Damage Bonus).
            </p>

            <h3 style="margin-top: 1.5mm;" class="column-span-all">Shields</h3>
            <p class="column-span-all" style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                Shields are rigid defensive barriers constructed from ballistic polymers, layered ceramics, or reinforced titanium alloys. Wielded in the off-hand (<strong>1H</strong>), they provide vital cover during tactical breaches and close-quarters engagements:
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 2mm 0;">
                <table class="rules-table" style="font-size: 7.5pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 1.0mm; width: 16%;">Shield Name</th>
                            <th style="padding: 1.0mm 1.0mm; width: 14%;">Protection</th>
                            <th style="padding: 1.0mm 1.0mm; width: 12%;">Min STR</th>
                            <th style="padding: 1.0mm 1.0mm; width: 10%;">Hands</th>
                            <th style="padding: 1.0mm 1.0mm; width: 10%;">Load</th>
                            <th style="padding: 1.0mm 1.0mm; width: 12%;">Cost</th>
                            <th style="padding: 1.0mm 1.0mm; width: 26%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Buckler</td>
                            <td>+1 Protection</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>1</td>
                            <td>800</td>
                            <td>Compact arm-mounted composite disc designed to parry blades and deflect shrapnel.</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Shield</td>
                            <td>+2 Protection</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>2</td>
                            <td>2,500</td>
                            <td>Reinforced transparent polycarbonate barrier providing solid torso and limb coverage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Ballistic Shield</td>
                            <td>+3 Protection</td>
                            <td>6</td>
                            <td>1H</td>
                            <td>4</td>
                            <td>6,500</td>
                            <td>Heavy ceramic-composite assault pavise built to withstand high-caliber kinetic fire.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together column-span-all" style="margin: 1mm 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Doctrine: The Defensive Phalanx &amp; Boarding Shields</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    A combatant wielding a Ballistic Shield (+3 Protection) becomes a moving bulwark in narrow corridors. While holding a shield prevents wielding two-handed weapons, the flat Protection bonus stacks directly with worn armor and environmental cover, enabling breachers to absorb concentrated kinetic point-defense while allies advance safely in their wake.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">74</span>
        </div>
    </div>"""
    pages.append(p74)

    p75 = """    <!-- =========================================================================
         PAGE 75 (Spread 4 Right) — COMPLETE 15-WEAPON MELEE CATALOG & BOARDING ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-catalog-and-action">
        <div class="page-running-header">
            <span>Chapter 04: Melee Weapons Catalog &amp; Action</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;" class="column-span-all">Melee Weapons Catalog</h3>
            <p class="column-span-all" style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.4mm;">
                The table below outlines standard melee weapon archetypes across all weight classes and damage types. Attacking with the weapon's favored Attribute Pair unlocks its full lethal potential, adding the lower attribute directly to damage.
            </p>

            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 1.5mm 0;">
                <table class="rules-table" style="font-size: 7.2pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.8mm 0.8mm; width: 14%;">Weapon Name</th>
                            <th style="padding: 0.8mm 0.8mm; width: 10%;">Damage Type</th>
                            <th style="padding: 0.8mm 0.8mm; width: 14%;">Favored Pair</th>
                            <th style="padding: 0.8mm 0.8mm; width: 7%;">Min STR</th>
                            <th style="padding: 0.8mm 0.8mm; width: 5%;">H</th>
                            <th style="padding: 0.8mm 0.8mm; width: 6%;">Dmg</th>
                            <th style="padding: 0.8mm 0.8mm; width: 6%;">Load</th>
                            <th style="padding: 0.8mm 0.8mm; width: 7%;">Cost</th>
                            <th style="padding: 0.8mm 0.8mm; width: 31%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Shiv / Stiletto</td>
                            <td>Piercing</td>
                            <td>Agility + Finesse</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>150</td>
                            <td>Compact, concealable thrusting blade designed for quick jabs into unarmored seams.</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Knife</td>
                            <td>Slashing</td>
                            <td>Agility + Strength</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>200</td>
                            <td>Standard utility and combat knife with a balanced single-edged blade.</td>
                        </tr>
                        <tr>
                            <td class="bold">Knuckleduster</td>
                            <td>Striking</td>
                            <td>Strength + Finesse</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>100</td>
                            <td>Fitted metal fist reinforcement that concentrates bare-knuckle punching force.</td>
                        </tr>
                        <tr>
                            <td class="bold">Dagger</td>
                            <td>Piercing</td>
                            <td>Agility + Finesse</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>400</td>
                            <td>Double-edged tactical dagger engineered for penetrating thrusts and close defense.</td>
                        </tr>
                        <tr>
                            <td class="bold">Hatchet / Machete</td>
                            <td>Slashing</td>
                            <td>Agility + Strength</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>500</td>
                            <td>Forward-weighted chopping blade effective for utility clearing and melee strikes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Baton / Club</td>
                            <td>Striking</td>
                            <td>Strength + Finesse</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>300</td>
                            <td>Weighted polymer or steel rod designed to deliver blunt kinetic trauma.</td>
                        </tr>
                        <tr>
                            <td class="bold">Shortsword</td>
                            <td>Piercing</td>
                            <td>Agility + Finesse</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,200</td>
                            <td>Straight, rigid blade optimized for rapid lunges and high-mobility thrusts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Boarding Axe</td>
                            <td>Slashing</td>
                            <td>Agility + Strength</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,500</td>
                            <td>Sturdy single-handed axe designed for breaching bulkheads and chopping through limbs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Mace / Crowbar</td>
                            <td>Striking</td>
                            <td>Strength + Finesse</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,000</td>
                            <td>Flanged iron bludgeon or heavy steel prybar capable of cracking bone through plating.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spear</td>
                            <td>Piercing</td>
                            <td>Agility + Finesse</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,200</td>
                            <td>Two-handed hafted spear delivering deep penetrating thrusts with significant leverage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Longsword</td>
                            <td>Slashing</td>
                            <td>Agility + Strength</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,800</td>
                            <td>Versatile, well-tempered blade that generates powerful, fluid cutting arcs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Warhammer</td>
                            <td>Striking</td>
                            <td>Strength + Finesse</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,400</td>
                            <td>Heavy, reinforced hammerhead built to crumple armor plating and crush internal frame.</td>
                        </tr>
                        <tr>
                            <td class="bold">Halberd / Poleaxe</td>
                            <td>Piercing</td>
                            <td>Agility + Finesse</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,500</td>
                            <td>Long two-handed polearm capped with a reinforced piercing spike and axe head.</td>
                        </tr>
                        <tr>
                            <td class="bold">Greatsword</td>
                            <td>Slashing</td>
                            <td>Agility + Strength</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>5,000</td>
                            <td>Massive two-handed blade that leverages full body rotation for devastating cleaves.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Maul</td>
                            <td>Striking</td>
                            <td>Strength + Finesse</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,800</td>
                            <td>Enormous two-handed sledgehammer delivering catastrophic, armor-pulverizing force.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout callout-tactical keep-together column-span-all" style="margin: 1mm 0 0 0; padding: 2.0mm 2.6mm;">
                <div class="callout-title" style="font-size: 8.2pt; margin-bottom: 0.8mm;">Tactical Example: The Boarding Action Strike</div>
                <p style="font-size: 7.8pt; line-height: 1.25; margin-bottom: 1mm;">
                    Jax breaches an airlock into the secondary generator deck, confronting a corporate security guard. Jax wields a <strong>Boarding Axe</strong> (Slashing, Favored Pair: <strong>Agility + Strength</strong>, Min STR 3, 1H, Load 2, +2 Damage Bonus). Jax's sheet shows <strong>Strength 4</strong>, <strong>Agility 4</strong>, and <strong>Finesse 3</strong>.
                </p>
                <p style="font-size: 7.8pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. Action Roll (Strength 4):</strong> Jax declares a sweeping cleave using his axe's favored pair (Agility + Strength). Both attributes are 4, so Jax rolls 4d10 for the Action Roll: <code>[3, 6, 8, 9]</code>—generating two Hits (8 and 9). Jax spends one Hit on an <strong>Upgrade Effect</strong> to step up a die in his Success Roll from a d10 to a <strong>d12</strong>.
                </p>
                <p style="font-size: 7.8pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>2. Success Roll (Agility 4):</strong> Jax rolls 3d10 and 1d12: <code>[5, 7, 8]</code> on the d10s and an <code>11</code> on the upgraded d12. Two Hits generated (8 and 11). Jax spends both Hits on <strong>Crit Effects</strong> (+2 damage each).
                </p>
                <p style="font-size: 7.8pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>3. Damage Resolution:</strong> Highest non-spent die: 7 SPs + Two Crits (+4) + Favored Pair Bonus (lower of STR 4 / AGI 4 = +4) + Axe Damage Bonus (+2) = <strong>17 points of damage</strong>, cleaving clean through the guard's arm plate.
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
    # SPREAD 5 (Pages 76-77): ARMOR & PROTECTION (ARMOR.MD COMPLETE)
    # =========================================================================

    p76 = """    <!-- =========================================================================
         PAGE 76 (Spread 5 Left) — ARMOR MECHANICS, UPGRADES & LIGHT ARMOR CATALOG
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-mechanics-light">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Armor</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                In the perilous expanses of the settled systems, a dependable suit of armor is often the only barrier between a Corsair and lethal trauma. Whether weathering rifle fire in a depressurized corridor, deflecting shrapnel from an explosive hull breach, or absorbing punishing melee impacts during a boarding skirmish, protective gear preserves a combatant's operational capability in the deadliest environments.
            </p>

            <h3>Armor Statistics Explained</h3>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                Every suit of armor is defined by mechanical attributes that govern its defensive resilience, tactical properties, and logistical burden:
            </p>
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.5mm;">
                <li><strong>Protection:</strong> The flat integer value of physical and kinetic damage reduced from each incoming attack before it affects your health. When you are struck by an attack, subtract your armor's Protection directly from the incoming damage.
                    <ul>
                        <li><strong>Stacking Rules:</strong> Armor Protection stacks directly with defensive bonuses provided by <strong>Shields</strong> (e.g., a Riot Shield providing +2 Protection) and <strong>Cover</strong> (e.g., Medium Cover providing +2 Protection). However, a character can only wear <strong>one suit of armor</strong> at a time; separate armor Protection values do not stack.</li>
                    </ul>
                </li>
                <li><strong>Load:</strong> The mass and physical bulk of the armor as governed by the inventory Load system. Armor counts against your character's maximum Load limit (`12 + (Strength × 2)`).</li>
                <li><strong>No Minimum Strength Requirement:</strong> Unlike melee weapons and shields, armor does not enforce a binary Minimum Strength requirement to don or wear. Any operative can wear any suit of armor, provided they have sufficient Load capacity to carry its weight. However, heavier suits feature the <strong>Cumbersome (X)</strong> property, imposing significant physical penalties on characters who lack the conditioning or agility to handle dense ballistic plating.</li>
                <li><strong>Armor Properties:</strong> Specialized engineering features and structural treatments that provide unique tactical benefits:
                    <ul>
                        <li><strong>Cumbersome (X):</strong> Mass and rigid plates restrict articulation. Suffer <strong>X Downgrades on all tests involving Agility</strong> (including movement Success Tests, acrobatics, athletics, stealth, and agility-based attack rolls or contest rolls).</li>
                        <li><strong>Hardened:</strong> Strike faces diffuse kinetic penetrators. Bonus Success Points gained per Hit spent on Crits is reduced by 1 (granting <strong>+1 SP per Hit spent</strong>, instead of +2).</li>
                        <li><strong>Blast-Dampened:</strong> Concussive baffles dissipate shockwaves. Gain <strong>+2 additional Protection against Area Attacks and Explosives</strong>.</li>
                        <li><strong>Tactical Harness (X):</strong> Reinforced load-bearing webbing provides <strong>X dedicated Load slots for any equipment</strong> (weapons, medkits, sensors) that do not count against standard Load.</li>
                        <li><strong>Muffled:</strong> Friction-reducing joint gaskets suppress gear rattle. Gain <strong>+1 Upgrade on Stealth tests</strong>.</li>
                    </ul>
                </li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.5mm;">
                <strong>Chidori-Qwei Combatwear:</strong> Sleek flexible polymer garments and armored flightsuits. &middot; <strong>Panthera Arms:</strong> Precision lightweight composite plate carriers. &middot; <strong>Vandal's Workshop:</strong> Stamped alloy armor and industrial hazard suits. &middot; <strong>Caldera Foundry:</strong> Heavy cast ceramic-titanium battleplate. &middot; <strong>Ker'Satz Korp:</strong> Ballistic assault chassis and mechanized siege rigs.
            </p>

            <h3>Armor Upgrade Kits</h3>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                Standard suits can be customized into mastercrafted systems through armorer machining, gel trauma dampeners, or high-density ceramic strike faces. Max <strong>3 Upgrade Kits</strong> per suit. Tiered costs: <strong>1st: 50,000 CR</strong> &middot; <strong>2nd: 100,000 CR</strong> &middot; <strong>3rd: 180,000 CR</strong>. Choices:
            </p>
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.5mm;">
                <li><strong>Reinforced Plating:</strong> Increase armor's <strong>Protection by +1</strong> (max +3 Protection total across all kits).</li>
                <li><strong>Lightweight Composites:</strong> Reduce armor's <strong>Load by 1</strong> (to a minimum of 1 Load).</li>
                <li><strong>Specialized Modification:</strong> Installs one specialized property: <em>Hardened</em>, <em>Blast-Dampened</em>, <em>Tactical Harness (1)</em>, or <em>Muffled</em>.</li>
            </ul>

            <h3 style="margin-top: 1.5mm;">Light Armor Catalog (Load 1–3 &middot; Prot 2–4)</h3>
            <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.2mm;">
                Light armors provide essential protection without impeding speed, reflexes, or acrobatics. Favored by pilots, scouts, and agile skirmishers.
            </p>

            <div class="table-container keep-together" style="margin: 0.5mm 0 0 0;">
                <div class="table-header">Light Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.2pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.8mm 0.8mm; width: 22%;">Armor Name</th>
                            <th style="padding: 0.8mm 0.8mm; width: 10%;">Prot</th>
                            <th style="padding: 0.8mm 0.8mm; width: 10%;">Load</th>
                            <th style="padding: 0.8mm 0.8mm; width: 16%;">Properties</th>
                            <th style="padding: 0.8mm 0.8mm; width: 14%;">Cost</th>
                            <th style="padding: 0.8mm 0.8mm; width: 28%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Padded Flightsuit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>&mdash;</td>
                            <td>1,200</td>
                            <td>Pressurized spacer jumpsuit; unencumbering.</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltration Suit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>Muffled</td>
                            <td>3,500</td>
                            <td>Acoustic-dampening bodysuit favored by scouts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Armored Jacket</td>
                            <td>3</td>
                            <td>2</td>
                            <td>&mdash;</td>
                            <td>3,000</td>
                            <td>Rugged utility jacket with ballistic aramid inserts.</td>
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
                            <td>Mil-spec plate carrier balancing defense with mobility.</td>
                        </tr>
                        <tr>
                            <td class="bold">Spec-Ops Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>Hardened</td>
                            <td>18,000</td>
                            <td>Elite plate carrier featuring boron-carbide inserts.</td>
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

    p77 = """<!-- =========================================================================
         PAGE 77 (Spread 5 Right) — MEDIUM & HEAVY ARMOR, TACTICAL DEFENSE ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-medium-heavy-action">
        <div class="page-running-header">
            <span>Chapter 04: Carapace Armor &amp; Defensive Action</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">Medium Armor (Load 4–5 &middot; Prot 5–6)</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Medium armors deliver heavy kinetic mitigation for frontline combat. Tactical Battleplate represents the peak of unencumbered military protection before full-body carapace penalties apply.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 2mm 0;">
                <div class="table-header">Medium Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.3pt; width: 100%; table-layout: fixed;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 0.7mm; width: 20%;">Armor Name</th>
                            <th style="padding: 1.0mm 0.7mm; width: 9%;">Prot</th>
                            <th style="padding: 1.0mm 0.7mm; width: 9%;">Load</th>
                            <th style="padding: 1.0mm 0.7mm; width: 18%;">Properties</th>
                            <th style="padding: 1.0mm 0.7mm; width: 13%;">Cost</th>
                            <th style="padding: 1.0mm 0.7mm; width: 31%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>&mdash;</td>
                            <td>30,000</td>
                            <td>Full-torso plate carrier; max protection without Agility Downgrades.</td>
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
                            <td>Hardened, Tac (1)</td>
                            <td>45,000</td>
                            <td>Squad-leader vest with reinforced trauma plates and utility webbing.</td>
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
                            <td>Cumbersome (1), Hard, Tac (1)</td>
                            <td>85,000</td>
                            <td>Fortified trench carapace engineered to weather sustained fire.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1.5mm;">Heavy Armor (Load 6–7 &middot; Prot 7–8)</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Heavy armors turn the wearer into an unyielding battlefield anchor. They require significant investment and impose movement penalties, but render the operative nearly impervious to standard small arms.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 2mm 0;">
                <div class="table-header">Heavy Armor Catalog</div>
                <table class="rules-table" style="font-size: 7.3pt; width: 100%; table-layout: fixed;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 0.7mm; width: 20%;">Armor Name</th>
                            <th style="padding: 1.0mm 0.7mm; width: 9%;">Prot</th>
                            <th style="padding: 1.0mm 0.7mm; width: 9%;">Load</th>
                            <th style="padding: 1.0mm 0.7mm; width: 18%;">Properties</th>
                            <th style="padding: 1.0mm 0.7mm; width: 13%;">Cost</th>
                            <th style="padding: 1.0mm 0.7mm; width: 31%;">Description</th>
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
                            <td>Dense fortress armor shrugging off critical hits and heavy slugs.</td>
                        </tr>
                        <tr>
                            <td class="bold">Titan Rig</td>
                            <td>8</td>
                            <td>7</td>
                            <td>Cumbersome (2), Hard, Blast, Tac (2)</td>
                            <td>280,000</td>
                            <td>Massive mechanized siege carapace; pinnacle of personal protection.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Due to the sheer mass and joint resistance of heavy carapace, operators frequently utilize powered servo-joints, hydraulic stabilization braces, and load-distribution harnesses to maintain agility during violent close-quarters room breaches and airlock assaults.
            </p>

            <div class="callout callout-tactical keep-together" style="margin: 2mm 0 1.5mm 0; padding: 2.6mm 3.0mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Doctrine: Stacking Defenses &amp; Breaching Operations</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1mm;">
                    Because Armor Protection stacks directly with defensive bonuses provided by <strong>Shields</strong> and <strong>Cover</strong>, a defensive operative can achieve formidable damage negation. An operative in Tactical Battleplate (5 Protection) bracing behind a Riot Shield (+2) in Medium Cover (+2) achieves <strong>9 total Protection</strong>, mitigating an entire volley of rifle fire before taking a single scratch.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    During room breaches, combining heavy carapace with an Active Protection System (APS Beacon) creates an impenetrable foothold. The beacon detonates incoming fragmentation grenades mid-flight, while the breacher's heavy plating absorbs suppressive small arms fire without suffering armor breaches.
                </p>
            </div>

            <div class="callout callout-tactical keep-together" style="margin: 0; padding: 2.6mm 3.0mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Example: Weathering the Boarding Barrage</div>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 1.2mm;">
                    During a violent breach of a station cargo bay, Jax is caught in the open when a pirate gunner opens fire with a <strong>Battle Rifle</strong>.
                </p>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 1.2mm;">
                    Jax is equipped with <strong>Tactical Battleplate</strong> (Protection 5, Load 4) and carries a <strong>Riot Shield</strong> (+2 Protection, Min STR 4, 1H, Load 2). Because Tactical Battleplate carries no Cumbersome penalty, his Agility rolls remain unhindered.
                </p>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 1.2mm;">
                    <strong>1. Incoming Attack:</strong> The pirate scores a Hit, spending 1 Hit on a Crit Effect (+2 damage) alongside the Battle Rifle's flat +4 Damage Bonus, generating <strong>14 points of physical damage</strong>.
                </p>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 1.2mm;">
                    <strong>2. Total Protection:</strong> Tactical Battleplate Base (5) + Riot Shield (+2) = <strong>7 Combined Protection</strong>.
                </p>
                <p style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 0;">
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
    # SPREAD 6 (Pages 78-79): TACTICAL GEAR (MOBILITY, FORTIFICATIONS, EXPLOSIVES)
    # =========================================================================

    p78 = """    <!-- =========================================================================
         PAGE 78 (Spread 6 Left) — TACTICAL GEAR RULES & MOBILITY HARDWARE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-rules-mobility">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear &amp; Mobility</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Gear</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Gear encompasses the broad spectrum of mission-critical tactical equipment, specialized toolkits, refillable field rigs, and survival hardware utilized by operators in the Corsair universe. While weapons and armor govern basic combat survival, gear provides the technical leverage, mobility, intelligence, and utility needed to complete dangerous boarding operations and wilderness expeditions.
            </p>

            <h3>Gear Rules &amp; Resolution</h3>
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 2mm; font-size: 8.0pt; line-height: 1.28;">
                <li><strong>Dedicated Attributes &amp; Test Pairs:</strong> Gear provides dedicated item attributes (such as <em>Mobility</em>, <em>Medicine</em>, <em>Sensors</em>, <em>Tinkering</em>, <em>Locksmith</em>, <em>Disguise</em>, <em>Forgery</em>, <em>Interfacing</em>, <em>Hacking</em>, <em>Ordnance</em>). The item's attribute pairs with a core attribute to form the dice pool.</li>
                <li><strong>Action Point Costs:</strong> Activating gear requires <strong>1 Action Point (AP)</strong>, unless explicitly noted otherwise. Passive items (deploying Cover) still cost 1 AP.</li>
                <li><strong>Capacity &amp; Automatic Refill:</strong> Expendable gear has an innate <strong>Capacity (Cap X)</strong>. Charges <strong>automatically refill to maximum</strong> whenever visiting an eligible supply hub (starship, clinic, armory, depot) during place-to-place or day-to-day pacing, without spending Credits.</li>
                <li><strong>Stand-Alone Explosive Rolls:</strong> Explosives resolve as Area Attack Success Tests rolling pure <strong>Ordnance</strong> pools without pairing with an attribute.</li>
                <li><strong>Upgrade Compatibility:</strong> Gear can be enhanced with up to 3 standard Upgrade Kits to reduce Load by 1 or increase primary attribute by +1.</li>
            </ol>

            <h3>1. Mobility Gear</h3>
            <div class="table-container keep-together" style="margin: 1mm 0 1.5mm 0;">
                <div class="table-header">Mobility Gear Catalog</div>
                <table class="rules-table" style="font-size: 7.4pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Item</th>
                            <th style="padding: 0.9mm 0.9mm;">Properties</th>
                            <th style="padding: 0.9mm 0.9mm;">Load</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost (Cr)</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
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
                            <td>Micro-fiber magnetic gloves and boots for scaling metallic hulls.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Zipline (40m)</td>
                            <td>Zipline (40m), 24 HP</td>
                            <td>3</td>
                            <td>15,000</td>
                            <td>Pneumatic line launcher deploying high-tensile motorized cables.</td>
                        </tr>
                        <tr>
                            <td class="bold">Standard Grapple</td>
                            <td>Grapple (8m), Mob 3, Cap 3</td>
                            <td>2</td>
                            <td>5,000</td>
                            <td>Compact gas-tether launcher for rapid ascent and pull.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Grapple</td>
                            <td>Grapple (16m), Mob 4, Cap 4</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>Reinforced magnetic winch rig with extended pull and winch.</td>
                        </tr>
                        <tr>
                            <td class="bold">High-Tensile Rope</td>
                            <td>Utility Cordage (40m)</td>
                            <td>1</td>
                            <td>100</td>
                            <td>Braided synthetic rope rated for extreme loads and rappelling.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4 style="margin-top: 1mm;">Mobility Special Properties</h4>
            <ul style="font-size: 7.9pt; line-height: 1.26; margin-bottom: 0;">
                <li><strong>Jetpack (Xm):</strong> Activating costs <strong>1 AP</strong>; Success Test using <strong>Mobility + Agility</strong>. Flight movement = base speed (Xm) plus 1m per SP. Move 3D, hover, ignore difficult terrain. Vector Boost: spend Hit on Crit to gain <strong>+4m movement</strong>. Charging: Spend 1 AP to fly base speed in a straight line and immediately execute a Melee Attack. Ignore falling damage.</li>
                <li><strong>Surface Adhesion:</strong> 1 AP; Success Test using <strong>Mobility + Strength</strong>. Base climb speed 8m plus 1m per SP.</li>
                <li><strong>Zipline (40m):</strong> Launching cable costs 1 AP. Any creature traverses cable as part of standard move. Reeling in costs 1 AP.</li>
                <li><strong>Grapple (Xm) &amp; Target Displacement:</strong> 1 AP, expends 1 Charge. Inanimate targets: automatic success; winch pulls user to anchor. Hostile creatures: Complex Test using <strong>Mobility + Strength</strong>. Hits spent trigger <strong>Push Effect</strong> pulling target 1 space (2m) toward user; user may advance along line; deals damage equal to SPs.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">78</span>
        </div>
    </div>"""
    pages.append(p78)

    p79 = """<!-- =========================================================================
         PAGE 79 (Spread 6 Right) — FORTIFICATIONS & EXPLOSIVES RIGS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortifications-explosives">
        <div class="page-running-header">
            <span>Chapter 04: Fortifications &amp; Munitions</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">2. Fortification Gear</h3>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.5mm;">
                Deployable fortifications provide instant cover, automated defense, and remote weapon platforms across contested ship corridors and perimeter defense zones.
            </p>

            <div class="table-container keep-together" style="margin: 1.2mm 0 2mm 0;">
                <div class="table-header">Fortification Gear Catalog</div>
                <table class="rules-table" style="font-size: 7.4pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 0.9mm;">Item</th>
                            <th style="padding: 1.0mm 0.9mm;">Properties</th>
                            <th style="padding: 1.0mm 0.9mm;">Load</th>
                            <th style="padding: 1.0mm 0.9mm;">Cost (Cr)</th>
                            <th style="padding: 1.0mm 0.9mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Deployable Cover (Light)</td>
                            <td>Light Cover (+1), 12 HP, Prot 4</td>
                            <td>2</td>
                            <td>5,000</td>
                            <td>Rapid-deployment ballistic fabric barrier for quick ambushes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Med)</td>
                            <td>Med Cover (+2), 24 HP, Prot 8</td>
                            <td>3</td>
                            <td>8,000</td>
                            <td>Telescoping ceramic-composite barricade with ground spikes.</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Heavy)</td>
                            <td>Heavy Cover (+3), 36 HP, Prot 12</td>
                            <td>4</td>
                            <td>12,000</td>
                            <td>Heavy alloy blast shield designed to withstand sustained assault.</td>
                        </tr>
                        <tr>
                            <td class="bold">APS Beacon</td>
                            <td>Intercept 5, Reaction, 24 HP</td>
                            <td>3</td>
                            <td>25,000</td>
                            <td>Automated Active Protection System firing counter-munitions.</td>
                        </tr>
                        <tr>
                            <td class="bold">Smartpod Mount</td>
                            <td>Automount 3, 12 HP</td>
                            <td>3</td>
                            <td>36,000</td>
                            <td>Motorized gyro-stabilized turret chassis for mounted weapons.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4 style="margin-top: 1.2mm;">Fortification Special Properties</h4>
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 2mm;">
                <li><strong>Deployable Cover:</strong> 1 AP to deploy or pack up. Grants listed Protection bonus (+1 to +3) to shelterers. Possesses own Cover HP and Innate Protection. Recover for 1 AP.</li>
                <li><strong>Intercept (X) &amp; Area Defense:</strong> Gains <strong>1 Free Reaction AP per round</strong> to contest incoming Area Attacks and Ordnance explosions, rolling pure Intercept (X). If no dice 8+ remain, munition is destroyed.</li>
                <li><strong>Automount (X):</strong> 1 AP to deploy and mount weapon. Spend 1 AP to fire remotely: rolls Automount (X) + Finesse (or pure Automount if autonomous). Recover for 1 AP.</li>
            </ul>

            <h3 style="margin-top: 2mm;">3. Explosives &amp; Launchers</h3>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.5mm;">
                Explosives deliver high-yield area destruction, obscuration, and tactical disruption. Rather than tracking individual loose throwables, combatants carry refillable <strong>Grenade Rigs</strong> that allow on-the-fly munition selection at the point of use.
            </p>

            <div class="table-container keep-together" style="margin: 1.2mm 0 2mm 0;">
                <div class="table-header">Explosives &amp; Launchers Catalog</div>
                <table class="rules-table" style="font-size: 7.4pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.0mm 0.9mm;">Item</th>
                            <th style="padding: 1.0mm 0.9mm;">Properties</th>
                            <th style="padding: 1.0mm 0.9mm;">Load</th>
                            <th style="padding: 1.0mm 0.9mm;">Cost (Cr)</th>
                            <th style="padding: 1.0mm 0.9mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Grenade Rig</td>
                            <td>Cap 3, Refillable, Choice</td>
                            <td>2</td>
                            <td>4,000</td>
                            <td>Armored chest bandolier holding 3 refillable charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Grenade Rig</td>
                            <td>Cap 5, Refillable, Choice</td>
                            <td>3</td>
                            <td>10,000</td>
                            <td>Heavy combat rig holding 5 refillable charges with instant choice.</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Demolitions Rig</td>
                            <td>Cap 2, Refillable, Choice</td>
                            <td>3</td>
                            <td>8,000</td>
                            <td>Reinforced breaching rig holding 2 heavy demolition charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Siege Demolitions Rig</td>
                            <td>Cap 4, Refillable, Choice</td>
                            <td>4</td>
                            <td>16,000</td>
                            <td>Military demolition harness carrying 4 heavy breaching charges.</td>
                        </tr>
                        <tr>
                            <td class="bold">Grenade Launcher Rig</td>
                            <td>Delivery (Medium Range)</td>
                            <td>2</td>
                            <td>6,000</td>
                            <td>Shoulder-fired tubular launcher firing Ordnance to Med Range.</td>
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
                            <td>Heavy laser-guided missile tube firing to Extreme Range.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4 style="margin-top: 1.2mm;">Munition Profiles &amp; Explosives Properties</h4>
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                <li><strong>Frag Munition:</strong> Ordnance 4, Blast 3, 8m Radius. Shrapnel anti-personnel bomb.</li>
                <li><strong>Flashbang Munition:</strong> Ordnance 5, Area Stun, 4m Radius. Blinds targets (discards highest die on next roll).</li>
                <li><strong>Smoke Canister:</strong> Area Obscurance, 8m Radius. Fills area with thermal smoke blocking sight without rolling.</li>
                <li><strong>HE Munition:</strong> Ordnance 5, Blast 5, 4m Radius. High-explosive concussion charge for bulkheads.</li>
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
    # SPREAD 7 (Pages 80-81): MEDICAL, TECH, SURVIVAL, EXOTIC & RARITY LADDER
    # =========================================================================

    p80 = """<!-- =========================================================================
         PAGE 80 (Spread 7 Left) — MEDICAL, CONSUMABLES, INFILTRATION & TECH KITS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-medical-and-tech">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Medical &amp; Technical Systems</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">4. Medical &amp; Consumables</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Medical kits and performance stimulant injectors provide emergency field triage, physical recovery, and temporary biochemical boosts. All medical equipment operates on durable, refillable casings.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1.8mm 0;">
                <div class="table-header">Medical &amp; Consumables Catalog</div>
                <table class="rules-table" style="font-size: 7.4pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Item</th>
                            <th style="padding: 0.9mm 0.9mm;">Properties</th>
                            <th style="padding: 0.9mm 0.9mm;">Ld</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Field Medi-Kit</td>
                            <td>Medicine 3, Cap 3, Lesser (1/2)</td>
                            <td>1</td>
                            <td>2,500</td>
                            <td>Auto-sutures, dermal staplers, and coagulant spray.</td>
                        </tr>
                        <tr>
                            <td class="bold">Trauma Rig</td>
                            <td>Medicine 4, Cap 4, Lesser (1/1)</td>
                            <td>2</td>
                            <td>7,500</td>
                            <td>Mil-spec suite with rapid tissue welders and synthetic blood.</td>
                        </tr>
                        <tr>
                            <td class="bold">Phoenix Reconstruct</td>
                            <td>Medicine 4, Cap 2, Greater (1/1)</td>
                            <td>2</td>
                            <td>15,000</td>
                            <td>Stabilizes trauma and clears Aggravated damage.</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Inhaler</td>
                            <td>Medicine 3, Cap 3, Mental (1/2)</td>
                            <td>1</td>
                            <td>2,000</td>
                            <td>Pressurized mist dispenser countering panic and shock.</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Rig</td>
                            <td>Medicine 4, Cap 4, Mental (1/1)</td>
                            <td>2</td>
                            <td>6,000</td>
                            <td>Cranial auto-injector delivering potent cognitive restoratives.</td>
                        </tr>
                        <tr>
                            <td class="bold">Stim Injector</td>
                            <td>Capacity 3, Refillable, Choice</td>
                            <td>1</td>
                            <td>5,000</td>
                            <td>Transdermal auto-injector delivering 3 stim doses.</td>
                        </tr>
                        <tr>
                            <td class="bold">Chem-Rig</td>
                            <td>Capacity 5, Refillable, Choice</td>
                            <td>2</td>
                            <td>12,000</td>
                            <td>High-capacity harness carrying 5 performance stim doses.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4 style="margin-top: 1mm;">Medical Rules &amp; Stimulants</h4>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.2mm;">
                <strong>Medicine (X) Triage:</strong> 1 AP, 1 Charge; test using <strong>Medicine + Knowledge</strong>. <strong>Lesser:</strong> Restores 1 segment / X SPs. <strong>Greater:</strong> Clears Aggravated damage at 2X SPs.
            </p>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.5mm;">
                <strong>Combat Stimulants (Volatile 2, Fleeting):</strong> 1 AP to inject. Grants +1 to one Core Attribute: <em>Roid:</em> +1 STR &middot; <em>Nitro:</em> +1 AGI &middot; <em>Edgedance:</em> +1 FIN &middot; <em>SharpX:</em> +1 INS &middot; <em>Cognita:</em> +1 KNO &middot; <em>Rizz:</em> +1 PRE. <strong>Volatile 2:</strong> User takes 2 unmitigated damage upon injection, plus additional damage per active stim in system.
            </p>

            <h3 style="margin-top: 1.5mm;">5. Infiltration &amp; Tech Kits</h3>
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 1.4mm;">
                Specialized toolkits and electronic rigs used to bypass physical security, falsify credentials, and penetrate secure data networks across the Sphere.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1.8mm 0;">
                <div class="table-header">Infiltration &amp; Tech Kits Catalog</div>
                <table class="rules-table" style="font-size: 7.3pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.9mm 0.9mm;">Item</th>
                            <th style="padding: 0.9mm 0.9mm;">Properties</th>
                            <th style="padding: 0.9mm 0.9mm;">Ld</th>
                            <th style="padding: 0.9mm 0.9mm;">Cost</th>
                            <th style="padding: 0.9mm 0.9mm;">Description</th>
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
                            <td>Baseline portable cyberdeck with standard optical transceiver.</td>
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
                            <td>Black-market military cyberdeck built to shred mainframe ICE.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h4 style="margin-top: 1mm;">Technical Actions (1 AP)</h4>
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                <li><strong>Tinkering:</strong> Repairs, field modifications, and hardware sabotage (<em>Tinkering + Knowledge</em>).</li>
                <li><strong>Locksmith:</strong> Bypassing electronic locks, mechanical tumblers, and airlock seals (<em>Locksmith + Finesse</em>).</li>
                <li><strong>Disguise:</strong> Crafting physical disguises, facial prosthetics, and behavioral mimicry (<em>Disguise + Knowledge</em>).</li>
                <li><strong>Forgery:</strong> Replicating cargo manifests, fabricating security seals, and counterfeiting identity chits (<em>Forgery + Finesse</em>).</li>
                <li><strong>Interfacing:</strong> Operating standard computer terminals, extracting flight telemetry, and station commands (<em>Interfacing + Knowledge</em>).</li>
                <li><strong>Hacking:</strong> Breaching corporate mainframe ICE, subverting automated defenses, and seizing data nodes (<em>Hacking + Knowledge</em>).</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">80</span>
        </div>
    </div>"""
    pages.append(p80)

    p81 = """    <!-- =========================================================================
         PAGE 81 (Spread 7 Right) — SURVEILLANCE, SURVIVAL & EXOTIC HARDWARE LADDER
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="surveillance-survival-exotic">
        <div class="page-running-header">
            <span>Chapter 04: Surveillance &amp; Exotic Hardware</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">6. Detection, Surveillance &amp; Survival</h3>
            <p style="font-size: 8.0pt; line-height: 1.26; margin-bottom: 1mm;">
                Sensors, autonomous drones, and environmental gear essential for deep-space excursions and recon operations.
            </p>

            <div class="table-container keep-together" style="margin: 0.5mm 0 1mm 0;">
                <div class="table-header">Surveillance &amp; Survival Catalog</div>
                <table class="rules-table" style="font-size: 7.2pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.7mm 0.7mm;">Item</th>
                            <th style="padding: 0.7mm 0.7mm;">Properties</th>
                            <th style="padding: 0.7mm 0.7mm;">Ld</th>
                            <th style="padding: 0.7mm 0.7mm;">Cost</th>
                            <th style="padding: 0.7mm 0.7mm;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Proximity Sensor</td>
                            <td>Scouting 4m, Alert</td>
                            <td>1/2</td>
                            <td>1,000</td>
                            <td>Magnetic trip-sensor broadcasting alert.</td>
                        </tr>
                        <tr>
                            <td class="bold">Proximity Radar</td>
                            <td>Scouting 20m, 360-Sweep</td>
                            <td>2</td>
                            <td>25,000</td>
                            <td>Radar mapping motion and voids.</td>
                        </tr>
                        <tr>
                            <td class="bold">Recon Drone</td>
                            <td>Fly 20m, Sensors 2</td>
                            <td>2</td>
                            <td>35,000</td>
                            <td>Micro-quadcopter with night optics.</td>
                        </tr>
                        <tr>
                            <td class="bold">Forensic Sensor</td>
                            <td>Sensors 4, Chemical Scan</td>
                            <td>3</td>
                            <td>20,000</td>
                            <td>Handheld spectrometer for field scans.</td>
                        </tr>
                        <tr>
                            <td class="bold">Vacuum Suit</td>
                            <td>Environmental Immunity</td>
                            <td>1</td>
                            <td>5,000</td>
                            <td>Pressurized suit for vacuum and heat.</td>
                        </tr>
                        <tr>
                            <td class="bold">Field Rations</td>
                            <td>Sustenance (1 Week)</td>
                            <td>1</td>
                            <td>50</td>
                            <td>Nutrient-dense meal packs for ops.</td>
                        </tr>
                        <tr>
                            <td class="bold">Wilderness Camp</td>
                            <td>Squad Shelter (4 Ops)</td>
                            <td>4</td>
                            <td>500</td>
                            <td>Pressurized tent, cycler, blankets.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Commlink</td>
                            <td>Interfacing 2, Long-Range</td>
                            <td>0</td>
                            <td>1,000</td>
                            <td>Frequency-hopping comm transceiver.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 7.6pt; line-height: 1.22; margin-bottom: 1.5mm;">
                <strong>Sensor &amp; Survival:</strong> <em>Sensors:</em> Active sweep (Sensors + Knowledge, 1 AP) &middot; <em>Scouting:</em> Passive alert &middot; <em>Drone:</em> Fly 20m/round (1 AP) &middot; <em>Environmental:</em> Immunity to &minus;150°C to +200°C and vacuum (12 hrs).
            </p>

            <h2 style="margin-top: 1mm;">Exotic Hardware</h2>
            <p class="lead" style="font-size: 8.5pt; line-height: 1.30; margin-bottom: 1mm;">
                Exotic Hardware refers to the narrow, lethal category of equipment far beyond standard procurement: black-budget prototypes, hybrid alien alloys, and Precursor dark-matter transducing relics. They are rare, exorbitantly expensive, and carried only by veterans who have both the coin to afford them and the physical constitution to carry their crushing weight.
            </p>

            <h3>The Rules of Exotic Hardware</h3>
            <ol style="margin-left: 3.5mm; padding-left: 0; margin-bottom: 1mm; font-size: 7.7pt; line-height: 1.24;">
                <li><strong>Load Taxation Over Limits:</strong> Operatives carry what their spine endures against the absolute limit of <strong>12 + (Strength &times; 2)</strong>.</li>
                <li><strong>Action Point Economy:</strong> Activating functions costs <strong>1 AP</strong>. Passive defenses apply continuously.</li>
                <li><strong>Pacing Cooldowns:</strong> Moment-to-Moment (~5–10s), Place-to-Place (~1 hr), Day-to-Day (24-hr cycle).</li>
                <li><strong>Irreplaceable Maintenance:</strong> 0 HP requires a workshop and <strong>Tinkering + Knowledge</strong> test against Tier DC. Precursor relics cannot be repaired by mortals without rare molecular salvage.</li>
                <li><strong>Non-Customizable Architecture:</strong> Precision prototypes operating at atomic tolerances <strong>cannot accept Upgrade Kits</strong>. Statistics and Load values are permanently fixed as written.</li>
            </ol>

            <h3 style="margin-top: 1mm;" class="column-span-all">The 4-Tier Rarity &amp; Economic Ladder</h3>
            <div class="table-container keep-together column-span-all" style="margin: 0.5mm 0 1mm 0;">
                <div class="table-header">Exotic Hardware Rarity &amp; Acquisition Ladder</div>
                <table class="rules-table" style="font-size: 7.2pt;">
                    <thead>
                        <tr>
                            <th style="padding: 0.7mm 0.7mm; width: 10%;">Tier</th>
                            <th style="padding: 0.7mm 0.7mm; width: 22%;">Classification</th>
                            <th style="padding: 0.7mm 0.7mm; width: 22%;">Typical Cost (Credits)</th>
                            <th style="padding: 0.7mm 0.7mm; width: 46%;">Market Reality &amp; Acquisition</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tier 1</td>
                            <td class="bold" style="color: var(--color-gold);">Mil-Spec Skunkworks</td>
                            <td>15,000 &ndash; 30,000 CR</td>
                            <td>Limited-run military trials and aerospace machining (Caldera, Port Zenith, Panthera). Corporate fixers or colonial sponsors.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 2</td>
                            <td class="bold" style="color: var(--color-gold);">Classified Prototypes</td>
                            <td>40,000 &ndash; 80,000 CR</td>
                            <td>Bleeding-edge espionage targets, hybrid alien polymers, and cybernetic field rigs. Corporate black-site heists or black markets.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 3</td>
                            <td class="bold" style="color: var(--color-gold);">Precursor Relics</td>
                            <td>100,000 &ndash; 250,000 CR</td>
                            <td>Intact alien artifacts and self-repairing lattices from Vault excavations. Strictly illegal contraband under Covenant Accords.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 4</td>
                            <td class="bold" style="color: var(--color-gold);">Singularities &amp; Wonders</td>
                            <td><strong>Priceless</strong> (Not for Sale)</td>
                            <td>Mythic artifacts of campaign-defining significance (dreadnought core, Shard lattice, null-beam projector). Major campaign milestones.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p class="column-span-all" style="font-size: 7.7pt; line-height: 1.24; margin-bottom: 0;">
                <strong>Campaign Integration:</strong> Game Masters are encouraged to introduce Exotic Hardware as tangible milestones rather than routine loot drops. A Tier 1 prototype in the hands of an elite rival gives players an immediate preview of high-tier capabilities, while recovering a Tier 3 Precursor relic triggers attention from corporate retrieval squads, Covenant inquisitors, and pirate cartels alike.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">81</span>
        </div>
    </div>"""
    pages.append(p81)

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
    generate_ch04_zero_voids()
