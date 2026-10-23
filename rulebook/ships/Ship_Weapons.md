# Starship Weapons & Hardpoints

Starship weapon systems consist of external structural mounting collars called **Hardpoints** and the specialized kinetic, thermal, or guided ordnance fitted into them. Unlike personal firearms, naval weapons operate under extreme environmental constraints: massive recoil forces that affect flight vectors, immense electrical capacitor drains, and the physics of firing unguided projectiles across thousands of kilometers of vacuum.

---

## Hardpoint Classifications

Hardpoints are structural hull zones wired directly into power conduits and fire-control buses. They come in three standardized sizes:

* **Small Hardpoints:** Agile, high-traverse gimbals designed for rapid-tracking rotary PDCs, light seeker drones, pulse lasers, and proximity mine dispensers.
* **Medium Hardpoints:** Heavy turret wells and reinforced bays accommodating naval laser arrays, multi-missile pods, heavy PDCs, flak cannons, particle beams, and twin-barrel railgun batteries.
* **Large Hardpoints:** Massive structural keels and spinal mounting frames reserved for ship-length coilguns, heavy siege railguns, and thermonuclear fusion torpedo tubes. Large spinal weapons typically require aligning the ship's entire chassis to aim.

---

## Guided vs. Unguided Ordnance

Naval weaponry falls into two distinct operational paradigms:

* **Unguided Weapons:** Kinetic slugthrowers, PDCs, railguns, and laser arrays. Fired manually by calculating target lead vectors with a Complex Test using **Finesse + Accuracy**. Unguided weapons can be fired at any target within range without electronic acquisition.
* **Guided Weapons:** Missiles, torpedoes, and hunter drones equipped with onboard rocket thrusters and seeker packages. Guided ordnance **strictly requires an active Target Lock** before launch. Guided attacks are resolved with a Complex Test using **Tracking + Tracking**. Each level of Target Lock held on the target provides **1 Upgrade** to the roll.

---

## Naval Ballistics & Operational Physics

### Orbital Ballistics & Light-Speed Latency
Across thousands of kilometers, targeting a maneuvering ship is constrained by sensory delay. Because ladar echoes travel at the speed of light, sensor returns from a vessel 3,000 km away depict where the target was ten milliseconds ago. For unguided kinetic rounds traveling at twenty kilometers per second, projectile transit time spans several seconds, allowing a watchful pilot to bleed vector momentum and slip outside the incoming trajectory cone.

### Point-Defense Interception Screens
Defending against guided missile swarms requires establishing overlapping interception cones. A single rotary PDC creates a localized flak curtain; when two or more PDCs link their radar trackers through the ship's fire-control bus, they create an interlocking kill zone, granting +1 Upgrade per additional operational turret.

### Missile Guidance Architecture & Counter-Measures
Guided ordnance in the Sphere relies on autonomous seeker brains combining infrared imaging, passive ladar receivers, and inertial guidance. When approaching an active point-defense grid, modern missiles execute pre-programmed erratic vector pulses, rolling and dodging along their flight path to spoil optical lead solutions calculated by hostile PDCs.

### Target Lock & EWAR Electronic Battles
Establishing a Target Lock represents flooding an enemy hull with ladar pulses, passive optical tracking, and thermal lock-on. Gunners acquire locks using a Systems Simple Test within Sensor Range. However, targets equipped with electronic counter-measure suites can deploy broad-spectrum noise and false radar echoes to shatter locks before ordnance can be launched.

### Recoil Dynamics & Munitions Safety
Naval kinetic weapons produce violent Newton reaction forces upon discharge. Automated avionics fire synchronized cold-gas counter-bursts to maintain gunnery alignment and prevent recoil tumble. Furthermore, high-explosive torpedo magazines are encased in armored containment coffins with directional blowout hatches, venting secondary cook-offs into outer vacuum rather than collapsing interior decks.

---

## Special Weapon Properties

