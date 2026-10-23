"""
Chapter 07 - Part 6: The Megacorporations & Industrial Cartels (Pages 138 to 141)
Spreads 70 and 71 — Exactly 4 pages, balanced for 71% to 78% fill with zero overflow.
Verbatim fidelity to rulebook/lore/factions/Corporations.md.
"""

def get_part6_html():
    return """
    <!-- =========================================================================
         PAGE 138 (Spread 70 Left) — MEGACORPORATIONS: TRADE ALLIANCE & CALDERA
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="ch07-p138">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <h2 style="font-size: 14pt; margin-bottom: 2mm;">The Megacorporations</h2>
            <div class="card" style="margin-bottom: 3mm; padding: 2mm 3mm; background: rgba(0, 20, 30, 0.45); border-left: 3px solid var(--amber-dark);">
                <div style="font-family: var(--font-mono); font-size: 7.2pt; line-height: 1.25; color: var(--text-dim);">
                    <strong>JURISDICTION:</strong> Industrial Enclaves, Corporate Leaseholds, Refinery Orbits<br>
                    <strong>AUTHORITY:</strong> Proprietary Patent Codes, Employment Scrip, Private Charters<br>
                    <strong>PRIMARY HOUSES:</strong> Trade Alliance, Caldera, Panthera, Vandal's, KSK, CQV, RF, SRC
                </div>
            </div>

            <p class="lead" style="font-size: 8.7pt; line-height: 1.36; margin-bottom: 2.5mm;">
                In a universe where every breath of pressurized air must be metered by an intake valve and every kilogram of structural titanium must be blasted out of an airless crater by heavy excavators, corporations are not merely commercial businesses. They are sovereign, feudal superpowers with balance sheets instead of heraldry and private security battalions instead of royal guards.
            </p>
            <p>
                Planetary governments may hold the soil under the Skyline Accords, and the Flotilla may rule the void, but the corporations own the plumbing that connects them. They own the atmospheric scrubbers that prevent city spires from suffocating; they hold the patents on the Draco fusion drive coils that keep freighters burning between worlds; and in many mining basins, they print the only currency the commissary will accept.
            </p>

            <h3>1. The Trade Alliance</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                The <strong>Trade Alliance</strong> is the oldest and most politically entrenched commercial coalition in Newcomer civilization. Founded in 180 AA during the catastrophic Inter-Binary Famine&mdash;when the destruction of the Pelagia-Suncatcher water railguns threatened to starve the young colonies&mdash;the Alliance was formed by a desperate syndicate of independent freighter captains, warehouse syndicates, and bulk grain brokers who pooled their ships to run emergency relief convoys across the void.
            </p>
            <p>
                That humanitarian origin story has long since calcified into an all-encompassing, bureaucratic freight cartel. Their philosophy is unyielding: <em>Civilization is a supply chain, and anyone who disrupts the schedule is an enemy of progress.</em> They view planetary borders as irritating friction, naval blockades as supply-chain inefficiencies, and custom duties as an unprovoked assault on the natural right of cargo to move from point A to point B without someone opening the crate.
            </p>

            <h4 style="color: var(--amber-dark);">Leadership, Assets &amp; Relationship with Corsairs</h4>
            <p>
                The Alliance is governed by the <strong>Board of Syndics</strong> aboard the massive distribution hub <em>Cross-Drift Station</em> at Fume L1. While maintaining the armed <strong>Maritime Logistics Escort Division</strong>, their greatest weapon is the <strong>Central Clearing Ledger</strong>: if a planetary council pushes the Alliance too far, the Board declares the port an "Uninsured Vector," tripling shipping insurance premiums until the local economy grinds to a halt.
            </p>
            <p>
                The Alliance is the largest commercial underwriter of Corsair cells, issuing <strong>Commercial Protection Warrants</strong> to hunt down pirates, recover impounded grain shipments, and secure orbital depots, paying promptly in universal credits.
            </p>

            <h3>2. Caldera Foundry (CF)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                If the Sphere has a spine, <strong>Caldera Foundry</strong> forged it from hot iron, rolled titanium, and stubborn human sweat. Based in the volcanic craters of Suncatcher and maintaining heavy foundries in Landfall's industrial perimeter, Caldera manufactures the colossal bucket-wheel excavators that chew through planetary crusts, structural girders for arcologies, heavy armor plate for Flotilla cruisers, and devastating kinetic artillery.
            </p>
            <p>
                Their culture is unapologetically industrial and insular. Caldera communities in Dustwall are closed-loop company ecosystems paying miners in brass <strong>Caldera Scrip</strong>. Employees rally around the legendary <strong>Caldera Foundry baseball team</strong>, whose dust-swept matches against prospector clubs are frontier legends. Steered by the <strong>Board of Iron Masters</strong> under Managing Director <strong>Torin Calder</strong>, security is enforced by the cyber-augmented <strong>Foundry Iron Guard</strong> with pneumatic trench weapons.
            </p>
            <p>
                Signature assets include the <strong>"Anvil" Railgun Battery</strong>, the monstrous <strong>"Mjolnir" Spinal Coilgun</strong>, the heavy <strong>"Sledgehammer" Flak Cannon</strong>, and the rugged <strong>CF "Cinder" Strike Frigate</strong>. Caldera hires Corsairs to hunt Badland claim-jumpers and recover hijacked ore crawlers, paying in refined alloy ingots and proprietary starship heat sinks.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">138</span>
        </div>
    </div>

    <!-- =========================================================================
         PAGE 139 (Spread 70 Right) — DOSSIER 2: PANTHERA ARMS & VANDAL'S WORKSHOP
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="ch07-p139">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <h3>3. Panthera Aerospace &amp; Arms (PA)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                Where Caldera Foundry represents raw industrial mass, <strong>Panthera Aerospace &amp; Arms</strong> represents cold, lethal precision. Stamped with the distinctive silhouette of a snarling predatory cat, Panthera hardware is the undisputed gold standard for high-spec military operations, corporate private security, and wealthy Corsair cells.
            </p>
            <p>
                Based out of high-altitude aerospace complexes on Nimbus and maintaining gleaming orbital skunkworks, Panthera operates on an ethos of uncompromising engineering tolerance. They believe that a weapon or an aerospace hull should not merely be functional; it should be a marvel of ergonomic balance, acoustic dampening, and lethal efficiency. Panthera’s corporate atmosphere is sleek, sterile, and aggressively competitive. Executive suites are decorated in minimalist frosted glass and dark titanium; research teams are subjected to relentless peer performance reviews; and field agents dress in tailored, low-profile tactical suits that look equally appropriate in an executive boardroom or a zero-gravity boarding corridor.
            </p>

            <h4 style="color: var(--amber-dark);">Leadership, Paramilitary &amp; Assets</h4>
            <p>
                Panthera is governed by the <strong>Executive Directorate of Defense</strong>, presided over by Chief Executive <strong>Corinne Vance</strong>, a brilliant, ruthless former aerospace engineer whose family has held senior seats since the Scavenger Wars. Vance runs the company with military discipline, enforcing strict operational compartmentation across all research divisions.
            </p>
            <p>
                The company's private enforcement arm&mdash;<strong>Panthera Tactical Solutions (PTS)</strong>&mdash;is one of the most capable corporate paramilitary forces in the Sphere. Equipped with proprietary stealth interceptors, smart-linked composite armor, and high-velocity marksman rifles, PTS teams protect corporate VIPs, guard high-security research vaults, and conduct deniable "competitive asset acquisitions" against rival firms.
            </p>
            <p>
                Signature naval armaments include close-in point defenses: the ubiquitous <strong>"Sentinel" Rotary PDC</strong>, the heavy <strong>"Guardian" PDC</strong>, and the <strong>"Caltrop" Proximity Mine Dispenser</strong>, alongside precision rifles and the orbital <strong>PA Apex Skunkworks</strong>. Panthera frequently issues <strong>Field Evaluation Contracts</strong>, offering prototype rifles and experimental PDC fire-control software in exchange for real-world combat telemetry.
            </p>

            <h3>4. Vandal's Workshop (VW)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                If you ask an engineer from Panthera Arms how a firearm functions, they will give you a ninety-minute lecture on gas piston tolerances, ceramic barrel coatings, and micro-harmonic recoil vectors. If you ask an armorer from <strong>Vandal's Workshop</strong>, they will hand you a five-kilo stamped-sheet assault carbine, rack the bolt with a sound like a closing vault door, and tell you: <em>"Drop it in a mud swamp, bake it in a silica storm, drag it through hard vacuum, and pull the trigger. It goes bang. If it doesn't, hit it with a rock. Now pay me."</em>
            </p>
            <p>
                Born in the rough-and-tumble industrial outskirts of Landfall during the early expansion era, Vandal’s Workshop was founded by a cantankerous Craggen-Human mechanic collective who believed that frontier equipment had become too fragile, too expensive, and far too obsessed with polite aesthetics. Vandal’s Workshop prides itself on utter utilitarian ruggedness. Their weapons are built with thick stamped steel, oversized charging handles, and generous internal clearances that refuse to jam even when packed with abrasive red dust. In the brutal frontiers of Suncatcher, the soggy trenches of Kazahn, or the freezing ice shelves of Rime, spacers trust Vandal because Vandal gear simply refuses to die.
            </p>

            <h4 style="color: var(--amber-dark);">Guild Governance, Hardware &amp; Corsair Support</h4>
            <p>
                Vandal’s Workshop has no corporate board or glossy marketing department. The company is operated as an anarchic, highly efficient <strong>Artisans' Guild</strong>, presided over by the rotating Lead Foreman&mdash;currently <strong>Marta "Hammer-Hand" Kovic</strong>, a scarred Naga welder with forty years in industrial fabrication. Guild resolutions are decided over grease-stained workbenches in Foundry Row: if an apprentice designs a new part, the elders throw it off the roof, hit it with a sledgehammer, and soak it in hydraulic acid; if it survives, it enters production.
            </p>
            <p>
                Signature hardware includes stamped-sheet kinetic carbines, heavy submachine guns, zero-g pump shotguns, industrial hazard battleplate, universal field modification kits, and the sprawling <strong>Scrap-Works Garage</strong> on Landfall. Vandal is beloved by young Corsair crews for cheap, durable gear and lifetime repair warranties honored at any authorized greasy workbench across the Sphere.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">139</span>
        </div>
    </div>

    <!-- =========================================================================
         PAGE 140 (Spread 71 Left) — DOSSIER 2: KER'SATZ, CHIDORI-QWEI & REDFEATHER
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="ch07-p140">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <h3>5. Ker'Satz Korp (KSK)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                <strong>Ker'Satz Korp</strong> is the heavy life-support and long-range ordnance juggernaut of the Sphere. If you are breathing pressurized air on an orbital station, drinking recycled moisture in a mining outpost, or locking an airlock seal before atmospheric reentry, the tiny brass pressure regulator keeping you alive has the stylized hexagonal "K" of Ker'Satz stamped into its casing.
            </p>
            <p>
                Founded by Naga geothermal engineers and Human aerospace industrialists, KSK views civilization through the lens of thermodynamic survival: space is an active enemy that wants to suck your moisture, freeze your blood, and crush your chest; survival requires uncompromising structural integrity. Hardware is massive and over-engineered, designed for catastrophic structural punishment across interplanetary distances. Headquartered at <em>Station Hexagon</em> orbiting Fume under High Director <strong>Sseth Ker'Satz</strong>, security is maintained by the heavy-carapace <strong>Hexagon Vanguard</strong>.
            </p>
            <p>
                Signature assets include the <strong>"Harpoon" Kinetic Missile</strong>, the <strong>"Lance" Torpedo</strong>, the <strong>"Voidlance" Fusion Torpedo</strong>, radar-absorbent <strong>"Specter" Stealth Missile</strong>, the <strong>KSK "Dagger" Interdictor</strong>, and gargantuan <strong>KSK "Leviathan" Dreadnought</strong>, alongside life-support regulators and ballistic breach chassis. KSK issues <strong>Critical Asset Defense Contracts</strong>, rewarding Corsairs with mil-spec torpedo munitions and high-pressure environmental gear, demanding strict telemetry logs and zero warranty bypasses.
            </p>

            <h3>6. Chidori-Qwei Voidworks &amp; Combatwear (CQV)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                Perched in the gleaming spires of Cloudspire on Nimbus, <strong>Chidori-Qwei</strong> is where high fashion, bleeding-edge directed-energy physics, and tactical survivability collide. CQV caters to the high-society elite, executive protection details, and top-tier Corsair marshals who believe there is no reason to look like a grease-stained mechanic during a lethal firefight.
            </p>
            <p>
                Their <strong>Combatwear</strong> line features tailored trench coats, flightsuits, and evening jackets woven from ballistic smart-fibers that remain flexible in conversation but instantly stiffen into rigid kinetic-dispersing armor when struck by high-velocity rounds. Their <strong>Voidworks</strong> division specializes in directed-energy naval armaments: the <strong>"Wasp" Pulse Laser</strong>, <strong>"Solarflare" Laser Array</strong>, <strong>"Eclipse" Particle Beam</strong>, and massive <strong>"Prometheus" Heavy Laser</strong>, alongside the radar-absorbent <strong>CQV "Shinobi" Stealth Recon</strong> corvette and smart-linked machine pistols.
            </p>
            <p>
                Presided over by <strong>Lady Evelyn Qwei</strong> and guarded by the elite <strong>Silk Guard</strong>, CQV offers <strong>Brand Ambassador Sponsorships</strong> and discreet espionage contracts to stylish Corsair cells&mdash;recovering stolen fashion sketches, extracting compromised corporate fixers, or neutralizing rival blackmail rings.
            </p>

            <h3>7. Redfeather Aerospace (RF)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Corporate Ethos</h4>
            <p>
                If you ask any working-class spacer in the Sphere to draw a starship, they will sketch the clean, angular lines of a <strong>Redfeather Aerospace</strong> hull. Based on Landfall, Redfeather is the shipyard of the common people, building the honest, reliable, multi-role workhorses that carry the life of the system.
            </p>
            <p>
                Redfeather's design philosophy is mass production, modularity, and accessibility. Hulls feature standardized bulkhead dimensions, accessible conduit chases, and universal engine mounts accepting virtually any fusion drive. If a component breaks, spacers do not need advanced degrees; they buy a replacement gasket at any dusty port, bolt it into place with an adjustable wrench, and burn before the coffee cools. For generations of spacers, a second-hand Redfeather hull is freedom itself.
            </p>
            <p>
                Governed by the <strong>Board of Master Shipwrights</strong> under Chairman <strong>Arthur "Wings" Henderson</strong>, Redfeather maintains a close, ethical relationship with its unionized workforce and the High Council. Signature hulls include the <strong>RF "Kestrel" Multi-Role Corvette</strong> (the quintessential Corsair starter ship), <strong>RF "Talon" Light Interceptor</strong>, <strong>RF "Falcon" System Patrol Boat</strong>, and the massive <strong>Western Slipways</strong>. Redfeather actively subsidizes down-payments for promising young crews and issues escort and test-flight recovery warrants.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">140</span>
        </div>
    </div>

    <!-- =========================================================================
         PAGE 141 (Spread 71 Right) — DOSSIER 2: SRC & CORPORATE MATRIX
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="ch07-p141">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <h3>8. The Sphere Research Center (SRC)</h3>

            <h4 style="color: var(--amber-dark);">Commercial Profile &amp; Scientific Legacy</h4>
            <p>
                While technically an academic and scientific consortium rather than a profit-maximizing commercial corporation, the <strong>Sphere Research Center (SRC)</strong> wields industrial and geopolitical influence that eclipses most megacorporations. Headquartered in the sprawling ivory towers of Crossroads on Landfall and maintaining high-altitude lightning observatories in Cloudspire on Nimbus, the SRC is the paramount intellectual institution of Newcomer civilization.
            </p>
            <p>
                In 38 AA, working in direct consultation with <strong>Stormdrinker</strong>, SRC physicists unraveled the bio-fusion principles that led to the invention of the <strong>Draco Fusion Drive</strong>&mdash;the single breakthrough that made sub-light interplanetary spaceflight possible. Today, governed by the <strong>Council of Curators</strong> under <strong>Arch-Curator Varisia Lin</strong>, the SRC catalogs Precursor Vault ruins while enforcing strict containment protocols alongside Stormdrinker and Goldheart to prevent dormant defense networks from waking. Security is enforced by the elite <strong>Archive Wardens</strong>. The SRC issues <strong>Academic Recovery Petitions</strong> to Corsairs to explore newly discovered ruins and recover stolen data drives.
            </p>

            <div class="table-container keep-together column-span-all" style="margin-top: 3.5mm; margin-bottom: 3.5mm;">
                <div class="table-header">The Eight Megacorporations &amp; Industrial Cartels Matrix</div>
                <table class="rules-table" style="font-size: 7.0pt; line-height: 1.22;">
                    <thead>
                        <tr>
                            <th>Corporation</th>
                            <th>Primary Seat</th>
                            <th>Industrial Specialization</th>
                            <th>Flagship Hardware / Assets</th>
                            <th>Security Arm</th>
                            <th>Corsair Warrant Profile</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Trade Alliance</td>
                            <td>Fume L1 (Cross-Drift)</td>
                            <td>System-Wide Freight, Logistics, Banking</td>
                            <td>Cross-Drift Central, Clearing Ledger</td>
                            <td>Maritime Logistics Escort</td>
                            <td>Commercial Protection Warrants</td>
                        </tr>
                        <tr>
                            <td class="bold">Caldera Foundry</td>
                            <td>Dustwall (Suncatcher)</td>
                            <td>Heavy Mining, Smelting, Kinetic Ordnance</td>
                            <td>Anvil Railgun, Mjolnir Spinal Coilgun</td>
                            <td>Foundry Iron Guard</td>
                            <td>Badland Claim Defense &amp; Recovery</td>
                        </tr>
                        <tr>
                            <td class="bold">Panthera Arms</td>
                            <td>Cloudspire (Nimbus)</td>
                            <td>High-Spec Aerospace, PDCs, Precision Guns</td>
                            <td>Sentinel Rotary PDC, Guardian PDC</td>
                            <td>Panthera Tactical Solutions</td>
                            <td>Field Evaluation &amp; Prototype Trials</td>
                        </tr>
                        <tr>
                            <td class="bold">Vandal's Workshop</td>
                            <td>Foundry Row (Landfall)</td>
                            <td>Rugged Utilitarian Arms, Hazard Armor</td>
                            <td>Stamped Carbines, Scrap Carapace</td>
                            <td>Workshop Foremen Collective</td>
                            <td>Scrap Recovery &amp; Barricade Breaching</td>
                        </tr>
                        <tr>
                            <td class="bold">Ker'Satz Korp</td>
                            <td>Station Hexagon (Fume)</td>
                            <td>Life-Support Systems, Capital Torpedoes</td>
                            <td>Harpoon Missile, Voidlance Torpedo</td>
                            <td>Hexagon Vanguard</td>
                            <td>Critical Asset Defense Contracts</td>
                        </tr>
                        <tr>
                            <td class="bold">Chidori-Qwei</td>
                            <td>Cloudspire Upper Spire</td>
                            <td>Combatwear Smart-Fibers, Pulse Lasers</td>
                            <td>Prometheus Laser, Shinobi Stealth Recon</td>
                            <td>The Silk Guard</td>
                            <td>Brand Ambassador Sponsorships</td>
                        </tr>
                        <tr>
                            <td class="bold">Redfeather Aero</td>
                            <td>Western Slips (Landfall)</td>
                            <td>Modular Starship Construction &amp; Drydocks</td>
                            <td>RF "Kestrel" Corvette, Talon Interceptor</td>
                            <td>Yard Constabulary</td>
                            <td>Freelancer Subsidies &amp; Escorts</td>
                        </tr>
                        <tr>
                            <td class="bold">Sphere Research Ctr</td>
                            <td>Crossroads Institute</td>
                            <td>Precursor Science, Fusion Telemetry, Vaults</td>
                            <td>Draco Patent Trust, Storm Observatories</td>
                            <td>The Archive Wardens</td>
                            <td>Academic Recovery Petitions</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="card" style="padding: 2.2mm 3mm; background: rgba(16, 22, 30, 0.7); border-left: 3px solid var(--amber-dark);">
                <div style="font-family: var(--font-heading); font-size: 8.5pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    The Economic Engine of the Sphere
                </div>
                <p style="font-size: 7.7pt; line-height: 1.30; margin: 0; color: var(--text-dim);">
                    While governments debate in Crossroads and admirals review readiness in Redmane Station, the daily survival of the Sphere depends upon the fragile equilibrium of these eight corporate houses. A strike at Caldera's smelting foundries delays Redfeather's slipways; an unannounced tariff by the Trade Alliance strands grain on Landfall; and an aggressive hostile takeover by Panthera can trigger covert proxy wars in Cloudspire's ravines. Navigating these corporate rivalries is the ultimate test of a Corsair cell's tactical acumen.
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">141</span>
        </div>
    </div>
"""
