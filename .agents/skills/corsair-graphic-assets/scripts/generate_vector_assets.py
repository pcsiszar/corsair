#!/usr/bin/env python3
"""
Corsair Vector Icon & Banner Generator.
Generates all vector assets referenced in Asset_Gallery.html:
1. Mechanical In-line Icons (viewBox="0 0 32 32"):
   - hit.svg
   - crit.svg
   - upgrade.svg
   - downgrade.svg
   - gambit.svg
   - ap.svg
   - blocker.svg
   - chain.svg
   - push.svg
   - contest.svg

2. Vector Parallelogram Banners (viewBox="0 0 1200 160"):
   - banner_parallelogram_flotilla.svg
   - banner_parallelogram_tactical.svg
   - banner_parallelogram_hazard.svg
"""

import os

ASSETS_DIR = r"c:\Users\csisz\IdeaProjects\corsair\assets"
MECH_DIR = os.path.join(ASSETS_DIR, "images", "icons", "mechanical")
BANNER_DIR = os.path.join(ASSETS_DIR, "images", "banners")

os.makedirs(MECH_DIR, exist_ok=True)
os.makedirs(BANNER_DIR, exist_ok=True)

# ==============================================================================
# 1. MECHANICAL IN-LINE ICONS (32x32)
# ==============================================================================

# Hit Icon: Diamond reticle with 8+ threshold crosshair (Amber, no white hole)
HIT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- Diamond Target Reticle -->
  <polygon points="16,3 29,16 16,29 3,16" fill="#d97706" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2.2" stroke-linejoin="round"/>
  <circle cx="16" cy="16" r="6" stroke="#f59e0b" stroke-width="2"/>
  <line x1="16" y1="4" x2="16" y2="9" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
  <line x1="16" y1="23" x2="16" y2="28" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
  <line x1="4" y1="16" x2="9" y2="16" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
  <line x1="23" y1="16" x2="28" y2="16" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
</svg>'''

# Crit Icon: 5-Pointed Star in Amber matching Hit (+2 SP, no white hole)
CRIT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- 5-Pointed Tactical Star (Critical Effect) in Amber matching Hit -->
  <polygon points="16,2.2 19.5,11.5 29,11.5 21.5,17.5 24.5,27 16,21.5 7.5,27 10.5,17.5 3,11.5 12.5,11.5" fill="#d97706" fill-opacity="0.25" stroke="#f59e0b" stroke-width="2.2" stroke-linejoin="round"/>
  <!-- Internal Facet Ridges -->
  <line x1="16" y1="16" x2="16" y2="2.2" stroke="#fbbf24" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="16" y1="16" x2="29" y2="11.5" stroke="#fbbf24" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="16" y1="16" x2="24.5" y2="27" stroke="#fbbf24" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="16" y1="16" x2="7.5" y2="27" stroke="#fbbf24" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="16" y1="16" x2="3" y2="11.5" stroke="#fbbf24" stroke-width="1.2" stroke-linecap="round"/>
</svg>'''

# Upgrade Icon: Double upward tactical step chevron (d10 -> d12, no end diamond)
UPGRADE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- Upward Double Step Chevrons (d10 -> d12) -->
  <path d="M6 22 L16 12 L26 22" stroke="#16a34a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M6 14 L16 4 L26 14" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Downgrade Icon: Double downward tactical step chevron (d10 -> d8, no end diamond)
DOWNGRADE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- Downward Double Step Chevrons (d10 -> d8) -->
  <path d="M6 10 L16 20 L26 10" stroke="#991b1b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M6 18 L16 28 L26 18" stroke="#dc2626" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Gambit Icon: Classic d10 die projection in Amber (pushing luck, no white hole)
GAMBIT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- d10 Die Silhouette (Ten-Sided Die) in Amber -->
  <polygon points="16,2 28.5,15 16,30 3.5,15" fill="#d97706" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2.2" stroke-linejoin="round"/>
  <!-- Front Prominent Kite Face -->
  <polygon points="16,2 22.5,14 16,18 9.5,14" fill="#f59e0b" fill-opacity="0.3" stroke="#fbbf24" stroke-width="1.8" stroke-linejoin="round"/>
  <!-- Lower Central Ridge -->
  <line x1="16" y1="18" x2="16" y2="30" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round"/>
  <!-- Lateral Facet Ridges -->
  <line x1="9.5" y1="14" x2="3.5" y2="15" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="22.5" y1="14" x2="28.5" y2="15" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round"/>