* **Long-Range Ballistics (Railguns & Coilguns):** Projectiles exit electromagnetic barrels at hypersonic velocities (tens of kilometers per second). Accuracy dropoff on the Macro-Grid is measured in **10 km (10 hex) increments** rather than standard 1 km increments!
* **Point-Defense (Rating):** Rapid-traverse rotary cannons equipped with autonomous radar tracking. When intercepting incoming missiles, the gunner contests the attack using **Accuracy + Point-Defense Rating**. Multiple PDCs grant 1 Upgrade per additional cannon.

### Ammunition Logistics & Resupply

Refilling ordnance magazines requires authorized docking at any civilized port, orbital station, or naval tender. Standard resupply costs:
* **Small Weapons:** 2,000 Credits
* **Medium Weapons:** 4,000 Credits
* **Large Weapons:** 8,000 Credits

### Naval Combat Doctrines

* **The Kinetic Envelope:** Rotary PDCs and flak batteries form a ship's primary defensive umbrella. While individual tungsten flechettes deal modest hull damage, their high rate of fire allows gunners to fill closing engagement cones with dense screens of metal, shredding incoming missiles before impact.
* **Spinal Keel Alignment:** Large spinal railguns and coilguns represent terrifying kinetic force (+10 to +15 Damage Bonus). However, because they are mounted directly into the ship's longitudinal spine, the pilot must align the entire vessel's chassis along the target vector, restricting their fire to Advantage in dogfights.

---

## Master Starship Weapons Catalog

| Weapon Name | Size | Type | Acc (Dogfight)* | Acc (Macro)* | Trk | Dmg | RoF | Ammo | Special Properties | Cost (CR) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **GVI "Buzzer" Seeker Drone** | Small | Guided | — | — | 1 | +2 | 1 / turn | 6 | — | 200,000 |
| **PA "Sentinel" Rotary PDC** | Small | Unguided | 2 / 3 / 3 | 1 / 0 / — / — / — | — | +1 | Unlimited | Unlim | Point-Defense (5) | 250,000 |
| **GVI "Stinger" Light Missile** | Small | Guided | — | — | 2 | +3 | 1 / turn | 4 | — | 300,000 |
| **PA "Caltrop" Proximity Mine Dispenser** | Small | Unguided | 3 / — / — | — | — | +6 | 1 / turn | 4 | Rear Mine Dispenser | 350,000 |
| **CQV "Wasp" Pulse Laser** | Small | Unguided | — / 2 / 3 | 1 / — / — / — / — | — | +1 | Unlimited | Unlim | Reactor-Fed | 450,000 |
| **PA "Guardian" Heavy PDC** | Medium | Unguided | 1 / 2 / 2 | 2 / 1 / — / — / — | — | +2 | Unlimited | Unlim | Point-Defense (4) | 600,000 |
| **KSK "Harpoon" Kinetic Missile** | Small | Guided | — | — | 4 | +1 | 1 / turn | 6 | Kinetic Penetrator | 650,000 |
| **CF "Sledgehammer" Flak Cannon** | Medium | Unguided | — / 1 / 2 | 1 / — / — / — / — | — | +3 | 2 / turn | 12 | Point-Defense (3) | 750,000 |
| **CQV "Solarflare" Laser Array** | Medium | Unguided | — / 1 / 2 | 2 / 1 / 0 / — / — | — | +2 | Unlimited | Unlim | Chemical Thermal Laser | 850,000 |
| **GVI "Javelin" Guided Missile Pod** | Medium | Guided | — | — | 2 | +4 | 1 / turn | 4 | Quad Modular Salvo | 950,000 |
| **KSK "Lance" Kinetic Torpedo** | Medium | Guided | — | — | 3 | +3 | 1 / turn | 8 | Solid-Fuel Kinetic | 1,100,000 |
| **CF "Anvil" Railgun Battery** | Medium | Unguided | — / 1 / 2 | 2 / 1 / — / — / — | — | +5 | 2 / turn | 20 | Railgun (10km increments) | 1,200,000 |
| **GVI "Breacher" Thermal Lance** | Medium | Unguided | — / 1 / 3 | 1 / — / — / — / — | — | +8 | 1 / turn | Unlim | Plasma Cutting Lance | 1,350,000 |
| **GVI "Hydra" Multi-Missile Rack** | Medium | Guided | — | — | 1 | +2 | 4 / turn | 2 (8 msl) | Swarm Saturation | 1,500,000 |
| **CF "Bulwark" Point-Defense Battery** | Large | Unguided | 0 / 1 / 1 | 3 / 2 / 1 / — / — | — | +3 | Unlimited | Unlim | Point-Defense (5) | 1,800,000 |
| **CQV "Eclipse" Particle Beam** | Medium | Unguided | — / 0 / 2 | 3 / 2 / 1 / 0 / — | — | +4 | 1 / turn | Unlim | Relativistic Ion Stream | 2,200,000 |
| **KSK "Voidlance" Fusion Torpedo Tube** | Large | Guided | — | — | 1 | +12 | 1 / round | 2 | Thermonuclear Warhead | 3,200,000 |
| **GVI "Cataclysm" Siege Torpedo** | Large | Guided | — | — | 0 | +20 | 1 / round | 1 | Station Demolition | 3,800,000 |
| **KSK "Specter" Stealth Missile** | Medium | Guided | — | — | 5 | +4 | 1 / turn | 2 | Radar-Absorbent Stealth | 4,200,000 |
| **CF "Mjolnir" Spinal Coilgun** | Large | Unguided | — / — / 2 | 3 / 2 / 1 / 0 / — | — | +10 | 1 / turn | 6 | Spinal Mount, Railgun | 4,500,000 |
| **CQV "Prometheus" Heavy Laser Array** | Large | Unguided | — / 0 / 1 | 3 / 2 / 1 / 0 / — | — | +6 | Unlimited | Unlim | Continuous-Wave Beam | 5,000,000 |
| **CF "Gigant" Heavy Railgun** | Large | Unguided | — / — / 1 | 4 / 3 / 2 / 1 / 0 | — | +15 | 1 / turn | 4 | Heavy Spinal, Railgun | 6,500,000 |

