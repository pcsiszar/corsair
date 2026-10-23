#!/usr/bin/env python3
"""
Add Encounter Debrief callout to Page 95 to achieve ~88% fill with 0px overflow.
"""
from pathlib import Path

def add_p95_debrief():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    old_p95_end = """            <div class="example-box column-span-all" style="margin: 0 0 0 0; padding: 2.2mm 2.8mm;">
                <div class="example-title" style="font-size: 8.4pt;">GM Turn 2 (2 AP Spent &mdash; Failed Breakaway &amp; Surrender)</div>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 1mm;">
                    <strong>1. Pirate Desperate Breakaway (1 AP):</strong> Pinned at Position 2 from their view, the pirate pilot executes a Breakaway Burn. Success Test with <strong>Acceleration (2)</strong>: rolls <code>[9, 5]</code> (highest die 9 SPs).<br>
                    &bull; <em>Stay on Target Contest (1 AP):</em> Jax spends his final 1 AP to contest with Acceleration (3) + 1 Upgrade (Seat) = 1d12 + 2d10. Jax rolls <code>[10, 8, 4]</code>&mdash;two Hits (10 and 8)! Jax's two Hits eliminate both the 9 and 5 from the pirate's roll! With zero 8+ dice remaining, the contest succeeds: Breakaway yields <strong>0 SPs</strong>! The pirate remains pinned at Position 2. <em>(Jax: 0 AP left)</em>
                </p>
                <p style="font-size: 7.7pt; line-height: 1.25; margin-bottom: 0;">
                    <strong>2. Pirate Surrender (1 AP):</strong> Trapped before the charged laser array with hull plating ruptured, the pirate captain spends their final AP to vent thrusters and broadcast emergency surrender: <em>"Cease fire, Kestrel! We're dead in the water! We surrender!"</em>
                </p>
            </div>"""

    new_p95_end = """            <div class="example-box column-span-all" style="margin: 0 0 1.8mm 0; padding: 2.2mm 2.8mm;">
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
            </div>"""

    if old_p95_end in code:
        code = code.replace(old_p95_end, new_p95_end)
        print("Page 95 debrief added.")
    else:
        print("WARNING: Could not find old Page 95 end.")

    src_file.write_text(code, encoding="utf-8")
    print("Script written.")

if __name__ == "__main__":
    add_p95_debrief()
