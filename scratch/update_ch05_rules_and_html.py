#!/usr/bin/env python3
"""
Update Chapter 05 generator and HTML to strictly follow Corsair core rules:
1. Remove Vacuum Physics & Thermal Management on Page 82 and Page 86.
2. Update Contesting Breakaways & Maneuvers on Page 83 to use the standard 8+ elimination rule.
3. Update Tactical Play callout on Page 83 to demonstrate the 8+ elimination contest rule.
4. Update Page 95 combat walkthrough to layout Turns (Player Turn 1, GM Turn 1, Player Turn 2, GM Turn 2) using the 2 AP turn switch.
"""
from pathlib import Path
import re

def update_ch05():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # 1. Page 82: Remove Vacuum Physics & Thermal Management
    p82_old_target = """            <h3>Vacuum Physics &amp; Thermal Management</h3>
            <p>
                In the freezing vacuum of space, heat is an inescapable enemy. Starships generate enormous quantities of thermal energy through fusion reactions, laser capacitors, and high-G drive burns. Because vacuum is an exceptional insulator, heat cannot simply convect away; it must be radiated outward through deployable ceramic radiator arrays or absorbed by onboard heat sinks. When radiator panels are retracted for combat protection, internal compartment temperatures rise rapidly, filling corridors with the smell of scorched insulation and ozone.
            </p>

            <div class="callout callout-cyan" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="callout-title">Doctrine // Hard Sci-Fi Inertial Realism</div>
                <p style="font-size: 8.1pt; line-height: 1.34; margin-bottom: 0;">
                    Spacecraft in the Sphere do not fly like atmospheric aircraft. There is no air resistance to bank against, and shutting down the main drive does not cause a ship to halt; it merely causes the vessel to coast along its ballistic trajectory forever. Combat turns consist of main drive burns, cold-gas RCS rotation, and grueling flip-and-burn decelerations.
                </p>
            </div>"""

    # We replace it with an expanded hard sci-fi inertial navigation section and the clean doctrine callout
    p82_new_target = """            <h3>Inertial Trajectory &amp; Flip-and-Burn Deceleration</h3>
            <p>
                Because vacuum offers zero atmospheric drag, shutting down a vessel's main drive does not bring the ship to a halt; it merely causes the craft to drift along its established vector indefinitely. Changing heading requires firing cold-gas Reaction Control System (RCS) thrusters to pivot the vessel's nose, followed by burning the main fusion drive directly against the vector of travel—a grueling maneuver known among spacers as a flip-and-burn.
            </p>

            <div class="callout callout-cyan" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="callout-title">Doctrine // Hard Sci-Fi Inertial Flight</div>
                <p style="font-size: 8.1pt; line-height: 1.34; margin-bottom: 0;">
                    Starships in the Sphere do not bank or glide like aircraft. Velocity commitments are absolute: every kilonewton of forward momentum imparted by a burn must eventually be counteracted by an equal expenditure of reaction mass and engine thrust to alter vector or achieve orbital capture.
                </p>
            </div>"""

    if p82_old_target in code:
        code = code.replace(p82_old_target, p82_new_target)
        print("Page 82 updated successfully.")
    else:
        print("WARNING: Could not find Page 82 target.")

    # 2. Page 83: Update Contesting Breakaways & Maneuvers + Escaping the Kill Zone callout
    p83_old_target = """            <h3>Contesting Tactical Maneuvers</h3>
            <p>
                Void combat is actively contested. Opposing pilots can burn reaction time and thrusters to deny positional advantage:
            </p>
            <ul>
                <li><strong>Contesting Breakaways (1 AP):</strong> When an opposing ship attempts to break away from your space, you may spend 1 AP to immediately roll <strong>Acceleration</strong> in opposition. If you score a higher result, you execute a movement action on the Macro-Grid immediately after the fleeing ship during their turn. If your movement ends in the same hex, you maintain your position on the Dogfight Scale and climb by the difference in results! G-Strain applies to the sum of all movement.</li>
                <li><strong>Contesting Maneuvers (1 AP):</strong> When an opponent attempts to shift the Dogfight Scale on their turn, you may spend 1 AP to roll <strong>Maneuverability</strong>. Rather than eliminating dice, both vessels fall or climb the Dogfight Scale by the mathematical difference between your roll and the opponent's roll.</li>
            </ul>

            <div class="example-box" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="example-title">Tactical Play // Escaping the Kill Zone</div>
                <p>
                    The crew of the <em>Kestrel</em> is pinned at <strong>Position 2 (Disadvantage)</strong> with a corporate gunboat locked onto their rear quarters. Pilot Jax declares a Full Throttle breakaway burn, rolling Acceleration (3 dice) and scoring 5 Success Points.
                </p>
                <p>
                    Jax spends 2 SPs to shift from Position 2 to Position 4 (Neutral), clearing the engagement envelope. He spends the remaining 3 SPs to accelerate onto the Macro-Grid, moving 1 hex space (spending 2 SPs, with 1 SP unspent). The gunboat spends 1 AP to contest with Acceleration, but rolls only 3 SPs&mdash;failing to match the <em>Kestrel</em>'s speed. Jax successfully breaks contact into open void.
                </p>
            </div>"""

    p83_new_target = """            <h3>Contesting Tactical Maneuvers</h3>
            <p>
                Void combat is actively contested. Opposing pilots can burn reaction time and thrusters to deny positional advantage using standard contest rules:
            </p>
            <ul>
                <li><strong>Contesting Breakaways (1 AP):</strong> When an opposing ship attempts to break away from your dogfight space, a Pilot in the same hex can spend 1 AP to contest the action by rolling a Simple Test with the ship's <strong>Acceleration</strong>. Each Hit (8+) rolled on the contest eliminates one of the highest dice from the fleeing pilot's Acceleration roll. If all 8+ dice are eliminated, the contest succeeds: the fleeing ship scores 0 Success Points and is stopped in its tracks, unable to shift position or leave the hex.</li>
                <li><strong>Contesting Maneuvers (1 AP):</strong> When an opponent attempts a Combat Maneuver to shift the Dogfight Scale, an opposing Pilot can spend 1 AP to contest by rolling a Simple Test with <strong>Maneuverability</strong>. Each Hit (8+) rolled eliminates one of the highest dice from the active pilot's Action Roll. If all 8+ dice are eliminated, the Action Roll fails and the scale does not shift.</li>
            </ul>

            <div class="example-box" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="example-title">Tactical Play // Escaping the Kill Zone</div>
                <p>
                    The crew of the <em>Kestrel</em> is pinned at <strong>Position 2 (Disadvantage)</strong> with a gunboat on their tail. Pilot Jax declares a Full Throttle breakaway burn, making a Success Test with Acceleration (3 dice) and rolling <code>[9, 8, 4]</code>&mdash;yielding 9 Success Points (from the 9).
                </p>
                <p>
                    The gunboat pilot spends 1 AP to contest using Acceleration (3 dice), rolling <code>[8, 5, 2]</code>&mdash;scoring 1 Hit (the 8). The gunboat's Hit eliminates Jax's highest die (<code>9</code>), leaving <code>[8, 4]</code>. The highest remaining die is an 8, so Jax still secures 8 Success Points! Jax spends 2 SPs to climb from Position 2 to Position 4 (Neutral), and uses 4 of the remaining SPs to traverse 2 hexes onto the Macro-Grid, successfully evading the gunboat.
                </p>
            </div>"""

    if p83_old_target in code:
        code = code.replace(p83_old_target, p83_new_target)
        print("Page 83 updated successfully.")
    else:
        print("WARNING: Could not find Page 83 target.")

    # 3. Page 86: Remove Thermal Capacitors & Laser Cooling if present
    p86_therm_target = """            <h3>Thermal Capacitors &amp; Laser Cooling</h3>
            <p>
                Continuous-wave lasers and particle beams do not require solid ammunition, but their operational tempo is bounded by heat rejection. Firing high-output laser arrays dumps gigajoules of thermal energy directly into internal coolant loops. Starships equipped with heavy energy batteries must manage heat sinks carefully to prevent thermal runaway from cooking bridge crew alive.
            </p>"""
    if p86_therm_target in code:
        code = code.replace(p86_therm_target, "")
        print("Page 86 thermal section removed.")

    # 4. Page 95: Re-architect combat walkthrough into Turns following the 2 AP switch
    # Let's locate the page 95 content from <div class="page-body two-columns"> to </div>
    p95_old_walkthrough_pattern = re.compile(
        r'<h2 class="column-span-all" style="margin-top: 0; margin-bottom: 1.5mm;">Combat Walkthrough: The Skirmish at Vesta Void</h2>.*?(?=</div>\s*<div class="page-running-footer">)',
        re.DOTALL
    )

    p95_new_walkthrough = """<h2 class="column-span-all" style="margin-top: 0; margin-bottom: 1.2mm;">Combat Walkthrough: The Skirmish at Vesta Void</h2>
            <p class="column-span-all" style="font-size: 8.1pt; line-height: 1.3; margin-bottom: 1.8mm;">
                To illustrate how orbital vector mechanics, bridge command actions, point-defense screens, and G-Strain interact under <em>Corsair's</em> core rules, observe the following encounter during <strong>Round 1</strong> between the player crew's <strong>RF "Kestrel"</strong> (corvette) and an aggressive pirate <strong>GVI "Rusty Hook"</strong> in the debris belt of Vesta. Both crews begin with <strong>3 AP each</strong>, and control alternates between sides whenever an active side spends <strong>2 or more AP</strong>.
            </p>

            <div class="example-box column-span-all" style="margin: 0 0 1.8mm 0; padding: 2.2mm 2.8mm;">
                <div class="example-title" style="font-size: 8.4pt;">Player Turn 1 (2 AP Spent &mdash; Approach &amp; Interception)</div>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. The Engineer Shunts Power (1 AP):</strong> Sitting in the Engineer seat, Sarah makes a Simple Test with <strong>Systems (3)</strong> + 1 Upgrade (Seat) = 1d12 + 2d10. Rolling <code>[9]</code> on the d12 and <code>[8, 4]</code> on the d10s, she scores <strong>2 Hits</strong>. She allocates both hits as Upgrades to <em>Engines</em> (Acceleration and Maneuverability) until the end of the round. <em>(Sarah: 2 AP left)</em>
                </p>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>2. Pilot Full Throttle (1 AP):</strong> Jax sits in the Pilot seat and executes Full Throttle. Success Test with <strong>Acceleration (3)</strong> + 1 Upgrade (Seat) + 2 Upgrades (Shunt) = 3d12. Rolling <code>[11, 8, 7]</code>, highest die is 11. Jax spends 4 Success Points to traverse 2 hex spaces (2 km) straight into the pirate's hex (0 G-Strain). Moving into the hex grants Jax the <strong>Interception Advantage</strong>: the <em>Kestrel</em> begins at <strong>Position 6 (Attacker Edge)</strong>, the pirate at <strong>Position 5 (Defender Neutral)</strong>. <em>(Jax: 2 AP left)</em>
                </p>
            </div>

            <div class="example-box column-span-all" style="margin: 0 0 1.8mm 0; padding: 2.2mm 2.8mm;">
                <div class="example-title" style="font-size: 8.4pt;">GM Turn 1 (2 AP Spent &mdash; Guided Missile Salvo &amp; Point Defense)</div>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. Pirate Gunner Acquires Lock (1 AP):</strong> At Position 5, the pirate gunner rolls a Simple Test with <strong>Systems (2)</strong>, rolling <code>[8, 3]</code>. The 8 is a Hit! The pirate sacrifices the Hit to establish <strong>1 level of Target Lock</strong> on the <em>Kestrel</em>. <em>(Pirate Gunner: 2 AP left)</em>
                </p>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>2. Harpoon Launch &amp; PDC Reaction (1 AP):</strong> The pirate fires a <strong>KSK "Harpoon" Kinetic Missile</strong> (Tracking 4, Damage +1). Guided Complex Test with Tracking (4 dice) + 1 Upgrade (Target Lock) = 1d12 + 3d10. Action Roll: <code>[10, 8, 5, 2]</code>&mdash;two Hits (10 and 8).<br>
                    &bull; <em>Point Defense Reaction (1 AP):</em> Miller reacts from the Gunner seat with the <strong>PA "Sentinel" Rotary PDC</strong> (Point-Defense 5, +1 Seat Upgrade = 1d12 + 4d10). Simple Test: <code>[9, 8, 7, 6, 2]</code>&mdash;two Hits (9 and 8). Each Hit eliminates a highest die from the missile roll (10 and 8). With zero 8+ dice remaining, the missile is shredded 200m out! <em>(Miller: 2 AP left)</em>
                </p>
            </div>

            <div class="example-box column-span-all" style="margin: 0 0 1.8mm 0; padding: 2.2mm 2.8mm;">
                <div class="example-title" style="font-size: 8.4pt;">Player Turn 2 (2 AP Spent &mdash; Tail Position &amp; Laser Strike)</div>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. Combat Maneuver (1 AP):</strong> Jax executes a Combat Maneuver. Complex Test: <strong>Maneuverability (4) + Instinct (3)</strong> + 3 Upgrades (Seat + Shunt) = 3d12 + 1d10. Action Roll: <code>[11, 9, 8, 6]</code> (three Hits).<br>
                    &bull; <em>Pirate Contest (1 AP):</em> Pirate pilot spends 1 AP to contest with Maneuverability (4d10), rolling <code>[8, 5, 3, 2]</code> (one Hit). The 8 eliminates Jax's highest die (11), leaving <code>[9, 8, 6]</code>. Two Hits remain; Action succeeds! Jax takes Instinct (3) dice: <code>[9, 8, 6]</code>. Highest is 9. Jax spends 3 SPs to advance from Position 6 to <strong>Position 9 (Advantage: On their Tail!)</strong>. <em>(Jax: 1 AP left)</em>
                </p>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>2. Solarflare Laser Strike (1 AP):</strong> Miller fires the <strong>CQV "Solarflare" Laser Array</strong> (Damage +2). Complex Test: Finesse (3) + Advantage Accuracy (2) + 1 Upgrade (Seat) = 1d12 + 2d10. Action Roll: <code>[10, 8, 5]</code> (two Hits; Action succeeds). Success Roll (2 dice): <code>[10, 8]</code>&mdash;highest is 10 SPs! Total Damage: 10 SP + 2 Bonus = 12 damage. Pirate <strong>Armor 2</strong> absorbs 2; <strong>10 penetrating damage</strong> completely fills the pirate's <strong>First Hull Track (10/10 Light Wounds)</strong>! <em>(Miller: 1 AP left)</em>
                </p>
            </div>

            <div class="example-box column-span-all" style="margin: 0 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="example-title" style="font-size: 8.4pt;">GM Turn 2 (2 AP Spent &mdash; Failed Breakaway &amp; Surrender)</div>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. Pirate Desperate Breakaway (1 AP):</strong> Pinned at Position 2 from their view, the pirate pilot executes a Breakaway Burn. Success Test with <strong>Acceleration (2)</strong>: rolls <code>[9, 5]</code> (highest die 9 SPs).<br>
                    &bull; <em>Stay on Target Contest (1 AP):</em> Jax spends his final 1 AP to contest with Acceleration (3) + 1 Upgrade (Seat) = 1d12 + 2d10. Jax rolls <code>[10, 8, 4]</code>&mdash;two Hits (10 and 8)! Jax's two Hits eliminate both the 9 and 5 from the pirate's roll! With zero 8+ dice remaining, the contest succeeds: Breakaway yields <strong>0 SPs</strong>! The pirate remains pinned at Position 2. <em>(Jax: 0 AP left)</em>
                </p>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>2. Pirate Surrender (1 AP):</strong> Trapped before the charged laser array with hull plating ruptured, the pirate captain spends their final AP to vent thrusters and broadcast emergency surrender: <em>"Cease fire, Kestrel! We're dead in the water! We surrender!"</em>
                </p>
            </div>"""

    code = p95_old_walkthrough_pattern.sub(p95_new_walkthrough, code)
    print("Page 95 walkthrough updated.")

    src_file.write_text(code, encoding="utf-8")
    print("scratch/generate_ch05_starships.py updated and written.")

if __name__ == "__main__":
    update_ch05()
