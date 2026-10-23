# -*- coding: utf-8 -*-
"""
Applies targeted height tuning and 0px overflow fixes to scratch/generate_ch04_zero_voids.py.
"""
from pathlib import Path
import re

gen_file = Path("scratch/generate_ch04_zero_voids.py")
content = gen_file.read_text(encoding="utf-8")

# 1. PAGE 69: Tactical Doctrine callout + adjusted font-size/line-height
new_p69 = """    <!-- =========================================================================
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

# 2. PAGE 70: Workshop Fabrication + Range Bands & RoF detail
new_p70 = """    <!-- =========================================================================
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
            <p style="font-size: 8.2pt; line-height: 1.32; margin-bottom: 0;">
                <strong>Panthera Arms:</strong> Sleek high-tolerance carbines and marksman rifles favored by corporate strike teams. &middot; <strong>Vandal's Workshop:</strong> Stamped-sheet high-RoF submachine guns cycling reliably in dirt and vacuum. &middot; <strong>Caldera Foundry:</strong> Heavy-bore rifles and trench shotguns for boarding defense. &middot; <strong>Ker'Satz Korp:</strong> Precision magnetic rail drivers and magnum revolvers. &middot; <strong>Chidori-Qwei:</strong> Lightweight polymer smart-linked sidearms.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">70</span>
        </div>
    </div>"""

# 3. PAGE 72: Bipod bracing paragraph + balanced callout
new_p72 = """    <!-- =========================================================================
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

            <div class="callout callout-tactical keep-together column-span-all" style="margin: 1.5mm 0 0 0; padding: 2.8mm 3.2mm;">
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

# 4. PAGE 73: Ammunition, Optics Calibration & Vacuum Heat Dissipation
new_p73 = """    <!-- =========================================================================
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

# 5. PAGE 77: Medium & Heavy Armor tables (0px overflow) + Carapace note
new_p77 = """    <!-- =========================================================================
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
                            <th style="padding: 0.9mm 0.7mm; width: 20%;">Armor Name</th>
                            <th style="padding: 0.9mm 0.7mm; width: 9%;">Prot</th>
                            <th style="padding: 0.9mm 0.7mm; width: 9%;">Load</th>
                            <th style="padding: 0.9mm 0.7mm; width: 18%;">Properties</th>
                            <th style="padding: 0.9mm 0.7mm; width: 13%;">Cost</th>
                            <th style="padding: 0.9mm 0.7mm; width: 31%;">Description</th>
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
                            <th style="padding: 0.9mm 0.7mm; width: 20%;">Armor Name</th>
                            <th style="padding: 0.9mm 0.7mm; width: 9%;">Prot</th>
                            <th style="padding: 0.9mm 0.7mm; width: 9%;">Load</th>
                            <th style="padding: 0.9mm 0.7mm; width: 18%;">Properties</th>
                            <th style="padding: 0.9mm 0.7mm; width: 13%;">Cost</th>
                            <th style="padding: 0.9mm 0.7mm; width: 31%;">Description</th>
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
                Due to the sheer mass and joint resistance of heavy carapace, operators frequently utilize powered servo-joints and load-distribution harnesses to maintain stability during violent close-quarters room breaches.
            </p>

            <div class="callout callout-tactical keep-together" style="margin: 1.5mm 0 1.5mm 0; padding: 2.5mm 3.0mm;">
                <div class="callout-title" style="font-size: 8.4pt; margin-bottom: 1mm;">Tactical Doctrine: Stacking Defenses &amp; Breaching Operations</div>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1mm;">
                    Because Armor Protection stacks directly with defensive bonuses provided by <strong>Shields</strong> and <strong>Cover</strong>, a defensive operative can achieve formidable damage negation. An operative in Tactical Battleplate (5 Protection) bracing behind a Riot Shield (+2) in Medium Cover (+2) achieves <strong>9 total Protection</strong>, mitigating an entire volley of rifle fire before taking a single scratch.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 0;">
                    During room breaches, combining heavy carapace with an Active Protection System (APS Beacon) creates an impenetrable foothold. The beacon detonates incoming fragmentation grenades mid-flight, while the breacher's heavy plating absorbs suppressive small arms fire without suffering armor breaches.
                </p>
            </div>

            <div class="callout callout-tactical keep-together" style="margin: 0; padding: 2.5mm 3.0mm;">
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

