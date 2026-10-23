"""
Chapter 07 - Part 1: Welcome to the Sphere & The Corsairs (Pages 114 to 117)
Optimized for 78% to 88% fill across Spreads 58 and 59.
"""

def get_part1_html():
    return """
    <!-- =========================================================================
         PAGE 114 (Spread 58 Left) — CHAPTER 07 OPENER: WELCOME & LINEAGES
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="ch07-p114">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="p-banner-wrap p-banner-lore column-span-all" style="margin-bottom: 3mm;">
            <div class="p-banner-content">
                <h1 class="p-banner-title">Worlds of the Sphere</h1>
            </div>
        </div>

        <div class="page-body two-columns">
            <div class="card callout-quote" style="margin-bottom: 3mm;">
                <div class="card-header" style="font-family: var(--font-heading); font-size: 9.2pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1.2mm;">
                    The Setting at a Glance
                </div>
                <p style="font-size: 8.0pt; line-height: 1.34; margin: 0; color: var(--text-bright);">
                    <em>Corsair</em> is a tabletop roleplaying game of high-stakes frontier adventure, mystery, and intrigue, blending the mythic wonder of <strong>Space Fantasy</strong> with the grounded weight of <strong>Hard Science Fiction</strong>. Set within the <strong>Sphere</strong>&mdash;a breathtaking, macro-engineered solar system featuring more than a hundred habitable worlds locked in tight binary orbits around colossal gas giants&mdash;the setting pairs ancient cosmic dragons, forgotten alien vaults, and diverse lineages with the tangible reality of sub-light orbital mechanics and kinetic weaponry.
                </p>
                <p style="font-size: 8.0pt; line-height: 1.34; margin: 1.2mm 0 0 0; color: var(--text-dim);">
                    You and your crew play a <strong>Corsair Cell</strong>: licensed, independent operatives flying a nimble starship with a cross-jurisdictional charter. When planetary law ends at the clouds and the naval peacekeepers are light-minutes away, your sponsors call on you. Whether investigating corporate sabotage in an orbital arcology, braving hazardous Precursor ruins in search of lost technology, unmasking political conspiracies, or negotiating tense standoffs across a fraying frontier, your crew stands as the thin line holding a young civilization together.
                </p>
            </div>

            <p class="lead has-dropcap" style="margin-bottom: 2.2mm;">
                Five hundred years ago, automated seed arks brought the survivors of four dying worlds into the <strong>Sphere</strong>. Rather than a naturally accreted stellar system, the Sphere is a marvel of celestial engineering: concentric rings of massive gas giants locked in gravitational harmony around a quiet Orange Dwarf star.
            </p>

            <p>
                Within the magnetic shelters of these gas giants, terrestrial worlds orbit in close-knit binary pairs. Separated by mere tens of thousands of kilometers, neighboring moons hang like colossal jewels in each other's skies. Yet for all its mythic grandeur, everyday survival in the Sphere is governed by strict, tangible physical laws:
            </p>

            <ul class="bullet-list" style="margin-top: 1.2mm; margin-bottom: 2mm;">
                <li>
                    <strong>No Faster-Than-Light Travel:</strong> Interplanetary transit relies entirely on continuous-thrust fusion engines burning along calculated Brachistochrone trajectories. Hopping between twin binary moons takes mere hours, while journeys across the deep void between neighboring gas giants take only a few days.
                </li>
                <li>
                    <strong>No Artificial Gravity:</strong> Stations and ships obey Newtonian physics. Gravity exists only when an engine is under thrust or when an orbital station's habitat rings are spinning. Everywhere else, life is defined by magnetic boots, safety tethers, and the silent float of microgravity.
                </li>
                <li>
                    <strong>Kinetic and Thermal Realities:</strong> In place of energy shields or disintegrator beams, ships and ground operatives rely on layered composite armor, point-defense lasers, and ballistic firearms. Every burning engine and fired weapon generates waste heat that must be carefully radiated into the vacuum through glowing thermal arrays.
                </li>
                <li>
                    <strong>The Living Dragons:</strong> The titans of the void are not mere myths, but colossal, ancient biological entities that navigate the vacuum using internal bio-fusion dynamos. From gentle Goldheart watching over Landfall to the thunderous Stormdrinker circling the electrical storm-wells of Nimbus, dragons are sovereign beings whose presence and alliances shape the fate of entire worlds.
                </li>
            </ul>

            <h3 style="margin-top: 2mm;">Ten Lineages, Two Philosophies</h3>
            <p>
                Newcomer civilization is composed of ten distinct lineages, reimagining classic fantasy archetypes through an evolutionary and biological lens. All trace their ancestry back to the four original seed arks: the adaptable <strong>Humans</strong>, the crest-bearing and cold-blooded <strong>Naga</strong>, the dense-skinned and crystalline-eyed <strong>Craggen</strong>, and the tall, chlorophyllic <strong>Sylvan</strong>.
            </p>
            <p>
                Over five centuries of shared survival on Landfall and across the moons, six natural hybrid lineages took root: the draconic <strong>Drakelings</strong>, graceful <strong>Elves</strong>, ingenious <strong>Gnomes</strong>, stout and enduring <strong>Dwarves</strong>, nimble <strong>Kobolds</strong>, and towering <strong>Trolls</strong>. Yet, as the species intermingled, a profound philosophical rift divided Newcomer society:
            </p>
            <ul class="bullet-list" style="margin-top: 1.2mm;">
                <li>
                    <strong>Integrationism:</strong> The dominant cultural current, championed in metropolitan melting pots like Crossroads and Cloudspire. Integrationists believe that cultural blending, shared destiny, and inter-lineage solidarity represent the true future of the Sphere.
                </li>
                <li>
                    <strong>Preservationism:</strong> A traditionalist movement born from filial reverence for lost homeworlds. Preservationists maintain insular, single-lineage settlements on the outward frontiers, dedicated to keeping ancestral bloodlines, cultural rituals, and ancient languages pure to honor their forgotten ancestors.
                </li>
            </ul>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">114</span>
        </div>
    </div>

    <!-- =========================================================================
         PAGE 115 (Spread 58 Right) — LAW OF VOID, NEW WAVE & CORSAIR SPONSORS
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="ch07-p115">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <h3>The Law of the Void</h3>
            <p>
                Order across the populated moons is governed by the <strong>Skyline Accords</strong>, a historic treaty ratified in 335 AA that divided civilization into two distinct realms of legal authority:
            </p>
            <ol style="margin: 1.5mm 0 2mm 0; padding-left: 4.5mm; font-size: 8.2pt; line-height: 1.34; color: var(--text-dim);">
                <li style="margin-bottom: 1.2mm;">
                    <strong style="color: var(--text-bright);">The Sovereign Moons:</strong> Planetary governments hold total jurisdiction within their atmospheric gravity wells, enforcing their own local laws, taxation, and colonial charters.
                </li>
                <li>
                    <strong style="color: var(--text-bright);">The Flotilla:</strong> A massive, neutral peacekeeping fleet that holds supreme jurisdiction over open space, orbital transfer corridors, Lagrange stations, and void shipping lanes.
                </li>
            </ol>
            <p>
                While this separation prevented civil war, it created a dangerous legal seam. Smugglers, corporate raiders, rogue mercenaries, and political conspirators routinely commit crimes in planetary skies and burn into orbit, daring local authorities to chase them past their legal boundaries.
            </p>

            <div class="card" style="margin: 2mm 0; padding: 2.2mm 3mm; background: rgba(0, 20, 30, 0.45); border-left: 3px solid var(--amber-dark);">
                <div style="font-family: var(--font-heading); font-size: 8.6pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    The Skyline Seam: Why Dual Jurisdiction Exists
                </div>
                <p style="font-size: 7.9pt; line-height: 1.32; margin: 0; color: var(--text-dim);">
                    The division was not born of idealism, but exhaustion. Following the Drift Wars in the Fume rings, colonial leaders refused to surrender orbital sovereignty to the Flotilla, while the Admiralty refused to police squabbling planetary cities. The resulting boundary—the "Karman Verge"—became both a peace line and a haven for organized crime.
                </p>
            </div>

            <h3>The New Wave: Your Role as Corsairs</h3>
            <p>
                To bridge this jurisdictional void, the Flotilla and colonial administrations established the <strong>Corsairs</strong>&mdash;autonomous specialist crews granted cross-jurisdictional mandates to operate seamlessly from planetary mud to the cold vacuum of deep orbit.
            </p>
            <p>
                The year is <strong>518 AA</strong>. Exactly one decade ago, the apocalyptic Frontier War against the Orkish Empire and the catastrophic fall of the ancient alien super-dreadnought <em>Evergaol</em> shattered the Flotilla's veteran battle fleet. With naval hulls in short supply and the frontier fraying under piracy, corporate land-grabs, and border skirmishes, the High Council has issued emergency charters to recruit a <strong>New Wave of Corsairs</strong>.
            </p>

            <div class="card" style="margin: 2mm 0; padding: 2.2mm 3mm; background: rgba(0, 20, 30, 0.45); border-left: 3px solid var(--amber-dark);">
                <div style="font-family: var(--font-heading); font-size: 8.8pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    The Corsair Cell
                </div>
                <p style="font-size: 7.9pt; line-height: 1.32; margin: 0; color: var(--text-dim);">
                    As players, you form a <strong>Corsair Cell</strong>&mdash;a tight-knit crew of 3 to 5 specialists operating aboard an agile, multi-role starship. Every cell is unique: backed by multiple Sponsors (such as a naval officer, a governor, a corporation, or an independent union) to preserve operational neutrality. Supervised by an Oversight Committee of retired veteran Corsairs and civilian delegates, your cell enjoys total freedom of approach across the void.
                </p>
            </div>

            <h3 style="margin-top: 2mm;">The Corsairs of the Sphere</h3>
            <p>
                The Corsair system was established to manage jurisdictional friction between the <strong>Flotilla</strong> and the <strong>Sovereign Moons</strong>. It provides a mechanism for cross-jurisdictional operations in cases where local laws and orbital regulations overlap. Corsairs are operatives granted a cross-jurisdictional mandate to operate in both planetary and orbital environments.
            </p>

            <h4 style="color: var(--amber-dark);">Background and Origins</h4>
            <p>
                The Corsairs originated as a specialized division within the Patrol Wing following a landmark legal decision that established their jurisdiction to operate seamlessly across both orbital space and planetary surfaces. Initially, their mandate was focused on cross-jurisdictional investigations and bounty hunting. However, as the system proved its utility, both the Flotilla and the planetary colonies began offloading other critical duties. Today, Corsair cells are regularly tasked with localized law enforcement, reconnaissance, search and rescue, and recovery operations&mdash;missions ideally suited for a small, versatile crew.
            </p>

            <h4 style="color: var(--amber-dark);">The Sponsors</h4>
            <p>
                Behind every Corsair, there is a major power in the Sphere that sponsored their entry into the organization. The system could not exist without the sponsors who grant the means for it to operate, both in terms of granting them legal jurisdiction and in terms of funding their existence.
            </p>
            <p>
                Being a sponsor grants you the right to bring matters to the attention of the Corsair Cells. When you need a perceived injustice or a threat investigated or handled, you can directly petition the organization to act. In exchange, sponsors are required to fund the entry of at least one member into the Corsairs, the majority of which is for the ship they will be operating from. Sponsors handpick the individuals who become Corsair agents and provide their initial funding.
            </p>
            <p>
                Furthermore, sponsors gain a voice in the organization's governance. Representatives from each sponsor sit on the <strong>Sponsor Board</strong>, allowing them to vote on broader decisions that concern the organization's overall policies, budget, and leadership.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">115</span>
        </div>
    </div>

    <!-- =========================================================================
         PAGE 116 (Spread 59 Left) — OVERSIGHT, CELLS & RECRUITMENT PATHS
         ========================================================================= -->
    <div class="book-page spread-bg-1" id="ch07-p116">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <p>
                The biggest sponsors of the Corsairs are the Flotilla and the Colonies, but there are also a number of smaller organizations that have been granted sponsorship, such as corporations, NGOs, and even private individuals. To retain their voting seat on the Board, sponsors must maintain their funded assets in good standing and subject their petitions to the scrutiny of the central registry.
            </p>

            <h4 style="color: var(--amber-dark);">The Oversight Committee</h4>
            <p>
                To prevent sponsors from wielding the Corsairs as personal weapons or using them to advance partisan agendas, the organization is supervised by the <strong>Oversight Committee</strong>. This body is composed of former Corsair agents with exemplary service records, alongside civilian officials approved by the Sponsor Board. The Committee's role is twofold:
            </p>
            <ul class="bullet-list" style="margin-top: 1mm; margin-bottom: 2mm;">
                <li>
                    <strong>Contract Review:</strong> They evaluate all contracts submitted by sponsors to ensure they serve the public interest and the common good, filtering out requests that are purely self-serving or malicious.
                </li>
                <li>
                    <strong>Internal Investigations:</strong> They investigate allegations of misconduct or inappropriate behavior by active Corsair agents, holding the authority to hand down disciplinary actions or strip agents of their mandate if found guilty.
                </li>
                <li>
                    <strong>Audit of Arms &amp; Munitions:</strong> They maintain continuous remote monitoring of high-yield ordnance, boarding charges, and restricted telemetry arrays deployed to licensed hulls.
                </li>
            </ul>

            <div class="card" style="margin: 2mm 0; padding: 2.2mm 3mm; background: rgba(16, 24, 32, 0.6); border-left: 3px solid var(--amber-dark);">
                <div style="font-family: var(--font-heading); font-size: 8.6pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    The Charter Token &amp; Verification Protocol
                </div>
                <p style="font-size: 7.9pt; line-height: 1.32; margin: 0; color: var(--text-dim);">
                    Every licensed Corsair vessel carries a cryptographic <strong>Charter Token</strong> hardwired into its primary comms transponder. When challenged by local planetary militia or Flotilla patrol cruisers, broadcasting the token initiates an automated handshake with the nearest relay beacon, confirming the crew's legal clearance to transit airspace, carry combat armor, and execute warrants without interference.
                </p>
            </div>

            <h4 style="color: var(--amber-dark);">The Corsair Cell: The Fundamental Unit</h4>
            <p>
                The Corsair system is decentralized and operates through the <strong>Corsair Cell</strong>. Each cell is a small, autonomous group of <strong>3 to 5 specialists</strong> based on a single, high-performance vessel.
            </p>
            <p>
                This small-scale structure is a strategic choice: a single vessel can operate in crowded spaceports like Pelagia, dock at Nimbus refineries, or land at fringe outposts on Kazahn without the political implications of a military deployment. This versatility allows cells to handle investigations and tactical operations that would otherwise be complicated by interplanetary bureaucracy.
            </p>
            <p>
                To ensure neutrality, every cell is a mandatory collaboration between different <strong>Sponsors</strong>. Candidates are typically placed into cells with mixed sponsorships. This structure provides a self-policing environment; because members represent different interests, the cell is discouraged from serving any single power's exclusive agenda, enforcing their impartiality.
            </p>

            <h4 style="color: var(--amber-dark);">Cell Operational Roles</h4>
            <p>
                While every cell tailors its operational dynamic to its members' talents, most balanced crews organize into five key operational functions:
            </p>
            <ul class="bullet-list" style="margin-top: 1mm; margin-bottom: 2mm;">
                <li>
                    <strong>Commander / Negotiator:</strong> Manages legal warrants, charter compliance, sponsor negotiations, and diplomatic de-escalation under pressure.
                </li>
                <li>
                    <strong>Helm / Astrogator:</strong> Plots Brachistochrone burns, calculates orbital slingshots, manages propellant reserves, and maneuvers in tight dockings.
                </li>
                <li>
                    <strong>Tactical / Point Defense:</strong> Operates fire-control computers, manages kinetic coilguns, and coordinates intercept geometry against hostile bogeys.
                </li>
                <li>
                    <strong>Breaching Specialist:</strong> Wields MANTLE rigs in zero-g boarding actions, CQB clearing, structural cutting, and physical site security.
                </li>
                <li>
                    <strong>Systems Engineer / Tech:</strong> Calibrates drive plumes, maintains life support scrubbers, radiates reactor heat, and overrides security locks.
                </li>
            </ul>

            <h3>Recruitment and Selection</h3>
            <p>
                Becoming a Corsair agent is a prestigious but difficult path. There are two primary avenues for entering the organization:
            </p>

            <h4 style="color: var(--amber-dark);">The Institutional Path</h4>
            <p>
                Candidates can enlist directly with a major sponsor&mdash;such as the Flotilla or a colonial law enforcement agency&mdash;and work their way through the ranks. Outstanding performance, dedication, and recommendations from superiors within these organizations can eventually lead to a nomination for sponsorship as a Corsair agent.
            </p>

            <h4 style="color: var(--amber-dark);">The Freelance Path</h4>
            <p>
                Alternatively, individuals can build a reputation through bounty hunting, security consulting, or other freelance work across the Sphere. When a sponsor cannot find a suitable nominee within their own ranks, they often turn to established freelancers. To facilitate this, retired Corsairs run several smaller organizations and networks dedicated to mentoring promising freelancers; recommendations from these veterans carry significant weight with the Sponsor Board.
            </p>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">116</span>
        </div>
    </div>

    <!-- =========================================================================
         PAGE 117 (Spread 59 Right) — OPERATIONAL MODES, MANTLES & MATRIX
         ========================================================================= -->
    <div class="book-page spread-bg-2" id="ch07-p117">
        <div class="page-running-header">
            <span>Act IV: Lore of the Sphere</span>
            <span>Chapter 07: Worlds of the Sphere</span>
        </div>

        <div class="page-body two-columns" style="margin-top: 2mm;">
            <h3>Operational Variations</h3>
            <p>
                While the standard mandate establishes chartered cells sponsored by major powers and equipped with dedicated starships, two distinct operational variations operate across the Sphere:
            </p>

            <h4 style="color: var(--amber-dark);">Freelancer Crews (Aspirants)</h4>
            <p>
                Not all who seek to become Corsairs have secured a charter or a ship. Freelancer crews operate on the ground level, taking contract security, planetary tracking, and low-level salvage to prove their capabilities to watching sponsor scouts. Without a personal vessel, they rely on commercial transport, cargo shuttles, and station transit across the Sovereign Moons, striving to build the reputation needed to earn a sponsor's backing.
            </p>

            <h4 style="color: var(--amber-dark);">Rogue Corsairs (Outlaws)</h4>
            <p>
                At the opposite end of the spectrum are Rogue Corsairs&mdash;operatives who were stripped of their mandate by the Oversight Committee, broke strict neutrality protocols, or walked away from corrupt superiors. Operating unregistered, jury-rigged, or re-flagged starships, rogue cells take on high-risk, legally questionable contracts in the grey and black markets. Though officially hunted as outlaws, many maintain precarious backchannel contacts, mutual blackmail arrangements, or clandestine pipelines with their former sponsors.
            </p>

            <div class="card" style="margin-top: 2.5mm; padding: 2.5mm 3.2mm; background: rgba(16, 22, 30, 0.7); border-left: 3px solid var(--amber-dark);">
                <div style="font-family: var(--font-heading); font-size: 8.8pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    MANTLE Chassis &amp; The Freelancer Network
                </div>
                <p style="font-size: 7.9pt; line-height: 1.34; margin: 0; color: var(--text-dim);">
                    MANTLE rigs (<em>Modular Adaptive Neural Transmission Linked Equipment</em>) are classified as Tier-1 Restricted Military Hardware, legally manufactured and controlled by the Flotilla for specialist strike corps. While commissioned Corsairs receive officially sanctioned frames underwritten by their sponsors, Freelancers acquire their required starting MANTLE either through competitive <strong>Sponsor Candidate Pipelines</strong> (training programs pending formal charter confirmation) or via <strong>The Freelancer Network</strong>&mdash;an underground fraternity of retired Corsair veterans, mentors, and dockside armorers who distribute repaired, surplused, or salvaged frames to promising aspirants.
                </p>
            </div>

            <div class="card" style="margin-top: 2.2mm; padding: 2.2mm 3mm; background: rgba(22, 16, 16, 0.5); border-left: 3px solid var(--crimson-mid);">
                <div style="font-family: var(--font-heading); font-size: 8.6pt; font-weight: 700; color: var(--crimson-mid); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    The Black Market Economy &amp; Transponder Spoofing
                </div>
                <p style="font-size: 7.9pt; line-height: 1.32; margin: 0; color: var(--text-dim);">
                    Rogue crews survive by disabling their vessel's primary transponders, adopting forged ID beacons burned into civilian comm-chips by syndicate slicers. However, operating without a clean charter carries severe risks: unflagged vessels have zero legal protections in open space and may be targeted on sight by Flotilla patrol cutters or colonial defense craft without warning.
                </p>
            </div>

            <h4 style="color: var(--amber-dark); margin-top: 2.2mm;">The Candidate Pipeline &amp; Evaluation</h4>
            <p style="font-size: 8.0pt; line-height: 1.34; margin-bottom: 1.8mm;">
                Before any charter token is minted, prospective candidates undergo exhaustive evaluation. Flotilla intelligence and corporate sponsors run applicants through high-fidelity flight simulators, stress-tolerance tanks, and live-fire tactical drills. The attrition rate exceeds eighty percent; those who wash out either return to commercial transport ranks or drift toward the freelance underground, carrying half-completed training and bruised pride.
            </p>

            <h4 style="color: var(--amber-dark); margin-top: 1.8mm;">Sanctioned vs. Outlawed Ordnance</h4>
            <p style="font-size: 8.0pt; line-height: 1.34; margin-bottom: 1.8mm;">
                Under the Skyline Accords, chartered Corsair cells are authorized to carry military-grade railguns, point-defense lasers, and shaped-charge boarding torpedoes. However, strict naval conventions prohibit high-yield nuclear warheads, unguided kinetic swarms in commercial orbits, and biological agents. Possessing such outlawed ordnance triggers instant charter revocation and an unconditional Flotilla strike warrant.
            </p>

            <h4 style="color: var(--amber-dark); margin-top: 1.8mm;">The Contract Registry &amp; Escrow</h4>
            <p style="font-size: 8.0pt; line-height: 1.34; margin-bottom: 2mm;">
                All sanctioned Corsair contracts post their performance bonds into escrow accounts managed by the Flotilla Bank of Fume. Upon verifiable completion of operational objectives, funds are released directly to the cell's ship ledger, ensuring that crews operating across hostile borders never have to chase delinquent sponsors for promised payouts.
            </p>

            <div class="table-container keep-together" style="margin-top: 2.5mm;">
                <div class="table-header">Operational Modes Matrix</div>
                <table class="rules-table" style="font-size: 7.2pt; line-height: 1.22;">
                    <thead>
                        <tr>
                            <th>Mode</th>
                            <th>Legal Status</th>
                            <th>Vessel Access</th>
                            <th>MANTLE Source</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="bold">Freelancer (Aspirant)</td>
                            <td>Civilian Contractor</td>
                            <td>Commercial Transit</td>
                            <td>Surplus / Pipeline</td>
                        </tr>
                        <tr>
                            <td class="bold">Corsair (Chartered)</td>
                            <td>Cross-Jurisdictional</td>
                            <td>Dedicated Starship</td>
                            <td>Sponsor-Sanctioned</td>
                        </tr>
                        <tr>
                            <td class="bold">Rogue (Outlaw)</td>
                            <td>Hunted / Unlicensed</td>
                            <td>Unregistered Hull</td>
                            <td>Black Market / Retained</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="card callout-quote" style="margin-top: 2.5mm;">
                <div class="card-header" style="font-family: var(--font-heading); font-size: 8.8pt; font-weight: 700; color: var(--amber-dark); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1mm;">
                    The Charter's Weight
                </div>
                <p style="font-size: 7.9pt; line-height: 1.32; margin: 0; color: var(--text-bright);">
                    "A charter does not make you a hero; it makes you an accountant with a railgun. Every shell you fire, every airlock you breach, and every treaty you cite is logged in the Committee's ledgers. Walk straight, mind your vector, and never lie to your crew."
                </p>
            </div>
        </div>

        <div class="page-running-footer">
            <span>Volume I // Core Rulebook</span>
            <span class="page-num">117</span>
        </div>
    </div>
"""

