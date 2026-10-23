#!/usr/bin/env python3
"""
Perfect tune for Page 85 and Page 86.
"""
from pathlib import Path

def apply_perfect_p85_p86():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # 1. Page 85: Replace the bottom half of Page 85
    old_p85_bottom = """            <h3>Bridge Communication Protocols</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Combat operations demand strict voice discipline under high acceleration. Gunners announce lock-on solutions ("Ladar hard on bearing two-seven, salvo away"), while engineers confirm reactor load tolerances ("Shunting four megawatts to RCS manifold, capacitors holding"). Spacers who talk over the primary comm loop risk catastrophic miscoordination.
            </p>

            <h3>EWAR &amp; Sensor Warfare Stations</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Dedicated electronic warfare (EWAR) consoles monitor passive radio frequency emissions, ladar scatter, and drive plume thermals. From this station, an operator can execute <em>Passive Surveillance</em> to track hostile vessels without radiating active ladar signatures, maintaining stealth until firing solutions are passed to weapons stations.
            </p>

            <h3>Damage Control Teams &amp; Combat Depressurization</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                When penetrating hits buckle outer bulkheads, damage control teams don magnetic boots and pressurized patch-suits to manually seal compartments, dog down emergency hatches, and flood burning avionics bays with halon gas. Crew members unassigned to primary flight stations can spend 1 AP to assist the Engineer's repair tests, granting +1 Upgrade to the check. Prior to engagement, veteran crews execute combat depressurization, pumping cabin air back into reserve tanks to eliminate explosive decompression and flash fires when bulkheads are breached.
            </p>

            <h3>Auxiliary Stations &amp; Skeleton Crews</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">
                Larger starships carry multiple Gunner and Engineer consoles, allowing simultaneous defensive PDC coverage, missile targeting, and active damage control. Shorthanded vessels operating with a skeleton crew suffer severe tactical limitations: without a dedicated Gunner, PDCs cannot execute defensive reaction intercepts; without an Engineer, power cannot be redistributed and battle damage cannot be repaired mid-flight.
            </p>"""

    new_p85_bottom = """            <h3>Tactical Comms &amp; Sensor Warfare</h3>
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
            </p>"""

    if old_p85_bottom in code:
        code = code.replace(old_p85_bottom, new_p85_bottom)
        print("Page 85 tightened successfully.")
    else:
        print("WARNING: Could not find Page 85 bottom.")

    # 2. Page 86: Tighten Recoil Dynamics
    old_p86_recoil = """            <h3>Recoil Dynamics &amp; Munitions Safety</h3>
            <p>
                Naval kinetic weapons—particularly rotary PDCs and spinal rail cannons—produce violent Newton reaction forces upon discharge. Automated avionics link firing triggers directly to attitude control thrusters, firing synchronized cold-gas counter-bursts to maintain gunnery alignment and prevent recoil from imparting unwanted angular tumble. Furthermore, high-explosive torpedo magazines are encased in armored containment coffins equipped with directional blowout hatches, venting secondary cook-offs into outer vacuum rather than collapsing interior decks.
            </p>"""

    new_p86_recoil = """            <h3>Recoil Dynamics &amp; Munitions Safety</h3>
            <p>
                Naval kinetic weapons produce violent Newton reaction forces upon discharge. Automated avionics fire synchronized cold-gas counter-bursts to maintain gunnery alignment and prevent recoil tumble. Furthermore, high-explosive torpedo magazines are encased in armored containment coffins with directional blowout hatches, venting secondary cook-offs into outer vacuum rather than collapsing interior decks.
            </p>"""

    if old_p86_recoil in code:
        code = code.replace(old_p86_recoil, new_p86_recoil)
        print("Page 86 tightened successfully.")
    else:
        print("WARNING: Could not find Page 86 recoil.")

    src_file.write_text(code, encoding="utf-8")
    print("Script written.")

if __name__ == "__main__":
    apply_perfect_p85_p86()