*\* Acc (Dogfight) covers Disadvantage / Neutral / Advantage positions. Acc (Macro) covers 1 / 2 / 3 / 4 / 5+ km (Railguns and Spinal Coilguns measure Macro-Grid accuracy in 10 km increments due to Long-Range Ballistics).*

---

## Detailed Weapon Profiles

### 1. GVI "Buzzer" Seeker Drone
*A low-cost, expendable seeker equipped with cold-gas attitude thrusters and a shaped high-explosive warhead. Slow and easily outmaneuvered by seasoned pilots, but cheap enough for persistent swarming harassment.*
* **Mount / Mechanism:** Cold-gas attitude thrusters with micro-rocket sustainer and contact piezo-electric trigger fuze.
* **Size:** Small | **Type:** Guided | **Tracking:** 1 | **Damage Bonus:** +2 | **Rate of Fire:** 1 / turn | **Ammo:** 6 | **Cost:** 200,000 CR
* **Tactical Doctrine:** Deployed in multi-drone flights to saturate hostile point-defense grids, forcing opposing gunners to exhaust reaction APs before heavier torpedoes arrive.

### 2. PA "Sentinel" Rotary PDC
*The gold standard for close-in defense across the Sphere. Composed of a six-barreled rotary autocannon on a high-speed hydraulic gimbal, firing tungsten flechettes to paint an impenetrable wall of lead.*
* **Mount / Mechanism:** Six-barrel motorized Gatling gimbal with liquid-nitrogen jacket and high-rate linkless ammunition feed.
* **Size:** Small | **Type:** Unguided | **Dogfight Acc:** 2 / 3 / 3 | **Macro Acc:** 1 / 0 / — / — / — | **Special:** Point-Defense (5) | **Damage Bonus:** +1 | **Rate of Fire:** Unlimited | **Ammo:** Unlimited | **Cost:** 250,000 CR
* **Tactical Doctrine:** Essential survivability installation. Dedicated gunners hold reactions to shred inbound torpedoes within 500 meters of the hull.

