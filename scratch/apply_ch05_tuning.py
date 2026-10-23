#!/usr/bin/env python3
"""
Tuning patch script for scratch/generate_ch05_starships.py.
Applies targeted micro-expansions to Pages 85, 86, 88, 89, 92, 93, 94 to bring all pages into the 84%–94% fill range.
"""
from pathlib import Path
import re

def update_ch05_script():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # 1. PAGE 85 EXPANSION: Add Combat Depressurization and Console Shunting
    old_p85_end = """            <h3>Auxiliary Stations &amp; Skeleton Crews</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">
                Larger starships carry multiple Gunner and Engineer consoles, allowing simultaneous defensive PDC coverage, missile targeting, and active damage control. Shorthanded vessels operating with a skeleton crew suffer severe tactical limitations: without a dedicated Gunner, PDCs cannot execute defensive reaction intercepts; without an Engineer, power cannot be redistributed and battle damage cannot be repaired mid-flight.
            </p>"""

    new_p85_end = """            <h3>Auxiliary Stations &amp; Skeleton Crews</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Larger starships carry multiple Gunner and Engineer consoles, allowing simultaneous defensive PDC coverage, missile targeting, and active damage control. Shorthanded vessels operating with a skeleton crew suffer severe tactical limitations: without a dedicated Gunner, PDCs cannot execute defensive reaction intercepts; without an Engineer, power cannot be redistributed and battle damage cannot be repaired mid-flight.
            </p>

            <h3>Combat Depressurization Protocols</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Prior to entering high-risk engagement envelopes, veteran corsair crews execute combat depressurization: internal atmospheric scrubbers pump cabin oxygen and nitrogen back into armored reserve tanks, reducing interior compartments to near-vacuum. By venting atmospheric gases before kinetic shells breach bulkheads, the danger of catastrophic cabin overpressure, violent explosive decompression, and out-of-control internal flash fires is eliminated. All personnel remain sealed inside pressurized EVA flight suits tethered to emergency oxygen umbilical lines.
            </p>

            <h3>Bridge Casualties &amp; Console Shunting</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">
                If a pilot or gunner is incapacitated by crushing G-Strain or concussion shock from hull-rattling torpedo detonations, secondary terminals can execute emergency console shunting. An operational crew member at any active workstation can spend 1 AP to re-route fire-control or thruster authority to their current display, assuming emergency vessel control without unstrapping from their acceleration couch mid-vector.
            </p>"""

    if old_p85_end in code:
        code = code.replace(old_p85_end, new_p85_end)
        print("Page 85 updated successfully.")
    else:
        print("WARNING: Could not find Page 85 target.")

    # 2. PAGE 86 EXPANSION: Add Kinetic Recoil, Magazine Safety, Chaff Screens
    old_p86_target = """            <h3>Target Lock &amp; EWAR Electronic Battles</h3>
            <p>
                Establishing a Target Lock represents flooding an enemy hull with ladar pulses, passive optical tracking, and thermal lock-on. Gunners acquire locks using a Systems Simple Test within Sensor Range. However, targets equipped with electronic counter-measure suites can deploy broad-spectrum noise and false radar echoes to shatter locks before ordnance can be launched.
            </p>"""

    new_p86_target = """            <h3>Target Lock &amp; EWAR Electronic Battles</h3>
            <p>
                Establishing a Target Lock represents flooding an enemy hull with ladar pulses, passive optical tracking, and thermal lock-on. Gunners acquire locks using a Systems Simple Test within Sensor Range. However, targets equipped with electronic counter-measure suites can deploy broad-spectrum noise and false radar echoes to shatter locks before ordnance can be launched.
            </p>

            <h3>Kinetic Recoil &amp; Reaction Counter-Thrusters</h3>
            <p>
                Naval kinetic weapons—particularly rotary PDCs and spinal rail cannons—produce violent Newton reaction forces upon discharge. A sustained six-barrel PDC burst against an incoming torpedo imparts hundreds of kilonewtons of counter-vector impulse. Automated avionics link firing triggers directly to attitude control thrusters, firing synchronized cold-gas counter-bursts to maintain the ship's gunnery alignment and prevent weapon recoil from throwing the vessel into an uncontrollable tumble.
            </p>

            <h3>Munition Containment &amp; Blowout Hatches</h3>
            <p>
                Storing hundreds of tons of high-explosive guided missiles and volatile propellant cakes inside a pressurized hull introduces existential risk of secondary cook-offs. Naval ammunition magazines are encased in dedicated armored containment coffins equipped with directional blowout hatches. If an incoming penetrator cooks off internal warhead racks, explosive pressure is vented directly into outer vacuum through rupture panels rather than collapsing internal living spaces.
            </p>

            <h3>Chaff Screens &amp; Flare Counter-Measures</h3>
            <p>
                When guided ordnance survives point-defense interception screens, crews rely on deployable counter-measures. Firing chaff pods blankets local void with millions of aluminized dipole fibers that reflect radar scatter, while pyrophoric magnesium flares create dazzling infrared decoys. These measures introduce electromagnetic noise, degrading the tracking algorithms of incoming missiles and forcing them to re-acquire their target vector.
            </p>"""

    if old_p86_target in code:
        code = code.replace(old_p86_target, new_p86_target)
        print("Page 86 updated successfully.")
    else:
        print("WARNING: Could not find Page 86 target.")

    # 3. PAGE 88 EXPANSION: Add physical mechanism lines to Profiles 1 to 11
    p88_mechanisms = [
        ('1. GVI "Buzzer" Seeker Drone', '<strong>Mechanism:</strong> Cold-gas attitude thrusters with micro-rocket sustainer and contact piezo-electric trigger fuze.'),
        ('2. PA "Sentinel" Rotary PDC', '<strong>Mechanism:</strong> Six-barrel motorized Gatling gimbal with liquid-nitrogen jacket and high-rate linkless ammunition feed.'),
        ('3. GVI "Stinger" Light Missile', '<strong>Mechanism:</strong> Solid-fuel booster core with gimbaled thrust-vector nozzle and dual optical/RF terminal sensor array.'),
        ('4. PA "Caltrop" Proximity Mine Dispenser', '<strong>Mechanism:</strong> Rear-venting pneumatic rotary rack launching magnetized shaped-charge canisters with command-destruct codes.'),
        ('5. CQV "Wasp" Pulse Laser', '<strong>Mechanism:</strong> Rapid-pulsing diode-pumped solid-state laser cavity mounted on high-traverse piezoelectric mirror mounts.'),
        ('6. PA "Guardian" Heavy PDC', '<strong>Mechanism:</strong> Motorized twin-barrel 30mm autocannon with integrated millimetric radar tracker and recoil-damping hydraulic dampers.'),
        ('7. KSK "Harpoon" Kinetic Missile', '<strong>Mechanism:</strong> High-density depleted uranium dart driven by two-stage solid rocket booster with inertial gyro autopilot.'),
        ('8. CF "Sledgehammer" Flak Cannon', '<strong>Mechanism:</strong> Heavy rifled naval cannon firing pre-fragmented titanium canister rounds with variable electronic time fuzes.'),
        ('9. CQV "Solarflare" Laser Array', '<strong>Mechanism:</strong> Multi-megawatt continuous-wave chemical oxygen-iodine laser channel with liquid-helium radiator loops.'),
        ('10. GVI "Javelin" Guided Missile Pod', '<strong>Mechanism:</strong> Hexagonal four-tube modular launch pod with pneumatic soft-ejection and programmable ripple-fire logic.'),
        ('11. KSK "Lance" Kinetic Torpedo', '<strong>Mechanism:</strong> Heavy hardened tungsten-carbide core encased in thermal ablative shroud with solid-fuel pursuit motor.')
    ]

    for title, mech in p88_mechanisms:
        # Insert mechanism right after the italicized description
        pattern = re.compile(rf'(<h4[^>]*>{re.escape(title)}</h4>\s*<p[^>]*><em>.*?</em></p>)', re.DOTALL)
        replacement = rf'\1\n            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0.8mm; color: var(--text-body);">{mech}</p>'
        if pattern.search(code):
            code = pattern.sub(replacement, code, count=1)
        else:
            print(f"WARNING: Could not find pattern for {title}")
    print("Page 88 mechanisms applied.")

    # 4. PAGE 89 EXPANSION: Add physical mechanism lines to Profiles 12 to 22
    p89_mechanisms = [
        ('12. CF "Anvil" Railgun Battery', '<strong>Mechanism:</strong> Parallel copper-alloy magnetic rail guides launching hypervelocity tungsten sabots at 25 kilometers per second.'),
        ('13. GVI "Breacher" Thermal Lance', '<strong>Mechanism:</strong> Overclocked industrial cutting beam focusing plasma-arc thermal energy through heavy sapphire magnetic collimators.'),
        ('14. GVI "Hydra" Multi-Missile Rack', '<strong>Mechanism:</strong> Pneumatic rapid-fire launcher dispensing ripple-fire cluster micro-missiles with coordinated swarm algorithms.'),
        ('15. CF "Bulwark" Point-Defense Battery', '<strong>Mechanism:</strong> Quad-barrel 40mm rotary battery tied directly to ship mainframe fire-control buses and dedicated cooling shunts.'),
        ('16. CQV "Eclipse" Particle Beam', '<strong>Mechanism:</strong> Electrostatic subatomic particle accelerator utilizing superconducting magnets to collimate relativistic ion streams.'),
        ('17. KSK "Voidlance" Fusion Torpedo Tube', '<strong>Mechanism:</strong> Pressurized naval torpedo tube launching multi-megaton thermonuclear warheads with armored terminal penetration caps.'),
        ('18. GVI "Cataclysm" Siege Torpedo', '<strong>Mechanism:</strong> Heavy demolition missile carrying high-yield shaped fusion payload with autonomous terminal dogfight thrusters.'),
        ('19. KSK "Specter" Stealth Missile', '<strong>Mechanism:</strong> Radar-absorbent ferrite composite airframe equipped with ultra-low-signature cold-gas vector thrusters.'),
        ('20. CF "Mjolnir" Spinal Coilgun', '<strong>Mechanism:</strong> Multi-stage electromagnetic induction coil assembly running the entire longitudinal structural keel of the vessel.'),
        ('21. CQV "Prometheus" Heavy Laser Array', '<strong>Mechanism:</strong> High-output continuous-wave chemical laser driven by triple-core ruby resonators and high-capacity radiator vanes.'),
        ('22. CF "Gigant" Heavy Railgun', '<strong>Mechanism:</strong> Super-heavy naval railgun barrel with reinforced cryogenic field coils, firing multi-ton hypervelocity kinetic penetrators.')
    ]

    for title, mech in p89_mechanisms:
        pattern = re.compile(rf'(<h4[^>]*>{re.escape(title)}</h4>\s*<p[^>]*><em>.*?</em></p>)', re.DOTALL)
        replacement = rf'\1\n            <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0.8mm; color: var(--text-body);">{mech}</p>'
        if pattern.search(code):
            code = pattern.sub(replacement, code, count=1)
        else:
            print(f"WARNING: Could not find pattern for {title}")
    print("Page 89 mechanisms applied.")

    # 5. PAGE 92 EXPANSION: Chassis specs + 4th doctrine point for small ships + Callout
    # Ship 1: Rusty Hook
    old_p92_s1 = """                    <strong>Standard Weapons:</strong> 1x PA "Sentinel" Rotary PDC (S), 1x PA "Caltrop" Mine Dispenser (S), 1x KSK "Harpoon" Kinetic Missile (S)<br>
                    <strong>Installed Modules:</strong> Extra Ammo Storage (1 slot), Injector Seats (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>The Rusty Hook is a close-quarters brawler that lures enemies in, using Armor 2 to absorb incoming fire.</li>
                        <li>Punishes pursuing craft with the PA "Caltrop" Mine Dispenser while landing high-velocity Harpoon penetrators.</li>
                        <li>Dual Engineer stations allow simultaneous power shunting to thrusters and active damage control in combat.</li>
                    </ul>"""

    new_p92_s1 = """                    <strong>Chassis Specifications:</strong> LOA 48m &bull; Beam 22m &bull; Dry Displacement 620 metric tons &bull; Welded container frame with high-tensile trunnions.<br>
                    <strong>Standard Weapons:</strong> 1x PA "Sentinel" Rotary PDC (S), 1x PA "Caltrop" Mine Dispenser (S), 1x KSK "Harpoon" Kinetic Missile (S)<br>
                    <strong>Installed Modules:</strong> Extra Ammo Storage (1 slot), Injector Seats (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>The Rusty Hook is a close-quarters brawler that lures enemies in, using Armor 2 to absorb incoming fire.</li>
                        <li>Punishes pursuing craft with the PA "Caltrop" Mine Dispenser while landing high-velocity Harpoon penetrators.</li>
                        <li>Dual Engineer stations allow simultaneous power shunting to thrusters and active damage control in combat.</li>
                        <li>Reinforced structural tow-winches allow rapid grappling and recovery of disabled derelict hulls in deep vacuum.</li>
                    </ul>"""

    # Ship 2: Kestrel
    old_p92_s2 = """                    <strong>Standard Weapons:</strong> 1x PA "Sentinel" Rotary PDC (S), 1x GVI "Stinger" Light Missile (S), 1x CQV "Solarflare" Laser Array (M)<br>
                    <strong>Installed Modules:</strong> Injector Seats (1 slot), Fire-Control Computer (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Versatile all-rounder with Systems 3 and 6 km Sensor Range, operating effectively across all tactical envelopes.</li>
                        <li>Carries a triad weapon mix: unguided PDC defense, guided Stinger burst, and sustained Solarflare thermal damage.</li>
                        <li>Balanced 4-seat bridge ensures Pilot, Gunner, and Engineers each have the tools needed to contribute to the fight.</li>
                    </ul>"""

    new_p92_s2 = """                    <strong>Chassis Specifications:</strong> LOA 62m &bull; Beam 28m &bull; Dry Displacement 850 metric tons &bull; Modular extruded titanium alloy monocoque.<br>
                    <strong>Standard Weapons:</strong> 1x PA "Sentinel" Rotary PDC (S), 1x GVI "Stinger" Light Missile (S), 1x CQV "Solarflare" Laser Array (M)<br>
                    <strong>Installed Modules:</strong> Injector Seats (1 slot), Fire-Control Computer (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Versatile all-rounder with Systems 3 and 6 km Sensor Range, operating effectively across all tactical envelopes.</li>
                        <li>Carries a triad weapon mix: unguided PDC defense, guided Stinger burst, and sustained Solarflare thermal damage.</li>
                        <li>Balanced 4-seat bridge ensures Pilot, Gunner, and Engineers each have the tools needed to contribute to the fight.</li>
                        <li>Slaves sensor telemetry through the Fire-Control Computer to share precision Target Locks across allied escorts.</li>
                    </ul>"""

    # Ship 3: Shinobi
    old_p92_s3 = """                    <strong>Standard Weapons:</strong> 1x CQV "Wasp" Pulse Laser (S), 1x KSK "Specter" Stealth Missile (M)<br>
                    <strong>Installed Modules:</strong> Signal Scrambler (1 slot), Fire-Control Computer (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Relies on stealth and first-strike capability; Systems 4 and 8 km sensors acquire locks before detection.</li>
                        <li>Uses extreme Maneuverability 7 to maintain Advantage (8–10) while staying out of the enemy's forward firing cone.</li>
                        <li>Signal Scrambler enables the Engineer to break hostile locks while the Gunner fires stealth Specter missiles.</li>
                    </ul>"""

    new_p92_s3 = """                    <strong>Chassis Specifications:</strong> LOA 54m &bull; Beam 20m &bull; Dry Displacement 480 metric tons &bull; Faceted carbon-nanotube radar-absorbent shell.<br>
                    <strong>Standard Weapons:</strong> 1x CQV "Wasp" Pulse Laser (S), 1x KSK "Specter" Stealth Missile (M)<br>
                    <strong>Installed Modules:</strong> Signal Scrambler (1 slot), Fire-Control Computer (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Relies on stealth and first-strike capability; Systems 4 and 8 km sensors acquire locks before detection.</li>
                        <li>Uses extreme Maneuverability 7 to maintain Advantage (8–10) while staying out of the enemy's forward firing cone.</li>
                        <li>Signal Scrambler enables the Engineer to break hostile locks while the Gunner fires stealth Specter missiles.</li>
                        <li>Cools outer hull plating with internal liquid-helium heat sinks to vanish completely from enemy passive IR sensors.</li>
                    </ul>"""

    # Ship 4: Talon
    old_p92_s4 = """                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x GVI "Javelin" Missile Pod (M)<br>
                    <strong>Installed Modules:</strong> Injector Seats (1 slot), Auto-Loaders (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Excels at closing distance rapidly to establish Advantage (Positions 8–10) using high Maneuverability 6.</li>
                        <li>Once on the target's tail, Gunner fires Javelin guided missiles while Auto-Loaders cycle rapid follow-up salvos.</li>
                        <li>Dual Gunner seats ensure complete coverage of both offensive missile targeting and defensive PDC interception.</li>
                    </ul>"""

    new_p92_s4 = """                    <strong>Chassis Specifications:</strong> LOA 58m &bull; Beam 24m &bull; Dry Displacement 710 metric tons &bull; Reinforced tubular aerospace alloy spaceframe.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x GVI "Javelin" Missile Pod (M)<br>
                    <strong>Installed Modules:</strong> Injector Seats (1 slot), Auto-Loaders (1 slot) [Total: 2/4 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.3pt; line-height: 1.2; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Excels at closing distance rapidly to establish Advantage (Positions 8–10) using high Maneuverability 6.</li>
                        <li>Once on the target's tail, Gunner fires Javelin guided missiles while Auto-Loaders cycle rapid follow-up salvos.</li>
                        <li>Dual Gunner seats ensure complete coverage of both offensive missile targeting and defensive PDC interception.</li>
                        <li>High lateral RCS clusters allow radical 180-degree flip-and-burn vector turns without bleeding closing velocity.</li>
                    </ul>"""

    code = code.replace(old_p92_s1, new_p92_s1)
    code = code.replace(old_p92_s2, new_p92_s2)
    code = code.replace(old_p92_s3, new_p92_s3)
    code = code.replace(old_p92_s4, new_p92_s4)

    # Add Callout at bottom of Page 92
    p92_end_pattern = """            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">92</span>"""

    p92_callout = """            </div>

            <div class="callout column-span-all" style="margin-top: 2mm; margin-bottom: 0; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 8.4pt;">Doctrine // Small Craft Operational Logistics</div>
                <p style="font-size: 7.5pt; line-height: 1.25; margin-bottom: 0;">
                    Small starships represent the tactical backbone of corsair privateering across the Sphere. Their low displacement allows agile thrust-to-weight ratios and minimal reaction water consumption during interplanetary transit. However, limited internal magazine volume requires disciplined fire control: pilots who exhaust their ordnance in early skirmishes must flee to friendly orbital stations or face capital gunboats with empty launcher racks.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">92</span>"""

    code = code.replace(p92_end_pattern, p92_callout)
    print("Page 92 updated successfully.")

    # 6. PAGE 93 EXPANSION: Medium Ships Chassis specs + 5th doctrine point + Callout
    # Ship 5: Ironbound
    old_p93_s5 = """                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 2x Empty Small Mounts, 1x CQV "Solarflare" Laser Array (M), 1x CF "Sledgehammer" Flak Cannon (M)<br>
                    <strong>Installed Modules:</strong> Advanced MedBay (2 slots), Advanced Repair Drones (1 slot), Reinforced Bulkheads (1 slot) [Total: 4/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Operates on a war of attrition; Armor 3 reduces damage while 10-wound tracks absorb heavy punishment.</li>
                        <li>Engineer shunts power to Weapons or Systems, granting Upgrades to the Gunner's laser and flak strikes.</li>
                        <li>Gunner weakens targets with continuous thermal beams before tearing through exposed hulls with flak bursts.</li>
                        <li>Second Engineer directs Advanced Repair Drones with Knowledge + Systems to restore integrity mid-combat.</li>
                    </ul>"""

    new_p93_s5 = """                    <strong>Chassis Specifications:</strong> LOA 112m &bull; Beam 44m &bull; Dry Displacement 3,400 metric tons &bull; Cast-steel multi-frame keel with heavy bulkhead web.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 2x Empty Small Mounts, 1x CQV "Solarflare" Laser Array (M), 1x CF "Sledgehammer" Flak Cannon (M)<br>
                    <strong>Installed Modules:</strong> Advanced MedBay (2 slots), Advanced Repair Drones (1 slot), Reinforced Bulkheads (1 slot) [Total: 4/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Operates on a war of attrition; Armor 3 reduces damage while 10-wound tracks absorb heavy punishment.</li>
                        <li>Engineer shunts power to Weapons or Systems, granting Upgrades to the Gunner's laser and flak strikes.</li>
                        <li>Gunner weakens targets with continuous thermal beams before tearing through exposed hulls with flak bursts.</li>
                        <li>Second Engineer directs Advanced Repair Drones with Knowledge + Systems to restore integrity mid-combat.</li>
                        <li>Internal hydro-recyclers and expansive machine shops permit months of independent patrol off civilized supply lanes.</li>
                    </ul>"""

    # Ship 6: Falcon
    old_p93_s6 = """                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x PA "Guardian" Heavy PDC (M), 1x CF "Anvil" Railgun Battery (M), 1x GVI "Javelin" Missile Pod (M)<br>
                    <strong>Installed Modules:</strong> Advanced MedBay (2 slots), Extra Ammo Storage (1 slot) [Total: 3/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Uses Armor 4 and dual PDC screens to withstand incoming missile salvos while closing engagement gaps.</li>
                        <li>The CF "Anvil" Railgun Battery delivers consistent kinetic trauma across medium Macro-Grid ranges (10–20 km).</li>
                        <li>Focuses on area denial and intercepting hostile boarding craft before they reach docking collars.</li>
                        <li>Dual Gunner stations allow simultaneous long-range railgun fire and defensive point-defense interception.</li>
                    </ul>"""

    new_p93_s6 = """                    <strong>Chassis Specifications:</strong> LOA 135m &bull; Beam 52m &bull; Dry Displacement 4,600 metric tons &bull; Double-hulled layered composite armored belt.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x PA "Guardian" Heavy PDC (M), 1x CF "Anvil" Railgun Battery (M), 1x GVI "Javelin" Missile Pod (M)<br>
                    <strong>Installed Modules:</strong> Advanced MedBay (2 slots), Extra Ammo Storage (1 slot) [Total: 3/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Uses Armor 4 and dual PDC screens to withstand incoming missile salvos while closing engagement gaps.</li>
                        <li>The CF "Anvil" Railgun Battery delivers consistent kinetic trauma across medium Macro-Grid ranges (10–20 km).</li>
                        <li>Focuses on area denial and intercepting hostile boarding craft before they reach docking collars.</li>
                        <li>Dual Gunner stations allow simultaneous long-range railgun fire and defensive point-defense interception.</li>
                        <li>Interlocking fire arcs create a forward kill corridor that prevents smaller corvettes from closing without taking heavy rail fire.</li>
                    </ul>"""

    # Ship 7: Dagger
    old_p93_s7 = """                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x KSK "Lance" Kinetic Torpedo (M), 1x CQV "Eclipse" Particle Beam (M)<br>
                    <strong>Installed Modules:</strong> Fire-Control Computer (1 slot), Enhanced Sensor Suite (1 slot) [Total: 2/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Unrivaled at the Breakaway contest, using Acceleration 5 to stay glued to an escaping target's tail.</li>
                        <li>The CQV "Eclipse" Particle Beam maintains tight beam focus out to 4 km, softening armor before torpedo impact.</li>
                        <li>The KSK "Lance" Kinetic Torpedo uses heavy kinetic closing velocity to punch directly into hostile engine compartments.</li>
                    </ul>"""

    new_p93_s7 = """                    <strong>Chassis Specifications:</strong> LOA 120m &bull; Beam 36m &bull; Dry Displacement 3,800 metric tons &bull; High-density ceramic-matrix reinforced pursuit chassis.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x KSK "Lance" Kinetic Torpedo (M), 1x CQV "Eclipse" Particle Beam (M)<br>
                    <strong>Installed Modules:</strong> Fire-Control Computer (1 slot), Enhanced Sensor Suite (1 slot) [Total: 2/8 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Unrivaled at the Breakaway contest, using Acceleration 5 to stay glued to an escaping target's tail.</li>
                        <li>The CQV "Eclipse" Particle Beam maintains tight beam focus out to 4 km, softening armor before torpedo impact.</li>
                        <li>The KSK "Lance" Kinetic Torpedo uses heavy kinetic closing velocity to punch directly into hostile engine compartments.</li>
                        <li>Supercooled cryogenic sensor arrays burn through passive electromagnetic stealth at ranges exceeding 10 kilometers.</li>
                    </ul>"""

    code = code.replace(old_p93_s5, new_p93_s5)
    code = code.replace(old_p93_s6, new_p93_s6)
    code = code.replace(old_p93_s7, new_p93_s7)

    # Add Callout at bottom of Page 93
    p93_end_pattern = """            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">93</span>"""

    p93_callout = """            </div>

            <div class="callout column-span-all" style="margin-top: 2mm; margin-bottom: 0; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 8.4pt;">Doctrine // Medium Hull Endurance &amp; Hydro-Loops</div>
                <p style="font-size: 7.5pt; line-height: 1.25; margin-bottom: 0;">
                    Medium hulls (80–150m) represent independent expeditionary platforms capable of long-range interplanetary transit. Unlike cramped corvettes, their internal displacement accommodates private bunk spaces, closed-loop hydroponic water recycling, and multi-week vacuum endurance. This operational self-sufficiency makes them the premier choice for corsair crews venturing far beyond the inner moons into uncharted asteroid corridors.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">93</span>"""

    code = code.replace(p93_end_pattern, p93_callout)
    print("Page 93 updated successfully.")

    # 7. PAGE 94 EXPANSION: Capital Ships Chassis specs + 4th doctrine point + Callout
    # Ship 8: Bastion
    old_p94_s8 = """                    <strong>Standard Weapons:</strong> 4x PA "Sentinel" Rotary PDC (S), 4x PA "Caltrop" Mine Dispenser (S), 2x CF "Sledgehammer" Flak Cannon (M)<br>
                    <strong>Installed Modules:</strong> 2x Reinforced Bulkheads (2 slots), Advanced Repair Drones (1 slot), Extra Ammo Storage (1 slot), Injector Seats (1 slot) [Total: 5/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>A nightmare for close-range attackers; eight small hardpoints deploy dense minefields and PDC walls.</li>
                        <li>Entering the Bastion's macro hex is suicidal for light craft; mines force pursuers to break or explode.</li>
                        <li>Dual Gunners track multiple closing vectors simultaneously while dual Engineers run continuous drone repairs.</li>
                    </ul>"""

    new_p94_s8 = """                    <strong>Chassis Specifications:</strong> LOA 210m &bull; Beam 95m &bull; Dry Displacement 18,500 metric tons &bull; Cast-iron and composite armor slab citadel.<br>
                    <strong>Standard Weapons:</strong> 4x PA "Sentinel" Rotary PDC (S), 4x PA "Caltrop" Mine Dispenser (S), 2x CF "Sledgehammer" Flak Cannon (M)<br>
                    <strong>Installed Modules:</strong> 2x Reinforced Bulkheads (2 slots), Advanced Repair Drones (1 slot), Extra Ammo Storage (1 slot), Injector Seats (1 slot) [Total: 5/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>A nightmare for close-range attackers; eight small hardpoints deploy dense minefields and PDC walls.</li>
                        <li>Entering the Bastion's macro hex is suicidal for light craft; mines force pursuers to break or explode.</li>
                        <li>Dual Gunners track multiple closing vectors simultaneously while dual Engineers run continuous drone repairs.</li>
                        <li>Functions as an immovable anchor for convoy defense, using overlapping flak envelopes to deny entire orbital hexes.</li>
                    </ul>"""

    # Ship 9: Cinder
    old_p94_s9 = """                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x CF "Mjolnir" Spinal Coilgun (L), 1x CQV "Solarflare" Laser (M), 1x GVI "Javelin" Missile (M), 1x KSK "Voidlance" Torpedo (M retrofit)<br>
                    <strong>Installed Modules:</strong> Fire-Control Computer (1 slot), Enhanced Sensor Suite (1 slot), Extra Ammo Storage (1 slot), 2x Reinforced Bulkheads (2 slots) [Total: 5/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>The CF "Mjolnir" Spinal Coilgun possesses extreme range out to 40 km; pilot aligns chassis along target vectors.</li>
                        <li>If hostile craft enter close dogfights, the Pilot uses Acceleration 5 to Full Throttle breakaway into open space.</li>
                        <li>Gunners utilize the Voidlance Torpedo Tube and Javelin Missile Pod to suppress targets before they enter knife-range.</li>
                    </ul>"""

    new_p94_s9 = """                    <strong>Chassis Specifications:</strong> LOA 245m &bull; Beam 48m &bull; Dry Displacement 16,200 metric tons &bull; Longitudinal forged-tungsten spinal keel.<br>
                    <strong>Standard Weapons:</strong> 2x PA "Sentinel" Rotary PDC (S), 1x CF "Mjolnir" Spinal Coilgun (L), 1x CQV "Solarflare" Laser (M), 1x GVI "Javelin" Missile (M), 1x KSK "Voidlance" Torpedo (M retrofit)<br>
                    <strong>Installed Modules:</strong> Fire-Control Computer (1 slot), Enhanced Sensor Suite (1 slot), Extra Ammo Storage (1 slot), 2x Reinforced Bulkheads (2 slots) [Total: 5/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>The CF "Mjolnir" Spinal Coilgun possesses extreme range out to 40 km; pilot aligns chassis along target vectors.</li>
                        <li>If hostile craft enter close dogfights, the Pilot uses Acceleration 5 to Full Throttle breakaway into open space.</li>
                        <li>Gunners utilize the Voidlance Torpedo Tube and Javelin Missile Pod to suppress targets before they enter knife-range.</li>
                        <li>Executes hit-and-run relativistic strikes, firing spinal rounds along planetary flyby trajectories before bleeding momentum.</li>
                    </ul>"""

    # Ship 10: Leviathan
    old_p94_s10 = """                    <strong>Standard Weapons:</strong> 4x PA "Sentinel" Rotary PDC (S), 2x KSK "Harpoon" Kinetic Missile (S), 2x CF "Anvil" Railgun Battery (M), 2x GVI "Hydra" Multi-Missile Rack (M)<br>
                    <strong>Installed Modules:</strong> Extra Hardpoint (2 slots), Advanced Repair Drones (1 slot), Advanced MedBay (2 slots), Reinforced Bulkheads (1 slot), Fire-Control Computer (1 slot), Injector Seats (1 slot) [Total: 8/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Designed to absorb everything an enemy fleet can unleash; Armor 6 and four PDCs intercept almost all missile fire.</li>
                        <li>Three dedicated Gunners maintain multiple Target Locks simultaneously, synchronizing railguns and missile swarms.</li>
                        <li>Dual Engineers coordinate advanced nanite repair swarms, keeping weapons online and repairing bulkheads mid-fight.</li>
                    </ul>"""

    new_p94_s10 = """                    <strong>Chassis Specifications:</strong> LOA 320m &bull; Beam 110m &bull; Dry Displacement 34,000 metric tons &bull; Multi-layered composite ceramic armored citadel.<br>
                    <strong>Standard Weapons:</strong> 4x PA "Sentinel" Rotary PDC (S), 2x KSK "Harpoon" Kinetic Missile (S), 2x CF "Anvil" Railgun Battery (M), 2x GVI "Hydra" Multi-Missile Rack (M)<br>
                    <strong>Installed Modules:</strong> Extra Hardpoint (2 slots), Advanced Repair Drones (1 slot), Advanced MedBay (2 slots), Reinforced Bulkheads (1 slot), Fire-Control Computer (1 slot), Injector Seats (1 slot) [Total: 8/12 Slots]<br>
                    <strong>Tactical Doctrine:</strong>
                    <ul style="font-size: 7.4pt; line-height: 1.21; margin: 0.5mm 0 0 0; padding-left: 3mm;">
                        <li>Designed to absorb everything an enemy fleet can unleash; Armor 6 and four PDCs intercept almost all missile fire.</li>
                        <li>Three dedicated Gunners maintain multiple Target Locks simultaneously, synchronizing railguns and missile swarms.</li>
                        <li>Dual Engineers coordinate advanced nanite repair swarms, keeping weapons online and repairing bulkheads mid-fight.</li>
                        <li>Maintains absolute sector supremacy; coordinated secondary missile batteries prevent swarm tactics from overwhelming the dreadnought.</li>
                    </ul>"""

    code = code.replace(old_p94_s8, new_p94_s8)
    code = code.replace(old_p94_s9, new_p94_s9)
    code = code.replace(old_p94_s10, new_p94_s10)

    # Add Callout at bottom of Page 94
    p94_end_pattern = """            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">94</span>"""

    p94_callout = """            </div>

            <div class="callout column-span-all" style="margin-top: 2mm; margin-bottom: 0; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 8.4pt;">Naval Doctrine // Capital Keels &amp; Orbital Fleet Dominance</div>
                <p style="font-size: 7.5pt; line-height: 1.25; margin-bottom: 0;">
                    Capital dreadnoughts and monitors cannot make planetary landfall without suffering catastrophic structural collapse under their own gravity. They are permanently space-borne naval leviathans requiring orbital drydocks, fuel tankers, and pressurized crew shuttles for resupply. Mounting spine-length kinetic keels capable of orbital bombardment, their presence in any planetary orbit signifies absolute operational hegemony.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">94</span>"""

    code = code.replace(p94_end_pattern, p94_callout)
    print("Page 94 updated successfully.")

    src_file.write_text(code, encoding="utf-8")
    print("scratch/generate_ch05_starships.py updated and written.")

if __name__ == "__main__":
    update_ch05_script()
