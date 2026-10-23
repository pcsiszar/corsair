# -*- coding: utf-8 -*-
"""
Fine-tunes p70, p72, p73, p77, and p79 in scratch/generate_ch04_zero_voids.py
to eliminate remaining bottom voids while guaranteeing 0px horizontal overflow.
"""
from pathlib import Path
import re

gen_file = Path("scratch/generate_ch04_zero_voids.py")
content = gen_file.read_text(encoding="utf-8")

# --- REFINED P70 (Adds Tactical Doctrine callout) ---
p70_code = '''    p70 = """<!-- =========================================================================
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
    </div>"""'''

# --- REFINED P72 (Increases callout padding) ---
p72_code = '''    p72 = """<!-- =========================================================================
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
    </div>"""'''

# --- REFINED P79 (Increases margins and line height) ---
p79_code = '''    p79 = """<!-- =========================================================================
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
    </div>"""'''

# Precise replacements using start / end boundaries
# 1. p70
start_p70 = content.find('    p70 = """')
end_p70 = content.find('    pages.append(p70)', start_p70)
if start_p70 != -1 and end_p70 != -1:
    content = content[:start_p70] + p70_code + "\n" + content[end_p70:]
    print("Replaced p70")

# 2. p72
start_p72 = content.find('    p72 = """')
end_p72 = content.find('    pages.append(p72)', start_p72)
if start_p72 != -1 and end_p72 != -1:
    content = content[:start_p72] + p72_code + "\n" + content[end_p72:]
    print("Replaced p72")

# 3. p79
start_p79 = content.find('    p79 = """')
end_p79 = content.find('    pages.append(p79)', start_p79)
if start_p79 != -1 and end_p79 != -1:
    content = content[:start_p79] + p79_code + "\n" + content[end_p79:]
    print("Replaced p79")

gen_file.write_text(content, encoding="utf-8")
print("Done writing to scratch/generate_ch04_zero_voids.py")