### 3. GVI "Stinger" Light Missile
*A compact, high-velocity missile designed for light interceptors. It trades raw explosive mass for a sophisticated seeker matrix that makes it remarkably difficult to shake in close dogfights.*
* **Mount / Mechanism:** Solid-fuel booster core with gimbaled thrust-vector nozzle and dual optical/RF terminal sensor array.
* **Size:** Small | **Type:** Guided | **Tracking:** 2 | **Damage Bonus:** +3 | **Rate of Fire:** 1 / turn | **Ammo:** 4 | **Cost:** 300,000 CR
* **Tactical Doctrine:** Standard offensive strike armament for corsair corvettes; delivers dependable punch against unarmored utility craft.

### 4. PA "Caltrop" Proximity Mine Dispenser
*A rear-mounted pneumatic dispenser releasing shaped-charge proximity mines. Useless in an offensive chase, but devastating when a pursuer sits on your tail at Disadvantage.*
* **Mount / Mechanism:** Rear-venting pneumatic rotary rack launching magnetized shaped-charge canisters with command-destruct codes.
* **Size:** Small | **Type:** Unguided | **Dogfight Acc:** 3 / — / — | **Macro Acc:** — | **Damage Bonus:** +6 | **Rate of Fire:** 1 / turn | **Ammo:** 4 | **Cost:** 350,000 CR
* **Tactical Doctrine:** The ultimate defensive equalizer for slow freighters; turns an enemy's tail pursuit into catastrophic hull trauma.

### 5. CQV "Wasp" Pulse Laser
*A specialized dogfighting laser firing rapid ultraviolet pulses. Lacks cutting power against heavy armor, but high mirror slew speeds grant pinpoint accuracy against agile targets.*
* **Mount / Mechanism:** Rapid-pulsing diode-pumped solid-state laser cavity mounted on high-traverse piezoelectric mirror mounts.
* **Size:** Small | **Type:** Unguided | **Dogfight Acc:** — / 2 / 3 | **Macro Acc:** 1 / — / — / — / — | **Damage Bonus:** +1 | **Rate of Fire:** Unlimited | **Ammo:** Unlimited (Reactor) | **Cost:** 450,000 CR
* **Tactical Doctrine:** Infinite ammunition draws directly from reactor loops, making it an excellent suppression weapon during extended zero-resupply operations.

### 6. PA "Guardian" Heavy PDC
*A medium-caliber evolution of the Sentinel. Uses 30mm tungsten-jacketed rounds and heavy liquid-nitrogen cooling loops, extending defensive interception envelopes out to 2 km.*
* **Mount / Mechanism:** Motorized twin-barrel 30mm autocannon with integrated millimetric radar tracker and recoil-damping hydraulic dampers.
* **Size:** Medium | **Type:** Unguided | **Dogfight Acc:** 1 / 2 / 2 | **Macro Acc:** 2 / 1 / — / — / — | **Special:** Point-Defense (4) | **Damage Bonus:** +2 | **Rate of Fire:** Unlimited | **Ammo:** Unlimited | **Cost:** 600,000 CR
* **Tactical Doctrine:** Combines reliable point defense with genuine offensive bite against medium hulls at macro approach distances.

### 7. KSK "Harpoon" Kinetic Missile
*Fires an ultra-dense depleted uranium penetrator dart at extreme closing speeds. While it lacks explosive yield, its pinpoint tracking makes it a favorite for sniping engines.*
* **Mount / Mechanism:** High-density depleted uranium dart driven by two-stage solid rocket booster with inertial gyro autopilot.
* **Size:** Small | **Type:** Guided | **Tracking:** 4 | **Damage Bonus:** +1 | **Rate of Fire:** 1 / turn | **Ammo:** 6 | **Cost:** 650,000 CR
* **Tactical Doctrine:** Extraordinary base Tracking 4 ensures reliable hits even through heavy hostile EWAR jamming environments.