</svg>'''

# Action Points (AP): Hexagonal kinetic power cell (no white hole)
AP_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- Hexagonal Power Cell -->
  <polygon points="16,3 28,9.5 28,22.5 16,29 4,22.5 4,9.5" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2.2" stroke-linejoin="round"/>
  <polygon points="16,8.5 23,12.5 23,19.5 16,23.5 9,19.5 9,12.5" fill="#0284c7" stroke="#7dd3fc" stroke-width="1.6" stroke-linejoin="round"/>
</svg>'''

# Blocker Effect: Tactical interdict / lockout octagon (no white hole)
BLOCKER_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <!-- Interdict / Lockout Octagon -->
  <polygon points="10,3 22,3 29,10 29,22 22,29 10,29 3,22 3,10" fill="#dc2626" fill-opacity="0.2" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="8" y1="8" x2="24" y2="24" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>
</svg>'''

# Chain Effect: Branching tactical telemetry links
CHAIN_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <circle cx="8" cy="16" r="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="24" cy="8" r="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="24" cy="24" r="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <path d="M12 16 L20 8" stroke="#7dd3fc" stroke-width="2" stroke-linecap="round"/>
  <path d="M12 16 L20 24" stroke="#7dd3fc" stroke-width="2" stroke-linecap="round"/>
</svg>'''

# Push Effect: High-velocity displacement vector
PUSH_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <path d="M4 16 H23 M16 9 L23 16 L16 23" stroke="#f59e0b" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="28" y1="7" x2="28" y2="25" stroke="#f59e0b" stroke-width="2.8" stroke-linecap="round"/>
</svg>'''

# Contest Effect: Opposing kinetic impact vectors
CONTEST_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100%" height="100%" fill="none">
  <path d="M3 10 L14 16 L3 22" stroke="#38bdf8" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M29 10 L18 16 L29 22" stroke="#f87171" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="16" y1="6" x2="16" y2="26" stroke="#64748b" stroke-width="2" stroke-linecap="round"/>
</svg>'''

# ==============================================================================
# 2. VECTOR PARALLELOGRAM BANNERS (1200x160)
# ==============================================================================

# Flotilla Fleet Operational Header Banner
BANNER_FLOTILLA = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 160" width="100%" height="100%" fill="none">
  <defs>
    <linearGradient id="bg-flotilla" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a121e" stop-opacity="0.98"/>
      <stop offset="50%" stop-color="#0f1a2a" stop-opacity="0.98"/>
      <stop offset="100%" stop-color="#070c14" stop-opacity="0.98"/>
    </linearGradient>
    <pattern id="grid-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1e3a5f" fill-opacity="0.4"/>
    </pattern>
  </defs>

  <!-- Main Tilted Parallelogram -->
  <polygon points="28,4 1196,4 1172,156 4,156" fill="url(#bg-flotilla)" stroke="#0284c7" stroke-width="2" stroke-linejoin="round"/>
  <!-- Dot Grid Texture in Center -->
  <polygon points="30,6 1194,6 1170,154 6,154" fill="url(#grid-dots)"/>

  <!-- Left Accent Chevron (Cobalt/Cyan) -->
  <polygon points="28,4 56,4 32,156 4,156" fill="#0284c7" fill-opacity="0.8"/>
  <line x1="58" y1="4" x2="34" y2="156" stroke="#38bdf8" stroke-width="2"/>

  <!-- Right Accent Chevron with Solar Amber Tick -->
  <polygon points="1168,4 1196,4 1172,156 1144,156" fill="#0369a1" fill-opacity="0.4"/>
  <line x1="1142" y1="4" x2="1118" y2="156" stroke="#f59e0b" stroke-width="2.5"/>

  <!-- Top and Bottom Precision Telemetry Rails -->
  <line x1="68" y1="12" x2="1130" y2="12" stroke="#1e3a5f" stroke-width="1.5"/>
  <line x1="44" y1="148" x2="1106" y2="148" stroke="#1e3a5f" stroke-width="1.5"/>

  <!-- Outer Corner Crosshairs -->
  <line x1="24" y1="4" x2="36" y2="4" stroke="#38bdf8" stroke-width="2"/>
  <line x1="1164" y1="156" x2="1176" y2="156" stroke="#38bdf8" stroke-width="2"/>

  <!-- Stenciled Telemetry Tag -->
  <text x="80" y="32" font-family="'Share Tech Mono', monospace" font-size="11" fill="#38bdf8" letter-spacing="2">FLOTILLA COMMAND // ACCORDS SECTOR 04 // MANDATE: ACTIVE</text>
  <text x="1090" y="32" text-anchor="end" font-family="'Share Tech Mono', monospace" font-size="11" fill="#64748b" letter-spacing="1">REF.518-AA</text>
