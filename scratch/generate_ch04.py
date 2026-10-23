# -*- coding: utf-8 -*-
"""
Generate html/04_Armory_and_Gear.html for Corsair TTRPG Core Rulebook.
Covers:
- rulebook/combat/Combat.md
- rulebook/equipment/Equipment.md
- rulebook/equipment/Firearms.md
- rulebook/equipment/Melee.md
- rulebook/equipment/Armor.md
- rulebook/equipment/Gear.md
- rulebook/equipment/Exotic_Hardware.md

Pages: 68 to 91 (24 pages, 12 spreads).
Strict verbatim fidelity, zero <a> tags, zero sci-fi telemetry tags, print-ready A4.
"""

from pathlib import Path

def generate_chapter_04():
    pages = []

    # =========================================================================
    # PAGE 68 (Spread 1 Left) — CHAPTER 04 OPENER: COMBAT & TACTICAL MOVEMENT
    # =========================================================================
    p68 = """    <!-- =========================================================================
         PAGE 68 (Spread 1 Left) — CHAPTER 04 OPENER: COMBAT & TACTICAL MOVEMENT
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="chapter-04">
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
            <p class="lead" style="font-size: 9.2pt; line-height: 1.40; margin-bottom: 2.2mm;">
                In the world of Corsair, conflict is inevitable. Whether facing down a squad of corporate enforcers, battling a monstrous alien in the depths of a derelict ship, or engaging in a desperate firefight across depressurized docking gantries, combat is a thrilling and dangerous reality of high-frontier survival.
            </p>
            <p>
                When a conflict turns violent and every second matters, the game shifts into <strong>Moment to Moment</strong> pacing. While you can resolve skirmishes using "theater of the mind," employing a grid-based battle map adds tactical clarity to positioning, cover, and engagement lines.
            </p>

            <h3>Movement</h3>
            <p>
                Navigating the battlefield is crucial for survival. Positioning determines cover angles, line of sight, and your ability to engage or evade foes.
            </p>
            <p>
                In combat, you can spend <strong>1 Action Point (AP)</strong> to move. When you move, you perform a <strong>Success Test</strong>, typically with <strong>Agility</strong>, then move a number of meters equal to the result plus your base speed (by default, <strong>4 meters</strong>).
            </p>
            <p>
                The Success Test is typically made with your <strong>Agility</strong> attribute, representing your ability to sprint, vault, and clear terrain. The GM may call for a different attribute based on physical context (such as <strong>Strength</strong> for scaling a sheer cliff).
            </p>

            <h3>Movement on a Grid</h3>
            <p>
                For ease of play, use a battle grid with squares or hexes representing a <strong>4-meter diameter space</strong>. On a grid, movement is calculated as follows:
            </p>
            <ul>
                <li>Your base speed of 4 meters translates to <strong>1 space</strong>.</li>
                <li>Your Success Test adds additional movement: divide the number of meters rolled on your test by four, rounding up, and move an additional number of spaces equal to the result.</li>
            </ul>
            <p>
                A single move action covers a maximum of 16 meters (4 spaces). Because an operative can spend multiple Action Points on movement, potential distances covered in a round can be significant.
            </p>

            <h3>Verticality</h3>
            <p>
                Battlefields are three-dimensional. When verticality is introduced, model it by layering horizontal grids separated by <strong>2 meters</strong>. Moving up and down between vertical layers is always considered <strong>Difficult Terrain</strong>—unless you fall.
            </p>
            <p>
                When you fall more than 2 meters, you take damage equal to <strong>three times the number of meters fallen</strong>. This falling damage is kinetic trauma and is <strong>not reduced by Protection</strong>. Stories in an orbital habitat roughly correspond to vertical layers.
            </p>

            <h3>Flying</h3>
            <p>
                Flight allows an operative to move through three-dimensional air as if on solid ground. Ascending costs double: ascending 2 meters consumes 4 meters of movement. Moving downward or horizontally uses movement normally. Flying creatures completely <strong>ignore Difficult Terrain</strong>.
            </p>
            <p>
                During the turn you lose flight, you remain suspended until the end of the turn, falling at turn's end and taking falling damage if above 2 meters.
            </p>

            <h3>Difficult Terrain</h3>
            <p>
                Hindered ground—such as knee-deep slurry, dense wreckage, or active coolant vents—costs <strong>2 meters of speed for every 1 meter of progress</strong>. Moving into a difficult space costs <strong>8 meters</strong> (2 spaces of movement). This penalty also applies when vaulting barricades or scrambling up ledges.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">68</span>
        </div>
    </div>"""
    pages.append(p68)

    # =========================================================================
    # PAGE 69 (Spread 1 Right) — CONTESTING MOVEMENT & SPACE OCCUPANCY
    # =========================================================================
    p69 = """    <!-- =========================================================================
         PAGE 69 (Spread 1 Right) — CONTESTING MOVEMENT & SPACE OCCUPANCY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="contesting-movement">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Movement</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Contesting Movement</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Movement is not always unopposed. A defender can attempt to physically intercept, tackle, or trip a creature trying to push past them.
            </p>
            <p>
                When a creature's path takes them through a space occupied by a hostile character, that character can choose to contest the movement using the standard contest rules:
            </p>
            <ol style="margin-left: 3.5mm; margin-bottom: 2.5mm; font-size: 8.4pt; line-height: 1.34;">
                <li><strong>The Contester Narrates:</strong> The defender describes their interception (e.g., body-checking, grabbing clothing, or sweeping legs).</li>
                <li><strong>The GM Chooses an Attribute:</strong> The GM selects a relevant Attribute for the contest, such as <strong>Strength</strong> to grapple or <strong>Agility</strong> to trip.</li>
                <li><strong>The Contest Roll:</strong> The contester rolls a dice pool equal to their chosen Attribute.</li>
                <li><strong>Eliminating Dice:</strong> For each success (8+) on the contest roll, the contester eliminates one of the highest dice from the runner's movement Success Test. If no dice showing 8+ remain, the moving creature is immediately stopped and stuck in the contester's space.</li>
            </ol>

            <div class="example-box keep-together">
                <div class="example-title">Tactical Contest: Stopping Jax</div>
                <p>
                    <strong>The Scenario:</strong> Jax attempts to sprint past a burly corporate enforcer to reach an airlock control panel. Jax spends 1 AP on a move action and rolls an <strong>Agility 4</strong> Success Test, rolling <code>[9, 7, 5, 2]</code>. The highest die is 9, granting Jax his base 1 space plus 2 extra spaces (9 meters &divide; 4, rounded up = 3 spaces total).
                </p>
                <p>
                    The enforcer stands along Jax's path and declares a contest.
                </p>
                <p>
                    <strong>1. The Contest Roll:</strong> The enforcer has <strong>Strength 5</strong> and lunges to bear-hug Jax. The enforcer rolls 5d10: <code>[10, 8, 6, 4, 1]</code>—two successes (10 and 8).
                </p>
                <p>
                    <strong>2. Eliminating Dice:</strong> The enforcer's two successes eliminate the two highest dice from Jax's movement roll (the 9 and 7).
                </p>
                <p>
                    <strong>3. Final Outcome:</strong> Jax's remaining pool is <code>[5, 2]</code>. Because no dice showing 8+ remain, the contest succeeds completely. Jax's sprint ends dead in the enforcer's space, stopped in his tracks before reaching the console.
                </p>
            </div>

            <h2>Space and Occupancy</h2>
            <p>
                Combat in Corsair is dynamic and claustrophobic. A single 4&times;4 meter grid space is not limited to a single combatant. A standard space comfortably accommodates up to <strong>4 standard-sized creatures</strong>.
            </p>
            <p>
                Many actions—especially hand-to-hand melee attacks, point-blank medical triage, and close teamwork maneuvers—require operatives to occupy the same space.
            </p>

            <h3>Outnumbering</h3>
            <p>
                Ganging up on an isolated foe is an effective tactical doctrine. When you and your allies outnumber hostile combatants within a single space, you gain a decisive melee advantage.
            </p>
            <p>
                You receive a number of <strong>Upgrades</strong> on melee attack tests equal to the difference between allied and hostile creatures in that space. For example, if 3 Corsairs crowd a space with 1 syndicate enforcer, all 3 Corsairs receive <strong>2 Upgrades</strong> (3 &minus; 1 = 2) on their melee strikes against that enforcer.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">69</span>
        </div>
    </div>"""
    pages.append(p69)

    # =========================================================================
    # PAGE 70 (Spread 2 Left) — MELEE ENGAGEMENT, SIZES & CQC
    # =========================================================================
    p70 = """    <!-- =========================================================================
         PAGE 70 (Spread 2 Left) — MELEE ENGAGEMENT, SIZES & CQC
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-and-cqc">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Close Quarters Combat</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Engagement</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                You can attack a creature in the same space as you, or an adjacent space. Hand-to-hand combat requires combining two separate Physical Attributes.
            </p>
            <p>
                For example, an operative might combine <strong>Strength + Agility</strong> to drive a boarding axe through reinforced body armor, or pair <strong>Agility + Finesse</strong> when slipping a vibro-blade into a visor gasket.
            </p>
            <p>
                When attacking a creature in an adjacent space, you automatically move into that space, provided it currently holds fewer than 4 creatures. If the target space is already full, you resolve the attack from your current space, but calculate <strong>Outnumbering Upgrades</strong> as if you and all allies in your space were inside the defender's space.
            </p>

            <h3>Creature Size</h3>
            <p>
                Not all combatants share standard human proportions. The capacity of a 4&times;4m space is dictated by biological mass:
            </p>
            <ul>
                <li><strong>Standard Creatures:</strong> Humans, Elves, Dwarves, and typical humanoids. 1 capacity slot each (up to 4 per space).</li>
                <li><strong>Large Creatures:</strong> Heavy war-drones, armored Ogres, and biological brutes. Each occupies the capacity of <strong>2 standard creatures</strong> (maximum 2 per space).</li>
                <li><strong>Huge Creatures:</strong> Light utility shuttles, apex alien predators, and combat walkers. Each fills an entire space, taking up the capacity of <strong>4 standard creatures</strong>.</li>
            </ul>
            <p>
                Massive entities extending across multiple spaces count as Large or Huge in each space their frame touches for occupancy and targeting.
            </p>

            <h2>Close Quarters Combat (CQC)</h2>
            <p>
                When you share a grid space with an active hostile creature, you are locked in <strong>Close Quarters Combat (CQC)</strong>. This chaotic state severely disrupts firearms handling:
            </p>
            <ul>
                <li><strong>Firing in CQC:</strong> Attempting to discharge a ranged weapon while sharing a space with a hostile imposes <strong>2 Downgrades</strong> on the attack test. Wrestling for weapon alignment under point-blank physical pressure makes accurate fire extremely difficult.</li>
                <li><strong>Firing into CQC:</strong> Firing from an outside space into a melee where allies and hostiles are interlocked imposes <strong>1 Downgrade</strong> on the attack test to reflect the risk of hitting friendly targets.</li>
            </ul>

            <h2>Cover</h2>
            <p>
                Taking cover is essential for surviving high-velocity kinetic firefights. Sturdy bulkheads, cargo containers, and machinery provide flat damage mitigation:
            </p>
            <p>
                Cover provides a flat bonus to <strong>Protection</strong> that stacks with worn armor, reducing incoming damage before it harms health. This bonus applies only against attacks originating from <em>outside</em> the defender's space:
            </p>
            <ul>
                <li><strong>Light Cover (+1 Protection):</strong> Partial concealment, such as narrow pipes or light furniture.</li>
                <li><strong>Medium Cover (+2 Protection):</strong> Solid waist-high barriers, such as engine blocks or reinforced crates.</li>
                <li><strong>Heavy Cover (+3 Protection):</strong> Impassable fortified barricades, reinforced bulkheads, or stone bunkers.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""
    pages.append(p70)

    # =========================================================================
    # PAGE 71 (Spread 2 Right) — COVER DESTRUCTION & COVER FACING
    # =========================================================================
    p71 = """    <!-- =========================================================================
         PAGE 71 (Spread 2 Right) — COVER DESTRUCTION & COVER FACING
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="cover-mechanics">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Combat Cover</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Destroying Cover</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Cover is not invulnerable. Sustained ballistic fire, explosive detonations, and heavy breaching weapons can pulverize defensive positions.
            </p>
            <p>
                Light, Medium, and Heavy Cover possess <strong>12, 24, and 36 Health Points (HP)</strong> and an innate Protection rating of <strong>4, 8, and 12</strong> respectively when directly targeted:
            </p>
            <ul>
                <li>Attacking cover is resolved as a <strong>Success Test</strong> rather than a Complex Test.</li>
                <li>For every <strong>12 points of damage</strong> the cover absorbs, its defensive Protection bonus is permanently reduced by 1.</li>
                <li>Specialized breaching charges, anti-materiel rifles, and demolition munitions specifically <strong>ignore cover's innate Protection</strong>.</li>
            </ul>

            <div class="table-container keep-together">
                <div class="table-header">Cover Defensive &amp; Structural Ratings</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Cover Tier</th>
                            <th>Bonus Prot</th>
                            <th>Cover HP</th>
                            <th>Innate Prot</th>
                            <th>Degrade Threshold</th>
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
                Utilizing cover is about directional angling. The first time you are attacked in a round where you would benefit from cover, draw a straight line from the attacker to your position:
            </p>
            <p>
                Whichever side of your space that line crosses becomes your <strong>covering side</strong>. This establishes which flank of the physical obstacle you are bracing behind. If the attack line crosses an exact corner, both adjacent sides become covering sides.
            </p>
            <p>
                On any subsequent attacks during the combat round:
            </p>
            <ul>
                <li><strong>Full Bonus:</strong> If the line of attack crosses your covering side, you receive the full Protection bonus.</li>
                <li><strong>Reduced Bonus:</strong> If the line of attack crosses a side <em>adjacent</em> to the covering side, the Protection bonus is reduced by <strong>1 on a hex grid</strong> and by <strong>2 on a square grid</strong>.</li>
                <li><strong>No Bonus (Exposed):</strong> If the line of attack crosses a side <em>not adjacent</em> to the covering side (your rear or open flank), you gain no benefit from the cover. You are considered fully exposed.</li>
            </ul>

            <div class="callout callout-amber keep-together">
                <div class="callout-title">Tactical Flanking Doctrine</div>
                <p>
                    Because cover is directional, an entrenched squad cannot protect all angles simultaneously. Coordinated fire teams should pin enemies behind cover from one flank while mobile operatives maneuver along perpendicular axes to deny cover bonuses entirely.
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
    # PAGE 72 (Spread 3 Left) — THE ARMORY & LOAD CAPACITY
    # =========================================================================
    p72 = """    <!-- =========================================================================
         PAGE 72 (Spread 3 Left) — THE ARMORY & LOAD CAPACITY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="the-armory-load">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: The Armory &amp; Load</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">The Armory &amp; Logistics</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Not every item carried by an operative has mechanical significance. Everyday belongings like commlinks, hab keys, or trinkets are assumed gear. Items providing tangible tactical advantages—weapons, armor, sensor suites, and tech kits—are governed by the <strong>Load system</strong>.
            </p>

            <h3>Load Capacity</h3>
            <p>
                Every piece of equipment has a <strong>Load</strong> value reflecting its mass, bulk, and encumbrance. Carrying capacity is strictly limited by physical conditioning:
            </p>
            <div class="callout callout-cyan keep-together" style="margin: 2.5mm 0;">
                <div class="callout-title">Maximum Load Invariant</div>
                <p style="font-size: 9.5pt; font-weight: 700; text-align: center; margin: 0;">
                    \text{Maximum Load Capacity} = 12 + (\text{Strength} \times 2)
                </p>
            </div>
            <p>
                This limit is absolute; an operative cannot carry gear exceeding this capacity under any circumstances. Leaving open Load capacity is often a wise tactical choice, preserving space for recovered salvage, mission assets, or captured hardware.
            </p>

            <h3>Equipment Categories</h3>
            <p>
                Hardware is divided into four major functional classifications:
            </p>
            <ul>
                <li><strong>Weapons:</strong> Tools engineered to inflict physical damage, divided into Melee and Ranged platforms.</li>
                <li><strong>Armor:</strong> Protective ballistic carapaces and suits mitigating incoming kinetic trauma.</li>
                <li><strong>Gear:</strong> Tactical kits, mobility rigs, consumables, explosives, and surveillance equipment.</li>
                <li><strong>Exotic Hardware:</strong> Black-budget prototypes and Precursor artifacts operating beyond standard procurement.</li>
            </ul>

            <h3>Damage Bonus</h3>
            <p>
                All weapons share a <strong>Damage Bonus</strong>. This flat integer is added directly to the Success Points generated on a successful attack roll, increasing net damage dealt.
            </p>

            <h3>Melee Weapon Fundamentals</h3>
            <p>
                Melee weapons inflict <strong>Piercing</strong>, <strong>Slashing</strong>, or <strong>Striking</strong> damage, each aligned with a favored physical Attribute Pair. Striking with a weapon's favored pair adds the <strong>lower attribute</strong> of the test directly to damage, in addition to the weapon's flat Damage Bonus.
            </p>

            <h3>Ranged Weapon Fundamentals</h3>
            <p>
                Firearms and ranged weapons are defined by:
            </p>
            <ul>
                <li><strong>Accuracy Array (S / M / L / E):</strong> Calibrated accuracy across four combat Range Bands (Short 0–5 spaces, Medium 6–12 spaces, Long 13–20 spaces, Extreme 20+ spaces). Fired using <strong>Accuracy + Finesse</strong>.</li>
                <li><strong>Rate of Fire (RoF):** Burst capability capping the total number of **Crit Effects** and **Chain Effects** that can be activated on an attack roll.</li>
                <li><strong>Hands &amp; Load:</strong> One-handed (1H) or two-handed (2H) requirements and physical inventory burden.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">72</span>
        </div>
    </div>"""
    pages.append(p72)

    # =========================================================================
    # PAGE 73 (Spread 3 Right) — DEFENSE, GEAR & REPAIR OPERATIONS
    # =========================================================================
    p73 = """    <!-- =========================================================================
         PAGE 73 (Spread 3 Right) — DEFENSE, GEAR & REPAIR OPERATIONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="repairs-and-maintenance">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: The Armory &amp; Load</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Armor Fundamentals</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Armor provides flat damage reduction against incoming attacks. Every suit is governed by four core metrics:
            </p>
            <ul>
                <li><strong>Protection:</strong> Subtracted directly from incoming kinetic and physical damage before applying wounds to Condition tracks. Protection stacks with Shields and Cover, but an operative can wear only one suit of armor at a time.</li>
                <li><strong>Load &amp; Cumbersome (X):</strong> Armor enforces no binary Strength minimum to wear. However, heavy and siege carapaces impose <strong>X Downgrades on all Agility tests</strong> (including speed and evasion).</li>
                <li><strong>Armor Properties:</strong> Engineering treatments such as <strong>Hardened</strong> (blunting critical hits), <strong>Blast-Dampened</strong> (+2 Protection vs Area/Explosives), and <strong>Tactical Harness</strong> (dedicated Load slots).</li>
            </ul>

            <h2>Tactical Gear Overview</h2>
            <p>
                Gear encompasses field hardware, toolkits, and consumables divided across seven tactical categories:
            </p>
            <ol style="margin-left: 3.5mm; margin-bottom: 2.5mm; font-size: 8.4pt; line-height: 1.34;">
                <li><strong>Mobility:</strong> Jump-packs, magnetic climbing kits, and motorized ziplines.</li>
                <li><strong>Fortification:</strong> Deployable cover, active defense beacons, and automated turrets.</li>
                <li><strong>Explosives &amp; Launchers:</strong> Multi-charge grenade bandoliers and rocket systems.</li>
                <li><strong>Medical &amp; Consumables:</strong> Trauma suites, neural dampers, and combat stimulants.</li>
                <li><strong>Infiltration &amp; Tech:</strong> Locksmith kits, biometric disguises, and cyberdecks.</li>
                <li><strong>Detection &amp; Surveillance:</strong> Proximity radars, recon drones, and spectrometers.</li>
                <li><strong>Survival &amp; Utility:</strong> Environmental hazard suits, rations, and shelter.</li>
            </ol>
            <p>
                Gear items provide dedicated <strong>Item Attributes</strong> (such as <em>Mobility</em>, <em>Sensors</em>, or <em>Tinkering</em>) pairing with operative attributes for actions costing <strong>1 AP</strong>.
            </p>

            <h2>Equipment Damage &amp; Repairs</h2>
            <p>
                Deployable gear, barricades, vehicles, and technological equipment possess structure ratings measured in <strong>Health Points (HP)</strong>. When an item takes damage, its HP is reduced accordingly. At 0 HP, the item is disabled until repaired:
            </p>
            <ul>
                <li><strong>Field Repair Action:</strong> Restoring HP to damaged equipment costs <strong>1 AP</strong> (in combat) or narrative time (in downtime) and requires a <strong>Success Test</strong> using <strong>Tinkering + Knowledge</strong>.</li>
                <li><strong>HP Restored:</strong> The item recovers <strong>1 HP per Success Point</strong> generated, up to its maximum HP rating.</li>
                <li><strong>Severe Destruction:</strong> Hardware reduced to 0 HP by catastrophic explosive damage or disintegration requires a dedicated machine shop and spare components to rebuild.</li>
            </ul>

            <div class="callout callout-cyan keep-together">
                <div class="callout-title">Refillable Casings Doctrine</div>
                <p>
                    Corsair eliminates bean-counting for field munitions and medical supplies. Rigs, stim injectors, and medi-kits feature a fixed <strong>Capacity (Cap X)</strong>. All expended charges automatically replenish to full whenever the crew visits a supply hub during place-to-place or day-to-day downtime.
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
    # PAGE 74 (Spread 4 Left) — FIREARMS FUNDAMENTALS & HANDGUNS
    # =========================================================================
    p74 = """    <!-- =========================================================================
         PAGE 74 (Spread 4 Left) — FIREARMS FUNDAMENTALS & HANDGUNS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-handguns">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Firearms &amp; Ballistics</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                In the cold vacuum of space, across contested orbital platforms, and inside pressurized corridors, firearms are the ultimate arbiters of ranged combat. Ranging from rugged chemical-propellant slugthrowers to electro-thermal chemical (ETC) rifles and high-velocity magnetic rail drivers, firearms grant the stopping power needed to overwhelm hostile forces before they close the distance.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <ul>
                <li><strong>Accuracy (S / M / L / E):</strong> Four ratings corresponding to the standard Range Bands (Short 0–5 spaces, Medium 6–12 spaces, Long 13–20 spaces, Extreme 20+ spaces). Fired using <strong>Accuracy + Finesse</strong>. A dash (<code>&minus;</code>) indicates the weapon cannot engage at that range.</li>
                <li><strong>Rate of Fire (RoF):</strong> Cyclic burst capability. RoF sets the strict upper limit on the total number of <strong>Crit Effects</strong> and <strong>Chain Effects</strong> that can be activated on an attack roll:
                    <ul>
                        <li><em>RoF 0 (Heavy-Hitters):</em> High-caliber single-shot weapons; deliver massive kinetic impact but cannot trigger RoF-based Crits or Chain.</li>
                        <li><em>RoF 1 (Semi-Auto):</em> Disciplined shot placement; up to 1 Crit or Chain effect.</li>
                        <li><em>RoF 2 (Burst/Auto):</em> Assault carbines and combat shotguns; up to 2 Crit/Chain effects.</li>
                        <li><em>RoF 3–4 (Suppression/Rotary):</em> High-cyclic machine guns; up to 3–4 Crit/Chain effects.</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added to Success Points on a hit.</li>
                <li><strong>Hands &amp; Load:</strong> 1H (sidearm) or 2H (long gun), plus inventory Load.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p>
                <strong>Panthera Arms:</strong> High-tolerance corporate carbines and DMRs.<br>
                <strong>Vandal's Workshop:</strong> Stamped-sheet, high-RoF submachine guns.<br>
                <strong>Caldera Foundry:</strong> Heavy-bore shotguns for boarding actions.<br>
                <strong>Ker'Satz Korp:</strong> Precision magnetic rail drivers and magnum revolvers.<br>
                <strong>Chidori-Qwei:</strong> Polymer smart-linked sidearms and PDWs.
            </p>

            <h3>Handguns Catalog</h3>
            <div class="table-container keep-together">
                <div class="table-header">Handguns &amp; Sidearms</div>
                <table class="rules-table" style="font-size: 8.1pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.6mm 1.6mm;">Weapon</th>
                            <th style="padding: 1.6mm 1.6mm;">Accuracy (S/M/L/E)</th>
                            <th style="padding: 1.6mm 1.6mm;">RoF</th>
                            <th style="padding: 1.6mm 1.6mm;">H</th>
                            <th style="padding: 1.6mm 1.6mm;">Dmg</th>
                            <th style="padding: 1.6mm 1.6mm;">Load</th>
                            <th style="padding: 1.6mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Holdout Pistol</td>
                            <td style="padding: 1.4mm 1.6mm;">2 / 1 / &minus; / &minus;</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">1H</td>
                            <td style="padding: 1.4mm 1.6mm;">+0</td>
                            <td style="padding: 1.4mm 1.6mm;">1/2</td>
                            <td style="padding: 1.4mm 1.6mm;">300</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Service Pistol</td>
                            <td style="padding: 1.4mm 1.6mm;">3 / 2 / 1 / &minus;</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">1H</td>
                            <td style="padding: 1.4mm 1.6mm;">+1</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">800</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Heavy Revolver</td>
                            <td style="padding: 1.4mm 1.6mm;">3 / 2 / 1 / &minus;</td>
                            <td style="padding: 1.4mm 1.6mm;">0</td>
                            <td style="padding: 1.4mm 1.6mm;">1H</td>
                            <td style="padding: 1.4mm 1.6mm;">+2</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">1,200</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Machine Pistol</td>
                            <td style="padding: 1.4mm 1.6mm;">3 / 2 / &minus; / &minus;</td>
                            <td style="padding: 1.4mm 1.6mm;">2</td>
                            <td style="padding: 1.4mm 1.6mm;">1H</td>
                            <td style="padding: 1.4mm 1.6mm;">+0</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">1,500</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Hand Cannon</td>
                            <td style="padding: 1.4mm 1.6mm;">2 / 3 / 2 / 0</td>
                            <td style="padding: 1.4mm 1.6mm;">0</td>
                            <td style="padding: 1.4mm 1.6mm;">1H</td>
                            <td style="padding: 1.4mm 1.6mm;">+2</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">2,200</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p style="font-size: 8.2pt; line-height: 1.32; color: var(--text-muted);">
                <em>Descriptions:</em> <strong>Holdout:</strong> Ultra-compact concealable backup. <strong>Service:</strong> Standard semi-auto duty sidearm. <strong>Heavy Revolver:</strong> Magnum cylinder gun with punishing recoil. <strong>Machine Pistol:</strong> Point-blank burst sidearm. <strong>Hand Cannon:</strong> Reinforced anti-armor kinetic handgun.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">74</span>
        </div>
    </div>"""
    pages.append(p74)

    # =========================================================================
    # PAGE 75 (Spread 4 Right) — SUBMACHINE GUNS & SHOTGUNS
    # =========================================================================
    p75 = """    <!-- =========================================================================
         PAGE 75 (Spread 4 Right) — SUBMACHINE GUNS & SHOTGUNS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-smg-shotguns">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Submachine Guns &amp; Shotguns</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Close-quarters primary weapons engineered for boarding operations, clearing tight ship bulkheads, and dominating short-range firefights across station gangways.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Submachine Guns &amp; Shotguns</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Weapon</th>
                            <th>Accuracy (S/M/L/E)</th>
                            <th>RoF</th>
                            <th>H</th>
                            <th>Dmg</th>
                            <th>Load</th>
                            <th>Cost</th>
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

            <h3>Operational Profiles</h3>
            <ul>
                <li><strong>Compact SMG:</strong> Lightweight collapsible submachine gun designed for vehicle crews, security officers, and boarding parties clearing cramped crawlspaces.</li>
                <li><strong>Tactical SMG:</strong> Balanced automatic platform featuring integral gas recoil compensators, high cyclic fire rates, and extended optical rails.</li>
                <li><strong>Trench Shotgun:</strong> Heavy pump-action smoothbore scattergun delivering catastrophic kinetic spread at point-blank range; lacks burst capacity but hits with massive shock.</li>
                <li><strong>Combat Shotgun:</strong> Semi-automatic magazine-fed shotgun engineered for rapid room clearing, breach support, and aggressive assault corridors.</li>
                <li><strong>Riot Scattergun:</strong> Fully automatic drum-fed scattergun delivering overwhelming projectile swarms designed to shred unarmored boarding squads.</li>
            </ul>

            <div class="callout callout-amber keep-together">
                <div class="callout-title">Boarding Engagement Geometry</div>
                <p>
                    Corridor fighting favors weapons with peak <strong>Short Range Accuracy (4 or 5)</strong>. While rifles lose effectiveness inside 0–5 spaces, shotguns and submachine guns dominate tight quarters, maximizing hit probabilities before hostiles can close into hand-to-hand combat.
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
    # PAGE 76 (Spread 5 Left) — RIFLES & HEAVY SUPPORT WEAPONS
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
            <h2 style="margin-top: 0;">Rifles Catalog</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Versatile long guns balancing range, stopping power, and tactical flexibility across station concourses, cargo bays, and planetary surfaces.
            </p>

            <div class="table-container keep-together" style="margin: 2mm 0;">
                <div class="table-header">Combat &amp; Precision Rifles</div>
                <table class="rules-table" style="font-size: 8.1pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.6mm 1.6mm;">Weapon</th>
                            <th style="padding: 1.6mm 1.6mm;">Accuracy (S/M/L/E)</th>
                            <th style="padding: 1.6mm 1.6mm;">RoF</th>
                            <th style="padding: 1.6mm 1.6mm;">H</th>
                            <th style="padding: 1.6mm 1.6mm;">Dmg</th>
                            <th style="padding: 1.6mm 1.6mm;">Load</th>
                            <th style="padding: 1.6mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Assault Carbine</td>
                            <td style="padding: 1.4mm 1.6mm;">3 / 3 / 2 / 1</td>
                            <td style="padding: 1.4mm 1.6mm;">2</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+2</td>
                            <td style="padding: 1.4mm 1.6mm;">3</td>
                            <td style="padding: 1.4mm 1.6mm;">3,800</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Assault Rifle</td>
                            <td style="padding: 1.4mm 1.6mm;">2 / 4 / 3 / 1</td>
                            <td style="padding: 1.4mm 1.6mm;">2</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+2</td>
                            <td style="padding: 1.4mm 1.6mm;">3</td>
                            <td style="padding: 1.4mm 1.6mm;">4,800</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Battle Rifle</td>
                            <td style="padding: 1.4mm 1.6mm;">2 / 3 / 4 / 2</td>
                            <td style="padding: 1.4mm 1.6mm;">0</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+4</td>
                            <td style="padding: 1.4mm 1.6mm;">3</td>
                            <td style="padding: 1.4mm 1.6mm;">5,500</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">DMR</td>
                            <td style="padding: 1.4mm 1.6mm;">1 / 3 / 5 / 3</td>
                            <td style="padding: 1.4mm 1.6mm;">1</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+4</td>
                            <td style="padding: 1.4mm 1.6mm;">4</td>
                            <td style="padding: 1.4mm 1.6mm;">7,000</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Sniper Rifle</td>
                            <td style="padding: 1.4mm 1.6mm;">0 / 2 / 5 / 4</td>
                            <td style="padding: 1.4mm 1.6mm;">0</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+5</td>
                            <td style="padding: 1.4mm 1.6mm;">4</td>
                            <td style="padding: 1.4mm 1.6mm;">9,500</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted); margin-bottom: 2mm;">
                <em>Descriptions:</em> <strong>Assault Carbine:</strong> Short-barreled mobility rifle. <strong>Assault Rifle:</strong> Standard military multi-range platform. <strong>Battle Rifle:</strong> Heavy-caliber semi-auto armor-cracker. <strong>DMR:</strong> Mid-to-long range precision rifle. <strong>Sniper Rifle:</strong> Extreme standoff precision weapon.
            </p>

            <h2 style="margin-top: 1mm; margin-bottom: 1.2mm;">Heavy Support Weapons</h2>
            <p style="margin-bottom: 1.5mm;">
                Reinforced heavy weapons requiring physical leverage to operate, delivering suppressive fire and anti-armor kinetic energy.
            </p>

            <div class="table-container keep-together" style="margin: 2mm 0;">
                <div class="table-header">Heavy Support Weapons</div>
                <table class="rules-table" style="font-size: 8.1pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.6mm 1.6mm;">Weapon</th>
                            <th style="padding: 1.6mm 1.6mm;">Accuracy (S/M/L/E)</th>
                            <th style="padding: 1.6mm 1.6mm;">RoF</th>
                            <th style="padding: 1.6mm 1.6mm;">H</th>
                            <th style="padding: 1.6mm 1.6mm;">Dmg</th>
                            <th style="padding: 1.6mm 1.6mm;">Load</th>
                            <th style="padding: 1.6mm 1.6mm;">Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">SAW</td>
                            <td style="padding: 1.4mm 1.6mm;">3 / 4 / 3 / 1</td>
                            <td style="padding: 1.4mm 1.6mm;">3</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+3</td>
                            <td style="padding: 1.4mm 1.6mm;">4</td>
                            <td style="padding: 1.4mm 1.6mm;">8,500</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">HMG</td>
                            <td style="padding: 1.4mm 1.6mm;">3 / 5 / 4 / 2</td>
                            <td style="padding: 1.4mm 1.6mm;">4</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+4</td>
                            <td style="padding: 1.4mm 1.6mm;">5</td>
                            <td style="padding: 1.4mm 1.6mm;">12,000</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">Rotary Cannon</td>
                            <td style="padding: 1.4mm 1.6mm;">5 / 4 / 2 / 1</td>
                            <td style="padding: 1.4mm 1.6mm;">4</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+4</td>
                            <td style="padding: 1.4mm 1.6mm;">5</td>
                            <td style="padding: 1.4mm 1.6mm;">16,000</td>
                        </tr>
                        <tr>
                            <td class="bold" style="padding: 1.4mm 1.6mm;">AMR</td>
                            <td style="padding: 1.4mm 1.6mm;">0 / 2 / 5 / 5</td>
                            <td style="padding: 1.4mm 1.6mm;">0</td>
                            <td style="padding: 1.4mm 1.6mm;">2H</td>
                            <td style="padding: 1.4mm 1.6mm;">+7</td>
                            <td style="padding: 1.4mm 1.6mm;">5</td>
                            <td style="padding: 1.4mm 1.6mm;">15,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted); margin-bottom: 0;">
                <em>Descriptions:</em> <strong>SAW:</strong> Squad automatic weapon for continuous suppression. <strong>HMG:</strong> High-caliber gun tearing through light cover. <strong>Rotary:</strong> Devastating motorized saturation cannon. <strong>AMR:</strong> Anti-materiel rail rifle disabling vehicles and breaching blast doors.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">76</span>
        </div>
    </div>"""
    pages.append(p76)

    # =========================================================================
    # PAGE 77 (Spread 5 Right) — DUAL WIELDING, UPGRADES & RANGED EXAMPLE
    # =========================================================================
    p77 = """    <!-- =========================================================================
         PAGE 77 (Spread 5 Right) — DUAL WIELDING, UPGRADES & RANGED EXAMPLE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-customization">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Dual Wielding Firearms</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Wielding a sidearm in each hand allows intense suppression and multi-target engagement:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield weapons with the <strong>1H designation</strong>.</li>
                <li><strong>Combined Output (Damage &amp; RoF):</strong> Add together both the flat <strong>Damage Bonus</strong> and the <strong>Rate of Fire (RoF)</strong> of the two firearms on your attack roll.</li>
                <li><strong>Worse Accuracy:</strong> Discharging two weapons simultaneously compromises sight alignment. You must use the <strong>worse (lower) Accuracy rating</strong> at the target's current range band between the two weapons.</li>
            </ul>

            <h2>Firearm Upgrade Kits</h2>
            <p>
                Custom gunsmithing enhances stock firearms with match barrels, tuned gas blocks, and optics. Upgrades escalate in cost with each installation:
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
                        <li><em>Lightweight Chassis:</em> Reduces weapon's <strong>Load by 1</strong> (min 1/2 Load).</li>
                        <li><em>Lethal Tuning:</em> Increases flat <strong>Damage Bonus by +1</strong>.</li>
                        <li><em>Recoil Dampening:</em> Increases weapon's <strong>RoF by 1</strong>.</li>
                        <li><em>Optic Calibration:</em> Increases <strong>Accuracy by +1</strong> at one designated range band.</li>
                    </ul>
                </li>
            </ul>

            <div class="example-box keep-together">
                <div class="example-title">Ranged Combat: The Hangar Deck Firefight</div>
                <p>
                    <strong>The Scenario:</strong> Jax advances along an industrial catwalk. Positioned <strong>8 spaces (26 meters)</strong> away behind freight crates, an armed syndicate mercenary returns fire. The distance places the target squarely at <strong>Medium Range</strong>.
                </p>
                <p>
                    Jax wields an <strong>Assault Rifle</strong> (Accuracy <code>2 / 4 / 3 / 1</code>, RoF 2, 2H, Load 3, +2 Damage Bonus). Jax's character sheet shows <strong>Finesse 5</strong>.
                </p>
                <p>
                    <strong>1. Action Roll (Higher = Finesse 5):</strong> Jax declares an <strong>Accuracy + Finesse</strong> Complex Test. At Medium Range, rifle Accuracy is 4. Pairing with Finesse 5, Jax rolls 5d10: <code>[2, 5, 8, 8, 9]</code>—three Hits (8, 8, 9). Jax spends one Hit (8) on an <strong>Upgrade Effect</strong>, stepping up one upcoming Success die from a d10 to a <strong>d12</strong>.
                </p>
                <p>
                    <strong>2. Success Roll (Lower = Accuracy 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 7, 8]</code> on d10s and <code>10</code> on the d12.
                </p>
                <p>
                    <strong>3. Effects &amp; RoF:</strong> The roll produced two Hits (8 and 10). Jax spends both on <strong>Crit Effects</strong> (+2 damage per Crit). The rifle's <strong>RoF 2</strong> perfectly accommodates spending 2 Hits on Crits.
                </p>
                <p>
                    <strong>4. Total Damage:</strong> Highest unspent die (7) + Two Crits (+4) + Rifle Damage Bonus (+2) = <strong>13 points of damage</strong>, punching through the container seam.
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
    # PAGE 78 (Spread 6 Left) — MELEE WEAPONS FUNDAMENTALS
    # =========================================================================
    p78 = """    <!-- =========================================================================
         PAGE 78 (Spread 6 Left) — MELEE WEAPONS FUNDAMENTALS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-fundamentals">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Melee Weapons &amp; Shields</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                In the tight corridors of starships, depressurized maintenance shafts, and orbital stations, discharging a firearm risks puncturing critical hull plating or ricocheting in zero-gravity. In confined environments, a dependable melee weapon is an indispensable tool for survival. Close-quarters combat demands physical prowess, tactical positioning, and mastery over your weapon's mechanical profile.
            </p>

            <h3>Weapon Statistics Explained</h3>
            <p>
                Every melee weapon is defined by mechanical attributes that govern how it interacts with physical statistics:
            </p>
            <ul>
                <li><strong>Damage Type &amp; Favored Pair:</strong> Melee weapons inflict damage through one of three physical methods, each aligned with a favored physical Attribute Pair:
                    <ul>
                        <li><strong>Piercing (Agility + Finesse):</strong> Swift, pinpoint thrusts directed at structural seams, visor slits, and armor joints.</li>
                        <li><strong>Slashing (Agility + Strength):</strong> Wide, sweeping kinetic cuts combining dynamic movement with cutting leverage.</li>
                        <li><strong>Striking (Strength + Finesse):</strong> Bone-shattering impacts delivered with disciplined body mechanics and leverage.</li>
                    </ul>
                </li>
                <li><strong>Favored Pair Damage Bonus:</strong> Attacking with a weapon's favored Attribute Pair grants a damage bonus equal to the <strong>lower attribute</strong> in that pair, added directly to the total damage alongside the weapon's flat Damage Bonus.</li>
                <li><strong>Minimum Strength (Min STR):</strong> Weapons require physical leverage to wield:
                    <ul>
                        <li><em>One-Handed (1H):</em> If your Strength is lower than Min STR, you cannot wield it in one hand; you must wield it with <strong>two hands</strong> to attack.</li>
                        <li><em>Two-Handed (2H):</em> If your Strength is lower than Min STR, the weapon is too heavy and you <strong>cannot attack with it</strong> under any circumstances.</li>
                    </ul>
                </li>
                <li><strong>Damage Bonus:</strong> Flat integer added directly to Success Points on a successful hit. Heavier weapons feature substantially larger bonuses.</li>
                <li><strong>Hands, Load &amp; Cost:</strong> Natural hand requirements (1H/2H), inventory Load, and market price in Credits.</li>
            </ul>

            <div class="callout callout-cyan keep-together">
                <div class="callout-title">The Favored Pair Advantage</div>
                <p>
                    While an operative can narrate and execute a melee attack with any combination of two physical attributes, striking with the weapon's favored pair unlocks its full kinetic potential. An operative with Strength 5 and Agility 4 swinging a slashing weapon adds +4 damage before weapon bonuses are even applied!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">78</span>
        </div>
    </div>"""
    pages.append(p78)

    # =========================================================================
    # PAGE 79 (Spread 6 Right) — MELEE WEAPONS CATALOG & DUAL WIELDING
    # =========================================================================
    p79 = """    <!-- =========================================================================
         PAGE 79 (Spread 6 Right) — MELEE WEAPONS CATALOG & DUAL WIELDING
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-catalog">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Weapons Catalog</h2>
            <div class="table-container keep-together">
                <div class="table-header">Close-Quarters Melee Weapons</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Weapon Name</th>
                            <th>Type</th>
                            <th>Min STR</th>
                            <th>H</th>
                            <th>Dmg</th>
                            <th>Load</th>
                            <th>Cost</th>
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

            <h2>Dual Wielding Melee</h2>
            <p>
                Fighting with a weapon in each hand creates an aggressive combat style that overwhelms defensive guards:
            </p>
            <ul>
                <li><strong>One-Handed Only:</strong> You can only dual wield weapons with the <strong>1H designation</strong>. You must meet the Min STR of each weapon individually.</li>
                <li><strong>Combined Damage Bonus:</strong> When you make a melee attack while dual wielding two 1H weapons, you gain the flat <strong>Damage Bonus of both weapons</strong> added to your total outcome.</li>
                <li><strong>Attack Resolution:</strong> Designate which of your two weapons leads the strike to determine the attack's <strong>Damage Type</strong> (Piercing, Slashing, or Striking) and its corresponding favored pair. If your declared action utilizes that favored pair, add the lower attribute of the test to the combined damage.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">79</span>
        </div>
    </div>"""
    pages.append(p79)

    # =========================================================================
    # PAGE 80 (Spread 7 Left) — UPGRADES & DEFENSIVE SHIELDS
    # =========================================================================
    p80 = """    <!-- =========================================================================
         PAGE 80 (Spread 7 Left) — UPGRADES & DEFENSIVE SHIELDS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-upgrades-shields">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons &amp; Shields</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Upgrade Kits</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Custom armorer tuning enhances melee weapons through monomolecular honing, vibro-motors, and composite counter-balancing:
            </p>
            <ul>
                <li><strong>Upgrade Limits:</strong> Two-handed weapons accept up to <strong>3 Upgrade Kits</strong>; 1H weapons accept up to <strong>2 Upgrade Kits</strong>.</li>
                <li><strong>Tiered Cost Structure:</strong>
                    <ul>
                        <li><strong>1st Upgrade:</strong> 10,000 Credits</li>
                        <li><strong>2nd Upgrade:</strong> 25,000 Credits</li>
                        <li><strong>3rd Upgrade:</strong> 50,000 Credits</li>
                    </ul>
                </li>
                <li><strong>Upgrade Choices:</strong>
                    <ul>
                        <li><em>Lightweight Tuning:</em> Reduces weapon's <strong>Load by 1</strong> (min 1/2 Load).</li>
                        <li><em>Lethal Edge / Weighted Core:</em> High-frequency vibration motors or carbide weights increase flat <strong>Damage Bonus by +1</strong>.</li>
                    </ul>
                </li>
            </ul>

            <h2>Defensive Shields</h2>
            <p>
                Shields are rigid ballistic barriers constructed from layered polymers, ceramics, or titanium alloys. Wielded in the off-hand, they provide vital cover during corridor breeches:
            </p>
            <ul>
                <li><strong>One Free Hand Required (1H):</strong> Wielding a shield occupies one hand. You cannot wield a two-handed weapon or perform two-handed tasks while holding a shield.</li>
                <li><strong>Physical Protection Bonus:</strong> While held, a shield grants a flat bonus to your <strong>Physical Protection</strong> (+1, +2, or +3). This bonus stacks directly with your worn armor.</li>
                <li><strong>No Dual Wielding Shields:</strong> A character cannot wield two shields simultaneously, nor benefit from more than one shield's Protection bonus at a time.</li>
                <li><strong>Minimum Strength:</strong> Heavier shields require conditioning to brace against impacts. If your Strength is lower than a shield's Min STR, you cannot wield it.</li>
            </ul>

            <div class="table-container keep-together">
                <div class="table-header">Defensive Shields</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Shield Name</th>
                            <th>Bonus Prot</th>
                            <th>Min STR</th>
                            <th>H</th>
                            <th>Load</th>
                            <th>Cost</th>
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
            <p style="font-size: 8.2pt; line-height: 1.32; color: var(--text-muted);">
                <em>Descriptions:</em> <strong>Buckler:</strong> Compact arm-mounted disc parrying blades. <strong>Riot Shield:</strong> Polycarbonate barrier offering full torso coverage. <strong>Ballistic Shield:</strong> Heavy ceramic pavise built to endure heavy kinetic fire.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">80</span>
        </div>
    </div>"""
    pages.append(p80)

    # =========================================================================
    # PAGE 81 (Spread 7 Right) — MELEE COMBAT IN ACTION
    # =========================================================================
    p81 = """    <!-- =========================================================================
         PAGE 81 (Spread 7 Right) — MELEE COMBAT IN ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-action-example">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons &amp; Shields</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Combat in Action</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                The boarding example below illustrates the resolution sequence of hand-to-hand melee combat, demonstrating favored attribute pairs, strength thresholds, and damage bonus stacking.
            </p>

            <div class="example-box keep-together">
                <div class="example-title">Tactical Strike: The Airlock Breach</div>
                <p>
                    <strong>The Scenario:</strong> Jax breaches a contested airlock space occupied by an armed pirate enforcer. Armed with a <strong>Boarding Axe</strong> (Slashing, Min STR 3, 1H, Load 2, +2 Damage Bonus), Jax initiates a close-quarters melee strike. Jax's character sheet shows <strong>Strength 5</strong>, <strong>Agility 4</strong>, and <strong>Finesse 3</strong>.
                </p>
                <p>
                    Because the Boarding Axe is a <strong>Slashing</strong> weapon, its favored Attribute Pair is <strong>Agility + Strength</strong>. Jax declares a sweeping overhand cleave, taking full advantage of the weapon's favored pair. With Strength 5, Jax easily meets the Min STR 3 requirement, wielding it comfortably in one hand.
                </p>
                <p>
                    <strong>1. Action Roll (Higher = Strength 5):</strong> Jax rolls 5d10: <code>[3, 5, 7, 8, 9]</code>. Both 8 and 9 are Hits (8+), meaning the Action Roll succeeds. Jax spends one Hit (8) to activate an <strong>Upgrade Effect</strong>, stepping up one upcoming Success die from a d10 to a <strong>d12</strong>.
                </p>
                <p>
                    <strong>2. Success Roll (Lower = Agility 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 6, 7]</code> on the d10s and a <code>9</code> on the upgraded d12. The highest single die value is <strong>9</strong>, granting Jax a base of <strong>9 Success Points</strong>.
                </p>
                <p>
                    <strong>3. Calculating Total Damage:</strong> Because Jax attacked using the weapon's favored pair (Agility + Strength), he adds the value of the lower attribute (<strong>Agility 4</strong>) directly to damage:
                </p>
                <ul>
                    <li>Base Success Points: <strong>9</strong></li>
                    <li>Favored Pair Bonus (Lower Attribute = Agility): <strong>+4</strong></li>
                    <li>Weapon Flat Damage Bonus: <strong>+2</strong></li>
                </ul>
                <p>
                    <strong>Total Damage Dealt:</strong> 9 + 4 + 2 = <strong>15 points of damage</strong>, cleaving cleanly through the enforcer's armor plating.
                </p>
            </div>

            <div class="callout callout-amber keep-together">
                <div class="callout-title">Breaching Safety Protocol</div>
                <p>
                    In depressurized environments or near vacuum seals, edged weapons eliminate the risk of spalling, accidental projectile ricochet, or explosive decompression. A veteran Corsair boarding team often carries boarding axes and heavy mauls specifically to breach bulkheads without rupturing atmospheric scrubbers.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">81</span>
        </div>
    </div>"""
    pages.append(p81)

    # =========================================================================
    # PAGE 82 (Spread 8 Left) — ARMOR MECHANICS & PROPERTIES
    # =========================================================================
    p82 = """    <!-- =========================================================================
         PAGE 82 (Spread 8 Left) — ARMOR MECHANICS & PROPERTIES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-mechanics">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Armor &amp; Protective Gear</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                In the perilous expanses of the settled systems, a dependable suit of armor is often the only barrier between an operative and lethal trauma. Whether weathering rifle fire in a depressurized corridor, deflecting shrapnel from an explosive breach, or absorbing punishing melee impacts, protective gear preserves operational capability in the deadliest environments.
            </p>

            <h3>Armor Statistics Explained</h3>
            <ul>
                <li><strong>Protection:</strong> Flat integer subtracted directly from physical and kinetic damage before applying wounds. Protection stacks with Shields (+1 to +3) and Cover (+1 to +3). An operative can wear only <strong>one suit of armor</strong> at a time.</li>
                <li><strong>Load:</strong> Physical mass counting against inventory capacity ($12 + \text{STR} \times 2$).</li>
                <li><strong>No Minimum Strength Requirement:</strong> Armor does not enforce a binary Strength requirement to wear. Any operative can wear any suit of armor, provided they have sufficient Load capacity. However, heavier suits carry the <strong>Cumbersome (X)</strong> property.</li>
            </ul>

            <h3>Specialized Armor Properties</h3>
            <ul>
                <li><strong>Cumbersome (X):</strong> Mass and rigid plates restrict sudden articulation. The wearer suffers <strong>X Downgrades on all Agility tests</strong> (including movement rolls, evasion, athletics, and stealth).</li>
                <li><strong>Hardened:</strong> Boron-carbide strike faces diffuse kinetic penetrators. When an attacker scores a <strong>Crit Effect</strong> against you, bonus Success Points gained per Hit spent is reduced by 1 (granting <strong>+1 SP per Hit spent</strong> instead of +2).</li>
                <li><strong>Blast-Dampened:</strong> Aramid spall-liners dissipate explosive concussions. You gain <strong>+2 additional Protection against Area Attacks and Explosives</strong>.</li>
                <li><strong>Tactical Harness (X):</strong> Reinforced webbing and quick-draw pouches provide <strong>X dedicated Load slots</strong> for any gear (weapons, medkits, ammo, tools). Items stowed here do not count against standard Load capacity, up to X Load.</li>
                <li><strong>Muffled:</strong> Acoustic micro-weaves suppress gear rattle, granting <strong>+1 Upgrade on Stealth tests</strong>.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p>
                <strong>Chidori-Qwei:</strong> Flexible polymer flightsuits and smart-fiber jackets.<br>
                <strong>Panthera Arms:</strong> Lightweight composite plate carriers.<br>
                <strong>Vandal's Workshop:</strong> Stamped-sheet alloy hazard suits.<br>
                <strong>Caldera Foundry:</strong> Heavy cast ceramic-titanium battleplate.<br>
                <strong>Ker'Satz Korp:</strong> Industrial siege carapaces and exosuits.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">82</span>
        </div>
    </div>"""
    pages.append(p82)

    # =========================================================================
    # PAGE 83 (Spread 8 Right) — ARMOR CATALOG
    # =========================================================================
    p83 = """    <!-- =========================================================================
         PAGE 83 (Spread 8 Right) — ARMOR CATALOG
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-catalog">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Light Armor (Load 1–3 · Prot 2–4)</h2>
            <p style="font-size: 8.4pt; line-height: 1.34; margin-bottom: 2mm;">
                Light armors impose no Agility penalties, favored by pilots, scouts, and agile skirmishers.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Light Armor Catalog</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Armor Name</th>
                            <th>Prot</th>
                            <th>Load</th>
                            <th>Properties</th>
                            <th>Cost</th>
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
            <p style="font-size: 8.4pt; line-height: 1.34; margin-bottom: 2mm;">
                Frontline protection balancing kinetic defense before full-body carapace penalties apply.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Medium Armor Catalog</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Armor Name</th>
                            <th>Prot</th>
                            <th>Load</th>
                            <th>Properties</th>
                            <th>Cost</th>
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
            <div class="table-container keep-together">
                <div class="table-header">Heavy Fortress Armor</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Armor Name</th>
                            <th>Prot</th>
                            <th>Load</th>
                            <th>Properties</th>
                            <th>Cost</th>
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
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">83</span>
        </div>
    </div>"""
    pages.append(p83)

    # =========================================================================
    # PAGE 84 (Spread 9 Left) — ARMOR UPGRADES & DEFENSIVE EXAMPLE
    # =========================================================================
    p84 = """    <!-- =========================================================================
         PAGE 84 (Spread 9 Left) — ARMOR UPGRADES & DEFENSIVE EXAMPLE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-upgrades-example">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Armor Upgrade Kits</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Custom armorer tuning enhances armor suits through high-density strike faces, composite skeletonization, and spall dampeners:
            </p>
            <ul>
                <li><strong>Upgrade Limit:</strong> A suit of armor can benefit from a maximum of <strong>3 Upgrade Kits</strong> in total.</li>
                <li><strong>Tiered Cost Structure:</strong>
                    <ul>
                        <li><strong>1st Upgrade:</strong> 50,000 Credits</li>
                        <li><strong>2nd Upgrade:</strong> 100,000 Credits</li>
                        <li><strong>3rd Upgrade:</strong> 180,000 Credits</li>
                    </ul>
                </li>
                <li><strong>Upgrade Choices:</strong>
                    <ul>
                        <li><em>Reinforced Plating:</em> Ceramic-carbide strike faces increase the armor's <strong>Protection by +1</strong> (maximum +3 Protection total across all kits).</li>
                        <li><em>Lightweight Composites:</em> Precision skeletonization reduces the armor's <strong>Load by 1</strong> (minimum 1 Load).</li>
                        <li><em>Specialized Modification:</em> Installs one specialized property: <strong>Hardened</strong>, <strong>Blast-Dampened</strong>, <strong>Tactical Harness (1)</strong>, or <strong>Muffled</strong>. Adding Tactical Harness to a suit already featuring it increases its rating by +1 (max Tactical Harness 2).</li>
                    </ul>
                </li>
            </ul>

            <div class="example-box keep-together">
                <div class="example-title">Defensive Action: Weathering the Barrage</div>
                <p>
                    <strong>The Scenario:</strong> During a violent airlock breach, Jax is caught in the open when a pirate gunner opens fire with a heavy <strong>Battle Rifle</strong>.
                </p>
                <p>
                    Jax is equipped with <strong>Tactical Battleplate</strong> (Protection 5, Load 4) and wields a <strong>Riot Shield</strong> (+2 Protection Bonus, Min STR 4, 1H, Load 2). Because Jax's armor is Tactical Battleplate, it carries no Cumbersome penalty, leaving his Agility rolls completely unhindered.
                </p>
                <p>
                    <strong>1. Incoming Attack:</strong> The pirate gunner rolls a successful attack test, spending 1 Hit on a <strong>Crit Effect</strong> (+2 damage) alongside the Battle Rifle's flat +4 Damage Bonus, generating <strong>14 points of physical damage</strong>.
                </p>
                <p>
                    <strong>2. Total Protection:</strong> Tactical Battleplate Base Protection (5) + Riot Shield Bonus (+2) = <strong>7 Combined Protection</strong>.
                </p>
                <p>
                    <strong>3. Damage Reduction:</strong>
                </p>
                <ul>
                    <li>Incoming Damage: <strong>14</strong></li>
                    <li>Subtracted Protection: <strong>&minus;7</strong></li>
                    <li><strong>Net Damage Received:</strong> 14 &minus; 7 = <strong>7 points of damage</strong>.</li>
                </ul>
                <p>
                    Thanks to the combined protection of his battleplate and riot shield, Jax absorbs half the kinetic energy, containing the wound cleanly within Track I of his Physical Condition.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">84</span>
        </div>
    </div>"""
    pages.append(p84)

    # =========================================================================
    # PAGE 85 (Spread 9 Right) — GEAR RULES & MOBILITY SYSTEMS
    # =========================================================================
    p85 = """    <!-- =========================================================================
         PAGE 85 (Spread 9 Right) — GEAR RULES & MOBILITY SYSTEMS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-rules-mobility">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Tactical Gear &amp; Mobility</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Gear encompasses specialized toolkits, refillable field rigs, explosives, and survival hardware. While weapons and armor govern combat survival, gear provides the technical leverage, vertical mobility, and utility needed to complete dangerous boarding operations.
            </p>

            <h3>Gear Rules &amp; Resolution</h3>
            <ul>
                <li><strong>Dedicated Item Attributes:</strong> Gear provides dedicated ratings (such as <em>Mobility</em>, <em>Medicine</em>, <em>Sensors</em>, <em>Tinkering</em>, <em>Locksmith</em>, <em>Interfacing</em>, or <em>Ordnance</em>) pairing with operative attributes.</li>
                <li><strong>Action Point Cost:</strong> Deploying or activating gear requires <strong>1 AP</strong>.</li>
                <li><strong>Capacity &amp; Automatic Refill:</strong> Consumable rigs possess a fixed <strong>Capacity (Cap X)</strong>. Expending charges is free; all charges automatically refill upon visiting any supply hub or starship in downtime.</li>
                <li><strong>Stand-Alone Explosive Rolls:</strong> Explosives do not pair with attributes; they roll pure <strong>Ordnance</strong> pools for Area Attacks.</li>
            </ul>

            <h2>1. Mobility Gear</h2>
            <div class="table-container keep-together">
                <div class="table-header">Mobility Hardware</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
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
                            <td class="bold">Assault Zipline (40m)</td>
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
                <li><strong>Jetpack (Xm):</strong> 1 AP, Success Test using <strong>Mobility + Agility</strong>. Flight speed equals base speed (Xm) plus 1m per Success Point. Ignore difficult terrain and falling damage. <em>Vector Boost (Crit):</em> Spending a Hit grants <strong>+4m movement</strong> instead of +2 SPs. <em>Charging:</em> Spend 1 AP to fly base speed in a straight line and execute a Melee Attack.</li>
                <li><strong>Surface Adhesion:</strong> 1 AP, Success Test using <strong>Mobility + Strength</strong>. Adhere to sheer/vertical/inverted hulls; climb 8m plus 1m per SP.</li>
                <li><strong>Grapple (Xm):</strong> 1 AP, expends 1 Charge. Solid terrain: automatic pull to anchor. Hostiles: Complex Test using <strong>Mobility + Strength</strong>; each Hit spent triggers a <strong>Push Effect</strong> pulling the target 1 space toward you. User may advance along tether or deal SPs as tearing damage.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">85</span>
        </div>
    </div>"""
    pages.append(p85)

    # =========================================================================
    # PAGE 86 (Spread 10 Left) — FORTIFICATION GEAR & DEFENSE BEACONS
    # =========================================================================
    p86 = """    <!-- =========================================================================
         PAGE 86 (Spread 10 Left) — FORTIFICATION GEAR & DEFENSE BEACONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortification">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">2. Fortification Gear</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Deployable fortifications provide instant cover, automated point defense against incoming ordnance, and remote heavy weapon platforms.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Fortification &amp; Defense Systems</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
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
                            <td>Intercept 5, Area-Defense Reaction, 24 HP</td>
                            <td>3</td>
                            <td>25,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Smartpod Remote Mount</td>
                            <td>Automount 3, 12 HP</td>
                            <td>3</td>
                            <td>36,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Fortification Special Properties</h3>
            <ul>
                <li><strong>Deployable Cover:</strong> Deploying or repacking a barricade costs <strong>1 AP</strong>. Occupies one space and grants its Cover Protection bonus (+1 to +3) to any creature sheltering behind it. Possesses its own Cover HP and Innate Protection; degraded by 1 Prot per 12 damage taken. Can be recovered for 1 AP.</li>
                <li><strong>Intercept (X) &amp; Area-Defense:</strong> Once deployed (1 AP), the Active Protection System automatically monitors its space and all adjacent spaces. It gains <strong>1 Free Reaction AP per round</strong> to contest incoming Area Attacks and explosive munitions. Resolves an <strong>Intercept Contest</strong> rolling pure <strong>Intercept (X)</strong>. If no dice showing 8+ remain after the contest, the incoming munition is intercepted mid-air and completely negated.</li>
                <li><strong>Automount (X):</strong> Motorized tripod and optical sensor package. Deploying or dismounting (with any mounted ranged weapon) costs <strong>1 AP</strong>. An operator or linked ally can spend <strong>1 AP</strong> to fire the mounted weapon remotely, rolling <strong>Automount (X) + Finesse</strong> (or pure Automount X if automated). Recoverable for 1 AP.</li>
            </ul>

            <div class="callout callout-cyan keep-together">
                <div class="callout-title">Chokepoint Lockdown Protocol</div>
                <p>
                    Deploying an APS Beacon alongside a Medium Barricade turns an open airlock into a hardened bunker. The beacon shoots down enemy grenades in mid-flight while operators lay down suppressive fire from behind reinforced ballistic plating.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">86</span>
        </div>
    </div>"""
    pages.append(p86)

    # =========================================================================
    # PAGE 87 (Spread 10 Right) — EXPLOSIVES & HEAVY ORDNANCE
    # =========================================================================
    p87 = """    <!-- =========================================================================
         PAGE 87 (Spread 10 Right) — EXPLOSIVES & HEAVY ORDNANCE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-explosives">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">3. Explosives &amp; Launchers</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Explosives deliver high-yield area destruction. Instead of tracking loose grenades, combatants carry refillable <strong>Grenade Rigs</strong> allowing on-the-fly munition selection at the point of use.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Explosives &amp; Launcher Rigs</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tactical Grenade Rig</td>
                            <td>Capacity 3, Refillable, Point-of-Use Choice</td>
                            <td>2</td>
                            <td>4,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Assault Grenade Rig</td>
                            <td>Capacity 5, Refillable, Point-of-Use Choice</td>
                            <td>3</td>
                            <td>10,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy Demolitions Rig</td>
                            <td>Capacity 2, Refillable, Point-of-Use Choice</td>
                            <td>3</td>
                            <td>8,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Siege Demolitions Rig</td>
                            <td>Capacity 4, Refillable, Point-of-Use Choice</td>
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

            <h3>Available Munition Profiles</h3>
            <p>
                When expending a charge (1 AP), the user chooses one profile at the moment of priming:
            </p>
            <ul>
                <li><strong>Frag Munition:</strong> <strong>Ordnance 4, Blast 3, 8m Radius.</strong> Anti-personnel fragmentation bomb with serrated wire casing.</li>
                <li><strong>Flashbang Munition:</strong> <strong>Ordnance 5, Area Stun, 4m Radius.</strong> Pyrotechnic stun canister blinding and deafening hostiles.</li>
                <li><strong>Smoke Canister:</strong> <strong>Area Obscurance, 8m Radius.</strong> Fills area with opaque thermal smoke without rolling; blocks line of sight.</li>
                <li><strong>HE Munition:</strong> <strong>Ordnance 5, Blast 5, 4m Radius.</strong> High-explosive concussion charge for enclosed bulkheads.</li>
                <li><strong>Remote Demolition Charge:</strong> <strong>Ordnance 7, Blast 5, 12m Radius, Remote.</strong> Heavy breaching explosive. Demolitions Rig only.</li>
            </ul>

            <h3>Explosives Special Properties</h3>
            <ul>
                <li><strong>Ordnance (X) Area Attack:</strong> Throwing or firing costs 1 AP and expends 1 Charge. Hand-thrown grenades target Short Range (0–5 spaces); launcher rigs extend range to Medium, Long, or Extreme. Resolves as an Area Attack Success Test rolling pure <strong>Ordnance (X)</strong>.</li>
                <li><strong>Blast (X):</strong> Modifies bonus damage from Crit Effects: spending a Hit on the Success Roll adds <strong>+X damage</strong> per Hit spent instead of +2.</li>
                <li><strong>Area Stun:</strong> For each 8+ on Ordnance test, every creature caught within blast discards its highest die on its next roll until next Player Turn.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">87</span>
        </div>
    </div>"""
    pages.append(p87)

    # =========================================================================
    # PAGE 88 (Spread 11 Left) — MEDICAL SUITES & STIMULANTS
    # =========================================================================
    p88 = """    <!-- =========================================================================
         PAGE 88 (Spread 11 Left) — MEDICAL SUITES & STIMULANTS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-medical">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">4. Medical &amp; Consumables</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Medical suites and chemical auto-injectors provide emergency field triage and biological enhancement. All medical gear operates on durable, refillable casings.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Medical Kits &amp; Injectors</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
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
                            <td class="bold">Combat Stim Injector</td>
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

            <h3>Medical &amp; Consumable Properties</h3>
            <ul>
                <li><strong>Medicine (X) Triage:</strong> Applying a medical kit to yourself or an adjacent ally costs <strong>1 AP</strong>, expends 1 Charge, and requires a <strong>Success Test</strong> using <strong>Medicine + Knowledge</strong>.</li>
                <li><strong>Lesser Healing (1/X, Track):</strong> Restores <strong>1 segment</strong> on the designated track (Physical or Mental) per <strong>X Success Points</strong> generated. Cannot repair locked (Aggravated) damage.</li>
                <li><strong>Greater Healing (1/X, Track):</strong> Restores damage at standard rate. Additionally clears <strong>Aggravated damage segments</strong> at double the SP cost (2X SPs per locked segment).</li>
                <li><strong>Point-of-Use Stim Choice:</strong> Activating an injector (1 AP, 1 Charge) administers one chemical booster (Volatile 2, Fleeting):
                    <ul>
                        <li><em>Roid (+1 Strength):</em> Anabolic surge for physical leverage.</li>
                        <li><em>Nitro (+1 Agility):</em> Adrenaline booster for speed and evasion.</li>
                        <li><em>Edgedance (+1 Finesse):</em> Fine-motor neural precision booster.</li>
                        <li><em>SharpX (+1 Instinct):</em> Sensory cortex alertness stimulant.</li>
                        <li><em>Cognita (+1 Knowledge):</em> Nootropic tactical accelerator.</li>
                        <li><em>Rizz (+1 Presence):</em> Pheromonal vocal poise enhancement.</li>
                    </ul>
                </li>
                <li><strong>Volatile (X):</strong> Immediate strain; user suffers <strong>X unmitigated damage</strong> upon administration. Stacking stings causes extra damage equal to active substances. <em>Fleeting:</em> Lasts until end of round.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">88</span>
        </div>
    </div>"""
    pages.append(p88)

    # =========================================================================
    # PAGE 89 (Spread 11 Right) — INFILTRATION & TECH KITS
    # =========================================================================
    p89 = """    <!-- =========================================================================
         PAGE 89 (Spread 11 Right) — INFILTRATION & TECH KITS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-tech-infiltration">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">5. Infiltration &amp; Tech Kits</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Specialized toolkits and cyberdecks utilized to bypass physical bulkheads, forge security passes, and penetrate encrypted station mainframes.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Infiltration Rigs &amp; Cyberdecks</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
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

            <h3>Infiltration &amp; Tech Properties</h3>
            <ul>
                <li><strong>Tinkering (X):</strong> Disabling physical traps, field sabotaging machinery, or conducting repairs costs <strong>1 AP</strong> and requires a test using <strong>Tinkering + Knowledge</strong>.</li>
                <li><strong>Locksmith (X):</strong> Picking mechanical tumbler locks or bypassing electronic access panels costs <strong>1 AP</strong> and requires a test using <strong>Locksmith + Finesse</strong>.</li>
                <li><strong>Disguise (X):</strong> Crafting convincing cosmetic disguises, uniforms, and character personas costs 1 AP (or narrative downtime) and requires a test using <strong>Disguise + Knowledge</strong>.</li>
                <li><strong>Forgery (X):</strong> Counterfeiting security manifests, cargo passes, and digital identification papers costs 1 AP and requires a test using <strong>Forgery + Finesse</strong>.</li>
                <li><strong>Interfacing (X):</strong> Establishing secure hardware bridges, navigating network nodes, and querying databases costs <strong>1 AP</strong> and uses <strong>Interfacing + Knowledge</strong>.</li>
                <li><strong>Hacking (X):</strong> Shredding hostile ICE, bypassing security firewalls, and subverting defensive turrets costs <strong>1 AP</strong> and uses <strong>Hacking + Knowledge</strong>.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">89</span>
        </div>
    </div>"""
    pages.append(p89)

    # =========================================================================
    # PAGE 90 (Spread 12 Left) — SURVEILLANCE & SURVIVAL UTILITY
    # =========================================================================
    p90 = """    <!-- =========================================================================
         PAGE 90 (Spread 12 Left) — SURVEILLANCE & SURVIVAL UTILITY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-surveillance-survival">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">6. Detection &amp; Surveillance</h2>
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Sensors, spectrometers, and autonomous recon drones reveal hidden hostiles and map hostile installations.
            </p>

            <div class="table-container keep-together">
                <div class="table-header">Surveillance &amp; Reconnaissance</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
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
                <li><strong>Sensors (X):</strong> Active scanning for hidden hostiles or analyzing toxic environments costs <strong>1 AP</strong> and uses <strong>Sensors + Knowledge</strong>.</li>
                <li><strong>Scouting (Xm):</strong> Passive automated detection radius. Any creature moving within X meters triggers an instant alert unless electronically cloaked.</li>
                <li><strong>Remote Control:</strong> Piloting a drone costs <strong>1 AP</strong>; drones fly up to 20m/round and conduct active sweeps with onboard Sensors.</li>
            </ul>

            <h2>7. Survival &amp; Field Utility</h2>
            <div class="table-container keep-together">
                <div class="table-header">Survival &amp; Utility Gear</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Properties</th>
                            <th>Load</th>
                            <th>Cost</th>
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
                <li><strong>Environmental Immunity:</strong> Immune to extreme temperatures (&minus;150&deg;C to +200&deg;C), toxins, and vacuum exposure for 12 hours.</li>
                <li><strong>Long-Range Comm:</strong> Orbital voice/data broadcast; decryption tests use <strong>Interfacing + Knowledge</strong>.</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">90</span>
        </div>
    </div>"""
    pages.append(p90)

    # =========================================================================
    # PAGE 91 (Spread 12 Right) — EXOTIC HARDWARE: RULES & RARITY LADDER
    # =========================================================================
    p91 = """    <!-- =========================================================================
         PAGE 91 (Spread 12 Right) — EXOTIC HARDWARE: RULES & RARITY LADDER
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-hardware">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Exotic Hardware</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3.5mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Exotic Hardware</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.1pt; line-height: 1.40; margin-bottom: 2mm;">
                Beyond standard military procurement exists a narrow, intoxicating, and lethal category of equipment: <strong>Exotic Hardware</strong>. These are the crown jewels of black-budget skunkworks, un-cataloged corporate prototypes liberated from clandestine laboratories, and cold-glass relics dragged from subterranean Precursor vaults.
            </p>
            <p>
                In accordance with the laws of the Sphere, there is no magic here. Prototypes operate on bleeding-edge physics and extreme thermal shunting. Precursor relics are solid-state transducers tapping into the diffuse dark matter halo engineered by the Singularity.
            </p>

            <h3>The Rules of Exotic Hardware</h3>
            <ol style="margin-left: 3.5mm; margin-bottom: 2.5mm; font-size: 8.3pt; line-height: 1.32;">
                <li><strong>Load Taxation Over Attunement:</strong> There is no mystical attunement cap in Corsair. An operative can carry as many pieces of Exotic Hardware as their spine can endure. However, exotic hardware carries heavy <strong>Load (typically Load 2 to 5)</strong>. Packing multiple exotic systems forces agonizing tradeoffs against essential field rations, medical rigs, and armor.</li>
                <li><strong>Action Point Economy:</strong> Activating an exotic function costs <strong>1 AP</strong> or integrates into an existing 1-AP combat action. Passive systems apply continuously, but active bursts demand dedicated focus.</li>
                <li><strong>Thermal Pacing Cooldowns:</strong> Exotic cooling cycles align with narrative pacing:
                    <ul>
                        <li><em>Moment-to-Moment:</em> Recovers after 1 combat round (~5–10s), resetting at start of next turn.</li>
                        <li><em>Place-to-Place:</em> Recovers after 1 transit round (~1 hour) via coolant loops or starship heat sinks.</li>
                        <li><em>Day-to-Day:</em> Recovers after a 24-hour downtime cycle.</li>
                    </ul>
                </li>
                <li><strong>Irreplaceable Maintenance:</strong> Reduced to 0 HP, prototypes require a dedicated workshop and a successful <strong>Tinkering + Knowledge</strong> test. Precursor relics cannot be repaired by mortal tools without rare molecular salvage or Ancestral favor.</li>
                <li><strong>Non-Customizable Architecture:</strong> Exotic hardware <strong>cannot accept standard Upgrade Kits</strong>. Machining attempts ruin their atomic harmonic calibration; stats and Load are permanently fixed as written.</li>
            </ol>

            <h3>The 4-Tier Rarity &amp; Economic Ladder</h3>
            <div class="table-container keep-together">
                <div class="table-header">Exotic Rarity Ladder</div>
                <table class="rules-table">
                    <thead>
                        <tr>
                            <th>Tier</th>
                            <th>Classification</th>
                            <th>Cost (Credits)</th>
                            <th>Market Reality &amp; Acquisition</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Tier 1</td>
                            <td>Mil-Spec Skunkworks</td>
                            <td>15,000–30,000</td>
                            <td>Limited-run military trials and high-spec foundry prototypes. Corporate fixers or veteran armories.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 2</td>
                            <td>Classified Prototypes</td>
                            <td>40,000–80,000</td>
                            <td>Espionage targets and reverse-engineered alien polymers. Black-site heists and high-threat contracts.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 3</td>
                            <td>Precursor Relics</td>
                            <td>100,000–250,000</td>
                            <td>Non-baryonic catalytic lattices and self-repairing alloys. Deep underworld auctions (Jailers, Iron Fang).</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 4</td>
                            <td>Singularities &amp; Wonders</td>
                            <td>Priceless</td>
                            <td>One-of-a-kind mythic artifacts (dreadnought cores, null-beams). Major campaign milestones.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">91</span>
        </div>
    </div>"""
    pages.append(p91)

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
    print(f"Successfully generated {out_path} with {len(pages)} pages (Pages 68 to 91).")

if __name__ == "__main__":
    generate_chapter_04()