### 8. CF "Sledgehammer" Flak Cannon
*Fires heavy, proximity-fused explosive canisters that burst into razor-sharp titanium shrapnel clouds. Engineered to shred incoming missile clusters and strip sensor domes.*
* **Mount / Mechanism:** Heavy rifled naval cannon firing pre-fragmented titanium canister rounds with variable electronic time fuzes.
* **Size:** Medium | **Type:** Unguided | **Dogfight Acc:** — / 1 / 2 | **Macro Acc:** 1 / — / — / — / — | **Special:** Point-Defense (3) | **Damage Bonus:** +3 | **Rate of Fire:** 2 / turn | **Ammo:** 12 | **Cost:** 750,000 CR
* **Tactical Doctrine:** Excellent area denial; creates dense kinetic screens that degrade light interceptors attempting knife-fighting flybys.

### 9. CQV "Solarflare" Laser Array
*A continuous multi-megawatt chemical laser focusing thermal energy through synthetic sapphire optics. Delivers damage at the speed of light, melting structural ribs and vaporizing armor.*
* **Mount / Mechanism:** Multi-megawatt continuous-wave chemical oxygen-iodine laser channel with liquid-helium radiator loops.
* **Size:** Medium | **Type:** Unguided | **Dogfight Acc:** — / 1 / 2 | **Macro Acc:** 2 / 1 / 0 / — / — | **Damage Bonus:** +2 | **Rate of Fire:** Unlimited | **Ammo:** Unlimited (Reactor) | **Cost:** 850,000 CR
* **Tactical Doctrine:** Near-zero flight time makes it impossible for targets to evade at close range, stripping ablative plates with ruthless precision.

### 10. GVI "Javelin" Guided Missile Pod
*A modular quad-launcher packed with high-thrust tactical missiles. Upon Target Lock acquisition, the salvo launches in a coordinated fan, adjusting vector mid-flight to overwhelm point defense.*
* **Mount / Mechanism:** Hexagonal four-tube modular launch pod with pneumatic soft-ejection and programmable ripple-fire logic.
* **Size:** Medium | **Type:** Guided | **Tracking:** 2 | **Damage Bonus:** +4 | **Rate of Fire:** 1 / turn | **Ammo:** 4 salvos | **Cost:** 950,000 CR
* **Tactical Doctrine:** Heavy tactical warheads crack frigate-grade bulkheads once hostile point-defense turrets are distracted or suppressed.

### 11. KSK "Lance" Kinetic Torpedo
*A fin-stabilized kinetic torpedo driven by a solid-fuel booster core. Relies on immense closing momentum to smash deep into an adversary's internal machinery and shatter drive mounts.*
* **Mount / Mechanism:** Heavy hardened tungsten-carbide core encased in thermal ablative shroud with solid-fuel pursuit motor.
* **Size:** Medium | **Type:** Guided | **Tracking:** 3 | **Damage Bonus:** +3 | **Rate of Fire:** 1 / turn | **Ammo:** 8 | **Cost:** 1,100,000 CR
* **Tactical Doctrine:** Hardened seeker casing resists electronic countermeasures; devastating for crippling fleeing targets during high-G pursuit.

### 12. CF "Anvil" Railgun Battery
*Twin electromagnetic accelerators firing tungsten slugs at hyper-velocity. Bridges the gap between light PDCs and spinal mounts with reliable medium-range striking power without extreme alignment limits.*
* **Mount / Mechanism:** Parallel copper-alloy magnetic rail guides launching hypervelocity tungsten sabots at 25 kilometers per second.
* **Size:** Medium | **Type:** Unguided | **Dogfight Acc:** — / 1 / 2 | **Macro Acc (10km):** 2 / 1 / — / — / — | **Special:** Railgun | **Damage Bonus:** +5 | **Rate of Fire:** 2 / turn | **Ammo:** 20 | **Cost:** 1,200,000 CR
* **Tactical Doctrine:** Long-Range Ballistics allow effective fire out to 20 km; excellent for softening approaching combatants before dogfight transition.

