#!/usr/bin/env python3
"""
Tuning patch script for Pages 88 and 89 in scratch/generate_ch05_starships.py.
"""
from pathlib import Path

def patch_weapons():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # Dictionary of (unique text in stats line, mechanism text to insert before it)
    patches = [
        # Page 88
        ('<strong>Size:</strong> Small &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 1 &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 6 &bull; <strong>Cost:</strong> 200,000 CR.',
         '<strong>Mechanism:</strong> Cold-gas attitude thrusters with micro-rocket sustainer and contact piezo-electric trigger fuze.'),
        
        ('<strong>Size:</strong> Small &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 2/3/3 &bull; <strong>Macro Acc:</strong> 1/0/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (5)',
         '<strong>Mechanism:</strong> Six-barrel motorized Gatling gimbal with liquid-nitrogen jacket and high-rate linkless ammunition feed.'),
        
        ('<strong>Size:</strong> Small &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 2 &bull; <strong>Damage:</strong> +3 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 4 &bull; <strong>Cost:</strong> 300,000 CR.',
         '<strong>Mechanism:</strong> Solid-fuel booster core with gimbaled thrust-vector nozzle and dual optical/RF terminal sensor array.'),
        
        ('<strong>Size:</strong> Small &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 3/&mdash;/&mdash; &bull; <strong>Macro Acc:</strong> &mdash; &bull; <strong>Damage:</strong> +6',
         '<strong>Mechanism:</strong> Rear-venting pneumatic rotary rack launching magnetized shaped-charge canisters with command-destruct codes.'),
        
        ('<strong>Size:</strong> Small &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/2/3 &bull; <strong>Macro Acc:</strong> 1/&mdash;/&mdash;/&mdash;/&mdash; &bull; <strong>Damage:</strong> +1',
         '<strong>Mechanism:</strong> Rapid-pulsing diode-pumped solid-state laser cavity mounted on high-traverse piezoelectric mirror mounts.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 1/2/2 &bull; <strong>Macro Acc:</strong> 2/1/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (4)',
         '<strong>Mechanism:</strong> Motorized twin-barrel 30mm autocannon with integrated millimetric radar tracker and recoil-damping hydraulic dampers.'),
        
        ('<strong>Size:</strong> Small &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 4 &bull; <strong>Damage:</strong> +1 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 6 &bull; <strong>Cost:</strong> 650,000 CR.',
         '<strong>Mechanism:</strong> High-density depleted uranium dart driven by two-stage solid rocket booster with inertial gyro autopilot.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/2 &bull; <strong>Macro Acc:</strong> 1/&mdash;/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (3)',
         '<strong>Mechanism:</strong> Heavy rifled naval cannon firing pre-fragmented titanium canister rounds with variable electronic time fuzes.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/2 &bull; <strong>Macro Acc:</strong> 2/1/0/&mdash;/&mdash; &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 850,000 CR.',
         '<strong>Mechanism:</strong> Multi-megawatt continuous-wave chemical oxygen-iodine laser channel with liquid-helium radiator loops.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 2 &bull; <strong>Damage:</strong> +4 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 4 salvos &bull; <strong>Cost:</strong> 950,000 CR.',
         '<strong>Mechanism:</strong> Hexagonal four-tube modular launch pod with pneumatic soft-ejection and programmable ripple-fire logic.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 3 &bull; <strong>Damage:</strong> +3 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 8 &bull; <strong>Cost:</strong> 1,100,000 CR.',
         '<strong>Mechanism:</strong> Heavy hardened tungsten-carbide core encased in thermal ablative shroud with solid-fuel pursuit motor.'),

        # Page 89
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/2 &bull; <strong>Macro Acc (10km):</strong> 2/1/&mdash;/&mdash;/&mdash; &bull; <strong>Special:</strong> Railgun &bull; <strong>Damage:</strong> +5',
         '<strong>Mechanism:</strong> Parallel copper-alloy magnetic rail guides launching hypervelocity tungsten sabots at 25 kilometers per second.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/1/3 &bull; <strong>Macro Acc:</strong> 1/&mdash;/&mdash;/&mdash;/&mdash; &bull; <strong>Damage:</strong> +8',
         '<strong>Mechanism:</strong> Overclocked industrial cutting beam focusing plasma-arc thermal energy through heavy sapphire magnetic collimators.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 1 &bull; <strong>Damage:</strong> +2 &bull; <strong>RoF:</strong> 4/turn &bull; <strong>Ammo:</strong> 2 salvos (8 missiles) &bull; <strong>Cost:</strong> 1,500,000 CR.',
         '<strong>Mechanism:</strong> Pneumatic rapid-fire launcher dispensing ripple-fire cluster micro-missiles with coordinated swarm algorithms.'),
        
        ('<strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> 0/1/1 &bull; <strong>Macro Acc:</strong> 3/2/1/&mdash;/&mdash; &bull; <strong>Special:</strong> Point-Defense (5)',
         '<strong>Mechanism:</strong> Quad-barrel 40mm rotary battery tied directly to ship mainframe fire-control buses and dedicated cooling shunts.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/0/2 &bull; <strong>Macro Acc:</strong> 3/2/1/0/&mdash; &bull; <strong>Damage:</strong> +4 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 2,200,000 CR.',
         '<strong>Mechanism:</strong> Electrostatic subatomic particle accelerator utilizing superconducting magnets to collimate relativistic ion streams.'),
        
        ('<strong>Size:</strong> Large &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 1 &bull; <strong>Damage:</strong> +12 &bull; <strong>RoF:</strong> 1/round &bull; <strong>Ammo:</strong> 2 &bull; <strong>Cost:</strong> 3,200,000 CR.',
         '<strong>Mechanism:</strong> Pressurized naval torpedo tube launching multi-megaton thermonuclear warheads with armored terminal penetration caps.'),
        
        ('<strong>Size:</strong> Large &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 0 &bull; <strong>Damage:</strong> +20 &bull; <strong>RoF:</strong> 1/round &bull; <strong>Ammo:</strong> 1 &bull; <strong>Cost:</strong> 3,800,000 CR.',
         '<strong>Mechanism:</strong> Heavy demolition missile carrying high-yield shaped fusion payload with autonomous terminal dogfight thrusters.'),
        
        ('<strong>Size:</strong> Medium &bull; <strong>Type:</strong> Guided &bull; <strong>Tracking:</strong> 5 &bull; <strong>Damage:</strong> +4 &bull; <strong>RoF:</strong> 1/turn &bull; <strong>Ammo:</strong> 2 &bull; <strong>Cost:</strong> 4,200,000 CR.',
         '<strong>Mechanism:</strong> Radar-absorbent ferrite composite airframe equipped with ultra-low-signature cold-gas vector thrusters.'),
        
        ('<strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/&mdash;/2 &bull; <strong>Macro Acc (10km):</strong> 3/2/1/0/&mdash; &bull; <strong>Special:</strong> Railgun &bull; <strong>Damage:</strong> +10',
         '<strong>Mechanism:</strong> Multi-stage electromagnetic induction coil assembly running the entire longitudinal structural keel of the vessel.'),
        
        ('<strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/0/1 &bull; <strong>Macro Acc:</strong> 3/2/1/0/&mdash; &bull; <strong>Damage:</strong> +6 &bull; <strong>RoF:</strong> Unlimited &bull; <strong>Ammo:</strong> Unlimited (Reactor) &bull; <strong>Cost:</strong> 5,000,000 CR.',
         '<strong>Mechanism:</strong> High-output continuous-wave chemical laser driven by triple-core ruby resonators and high-capacity radiator vanes.'),
        
        ('<strong>Size:</strong> Large &bull; <strong>Type:</strong> Unguided &bull; <strong>Dogfight Acc:</strong> &mdash;/&mdash;/1 &bull; <strong>Macro Acc (10km):</strong> 4/3/2/1/0 &bull; <strong>Special:</strong> Railgun &bull; <strong>Damage:</strong> +15',
         '<strong>Mechanism:</strong> Super-heavy naval railgun barrel with reinforced cryogenic field coils, firing multi-ton hypervelocity kinetic penetrators.')
    ]

    applied_count = 0
    for target_needle, mech_text in patches:
        if target_needle in code:
            insertion = f'<p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0.8mm; color: var(--text-body);">{mech_text}</p>\n            '
            code = code.replace(target_needle, insertion + target_needle, 1)
            applied_count += 1
        else:
            print(f"FAILED to find: {target_needle[:60]}...")

    print(f"Applied {applied_count}/{len(patches)} weapon mechanisms.")
    src_file.write_text(code, encoding="utf-8")

if __name__ == "__main__":
    patch_weapons()