# 6. PAGE 79: Tighten bottom gap
new_p79 = """    <!-- =========================================================================
         PAGE 79 (Spread 6 Right) — FORTIFICATIONS & EXPLOSIVES RIGS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="gear-fortifications-explosives">
        <div class="page-running-header">
            <span>Chapter 04: Fortifications &amp; Munitions</span>
            <span>Volume I // Core Rulebook</span>
        </div>

        <div class="page-body two-columns">
            <h3 style="margin-top: 0;">2. Fortification Gear</h3>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.4mm;">
                Deployable fortifications provide instant cover, automated defense, and remote weapon platforms across contested ship corridors and perimeter defense zones.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1.8mm 0;">
                <div class="table-header">Fortification Gear Catalog</div>
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

            <h4 style="margin-top: 1mm;">Fortification Special Properties</h4>
            <ul style="font-size: 8.0pt; line-height: 1.28; margin-bottom: 1.8mm;">
                <li><strong>Deployable Cover:</strong> 1 AP to deploy or pack up. Grants listed Protection bonus (+1 to +3) to shelterers. Possesses own Cover HP and Innate Protection. Recover for 1 AP.</li>
                <li><strong>Intercept (X) &amp; Area Defense:</strong> Gains <strong>1 Free Reaction AP per round</strong> to contest incoming Area Attacks and Ordnance explosions, rolling pure Intercept (X). If no dice 8+ remain, munition is destroyed.</li>
                <li><strong>Automount (X):</strong> 1 AP to deploy and mount weapon. Spend 1 AP to fire remotely: rolls Automount (X) + Finesse (or pure Automount if autonomous). Recover for 1 AP.</li>
            </ul>

            <h3 style="margin-top: 1.5mm;">3. Explosives &amp; Launchers</h3>
            <p style="font-size: 8.1pt; line-height: 1.30; margin-bottom: 1.4mm;">
                Explosives deliver high-yield area destruction, obscuration, and tactical disruption. Rather than tracking individual loose throwables, combatants carry refillable <strong>Grenade Rigs</strong> that allow on-the-fly munition selection at the point of use.
            </p>

            <div class="table-container keep-together" style="margin: 1mm 0 1.8mm 0;">
                <div class="table-header">Explosives &amp; Launchers Catalog</div>
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

            <h4 style="margin-top: 1mm;">Munition Profiles &amp; Explosives Properties</h4>
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

# 7. PAGE 80: Bulleted technical actions + slightly larger font
new_p80 = """    <!-- =========================================================================
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

# Replace in content using regex pattern matching on the variable assignments
pattern_p69 = r'    p69 = """    <!-- =========================================================================\n         PAGE 69 .*?    </div>"""'
content = re.sub(pattern_p69, f'    p69 = """{new_p69.strip()}"""', content, flags=re.DOTALL)

pattern_p70 = r'    p70 = """    <!-- =========================================================================\n         PAGE 70 .*?    </div>"""'
content = re.sub(pattern_p70, f'    p70 = """{new_p70.strip()}"""', content, flags=re.DOTALL)

pattern_p72 = r'    p72 = """    <!-- =========================================================================\n         PAGE 72 .*?    </div>"""'
content = re.sub(pattern_p72, f'    p72 = """{new_p72.strip()}"""', content, flags=re.DOTALL)

pattern_p73 = r'    p73 = """    <!-- =========================================================================\n         PAGE 73 .*?    </div>"""'
content = re.sub(pattern_p73, f'    p73 = """{new_p73.strip()}"""', content, flags=re.DOTALL)

pattern_p77 = r'    p77 = """    <!-- =========================================================================\n         PAGE 77 .*?    </div>"""'
content = re.sub(pattern_p77, f'    p77 = """{new_p77.strip()}"""', content, flags=re.DOTALL)

pattern_p79 = r'    p79 = """    <!-- =========================================================================\n         PAGE 79 .*?    </div>"""'
content = re.sub(pattern_p79, f'    p79 = """{new_p79.strip()}"""', content, flags=re.DOTALL)

pattern_p80 = r'    p80 = """    <!-- =========================================================================\n         PAGE 80 .*?    </div>"""'
content = re.sub(pattern_p80, f'    p80 = """{new_p80.strip()}"""', content, flags=re.DOTALL)

gen_file.write_text(content, encoding="utf-8")
print("Updated scratch/generate_ch04_zero_voids.py successfully!")