### 13. GVI "Breacher" Thermal Lance
*An industrial salvage cutting laser retrofitted for close-quarters void brawls. Poor range, but its focused thermal output provides unmatched cutting power against heavy armor plating at point-blank range.*
* **Mount / Mechanism:** Overclocked industrial cutting beam focusing plasma-arc thermal energy through heavy sapphire magnetic collimators.
* **Size:** Medium | **Type:** Unguided | **Dogfight Acc:** — / 1 / 3 | **Macro Acc:** 1 / — / — / — / — | **Damage Bonus:** +8 | **Rate of Fire:** 1 / turn | **Ammo:** Unlimited | **Cost:** 1,350,000 CR
* **Tactical Doctrine:** Devastating finisher at Advantage (Positions 8–10); slices cleanly through armored bulkheads and disabled hulks alike.

### 14. GVI "Hydra" Multi-Missile Rack
*Sacrifices individual missile payload for sheer saturation volume. Fires four micro-missiles simultaneously, forcing target point-defense computers to spread intercept fire dangerously thin.*
* **Mount / Mechanism:** Pneumatic rapid-fire launcher dispensing ripple-fire cluster micro-missiles with coordinated swarm algorithms.
* **Size:** Medium | **Type:** Guided | **Tracking:** 1 | **Damage Bonus:** +2 | **Rate of Fire:** 4 / turn | **Ammo:** 2 salvos (8 missiles) | **Cost:** 1,500,000 CR
* **Tactical Doctrine:** Firing 4 missiles per turn overwhelms single-turret PDC grids through pure statistical target saturation.

### 15. CF "Bulwark" Point-Defense Battery
*A large-scale multi-barrel defensive installation for frigates and monitors. Backed by dedicated fire-control mainframes, it projects an impenetrable interception umbrella out to 3 km.*
* **Mount / Mechanism:** Quad-barrel 40mm rotary battery tied directly to ship mainframe fire-control buses and dedicated cooling shunts.
* **Size:** Large | **Type:** Unguided | **Dogfight Acc:** 0 / 1 / 1 | **Macro Acc:** 3 / 2 / 1 / — / — | **Special:** Point-Defense (5) | **Damage Bonus:** +3 | **Rate of Fire:** Unlimited | **Ammo:** Unlimited | **Cost:** 1,800,000 CR
* **Tactical Doctrine:** Fleet-level screen; shields adjacent friendly vessels from torpedo strikes across multi-kilometer macro engagements.

### 16. CQV "Eclipse" Particle Beam
*Accelerates ionized subatomic matter to relativistic velocities. Unlike lasers, the particle beam maintains focus at extreme ranges and delivers kinetic impact alongside thermal trauma.*
* **Mount / Mechanism:** Electrostatic subatomic particle accelerator utilizing superconducting magnets to collimate relativistic ion streams.
* **Size:** Medium | **Type:** Unguided | **Dogfight Acc:** — / 0 / 2 | **Macro Acc:** 3 / 2 / 1 / 0 / — | **Damage Bonus:** +4 | **Rate of Fire:** 1 / turn | **Ammo:** Unlimited (Reactor) | **Cost:** 2,200,000 CR
* **Tactical Doctrine:** Superb sniper weapon; strikes out to 4 km on the Macro-Grid with heavy accuracy and relentless armor erosion.

### 17. KSK "Voidlance" Fusion Torpedo Tube
*An instrument of absolute devastation. Launches an armored torpedo packing a multi-megaton thermonuclear payload. Slow and expensive, but a direct impact vaporizes heavy armor plating.*
* **Mount / Mechanism:** Pressurized naval torpedo tube launching multi-megaton thermonuclear warheads with armored terminal penetration caps.
* **Size:** Large | **Type:** Guided | **Tracking:** 1 | **Damage Bonus:** +12 | **Rate of Fire:** 1 / round | **Ammo:** 2 | **Cost:** 3,200,000 CR
* **Tactical Doctrine:** Capital ship executioner; a single penetrating strike tears through multiple hull condition tracks simultaneously.

