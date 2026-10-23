# -*- coding: utf-8 -*-
"""
Generate verbatim, continuous-flow html/04_Armory_and_Gear.html.
20 pages (10 complete spreads: Pages 68 to 87).
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

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Combat &amp; The Armory</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                In the world of Corsair, conflict is inevitable. Whether facing down a squad of corporate enforcers, battling a monstrous alien in the depths of a derelict ship, or engaging in a desperate firefight across depressurized docking gantries, combat is a thrilling and dangerous reality of high-frontier survival. When conflict turns violent and every action matters, the game shifts into <strong>Moment to Moment</strong> pacing. While you can resolve combat using "theater of the mind," employing a grid-based battle map adds tactical depth and clarity to character and enemy positioning.
            </p>

            <h3>Movement</h3>
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
                Since the world is not a 2D plane, you can move up and down as well as left and right. Model verticality by adding horizontal grid layers separated by <strong>2 meters</strong>. Moving up and down between layers is always considered <strong>Difficult Terrain</strong>—unless you fall. Falling more than 2 meters inflicts damage equal to <strong>three times the number of meters fallen</strong>, and the damage is <strong>not reduced by Protection</strong>. Stories in an orbital habitat roughly correspond to vertical layers.
            </p>

            <h3>Flying</h3>
            <p>
                Flying allows you to move through air as if on solid ground. Ascending costs double: to ascend 2 meters, you must spend 4 meters of movement. Moving downward or horizontally uses movement normally. Flying creatures completely <strong>ignore Difficult Terrain</strong>.
            </p>
            <p>
                During the turn you lose flight, you remain in the space you occupy in the air until the end of the turn, falling to the ground at turn's end and taking falling damage if above 2 meters.
            </p>

            <h3>Difficult Terrain</h3>
            <p>
                Hindered ground—rubble, knee-deep sludge, thick vegetation, or hazardous terrain—costs <strong>2 meters of speed for every 1 meter of progress</strong>. Moving into a space containing difficult terrain costs <strong>8 meters</strong> of movement instead of the usual 4 meters. This rule also applies if the boundary between two spaces is difficult (e.g., vaulting a barricade or climbing a ledge).
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">68</span>
        </div>
    </div>"""
    pages.append(p68)

    p69 = """    <!-- =========================================================================
         PAGE 69 (Spread 1 Right) — CONTESTING MOVEMENT & THE CONTEST WALKTHROUGH
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="contesting-movement">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Movement</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Contesting Movement</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Movement is not always unopposed. A character can attempt to block, trip, or tackle a creature moving through a space they occupy by contesting the moving creature's movement Success Test.
            </p>
            <p>
                When a creature's movement path takes them through a space occupied by a hostile character, that character can choose to contest the movement using standard contest resolution:
            </p>
            <ol style="margin-left: 3.5mm; margin-bottom: 2mm; font-size: 8.2pt; line-height: 1.30;">
                <li><strong>The Contester Narrates:</strong> The contesting character describes how they are impeding movement (e.g., tripping them, grabbing clothing, or blocking their path).</li>
                <li><strong>The GM Chooses an Attribute:</strong> The GM selects a relevant Attribute for the contest, such as <strong>Strength</strong> to grab or <strong>Agility</strong> to trip.</li>
                <li><strong>The Contest Roll:</strong> The contester rolls a number of d10s equal to their chosen Attribute.</li>
                <li><strong>Eliminating Dice:</strong> For each success (8+) on the contest roll, the contester eliminates one of the highest dice from the moving creature's movement Success Test roll. If no dice showing 8+ remain at the end, the moving creature is stopped dead and stuck in the contester's space.</li>
            </ol>

            <div class="example-box keep-together" style="margin: 2mm 0;">
                <div class="example-title">Contesting Movement Example</div>
                <p>
                    <strong>The Scenario:</strong> Jax is attempting to run past a burly corporate enforcer to reach an airlock control panel. Jax spends 1 Action Point for a move action and makes an <strong>Agility</strong> Success Test to determine distance. Jax has Agility 4 and rolls <code>[9, 7, 5, 2]</code>. The highest die is 9, so he can move his base 1 space + 2 extra spaces (9m &divide; 4, rounded up), for a total of 3 spaces.
                </p>
                <p>
                    The enforcer stands along Jax's path. As Jax enters the enforcer's space, the GM declares the enforcer will contest the movement.
                </p>
                <p>
                    <strong>1. The Contest Roll:</strong> The enforcer has <strong>Strength 5</strong>. The GM narrates that the enforcer attempts to grab Jax as he runs by. The enforcer rolls 5d10 for the contest.
                </p>
                <p>
                    <strong>2. The Result:</strong> The enforcer's roll is <code>[10, 8, 6, 4, 1]</code>—two successes (10 and 8).
                </p>
                <p>
                    <strong>3. Eliminating Dice:</strong> The two successes eliminate the two highest dice from Jax's movement roll (<code>[9, 7, 5, 2]</code>). The 9 and 7 are eliminated.
                </p>
                <p>
                    <strong>4. Final Outcome:</strong> Jax's movement roll is now <code>[5, 2]</code>. The highest remaining die is a 5. Since there are no dice with a result of 8 or higher, the contest is successful. Jax's movement ends immediately in the enforcer's space. He is stopped in his tracks, unable to reach the control panel this turn.
                </p>
            </div>

            <div class="callout callout-amber keep-together" style="margin-top: 2mm; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 9.2pt;">Chokepoint Interception Tactics</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    In pressurized starship corridors and narrow airlocks, contesting movement allows front-line defenders (such as Vanguards and armored Hazchem operatives) to physically bottle up enemy assault teams, preventing hostiles from slipping past to target vulnerable snipers or tech operators.
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
    # SPREAD 2 (Pages 70-71): SPACE OCCUPANCY, CQC, COVER & DESTRUCTION
    # =========================================================================

    p70 = """    <!-- =========================================================================
         PAGE 70 (Spread 2 Left) — SPACE OCCUPANCY, MELEE & CQC
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="space-occupancy-cqc">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Space &amp; CQC</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Space and Occupancy</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Combat in Corsair is dynamic and often close-quartered. A single 4&times;4 meter space is not limited to one character. Understanding how multiple characters occupy and interact within a single space is key to tactical success.
            </p>
            <p>
                A single 4&times;4 meter space can comfortably house up to <strong>4 standard-sized creatures</strong>. Many actions, especially melee attacks and certain Teamwork maneuvers, require you to share a space with your target or ally.
            </p>

            <h3>Outnumbering</h3>
            <p>
                Ganging up on a foe is a valid and effective tactic. When you and your allies outnumber your opponents within a single space, you gain a significant advantage in melee combat.
            </p>
            <p>
                You receive a number of <strong>Upgrades</strong> on your melee attack tests equal to the difference between the number of allied creatures and hostile creatures in that space. For example, if 3 allies are in a space with 1 enemy, all allies receive <strong>2 Upgrades</strong> (3 &minus; 1 = 2) on their melee attacks against that enemy.
            </p>

            <h3>Melee Engagement &amp; Moving into Spaces</h3>
            <p>
                You can attack a creature in the same space as you, or an adjacent space. Melee attacks must use any combination of two separate Physical Attributes (e.g., <strong>Strength + Agility</strong> to drive a heavy blade through an enforcer's guard, or <strong>Agility + Finesse</strong> for a surgical knife thrust at an unarmored seam).
            </p>
            <p>
                When you attack a creature in an adjacent space, you move into it, provided it holds fewer than 4 creatures. If already full, you perform the attack from your current space, but calculate outnumbering as if you and all allies in your space were inside the defender's space.
            </p>

            <h3>Creature Size</h3>
            <p>
                The capacity of a space is affected by biological and mechanical mass:
            </p>
            <ul>
                <li><strong>Standard:</strong> Typical humanoids (Humans, Elves, Dwarves). Occupies 1 slot (up to 4 per space).</li>
                <li><strong>Large:</strong> Hulking alien brutes and war-drones. Occupies the space of <strong>2 standard creatures</strong> (maximum 2 per space).</li>
                <li><strong>Huge:</strong> Small vehicles, combat walkers, and monstrous beasts. Occupies the space of <strong>4 standard creatures</strong> (fills entire space).</li>
            </ul>
            <p>
                Truly massive entities may extend across multiple spaces, counting as Large or Huge in each space for capacity and targeting.
            </p>

            <h2>Close Quarters Combat (CQC)</h2>
            <p>
                When in the same space as a hostile creature, you are in <strong>Close Quarters Combat (CQC)</strong>. This state has significant implications for ranged weaponry:
            </p>
            <ul>
                <li><strong>Firing in CQC:</strong> Discharging a ranged weapon while in CQC (an enemy in your space) imposes <strong>2 Downgrades</strong> to your attack test.</li>
                <li><strong>Firing into CQC:</strong> Firing from outside into a space where allies and enemies are engaged in CQC imposes <strong>1 Downgrade</strong> to avoid hitting friends.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""
    pages.append(p70)

    p71 = """    <!-- =========================================================================
         PAGE 71 (Spread 2 Right) — COVER, DESTRUCTION & COVER FACING
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="combat-cover">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Combat Cover</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Cover</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Taking cover is a fundamental tactic for surviving a firefight. Environmental features offer vital protection from incoming attacks.
            </p>
            <p>
                When a character is in a space containing cover (a crate, pillar, or low wall), they gain a bonus to their <strong>Protection</strong>. This bonus stacks with Protection from armor and provides a flat reduction to incoming damage. This bonus only applies against attacks originating from <em>outside</em> the character's current space:
            </p>
            <ul>
                <li><strong>Light Cover (+1 Protection):</strong> Small objects offering partial concealment, like a thin pipe or small barrel.</li>
                <li><strong>Medium Cover (+2 Protection):</strong> Solid objects hiding a significant portion of your body, like an engine block or bulkhead.</li>
                <li><strong>Heavy Cover (+3 Protection):</strong> Large, durable objects almost completely concealing you, like a fortified bunker wall or building corner.</li>
            </ul>

            <h3>Destroying Cover</h3>
            <p>
                Cover can be destroyed. Light, Medium, and Heavy Cover possess <strong>12, 24, and 36 Health Points (HP)</strong> and an innate Protection of <strong>4, 8, and 12</strong> respectively when directly targeted:
            </p>
            <ul>
                <li>Attacking cover is a <strong>Success Test</strong> instead of a Complex Test.</li>
                <li>For every <strong>12 damage</strong> the cover takes, its provided Protection benefit is reduced by 1.</li>
                <li>Specialized breaching charges, anti-materiel weapons, and demolition explosives specifically <strong>ignore cover's innate Protection</strong>.</li>
            </ul>

            <div class="table-container keep-together" style="margin: 2mm 0;">
                <div class="table-header">Cover Defensive &amp; Structural Ratings</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 2mm;">Cover Tier</th>
                            <th style="padding: 1.4mm 2mm;">Bonus Prot</th>
                            <th style="padding: 1.4mm 2mm;">Cover HP</th>
                            <th style="padding: 1.4mm 2mm;">Innate Prot</th>
                            <th style="padding: 1.4mm 2mm;">Degrade Threshold</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Light Cover</td>
                            <td>+1</td>
                            <td>12 HP</td>
                            <td>4</td>
                            <td>Destroyed at 12 Dmg</td>
                        </tr>
                        <tr>
                            <td class="bold">Medium Cover</td>
                            <td>+2</td>
                            <td>24 HP</td>
                            <td>8</td>
                            <td>&minus;1 Prot per 12 Dmg</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Cover</td>
                            <td>+3</td>
                            <td>36 HP</td>
                            <td>12</td>
                            <td>&minus;1 Prot per 12 Dmg</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h2>Cover Facing</h2>
            <p>
                Using cover effectively is about angling against incoming fire. The first time you take an attack where you benefit from the bonus, draw a line from the attacker to your position: whichever side of your space it crosses becomes your <strong>covering side</strong>. When the line crosses a corner, both adjacent sides become covering sides.
            </p>
            <p>
                On subsequent attacks during the turn:
            </p>
            <ul>
                <li><strong>Full Bonus:</strong> Line crosses covering side: receive full Protection bonus.</li>
                <li><strong>Reduced Bonus:</strong> Line crosses a side adjacent to covering side: Protection bonus reduced by <strong>1 on hex</strong>, and <strong>2 on square</strong>.</li>
                <li><strong>No Bonus (Exposed):</strong> Line crosses a side not adjacent to covering side: gain no benefit from cover against that attack.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">71</span>
        </div>
    </div>"""
    pages.append(p71)

    # =========================================================================
    # SPREAD 3 (Pages 72-73): THE ARMORY, LOAD SYSTEM & EQUIPMENT OVERVIEW
    # =========================================================================

    p72 = """    <!-- =========================================================================
         PAGE 72 (Spread 3 Left) — THE ARMORY, LOAD SYSTEM & WEAPON CLASSIFICATIONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="the-armory-load">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: The Armory &amp; Load</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">The Armory &amp; Equipment</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Not every item a character carries has a significant mechanical impact on the game. Everyday objects like personal commlinks, hab keys, or sentimental trinkets are assumed belongings without specific rules. However, items providing a distinct advantage in challenging situations—from weapons and armor to specialized tools—are classified as Equipment, governed by the <strong>Load system</strong>.
            </p>

            <h3>The Load Invariant</h3>
            <p>
                Every piece of mechanically significant equipment has a <strong>Load</strong> value representing its weight, bulk, and cumbersomeness. Carrying capacity is strictly limited by physical conditioning:
            </p>
            <div class="callout callout-cyan keep-together" style="margin: 2mm 0; padding: 2.5mm 3.5mm;">
                <p style="font-size: 9.5pt; font-weight: 700; text-align: center; margin: 0;">
                    \text{Maximum Load Capacity} = 12 + (\text{Strength} \times 2)
                </p>
            </div>
            <p>
                This limit is absolute; an operative cannot carry items exceeding this capacity under any circumstances. Leaving some Load capacity unused is a wise tactical choice, preserving space for vital salvage or mission assets discovered on the job.
            </p>

            <h3>Equipment Categories</h3>
            <p>
                Equipment is divided into major categories:
            </p>
            <ul>
                <li><strong>Weapons:</strong> Anything designed to inflict physical harm, divided into Melee and Ranged platforms.</li>
                <li><strong>Armor:</strong> Protective gear worn to reduce or negate incoming physical and kinetic damage.</li>
                <li><strong>Gear:</strong> Tactical kits, mobility rigs, consumables, explosives, and surveillance equipment.</li>
                <li><strong>Exotic Hardware:</strong> Classified prototypes, skunkworks gear, and salvaged Precursor relics.</li>
            </ul>

            <h3>Damage Bonus</h3>
            <p>
                All weapons share a <strong>Damage Bonus</strong>: a flat integer value added to the Success Points generated on a successful attack roll. These bonus points can only increase damage dealt and cannot be used for other effects.
            </p>

            <h3>Melee Weapons Fundamentals</h3>
            <p>
                Melee weapons are engineered for brutal close-quarters combat. Each deals a specific damage type—<strong>Piercing</strong>, <strong>Slashing</strong>, or <strong>Striking</strong>—aligned with a favored physical Attribute Pair. Attacking with a favored pair grants a damage bonus equal to the <strong>lower attribute</strong> of the test, in addition to the flat Damage Bonus.
            </p>

            <h3>Ranged Weapons Fundamentals</h3>
            <p>
                Ranged weapons are defined by Accuracy, Rate of Fire, Damage Bonus, and Hands:
            </p>
            <ul>
                <li><strong>Accuracy Array:</strong> Ranged attacks always pair the weapon's Accuracy at target distance with <strong>Finesse</strong> (<strong>Accuracy + Finesse</strong>) across four Range Bands: Short (0–5 spaces, ~0–20m), Medium (6–12 spaces, ~20–40m), Long (13–20 spaces, ~40–80m), and Extreme (20+ spaces, ~80m+).</li>
                <li><strong>Rate of Fire (RoF):</strong> Cyclic burst capability setting the strict upper limit on total <strong>Crit Effects</strong> and <strong>Chain Effects</strong> activatable on an attack roll.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">72</span>
        </div>
    </div>"""
    pages.append(p72)

    p73 = """    <!-- =========================================================================
         PAGE 73 (Spread 3 Right) — ARMOR, GEAR & REPAIR OPERATIONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armory-repairs-overview">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: The Armory &amp; Load</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Armor Overview</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Armor is protective gear worn by a character to reduce incoming physical and kinetic damage. Every suit is defined by Protection, Load, Properties, and Cost:
            </p>
            <ul>
                <li><strong>Protection:</strong> Flat integer reduction applied directly to incoming damage before affecting health. Armor Protection stacks with Shields and Cover, but an operative can benefit from only <strong>one worn suit of armor</strong> at a time.</li>
                <li><strong>Load &amp; Agility:</strong> Armor enforces no binary Strength minimum to wear. Any operative can don any suit if they have Load capacity. However, heavy and siege armors feature <strong>Cumbersome (X)</strong>, imposing Downgrades on all <strong>Agility</strong> tests (including speed and evasion).</li>
                <li><strong>Properties:</strong> Specialized features such as <strong>Hardened</strong> (reducing critical damage), <strong>Blast-Dampened</strong> (+2 Protection vs Area/Explosives), <strong>Tactical Harness</strong> (dedicated Load slots), and <strong>Muffled</strong> (+1 Upgrade on Stealth).</li>
            </ul>

            <h2>Gear Overview</h2>
            <p>
                Gear encompasses all mission-critical tactical equipment, specialized toolkits, field consumables, and survival hardware organized into seven categories:
            </p>
            <ol style="margin-left: 3.5mm; margin-bottom: 2mm; font-size: 8.2pt; line-height: 1.30;">
                <li><strong>Mobility:</strong> Jump-packs, climbing kits, and motorized ziplines for vertical traversal.</li>
                <li><strong>Fortification:</strong> Deployable cover barricades, active protection defense beacons, and turrets.</li>
                <li><strong>Explosives:</strong> Multi-munition grenade bandoliers and rocket launcher systems.</li>
                <li><strong>Medical:</strong> Trauma suites, neural stabilizers, and performance stimulant injectors.</li>
                <li><strong>Infiltration:</strong> Locksmith kits, biometric disguise tools, and military cyberdecks.</li>
                <li><strong>Sensors:</strong> Proximity radars, recon drones, and forensic spectrometers.</li>
                <li><strong>Survival:</strong> Pressurized environmental hazard suits, commlinks, and rations.</li>
            </ol>
            <p>
                Gear items provide dedicated <strong>Item Attributes</strong> pairing with character attributes for tests costing <strong>1 Action Point (AP)</strong>. Consumable rigs possess fixed <strong>Capacity (Cap X)</strong>, automatically refilling at any supply hub without spending Credits or tracking restock counts.
            </p>

            <h2>Equipment Damage &amp; Repairs</h2>
            <p>
                Deployable gear, fortifications, vehicles, and technological hardware possess structure measured in <strong>Health Points (HP)</strong>. Damage reduces HP; at 0 HP, the item is disabled:
            </p>
            <ul>
                <li><strong>Field Repairs:</strong> Restoring HP costs <strong>1 AP</strong> (combat) or narrative time (downtime), requiring a <strong>Success Test</strong> using <strong>Tinkering + Knowledge</strong>.</li>
                <li><strong>HP Restored:</strong> The item recovers <strong>1 HP per Success Point</strong> generated, up to maximum HP. Completely destroyed items require dedicated workshops and spare parts.</li>
            </ul>

            <div class="callout callout-cyan keep-together" style="margin-top: 2mm; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 9.2pt;">Exotic Hardware Segregation</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    Unlike baseline gear, Exotic Hardware represents priceless prototypes and Precursor artifacts. Constrained by heavy Load and thermal cooldowns, exotic hardware cannot accept aftermarket Upgrade Kits; its statistics and properties are permanently fixed as written.
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
    # SPREAD 4 (Pages 74-75): FIREARMS CATALOG (HANDGUNS, SMGS, SHOTGUNS)
    # =========================================================================

    p74 = """    <!-- =========================================================================
         PAGE 74 (Spread 4 Left) — FIREARMS STATS, MANUFACTURERS & HANDGUNS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-handguns">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Firearms &amp; Ballistics</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                In the cold vacuum of space, across contested orbital platforms, and inside pressurized ship corridors, firearms are the ultimate arbiters of ranged combat. Ranging from rugged chemical-propellant slugthrowers to electro-thermal chemical (ETC) rifles and high-velocity magnetic rail drivers, firearms give Corsairs stopping power and suppression capability.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <ul>
                <li><strong>Accuracy (S / M / L / E):</strong> Calibrated for specific operational distances across Short (0–5 spaces, ~0–20m), Medium (6–12 spaces, ~20–40m), Long (13–20 spaces, ~40–80m), and Extreme (20+ spaces, ~80m+). Attack tests always roll <strong>Accuracy + Finesse</strong>. A dash (<code>&minus;</code>) indicates ineffective range.</li>
                <li><strong>Rate of Fire (RoF):</strong> Cyclic burst capability capping the total number of <strong>Crit Effects</strong> and <strong>Chain Effects</strong> activatable on a single attack roll:
                    <ul>
                        <li><em>RoF 0 (Heavy-Hitters):</em> High-caliber single-shot rifles, heavy revolvers, slug guns; massive kinetic shock without burst Crits/Chains.</li>
                        <li><em>RoF 1 (Precision/Semi-Auto):</em> Service pistols, DMRs, combat shotguns; up to 1 Crit or Chain effect.</li>
                        <li><em>RoF 2 (Burst/Auto):</em> Assault carbines, submachine guns; up to 2 Crit/Chain effects.</li>
                        <li><em>RoF 3–4 (Suppression/Rotary):</em> Machine guns, rotary cannons; up to 3–4 Crit/Chain effects.</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to Success Points on a hit.</li>
                <li><strong>Hands &amp; Load:</strong> One-handed (1H) sidearm or two-handed (2H) long gun.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p style="font-size: 8.3pt; line-height: 1.32;">
                <strong>Panthera Arms:</strong> High-tolerance corporate carbines and DMRs.<br>
                <strong>Vandal's Workshop:</strong> Stamped-sheet, high-RoF submachine guns.<br>
                <strong>Caldera Foundry:</strong> Heavy-bore shotguns and trench rifles.<br>
                <strong>Ker'Satz Korp:</strong> Precision magnetic rail drivers and hand cannons.<br>
                <strong>Chidori-Qwei:</strong> Polymer smart-linked sidearms and PDWs.
            </p>

            <h3>Handguns Catalog</h3>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Handguns &amp; Sidearms</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm;">Weapon Name</th>
                            <th style="padding: 1.4mm 1.5mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.4mm 1.5mm;">RoF</th>
                            <th style="padding: 1.4mm 1.5mm;">H</th>
                            <th style="padding: 1.4mm 1.5mm;">Dmg</th>
                            <th style="padding: 1.4mm 1.5mm;">Load</th>
                            <th style="padding: 1.4mm 1.5mm;">Cost</th>
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
                        </tr>
                        <tr>
                            <td class="bold">Service Pistol</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>800</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Revolver</td>
                            <td>3 / 2 / 1 / &minus;</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>1,200</td>
                        </tr>
                        <tr>
                            <td class="bold">Machine Pistol</td>
                            <td>3 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1</td>
                            <td>1,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Hand Cannon</td>
                            <td>2 / 3 / 2 / 0</td>
                            <td>0</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>1</td>
                            <td>2,200</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted);">
                <em>Descriptions:</em> <strong>Holdout:</strong> Ultra-compact concealable polymer pistol. <strong>Service:</strong> Standard semi-auto duty sidearm. <strong>Heavy Revolver:</strong> Magnum cylinder gun with punishing recoil. <strong>Machine Pistol:</strong> Point-blank burst sidearm. <strong>Hand Cannon:</strong> Reinforced anti-armor kinetic handgun.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">74</span>
        </div>
    </div>"""
    pages.append(p74)

    p75 = """    <!-- =========================================================================
         PAGE 75 (Spread 4 Right) — SUBMACHINE GUNS & SHOTGUNS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-smgs-shotguns">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Submachine Guns &amp; Shotguns</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Close-quarters primary weapons engineered for boarding operations, clearing tight ship bulkheads, and dominating short-range firefights across station gangways.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Submachine Guns &amp; Shotguns</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm;">Weapon Name</th>
                            <th style="padding: 1.4mm 1.5mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.4mm 1.5mm;">RoF</th>
                            <th style="padding: 1.4mm 1.5mm;">H</th>
                            <th style="padding: 1.4mm 1.5mm;">Dmg</th>
                            <th style="padding: 1.4mm 1.5mm;">Load</th>
                            <th style="padding: 1.4mm 1.5mm;">Cost</th>
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
                        </tr>
                        <tr>
                            <td class="bold">Tactical SMG</td>
                            <td>3 / 4 / 2 / 0</td>
                            <td>3</td>
                            <td>2H</td>
                            <td>+1</td>
                            <td>2</td>
                            <td>2,800</td>
                        </tr>
                        <tr>
                            <td class="bold">Trench Shotgun</td>
                            <td>5 / 2 / &minus; / &minus;</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>2</td>
                            <td>2,400</td>
                        </tr>
                        <tr>
                            <td class="bold">Combat Shotgun</td>
                            <td>4 / 3 / 0 / &minus;</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>3,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Scattergun</td>
                            <td>4 / 2 / &minus; / &minus;</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Operational Descriptions</h3>
            <ul>
                <li><strong>Compact SMG:</strong> Lightweight collapsible submachine gun designed for vehicle crews, security officers, and boarding parties clearing cramped crawlspaces.</li>
                <li><strong>Tactical SMG:</strong> Balanced automatic platform featuring integral gas recoil compensators, high cyclic fire rates, and extended optical rails.</li>
                <li><strong>Trench Shotgun:</strong> Heavy pump-action smoothbore scattergun delivering catastrophic kinetic spread at point-blank range; lacks burst capacity but hits with massive shock.</li>
                <li><strong>Combat Shotgun:</strong> Semi-automatic magazine-fed shotgun engineered for rapid room clearing, breach support, and aggressive assault corridors.</li>
                <li><strong>Riot Scattergun:</strong> Fully automatic drum-fed scattergun delivering overwhelming projectile swarms designed to shred unarmored boarding squads.</li>
            </ul>

            <div class="callout callout-amber keep-together" style="margin-top: 2mm; padding: 2.5mm 3.5mm;">
                <div class="callout-title" style="font-size: 9.5pt;">Corridor Ballistic Geometry</div>
                <p style="font-size: 8.2pt; line-height: 1.30;">
                    Inside pressurized hulls, combat occurs almost entirely at <strong>Short Range (0–5 spaces)</strong>. High-Accuracy scatterguns and compact SMGs maximize hit probability before targets reach hand-to-hand engagement, making them essential weapons for marine boarding squads.
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
    # SPREAD 5 (Pages 76-77): RIFLES, HEAVY SUPPORT & RANGED ACTION
    # =========================================================================

    p76 = """    <!-- =========================================================================
         PAGE 76 (Spread 5 Left) — RIFLES & HEAVY SUPPORT WEAPONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-rifles-heavy">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Combat &amp; Precision Rifles</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Versatile long guns balancing effective range, kinetic penetration, and tactical flexibility across station concourses, cargo bays, and planetary battlegrounds.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Combat &amp; Precision Rifles</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.5mm;">Weapon Name</th>
                            <th style="padding: 1.3mm 1.5mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.3mm 1.5mm;">RoF</th>
                            <th style="padding: 1.3mm 1.5mm;">H</th>
                            <th style="padding: 1.3mm 1.5mm;">Dmg</th>
                            <th style="padding: 1.3mm 1.5mm;">Load</th>
                            <th style="padding: 1.3mm 1.5mm;">Cost</th>
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
                        </tr>
                        <tr>
                            <td class="bold">Assault Rifle</td>
                            <td>2 / 4 / 3 / 1</td>
                            <td>2</td>
                            <td>2H</td>
                            <td>+2</td>
                            <td>3</td>
                            <td>4,800</td>
                        </tr>
                        <tr>
                            <td class="bold">Battle Rifle</td>
                            <td>2 / 3 / 4 / 2</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>3</td>
                            <td>5,500</td>
                        </tr>
                        <tr>
                            <td class="bold">DMR</td>
                            <td>1 / 3 / 5 / 3</td>
                            <td>1</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>7,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Sniper Rifle</td>
                            <td>0 / 2 / 5 / 4</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+5</td>
                            <td>4</td>
                            <td>9,500</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 7.9pt; line-height: 1.26; color: var(--text-muted); margin-bottom: 2mm;">
                <em>Descriptions:</em> <strong>Assault Carbine:</strong> Short-barreled mobility rifle for fast acquisition. <strong>Assault Rifle:</strong> Standard military burst platform across all zones. <strong>Battle Rifle:</strong> Heavy-caliber semi-auto armor-cracker. <strong>DMR:</strong> Mid-to-long range marksman rifle with high optics. <strong>Sniper Rifle:</strong> Extreme standoff precision rifle.
            </p>

            <h2>Heavy Support Weapons</h2>
            <p style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Crew-served and reinforced platforms delivering suppressive fire and anti-armor kinetic energy.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Heavy Support Weapons</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.5mm;">Weapon Name</th>
                            <th style="padding: 1.3mm 1.5mm;">Acc (S/M/L/E)</th>
                            <th style="padding: 1.3mm 1.5mm;">RoF</th>
                            <th style="padding: 1.3mm 1.5mm;">H</th>
                            <th style="padding: 1.3mm 1.5mm;">Dmg</th>
                            <th style="padding: 1.3mm 1.5mm;">Load</th>
                            <th style="padding: 1.3mm 1.5mm;">Cost</th>
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
                        </tr>
                        <tr>
                            <td class="bold">HMG</td>
                            <td>3 / 5 / 4 / 2</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>5</td>
                            <td>12,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Rotary Cannon</td>
                            <td>5 / 4 / 2 / 1</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>5</td>
                            <td>16,000</td>
                        </tr>
                        <tr>
                            <td class="bold">AMR</td>
                            <td>0 / 2 / 5 / 5</td>
                            <td>0</td>
                            <td>2H</td>
                            <td>+7</td>
                            <td>5</td>
                            <td>15,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 7.9pt; line-height: 1.26; color: var(--text-muted);">
                <em>Descriptions:</em> <strong>SAW:</strong> Belt-fed light machine gun pinning down squads. <strong>HMG:</strong> Heavy gun tearing through vehicle plating and barricades. <strong>Rotary Autocannon:</strong> Multi-barrel motorized cannon delivering extreme saturation. <strong>AMR:</strong> Magnetic anti-tank rifle penetrating bulkheads.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">76</span>
        </div>
    </div>"""
    pages.append(p76)

    p77 = """    <!-- =========================================================================
         PAGE 77 (Spread 5 Right) — DUAL WIELDING, UPGRADES & RANGED ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-customization-action">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Dual Wielding Firearms</h2>
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Wielding a sidearm in each hand enables intense suppressive fire and multi-target engagement:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield sidearms with the <strong>1H designation</strong>.</li>
                <li><strong>Combined Firepower:</strong> Add together both the flat <strong>Damage Bonus</strong> and the <strong>Rate of Fire (RoF)</strong> of the two firearms on your attack roll.</li>
                <li><strong>Worse Accuracy:</strong> Discharging two weapons simultaneously compromises sight alignment; you must use the <strong>worse (lower) Accuracy rating</strong> at the target's range band between the two weapons.</li>
            </ul>

            <h2>Firearm Upgrade Kits</h2>
            <p style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Stock firearms can be customized through precision gunsmithing. Upgrades escalate in cost with each installation:
            </p>
            <ul>
                <li><strong>Upgrade Limits:</strong> Two-handed weapons accept up to <strong>3 Upgrade Kits</strong>; 1H sidearms accept up to <strong>2 Upgrade Kits</strong>.</li>
                <li><strong>Tiered Cost Structure:</strong>
                    <ul>
                        <li><strong>1st Upgrade:</strong> 10,000 Credits</li>
                        <li><strong>2nd Upgrade:</strong> 25,000 Credits</li>
                        <li><strong>3rd Upgrade:</strong> 50,000 Credits</li>
                    </ul>
                </li>
                <li><strong>Upgrade Choices:</strong>
                    <ul>
                        <li><em>Lightweight Chassis:</em> Precision skeletonization reduces weapon's <strong>Load by 1</strong> (min 1/2 Load).</li>
                        <li><em>Lethal Tuning:</em> Match-grade barrel rifling increases flat <strong>Damage Bonus by +1</strong>.</li>
                        <li><em>Recoil Dampening:</em> Hydraulic buffers increase weapon's <strong>RoF by 1</strong>.</li>
                        <li><em>Optic Calibration:</em> Advanced sights increase <strong>Accuracy by +1</strong> at one designated range band.</li>
                    </ul>
                </li>
            </ul>

            <div class="example-box keep-together" style="margin-top: 2mm;">
                <div class="example-title">Example: Ranged Combat in Action</div>
                <p>
                    <strong>The Scenario:</strong> Jax advances down an industrial catwalk overlooking a contested hangar. Positioned <strong>8 spaces (~26m)</strong> away behind freight crates, an armed mercenary returns fire—placing the target at <strong>Medium Range</strong>.
                </p>
                <p>
                    Jax wields an <strong>Assault Rifle</strong> (Accuracy <code>2 / 4 / 3 / 1</code>, RoF 2, 2H, Load 3, +2 Damage Bonus). Jax's sheet shows <strong>Finesse 5</strong>.
                </p>
                <p>
                    <strong>1. Test Pool:</strong> Declaring an <strong>Accuracy + Finesse</strong> Complex Test. At Medium Range, rifle Accuracy is 4. Pairing with Finesse 5, higher is Finesse 5, lower is Accuracy 4.
                </p>
                <p>
                    <strong>2. Action Roll (Finesse 5):</strong> Jax rolls 5d10: <code>[2, 5, 8, 8, 9]</code> (three Hits: 8, 8, 9). Jax spends one Hit (8) on an <strong>Upgrade Effect</strong>, stepping up one Success die from d10 to <strong>d12</strong>.
                </p>
                <p>
                    <strong>3. Success Roll (Accuracy 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 7, 8]</code> on d10s and <code>10</code> on d12 (two Hits: 8, 10).
                </p>
                <p>
                    <strong>4. Effects &amp; RoF:</strong> Jax spends both Hits on <strong>Crit Effects</strong> (+2 damage each). The rifle's <strong>RoF 2</strong> perfectly accommodates 2 Crits.
                </p>
                <p>
                    <strong>5. Total Damage:</strong> Highest unspent die (7) + Two Crits (+4) + Rifle Damage Bonus (+2) = <strong>13 points of damage</strong>, punching through the container seam!
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
    # SPREAD 6 (Pages 78-79): MELEE WEAPONS, SHIELDS & HAND-TO-HAND ACTION
    # =========================================================================

    p78 = """    <!-- =========================================================================
         PAGE 78 (Spread 6 Left) — MELEE FUNDAMENTALS, DUAL WIELDING & UPGRADES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-fundamentals">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Melee Weapons &amp; Shields</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                In the tight corridors of starships, depressurized maintenance shafts, and orbital stations, discharging a firearm risks puncturing critical hull plating or ricocheting in zero-gravity. In confined environments, close combat demands physical prowess, tactical positioning, and weapon mastery.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <ul>
                <li><strong>Damage Type &amp; Favored Attribute Pair:</strong> Melee weapons inflict damage through three physical methods, each paired with a favored physical Attribute Pair:
                    <ul>
                        <li><strong>Piercing (Agility + Finesse):</strong> Pinpoint thrusts directed at structural seams, visor slits, and armor joints.</li>
                        <li><strong>Slashing (Agility + Strength):</strong> Sweeping cuts combining dynamic movement with cutting force.</li>
                        <li><strong>Striking (Strength + Finesse):</strong> Controlled impacts delivered with disciplined body mechanics and leverage.</li>
                    </ul>
                </li>
                <li><strong>Favored Pair Damage Bonus:</strong> Attacking with a weapon's favored Attribute Pair grants a damage bonus equal to the <strong>lower attribute</strong> in that pair, added directly to total damage alongside the weapon's flat Damage Bonus.</li>
                <li><strong>Minimum Strength (Min STR):</strong> Weapons require muscular leverage:
                    <ul>
                        <li><em>One-Handed (1H):</em> If Strength &lt; Min STR, you must wield it with <strong>two hands</strong> to attack.</li>
                        <li><em>Two-Handed (2H):</em> If Strength &lt; Min STR, the weapon is too heavy and you <strong>cannot attack with it</strong>.</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to Success Points on a hit. Heavier weapons feature substantially larger bonuses.</li>
                <li><strong>Hands, Load &amp; Cost:</strong> Natural hand requirements (1H/2H), inventory Load, and market price in Credits.</li>
            </ul>

            <h3>Dual Wielding Melee</h3>
            <p>
                Fighting with a weapon in each hand creates an aggressive combat style that overwhelms defensive guards:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield weapons with the <strong>1H designation</strong>. You must meet the Min STR of each weapon individually.</li>
                <li><strong>Combined Damage Bonus:</strong> Gain the flat <strong>Damage Bonus of both weapons</strong> added to your total outcome.</li>
                <li><strong>Attack Resolution:</strong> Designate which weapon leads the strike for Damage Type and favored pair bonus.</li>
            </ul>

            <h3>Melee Upgrade Kits</h3>
            <p>
                Two-handed weapons accept up to <strong>3 Upgrade Kits</strong>; 1H weapons accept up to <strong>2 Upgrade Kits</strong> (10,000 / 25,000 / 50,000 Credits):
            </p>
            <ul>
                <li><em>Lightweight Tuning:</em> Precision skeletal milling reduces weapon's <strong>Load by 1</strong> (min 1/2 Load).</li>
                <li><em>Lethal Edge / Weighted Core:</em> High-frequency vibration motors or carbide weights increase flat <strong>Damage Bonus by +1</strong>.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">78</span>
        </div>
    </div>"""
    pages.append(p78)

    p79 = """    <!-- =========================================================================
         PAGE 79 (Spread 6 Right) — MELEE CATALOG, SHIELDS & BOARDING ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-catalog-shields-action">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Weapons Catalog</h2>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Close-Quarters Melee Weapons</div>
                <table class="rules-table" style="font-size: 7.7pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.1mm 1.4mm;">Weapon Name</th>
                            <th style="padding: 1.1mm 1.4mm;">Type</th>
                            <th style="padding: 1.1mm 1.4mm;">Min STR</th>
                            <th style="padding: 1.1mm 1.4mm;">H</th>
                            <th style="padding: 1.1mm 1.4mm;">Dmg</th>
                            <th style="padding: 1.1mm 1.4mm;">Load</th>
                            <th style="padding: 1.1mm 1.4mm;">Cost</th>
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
                        </tr>
                        <tr>
                            <td class="bold">Combat Knife</td>
                            <td>Slashing</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>200</td>
                        </tr>
                        <tr>
                            <td class="bold">Knuckleduster</td>
                            <td>Striking</td>
                            <td>1</td>
                            <td>1H</td>
                            <td>+0</td>
                            <td>1/2</td>
                            <td>100</td>
                        </tr>
                        <tr>
                            <td class="bold">Dagger</td>
                            <td>Piercing</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>400</td>
                        </tr>
                        <tr>
                            <td class="bold">Hatchet / Machete</td>
                            <td>Slashing</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>500</td>
                        </tr>
                        <tr>
                            <td class="bold">Baton / Club</td>
                            <td>Striking</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>+1</td>
                            <td>1</td>
                            <td>300</td>
                        </tr>
                        <tr>
                            <td class="bold">Shortsword</td>
                            <td>Piercing</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,200</td>
                        </tr>
                        <tr>
                            <td class="bold">Boarding Axe</td>
                            <td>Slashing</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Mace / Crowbar</td>
                            <td>Striking</td>
                            <td>3</td>
                            <td>1H</td>
                            <td>+2</td>
                            <td>2</td>
                            <td>1,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Spear</td>
                            <td>Piercing</td>
                            <td>4</td>
                            <td>2H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,200</td>
                        </tr>
                        <tr>
                            <td class="bold">Longsword</td>
                            <td>Slashing</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,800</td>
                        </tr>
                        <tr>
                            <td class="bold">Warhammer</td>
                            <td>Striking</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>+3</td>
                            <td>3</td>
                            <td>2,400</td>
                        </tr>
                        <tr>
                            <td class="bold">Halberd / Poleaxe</td>
                            <td>Piercing</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Greatsword</td>
                            <td>Slashing</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>5,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Maul</td>
                            <td>Striking</td>
                            <td>5</td>
                            <td>2H</td>
                            <td>+4</td>
                            <td>4</td>
                            <td>4,800</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h2>Defensive Shields</h2>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Defensive Shields</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.8mm;">Shield Name</th>
                            <th style="padding: 1.3mm 1.8mm;">Prot</th>
                            <th style="padding: 1.3mm 1.8mm;">Min STR</th>
                            <th style="padding: 1.3mm 1.8mm;">H</th>
                            <th style="padding: 1.3mm 1.8mm;">Load</th>
                            <th style="padding: 1.3mm 1.8mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Buckler</td>
                            <td>+1</td>
                            <td>2</td>
                            <td>1H</td>
                            <td>1</td>
                            <td>800</td>
                        </tr>
                        <tr>
                            <td class="bold">Riot Shield</td>
                            <td>+2</td>
                            <td>4</td>
                            <td>1H</td>
                            <td>2</td>
                            <td>2,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Ballistic Shield</td>
                            <td>+3</td>
                            <td>6</td>
                            <td>1H</td>
                            <td>4</td>
                            <td>6,500</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p style="font-size: 7.9pt; line-height: 1.26; color: var(--text-muted); margin-bottom: 2mm;">
                <em>Shield Rules:</em> 1H required; adds flat Protection bonus stacking with armor. If Strength &lt; Min STR, cannot wield. No dual wielding shields.
            </p>

            <div class="example-box keep-together" style="margin-top: 1.5mm;">
                <div class="example-title">Example: Melee Combat in Action</div>
                <p>
                    <strong>The Scenario:</strong> Jax breaches an airlock occupied by a hostile pirate. Armed with a <strong>Boarding Axe</strong> (Slashing, Min STR 3, 1H, Load 2, +2 Damage Bonus), Jax attacks. Jax has <strong>Strength 5</strong>, <strong>Agility 4</strong>, and <strong>Finesse 3</strong>.
                </p>
                <p>
                    Favored pair is <strong>Agility + Strength</strong>. Strength 5 meets Min STR 3.
                </p>
                <p>
                    <strong>1. Action Roll (Strength 5):</strong> 5d10: <code>[3, 5, 7, 8, 9]</code> (Hits: 8, 9). Spends 8 on an <strong>Upgrade Effect</strong>, stepping up a Success die to <strong>d12</strong>.
                </p>
                <p>
                    <strong>2. Success Roll (Agility 4):</strong> 3d10 and 1d12: <code>[4, 6, 7]</code> on d10s and <code>9</code> on d12 = <strong>9 base Success Points</strong>.
                </p>
                <p>
                    <strong>3. Damage:</strong> Base SPs (9) + Favored Pair Bonus (Agility 4) + Weapon Bonus (+2) = <strong>15 points of damage</strong>, smashing the enforcer!
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
    # SPREAD 7 (Pages 80-81): ARMOR DEFENSE, PROPERTIES, UPGRADES & CATALOG
    # =========================================================================

    p80 = """    <!-- =========================================================================
         PAGE 80 (Spread 7 Left) — ARMOR MECHANICS, PROPERTIES & UPGRADES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-mechanics">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Armor &amp; Protective Systems</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                In the perilous expanses of the settled systems, a dependable suit of armor is often the only barrier between a Corsair and lethal trauma. Whether weathering rifle fire in a depressurized corridor, deflecting shrapnel from an explosive hull breach, or absorbing punishing melee impacts, protective gear preserves operational capability in the deadliest environments.
            </p>

            <h3>Armor Statistics Explained</h3>
            <ul>
                <li><strong>Protection:</strong> Flat integer subtracted directly from physical and kinetic damage before affecting health. Stacks with Shields (+1 to +3) and Cover (+1 to +3). An operative can wear only <strong>one suit of armor</strong> at a time.</li>
                <li><strong>Load:</strong> Mass counting against inventory capacity ($12 + \text{STR} \times 2$).</li>
                <li><strong>No Minimum Strength Requirement:</strong> Armor does not enforce a binary Strength minimum. Any operative can wear any suit of armor if they have sufficient Load capacity. However, heavier suits feature the <strong>Cumbersome (X)</strong> property.</li>
            </ul>

            <h3>Specialized Armor Properties</h3>
            <ul>
                <li><strong>Cumbersome (X):</strong> Rigid mass restricts articulation; wearer suffers <strong>X Downgrades on all Agility tests</strong> (movement rolls, acrobatics, athletics, stealth, agility attacks).</li>
                <li><strong>Hardened:</strong> Diffuses kinetic penetrators. Attacker's <strong>Crit Effect</strong> grants only <strong>+1 Success Point per Hit spent</strong> (instead of +2).</li>
                <li><strong>Blast-Dampened:</strong> Dissipates shockwaves; gain <strong>+2 Protection against Area Attacks and Explosives</strong>.</li>
                <li><strong>Tactical Harness (X):</strong> Webbing provides <strong>X dedicated Load slots</strong> for any gear; stowed items do not count against standard Load limit.</li>
                <li><strong>Muffled:</strong> Acoustic-dampening micro-weaves grant <strong>+1 Upgrade on Stealth tests</strong>.</li>
            </ul>

            <h3>Manufacturers &amp; Custom Upgrades</h3>
            <p style="font-size: 8.3pt; line-height: 1.32;">
                <strong>Chidori-Qwei:</strong> Flexible polymer garments and stealth flightsuits.<br>
                <strong>Panthera Arms:</strong> Lightweight composite plate carriers.<br>
                <strong>Vandal's Workshop:</strong> Stamped-sheet alloy hazard suits.<br>
                <strong>Caldera Foundry:</strong> Heavy cast ceramic-titanium battleplate.<br>
                <strong>Ker'Satz Korp:</strong> Industrial siege carapaces and exosuits.
            </p>
            <p>
                Suits accept up to <strong>3 Upgrade Kits</strong> (50,000 / 100,000 / 180,000 Credits):
            </p>
            <ul>
                <li><em>Reinforced Plating:</em> Increases <strong>Protection by +1</strong> (max +3 total).</li>
                <li><em>Lightweight Composites:</em> Reduces <strong>Load by 1</strong> (min 1 Load).</li>
                <li><em>Specialized Modification:</em> Adds Hardened, Blast-Dampened, Tactical Harness (+1 rating), or Muffled.</li>
            </ul>

            <div class="example-box keep-together" style="margin-top: 2mm;">
                <div class="example-title">Example: Armor in Action</div>
                <p>
                    Jax is caught in the open when a pirate opens fire with a Battle Rifle. Jax wears <strong>Tactical Battleplate</strong> (Prot 5, Load 4) and holds a <strong>Riot Shield</strong> (+2 Prot, Min STR 4, Load 2) = <strong>7 Combined Protection</strong>.
                </p>
                <p>
                    The pirate hits with 1 Crit (+2) and +4 Damage Bonus = <strong>14 damage</strong>. Jax subtracts Protection: 14 &minus; 7 = <strong>7 net damage</strong>, contained within Track I!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">80</span>
        </div>
    </div>"""
    pages.append(p80)

    p81 = """    <!-- =========================================================================
         PAGE 81 (Spread 7 Right) — COMPLETE ARMOR CATALOG (LIGHT, MEDIUM, HEAVY)
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-catalog-full">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Light Armor (Load 1–3 · Prot 2–4)</h2>
            <p style="font-size: 8.6pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Light armors provide essential protection without impeding speed, reflexes, or acrobatics; favored by pilots, scouts, and skirmishers.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Light Armor Catalog</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Armor Name</th>
                            <th style="padding: 1.3mm 1.6mm;">Prot</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Padded Flightsuit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>&mdash;</td>
                            <td>1,200</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltration Suit</td>
                            <td>2</td>
                            <td>1</td>
                            <td>Muffled</td>
                            <td>3,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Armored Jacket</td>
                            <td>3</td>
                            <td>2</td>
                            <td>&mdash;</td>
                            <td>3,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Hardened Vest</td>
                            <td>3</td>
                            <td>2</td>
                            <td>Hardened</td>
                            <td>5,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Light Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>&mdash;</td>
                            <td>10,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Spec-Ops Combat Armor</td>
                            <td>4</td>
                            <td>3</td>
                            <td>Hardened</td>
                            <td>18,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h2>Medium Armor (Load 4–5 · Prot 5–6)</h2>
            <p style="font-size: 8.6pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Frontline protection balancing heavy kinetic mitigation before full carapace penalties apply.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Medium Armor Catalog</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Armor Name</th>
                            <th style="padding: 1.3mm 1.6mm;">Prot</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>&mdash;</td>
                            <td>30,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Flak Combat Rig</td>
                            <td>5</td>
                            <td>4</td>
                            <td>Blast-Dampened</td>
                            <td>38,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Vanguard Battleplate</td>
                            <td>5</td>
                            <td>4</td>
                            <td>Hardened, Harness (1)</td>
                            <td>45,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Carapace Armor</td>
                            <td>6</td>
                            <td>5</td>
                            <td>Cumbersome (1)</td>
                            <td>65,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Bastion Carapace</td>
                            <td>6</td>
                            <td>5</td>
                            <td>Cumbersome (1), Hardened, Harness (1)</td>
                            <td>85,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h2>Heavy Armor (Load 6–7 · Prot 7–8)</h2>
            <p style="font-size: 8.6pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Walking fortresses providing total protection against small arms at the cost of mobility.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Heavy Fortress Armor</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Armor Name</th>
                            <th style="padding: 1.3mm 1.6mm;">Prot</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Breacher Carapace</td>
                            <td>7</td>
                            <td>6</td>
                            <td>Cumbersome (1), Blast-Dampened, Harness (1)</td>
                            <td>140,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Juggernaut Armor</td>
                            <td>7</td>
                            <td>6</td>
                            <td>Cumbersome (1), Hardened</td>
                            <td>160,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Titan Rig</td>
                            <td>8</td>
                            <td>7</td>
                            <td>Cumbersome (2), Hardened, Blast-Dampened, Harness (2)</td>
                            <td>280,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 7.9pt; line-height: 1.28; color: var(--text-muted); margin-top: 1mm;">
                <em>Notes:</em> Tactical Battleplate represents the peak of unencumbered military armor (no Agility Downgrades). Carapaces and Titan Rigs transform operatives into fortified anchors capable of withstanding sniper fire and explosive concussions.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">81</span>
        </div>
    </div>"""
    pages.append(p81)

    # =========================================================================
    # SPREAD 8 (Pages 82-83): TACTICAL GEAR: MOBILITY, FORTIFICATIONS & MUNITIONS
    # =========================================================================

    p82 = """    <!-- =========================================================================
         PAGE 82 (Spread 8 Left) — TACTICAL GEAR RULES & MOBILITY HARDWARE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-rules-mobility">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Tactical Gear &amp; Mobility</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                Gear encompasses specialized toolkits, refillable field rigs, and survival hardware. While weapons and armor govern basic survival, gear provides the technical leverage, vertical mobility, and utility needed to complete dangerous boarding operations.
            </p>

            <h3>Gear Rules &amp; Resolution</h3>
            <ul>
                <li><strong>Dedicated Attributes &amp; Test Pairs:</strong> Items provide specific attributes (<em>Mobility</em>, <em>Sensors</em>, <em>Medicine</em>, <em>Tinkering</em>, <em>Locksmith</em>, <em>Interfacing</em>, <em>Hacking</em>, <em>Ordnance</em>) paired with character attributes.</li>
                <li><strong>Action Point Costs:</strong> Deploying or activating gear costs <strong>1 AP</strong>.</li>
                <li><strong>Capacity &amp; Automatic Refill:</strong> Consumable casings have fixed <strong>Capacity (Cap X)</strong>. Expending charges is free; all charges automatically replenish at any supply hub or ship in downtime without tracking individual restocks.</li>
                <li><strong>Stand-Alone Explosives:</strong> Munitions do not pair with attributes; they roll pure <strong>Ordnance</strong> pools for Area Attacks.</li>
                <li><strong>Upgrades:</strong> Mechanical gear accepts up to 3 kits (-1 Load or +1 Attribute).</li>
            </ul>

            <h2>1. Mobility Gear</h2>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Mobility Hardware</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Item</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Light Jump-Pack</td>
                            <td>Jetpack (8m), Mobility 3</td>
                            <td>3</td>
                            <td>35,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Jetpack</td>
                            <td>Jetpack (12m), Mobility 4</td>
                            <td>4</td>
                            <td>72,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Jump-Rig</td>
                            <td>Jetpack (16m), Mobility 5</td>
                            <td>5</td>
                            <td>120,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Gecko Climbing Kit</td>
                            <td>Mobility 3, Surface Adhesion</td>
                            <td>1</td>
                            <td>15,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Zipline</td>
                            <td>Zipline (40m), 24 HP</td>
                            <td>3</td>
                            <td>15,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Standard Grapple</td>
                            <td>Grapple (8m), Mobility 3, Cap 3</td>
                            <td>2</td>
                            <td>5,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Grapple</td>
                            <td>Grapple (16m), Mobility 4, Cap 4</td>
                            <td>2</td>
                            <td>12,000</td>
                        </tr>
                        <tr>
                            <td class="bold">High-Tensile Rope</td>
                            <td>Utility Cordage (40m)</td>
                            <td>1</td>
                            <td>100</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Mobility Special Properties</h3>
            <ul>
                <li><strong>Jetpack (Xm):</strong> 1 AP, Success Test using <strong>Mobility + Agility</strong>. Flight speed equals base (Xm) + 1m per Success Point. Ignore difficult terrain and falling damage. <em>Vector Boost (Crit):</em> Spending a Hit grants <strong>+4m movement</strong> instead of +2 SPs. <em>Charging:</em> Spend 1 AP to fly base speed in a straight line and execute a Melee Attack.</li>
                <li><strong>Surface Adhesion:</strong> 1 AP, Success Test using <strong>Mobility + Strength</strong>. Adhere to sheer/inverted hulls; climb 8m + 1m per SP.</li>
                <li><strong>Grapple (Xm):</strong> 1 AP, expends 1 Charge. Solid terrain: automatic pull to anchor. Hostiles: Complex Test using <strong>Mobility + Strength</strong>; each Hit spent triggers a <strong>Push Effect</strong> pulling target 1 space toward user. User may advance along line or deal SPs as damage.</li>
                <li><strong>Zipline (40m):</strong> Launch motorized cable (1 AP). Traversed as standard movement by any creature; reel in for 1 AP.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">82</span>
        </div>
    </div>"""
    pages.append(p82)

    p83 = """    <!-- =========================================================================
         PAGE 83 (Spread 8 Right) — FORTIFICATIONS & HEAVY ORDNANCE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortification-explosives">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">2. Fortification Gear</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Instant defensive barriers, automated point defense, and remote weapon platforms.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Fortifications &amp; Turrets</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Item</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Deployable Cover (Light)</td>
                            <td>Light Cover (+1), 12 HP, Innate Prot 4</td>
                            <td>2</td>
                            <td>5,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Medium)</td>
                            <td>Medium Cover (+2), 24 HP, Innate Prot 8</td>
                            <td>3</td>
                            <td>8,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Deployable Cover (Heavy)</td>
                            <td>Heavy Cover (+3), 36 HP, Innate Prot 12</td>
                            <td>4</td>
                            <td>12,000</td>
                        </tr>
                        <tr>
                            <td class="bold">APS Beacon</td>
                            <td>Intercept 5, Reaction Defense, 24 HP</td>
                            <td>3</td>
                            <td>25,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Smartpod Mount</td>
                            <td>Automount 3, 12 HP</td>
                            <td>3</td>
                            <td>36,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 2mm;">
                <strong>Deployable Cover:</strong> Deploy/pack (1 AP). Occupies 1 space, grants cover bonus (+1 to +3), degraded 1 Prot per 12 dmg.<br>
                <strong>APS Beacon:</strong> 1 Free Reaction AP per round; rolls pure <strong>Intercept 5</strong> to contest incoming Area Attacks/grenades, destroying them mid-air on 8+.<br>
                <strong>Automount (X):</strong> 1 AP deploy/mount. Fire remotely for 1 AP rolling <strong>Automount + Finesse</strong>.
            </p>

            <h2>3. Explosives &amp; Launchers</h2>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Explosives &amp; Launchers</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Item</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Grenade Rig</td>
                            <td>Capacity 3, Refillable, Choice at Use</td>
                            <td>2</td>
                            <td>4,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Grenade Rig</td>
                            <td>Capacity 5, Refillable, Choice at Use</td>
                            <td>3</td>
                            <td>10,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Demolitions Rig</td>
                            <td>Capacity 2, Refillable, Choice at Use</td>
                            <td>3</td>
                            <td>8,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Siege Demolitions Rig</td>
                            <td>Capacity 4, Refillable, Choice at Use</td>
                            <td>4</td>
                            <td>16,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Grenade Launcher Rig</td>
                            <td>Delivery (Medium Range)</td>
                            <td>2</td>
                            <td>6,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Rocket Launcher Rig</td>
                            <td>Delivery (Long Range)</td>
                            <td>4</td>
                            <td>22,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Missile Guidance Tube</td>
                            <td>Delivery (Extreme Range)</td>
                            <td>6</td>
                            <td>60,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Munition Profiles &amp; Properties</h3>
            <ul>
                <li><strong>Frag:</strong> <strong>Ordnance 4, Blast 3, 8m Radius.</strong> Anti-personnel shrapnel.</li>
                <li><strong>Flashbang:</strong> <strong>Ordnance 5, Area Stun, 4m Radius.</strong> Hostiles discard highest die next roll for each 8+.</li>
                <li><strong>Smoke:</strong> <strong>Area Obscurance, 8m Radius.</strong> Fills area with thermal smoke without rolling; blocks line of sight.</li>
                <li><strong>HE Munition:</strong> <strong>Ordnance 5, Blast 5, 4m Radius.</strong> Concussion charge.</li>
                <li><strong>Demolition Charge:</strong> <strong>Ordnance 7, Blast 5, 12m Radius, Remote.</strong> Breaching block triggered as Triggered Effect.</li>
                <li><strong>Ordnance Rules:</strong> Throwing/firing costs 1 AP (Short Range; launcher extends range). Rolls pure <strong>Ordnance</strong>. <strong>Blast (X):</strong> Crits add <strong>+X damage</strong> per Hit.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">83</span>
        </div>
    </div>"""
    pages.append(p83)

    # =========================================================================
    # SPREAD 9 (Pages 84-85): MEDICAL, TECH, SURVEILLANCE & SURVIVAL
    # =========================================================================

    p84 = """    <!-- =========================================================================
         PAGE 84 (Spread 9 Left) — MEDICAL SUITES, STIMULANTS & INFILTRATION KITS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-medical-tech">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Medical, Tech &amp; Utility</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">4. Medical &amp; Consumables</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Field triage suites and biochemical performance injectors operating on refillable casings.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Medical Kits &amp; Injectors</div>
                <table class="rules-table" style="font-size: 7.9pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.5mm;">Item</th>
                            <th style="padding: 1.2mm 1.5mm;">Properties</th>
                            <th style="padding: 1.2mm 1.5mm;">Load</th>
                            <th style="padding: 1.2mm 1.5mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Field Medi-Kit</td>
                            <td>Medicine 3, Cap 3, Lesser Physical (1/2)</td>
                            <td>1</td>
                            <td>2,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Trauma Rig</td>
                            <td>Medicine 4, Cap 4, Lesser Physical (1/1)</td>
                            <td>2</td>
                            <td>7,500</td>
                        </tr>
                        <tr>
                            <td class="bold">Phoenix Reconstructor</td>
                            <td>Medicine 4, Cap 2, Greater Physical (1/1)</td>
                            <td>2</td>
                            <td>15,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Inhaler</td>
                            <td>Medicine 3, Cap 3, Lesser Mental (1/2)</td>
                            <td>1</td>
                            <td>2,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Neuro-Rig</td>
                            <td>Medicine 4, Cap 4, Lesser Mental (1/1)</td>
                            <td>2</td>
                            <td>6,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Stim Injector</td>
                            <td>Capacity 3, Refillable, Stim Choice</td>
                            <td>1</td>
                            <td>5,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Chem-Rig</td>
                            <td>Capacity 5, Refillable, Stim Choice</td>
                            <td>2</td>
                            <td>12,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Medical &amp; Stimulant Properties</h3>
            <ul>
                <li><strong>Medicine (X) Triage:</strong> 1 AP, 1 Charge, <strong>Medicine + Knowledge</strong>. Restores 1 segment per X SPs. <em>Greater Healing:</em> Clears Aggravated damage at 2X SPs per segment.</li>
                <li><strong>Stimulant Formulas:</strong> 1 AP, 1 Charge (Volatile 2, Fleeting until round end):
                    <ul>
                        <li><em>Roid (+1 Strength):</em> Muscular leverage surge.</li>
                        <li><em>Nitro (+1 Agility):</em> Adrenaline boost for sprint/evasion.</li>
                        <li><em>Edgedance (+1 Finesse):</em> Micro-precision motor boost.</li>
                        <li><em>SharpX (+1 Instinct):</em> Cortex alertness stimulant.</li>
                        <li><em>Cognita (+1 Knowledge):</em> Nootropic tactical accelerator.</li>
                        <li><em>Rizz (+1 Presence):</em> Pheromonal vocal poise enhancer.</li>
                    </ul>
                </li>
                <li><strong>Volatile (X):</strong> User suffers <strong>X unmitigated damage</strong> upon injection. Stacking stings deals extra damage equal to active substances.</li>
            </ul>

            <h2>5. Infiltration &amp; Tech Kits</h2>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Infiltration Rigs &amp; Cyberdecks</div>
                <table class="rules-table" style="font-size: 7.9pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.5mm;">Item</th>
                            <th style="padding: 1.2mm 1.5mm;">Properties</th>
                            <th style="padding: 1.2mm 1.5mm;">Load</th>
                            <th style="padding: 1.2mm 1.5mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Mechanic's Kit</td>
                            <td>Tinkering 2, Locksmith 2</td>
                            <td>2</td>
                            <td>1,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Engineer's Kit</td>
                            <td>Tinkering 4, Locksmith 4</td>
                            <td>2</td>
                            <td>12,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Maker's Kit</td>
                            <td>Tinkering 6, Locksmith 6</td>
                            <td>2</td>
                            <td>25,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Infiltrator Kit</td>
                            <td>Disguise 2, Forgery 2</td>
                            <td>2</td>
                            <td>1,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Spy Kit</td>
                            <td>Disguise 4, Forgery 4</td>
                            <td>3</td>
                            <td>12,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Chameleon Kit</td>
                            <td>Disguise 6, Forgery 6</td>
                            <td>3</td>
                            <td>25,000</td>
                        </tr>
                        <tr>
                            <td class="bold">"Spider" Deck</td>
                            <td>Interfacing 3, Hacking 2</td>
                            <td>2</td>
                            <td>1,000</td>
                        </tr>
                        <tr>
                            <td class="bold">"Mantis" Deck</td>
                            <td>Interfacing 5, Hacking 4</td>
                            <td>3</td>
                            <td>12,000</td>
                        </tr>
                        <tr>
                            <td class="bold">"Scorpion" Deck</td>
                            <td>Interfacing 7, Hacking 6</td>
                            <td>3</td>
                            <td>25,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 7.8pt; line-height: 1.26; margin-top: 1mm;">
                <strong>Tinkering:</strong> Traps/repairs (Tinkering + Knowledge). <strong>Locksmith:</strong> Locks/latches (Locksmith + Finesse). <strong>Disguise:</strong> Personas (Disguise + Knowledge). <strong>Forgery:</strong> Passes (Forgery + Finesse). <strong>Interfacing:</strong> Nodes/consoles (Interfacing + Knowledge). <strong>Hacking:</strong> ICE/firewalls (Hacking + Knowledge).
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">84</span>
        </div>
    </div>"""
    pages.append(p84)

    p85 = """    <!-- =========================================================================
         PAGE 85 (Spread 9 Right) — SURVEILLANCE & SURVIVAL UTILITY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-surveillance-survival">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">6. Detection &amp; Surveillance</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Sensors, radar suites, and autonomous drones reveal hidden hostiles and map hostile installations.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Surveillance &amp; Reconnaissance</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Item</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Proximity Sensor</td>
                            <td>Scouting 4m, Automated Alert, Remote</td>
                            <td>1/2</td>
                            <td>1,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Proximity Radar</td>
                            <td>Scouting 20m, 360-Degree Sweep</td>
                            <td>2</td>
                            <td>25,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Recon Drone</td>
                            <td>Fly 20m, Sensors 2, Remote Control</td>
                            <td>2</td>
                            <td>35,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Forensic Suite</td>
                            <td>Sensors 4, Chemical &amp; Ballistic Scan</td>
                            <td>3</td>
                            <td>20,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Surveillance Properties</h3>
            <ul>
                <li><strong>Sensors (X):</strong> Active scanning for hidden hostiles or analyzing toxic hazards costs <strong>1 AP</strong> and uses <strong>Sensors + Knowledge</strong>.</li>
                <li><strong>Scouting (Xm):</strong> Passive automated detection radius. Any creature moving within X meters triggers an instant alert unless electronically cloaked.</li>
                <li><strong>Remote Control:</strong> Piloting a drone costs <strong>1 AP</strong>; drones fly up to 20m/round and conduct active sweeps with onboard Sensors.</li>
            </ul>

            <h2>7. Survival &amp; Field Utility</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Provisions, pressurized suits, and communications for deep-space and planetary excursions.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Survival &amp; Utility Gear</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.3mm 1.6mm;">Item</th>
                            <th style="padding: 1.3mm 1.6mm;">Properties</th>
                            <th style="padding: 1.3mm 1.6mm;">Load</th>
                            <th style="padding: 1.3mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Thermal Hazard Suit</td>
                            <td>Environmental Immunity, Sealed</td>
                            <td>1</td>
                            <td>5,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Field Rations (1 Wk)</td>
                            <td>Sustenance</td>
                            <td>1</td>
                            <td>50</td>
                        </tr>
                        <tr>
                            <td class="bold">Survival Camp</td>
                            <td>Squad Shelter (4 Persons)</td>
                            <td>4</td>
                            <td>500</td>
                        </tr>
                        <tr>
                            <td class="bold">Tactical Commlink</td>
                            <td>Interfacing 2, Long-Range Comm</td>
                            <td>0</td>
                            <td>1,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Survival Properties</h3>
            <ul>
                <li><strong>Environmental Immunity:</strong> Immune to extreme temperatures (&minus;150&deg;C to +200&deg;C), toxins, and vacuum exposure for up to 12 hours.</li>
                <li><strong>Long-Range Comm:</strong> Orbital voice/data broadcast; decryption tests use <strong>Interfacing + Knowledge</strong>.</li>
                <li><strong>Squad Shelter &amp; Sustenance:</strong> Prevents exhaustion and starvation during prolonged planetary excursions.</li>
            </ul>

            <div class="callout callout-cyan keep-together" style="margin-top: 1.5mm; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 9.5pt;">Logistical Preparedness</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    Vacuum exposure is unforgiving. A Corsair cell venturing onto an airless asteroid without sealed hazard suits and commlinks risks total mission failure from a single breached visor.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">85</span>
        </div>
    </div>"""
    pages.append(p85)

    # =========================================================================
    # SPREAD 10 (Pages 86-87): EXOTIC HARDWARE RULES & 4-TIER RARITY LADDER
    # =========================================================================

    p86 = """    <!-- =========================================================================
         PAGE 86 (Spread 10 Left) — EXOTIC HARDWARE: SKUNKWORKS & PRECURSOR RELICS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-hardware-rules">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Exotic Hardware</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Exotic Hardware</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 1.8mm;">
                In the commercial bazaars and scrap-alleys of the Sphere, money can buy you a great many things. A modest stack of Flotilla Credits will purchase a dependable pump shotgun that smells faintly of machine oil, a suit of reinforced ballistic weave that might keep your ribs inside your chest when an Ork marine kicks you through a bulkhead, or a pair of magnetic boots that only fail three percent of the time. These are the workhorse tools of Newcomer civilization: mass-produced, thoroughly documented, and priced so that a greenhorn Corsair cell doesn't bankrupt their sponsor on week two.
            </p>
            <p>
                And then there is the other stuff.
            </p>
            <p>
                Exotic Hardware refers to the narrow, intoxicating, and thoroughly lethal category of equipment that exists far beyond standard military procurement. These are the crown jewels of black-budget corporate skunkworks, un-cataloged prototypes liberated from clandestine research labs on Nimbus, and terrifying, cold-glass relics dragged kicking and screaming from subterranean Precursor vaults. In the lexicon of ancient fantasy tabletop games, they are the "magic items" of Corsair—objects possessing properties that seem to bend the rules of engagement.
            </p>
            <p>
                Yet in accordance with the fundamental laws of the Sphere, there is no magic here. Every prototype operates on bleeding-edge physics, extreme thermal shunting, and precision mechanical engineering. Every Precursor relic is a solid-state transducer tapping into the diffuse dark matter halo engineered by the Singularity. They are rare, exorbitantly expensive, and carried only by veterans who have both the coin to afford them and the physical constitution to carry their crushing weight.
            </p>

            <h3>The Rules of Exotic Hardware</h3>
            <ol style="margin-left: 3.5mm; margin-bottom: 2mm; font-size: 8.2pt; line-height: 1.30;">
                <li><strong>Load Taxation Over Arbitrary Limits:</strong> There is no mystical "attunement" ceiling in Corsair. An operative can carry as many pieces of Exotic Hardware as their spine can endure. However, exotic hardware carries heavy <strong>Load (typically Load 2 to 5)</strong>. Packing multiple exotic systems forces agonizing logistical tradeoffs against field rations, medical rigs, and armor.</li>
                <li><strong>Action Point Economy:</strong> Activating an exotic function costs <strong>1 Action Point (AP)</strong> or integrates into an existing 1-AP combat action. Passive systems apply continuously, but active bursts always demand dedicated tactical focus.</li>
                <li><strong>Pacing Cooldowns &amp; Thermal Cycles:</strong> Prototypes generate severe thermal spikes. Cooldowns align with narrative pacing:
                    <ul>
                        <li><em>Moment-to-Moment:</em> Recovers after <strong>1 combat round</strong> (~5–10s), resetting at the start of your next turn.</li>
                        <li><em>Place-to-Place:</em> Recovers after <strong>1 transit round</strong> (~1 hour) via coolant flush or ship heat sinks.</li>
                        <li><em>Day-to-Day:</em> Recovers after a <strong>24-hour downtime cycle</strong> with workshop recalibration.</li>
                    </ul>
                </li>
                <li><strong>Irreplaceable Maintenance:</strong> Reduced to 0 HP, prototypes require a dedicated workshop and a successful <strong>Tinkering + Knowledge</strong> test against Tier DC. Precursor relics cannot be repaired by mortal tools without rare molecular salvage or Ancestral favor.</li>
                <li><strong>Non-Customizable Architecture:</strong> Exotic hardware <strong>cannot accept standard Upgrade Kits</strong>. Machining attempts ruin their atomic harmonic calibration; stats and Load are permanently fixed as written.</li>
            </ol>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">86</span>
        </div>
    </div>"""
    pages.append(p86)

    p87 = """    <!-- =========================================================================
         PAGE 87 (Spread 10 Right) — 4-TIER RARITY LADDER & ACQUISITION REALITY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-rarity-ladder">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Exotic Hardware</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">The 4-Tier Rarity &amp; Economic Ladder</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.34; margin-bottom: 1.8mm;">
                To prevent market confusion and establish clear campaign progression, Exotic Hardware is organized into four distinct tiers of rarity, cost, and availability:
            </p>

            <div class="table-container keep-together" style="margin: 2mm 0;">
                <div class="table-header">Exotic Hardware Rarity &amp; Economic Ladder</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.6mm;">Tier</th>
                            <th style="padding: 1.4mm 1.6mm;">Classification</th>
                            <th style="padding: 1.4mm 1.6mm;">Cost (Credits)</th>
                            <th style="padding: 1.4mm 1.6mm;">Market Reality &amp; Procurement</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tier 1</td>
                            <td>Mil-Spec Skunkworks</td>
                            <td>15,000–30,000</td>
                            <td>Limited-run military trials and high-spec foundry prototypes (Caldera Foundry, Port Zenith, Panthera Arms). Available through high-end corporate fixers, retired veteran armories, or wealthy colonial sponsors.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 2</td>
                            <td>Classified Prototypes</td>
                            <td>40,000–80,000</td>
                            <td>Bleeding-edge corporate espionage targets, hybrid alien polymers, and experimental cybernetic field rigs. Heavily guarded; acquired through black-site heists or high-threat unsanctioned contracts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 3</td>
                            <td>Precursor Relics</td>
                            <td>100,000–250,000</td>
                            <td>Intact alien artifacts, non-baryonic catalytic lattices, and self-repairing alloys recovered from deep Vault excavations. Strictly contraband under Covenant Accords; traded in deep-underworld syndicates.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 4</td>
                            <td>Singularities &amp; Wonders</td>
                            <td>Priceless</td>
                            <td>Mythic, one-of-a-kind artifacts of campaign-defining significance (intact dreadnought cores, null-beams). Found exclusively as major campaign milestones or climactic salvage objectives.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Operational Acquisition &amp; Market Realities</h3>
            <p>
                Starting characters cannot afford Exotic Hardware. Even mid-tier operatives must weigh the strategic value of an experimental plasma-arc cutter against the recurring operating runway of fuel, rations, and ammunition for their starship.
            </p>
            <ul>
                <li><strong>Black Market Infiltration:</strong> Acquiring Tier 2 prototypes often places the crew on corporate kill-lists, prompting retaliatory asset recovery teams.</li>
                <li><strong>Covenant Accords Violations:</strong> Possessing unregistered Precursor relics triggers severe legal penalties across Sovereign jurisdictions, forcing cells into fringe underworld brokerages.</li>
            </ul>

            <div class="callout callout-cyan keep-together" style="margin-top: 2mm; padding: 2.5mm 3.5mm;">
                <div class="callout-title" style="font-size: 9.5pt;">Campaign Integration</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    Game Masters and players can author bespoke prototypes and relics for their campaigns using the guidelines and balancing invariants documented in the Exotic Equipment Design reference. Exotic systems should always offer distinctive tactical choices rather than simple numerical bloat.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">87</span>
        </div>
    </div>"""
    pages.append(p87)

    full_html = f"""<!DOCTYPE html>
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

{chr(10).join(pages)}

</body>
</html>
"""

    out_path = Path("html/04_Armory_and_Gear.html")
    out_path.write_text(full_html, encoding="utf-8")
    print(f"Successfully generated {out_path} with {len(pages)} pages (Pages 68 to 87).")

if __name__ == "__main__":
    build_full_fidelity_ch04()
