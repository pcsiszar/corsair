---
name: corsair-graphic-assets
description: >-
  Design guidelines, prompt engineering patterns, hard sci-fi constraints, automated Python post-processing (alpha keying, defringing, interior flattening), and HTML/CSS integration for creating TTRPG rulebook graphic design assets, callout textboxes, and chapter banners in Corsair.
---

# Corsair Graphic Asset Design & Processing Pipeline

This skill governs the authoring, generation, post-processing, and layout integration of visual UI containers (callout textboxes, rules panels, gameplay slates, hazard alerts, and chapter banners) for Corsair publications.

---

## 1. Golden Rules for Graphic Assets

1. **Assets Are Text Containers, Not Static Artworks**:
   Graphic assets exist to frame and host **live HTML typography**, rules tables, and story prose. The central reading area must remain clean, flat, and legible at all times.
2. **Strict Hard Sci-Fi Grounding**:
   Corsair follows hard science fiction rules mixed with a gritty space-cowboy aesthetic (*The Expanse*, *Mass Effect*, *Cowboy Bebop*, *Alien*).
   * **Never** use fantasy, medieval, or magical visual tropes (no glowing runes, spell circles, parchment paper, magical flames, or blood-magic splatter).
   * **Always** ground visual motifs in physical aerospace, naval, and industrial technology.
3. **Pure White Isolation for Deterministic Keying**:
   Every raw generation intended as a transparent container must be prompted with `isolated on a pure solid white background (#FFFFFF)`. Never allow soft drop shadows or bounding frames in the prompt, as they contaminate the alpha channel.
4. **Always Run the Post-Processing Script**:
   Never use raw AI-generated PNGs directly in HTML. Always execute the automated script to strip the background to 32-bit RGBA, defringe the 1px white border halos, flatten interior color noise, and calculate CSS padding insets.

---

## 2. Hard Sci-Fi Thematic Invariants

Corsair visual assets must strictly embody authentic aerospace, industrial, and cyber warfare motifs:

| Asset Function | Approved Hard Sci-Fi Motifs | Prohibited Tropes |
| :--- | :--- | :--- |
| **Rules Specifications** | Welded titanium armor plates, countersunk hex rivets, 45° chamfered cuts, brushed tungsten, stenciled industrial serial numbers. | Generic parchment, medieval stone slabs, glowing arcane runes, fantasy border filigree. |
| **Gameplay Examples** | Tactical avionics slates, ruggedized datapad chassis, polarized glass screens, corner status LED indicators, faint vector telemetry grids. | Ancient scrolls, torn paper scraps, magical scrying mirrors. |
| **Hazard / Alerts** | Weathered yellow/black or red hazard chevron striping, chipped industrial epoxy paint, emergency bulkhead latch plates, radiation trefoils. | Skulls with horns, fantasy hazard spikes, glowing demonic sigils. |
| **Damage / Breaches** | High-velocity kinetic ordnance impacts, sheared metal bites, scorched propellant backblast, hydraulic fluid/sealant spray, ablative chipping. | Fantasy blood splatters, gothic ink splotches, magical corrosion. |
| **Thermal / Propulsion** | Atmospheric re-entry thermal plasma flares, ablative heat-shield flaking, burning orange/amber sparks & drifting carbon motes. | Magical flames, wizard fire, mystical embers. |
| **Electronic Warfare** | Horizontal block displacement glitch shears, chromatic aberration (RGB channel phase shift), CRT phosphor scanline drift, data corruption. | Arcane distortion, magical shimmer, dream haze. |
| **Chapter Banners** | Astrophotographic deep-space nebulae, interstellar dust filaments, multi-magnitude star clusters with 4-point diffraction crosses. | Fantasy skyboxes, magical aurora borealis. |

---

## 3. The Prompting Formula for Text Containers

Every prompt for a callout textbox or UI panel MUST follow this standardized structure:

```text
Isolated flat graphic design element on a pure solid white background (#FFFFFF): one large solid-filled wide rectangular panel in flat [PRIMARY COLOR / HEX, e.g. dark carbon charcoal #121620]. The panel interior is a perfectly flat, uniform single color with absolutely no texture, no gradient, no pattern, no text, no highlights, and no shadows. Only the [SPECIFIC EDGES / CORNERS, e.g. top edge and right corner] are irregular, formed by [HARD SCI-FI MOTIF: e.g. atmospheric re-entry ablative burn with orange flame tongues and floating embers / kinetic ordnance impact with sheared metal and directional spray / horizontal digital glitch slices with cyan-magenta displacement]. Flat vector graphic design style, no drop shadow, no external border frame, panel fills most of the image.
```

### Prompt Engineering Invariants:
* **`Isolated on a pure solid white background (#FFFFFF)`**: Crucial for clean chroma-keying.
* **`Flat vector graphic design style`**: Encourages sharp, well-defined silhouettes without blurry painterly edges.
* **`No drop shadow, no border frame`**: Prevents semi-transparent dark halos that turn muddy when keyed.
* **`Panel interior is perfectly flat uniform single color`**: Ensures live text overlaid in CSS remains 100% readable.
* **`No text, no numbers, no words, no letters`**: Typography is handled entirely in HTML.

---

## 4. Automated Post-Processing Script

