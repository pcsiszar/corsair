#!/usr/bin/env python3
"""
Fix Page 85 and Page 86 to keep them strictly within 2 columns (0px overflow) while maintaining ~88-92% fill.
"""
from pathlib import Path

def fix_85_86():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # 1. Page 85: Merge Combat Depressurization into Damage Control, remove separate h3
    old_p85_block = """            <h3>Damage Control Teams in Zero-G</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                When penetrating hits buckle outer bulkheads, damage control teams don magnetic boots and pressurized patch-suits to manually seal compartments, dog down emergency hatches, and flood burning avionics bays with halon gas. Crew members unassigned to primary flight stations can spend 1 AP to assist the Engineer's repair tests, granting +1 Upgrade to the check.
            </p>

            <h3>Auxiliary Stations &amp; Skeleton Crews</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                Larger starships carry multiple Gunner and Engineer consoles, allowing simultaneous defensive PDC coverage, missile targeting, and active damage control. Shorthanded vessels operating with a skeleton crew suffer severe tactical limitations: without a dedicated Gunner, PDCs cannot execute defensive reaction intercepts; without an Engineer, power cannot be redistributed and battle damage cannot be repaired mid-flight.
            </p>

            <h3>Combat Depressurization Protocols</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">
                Prior to entering high-risk engagement envelopes, veteran corsair crews execute combat depressurization: internal atmospheric scrubbers pump cabin oxygen and nitrogen back into armored reserve tanks, reducing interior compartments to near-vacuum. By venting atmospheric gases before kinetic shells breach bulkheads, the danger of catastrophic cabin overpressure, violent explosive decompression, and out-of-control internal flash fires is eliminated. All personnel remain sealed inside pressurized EVA flight suits tethered to emergency oxygen umbilical lines.
            </p>"""

    new_p85_block = """            <h3>Damage Control Teams &amp; Combat Depressurization</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">
                When penetrating hits buckle outer bulkheads, damage control teams don magnetic boots and pressurized patch-suits to manually seal compartments, dog down emergency hatches, and flood burning avionics bays with halon gas. Crew members unassigned to primary flight stations can spend 1 AP to assist the Engineer's repair tests, granting +1 Upgrade to the check. Prior to engagement, veteran crews execute combat depressurization, pumping cabin air back into reserve tanks to eliminate explosive decompression and flash fires when bulkheads are breached.
            </p>

            <h3>Auxiliary Stations &amp; Skeleton Crews</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">
                Larger starships carry multiple Gunner and Engineer consoles, allowing simultaneous defensive PDC coverage, missile targeting, and active damage control. Shorthanded vessels operating with a skeleton crew suffer severe tactical limitations: without a dedicated Gunner, PDCs cannot execute defensive reaction intercepts; without an Engineer, power cannot be redistributed and battle damage cannot be repaired mid-flight.
            </p>"""

    if old_p85_block in code:
        code = code.replace(old_p85_block, new_p85_block)
        print("Page 85 merged block updated.")
    else:
        print("WARNING: Could not find Page 85 block.")

    # 2. Page 86: Merge Kinetic Recoil and Munition Containment into single section
    old_p86_block = """            <h3>Kinetic Recoil &amp; Reaction Counter-Thrusters</h3>
            <p>
                Naval kinetic weapons—particularly rotary PDCs and spinal rail cannons—produce violent Newton reaction forces upon discharge. A sustained six-barrel PDC burst against an incoming torpedo imparts hundreds of kilonewtons of counter-vector impulse. Automated avionics link firing triggers directly to attitude control thrusters, firing synchronized cold-gas counter-bursts to maintain the ship's gunnery alignment and prevent weapon recoil from throwing the vessel into an uncontrollable tumble.
            </p>

            <h3>Munition Containment &amp; Blowout Hatches</h3>
            <p>
                Storing hundreds of tons of high-explosive guided missiles and volatile propellant cakes inside a pressurized hull introduces existential risk of secondary cook-offs. Naval ammunition magazines are encased in dedicated armored containment coffins equipped with directional blowout hatches. If an incoming penetrator cooks off internal warhead racks, explosive pressure is vented directly into outer vacuum through rupture panels rather than collapsing internal living spaces.
            </p>"""

    new_p86_block = """            <h3>Recoil Dynamics &amp; Munitions Safety</h3>
            <p>
                Naval kinetic weapons—particularly rotary PDCs and spinal rail cannons—produce violent Newton reaction forces upon discharge. Automated avionics link firing triggers directly to attitude control thrusters, firing synchronized cold-gas counter-bursts to maintain gunnery alignment and prevent recoil from imparting unwanted angular tumble. Furthermore, high-explosive torpedo magazines are encased in armored containment coffins equipped with directional blowout hatches, venting secondary cook-offs into outer vacuum rather than collapsing interior decks.
            </p>"""

    if old_p86_block in code:
        code = code.replace(old_p86_block, new_p86_block)
        print("Page 86 merged block updated.")
    else:
        print("WARNING: Could not find Page 86 block.")

    src_file.write_text(code, encoding="utf-8")
    print("Script written.")

if __name__ == "__main__":
    fix_85_86()