</svg>'''

# Tactical Engagement Header Banner (Amber & Cyan High-Contrast)
BANNER_TACTICAL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 160" width="100%" height="100%" fill="none">
  <defs>
    <linearGradient id="bg-tactical" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#14120e"/>
      <stop offset="50%" stop-color="#1c1813"/>
      <stop offset="100%" stop-color="#0f0d0a"/>
    </linearGradient>
  </defs>

  <!-- Tilted Parallelogram -->
  <polygon points="30,4 1196,4 1170,156 4,156" fill="url(#bg-tactical)" stroke="#d97706" stroke-width="2"/>

  <!-- Left Warning Slash -->
  <polygon points="30,4 62,4 36,156 4,156" fill="#f59e0b"/>
  <!-- Secondary Slash -->
  <polygon points="70,4 82,4 56,156 44,156" fill="#d97706" fill-opacity="0.6"/>

  <!-- Bottom Amber Edge Notch -->
  <line x1="48" y1="150" x2="1160" y2="150" stroke="#f59e0b" stroke-width="2"/>
  <rect x="110" y="146" width="40" height="8" fill="#f59e0b"/>

  <!-- Telemetry -->
  <text x="96" y="32" font-family="'Share Tech Mono', monospace" font-size="11" fill="#f59e0b" letter-spacing="2">FIRE CONTROL // TAC-GRID ACTIVE // 0.88C SPINAL ACCELERATOR</text>
  <text x="1150" y="32" text-anchor="end" font-family="'Share Tech Mono', monospace" font-size="11" fill="#78350f" letter-spacing="1">TARGET LOCKED</text>
</svg>'''

# Bulkhead Hazard Advisory Banner (Solar Yellow / Hazard Chevron)
BANNER_HAZARD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 160" width="100%" height="100%" fill="none">
  <defs>
    <linearGradient id="bg-hazard" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#121008"/>
      <stop offset="50%" stop-color="#17140a"/>
      <stop offset="100%" stop-color="#0d0b05"/>
    </linearGradient>
    <pattern id="hazard-chevrons" width="30" height="30" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="30" stroke="#facc15" stroke-width="14"/>
      <line x1="15" y1="0" x2="15" y2="30" stroke="#000000" stroke-width="14"/>
    </pattern>
  </defs>

  <!-- Tilted Parallelogram -->
  <polygon points="30,4 1196,4 1170,156 4,156" fill="url(#bg-hazard)" stroke="#ca8a04" stroke-width="2"/>

  <!-- Left Hazard Chevron Block -->
  <polygon points="30,4 85,4 59,156 4,156" fill="url(#hazard-chevrons)"/>
  <line x1="88" y1="4" x2="62" y2="156" stroke="#facc15" stroke-width="2.5"/>

  <!-- Top Caution Border -->
  <line x1="95" y1="10" x2="1185" y2="10" stroke="#ca8a04" stroke-width="1.5" stroke-dasharray="16 4"/>

  <!-- Telemetry -->
  <text x="105" y="32" font-family="'Share Tech Mono', monospace" font-size="11" fill="#facc15" letter-spacing="2">[ CRITICAL ADVISORY // DECOMPRESSION WARNING ]</text>
  <text x="1155" y="32" text-anchor="end" font-family="'Share Tech Mono', monospace" font-size="11" fill="#dc2626" letter-spacing="1">LETHAL</text>
</svg>'''

# ==============================================================================
# WRITE FILES
# ==============================================================================

files_to_write = {
    # Mechanical
    os.path.join(MECH_DIR, "hit.svg"): HIT_SVG,
    os.path.join(MECH_DIR, "crit.svg"): CRIT_SVG,
    os.path.join(MECH_DIR, "upgrade.svg"): UPGRADE_SVG,
    os.path.join(MECH_DIR, "downgrade.svg"): DOWNGRADE_SVG,
    os.path.join(MECH_DIR, "gambit.svg"): GAMBIT_SVG,
    os.path.join(MECH_DIR, "ap.svg"): AP_SVG,
    os.path.join(MECH_DIR, "blocker.svg"): BLOCKER_SVG,
    os.path.join(MECH_DIR, "chain.svg"): CHAIN_SVG,
    os.path.join(MECH_DIR, "push.svg"): PUSH_SVG,
    os.path.join(MECH_DIR, "contest.svg"): CONTEST_SVG,

    # Banners
    os.path.join(BANNER_DIR, "banner_parallelogram_flotilla.svg"): BANNER_FLOTILLA,
    os.path.join(BANNER_DIR, "banner_parallelogram_tactical.svg"): BANNER_TACTICAL,
    os.path.join(BANNER_DIR, "banner_parallelogram_hazard.svg"): BANNER_HAZARD,
}

if __name__ == "__main__":
    for path, content in files_to_write.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated: {os.path.basename(path)}")

    print(f"\nAll {len(files_to_write)} referenced vector assets generated successfully!")