The post-processing script is located at:
[`.agents/skills/corsair-graphic-assets/scripts/process_asset.py`](file:///c:/Users/csisz/IdeaProjects/corsair/.agents/skills/corsair-graphic-assets/scripts/process_asset.py)

### CLI Usage:
```powershell
python .agents/skills/corsair-graphic-assets/scripts/process_asset.py --input "path/to/raw_generation.png" --output "rulebook/images/panel_name.png" [options]
```

### Arguments:
* `--input`, `-i` *(required)*: Path to the raw AI-generated image file.
* `--output`, `-o` *(required)*: Target destination for the processed RGBA PNG.
* `--no-flatten`: Skips interior color flattening (use only when a textured interior is explicitly intended).
* `--preview`, `-p`: Optional path to output a preview file composited over print-friendly paper (`#f8fafc`).
* `--lo` *(default: 12)*: Low threshold for white keying.
* `--hi` *(default: 60)*: High threshold for white keying.
* `--tol` *(default: 55)*: Interior flattening color difference tolerance.
* `--erode` *(default: 10)*: Interior erosion radius in pixels.

### Pipeline Execution Steps:
1. **Alpha Keying (`alpha_from_white`)**: Uses minimum-channel luminance math to convert `#FFFFFF` pixels to transparent alpha while preserving smooth anti-aliased edge contours.
2. **De-Fringing (`defringe`)**: Mathematically recalculates RGB values on semi-transparent edge pixels to eliminate the 1px white halo artifact.
3. **Interior Flattening (`flatten_interior`)**: Applies morphological erosion and flood-fills the deep interior with the median color, eliminating diffusion noise.
4. **Auto-Cropping (`autocrop`)**: Trims empty transparent padding to the visual bounding box.
5. **Safe Rect Calculation (`safe_rect`)**: Analyzes horizontal and vertical alpha cross-sections and prints the exact CSS `padding` insets (top, right, bottom, left) needed to keep text within the flat interior.

---

## 5. HTML & CSS Integration Patterns

### Reusable Container CSS
When applying a processed asset to a callout container, use the insets reported by the script:

```css
.callout-scifi {
    position: relative;
    width: 100%;
    min-height: 280px;
    background-image: url('./images/panel_solar_flame.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    
    /* Insets reported by process_asset.py safe_rect: */
    padding: 90px 140px 40px 80px;
    
    color: #e2e8f0;
    font-family: 'Barlow', sans-serif;
    font-size: 1rem;
    line-height: 1.55;
}

.callout-scifi h4 {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
    color: #f59e0b; /* Accent spot color */
}
```

### Full-Bleed Banners
For chapter header banners spanning the full width of a spread:
```css
.chapter-banner {
    position: relative;
    width: 100%;
    height: 220px;
    background: url('./images/banner_cosmic_nebula_hd.png') center / cover no-repeat;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}
```

---

## 6. Catalog of Core Hard Sci-Fi Asset Archetypes

Use these proven templates for generating assets across Corsair books:

### Archetype A: Atmospheric Re-Entry Thermal Plume (`panel_solar_flame`)
* **Use Case:** Environmental hazards, propulsion mechanics, high-heat ship modules.
* **Prompt:**
  ```text
  Isolated flat graphic design element on a pure solid white background (#FFFFFF): one large solid-filled wide rectangular panel in flat dark charcoal-navy (#10141e). The panel interior is a perfectly flat, uniform single color with absolutely no texture, no gradient, no pattern, no text, and no shadows. Only the top edge and top-right corner are irregular, burning away into atmospheric re-entry thermal plasma flares with licking orange-amber flame tongues and drifting sparks. The left and bottom edges are crisp industrial 45-degree chamfered corners. Flat vector graphic design style, no drop shadow, no external border frame.
  ```

### Archetype B: Cyber EMP Glitch Slate (`panel_emp_glitch`)
* **Use Case:** Electronic warfare, sensor degradation, AI anomalies, hacking rules.
* **Prompt:**
  ```text
  Isolated flat graphic design element on a pure solid white background (#FFFFFF): one large solid-filled wide rectangular panel in flat dark navy-slate (#0b1018). The panel interior is a perfectly flat, uniform single color with absolutely no texture, no gradient, no pattern, no text, and no shadows. Only the right edge is irregular, tearing apart into horizontal digital glitch block displacement slices with electric cyan and magenta chromatic aberration offsets. The left edge has clean high-tech HUD brackets. Flat vector graphic design style, no drop shadow, no external border frame.
  ```

### Archetype C: Kinetic Ordnance Breach (`panel_kinetic_splatter`)
* **Use Case:** Critical wound tables, depressurization rules, ballistic weapon statblocks.
* **Prompt:**
  ```text
  Isolated flat graphic design element on a pure solid white background (#FFFFFF): one large solid-filled wide rectangular panel in flat dark gunmetal charcoal (#18181c). The panel interior is a perfectly flat, uniform single color with absolutely no texture, no gradient, no pattern, no text, and no shadows. Only the top-left corner is irregular, formed by a violent kinetic projectile impact with jagged sheared metal edges and high-velocity crimson hydraulic fluid spray. The other three corners are clean industrial beveled angles. Flat vector graphic design style, no drop shadow, no external border frame.
  ```

### Archetype D: Deep-Space Cosmic Gas Banner (`banner_cosmic_nebula`)
* **Use Case:** Chapter headers, sector navigation, fleet action splashes.
* **Prompt:**
  ```text
  Graphic design asset engineered to serve as a wide horizontal chapter title background banner for a hard sci-fi tabletop RPG book. A panoramic deep-space vista with swirling cosmic nebula gases in deep indigo, electric cyan, and warm solar amber dust filaments. The center of the banner is composed with a deep, dark atmospheric void with soft, diffuse illumination, intentionally designed to provide high visual contrast and zero visual noise for large white heading text placed over it. Star clusters and intricate glowing gas clouds frame the outer perimeter. Astrophotography realism, no planets, no spaceships, no text, no watermark.
  ```