### 18. GVI "Cataclysm" Siege Torpedo
*The heaviest guided ordnance in the Sphere. Less a torpedo and more a demolition charge with rocket thrusters. Sluggish guidance, but its immense yield is sufficient to crack orbital stations.*
* **Mount / Mechanism:** Heavy demolition missile carrying high-yield shaped fusion payload with autonomous terminal dogfight thrusters.
* **Size:** Large | **Type:** Guided | **Tracking:** 0 | **Damage Bonus:** +20 | **Rate of Fire:** 1 / round | **Ammo:** 1 | **Cost:** 3,800,000 CR
* **Tactical Doctrine:** Station siege and fortress cracking; requires prior EWAR suppression to ensure the sluggish torpedo reaches its target.

### 19. KSK "Specter" Stealth Missile
*A marvel of black-budget engineering. Built with radar-scattering composites and cold-gas attitude jets. Nearly invisible to standard sensor suites, making it the premier assassination weapon.*
* **Mount / Mechanism:** Radar-absorbent ferrite composite airframe equipped with ultra-low-signature cold-gas vector thrusters.
* **Size:** Medium | **Type:** Guided | **Tracking:** 5 | **Damage Bonus:** +4 | **Rate of Fire:** 1 / turn | **Ammo:** 2 | **Cost:** 4,200,000 CR
* **Tactical Doctrine:** Tracking 5 slices through defensive jammers; lethal against high-value targets before defensive alarms trigger.

### 20. CF "Mjolnir" Spinal Coilgun
*A massive mass accelerator built directly into a frigate's longitudinal keel. Accelerates a 100 kg depleted uranium slug to a fraction of light speed. Aiming requires pointing the entire ship.*
* **Mount / Mechanism:** Multi-stage electromagnetic induction coil assembly running the entire longitudinal structural keel of the vessel.
* **Size:** Large | **Type:** Unguided | **Dogfight Acc:** — / — / 2 | **Macro Acc (10km):** 3 / 2 / 1 / 0 / — | **Special:** Railgun | **Damage Bonus:** +10 | **Rate of Fire:** 1 / turn | **Ammo:** 6 | **Cost:** 4,500,000 CR
* **Tactical Doctrine:** Devastating spinal sniper; fires across 10–40 km corridors to shatter heavy keels before enemies can close.

### 21. CQV "Prometheus" Heavy Laser Array
*A turreted ultraviolet laser array with triple-core ruby resonators. Sips massive reactor power to ablate reinforced bulkheads at ranges where kinetic rounds drift off target.*
* **Mount / Mechanism:** High-output continuous-wave chemical laser driven by triple-core ruby resonators and high-capacity radiator vanes.
* **Size:** Large | **Type:** Unguided | **Dogfight Acc:** — / 0 / 1 | **Macro Acc:** 3 / 2 / 1 / 0 / — | **Damage Bonus:** +6 | **Rate of Fire:** Unlimited | **Ammo:** Unlimited (Reactor) | **Cost:** 5,000,000 CR
* **Tactical Doctrine:** Sustained light-speed thermal lance; turreted mount allows continuous fire across neutral and advantage vectors alike.

### 22. CF "Gigant" Heavy Railgun
*The pinnacle of conventional mass acceleration. Fires multi-ton slugs capable of snapping a cruiser's spine in a single volley. Immense recoil can knock smaller hulls off course.*
* **Mount / Mechanism:** Super-heavy naval railgun barrel with reinforced cryogenic field coils, firing multi-ton hypervelocity kinetic penetrators.
* **Size:** Large | **Type:** Unguided | **Dogfight Acc:** — / — / 1 | **Macro Acc (10km):** 4 / 3 / 2 / 1 / 0 | **Special:** Railgun | **Damage Bonus:** +15 | **Rate of Fire:** 1 / turn | **Ammo:** 4 | **Cost:** 6,500,000 CR
* **Tactical Doctrine:** Interplanetary artillery; extreme range out to 50 km (50 hexes) forces entire battlefleets into evasive dispersed formations.
