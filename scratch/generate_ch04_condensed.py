# -*- coding: utf-8 -*-
"""
Generate a continuous-flow, space-efficient html/04_Armory_and_Gear.html.
16 pages (8 complete spreads: Pages 68 to 83).
Eliminates massive bottom voids, budgets content to 80-88% page fill,
maintains 100% verbatim rules fidelity, zero <a> tags, zero sci-fi telemetry tags.
"""

from pathlib import Path

def build_condensed_ch04():
    pages = []

    # =========================================================================
    # SPREAD 1 (Pages 68-69): TACTICAL COMBAT, MOVEMENT, CQC & COVER
    # =========================================================================

    # PAGE 68 (Left) — Combat Opener, Grid, Verticality, Flying, Contesting & Jax Example
    p68 = """    <!-- =========================================================================
         PAGE 68 (Spread 1 Left) — CHAPTER 04 OPENER: COMBAT, MOVEMENT & CONTESTS
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
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                In the world of Corsair, conflict is inevitable. Whether facing down corporate enforcers, battling an alien in the depths of a derelict ship, or engaging in a desperate firefight across depressurized gantries, combat is a thrilling and dangerous reality. When violence erupts, the game shifts into <strong>Moment to Moment</strong> pacing. While you can resolve skirmishes using "theater of the mind," employing a grid-based battle map adds tactical clarity to positioning, cover, and engagement lines.
            </p>

            <h3>Movement &amp; The Battle Grid</h3>
            <p>
                Navigating the battlefield is crucial for survival. In combat, you can spend <strong>1 Action Point (AP)</strong> to move. When you move, you perform a <strong>Success Test</strong> (typically with <strong>Agility</strong>, representing sprinting and vaulting), moving a number of meters equal to the result plus your base speed (by default, <strong>4 meters</strong>).
            </p>
            <p>
                On a grid with spaces representing a <strong>4-meter diameter space</strong>:
            </p>
            <ul>
                <li>Base speed of 4 meters translates to <strong>1 space</strong>.</li>
                <li>Your Success Test adds extra movement: divide meters rolled by four, rounding up, and move an additional number of spaces equal to the result.</li>
            </ul>
            <p>
                A single move action covers a maximum of 16 meters (4 spaces). An operative can spend multiple Action Points on movement to cover significant distances.
            </p>

            <h3>Verticality, Flight &amp; Terrain</h3>
            <p>
                Battlefields are three-dimensional. Model verticality by layering horizontal grids separated by <strong>2 meters</strong>. Moving vertically between layers is always <strong>Difficult Terrain</strong>—unless you fall. Falling more than 2 meters inflicts damage equal to <strong>three times the meters fallen</strong>, completely <strong>unmitigated by Protection</strong>.
            </p>
            <p>
                <strong>Flying</strong> allows 3D movement in air as if on solid ground. Ascending costs double (2m ascent consumes 4m movement); descending or moving horizontally costs normally. Flying creatures <strong>ignore Difficult Terrain</strong>. If flight is lost, you remain suspended until turn's end, falling and taking damage if above 2m.
            </p>
            <p>
                <strong>Difficult Terrain</strong> (slurry, rubble, barricades) costs <strong>2 meters of speed per 1 meter of progress</strong> (8m / 2 spaces per grid space).
            </p>

            <h3>Contesting Movement</h3>
            <p>
                A defender can physically intercept, tackle, or trip a creature moving through their space via a standard Contest:
            </p>
            <ol style="margin-left: 3.5mm; margin-bottom: 2mm; font-size: 8.2pt; line-height: 1.32;">
                <li><strong>Narrate Interception:</strong> Defender describes how they impede the movement (grabbing, tripping, blocking).</li>
                <li><strong>Attribute Selection:</strong> GM selects a relevant Attribute (e.g., <strong>Strength</strong> to grab, <strong>Agility</strong> to trip).</li>
                <li><strong>Contest Roll:</strong> The contester rolls a pool equal to their chosen Attribute.</li>
                <li><strong>Eliminating Dice:</strong> Each success (8+) eliminates one of the highest dice from the runner's movement roll. If no dice showing 8+ remain, the runner is stopped dead in the contester's space.</li>
            </ol>

            <div class="example-box keep-together" style="margin-top: 2mm;">
                <div class="example-title">Contest Example: Stopping Jax</div>
                <p>
                    Jax attempts to sprint past an enforcer toward an airlock console. Jax spends 1 AP for a move action, rolling an <strong>Agility 4</strong> Success Test: <code>[9, 7, 5, 2]</code>. The 9 allows Jax to move his base 1 space + 2 extra spaces (9m &divide; 4, rounded up) = 3 spaces.
                </p>
                <p>
                    The enforcer declares a contest with <strong>Strength 5</strong>, rolling 5d10: <code>[10, 8, 6, 4, 1]</code> (two successes: 10, 8). These eliminate Jax's two highest dice (9 and 7), leaving <code>[5, 2]</code>. With no dice showing 8+ remaining, Jax is stopped dead in his tracks in the enforcer's space!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">68</span>
        </div>
    </div>"""
    pages.append(p68)

    # PAGE 69 (Right) — Space, Occupancy, CQC, Cover, Destruction & Facing
    p69 = """    <!-- =========================================================================
         PAGE 69 (Spread 1 Right) — SPACE, OCCUPANCY, CQC & COVER MECHANICS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="space-cqc-cover">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Space, CQC &amp; Cover</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Space &amp; Occupancy</h2>
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                A single 4&times;4 meter space accommodates up to <strong>4 standard-sized creatures</strong>. Hand-to-hand combat, point-blank triage, and close teamwork maneuvers require operatives to share a space.
            </p>

            <h3>Outnumbering &amp; Melee Engagement</h3>
            <p>
                When you and your allies outnumber hostiles within a single space, you gain a number of <strong>Upgrades</strong> on melee attacks equal to the difference between allied and hostile creatures (e.g., 3 allies vs. 1 enemy grants <strong>2 Upgrades</strong> to all allies).
            </p>
            <p>
                You can attack a target in your space or an adjacent space using any two Physical Attributes. When attacking into an adjacent space holding fewer than 4 creatures, you move into it; if full, you attack from your current space while treating all allies in your space as present for outnumbering.
            </p>

            <h3>Creature Sizing</h3>
            <ul>
                <li><strong>Standard (Humans, Elves, Dwarves):</strong> 1 capacity slot (up to 4 per space).</li>
                <li><strong>Large (War-drones, Ogres, Brutes):</strong> Fills <strong>2 slots</strong> (max 2 per space).</li>
                <li><strong>Huge (Vehicles, Walkers, Behemoths):</strong> Fills <strong>4 slots</strong> (1 per space).</li>
            </ul>

            <h2>Close Quarters Combat (CQC)</h2>
            <p>
                Sharing a space with an active hostile places you in <strong>CQC</strong>, severely disrupting firearms handling:
            </p>
            <ul>
                <li><strong>Firing in CQC:</strong> Discharging a ranged weapon while in CQC suffers <strong>2 Downgrades</strong> on the attack test.</li>
                <li><strong>Firing into CQC:</strong> Firing from outside into a space where allies and hostiles are engaged suffers <strong>1 Downgrade</strong> to avoid friendly fire.</li>
            </ul>

            <h2>Cover &amp; Damage Mitigation</h2>
            <p>
                Cover provides a flat bonus to <strong>Protection</strong> that stacks with worn armor against attacks originating from <em>outside</em> the defender's space:
            </p>
            <ul>
                <li><strong>Light Cover (+1 Protection):</strong> Partial concealment (thin pipes, barrels).</li>
                <li><strong>Medium Cover (+2 Protection):</strong> Solid barriers (engine blocks, crates).</li>
                <li><strong>Heavy Cover (+3 Protection):</strong> Fortified bunkers, bulkheads, corners.</li>
            </ul>

            <h3>Destroying Cover</h3>
            <p>
                Light, Medium, and Heavy Cover possess <strong>12, 24, and 36 Health Points (HP)</strong> and innate Protection of <strong>4, 8, and 12</strong> when targeted directly:
            </p>
            <ul>
                <li>Attacking cover is resolved as a <strong>Success Test</strong>.</li>
                <li>For every <strong>12 damage</strong> absorbed, the cover's Protection bonus is reduced by 1.</li>
                <li>Breaching charges and anti-materiel weapons ignore cover's innate Protection.</li>
            </ul>

            <div class="table-container keep-together" style="margin: 2mm 0;">
                <div class="table-header">Cover Defensive &amp; Structural Ratings</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.5mm 2mm;">Tier</th>
                            <th style="padding: 1.5mm 2mm;">Bonus</th>
                            <th style="padding: 1.5mm 2mm;">HP</th>
                            <th style="padding: 1.5mm 2mm;">Innate Prot</th>
                            <th style="padding: 1.5mm 2mm;">Degrade Threshold</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Light</td>
                            <td>+1</td>
                            <td>12 HP</td>
                            <td>4</td>
                            <td>Destroyed at 12 Dmg</td>
                        </tr>
                        <tr>
                            <td class="bold">Medium</td>
                            <td>+2</td>
                            <td>24 HP</td>
                            <td>8</td>
                            <td>&minus;1 Prot per 12 Dmg</td>
                        </tr>
                        <tr>
                            <td class="bold">Heavy</td>
                            <td>+3</td>
                            <td>36 HP</td>
                            <td>12</td>
                            <td>&minus;1 Prot per 12 Dmg</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>Cover Facing</h3>
            <p>
                The first time you are attacked in a round, draw a straight line from attacker to your space: the side crossed becomes your <strong>covering side</strong> (corner crossings cover both adjacent sides). On subsequent attacks:
            </p>
            <ul>
                <li><strong>Covering Side:</strong> Full Protection bonus.</li>
                <li><strong>Adjacent Side:</strong> Reduced bonus (&minus;1 on hex, &minus;2 on square).</li>
                <li><strong>Non-Adjacent Side:</strong> No bonus (fully exposed).</li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">69</span>
        </div>
    </div>"""
    pages.append(p69)

    # =========================================================================
    # SPREAD 2 (Pages 70-71): THE ARMORY, LOAD & FIREARMS (HANDGUNS, SMGS, SHOTGUNS)
    # =========================================================================

    # PAGE 70 (Left) — The Armory, Load System, Damage Bonus, Maintenance & Firearms Fundamentals
    p70 = """    <!-- =========================================================================
         PAGE 70 (Spread 2 Left) — THE ARMORY, LOAD SYSTEM & FIREARMS FUNDAMENTALS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armory-firearms-fundamentals">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: The Armory &amp; Load</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">The Armory &amp; Firearms</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                Everyday items like commlinks and keys are assumed belongings. Items providing tactical advantages—weapons, armor, sensor suites, and tech kits—are governed by the <strong>Load system</strong>.
            </p>

            <h3>The Load Invariant</h3>
            <p>
                Every mechanically significant item has a <strong>Load</strong> value reflecting mass and encumbrance. An operative's carrying capacity is strictly bound by physical conditioning:
            </p>
            <div class="callout callout-cyan keep-together" style="margin: 2mm 0; padding: 2.5mm 3.5mm;">
                <p style="font-size: 9.5pt; font-weight: 700; text-align: center; margin: 0;">
                    \text{Maximum Load Capacity} = 12 + (\text{Strength} \times 2)
                </p>
            </div>
            <p>
                This limit is absolute; an operative cannot exceed it under any circumstances. Preserving open Load capacity allows hauling mission-critical salvage and captured gear.
            </p>

            <h3>Equipment Damage &amp; Field Repairs</h3>
            <p>
                Hardware and vehicles have structure rated in <strong>Health Points (HP)</strong>. Reduced to 0 HP, an item ceases functioning. Field repairs cost <strong>1 AP</strong> (combat) or narrative time (downtime), requiring a <strong>Success Test</strong> using <strong>Tinkering + Knowledge</strong>. The item restores <strong>1 HP per Success Point</strong> up to maximum HP.
            </p>

            <h3>Damage Bonus Mechanics</h3>
            <p>
                All weapons feature a flat <strong>Damage Bonus</strong> added directly to Success Points on a hit to increase net damage dealt.
            </p>

            <h2>Firearms Fundamentals</h2>
            <p>
                From chemical slugthrowers to electro-thermal rifles and magnetic rail drivers, firearms govern ranged combat:
            </p>
            <ul>
                <li><strong>Accuracy Array (S / M / L / E):</strong> Calibrated accuracy across four Range Bands: Short (0–5 spaces, ~0–20m), Medium (6–12 spaces, ~20–40m), Long (13–20 spaces, ~40–80m), and Extreme (20+ spaces, ~80m+). Attacks roll <strong>Accuracy + Finesse</strong>. A dash (<code>&minus;</code>) indicates ineffective range.</li>
                <li><strong>Rate of Fire (RoF):</strong> Strict upper limit on the total number of <strong>Crit Effects</strong> and <strong>Chain Effects</strong> activatable on an attack roll:
                    <ul>
                        <li><em>RoF 0 (Heavy-Hitters):</em> High-caliber single shots; no burst Crits/Chains.</li>
                        <li><em>RoF 1 (Semi-Auto):</em> Disciplined fire; up to 1 Crit or Chain effect.</li>
                        <li><em>RoF 2 (Burst/Auto):</em> Assault weapons; up to 2 Crit/Chain effects.</li>
                        <li><em>RoF 3–4 (Suppression):</em> Heavy weapons; up to 3–4 Crit/Chain effects.</li>
                    </ul>
                </li>
                <li><strong>Hands &amp; Load:</strong> One-handed (1H) sidearm or two-handed (2H) long gun.</li>
            </ul>

            <h3>Prominent Manufacturers</h3>
            <p style="font-size: 8.3pt; line-height: 1.34;">
                <strong>Panthera Arms:</strong> High-tolerance corporate carbines and DMRs.<br>
                <strong>Vandal's Workshop:</strong> Stamped-sheet, high-RoF submachine guns.<br>
                <strong>Caldera Foundry:</strong> Heavy-bore shotguns and breaching rifles.<br>
                <strong>Ker'Satz Korp:</strong> Precision magnetic rail drivers and magnum hand cannons.<br>
                <strong>Chidori-Qwei:</strong> Polymer smart-linked sidearms and PDWs.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""
    pages.append(p70)

    # PAGE 71 (Right) — Handguns, Submachine Guns & Shotguns Catalogs
    p71 = """    <!-- =========================================================================
         PAGE 71 (Spread 2 Right) — HANDGUNS, SUBMACHINE GUNS & SHOTGUNS CATALOGS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-handguns-shotguns">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Handguns Catalog</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
                Compact sidearms for personal defense, emergency backup, and close-quarters deployment.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Handguns &amp; Sidearms</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm;">Weapon</th>
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

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted); margin-bottom: 2.5mm;">
                <em>Profiles:</em> <strong>Holdout:</strong> Concealable backup. <strong>Service:</strong> Standard semi-auto sidearm. <strong>Heavy Revolver:</strong> High-grain magnum with punishing recoil. <strong>Machine Pistol:</strong> Point-blank burst gun. <strong>Hand Cannon:</strong> Reinforced anti-armor kinetic pistol.
            </p>

            <h2>Submachine Guns &amp; Shotguns</h2>
            <p style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
                Close-quarters primaries for boarding actions and dominating tight station corridors.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Submachine Guns &amp; Shotguns</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm;">Weapon</th>
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

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted); margin-bottom: 2.5mm;">
                <em>Profiles:</em> <strong>Compact SMG:</strong> Collapsible PDW for vehicle crews. <strong>Tactical SMG:</strong> Balanced auto with recoil compensators. <strong>Trench Shotgun:</strong> Pump scattergun with massive point-blank spread. <strong>Combat Shotgun:</strong> Semi-auto box-fed breacher. <strong>Riot Scattergun:</strong> Drum-fed saturation sweeper.
            </p>

            <div class="callout callout-amber keep-together" style="margin-top: 1mm; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 9.5pt;">Corridor Ballistic Doctrine</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    Inside pressurized hulls, combat occurs almost entirely at <strong>Short Range (0–5 spaces)</strong>. High-Accuracy scatterguns and compact SMGs maximize hit probability before targets reach hand-to-hand engagement.
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
    # SPREAD 3 (Pages 72-73): RIFLES, HEAVY SUPPORT, CUSTOMIZATION & RANGED ACTION
    # =========================================================================

    # PAGE 72 (Left) — Combat Rifles & Heavy Support Weapons Catalogs
    p72 = """    <!-- =========================================================================
         PAGE 72 (Spread 3 Left) — COMBAT RIFLES & HEAVY SUPPORT WEAPONS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-rifles-heavy">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Combat &amp; Precision Rifles</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
                Versatile long guns balancing effective range, kinetic penetration, and burst handling.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Combat &amp; Precision Rifles</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm;">Weapon</th>
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

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted); margin-bottom: 2.5mm;">
                <em>Profiles:</em> <strong>Assault Carbine:</strong> High-mobility carbine. <strong>Assault Rifle:</strong> Balanced standard battle rifle. <strong>Battle Rifle:</strong> Heavy armor-cracking semi-auto. <strong>DMR:</strong> Mid-to-long range marksman rifle. <strong>Sniper Rifle:</strong> Extreme standoff bolt-action platform.
            </p>

            <h2>Heavy Support Weapons</h2>
            <p style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
                Crew-served and braced platforms delivering suppressive saturation and anti-armor energy.
            </p>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Heavy Support Weapons</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 1.5mm;">Weapon</th>
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

            <p style="font-size: 8.0pt; line-height: 1.28; color: var(--text-muted);">
                <em>Profiles:</em> <strong>SAW:</strong> Belt-fed light machine gun pinning down squads. <strong>HMG:</strong> Heavy gun chewing through light cover. <strong>Rotary Autocannon:</strong> Multi-barrel saturation sweeper. <strong>AMR:</strong> Magnetic anti-tank rifle penetrating bulkheads and vehicles.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">72</span>
        </div>
    </div>"""
    pages.append(p72)

    # PAGE 73 (Right) — Dual Wielding, Upgrade Kits & Tactical Walkthrough
    p73 = """    <!-- =========================================================================
         PAGE 73 (Spread 3 Right) — DUAL WIELDING, UPGRADES & RANGED ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="firearms-customization-action">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Firearms Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Dual Wielding Firearms</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
                Wielding a sidearm in each hand enables intense saturation and multi-target splits:
            </p>
            <ul>
                <li><strong>1H Only:</strong> You can only dual wield sidearms with the <strong>1H designation</strong>.</li>
                <li><strong>Combined Output:</strong> Add together both the flat <strong>Damage Bonus</strong> and the <strong>Rate of Fire (RoF)</strong> of the two firearms on your attack roll.</li>
                <li><strong>Worse Accuracy:</strong> Discharging two weapons simultaneously compromises sight alignment; you must use the <strong>worse (lower) Accuracy rating</strong> at the target's range band between the two weapons.</li>
            </ul>

            <h2>Firearm Upgrade Kits</h2>
            <p style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
                Precision gunsmithing enhances stock firearms. Upgrades escalate in cost with each installation:
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

            <div class="example-box keep-together" style="margin-top: 2mm;">
                <div class="example-title">Tactical Action: The Hangar Deck Firefight</div>
                <p>
                    <strong>The Scenario:</strong> Jax spots an armed syndicate mercenary <strong>8 spaces (~26m)</strong> away behind low freight crates—squarely at <strong>Medium Range</strong>. Jax is armed with an <strong>Assault Rifle</strong> (Accuracy <code>2 / 4 / 3 / 1</code>, RoF 2, 2H, Load 3, +2 Damage Bonus) and has <strong>Finesse 5</strong>.
                </p>
                <p>
                    <strong>1. Action Roll (Finesse 5):</strong> Declaring an <strong>Accuracy + Finesse</strong> Complex Test, Jax rolls 5d10: <code>[2, 5, 8, 8, 9]</code> (three Hits: 8, 8, 9). Jax spends one Hit (8) on an <strong>Upgrade Effect</strong>, stepping up one upcoming Success die from a d10 to a <strong>d12</strong>.
                </p>
                <p>
                    <strong>2. Success Roll (Accuracy 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 7, 8]</code> on d10s and <code>10</code> on the d12. Both 8 and 10 are Hits.
                </p>
                <p>
                    <strong>3. Effects &amp; RoF:</strong> Jax spends both Hits on <strong>Crit Effects</strong> (+2 damage per Crit). The rifle's <strong>RoF 2</strong> perfectly accommodates spending 2 Hits on Crits.
                </p>
                <p>
                    <strong>4. Total Damage:</strong> Highest unspent die (7) + Two Crits (+4) + Rifle Damage Bonus (+2) = <strong>13 points of damage</strong>, punching through the container seam!
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
    # SPREAD 4 (Pages 74-75): MELEE WEAPONS, SHIELDS & AIRLOCK ACTION
    # =========================================================================

    # PAGE 74 (Left) — Melee Fundamentals, Dual Wielding, Upgrades & Shields
    p74 = """    <!-- =========================================================================
         PAGE 74 (Spread 4 Left) — MELEE FUNDAMENTALS, UPGRADES & DEFENSIVE SHIELDS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-fundamentals-shields">
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
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                In pressurized starship corridors and depressurized maintenance shafts, discharging firearms risks puncturing critical hull plating or ricocheting in zero-gravity. In confined quarters, close combat demands physical prowess and weapon mastery.
            </p>

            <h3>Favored Attribute Pairs</h3>
            <p>
                Melee weapons deal damage through three physical methods, each inherently linked to a favored Physical Attribute Pair:
            </p>
            <ul>
                <li><strong>Piercing (Agility + Finesse):</strong> Swift thrusts into structural seams and visor slits.</li>
                <li><strong>Slashing (Agility + Strength):</strong> Sweeping kinetic cuts combining dynamic body rotation with edge leverage.</li>
                <li><strong>Striking (Strength + Finesse):</strong> Disciplined kinetic impacts cracking bone through armor plating.</li>
            </ul>
            <p>
                <strong>Favored Pair Damage Bonus:</strong> Striking with a weapon's favored pair adds the <strong>lower attribute</strong> in that pair directly to total damage alongside the weapon's flat Damage Bonus.
            </p>

            <h3>Minimum Strength &amp; Dual Wielding</h3>
            <ul>
                <li><strong>Minimum Strength (Min STR):</strong> Weapons require leverage:
                    <ul>
                        <li><em>1H Weapons:</em> If Strength &lt; Min STR, you must use <strong>two hands</strong> to attack with it.</li>
                        <li><em>2H Weapons:</em> If Strength &lt; Min STR, the weapon is too heavy and you <strong>cannot attack with it</strong>.</li>
                    </ul>
                </li>
                <li><strong>Dual Wielding Melee:</strong> Only 1H weapons. Must meet Min STR of each weapon individually. Add flat <strong>Damage Bonus of both weapons</strong> to total damage. Designate which weapon leads the strike for Damage Type and favored pair bonus.</li>
            </ul>

            <h3>Melee Upgrade Kits</h3>
            <p>
                Two-handed weapons accept up to <strong>3 Upgrade Kits</strong>; 1H weapons accept up to <strong>2 Upgrade Kits</strong> (10,000 / 25,000 / 50,000 Credits):
            </p>
            <ul>
                <li><em>Lightweight Tuning:</em> Reduces weapon's <strong>Load by 1</strong> (min 1/2 Load).</li>
                <li><em>Lethal Edge / Weighted Core:</em> Increases flat <strong>Damage Bonus by +1</strong>.</li>
            </ul>

            <h2>Defensive Shields</h2>
            <p>
                Rigid ballistic barriers made from polymers, ceramics, or titanium:
            </p>
            <ul>
                <li><strong>1H Required:</strong> Holding a shield occupies one hand.</li>
                <li><strong>Protection Stacking:</strong> Adds flat <strong>Protection Bonus (+1, +2, +3)</strong> stacking directly with worn armor.</li>
                <li><strong>Min STR:</strong> If Strength &lt; Min STR, you cannot wield the shield. No dual wielding shields.</li>
            </ul>

            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Defensive Shields</div>
                <table class="rules-table" style="font-size: 8.0pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.4mm 2mm;">Shield Name</th>
                            <th style="padding: 1.4mm 2mm;">Prot</th>
                            <th style="padding: 1.4mm 2mm;">Min STR</th>
                            <th style="padding: 1.4mm 2mm;">H</th>
                            <th style="padding: 1.4mm 2mm;">Load</th>
                            <th style="padding: 1.4mm 2mm;">Cost</th>
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
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">74</span>
        </div>
    </div>"""
    pages.append(p74)

    # PAGE 75 (Right) — Melee Catalog & Airlock Breach Action Walkthrough
    p75 = """    <!-- =========================================================================
         PAGE 75 (Spread 4 Right) — MELEE WEAPONS CATALOG & AIRLOCK BREACH ACTION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="melee-catalog-action">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Melee Weapons</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Melee Weapons Catalog</h2>
            <div class="table-container keep-together" style="margin: 1.5mm 0;">
                <div class="table-header">Close-Quarters Melee Weapons</div>
                <table class="rules-table" style="font-size: 7.8pt;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.5mm;">Weapon Name</th>
                            <th style="padding: 1.2mm 1.5mm;">Type</th>
                            <th style="padding: 1.2mm 1.5mm;">Min STR</th>
                            <th style="padding: 1.2mm 1.5mm;">H</th>
                            <th style="padding: 1.2mm 1.5mm;">Dmg</th>
                            <th style="padding: 1.2mm 1.5mm;">Load</th>
                            <th style="padding: 1.2mm 1.5mm;">Cost</th>
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

            <div class="example-box keep-together" style="margin-top: 2mm;">
                <div class="example-title">Tactical Action: The Airlock Breach</div>
                <p>
                    <strong>The Scenario:</strong> Jax breaches an airlock occupied by an armed pirate. Armed with a <strong>Boarding Axe</strong> (Slashing, Min STR 3, 1H, Load 2, +2 Damage Bonus), Jax initiates a strike. Jax's attributes are <strong>Strength 5</strong>, <strong>Agility 4</strong>, and <strong>Finesse 3</strong>.
                </p>
                <p>
                    As a Slashing weapon, its favored pair is <strong>Agility + Strength</strong>. Jax's Strength 5 easily satisfies Min STR 3.
                </p>
                <p>
                    <strong>1. Action Roll (Strength 5):</strong> Jax rolls 5d10: <code>[3, 5, 7, 8, 9]</code>. Both 8 and 9 are Hits. Jax spends one Hit (8) on an <strong>Upgrade Effect</strong>, stepping up an upcoming Success die from d10 to <strong>d12</strong>.
                </p>
                <p>
                    <strong>2. Success Roll (Agility 4):</strong> Jax rolls 3d10 and 1d12: <code>[4, 6, 7]</code> on d10s and <code>9</code> on d12. Highest single die is <strong>9</strong> base Success Points.
                </p>
                <p>
                    <strong>3. Damage Resolution:</strong>
                </p>
                <ul>
                    <li>Base Success Points: <strong>9</strong></li>
                    <li>Favored Pair Bonus (Lower = Agility): <strong>+4</strong></li>
                    <li>Weapon Damage Bonus: <strong>+2</strong></li>
                </ul>
                <p>
                    <strong>Total Damage Dealt:</strong> 9 + 4 + 2 = <strong>15 points of damage</strong>, cleaving through the pirate's defenses.
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
    # SPREAD 5 (Pages 76-77): ARMOR DEFENSE, UPGRADES & CARAPACE CATALOG
    # =========================================================================

    # PAGE 76 (Left) — Armor Mechanics, Properties, Manufacturers & Upgrades
    p76 = """    <!-- =========================================================================
         PAGE 76 (Spread 5 Left) — ARMOR MECHANICS, PROPERTIES & UPGRADE KITS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-mechanics-upgrades">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Armor &amp; Protective Gear</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                In the perilous expanses of the settled systems, dependable armor is the barrier between an operative and lethal trauma. Protective gear mitigates incoming kinetic trauma before it affects physical condition tracks.
            </p>

            <h3>Armor Statistics &amp; Stacking</h3>
            <ul>
                <li><strong>Protection:</strong> Flat integer subtracted directly from incoming damage. Protection stacks with Shields and Cover. An operative can wear only <strong>one suit of armor</strong> at a time.</li>
                <li><strong>Load &amp; Strength:</strong> Counts against Load ($12 + \text{STR} \times 2$). Armor has <strong>no minimum Strength</strong> requirement to wear, but heavier suits carry the <strong>Cumbersome</strong> penalty.</li>
            </ul>

            <h3>Specialized Armor Properties</h3>
            <ul>
                <li><strong>Cumbersome (X):</strong> Imposes <strong>X Downgrades on all Agility tests</strong> (including movement, evasion, athletics, and stealth).</li>
                <li><strong>Hardened:</strong> Diffuses kinetic penetrators. Attacker's <strong>Crit Effect</strong> grants only <strong>+1 SP per Hit spent</strong> (instead of +2).</li>
                <li><strong>Blast-Dampened:</strong> Dissipates shockwaves; gain <strong>+2 Protection against Area Attacks and Explosives</strong>.</li>
                <li><strong>Tactical Harness (X):</strong> Webbing provides <strong>X dedicated Load slots</strong> for any gear; stowed items do not count against personal Load limit.</li>
                <li><strong>Muffled:</strong> Acoustic weaves grant <strong>+1 Upgrade on Stealth tests</strong>.</li>
            </ul>

            <h3>Manufacturers &amp; Custom Upgrades</h3>
            <p style="font-size: 8.3pt; line-height: 1.32; margin-bottom: 2mm;">
                <strong>Chidori-Qwei:</strong> Flexible polymer garments and stealth suits.<br>
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
                <div class="example-title">Defensive Action: Weathering the Barrage</div>
                <p>
                    Jax is caught in the open during an airlock breach when a pirate opens fire with a Battle Rifle. Jax wears <strong>Tactical Battleplate</strong> (Prot 5, Load 4) and holds a <strong>Riot Shield</strong> (+2 Prot, Min STR 4, Load 2), totaling <strong>7 Protection</strong> with no Cumbersome penalties.
                </p>
                <p>
                    The gunner hits with 1 Crit (+2) and the rifle's flat +4 Damage Bonus, dealing <strong>14 physical damage</strong>. Jax subtracts his 7 Protection: 14 &minus; 7 = <strong>7 net damage</strong>, contained cleanly within Track I!
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">76</span>
        </div>
    </div>"""
    pages.append(p76)

    # PAGE 77 (Right) — Complete Armor Catalog (Light, Medium & Heavy)
    p77 = """    <!-- =========================================================================
         PAGE 77 (Spread 5 Right) — COMPLETE ARMOR CATALOG (LIGHT, MEDIUM, HEAVY)
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="armor-catalog-complete">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Armor &amp; Protection</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Light Armor (Load 1–3 · Prot 2–4)</h2>
            <p style="font-size: 8.6pt; line-height: 1.34; margin-bottom: 1.5mm;">
                Unencumbering protection imposing zero Agility penalties; favored by scouts, pilots, and snipers.
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
                Frontline protection balancing heavy mitigation before full carapace penalties apply.
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
            <span class="page-num">77</span>
        </div>
    </div>"""
    pages.append(p77)

    # =========================================================================
    # SPREAD 6 (Pages 78-79): TACTICAL GEAR: MOBILITY, FORTIFICATION & EXPLOSIVES
    # =========================================================================

    # PAGE 78 (Left) — Tactical Gear Rules & Mobility Systems
    p78 = """    <!-- =========================================================================
         PAGE 78 (Spread 6 Left) — TACTICAL GEAR RULES & MOBILITY HARDWARE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-rules-mobility">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Tactical Gear &amp; Munitions</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                Tactical gear encompasses field hardware, specialized toolkits, refillable rigs, and survival equipment providing operational leverage across station boarding and hostile environments.
            </p>

            <h3>Gear Rules &amp; Resolution</h3>
            <ul>
                <li><strong>Dedicated Attributes:</strong> Items provide specific attributes (<em>Mobility</em>, <em>Sensors</em>, <em>Medicine</em>, <em>Tinkering</em>, <em>Locksmith</em>, <em>Interfacing</em>, <em>Hacking</em>, <em>Ordnance</em>).</li>
                <li><strong>Action Point Cost:</strong> Activating or deploying gear costs <strong>1 AP</strong>.</li>
                <li><strong>Capacity &amp; Automatic Refill:</strong> Consumable casings have fixed <strong>Capacity (Cap X)</strong>. All expended charges automatically replenish at any supply hub or ship in downtime without tracking individual restocks.</li>
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
            <span class="page-num">78</span>
        </div>
    </div>"""
    pages.append(p78)

    # PAGE 79 (Right) — Fortification Gear & Explosives / Munitions
    p79 = """    <!-- =========================================================================
         PAGE 79 (Spread 6 Right) — FORTIFICATIONS & HEAVY EXPLOSIVES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortification-explosives">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">2. Fortification Gear</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 1.5mm;">
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

            <p style="font-size: 8.0pt; line-height: 1.30; margin-bottom: 2mm;">
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
            <span class="page-num">79</span>
        </div>
    </div>"""
    pages.append(p79)

    # =========================================================================
    # SPREAD 7 (Pages 80-81): TACTICAL GEAR: MEDICAL, TECH, SURVEILLANCE & SURVIVAL
    # =========================================================================

    # PAGE 80 (Left) — Medical Rigs, Stimulants & Infiltration Tech Kits
    p80 = """    <!-- =========================================================================
         PAGE 80 (Spread 7 Left) — MEDICAL, STIMULANTS & INFILTRATION KITS
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
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 1.5mm;">
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

            <p style="font-size: 7.8pt; line-height: 1.28; margin-top: 1mm;">
                <strong>Tinkering:</strong> Traps/repairs (Tinkering + Knowledge). <strong>Locksmith:</strong> Locks/latches (Locksmith + Finesse). <strong>Disguise:</strong> Personas (Disguise + Knowledge). <strong>Forgery:</strong> Passes (Forgery + Finesse). <strong>Interfacing:</strong> Nodes/consoles (Interfacing + Knowledge). <strong>Hacking:</strong> ICE/firewalls (Hacking + Knowledge).
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">80</span>
        </div>
    </div>"""
    pages.append(p80)

    # PAGE 81 (Right) — Detection, Surveillance, Survival & Field Utility
    p81 = """    <!-- =========================================================================
         PAGE 81 (Spread 7 Right) — DETECTION, SURVEILLANCE & SURVIVAL UTILITY
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-surveillance-survival">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Tactical Gear</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">6. Detection &amp; Surveillance</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 1.5mm;">
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
                <li><strong>Sensors (X):</strong> Active scanning for concealed hostiles or analyzing toxic hazards costs <strong>1 AP</strong> and uses <strong>Sensors + Knowledge</strong>.</li>
                <li><strong>Scouting (Xm):</strong> Passive automated detection radius. Any creature moving within X meters triggers an instant alert unless electronically cloaked.</li>
                <li><strong>Remote Control:</strong> Piloting a drone costs <strong>1 AP</strong>; drones fly up to 20m/round and conduct active sweeps with onboard Sensors.</li>
            </ul>

            <h2>7. Survival &amp; Field Utility</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 1.5mm;">
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
            <span class="page-num">81</span>
        </div>
    </div>"""
    pages.append(p81)

    # =========================================================================
    # SPREAD 8 (Pages 82-83): EXOTIC HARDWARE: RULES & 4-TIER RARITY LADDER
    # =========================================================================

    # PAGE 82 (Left) — Exotic Hardware Intro, Load Taxation & System Invariants
    p82 = """    <!-- =========================================================================
         PAGE 82 (Spread 8 Left) — EXOTIC HARDWARE: SKUNKWORKS & PRECURSOR RELICS
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
            <p class="lead" style="font-size: 9.0pt; line-height: 1.38; margin-bottom: 2mm;">
                Beyond standard military procurement exists a narrow, intoxicating, and lethal category of equipment: <strong>Exotic Hardware</strong>. These are the crown jewels of black-budget corporate skunkworks, un-cataloged prototypes liberated from clandestine laboratories on Nimbus, and terrifying cold-glass relics dragged from subterranean Precursor vaults.
            </p>
            <p>
                In the lexicon of ancient fantasy games, they are the "magic items" of Corsair. Yet in accordance with the laws of the Sphere, there is no magic here. Every prototype operates on bleeding-edge physics and extreme thermal shunting; every Precursor relic is a solid-state transducer tapping into the diffuse dark matter halo engineered by the Singularity.
            </p>

            <h3>The Rules of Exotic Hardware</h3>
            <ol style="margin-left: 3.5mm; margin-bottom: 2mm; font-size: 8.3pt; line-height: 1.32;">
                <li><strong>Load Taxation Over Arbitrary Limits:</strong> There is no mystical "attunement" ceiling in Corsair. An operative can carry as many pieces of Exotic Hardware as their spine can endure. However, exotic hardware carries heavy <strong>Load (typically Load 2 to 5)</strong>. Packing multiple exotic systems forces agonizing logistical tradeoffs against field rations, medical rigs, and armor.</li>
                <li><strong>Action Point Economy:</strong> Activating an exotic function costs <strong>1 Action Point (AP)</strong> or integrates into an existing 1-AP combat action. Passive systems apply continuously, but active bursts always demand dedicated tactical focus.</li>
                <li><strong>Thermal Pacing Cooldowns:</strong> Extreme prototypes generate severe thermal spikes. Cooldowns align with narrative pacing:
                    <ul>
                        <li><em>Moment-to-Moment:</em> Recovers after <strong>1 combat round</strong> (~5–10s), resetting at the start of your next turn.</li>
                        <li><em>Place-to-Place:</em> Recovers after <strong>1 transit round</strong> (~1 hour) via coolant flush or ship heat sinks.</li>
                        <li><em>Day-to-Day:</em> Recovers after a <strong>24-hour downtime cycle</strong> with workshop recalibration.</li>
                    </ul>
                </li>
                <li><strong>Irreplaceable Maintenance:</strong> Reduced to 0 HP, prototypes require a dedicated workshop and a successful <strong>Tinkering + Knowledge</strong> test against Tier DC. Precursor relics cannot be repaired by mortal tools without rare molecular salvage or Ancestral favor.</li>
                <li><strong>Non-Customizable Architecture:</strong> Exotic hardware <strong>cannot accept standard Upgrade Kits</strong>. Machining attempts ruin their atomic harmonic calibration; stats and Load are permanently fixed as written.</li>
            </ol>

            <div class="callout callout-amber keep-together" style="margin-top: 1.5mm; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 9.5pt;">The High Frontier Tradeoff</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    Carrying a Precursor null-beam projector means leaving behind your heavy armor or two trauma kits. Every exotic capability must justify its crushing inventory burden.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">82</span>
        </div>
    </div>"""
    pages.append(p82)

    # PAGE 83 (Right) — The 4-Tier Rarity Ladder & Operational Acquisition
    p83 = """    <!-- =========================================================================
         PAGE 83 (Spread 8 Right) — 4-TIER RARITY LADDER & ACQUISITION
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="exotic-rarity-ladder">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 04: Exotic Hardware</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">The 4-Tier Rarity Ladder</h2>
            <p class="lead" style="font-size: 8.8pt; line-height: 1.36; margin-bottom: 2mm;">
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
                            <td>Limited-run military trials and high-spec foundry prototypes. Sourced via corporate fixers or veteran armories.</td>
                        </tr>
                        <tr>
                            <td class="bold">Tier 2</td>
                            <td>Classified Prototypes</td>
                            <td>40,000–80,000</td>
                            <td>Corporate espionage targets and reverse-engineered alien polymers. Black-site heists and high-threat contracts.</td>
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

            <h3>Operational Acquisition &amp; Market Realities</h3>
            <ul>
                <li><strong>Tier 1 (Mil-Spec Skunkworks):</strong> Advanced field modifications from premier manufacturers (Caldera, Port Zenith, Panthera). Available to established Corsair cells with positive corporate reputation.</li>
                <li><strong>Tier 2 (Classified Prototypes):</strong> Cutting-edge corporate R&amp;D trials. Possessing unregistered prototypes triggers corporate bounty hunter tracking.</li>
                <li><strong>Tier 3 (Precursor Relics):</strong> Intact alien artifacts recovered from deep Vault excavations. Strictly contraband under the Covenant Accords; traded only in deep-underworld syndicates.</li>
                <li><strong>Tier 4 (Singularities &amp; Unique Wonders):</strong> Artifacts capable of shifting political balance across the Sphere (an uncorrupted Shard memory lattice or Precursor null-beam projector). Attainable only as climactic campaign objectives.</li>
            </ul>

            <div class="callout callout-cyan keep-together" style="margin-top: 2mm; padding: 2.5mm 3.5mm;">
                <div class="callout-title" style="font-size: 9.5pt;">Campaign Calibration</div>
                <p style="font-size: 8.0pt; line-height: 1.28;">
                    Game Masters can author bespoke prototypes and relics for their campaigns using the guidelines and balancing invariants documented in the Exotic Equipment Design reference. Exotic systems should always offer distinctive tactical choices rather than simple numerical bloat.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">83</span>
        </div>
    </div>"""
    pages.append(p83)

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
    print(f"Successfully generated {out_path} with {len(pages)} pages (Pages 68 to 83).")

if __name__ == "__main__":
    build_condensed_ch04()
