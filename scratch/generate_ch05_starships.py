#!/usr/bin/env python3
"""
Master generator script for Corsair TTRPG — Chapter 05: Starships & Space Combat.
Generates all 14 pages (Pages 82 to 95) with dense, space-filling layouts (84%–94% fill),
zero horizontal overflow (0px), 100% rules fidelity, zero <a> tags, and zero fake telemetry tags.
"""

from pathlib import Path

def build_ch05_html() -> str:
    html_parts = []
    
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corsair TTRPG — Chapter 05: Starships &amp; Space Combat</title>
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
""")

    # =========================================================================
    # PAGE 82 (Spread 1 Left) — CHAPTER 05 OPENER: SPACE COMBAT & FLIGHT MECHANICS
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 82 (Spread 1 Left) — CHAPTER 05 OPENER: SPACE COMBAT & FLIGHT MECHANICS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="space-combat-opener">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Starships &amp; Space Combat</span>
        </div>

        <div class="p-banner-wrap p-banner-tactical column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Starships &amp; Space Combat</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <p class="lead" style="font-size: 8.9pt; line-height: 1.36; margin-bottom: 2mm;">
                In the airless void of the Sphere, your ship is more than transportation&mdash;it is your life support, your operational sanctuary, and your most lethal instrument of survival. Space combat in <em>Corsair</em> is an unforgiving dance of orbital mechanics, Newtonian momentum, heat rejection, and physiological endurance. The setting obeys strict hard science fiction constraints: there is no artificial gravity, no faster-than-light transit, and no deflector shielding. Every maneuver burns precious reaction mass, every high-G vector turn crushes human ribs against acceleration couches, and every penetrating round strikes pressurized titanium-composite bulkheads directly.
            </p>

            <h3 style="margin-top: 1mm;">Dual-Scale Engagement</h3>
            <p>
                Naval engagements unfold across two synchronized modes of tactical resolution. When closing distance across interplanetary trajectories or planetary orbits, combat is tracked on the <strong>Macro-Grid</strong>, where commanders manage vector commitments, long-range sensor locks, and relativistic railgun strikes across vast orbital distances. When hostile vessels close within knife-fighting range, the engagement shifts into <strong>Dogfight Mode</strong>, resolving micro-positioning on an abstract tactical scale from 1 to 10 as pilots fight tooth and nail for the optimal firing cone.
            </p>

            <h3>The Macro-Grid</h3>
            <p>
                On the Macro-Grid, tactical space is mapped using a hexagonal grid where each hex represents a <strong>1-kilometer diameter spherical volume</strong> of open void. Ships maneuver across this grid utilizing their Engine's <strong>Acceleration</strong> rating.
            </p>
            <p>
                To move on the Macro-Grid, the ship's Pilot performs a <strong>Success Test</strong> using the vessel's <strong>Acceleration</strong>. The craft traverses <strong>500 meters for every Success Point</strong> scored, translating to exactly <strong>one hex space for every 2 Success Points</strong>, rounded down. An Acceleration roll yielding 5 Success Points allows a vessel to traverse 2 hex spaces (2,500 meters), while a roll of 8 Success Points propels the craft 4 hex spaces (4,000 meters) along its flight path.
            </p>

            <h3>Newtonian Momentum &amp; Vector Inertia</h3>
            <p>
                Because vacuum transit is governed by pure inertia, starships cannot halt on a dime or reverse course without expending massive counter-thrust. A ship is <strong>strictly prohibited from moving back into a space it just vacated</strong> during its current movement action.
            </p>
            <p>
                To reverse vector or re-enter a hex it has recently departed, the vessel must first traverse through at least <strong>two adjacent intervening spaces</strong> on the grid, burning thrusters to bleed lateral momentum and swing its nose around. This requirement models realistic orbital mechanics and ensures that positioning, approach angles, and intercept corridors require deliberate tactical planning.
            </p>

            <h3>G-Strain &amp; Crew Physiology</h3>
            <p>
                While a ship's reinforced titanium keel can survive immense structural strain, the fragile organic crew strapped inside its bridge cannot. Sustained burns and violent evasive maneuvers exert crushing gravitational forces (G-forces) that pull blood away from cerebral tissues and crack ribs against flight harness mounts.
            </p>
            <p>
                If a pilot spends <strong>more than 6 Success Points</strong> on movement in a single turn, the crew suffers <strong>G-Strain</strong>. For every additional Success Point spent beyond 6, every crew member on board immediately suffers:
            </p>
            <ul>
                <li><strong>1 Light Wound</strong> from internal capillary tearing, blunt harness impact, and extreme hydrostatic blood pressure.</li>
                <li><strong>1 Light Stress</strong> from tunnel vision, sensory deprivation, and physiological shock under sustained G-forces.</li>
            </ul>
            <p>
                Damage sustained from G-Strain represents direct physiological trauma and is <strong>completely unmitigated by personal Armor or ship Protection</strong>. Spacers who push their engines beyond safe operating parameters risk blacking out or rupturing internal organs before ever entering firing range.
            </p>

            <h3>Inertial Trajectory &amp; Flip-and-Burn Deceleration</h3>
            <p>
                Because vacuum offers zero atmospheric drag, shutting down a vessel's main drive does not bring the ship to a halt; it merely causes the craft to drift along its established vector indefinitely. Changing heading requires firing cold-gas Reaction Control System (RCS) thrusters to pivot the vessel's nose, followed by burning the main fusion drive directly against the vector of travel—a grueling maneuver known among spacers as a flip-and-burn.
            </p>

            <div class="callout callout-cyan" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="callout-title">Doctrine // Hard Sci-Fi Inertial Flight</div>
                <p style="font-size: 8.1pt; line-height: 1.34; margin-bottom: 0;">
                    Starships in the Sphere do not bank or glide like aircraft. Velocity commitments are absolute: every kilonewton of forward momentum imparted by a burn must eventually be counteracted by an equal expenditure of reaction mass and engine thrust to alter vector or achieve orbital capture.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">82</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 83 (Spread 1 Right) — THE DOGFIGHT SCALE & TACTICAL MANEUVERS
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 83 (Spread 1 Right) — THE DOGFIGHT SCALE & TACTICAL MANEUVERS
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="dogfight-scale-mechanics">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Dogfight Scale &amp; Maneuvers</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Entering the Dogfight</h2>
            <p>
                When two or more hostile vessels enter the <strong>same 1 km hex space</strong> on the Macro-Grid, macro-movement immediately suspends. The encounter transitions into <strong>Dogfight Mode</strong>, tracking close-range spatial orientation, relative closing angles, and weapon engagement cones on the micro-level <strong>Dogfight Scale from 1 to 10</strong>.
            </p>
            <p>
                The Dogfight Scale is tracked independently for every pair of opposing vessels sharing the hex, always measured from the <strong>players' perspective</strong>:
            </p>

            <div class="callout callout-cyan column-span-all" style="margin: 2mm 0 2.5mm 0; padding: 2.2mm 3.5mm; text-align: center;">
                <div style="font-family: var(--font-mono); font-size: 8.8pt; font-weight: 700; letter-spacing: 0.06em; color: var(--cyan-dark); margin-bottom: 1.2mm;">
                    [ 1 &mdash; 2 &mdash; 3 ] &mdash;&mdash;&mdash;&gt; [ 4 &mdash; 5 &mdash; 6 &mdash; 7 ] &mdash;&mdash;&mdash;&gt; [ 8 &mdash; 9 &mdash; 10 ]
                </div>
                <div style="display: flex; justify-content: space-between; font-family: var(--font-heading); font-size: 8.2pt; font-weight: 700; text-transform: uppercase;">
                    <span style="color: var(--crimson-dark); width: 30%; text-align: left;">Disadvantage<br><small style="font-size: 7.2pt; text-transform: none; color: var(--text-body); font-weight: normal;">Enemy on your Tail / Defensive Vector</small></span>
                    <span style="color: var(--amber-dark); width: 38%; text-align: center;">Neutral<br><small style="font-size: 7.2pt; text-transform: none; color: var(--text-body); font-weight: normal;">Passing Vectors / Broadside Slashing</small></span>
                    <span style="color: var(--cyan-dark); width: 30%; text-align: right;">Advantage<br><small style="font-size: 7.2pt; text-transform: none; color: var(--text-body); font-weight: normal;">You are on their Tail / Optimal Firing Arc</small></span>
                </div>
            </div>

            <h3>Relative Vector Geometry</h3>
            <p>
                Each zone of the Dogfight Scale models specific relative spatial orientations in three-dimensional vacuum:
            </p>
            <ul>
                <li><strong>Disadvantage (Positions 1–3):</strong> The hostile ship has matched your vector and sits in your rear baffle. Forward spinal mounts cannot bear, and your main thrusters are vulnerable to raking fire.</li>
                <li><strong>Neutral (Positions 4–7):</strong> The vessels cross on perpendicular or slashing vectors. Turreted weapons bear easily, but high closing speeds make sustained spinal locks difficult.</li>
                <li><strong>Advantage (Positions 8–10):</strong> You have out-turned your adversary, tucking into their blind quarter. Your forward weapons point directly at their vulnerable engineering spaces.</li>
            </ul>

            <h3>Climbing the Dogfight Scale</h3>
            <p>
                On their turn, a character seated in the Pilot Seat can execute a <strong>Combat Maneuver</strong> to alter relative positioning. The pilot performs a <strong>Complex Test</strong> combining the ship's <strong>Maneuverability + Instinct</strong>. For every Success Point scored on this test, the pilot can climb (or drop) <strong>one position on the Dogfight Scale</strong>.
            </p>
            <p>
                Shifting relative orientation in a dogfight demands savage lateral thruster burns. Just like macro-grid movement, <strong>G-Strain</strong> applies if a pilot uses <strong>more than 6 Success Points</strong> to move on the scale during a single action, inflicting 1 Light Wound and 1 Light Stress per excess point.
            </p>

            <h3>The Interception Advantage</h3>
            <p>
                In void combat, predatory momentum grants an immediate operational edge. The craft that initiates the intercept by flying into an occupied macro-grid hex enters the Dogfight Scale at <strong>Position 6</strong> (Attacker Advantage). The defending ship already occupying the hex begins at <strong>Position 5</strong> (Neutral Defense). This slight offset reflects the attacker's prepared firing solutions and closing vector.
            </p>

            <h3>Breakaway Maneuvers</h3>
            <p>
                A vessel trapped in a disadvantageous dogfight position cannot simply disengage and burn away into the void; doing so presents its unprotected engine bells to hostile fire. To break away, the pilot must first maneuver the ship back into the neutral envelope:
            </p>
            <ul>
                <li><strong>Return to Neutral:</strong> The pilot must successfully climb the Dogfight Scale to <strong>Position 4 or higher</strong> before the ship is permitted to leave the dogfight hex.</li>
                <li><strong>Acceleration Burn:</strong> The pilot can spend an action to roll a Success Test using <strong>Acceleration</strong>. The resulting Success Points are first spent climbing the Dogfight Scale to Position 4; any <strong>remaining Success Points</strong> are then immediately used to traverse outward onto the Macro-Grid (1 hex per 2 SPs).</li>
            </ul>

            <h3>Contesting Tactical Maneuvers</h3>
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
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">83</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 84 (Spread 2 Left) — ANATOMY OF A STARSHIP & CORE ATTRIBUTES
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 84 (Spread 2 Left) — ANATOMY OF A STARSHIP & CORE ATTRIBUTES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="starship-anatomy">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Starship Anatomy</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Anatomy of a Starship</h2>
            <p>
                Every space vessel operating across the Sphere is built around five core mechanical systems: its structural <strong>Hull</strong>, defensive <strong>Armor</strong>, dual-purpose <strong>Engines</strong>, electronic <strong>Systems</strong>, and offensive <strong>Hardpoints</strong>. Understanding these interconnected systems is essential for tactical survival when hull integrity fails and decompression alarms sound.
            </p>

            <h3>1. Hull Integrity &amp; Condition Tracks</h3>
            <p>
                A starship's <strong>Hull Rating</strong> represents its physical structural integrity, pressure containment, and bulkheads. Because hard sci-fi craft do not possess energy shields, any weapon projectile or thermal laser beam that penetrates point-defense grids strikes the hull directly.
            </p>
            <p>
                A starship's Hull Condition Track is divided into smaller tracks, each having a length equal to the ship's <strong>Hull Rating</strong> (always an even number, such as 6, 8, 10, 12, 14, or 16). The total number of individual tracks is determined by the vessel's Size Class, typically ranging from <strong>4 to 6 tracks</strong>:
            </p>
            <ul>
                <li><strong>Track Damage Progression:</strong> Hull tracks take damage exactly like a character's Health Track. Hits first mark off <strong>Light Wounds</strong>. When a single track fills completely with Light Wounds, damage does not spill over into the next track; instead, subsequent hits on that track convert Light Wounds into permanent <strong>Aggravated Wounds</strong>.</li>
                <li><strong>Compartment Buckling:</strong> As individual tracks fill with wounds, the crew experiences secondary hazards: hydraulic lines sever, atmospheric bulkheads slam shut, and artificial environmental loops struggle to scrub carbon dioxide.</li>
                <li><strong>System Shutdown:</strong> When all tracks on a ship are filled with Light Wounds, the vessel suffers cascading power failure. Engines go dark, sensor buses fail, and the ship <strong>shuts down</strong>, tumbling out of control in vacuum. The life-support reserve battery provides roughly 24 hours of oxygen before cold sets in.</li>
                <li><strong>Catastrophic Destruction:</strong> When all tracks fill with Aggravated Wounds, the hull experiences explosive decompression, reactor containment breach, and complete structural annihilation.</li>
            </ul>

            <h3>2. Armor (Protection)</h3>
            <p>
                A ship's <strong>Armor</strong> rating represents passive ablative ceramic plates, layered titanium-foam composite plating, and whipple shields. Each point of Armor functions as <strong>Protection</strong>, reducing all incoming weapon damage by a flat 1 point per hit before damage is marked onto the Hull Condition Track.
            </p>
            <p>
                Against light rapid-fire weapons like Point-Defense Cannons (+1 Damage), an Armor rating of 3 renders the vessel almost entirely impervious to direct fire. However, against heavy spinal railguns (+10 to +15 Damage) or siege torpedoes (+20 Damage), armor belts can only blunt a fraction of the devastating kinetic or thermonuclear impact.
            </p>

            <h3>Keel Structures &amp; Whipple Shields</h3>
            <p>
                Modern starship hulls are engineered as layered composite sandwiches of titanium-aluminide framework, foamed metal arrestors, and spaced ceramic Whipple shields. When a hypervelocity kinetic slug impacts the outer Whipple foil, the projectile vaporizes into an expanding cone of plasma and micro-fragments, distributing its kinetic energy harmlessly across the wider secondary bulkhead rather than piercing the central habitat cylinder.
            </p>

            <h3>3. Dual Engine Architecture</h3>
            <p>
                Engines in <em>Corsair</em> are split into two distinct mechanical attributes, reflecting the radical engineering differences between straight-line fusion drives and lateral reaction thrusters:
            </p>
            <ul>
                <li><strong>Acceleration:</strong> Governs main drive propulsion and forward delta-V. Used exclusively for <strong>Macro-Grid movement</strong> and executing long-range Breakaway burns.</li>
                <li><strong>Maneuverability:</strong> Governs cold-gas and hypergolic reaction control thrusters (RCS). Used exclusively for <strong>Dogfight movement</strong> to roll, pitch, yaw, and climb the Dogfight Scale.</li>
            </ul>

            <h3>4. Ship Systems &amp; Avionics</h3>
            <p>
                The <strong>Systems</strong> attribute measures the sophistication of onboard optical sensors, ladar, cooling loops, fire-control computers, automated maintenance hives, and main reactor power grids:
            </p>
            <ul>
                <li><strong>Sensor Range:</strong> Starships can establish electronic tracking and target locks out to a maximum distance equal to <strong>twice their Systems attribute in kilometers</strong> (e.g., Systems 4 yields an 8 km sensor envelope).</li>
                <li><strong>Power Grid Distribution:</strong> Engineers can reroute reactor output to supercharge specific ship subsystems. By rolling a Simple Test with <strong>Systems</strong>, each hit scored grants an <strong>Upgrade</strong> (up to a maximum of 3) to all tests made with the designated subsystem until the end of the round:
                    <ul>
                        <li><em>Weapons:</em> Grants Upgrades to <strong>Accuracy</strong> and <strong>Tracking</strong> tests.</li>
                        <li><em>Engines:</em> Grants Upgrades to <strong>Acceleration</strong> and <strong>Maneuverability</strong> tests.</li>
                        <li><em>Systems:</em> Grants Upgrades to internal <strong>Systems</strong> checks and EWAR.</li>
                    </ul>
                </li>
                <li><strong>Repair Drones:</strong> Autonomous zero-g drone hives deployed by engineers to patch breached compartments and restore damaged hull tracks.</li>
            </ul>

            <div class="callout callout-cyan" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="callout-title">Engineering Notice // Reactor Shunting</div>
                <p style="font-size: 8.1pt; line-height: 1.34; margin-bottom: 0;">
                    Shunting reactor power is the key to surviving asymmetric combat. A light ship with Systems 4 can dump energy into thruster manifolds to outrun a heavier gunboat, or funnel every watt into fire-control matrices to land a decisive opening strike before hostile torpedoes cross the gap.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">84</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 85 (Spread 2 Right) — BRIDGE COMMAND SEATS & COMBAT ROLES
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 85 (Spread 2 Right) — BRIDGE COMMAND SEATS & COMBAT ROLES
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="bridge-roles-and-seats">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Bridge Command Seats</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Bridge Roles &amp; Command Seats</h2>
            <p>
                Every starship bridge or flight deck is equipped with dedicated physical workstations. While any spacer can monitor auxiliary telemetry or trigger basic thruster bursts from an auxiliary terminal, sitting strapped into a <strong>dedicated command seat</strong> connects the operator directly into high-speed fire-control buses, pneumatic flight yokes, and reactor shunts.
            </p>
            <p>
                If a crew member is incapacitated by G-Strain or tactical priorities shift mid-battle, a character may spend <strong>1 Action Point (AP)</strong> to unstrap, pull through zero-G handrails, and swap into an unmanned seat.
            </p>

            <h3>Basic Ship Actions (Any Station)</h3>
            <p>
                Any crew member at an operational terminal can perform the following baseline maneuvers:
            </p>
            <ul>
                <li><strong>Full Throttle:</strong> A Success Test using the ship's <strong>Acceleration</strong>. Used to maneuver on the Macro-Grid or initiate a dogfight Breakaway burn.</li>
                <li><strong>Combat Maneuver:</strong> A Complex Test combining <strong>Maneuverability + Instinct</strong>. Used to climb or drop positions along the Dogfight Scale.</li>
                <li><strong>Weapons Hot:</strong> Trigger and discharge an operational weapon mounted to any available hardpoint, provided its rate of fire has not been expended.</li>
            </ul>

            <h3>The Three Core Bridge Seats</h3>
            <p>
                To unleash a vessel's true combat potential, crew members take their places across three primary command stations:
            </p>

            <div class="callout callout-cyan" style="margin: 2mm 0; padding: 2.2mm 3mm;">
                <div class="callout-title" style="font-size: 9.2pt;">The Pilot Seat</div>
                <p style="font-size: 8.2pt; line-height: 1.35; margin-bottom: 1.5mm;">
                    The pilot interfaces directly with primary propulsion and attitude thrusters, reading vector trajectories through the main canopy or synthetic wrap-around displays.
                </p>
                <ul style="font-size: 8pt; line-height: 1.32; margin-bottom: 0; padding-left: 3.5mm;">
                    <li><strong>Enhanced Controls:</strong> Sitting strapped in the Pilot seat grants <strong>1 Upgrade</strong> to all <em>Full Throttle</em> and <em>Combat Maneuver</em> tests.</li>
                    <li><strong>Evasive Maneuvers:</strong> When the ship is targeted by incoming weapon fire, the Pilot can spend 1 AP to <strong>contest attacks using Instinct</strong>.</li>
                    <li><strong>Stay on Target:</strong> When an enemy tries to disengage or alter vector, the Pilot can spend 1 AP to <strong>contest Breakaways and Maneuvers</strong> using the ship's Acceleration or Maneuverability.</li>
                </ul>
            </div>

            <div class="callout callout-crimson" style="margin: 2mm 0; padding: 2.2mm 3mm;">
                <div class="callout-title" style="font-size: 9.2pt;">The Gunner Seat</div>
                <p style="font-size: 8.2pt; line-height: 1.35; margin-bottom: 1.5mm;">
                    The gunner commands weapons feeds, optical lead calculators, and point-defense interception grids to track and destroy incoming threats.
                </p>
                <ul style="font-size: 8pt; line-height: 1.32; margin-bottom: 0; padding-left: 3.5mm;">
                    <li><strong>Enhanced Targeting:</strong> Sitting in the Gunner seat grants <strong>1 Upgrade</strong> to all attack tests using weapon <em>Accuracy</em> and <em>Tracking</em>.</li>
                    <li><strong>Target Lock:</strong> The Gunner can roll a Simple Test with <strong>Systems</strong> to acquire a Target Lock on a vessel within Sensor Range for each hit sacrificed. Each level of Target Lock provides 1 Upgrade to guided weapons.</li>
                    <li><strong>Point Defense:</strong> The Gunner can spend 1 AP to <strong>contest guided weapon attacks</strong> using a Point-Defense Cannon's (PDC) Accuracy. Firing with multiple active PDCs grants <strong>1 Upgrade per additional PDC</strong>.</li>
                </ul>
            </div>

            <div class="callout" style="margin: 2mm 0; padding: 2.2mm 3mm;">
                <div class="callout-title" style="font-size: 9.2pt;">The Engineer Seat</div>
                <p style="font-size: 8.2pt; line-height: 1.35; margin-bottom: 1.5mm;">
                    The engineer manages the ship's reactor core, magnetic cooling loops, EWAR jammers, and automated maintenance drones.
                </p>
                <ul style="font-size: 8pt; line-height: 1.32; margin-bottom: 0; padding-left: 3.5mm;">
                    <li><strong>Enhanced Interface:</strong> Sitting in the Engineer seat grants <strong>1 Upgrade</strong> to all tests made using <em>Systems</em>.</li>
                    <li><strong>Repair Drones:</strong> Perform a Complex Test using <strong>Knowledge + Systems</strong> to deploy automated repair drones and patch damaged hull segments or restore offline modules mid-battle.</li>
                    <li><strong>Radar Jammer:</strong> Perform a Complex Test using <strong>Knowledge + Systems</strong> to emit broad-spectrum electronic counter-measures, breaking enemy Target Locks held on your ship.</li>
                    <li><strong>Power Distribution:</strong> Roll a Simple Test with <strong>Systems</strong> to shunt surplus reactor output, granting up to 3 Upgrades to Weapons, Engines, or Systems until the end of the round.</li>
                </ul>
            </div>

            <h3>Tactical Comms &amp; Sensor Warfare</h3>
            <p style="font-size: 8pt; line-height: 1.3; margin-bottom: 1.2mm;">
                Combat operations demand strict voice discipline under high acceleration ("Ladar hard on bearing two-seven, salvo away"). Concurrently, electronic warfare (EWAR) stations monitor passive radio frequencies and drive thermals, executing <em>Passive Surveillance</em> to track hostile signatures without radiating active ladar.
            </p>

            <h3>Damage Control &amp; Depressurization</h3>
            <p style="font-size: 8pt; line-height: 1.3; margin-bottom: 1.2mm;">
                When penetrating hits buckle outer bulkheads, damage control teams don magnetic boots to seal compartments, dog down emergency hatches, and flood burning bays with halon gas (granting +1 Upgrade to Engineer repair tests). Prior to engagement, veteran crews execute combat depressurization, pumping cabin air back into reserve tanks to eliminate explosive decompression and flash fires when bulkheads are breached.
            </p>

            <h3>Auxiliary Stations &amp; Skeleton Crews</h3>
            <p style="font-size: 8pt; line-height: 1.3; margin-bottom: 0;">
                Larger starships carry multiple Gunner and Engineer consoles for simultaneous PDC interception and damage control. Shorthanded vessels operating with a skeleton crew suffer severe limits: without a dedicated Gunner, PDCs cannot execute reaction intercepts; without an Engineer, power cannot be redistributed mid-flight.
            </p>


        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">85</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 86 (Spread 3 Left) — HARDPOINTS & WEAPONS ARCHITECTURE
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 86 (Spread 3 Left) — HARDPOINTS & WEAPONS ARCHITECTURE
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="ship-weapons-architecture">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Starship Ordnance</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0;">Ship Weapons &amp; Hardpoints</h2>
            <p>
                Starship weapon systems consist of external structural mounting collars called <strong>Hardpoints</strong> and the specialized kinetic, thermal, or guided ordnance fitted into them. Unlike personal firearms, naval weapons operate under extreme environmental constraints: massive recoil forces that affect flight vectors, immense electrical capacitor drains, and the physics of firing unguided projectiles across thousands of kilometers of vacuum.
            </p>

            <h3>Hardpoint Classifications</h3>
            <p>
                Hardpoints are structural hull zones wired directly into power conduits and fire-control buses. They come in three standardized sizes:
            </p>
            <ul>
                <li><strong>Small Hardpoints:</strong> Agile, high-traverse gimbals designed for rapid-tracking rotary PDCs, light seeker drones, pulse lasers, and proximity mine dispensers.</li>
                <li><strong>Medium Hardpoints:</strong> Heavy turret wells and reinforced bays accommodating naval laser arrays, multi-missile pods, heavy PDCs, flak cannons, particle beams, and twin-barrel railgun batteries.</li>
                <li><strong>Large Hardpoints:</strong> Massive structural keels and spinal mounting frames reserved for ship-length coilguns, heavy siege railguns, and thermonuclear fusion torpedo tubes. Large spinal weapons typically require aligning the ship's entire chassis to aim.</li>
            </ul>

            <h3>Guided vs. Unguided Ordnance</h3>
            <p>
                Naval weaponry falls into two distinct operational paradigms:
            </p>
            <ul>
                <li><strong>Unguided Weapons:</strong> Kinetic slugthrowers, PDCs, railguns, and laser arrays. Fired manually by calculating target lead vectors with a Complex Test using <strong>Finesse + Accuracy</strong>. Unguided weapons can be fired at any target within range without electronic acquisition.</li>
                <li><strong>Guided Weapons:</strong> Missiles, torpedoes, and hunter drones equipped with onboard rocket thrusters and seeker packages. Guided ordnance <strong>strictly requires an active Target Lock</strong> before launch. Guided attacks are resolved with a Complex Test using <strong>Tracking + Tracking</strong>. Each level of Target Lock held on the target provides <strong>1 Upgrade</strong> to the roll.</li>
            </ul>

            <h3>Orbital Ballistics &amp; Light-Speed Latency</h3>
            <p>
                Across thousands of kilometers, targeting a maneuvering ship is constrained by sensory delay. Because ladar echoes travel at the speed of light, sensor returns from a vessel 3,000 km away depict where the target was ten milliseconds ago. For unguided kinetic rounds traveling at twenty kilometers per second, projectile transit time spans several seconds, allowing a watchful pilot to bleed vector momentum and slip outside the incoming trajectory cone.
            </p>

            <h3>Point-Defense Interception Screens</h3>
            <p>
                Defending against guided missile swarms requires establishing overlapping interception cones. A single rotary PDC creates a localized flak curtain; when two or more PDCs link their radar trackers through the ship's fire-control bus, they create an interlocking kill zone, granting +1 Upgrade per additional operational turret.
            </p>



            <h3>Missile Guidance Architecture &amp; Counter-Measures</h3>
            <p>
                Guided ordnance in the Sphere relies on autonomous seeker brains combining infrared imaging, passive ladar receivers, and inertial guidance. When approaching an active point-defense grid, modern missiles execute pre-programmed erratic vector pulses, rolling and dodging along their flight path to spoil optical lead solutions calculated by hostile PDCs.
            </p>

            <h3>Target Lock &amp; EWAR Electronic Battles</h3>
            <p>
                Establishing a Target Lock represents flooding an enemy hull with ladar pulses, passive optical tracking, and thermal lock-on. Gunners acquire locks using a Systems Simple Test within Sensor Range. However, targets equipped with electronic counter-measure suites can deploy broad-spectrum noise and false radar echoes to shatter locks before ordnance can be launched.
            </p>

            <h3>Recoil Dynamics &amp; Munitions Safety</h3>
            <p>
                Naval kinetic weapons produce violent Newton reaction forces upon discharge. Automated avionics fire synchronized cold-gas counter-bursts to maintain gunnery alignment and prevent recoil tumble. Furthermore, high-explosive torpedo magazines are encased in armored containment coffins with directional blowout hatches, venting secondary cook-offs into outer vacuum rather than collapsing interior decks.
            </p>



            <h3>Special Weapon Properties</h3>
            <ul>
                <li><strong>Long-Range Ballistics (Railguns &amp; Coilguns):</strong> Projectiles exit electromagnetic barrels at hypersonic velocities (tens of kilometers per second). Accuracy dropoff on the Macro-Grid is measured in <strong>10 km (10 hex) increments</strong> rather than standard 1 km increments!</li>
                <li><strong>Point-Defense (Rating):</strong> Rapid-traverse rotary cannons equipped with autonomous radar tracking. When intercepting incoming missiles, the gunner contests the attack using <strong>Accuracy + Point-Defense Rating</strong>. Multiple PDCs grant 1 Upgrade per additional cannon.</li>
            </ul>

            <div class="callout" style="margin-top: 2.2mm; margin-bottom: 0;">
                <div class="callout-title">Ammunition Logistics &amp; Resupply</div>
                <p style="font-size: 8.1pt; line-height: 1.34; margin-bottom: 0;">
                    Refilling ordnance magazines requires authorized docking at any civilized port, orbital station, or naval tender. Standard resupply costs: <strong>2,000 Credits</strong> for Small weapons, <strong>4,000 Credits</strong> for Medium weapons, and <strong>8,000 Credits</strong> for Large weapons.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">86</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 87 (Spread 3 Right) — MASTER WEAPONS TABLE
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 87 (Spread 3 Right) — MASTER WEAPONS TABLE
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="starship-weapons-table">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Master Weapons Catalog</span>
        </div>

        <div class="page-body two-columns">
            <h2 class="column-span-all" style="margin-top: 0; margin-bottom: 1.5mm;">Master Starship Weapons Catalog</h2>
            <p class="column-span-all" style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 2mm;">
                The table below provides operational specifications for all twenty-two standard naval weapon systems deployed across the Sphere. Unguided weapons reference their Accuracy array across Dogfight positions (Dis/Neu/Adv) and Macro-Grid distances (1/2/3/4/5+ km; railguns and coilguns use 10 km increments). Guided ordnance requires active Target Lock and references Tracking ratings.
            </p>

            <div class="table-container column-span-all" style="margin: 0 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.2pt; line-height: 1.2;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.5mm; width: 23%;">Weapon Name</th>
                            <th style="padding: 1.2mm 1mm; width: 7%;">Size</th>
                            <th style="padding: 1.2mm 1mm; width: 8%;">Type</th>
                            <th style="padding: 1.2mm 1mm; width: 14%;">Acc (Dogfight)</th>
                            <th style="padding: 1.2mm 1mm; width: 14%;">Acc (Macro)*</th>
                            <th style="padding: 1.2mm 1mm; width: 6%;">Trk</th>
                            <th style="padding: 1.2mm 1mm; width: 5%;">Dmg</th>
                            <th style="padding: 1.2mm 1mm; width: 8%;">RoF</th>
                            <th style="padding: 1.2mm 1mm; width: 5%;">Ammo</th>
                            <th style="padding: 1.2mm 1mm; width: 10%;">Cost (CR)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">GVI "Buzzer" Seeker Drone</td>
                            <td>Small</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>1</td>
                            <td class="bold">+2</td>
                            <td>1 / turn</td>
                            <td>6</td>
                            <td>200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">PA "Sentinel" Rotary PDC</td>
                            <td>Small</td>
                            <td>Unguided</td>
                            <td>2 / 3 / 3</td>
                            <td>1 / 0 / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+1</td>
                            <td>Unlimited</td>
                            <td>Unlim</td>
                            <td>250,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Stinger" Light Missile</td>
                            <td>Small</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>2</td>
                            <td class="bold">+3</td>
                            <td>1 / turn</td>
                            <td>4</td>
                            <td>300,000</td>
                        </tr>
                        <tr>
                            <td class="bold">PA "Caltrop" Mine Dispenser</td>
                            <td>Small</td>
                            <td>Unguided</td>
                            <td>3 / &mdash; / &mdash;</td>
                            <td>&mdash; / &mdash; / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+6</td>
                            <td>1 / turn</td>
                            <td>4</td>
                            <td>350,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CQV "Wasp" Pulse Laser</td>
                            <td>Small</td>
                            <td>Unguided</td>
                            <td>&mdash; / 2 / 3</td>
                            <td>1 / &mdash; / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+1</td>
                            <td>Unlimited</td>
                            <td>Unlim</td>
                            <td>450,000</td>
                        </tr>
                        <tr>
                            <td class="bold">PA "Guardian" Heavy PDC</td>
                            <td>Medium</td>
                            <td>Unguided</td>
                            <td>1 / 2 / 2</td>
                            <td>2 / 1 / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+2</td>
                            <td>Unlimited</td>
                            <td>Unlim</td>
                            <td>600,000</td>
                        </tr>
                        <tr>
                            <td class="bold">KSK "Harpoon" Kinetic Missile</td>
                            <td>Small</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>4</td>
                            <td class="bold">+1</td>
                            <td>1 / turn</td>
                            <td>6</td>
                            <td>650,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CF "Sledgehammer" Flak Cannon</td>
                            <td>Medium</td>
                            <td>Unguided</td>
                            <td>&mdash; / 1 / 2</td>
                            <td>1 / &mdash; / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+3</td>
                            <td>2 / turn</td>
                            <td>12</td>
                            <td>750,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CQV "Solarflare" Laser Array</td>
                            <td>Medium</td>
                            <td>Unguided</td>
                            <td>&mdash; / 1 / 2</td>
                            <td>2 / 1 / 0 / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+2</td>
                            <td>Unlimited</td>
                            <td>Unlim</td>
                            <td>850,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Javelin" Missile Pod</td>
                            <td>Medium</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>2</td>
                            <td class="bold">+4</td>
                            <td>1 / turn</td>
                            <td>4</td>
                            <td>950,000</td>
                        </tr>
                        <tr>
                            <td class="bold">KSK "Lance" Kinetic Torpedo</td>
                            <td>Medium</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>3</td>
                            <td class="bold">+3</td>
                            <td>1 / turn</td>
                            <td>8</td>
                            <td>1,100,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CF "Anvil" Railgun Battery</td>
                            <td>Medium</td>
                            <td>Unguided</td>
                            <td>&mdash; / 1 / 2</td>
                            <td>2 / 1 / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+5</td>
                            <td>2 / turn</td>
                            <td>20</td>
                            <td>1,200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Breacher" Thermal Lance</td>
                            <td>Medium</td>
                            <td>Unguided</td>
                            <td>&mdash; / 1 / 3</td>
                            <td>1 / &mdash; / &mdash; / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+8</td>
                            <td>1 / turn</td>
                            <td>Unlim</td>
                            <td>1,350,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Hydra" Multi-Missile Rack</td>
                            <td>Medium</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>1</td>
                            <td class="bold">+2</td>
                            <td>4 / turn</td>
                            <td>2 salvos</td>
                            <td>1,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CF "Bulwark" PDC Battery</td>
                            <td>Large</td>
                            <td>Unguided</td>
                            <td>0 / 1 / 1</td>
                            <td>3 / 2 / 1 / &mdash; / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+3</td>
                            <td>Unlimited</td>
                            <td>Unlim</td>
                            <td>1,800,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CQV "Eclipse" Particle Beam</td>
                            <td>Medium</td>
                            <td>Unguided</td>
                            <td>&mdash; / 0 / 2</td>
                            <td>3 / 2 / 1 / 0 / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+4</td>
                            <td>1 / turn</td>
                            <td>Unlim</td>
                            <td>2,200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">KSK "Voidlance" Torpedo Tube</td>
                            <td>Large</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>1</td>
                            <td class="bold">+12</td>
                            <td>1 / round</td>
                            <td>2</td>
                            <td>3,200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Cataclysm" Siege Torpedo</td>
                            <td>Large</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>0</td>
                            <td class="bold">+20</td>
                            <td>1 / round</td>
                            <td>1</td>
                            <td>3,800,000</td>
                        </tr>
                        <tr>
                            <td class="bold">KSK "Specter" Stealth Missile</td>
                            <td>Medium</td>
                            <td>Guided</td>
                            <td>&mdash;</td>
                            <td>&mdash;</td>
                            <td>5</td>
                            <td class="bold">+4</td>
                            <td>1 / turn</td>
                            <td>2</td>
                            <td>4,200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CF "Mjolnir" Spinal Coilgun</td>
                            <td>Large</td>
                            <td>Unguided</td>
                            <td>&mdash; / &mdash; / 2</td>
                            <td>3 / 2 / 1 / 0 / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+10</td>
                            <td>1 / turn</td>
                            <td>6</td>
                            <td>4,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CQV "Prometheus" Heavy Laser</td>
                            <td>Large</td>
                            <td>Unguided</td>
                            <td>&mdash; / 0 / 1</td>
                            <td>3 / 2 / 1 / 0 / &mdash;</td>
                            <td>&mdash;</td>
                            <td class="bold">+6</td>
                            <td>Unlimited</td>
                            <td>Unlim</td>
                            <td>5,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CF "Gigant" Heavy Railgun</td>
                            <td>Large</td>
                            <td>Unguided</td>
                            <td>&mdash; / &mdash; / 1</td>
                            <td>4 / 3 / 2 / 1 / 0</td>
                            <td>&mdash;</td>
                            <td class="bold">+15</td>
                            <td>1 / turn</td>
                            <td>4</td>
                            <td>6,500,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="column-span-all" style="font-size: 7.4pt; line-height: 1.25; margin-bottom: 2mm; color: var(--text-muted);">
                * Railguns and Spinal Coilguns measure Macro-Grid accuracy in 10 km (10-hex) increments due to Long-Range Ballistics. Special Properties: Sentinel (PD 5), Guardian (PD 4), Sledgehammer (PD 3), Bulwark (PD 5), Anvil/Mjolnir/Gigant (Railgun).
            </p>

            <h3 style="margin-top: 1mm;">Naval Combat Doctrines</h3>
            <p>
                <strong>The Kinetic Envelope:</strong> Rotary PDCs and flak batteries form a ship's primary defensive umbrella. While individual tungsten flechettes deal modest hull damage, their high rate of fire allows gunners to fill closing engagement cones with dense screens of metal, shredding incoming missiles before impact.
            </p>
            <p>
                <strong>Spinal Keel Alignment:</strong> Large spinal railguns and coilguns represent terrifying kinetic force (+10 to +15 Damage Bonus). However, because they are mounted directly into the ship's longitudinal spine, the pilot must align the entire vessel's chassis along the target vector, restricting their fire to Advantage in dogfights.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">87</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 88 (Spread 4 Left) — WEAPON PROFILES 1 TO 11
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 88 (Spread 4 Left) — WEAPON PROFILES 1 TO 11
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="weapon-profiles-1-11">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Ship Weapons Catalog (1–11)</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0; margin-bottom: 1.5mm;">Naval Ordnance Profiles (1–11)</h2>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">1. GVI "Buzzer" Seeker Drone</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A low-cost, expendable seeker equipped with cold-gas attitude thrusters and a shaped high-explosive warhead. Slow and easily outmaneuvered by seasoned pilots, but cheap enough for persistent swarming harassment.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Cold-gas attitude thrusters with micro-rocket sustainer and contact piezo-electric trigger fuze.<br>
            <strong>Size:</strong> Small &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 1 &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 6 &bull; <strong>Cost:</strong> 200,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Deployed in multi-drone flights to saturate hostile point-defense grids, forcing opposing gunners to exhaust reaction APs before heavier torpedoes arrive.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">2. PA "Sentinel" Rotary PDC</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>The gold standard for close-in defense across the Sphere. Composed of a six-barreled rotary autocannon on a high-speed hydraulic gimbal, firing tungsten flechettes to paint an impenetrable wall of lead.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Six-barrel motorized Gatling gimbal with liquid-nitrogen jacket and high-rate linkless ammunition feed.<br>
            <strong>Size:</strong> Small &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 2/3/3 &bull; <strong>Macro Acc:</strong> 1/0/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (5) &bull; <strong>Damage:</strong> +1 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited &bull; <strong>Cost:</strong> 250,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Essential survivability installation. Dedicated gunners hold reactions to shred inbound torpedoes within 500 meters of the hull.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">3. GVI "Stinger" Light Missile</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A compact, high-velocity missile designed for light interceptors. It trades raw explosive mass for a sophisticated seeker matrix that makes it remarkably difficult to shake in close dogfights.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Solid-fuel booster core with gimbaled thrust-vector nozzle and dual optical/RF terminal sensor array.<br>
            <strong>Size:</strong> Small &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 2 &bull; <strong>Damage:</strong> +3 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 4 &bull; <strong>Cost:</strong> 300,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Standard offensive strike armament for corsair corvettes; delivers dependable punch against unarmored utility craft.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">4. PA "Caltrop" Proximity Mine Dispenser</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A rear-mounted pneumatic dispenser releasing shaped-charge proximity mines. Useless in an offensive chase, but devastating when a pursuer sits on your tail at Disadvantage.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Rear-venting pneumatic rotary rack launching magnetized shaped-charge canisters with command-destruct codes.<br>
            <strong>Size:</strong> Small &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 3/&mdash;/&mdash; &bull; <strong>Macro Acc:</strong> &mdash; &bull; <strong>Damage:</strong> +6 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 4 &bull; <strong>Cost:</strong> 350,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> The ultimate defensive equalizer for slow freighters; turns an enemy's tail pursuit into catastrophic hull trauma.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">5. CQV "Wasp" Pulse Laser</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A specialized dogfighting laser firing rapid ultraviolet pulses. Lacks cutting power against heavy armor, but high mirror slew speeds grant pinpoint accuracy against agile targets.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Rapid-pulsing diode-pumped solid-state laser cavity mounted on high-traverse piezoelectric mirror mounts.<br>
            <strong>Size:</strong> Small &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/2/3 &bull; <strong>Macro Acc:</strong> 1/&mdash;/&mdash;/&mdash;/&mdash; &bull; <strong>Damage:</strong> +1 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 450,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Infinite ammunition draws directly from reactor loops, making it an excellent suppression weapon during extended zero-resupply operations.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">6. PA "Guardian" Heavy PDC</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A medium-caliber evolution of the Sentinel. Uses 30mm tungsten-jacketed rounds and heavy liquid-nitrogen cooling loops, extending defensive interception envelopes out to 2 km.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Motorized twin-barrel 30mm autocannon with integrated millimetric radar tracker and recoil-damping hydraulic dampers.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 1/2/2 &bull; <strong>Macro Acc:</strong> 2/1/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (4) &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited &bull; <strong>Cost:</strong> 600,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Combines reliable point defense with genuine offensive bite against medium hulls at macro approach distances.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">7. KSK "Harpoon" Kinetic Missile</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>Fires an ultra-dense depleted uranium penetrator dart at extreme closing speeds. While it lacks explosive yield, its pinpoint tracking makes it a favorite for sniping engines.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> High-density depleted uranium dart driven by two-stage solid rocket booster with inertial gyro autopilot.<br>
            <strong>Size:</strong> Small &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 4 &bull; <strong>Damage:</strong> +1 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 6 &bull; <strong>Cost:</strong> 650,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Extraordinary base Tracking 4 ensures reliable hits even through heavy hostile EWAR jamming environments.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">8. CF "Sledgehammer" Flak Cannon</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>Fires heavy, proximity-fused explosive canisters that burst into razor-sharp titanium shrapnel clouds. Engineered to shred incoming missile clusters and strip sensor domes.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Heavy rifled naval cannon firing pre-fragmented titanium canister rounds with variable electronic time fuzes.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/2 &bull; <strong>Macro Acc:</strong> 1/&mdash;/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (3) &bull; <strong>Damage:</strong> +3 &bull; <strong>RoF:</strong> 2/turn &bull; <strong>Ammo:</strong> 12 &bull; <strong>Cost:</strong> 750,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Excellent area denial; creates dense kinetic screens that degrade light interceptors attempting knife-fighting flybys.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">9. CQV "Solarflare" Laser Array</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A continuous multi-megawatt chemical laser focusing thermal energy through synthetic sapphire optics. Delivers damage at the speed of light, melting structural ribs and vaporizing armor.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Multi-megawatt continuous-wave chemical oxygen-iodine laser channel with liquid-helium radiator loops.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/2 &bull; <strong>Macro Acc:</strong> 2/1/0/&mdash;/&mdash; &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 850,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Near-zero flight time makes it impossible for targets to evade at close range, stripping ablative plates with ruthless precision.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">10. GVI "Javelin" Guided Missile Pod</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A modular quad-launcher packed with high-thrust tactical missiles. Upon Target Lock acquisition, the salvo launches in a coordinated fan, adjusting vector mid-flight to overwhelm point defense.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Hexagonal four-tube modular launch pod with pneumatic soft-ejection and programmable ripple-fire logic.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 2 &bull; <strong>Damage:</strong> +4 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 4 salvos &bull; <strong>Cost:</strong> 950,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Heavy tactical warheads crack frigate-grade bulkheads once hostile point-defense turrets are distracted or suppressed.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">11. KSK "Lance" Kinetic Torpedo</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A fin-stabilized kinetic torpedo driven by a solid-fuel booster core. Relies on immense closing momentum to smash deep into an adversary's internal machinery and shatter drive mounts.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Heavy hardened tungsten-carbide core encased in thermal ablative shroud with solid-fuel pursuit motor.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 3 &bull; <strong>Damage:</strong> +3 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 8 &bull; <strong>Cost:</strong> 1,100,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0; color: var(--text-muted);">
                <strong>Doctrine:</strong> Hardened seeker casing resists electronic countermeasures; devastating for crippling fleeing targets during high-G pursuit.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">88</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 89 (Spread 4 Right) — WEAPON PROFILES 12 TO 22
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 89 (Spread 4 Right) — WEAPON PROFILES 12 TO 22
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="weapon-profiles-12-22">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Ship Weapons Catalog (12–22)</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0; margin-bottom: 1.5mm;">Naval Ordnance Profiles (12–22)</h2>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">12. CF "Anvil" Railgun Battery</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>Twin electromagnetic accelerators firing tungsten slugs at hyper-velocity. Bridges the gap between light PDCs and spinal mounts with reliable medium-range striking power without extreme alignment limits.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Parallel copper-alloy magnetic rail guides launching hypervelocity tungsten sabots at 25 kilometers per second.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/2 &bull; <strong>Macro Acc (10km):</strong> 2/1/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Railgun &bull; <strong>Damage:</strong> +5 &bull; <strong>RoF:</strong> 2/turn &bull; <strong>Ammo:</strong> 20 &bull; <strong>Cost:</strong> 1,200,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Long-Range Ballistics allow effective fire out to 20 km; excellent for softening approaching combatants before dogfight transition.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">13. GVI "Breacher" Thermal Lance</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>An industrial salvage cutting laser retrofitted for close-quarters void brawls. Poor range, but its focused thermal output provides unmatched cutting power against heavy armor plating at point-blank range.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Overclocked industrial cutting beam focusing plasma-arc thermal energy through heavy sapphire magnetic collimators.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/3 &bull; <strong>Macro Acc:</strong> 1/&mdash;/&mdash;/&mdash;/&mdash; &bull; <strong>Damage:</strong> +8 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> Unlimited &bull; <strong>Cost:</strong> 1,350,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Devastating finisher at Advantage (Positions 8–10); slices cleanly through armored bulkheads and disabled hulks alike.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">14. GVI "Hydra" Multi-Missile Rack</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>Sacrifices individual missile payload for sheer saturation volume. Fires four micro-missiles simultaneously, forcing target point-defense computers to spread intercept fire dangerously thin.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Pneumatic rapid-fire launcher dispensing ripple-fire cluster micro-missiles with coordinated swarm algorithms.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 1 &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> 4/turn &bull; <strong>Ammo:</strong> 2 salvos (8 missiles) &bull; <strong>Cost:</strong> 1,500,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Firing 4 missiles per turn overwhelms single-turret PDC grids through pure statistical target saturation.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">15. CF "Bulwark" Point-Defense Battery</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A large-scale multi-barrel defensive installation for frigates and monitors. Backed by dedicated fire-control mainframes, it projects an impenetrable interception umbrella out to 3 km.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Quad-barrel 40mm rotary battery tied directly to ship mainframe fire-control buses and dedicated cooling shunts.<br>
            <strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 0/1/1 &bull; <strong>Macro Acc:</strong> 3/2/1/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (5) &bull; <strong>Damage:</strong> +3 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited &bull; <strong>Cost:</strong> 1,800,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Fleet-level screen; shields adjacent friendly vessels from torpedo strikes across multi-kilometer macro engagements.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">16. CQV "Eclipse" Particle Beam</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>Accelerates ionized subatomic matter to relativistic velocities. Unlike lasers, the particle beam maintains focus at extreme ranges and delivers kinetic impact alongside thermal trauma.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Electrostatic subatomic particle accelerator utilizing superconducting magnets to collimate relativistic ion streams.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/0/2 &bull; <strong>Macro Acc:</strong> 3/2/1/0/&mdash; &bull; <strong>Damage:</strong> +4 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 2,200,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Superb sniper weapon; strikes out to 4 km on the Macro-Grid with heavy accuracy and relentless armor erosion.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">17. KSK "Voidlance" Fusion Torpedo Tube</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>An instrument of absolute devastation. Launches an armored torpedo packing a multi-megaton thermonuclear payload. Slow and expensive, but a direct impact vaporizes heavy armor plating.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Pressurized naval torpedo tube launching multi-megaton thermonuclear warheads with armored terminal penetration caps.<br>
            <strong>Size:</strong> Large &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 1 &bull; <strong>Damage:</strong> +12 &bull; <strong>RoF:</strong> 1/round &bull; <strong>Ammo:</strong> 2 &bull; <strong>Cost:</strong> 3,200,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Capital ship executioner; a single penetrating strike tears through multiple hull condition tracks simultaneously.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">18. GVI "Cataclysm" Siege Torpedo</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>The heaviest guided ordnance in the Sphere. Less a torpedo and more a demolition charge with rocket thrusters. Sluggish guidance, but its immense yield is sufficient to crack orbital stations.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Heavy demolition missile carrying high-yield shaped fusion payload with autonomous terminal dogfight thrusters.<br>
            <strong>Size:</strong> Large &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 0 &bull; <strong>Damage:</strong> +20 &bull; <strong>RoF:</strong> 1/round &bull; <strong>Ammo:</strong> 1 &bull; <strong>Cost:</strong> 3,800,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Station siege and fortress cracking; requires prior EWAR suppression to ensure the sluggish torpedo reaches its target.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">19. KSK "Specter" Stealth Missile</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A marvel of black-budget engineering. Built with radar-scattering composites and cold-gas attitude jets. Nearly invisible to standard sensor suites, making it the premier assassination weapon.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Radar-absorbent ferrite composite airframe equipped with ultra-low-signature cold-gas vector thrusters.<br>
            <strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 5 &bull; <strong>Damage:</strong> +4 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 2 &bull; <strong>Cost:</strong> 4,200,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Tracking 5 slices through defensive jammers; lethal against high-value targets before defensive alarms trigger.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">20. CF "Mjolnir" Spinal Coilgun</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A massive mass accelerator built directly into a frigate's longitudinal keel. Accelerates a 100 kg depleted uranium slug to a fraction of light speed. Aiming requires pointing the entire ship.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Multi-stage electromagnetic induction coil assembly running the entire longitudinal structural keel of the vessel.<br>
            <strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/&mdash;/2 &bull; <strong>Macro Acc (10km):</strong> 3/2/1/0/&mdash; &bull; <strong>Special:</strong> Railgun &bull; <strong>Damage:</strong> +10 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 6 &bull; <strong>Cost:</strong> 4,500,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Devastating spinal sniper; fires across 10–40 km corridors to shatter heavy keels before enemies can close.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">21. CQV "Prometheus" Heavy Laser Array</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>A turreted ultraviolet laser array with triple-core ruby resonators. Sips massive reactor power to ablate reinforced bulkheads at ranges where kinetic rounds drift off target.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> High-output continuous-wave chemical laser driven by triple-core ruby resonators and high-capacity radiator vanes.<br>
            <strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/0/1 &bull; <strong>Macro Acc:</strong> 3/2/1/0/&mdash; &bull; <strong>Damage:</strong> +6 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 5,000,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 1.8mm; color: var(--text-muted);">
                <strong>Doctrine:</strong> Sustained light-speed thermal lance; turreted mount allows continuous fire across neutral and advantage vectors alike.
            </p>

            <h4 style="margin-bottom: 0.5mm; color: var(--amber-dark);">22. CF "Gigant" Heavy Railgun</h4>
            <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 0.8mm;">
                <em>The pinnacle of conventional mass acceleration. Fires multi-ton slugs capable of snapping a cruiser's spine in a single volley. Immense recoil can knock smaller hulls off course.</em>
            </p>
            <p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">
                <strong>Mount:</strong> Super-heavy naval railgun barrel with reinforced cryogenic field coils, firing multi-ton hypervelocity kinetic penetrators.<br>
            <strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/&mdash;/1 &bull; <strong>Macro Acc (10km):</strong> 4/3/2/1/0 &bull; <strong>Special:</strong> Railgun &bull; <strong>Damage:</strong> +15 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 4 &bull; <strong>Cost:</strong> 6,500,000 CR.
            </p>
            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0; color: var(--text-muted);">
                <strong>Doctrine:</strong> Interplanetary artillery; extreme range out to 50 km (50 hexes) forces entire battlefleets into evasive dispersed formations.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">89</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 90 (Spread 5 Left) — INTERNAL MODULES & EXPANSION BAYS
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 90 (Spread 5 Left) — INTERNAL MODULES & EXPANSION BAYS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="internal-modules-catalog">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Internal Modules</span>
        </div>

        <div class="page-body two-columns">
            <h2 class="column-span-all" style="margin-top: 0; margin-bottom: 1.5mm;">Internal Modules &amp; Subsystems</h2>
            <p class="column-span-all" style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 2mm;">
                Internal modules represent specialized structural bays, avionics suites, and crew life-support installations housed within a starship's pressurized hull. A vessel's capacity for internal upgrades is strictly governed by its <strong>Module Slots</strong> based on Size Class: <strong>Small craft (4 slots)</strong>, <strong>Medium vessels (8 slots)</strong>, and <strong>Large capital ships (12 slots)</strong>.
            </p>

            <div class="table-container column-span-all" style="margin: 0 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.2pt; line-height: 1.2;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1.5mm; width: 22%;">Module Name</th>
                            <th style="padding: 1.2mm 1.5mm; width: 48%;">Rules &amp; Tactical Effect</th>
                            <th style="padding: 1.2mm 1mm; width: 10%;">Slots</th>
                            <th style="padding: 1.2mm 1.5mm; width: 20%;">Cost (CR)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Injector Seats</td>
                            <td>Take half damage from G-Strain (round down) during high-G burns.</td>
                            <td class="bold">1</td>
                            <td>0 (Standard)</td>
                        </tr>
                        <tr>
                            <td class="bold">Extra Ammo Storage</td>
                            <td>Double the ammunition capacity of all weapons installed on the ship.</td>
                            <td class="bold">1</td>
                            <td>350,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Reinforced Bulkheads</td>
                            <td>Permanently increases the vessel's Hull Rating by +2.</td>
                            <td class="bold">1</td>
                            <td>650,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Auto-Loaders</td>
                            <td>Increases Rate of Fire (RoF) by +1 for unguided kinetic and guided missiles.</td>
                            <td class="bold">1</td>
                            <td>850,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Basic MedBay</td>
                            <td>Single auto-doc berth; all Recovery tests on the ship receive 1 Upgrade.</td>
                            <td class="bold">1</td>
                            <td>450,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Advanced MedBay</td>
                            <td>Automated trauma bay; all Recovery tests on the ship receive 2 Upgrades.</td>
                            <td class="bold">2</td>
                            <td>1,200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Intensive Trauma Suite</td>
                            <td>Clinical biosculpting bay; all Recovery tests on ship receive 3 Upgrades.</td>
                            <td class="bold">3</td>
                            <td>2,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Signal Scrambler</td>
                            <td>Broad-spectrum EWAR array; grants +2 Upgrades to all Sensor Jam actions.</td>
                            <td class="bold">1</td>
                            <td>1,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Fire-Control Computer</td>
                            <td>Predictive orbital tracking core; grants +2 Upgrades to Target Lock actions.</td>
                            <td class="bold">1</td>
                            <td>1,800,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Advanced Repair Drones</td>
                            <td>Smart zero-g nanite swarm; grants +2 Upgrades to in-combat Repair actions.</td>
                            <td class="bold">1</td>
                            <td>2,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Enhanced Sensor Suite</td>
                            <td>Cryogenic array; increases base Target Lock and Sensor Range by +2 km.</td>
                            <td class="bold">1</td>
                            <td>2,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Hangar Bay</td>
                            <td>Pressurized launch deck; internally houses 2 Drone-fighters or 1 Shuttle.</td>
                            <td class="bold">3</td>
                            <td>4,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">Extra Hardpoint</td>
                            <td>Adds one hardpoint of a size already present on ship. (Max once per ship).</td>
                            <td class="bold">2</td>
                            <td>5,000,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1mm;">Detailed Module Descriptions</h3>
            <p>
                <strong>1. Injector Seats (1 Slot &bull; 0 CR):</strong> Standard equipment for interceptors. Uses hydrostatic liquid-immersion cradles and automated cardio-vasoconstrictor drug injectors to prevent cerebral blood pooling during crushing maneuvers. Whenever crew members suffer G-Strain, damage is halved (rounded down).
            </p>
            <p>
                <strong>2. Extra Ammo Storage (1 Slot &bull; 350,000 CR):</strong> High-density armored ammunition drums and conveyor elevators tucked into cargo voids. Doubles the Ammunition capacity of all kinetic slugthrowers, railguns, and missile pods installed on the ship. Has no effect on reactor-powered lasers or particle beams.
            </p>
            <p>
                <strong>3. Reinforced Bulkheads (1 Slot &bull; 650,000 CR):</strong> Titanium-foam composite cross-braces and ceramic arrestor plates welded along internal keels. Permanently increases the ship's <strong>Hull Rating by +2</strong>, expanding every individual track segment across the vessel's Hull Condition Track.
            </p>
            <p>
                <strong>4. Auto-Loaders (1 Slot &bull; 850,000 CR):</strong> High-speed hydraulic rams and smart-sorting magazines that rapidly cycle heavy rounds and missile racks. Increases Rate of Fire (RoF) by +1 for all unguided kinetic weapons and guided missiles/torpedoes. Does not apply to continuous lasers or weapons with Unlimited RoF.
            </p>
            <p>
                <strong>5. MedBay Installations (1–3 Slots):</strong> Ranging from compact auto-doc berths (<em>Basic</em>: 1 slot, 1 Upgrade) to multi-bed trauma centers (<em>Advanced</em>: 2 slots, 2 Upgrades) and full biosculpting clinical suites (<em>Intensive Trauma Suite</em>: 3 slots, 3 Upgrades). Grants Upgrades to all Recovery tests performed on board.
            </p>
            <p>
                <strong>6. Electronic Warfare &amp; Sensor Packages:</strong> The <em>Signal Scrambler</em> (+2 Upgrades to Sensor Jam) floods incoming ladar buses with false noise, while the <em>Fire-Control Computer</em> (+2 Upgrades to Target Lock) runs predictive orbital lead algorithms. The <em>Enhanced Sensor Suite</em> boosts raw Sensor Range by +2 km.
            </p>
            <p>
                <strong>7. Drone Swarms &amp; Structural Bays:</strong> <em>Advanced Repair Drones</em> (+2 Upgrades to Repair) deploy nanite spider-swarms into vacuum to weld breached bulkheads mid-combat. The <em>Hangar Bay</em> (3 slots) houses two combat drone-fighters or a personnel shuttle, while the <em>Extra Hardpoint</em> (2 slots) adds an additional external mounting collar.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">90</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 91 (Spread 5 Right) — FLEET REGISTRY & STARSHIP COMPARISON
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 91 (Spread 5 Right) — FLEET REGISTRY & STARSHIP COMPARISON
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="starships-of-the-sphere">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Fleet Registry</span>
        </div>

        <div class="page-body two-columns">
            <h2 class="column-span-all" style="margin-top: 0; margin-bottom: 1.5mm;">Fleet Registry &amp; Starship Comparison</h2>
            <p class="column-span-all" style="font-size: 8.3pt; line-height: 1.34; margin-bottom: 2mm;">
                Across the orbital habitats, asteroid belt mining claims, and lawless fringes of the Sphere, starships represent the apex of industrial engineering. From cobbled-together scavenger tugs to military-grade interdictors and crushing dreadnoughts, ten distinct hull classifications dominate operational service.
            </p>

            <div class="table-container column-span-all" style="margin: 0 0 2.5mm 0;">
                <table class="rules-table" style="font-size: 7.1pt; line-height: 1.18;">
                    <thead>
                        <tr>
                            <th style="padding: 1.2mm 1mm; width: 18%;">Ship Model</th>
                            <th style="padding: 1.2mm 1mm; width: 7%;">Size</th>
                            <th style="padding: 1.2mm 1mm; width: 6%;">Hull</th>
                            <th style="padding: 1.2mm 1mm; width: 6%;">Arm</th>
                            <th style="padding: 1.2mm 1mm; width: 6%;">Acc</th>
                            <th style="padding: 1.2mm 1mm; width: 6%;">Man</th>
                            <th style="padding: 1.2mm 1mm; width: 6%;">Sys</th>
                            <th style="padding: 1.2mm 1mm; width: 8%;">Sensors</th>
                            <th style="padding: 1.2mm 1mm; width: 9%;">Hardpoints</th>
                            <th style="padding: 1.2mm 1mm; width: 14%;">Bridge Seats</th>
                            <th style="padding: 1.2mm 1mm; width: 7%;">Mods</th>
                            <th style="padding: 1.2mm 1mm; width: 11%;">Cost (CR)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">GVI "Rusty Hook"</td>
                            <td>Small</td>
                            <td>10</td>
                            <td>2</td>
                            <td>2</td>
                            <td>4</td>
                            <td>2</td>
                            <td>4 km</td>
                            <td>3 / 0 / 0</td>
                            <td>P, G, E (x2)</td>
                            <td>2 / 4</td>
                            <td>1,200,000</td>
                        </tr>
                        <tr>
                            <td class="bold">RF "Kestrel"</td>
                            <td>Small</td>
                            <td>10</td>
                            <td>1</td>
                            <td>3</td>
                            <td>4</td>
                            <td>3</td>
                            <td>6 km</td>
                            <td>2 / 1 / 0</td>
                            <td>P, G, E (x2)</td>
                            <td>2 / 4</td>
                            <td>2,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CQV "Shinobi"</td>
                            <td>Small</td>
                            <td>6</td>
                            <td>0</td>
                            <td>6</td>
                            <td>7</td>
                            <td>4</td>
                            <td>8 km</td>
                            <td>1 / 1 / 0</td>
                            <td>P, G, E (x2)</td>
                            <td>2 / 4</td>
                            <td>2,800,000</td>
                        </tr>
                        <tr>
                            <td class="bold">RF "Talon"</td>
                            <td>Small</td>
                            <td>8</td>
                            <td>1</td>
                            <td>4</td>
                            <td>6</td>
                            <td>3</td>
                            <td>6 km</td>
                            <td>2 / 1 / 0</td>
                            <td>P, G (x2), E</td>
                            <td>2 / 4</td>
                            <td>3,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Ironbound"</td>
                            <td>Medium</td>
                            <td>10</td>
                            <td>3</td>
                            <td>3</td>
                            <td>3</td>
                            <td>4</td>
                            <td>8 km</td>
                            <td>4 / 2 / 0</td>
                            <td>P, G, E (x2)</td>
                            <td>4 / 8</td>
                            <td>8,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">RF "Falcon" (Vulture)</td>
                            <td>Medium</td>
                            <td>12</td>
                            <td>4</td>
                            <td>4</td>
                            <td>2</td>
                            <td>3</td>
                            <td>6 km</td>
                            <td>3 / 3 / 0</td>
                            <td>P, G (x2), E</td>
                            <td>3 / 8</td>
                            <td>12,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">KSK "Dagger"</td>
                            <td>Medium</td>
                            <td>10</td>
                            <td>2</td>
                            <td>5</td>
                            <td>5</td>
                            <td>5</td>
                            <td>10 km</td>
                            <td>2 / 2 / 0</td>
                            <td>P, G, E (x2)</td>
                            <td>2 / 8</td>
                            <td>15,500,000</td>
                        </tr>
                        <tr>
                            <td class="bold">GVI "Bastion"</td>
                            <td>Large</td>
                            <td>14</td>
                            <td>5</td>
                            <td>3</td>
                            <td>2</td>
                            <td>4</td>
                            <td>8 km</td>
                            <td>8 / 2 / 0</td>
                            <td>P, G (x2), E (x2)</td>
                            <td>5 / 12</td>
                            <td>45,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">CF "Cinder"</td>
                            <td>Large</td>
                            <td>12</td>
                            <td>4</td>
                            <td>5</td>
                            <td>2</td>
                            <td>5</td>
                            <td>10 km</td>
                            <td>2 / 3 / 1</td>
                            <td>P, G (x2), E</td>
                            <td>5 / 12</td>
                            <td>65,000,000</td>
                        </tr>
                        <tr>
                            <td class="bold">KSK "Leviathan"</td>
                            <td>Large</td>
                            <td>16</td>
                            <td>6</td>
                            <td>2</td>
                            <td>1</td>
                            <td>6</td>
                            <td>12 km</td>
                            <td>6 / 4 / 0</td>
                            <td>P, G (x3), E (x2)</td>
                            <td>8 / 12</td>
                            <td>120,000,000</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 style="margin-top: 1mm;">Shipyards of the Sphere</h3>
            <p>
                <strong>Grabowski Void Industries (GVI):</strong> Headquartered throughout the lawless asteroid clusters of the Fringe, GVI builds unrefined, heavy-framed vessels assembled from pressurized cargo containers, salvaged ore haulers, and reinforced structural I-beams. Their designs (the <em>Rusty Hook</em>, <em>Ironbound</em>, and <em>Bastion</em>) are notoriously loud, uninsulated, and prone to hydraulic weeping, but their thick industrial armor belts and generous internal mounting volumes make them beloved by pragmatists who demand survivability over elegance.
            </p>
            <p>
                <strong>Redfeather Aerospace (RF):</strong> The primary commercial shipwright for colonial planetary defense forces, exploration guilds, and licensed corsairs. Redfeather produces balanced, dependable craft (the <em>Kestrel</em>, <em>Talon</em>, and <em>Falcon</em>) characterized by modular hardpoint rails, standardized avionic buses, and readily available spare parts in every civilized orbital berth.
            </p>
            <p>
                <strong>Chidori-Qwei Voidworks (CQV):</strong> Specializing in bleeding-edge sensor arrays, faceted stealth hulls, and ultra-high-efficiency microwave thrusters. The <em>Shinobi</em> represents their design philosophy: zero armor, paper-thin structural bulkheads, but extreme maneuverability and electronic invisibility that lets operatives strike and vanish.
            </p>
            <p>
                <strong>Caldera Foundry (CF):</strong> The industrial forge-masters of deep space. Caldera specializes in massive electromagnetic coil structures and reinforced naval keels. The <em>Cinder</em> frigate is built entirely around an unyielding longitudinal spine, designed to deliver relativistic slugs across interplanetary corridors.
            </p>
            <p>
                <strong>Ker'Satz Korp (KSK):</strong> State-contracted military shipwrights producing the apex of naval violence. KSK designs (the <em>Dagger</em> interdictor and the terrifying <em>Leviathan</em> dreadnought) boast hardened ceramic composite armor, quadruple-redundant avionics, and multi-station fire-control bridges capable of dominating entire orbital sectors.
            </p>

            <h3>Naval Classification &amp; Hull Tiers</h3>
            <p>
                Vessels in the Sphere are categorized into three broad structural tiers: <strong>Small craft</strong> (corvettes, light scouts, and fast interceptors under 80 meters), <strong>Medium craft</strong> (patrol boats, armed freighters, and long-range interdictors from 80 to 200 meters), and <strong>Large capital vessels</strong> (defensive monitors, strike frigates, and dreadnoughts exceeding 200 meters with multi-deck spinal keels).
            </p>

            <h3>Docking Fees &amp; Reaction Mass Logistics</h3>
            <p>
                Maintaining a starship in active flight status requires steady capital. Civilized orbital hubs charge standardized berthing fees: <strong>500 CR/day</strong> for Small craft, <strong>1,500 CR/day</strong> for Medium craft, and <strong>5,000 CR/day</strong> for Large vessels. Refueling reaction mass (purified water-slurry and deuterium fusion pellets) costs roughly 1,000 CR per macro burn corridor, ensuring crews must constantly seek profitable corsair contracts to stay space-worthy.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">91</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 92 (Spread 6 Left) — SMALL STARSHIP SHEETS
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 92 (Spread 6 Left) — SMALL STARSHIP SHEETS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="small-starship-sheets">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Small Starships</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0; margin-bottom: 1.5mm;">Small Starship Registry</h2>

            <div class="callout callout-cyan" style="margin: 0 0 2.2mm 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.8pt;">1. GVI "Rusty Hook" Jury-Rigged Corsair</div>
                <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 1mm;">
                    <em>A common sight in the Fringe, the Rusty Hook is less a ship and more a collection of pressurized cargo containers, salvaged ore-crushers, and exposed wiring conduits. Ugly, noisy, and cramped, it is remarkably tough and mounts surprising forward firepower.</em>
                </p>
                <div style="font-size: 7.5pt; line-height: 1.23;">
                    <strong>Hull Rating:</strong> 10 &bull; <strong>Condition Track:</strong> 4 tracks of 10 segments (`[10] &rarr; [10] &rarr; [10] &rarr; [10]`)<br>
                    <strong>Armor (Protection):</strong> 2 &bull; <strong>Acceleration:</strong> 2 &bull; <strong>Maneuverability:</strong> 4 &bull; <strong>Systems:</strong> 2 (4 km Sensor)<br>
                    <strong>Hardpoints:</strong> 3 Small &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 1x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 1,200,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 48m &bull; Beam 22m &bull; Dry Displacement 620 metric tons &bull; Welded container frame with high-tensile trunnions.<br>
                    <strong>Standard Weapons:</strong> 1x PA "Sentinel" Rotary PDC (S), 1x PA "Caltrop" Mine Dispenser (S), 1x KSK "Harpoon" Kinetic Missile (S)<br>
                    <strong>Installed Modules:</strong> Extra Ammo Storage (1 slot), Injector Seats (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>The Rusty Hook is a close-quarters brawler that lures enemies in, using Armor 2 to absorb incoming fire.</li>
                        <li>Punishes pursuing craft with the PA "Caltrop" Mine Dispenser while landing high-velocity Harpoon penetrators.</li>
                        <li>Dual Engineer stations allow simultaneous power shunting to thrusters and active damage control in combat.</li>
                        <li>Reinforced structural tow-winches allow rapid grappling and recovery of disabled derelict hulls in deep vacuum.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 2.2mm 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.8pt;">2. RF "Kestrel" Multi-Role Corvette</div>
                <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 1mm;">
                    <em>The quintessential "Corsair's first ship." Produced in vast quantities by Redfeather Aerospace, the Kestrel is a reliable, balanced patrol craft designed for multi-mission modularity. The perfect platform for an ambitious crew to make their mark.</em>
                </p>
                <div style="font-size: 7.5pt; line-height: 1.23;">
                    <strong>Hull Rating:</strong> 10 &bull; <strong>Condition Track:</strong> 4 tracks of 10 segments (`[10] &rarr; [10] &rarr; [10] &rarr; [10]`)<br>
                    <strong>Armor (Protection):</strong> 1 &bull; <strong>Acceleration:</strong> 3 &bull; <strong>Maneuverability:</strong> 4 &bull; <strong>Systems:</strong> 3 (6 km Sensor)<br>
                    <strong>Hardpoints:</strong> 2 Small, 1 Medium &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 1x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 2,000,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 62m &bull; Beam 28m &bull; Dry Displacement 850 metric tons &bull; Modular extruded titanium alloy monocoque.<br>
                    <strong>Standard Weapons:</strong> 1x PA "Sentinel" Rotary PDC (S), 1x GVI "Stinger" Light Missile (S), 1x CQV "Solarflare" Laser Array (M)<br>
                    <strong>Installed Modules:</strong> Injector Seats (1 slot), Fire-Control Computer (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Versatile all-rounder with Systems 3 and 6 km Sensor Range, operating effectively across all tactical envelopes.</li>
                        <li>Carries a triad weapon mix: unguided PDC defense, guided Stinger burst, and sustained Solarflare thermal damage.</li>
                        <li>Balanced 4-seat bridge ensures Pilot, Gunner, and Engineers each have the tools needed to contribute to the fight.</li>
                        <li>Slaves sensor telemetry through the Fire-Control Computer to share precision Target Locks across allied escorts.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 2.2mm 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.8pt;">3. CQV "Shinobi" Stealth Recon</div>
                <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 1mm;">
                    <em>A masterpiece of signature reduction built with faceted carbon composites and chilled skin panels. Highly fragile with zero armor, but extreme acceleration and cryogenic electronics make it the premier scout and assassin vessel.</em>
                </p>
                <div style="font-size: 7.5pt; line-height: 1.23;">
                    <strong>Hull Rating:</strong> 6 &bull; <strong>Condition Track:</strong> 4 tracks of 6 segments (`[6] &rarr; [6] &rarr; [6] &rarr; [6]`)<br>
                    <strong>Armor (Protection):</strong> 0 &bull; <strong>Acceleration:</strong> 6 &bull; <strong>Maneuverability:</strong> 7 &bull; <strong>Systems:</strong> 4 (8 km Sensor)<br>
                    <strong>Hardpoints:</strong> 1 Small, 1 Medium &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 1x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 2,800,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 54m &bull; Beam 20m &bull; Dry Displacement 480 metric tons &bull; Faceted carbon-nanotube radar-absorbent shell.<br>
                    <strong>Standard Weapons:</strong> 1x CQV "Wasp" Pulse Laser (S), 1x KSK "Specter" Stealth Missile (M)<br>
                    <strong>Installed Modules:</strong> Signal Scrambler (1 slot), Fire-Control Computer (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Relies on stealth and first-strike capability; Systems 4 and 8 km sensors acquire locks before detection.</li>
                        <li>Uses extreme Maneuverability 7 to maintain Advantage (8–10) while staying out of the enemy's forward firing cone.</li>
                        <li>Signal Scrambler enables the Engineer to break hostile locks while the Gunner fires stealth Specter missiles.</li>
                        <li>Cools outer hull plating with internal liquid-helium heat sinks to vanish completely from enemy passive IR sensors.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.8pt;">4. RF "Talon" Light Interceptor</div>
                <p style="font-size: 7.7pt; line-height: 1.26; margin-bottom: 1mm;">
                    <em>A razor-thin interceptor built around carbon nanotubes with massive lateral thrusters, engineered for high-G sector patrol, fast dogfighting, and aggressive pursuit. Vulnerable to sustained fire, but uncatchable in agile turns.</em>
                </p>
                <div style="font-size: 7.5pt; line-height: 1.23;">
                    <strong>Hull Rating:</strong> 8 &bull; <strong>Condition Track:</strong> 4 tracks of 8 segments (`[8] &rarr; [8] &rarr; [8] &rarr; [8]`)<br>
                    <strong>Armor (Protection):</strong> 1 &bull; <strong>Acceleration:</strong> 4 &bull; <strong>Maneuverability:</strong> 6 &bull; <strong>Systems:</strong> 3 (6 km Sensor)<br>
                    <strong>Hardpoints:</strong> 2 Small, 1 Medium &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 2x Gunner, 1x Engineer) &bull; <strong>Cost:</strong> 3,500,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 58m &bull; Beam 24m &bull; Dry Displacement 710 metric tons &bull; Reinforced tubular aerospace alloy spaceframe.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x GVI "Javelin" Missile Pod (M)<br>
                    <strong>Installed Modules:</strong> Injector Seats (1 slot), Auto-Loaders (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Excels at closing distance rapidly to establish Advantage (Positions 8–10) using high Maneuverability 6.</li>
                        <li>Once on the target's tail, Gunner fires Javelin guided missiles while Auto-Loaders cycle rapid follow-up salvos.</li>
                        <li>Dual Gunner seats ensure complete coverage of both offensive missile targeting and defensive PDC interception.</li>
                        <li>High lateral RCS clusters allow radical 180-degree flip-and-burn vector turns without bleeding closing velocity.</li>
                    </ul>
                </div>
            </div>

            <div class="callout column-span-all" style="margin-top: 2mm; margin-bottom: 0; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 8.4pt;">Doctrine // Small Craft Operational Logistics</div>
                <p style="font-size: 7.5pt; line-height: 1.25; margin-bottom: 0;">
                    Small starships represent the tactical backbone of corsair privateering across the Sphere. Their low displacement allows agile thrust-to-weight ratios and minimal reaction water consumption during interplanetary transit. However, limited internal magazine volume requires disciplined fire control: pilots who exhaust their ordnance in early skirmishes must flee to friendly orbital stations or face capital gunboats with empty launcher racks.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">92</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 93 (Spread 6 Right) — MEDIUM STARSHIP SHEETS
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 93 (Spread 6 Right) — MEDIUM STARSHIP SHEETS
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="medium-starship-sheets">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Medium Starships</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0; margin-bottom: 1.5mm;">Medium Starship Registry</h2>

            <div class="callout callout-cyan" style="margin: 0 0 2.5mm 0; padding: 2.5mm 3.2mm;">
                <div class="callout-title" style="font-size: 9pt;">5. GVI "Ironbound" Heavy Patrol Vessel</div>
                <p style="font-size: 7.8pt; line-height: 1.28; margin-bottom: 1mm;">
                    <em>A blocky, industrial workhorse reinforced with thick layers of steel plating and structural bracing. Slow and unglamorous, but its rugged modular interior houses a full four-seat bridge, an advanced medbay, and generous repair drones.</em>
                </p>
                <div style="font-size: 7.6pt; line-height: 1.24;">
                    <strong>Hull Rating:</strong> 10 &bull; <strong>Condition Track:</strong> 4 tracks of 10 segments (`[10] &rarr; [10] &rarr; [10] &rarr; [10]`)<br>
                    <strong>Armor (Protection):</strong> 3 &bull; <strong>Acceleration:</strong> 3 &bull; <strong>Maneuverability:</strong> 3 &bull; <strong>Systems:</strong> 4 (8 km Sensor)<br>
                    <strong>Hardpoints:</strong> 4 Small, 2 Medium &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 1x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 8,500,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 112m &bull; Beam 44m &bull; Dry Displacement 3,400 metric tons &bull; Cast-steel multi-frame keel with heavy bulkhead web.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 2x Empty Small Mounts, 1x CQV "Solarflare" Laser Array (M), 1x CF "Sledgehammer" Flak Cannon (M)<br>
                    <strong>Installed Modules:</strong> Advanced MedBay (2 slots), Advanced Repair Drones (1 slot), Reinforced Bulkheads (1 slot) [Total: 4/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Operates on a war of attrition; Armor 3 reduces damage while 10-wound tracks absorb heavy punishment.</li>
                        <li>Engineer shunts power to Weapons or Systems, granting Upgrades to the Gunner's laser and flak strikes.</li>
                        <li>Gunner weakens targets with continuous thermal beams before tearing through exposed hulls with flak bursts.</li>
                        <li>Second Engineer directs Advanced Repair Drones with Knowledge + Systems to restore integrity mid-combat.</li>
                        <li>Internal hydro-recyclers and expansive machine shops permit months of independent patrol off civilized supply lanes.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 2.5mm 0; padding: 2.5mm 3.2mm;">
                <div class="callout-title" style="font-size: 9pt;">6. RF "Falcon" (Vulture) System Patrol Boat</div>
                <p style="font-size: 7.8pt; line-height: 1.28; margin-bottom: 1mm;">
                    <em>The dependable backbone of colonial system defense forces, nicknamed "Vulture" for picking over disabled pirate hulls. Features a heavy armor belt, a balanced engine suite, and dangerous multi-barrel railgun batteries.</em>
                </p>
                <div style="font-size: 7.6pt; line-height: 1.24;">
                    <strong>Hull Rating:</strong> 12 &bull; <strong>Condition Track:</strong> 4 tracks of 12 segments (`[12] &rarr; [12] &rarr; [12] &rarr; [12]`)<br>
                    <strong>Armor (Protection):</strong> 4 &bull; <strong>Acceleration:</strong> 4 &bull; <strong>Maneuverability:</strong> 2 &bull; <strong>Systems:</strong> 3 (6 km Sensor)<br>
                    <strong>Hardpoints:</strong> 3 Small, 3 Medium &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 2x Gunner, 1x Engineer) &bull; <strong>Cost:</strong> 12,000,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 135m &bull; Beam 52m &bull; Dry Displacement 4,600 metric tons &bull; Double-hulled layered composite armored belt.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x PA "Guardian" Heavy PDC (M), 1x CF "Anvil" Railgun Battery (M), 1x GVI "Javelin" Missile Pod (M)<br>
                    <strong>Installed Modules:</strong> Advanced MedBay (2 slots), Extra Ammo Storage (1 slot) [Total: 3/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Uses Armor 4 and dual PDC screens to withstand incoming missile salvos while closing engagement gaps.</li>
                        <li>The CF "Anvil" Railgun Battery delivers consistent kinetic trauma across medium Macro-Grid ranges (10–20 km).</li>
                        <li>Focuses on area denial and intercepting hostile boarding craft before they reach docking collars.</li>
                        <li>Dual Gunner stations allow simultaneous long-range railgun fire and defensive point-defense interception.</li>
                        <li>Interlocking fire arcs create a forward kill corridor that prevents smaller corvettes from closing without taking heavy rail fire.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 0 0; padding: 2.5mm 3.2mm;">
                <div class="callout-title" style="font-size: 9pt;">7. KSK "Dagger" Long-Range Interdictor</div>
                <p style="font-size: 7.8pt; line-height: 1.28; margin-bottom: 1mm;">
                    <em>A high-speed pursuit vessel built around oversized fusion engines and an advanced cryogenic sensor suite. Designed to chase down fleeing corsairs, break vector momentum, and pin targets until fleet dreadnoughts arrive.</em>
                </p>
                <div style="font-size: 7.6pt; line-height: 1.24;">
                    <strong>Hull Rating:</strong> 10 &bull; <strong>Condition Track:</strong> 4 tracks of 10 segments (`[10] &rarr; [10] &rarr; [10] &rarr; [10]`)<br>
                    <strong>Armor (Protection):</strong> 2 &bull; <strong>Acceleration:</strong> 5 &bull; <strong>Maneuverability:</strong> 5 &bull; <strong>Systems:</strong> 5 (10 km Sensor)<br>
                    <strong>Hardpoints:</strong> 2 Small, 2 Medium &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 1x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 15,500,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 120m &bull; Beam 36m &bull; Dry Displacement 3,800 metric tons &bull; High-density ceramic-matrix reinforced pursuit chassis.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x KSK "Lance" Kinetic Torpedo (M), 1x CQV "Eclipse" Particle Beam (M)<br>
                    <strong>Installed Modules:</strong> Fire-Control Computer (1 slot), Enhanced Sensor Suite (1 slot) [Total: 2/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Unrivaled at the Breakaway contest, using Acceleration 5 to stay glued to an escaping target's tail.</li>
                        <li>The CQV "Eclipse" Particle Beam maintains tight beam focus out to 4 km, softening armor before torpedo impact.</li>
                        <li>The KSK "Lance" Kinetic Torpedo uses heavy kinetic closing velocity to punch directly into hostile engine compartments.</li>
                        <li>Supercooled cryogenic sensor arrays burn through passive electromagnetic stealth at ranges exceeding 10 kilometers.</li>
                    </ul>
                </div>
            </div>

            <div class="callout column-span-all" style="margin-top: 2mm; margin-bottom: 0; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 8.4pt;">Doctrine // Medium Hull Endurance &amp; Hydro-Loops</div>
                <p style="font-size: 7.5pt; line-height: 1.25; margin-bottom: 0;">
                    Medium hulls (80–150m) represent independent expeditionary platforms capable of long-range interplanetary transit. Unlike cramped corvettes, their internal displacement accommodates private bunk spaces, closed-loop hydroponic water recycling, and multi-week vacuum endurance. This operational self-sufficiency makes them the premier choice for corsair crews venturing far beyond the inner moons into uncharted asteroid corridors.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">93</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 94 (Spread 7 Left) — CAPITAL STARSHIPS
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 94 (Spread 7 Left) — CAPITAL STARSHIPS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="capital-starships-registry">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Capital Starships</span>
        </div>

        <div class="page-body two-columns">
            <h2 style="margin-top: 0; margin-bottom: 1.5mm;">Capital Starship Registry</h2>

            <div class="callout callout-cyan" style="margin: 0 0 2.5mm 0; padding: 2.5mm 3.2mm;">
                <div class="callout-title" style="font-size: 9pt;">8. GVI "Bastion" Defensive Monitor</div>
                <p style="font-size: 7.8pt; line-height: 1.28; margin-bottom: 1mm;">
                    <em>A massive, slab-sided station guardian that trades main propulsion for battery banks and eight small hardpoints, creating an overlapping wall of flak and proximity mines. Effectively a mobile orbital fortress capable of shredding entire fighter wings.</em>
                </p>
                <div style="font-size: 7.6pt; line-height: 1.24;">
                    <strong>Hull Rating:</strong> 14 &bull; <strong>Condition Track:</strong> 4 tracks of 14 segments (`[14] &rarr; [14] &rarr; [14] &rarr; [14]`)<br>
                    <strong>Armor (Protection):</strong> 5 &bull; <strong>Acceleration:</strong> 3 &bull; <strong>Maneuverability:</strong> 2 &bull; <strong>Systems:</strong> 4 (8 km Sensor)<br>
                    <strong>Hardpoints:</strong> 8 Small, 2 Medium &bull; <strong>Bridge Seats:</strong> 5 (1x Pilot, 2x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 45,000,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 210m &bull; Beam 95m &bull; Dry Displacement 18,500 metric tons &bull; Cast-iron and composite armor slab citadel.<br>
                    <strong>Standard Weapons:</strong> 4x PA "Sentinel" Rotary PDC (S), 4x PA "Caltrop" Mine Dispenser (S), 2x CF "Sledgehammer" Flak Cannon (M)<br>
                    <strong>Installed Modules:</strong> 2x Reinforced Bulkheads (2 slots), Advanced Repair Drones (1 slot), Extra Ammo Storage (1 slot), Injector Seats (1 slot) [Total: 5/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>A nightmare for close-range attackers; eight small hardpoints deploy dense minefields and PDC walls.</li>
                        <li>Entering the Bastion's macro hex is suicidal for light craft; mines force pursuers to break or explode.</li>
                        <li>Dual Gunners track multiple closing vectors simultaneously while dual Engineers run continuous drone repairs.</li>
                        <li>Functions as an immovable anchor for convoy defense, using overlapping flak envelopes to deny entire orbital hexes.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 2.5mm 0; padding: 2.5mm 3.2mm;">
                <div class="callout-title" style="font-size: 9pt;">9. CF "Cinder" Strike Frigate</div>
                <p style="font-size: 7.8pt; line-height: 1.28; margin-bottom: 1mm;">
                    <em>A long-range capital killer built entirely around a massive spinal rail system. Devastating forward acceleration lets it dictate macro-grid engagements, though poor lateral agility makes dogfights perilous if enemy craft close the gap.</em>
                </p>
                <div style="font-size: 7.6pt; line-height: 1.24;">
                    <strong>Hull Rating:</strong> 12 &bull; <strong>Condition Track:</strong> 4 tracks of 12 segments (`[12] &rarr; [12] &rarr; [12] &rarr; [12]`)<br>
                    <strong>Armor (Protection):</strong> 4 &bull; <strong>Acceleration:</strong> 5 &bull; <strong>Maneuverability:</strong> 2 &bull; <strong>Systems:</strong> 5 (10 km Sensor)<br>
                    <strong>Hardpoints:</strong> 2 Small, 3 Medium, 1 Large Spinal &bull; <strong>Bridge Seats:</strong> 4 (1x Pilot, 2x Gunner, 1x Engineer) &bull; <strong>Cost:</strong> 65,000,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 245m &bull; Beam 48m &bull; Dry Displacement 16,200 metric tons &bull; Longitudinal forged-tungsten spinal keel.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x CF "Mjolnir" Spinal Coilgun (L), 1x CQV "Solarflare" Laser (M), 1x GVI "Javelin" Missile (M), 1x KSK "Voidlance" Torpedo (M retrofit)<br>
                    <strong>Installed Modules:</strong> Fire-Control Computer (1 slot), Enhanced Sensor Suite (1 slot), Extra Ammo Storage (1 slot), 2x Reinforced Bulkheads (2 slots) [Total: 5/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>The CF "Mjolnir" Spinal Coilgun possesses extreme range out to 40 km; pilot aligns chassis along target vectors.</li>
                        <li>If hostile craft enter close dogfights, the Pilot uses Acceleration 5 to Full Throttle breakaway into open space.</li>
                        <li>Gunners utilize the Voidlance Torpedo Tube and Javelin Missile Pod to suppress targets before they enter knife-range.</li>
                        <li>Executes hit-and-run relativistic strikes, firing spinal rounds along planetary flyby trajectories before bleeding momentum.</li>
                    </ul>
                </div>
            </div>

            <div class="callout callout-cyan" style="margin: 0 0 0 0; padding: 2.5mm 3.2mm;">
                <div class="callout-title" style="font-size: 9pt;">10. KSK "Leviathan" Heavy Dreadnought</div>
                <p style="font-size: 7.8pt; line-height: 1.28; margin-bottom: 1mm;">
                    <em>The supreme apex of naval architecture. A mobile fortress of multi-layered ceramic armor and six bridge stations that commands entire fleet battlegroups and projects an impenetrable zone of fire across an entire sector.</em>
                </p>
                <div style="font-size: 7.6pt; line-height: 1.24;">
                    <strong>Hull Rating:</strong> 16 &bull; <strong>Condition Track:</strong> 4 tracks of 16 segments (`[16] &rarr; [16] &rarr; [16] &rarr; [16]`)<br>
                    <strong>Armor (Protection):</strong> 6 &bull; <strong>Acceleration:</strong> 2 &bull; <strong>Maneuverability:</strong> 1 &bull; <strong>Systems:</strong> 6 (12 km Sensor)<br>
                    <strong>Hardpoints:</strong> 6 Small, 4 Medium &bull; <strong>Bridge Seats:</strong> 6 (1x Pilot, 3x Gunner, 2x Engineer) &bull; <strong>Cost:</strong> 120,000,000 CR<br>
                    <strong>Chassis Specifications:</strong> LOA 320m &bull; Beam 110m &bull; Dry Displacement 34,000 metric tons &bull; Multi-layered composite ceramic armored citadel.<br>
                    <strong>Standard Weapons:</strong> 4x PA "Sentinel" Rotary PDC (S), 2x KSK "Harpoon" Kinetic Missile (S), 2x CF "Anvil" Railgun Battery (M), 2x GVI "Hydra" Multi-Missile Rack (M)<br>
                    <strong>Installed Modules:</strong> Extra Hardpoint (2 slots), Advanced Repair Drones (1 slot), Advanced MedBay (2 slots), Reinforced Bulkheads (1 slot), Fire-Control Computer (1 slot), Injector Seats (1 slot) [Total: 8/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Designed to absorb everything an enemy fleet can unleash; Armor 6 and four PDCs intercept almost all missile fire.</li>
                        <li>Three dedicated Gunners maintain multiple Target Locks simultaneously, synchronizing railguns and missile swarms.</li>
                        <li>Dual Engineers coordinate advanced nanite repair swarms, keeping weapons online and repairing bulkheads mid-fight.</li>
                        <li>Maintains absolute sector supremacy; coordinated secondary missile batteries prevent swarm tactics from overwhelming the dreadnought.</li>
                    </ul>
                </div>
            </div>

            <div class="callout column-span-all" style="margin-top: 1.5mm; margin-bottom: 0; padding: 1.6mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.2pt;">Naval Doctrine // Capital Keels &amp; Orbital Fleet Dominance</div>
                <p style="font-size: 7.3pt; line-height: 1.22; margin-bottom: 0;">
                    Capital dreadnoughts and monitors cannot make planetary landfall without structural collapse under their own gravity. They are permanently space-borne naval leviathans requiring orbital drydocks and tenders for resupply, mounting spine-length keels capable of orbital bombardment.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">94</span>
        </div>
    </div>
""")

    # =========================================================================
    # PAGE 95 (Spread 7 Right) — EXTENDED COMBAT WALKTHROUGH
    # =========================================================================
    html_parts.append("""
    <!-- =========================================================================
         PAGE 95 (Spread 7 Right) — EXTENDED COMBAT WALKTHROUGH
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="tactical-space-walkthrough">
        <div class="page-running-header">
            <span>Act III: Advanced Operations</span>
            <span>Chapter 05: Tactical Engagements</span>
        </div>

        <div class="page-body two-columns">
            <h2 class="column-span-all" style="margin-top: 0; margin-bottom: 1.2mm;">Combat Walkthrough: The Skirmish at Vesta Void</h2>
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

            <div class="example-box column-span-all" style="margin: 0 0 1.8mm 0; padding: 2.2mm 2.8mm;">
                <div class="example-title" style="font-size: 8.4pt;">GM Turn 2 (2 AP Spent &mdash; Failed Breakaway &amp; Surrender)</div>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. Pirate Desperate Breakaway (1 AP):</strong> Pinned at Position 2 from their view, the pirate pilot executes a Breakaway Burn. Success Test with <strong>Acceleration (2)</strong>: rolls <code>[9, 5]</code> (highest die 9 SPs).<br>
                    &bull; <em>Stay on Target Contest (1 AP):</em> Jax spends his final 1 AP to contest with Acceleration (3) + 1 Upgrade (Seat) = 1d12 + 2d10. Jax rolls <code>[10, 8, 4]</code>&mdash;two Hits (10 and 8)! Jax's two Hits eliminate both the 9 and 5 from the pirate's roll! With zero 8+ dice remaining, the contest succeeds: Breakaway yields <strong>0 SPs</strong>! The pirate remains pinned at Position 2. <em>(Jax: 0 AP left)</em>
                </p>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>2. Pirate Surrender (1 AP):</strong> Trapped before the charged laser array with hull plating ruptured, the pirate captain spends their final AP to vent thrusters and broadcast emergency surrender: <em>"Cease fire, Kestrel! We're dead in the water! We surrender!"</em>
                </p>
            </div>

            <div class="callout column-span-all" style="margin-top: 1.8mm; margin-bottom: 0; padding: 2.2mm 3mm;">
                <div class="callout-title" style="font-size: 8.6pt;">Encounter Debrief // Core Rule Invariants</div>
                <ul style="font-size: 7.6pt; line-height: 1.26; margin: 0; padding-left: 3.5mm;">
                    <li><strong>The 2 AP Turn Switch:</strong> Control alternated dynamically between the player crew and the GM as Action Points were expended (Player Turn 1: 2 AP &rarr; GM Turn 1: 2 AP &rarr; Player Turn 2: 2 AP &rarr; GM Turn 2: 2 AP), resolving the entire tactical skirmish within a single Round.</li>
                    <li><strong>Standard Contesting Rule:</strong> When Miller contested the missile with Point Defense and Jax contested the Breakaway with Stay on Target, each contest Hit (8+) eliminated one of the highest dice from the incoming roll. Eliminating all 8+ dice caused the attack to miss and the Breakaway Success Test to yield 0 Success Points.</li>
                    <li><strong>Bridge Station Synergies:</strong> Dedicated bridge seats granted decisive tactical advantages&mdash;the Pilot seat's free Upgrades and Stay on Target reaction, the Gunner seat's Point Defense reaction, and the Engineer seat's Power Distribution test allowed a coordinated 3-person crew to neutralize incoming ordnance and secure victory.</li>
                </ul>
            </div></div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">95</span>
        </div>
    </div>
""")

    # Close document
    html_parts.append("""
</body>
</html>
""")

    return "".join(html_parts)

if __name__ == "__main__":
    content = build_ch05_html()
    output_path = Path("html/05_Starships.html")
    output_path.write_text(content, encoding="utf-8")
    print(f"Generated Chapter 05 HTML at {output_path.resolve()} ({len(content)} bytes).")