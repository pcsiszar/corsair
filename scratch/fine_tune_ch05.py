#!/usr/bin/env python3
"""
Fine-tuning adjustments for Chapter 05:
1. Page 85: Remove the extra 'Bridge Casualties & Console Shunting' section to keep it strictly in 2 columns.
2. Page 86: Remove 'Chaff Screens & Flare Counter-Measures' (keep Recoil and Munition containment) to keep strictly in 2 columns.
3. Pages 88 & 89: Convert the standalone <p><strong>Mechanism:</strong> ...</p> into an inline mechanism within the <strong>Size:</strong> line, preventing extra paragraph break overhead.
4. Page 94: Tighten the Callout slightly so gap is ~18mm (fill ~92%) instead of 8.8mm.
"""
from pathlib import Path
import re

def fine_tune():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # 1. Page 85: remove Bridge Casualties
    p85_rem = """            <h3>Bridge Casualties &amp; Console Shunting</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">
                If a pilot or gunner is incapacitated by crushing G-Strain or concussion shock from hull-rattling torpedo detonations, secondary terminals can execute emergency console shunting. An operational crew member at any active workstation can spend 1 AP to re-route fire-control or thruster authority to their current display, assuming emergency vessel control without unstrapping from their acceleration couch mid-vector.
            </p>"""
    if p85_rem in code:
        code = code.replace(p85_rem, "")
        # ensure previous p has margin-bottom: 0
        code = code.replace("""            <h3>Combat Depressurization Protocols</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 1.5mm;">""",
                            """            <h3>Combat Depressurization Protocols</h3>
            <p style="font-size: 8.1pt; line-height: 1.32; margin-bottom: 0;">""")
        print("Page 85 fine-tuned.")
    else:
        print("Page 85 target not found.")

    # 2. Page 86: remove Chaff Screens
    p86_rem = """            <h3>Chaff Screens &amp; Flare Counter-Measures</h3>
            <p>
                When guided ordnance survives point-defense interception screens, crews rely on deployable counter-measures. Firing chaff pods blankets local void with millions of aluminized dipole fibers that reflect radar scatter, while pyrophoric magnesium flares create dazzling infrared decoys. These measures introduce electromagnetic noise, degrading the tracking algorithms of incoming missiles and forcing them to re-acquire their target vector.
            </p>"""
    if p86_rem in code:
        code = code.replace(p86_rem, "")
        print("Page 86 fine-tuned.")
    else:
        print("Page 86 target not found.")

    # 3. Pages 88 & 89: Inline the mechanism lines into the stats line
    # Match: <p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0.8mm; color: var(--text-body);"><strong>Mechanism:</strong> (.*?)</p>\s*<p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">\s*<strong>Size:</strong>
    inline_pat = re.compile(
        r'<p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0.8mm; color: var(--text-body);"><strong>Mechanism:</strong> (.*?)</p>\s*<p style="font-size: 7.6pt; line-height: 1.23; margin-bottom: 0.8mm;">\s*<strong>Size:</strong>',
        re.DOTALL
    )
    def repl_inline(m):
        mech = m.group(1).strip()
        return f'<p style="font-size: 7.5pt; line-height: 1.21; margin-bottom: 0.8mm;">\n                <strong>Mount:</strong> {mech}<br>\n                <strong>Size:</strong>'

    code, count = inline_pat.subn(repl_inline, code)
    print(f"Inlined mechanisms for {count} weapon profiles.")

    # 4. Page 94: Tighten callout slightly
    old_p94_callout = """            <div class="callout column-span-all" style="margin-top: 2mm; margin-bottom: 0; padding: 2mm 3mm;">
                <div class="callout-title" style="font-size: 8.4pt;">Naval Doctrine // Capital Keels &amp; Orbital Fleet Dominance</div>
                <p style="font-size: 7.5pt; line-height: 1.25; margin-bottom: 0;">
                    Capital dreadnoughts and monitors cannot make planetary landfall without suffering catastrophic structural collapse under their own gravity. They are permanently space-borne naval leviathans requiring orbital drydocks, fuel tankers, and pressurized crew shuttles for resupply. Mounting spine-length kinetic keels capable of orbital bombardment, their presence in any planetary orbit signifies absolute operational hegemony.
                </p>
            </div>"""

    new_p94_callout = """            <div class="callout column-span-all" style="margin-top: 1.5mm; margin-bottom: 0; padding: 1.6mm 2.8mm;">
                <div class="callout-title" style="font-size: 8.2pt;">Naval Doctrine // Capital Keels &amp; Orbital Fleet Dominance</div>
                <p style="font-size: 7.3pt; line-height: 1.22; margin-bottom: 0;">
                    Capital dreadnoughts and monitors cannot make planetary landfall without structural collapse under their own gravity. They are permanently space-borne naval leviathans requiring orbital drydocks and tenders for resupply, mounting spine-length keels capable of orbital bombardment.
                </p>
            </div>"""
    if old_p94_callout in code:
        code = code.replace(old_p94_callout, new_p94_callout)
        print("Page 94 callout tightened.")
    else:
        print("Page 94 callout target not found.")

    src_file.write_text(code, encoding="utf-8")
    print("fine_tune completed.")

if __name__ == "__main__":
    fine_tune()
