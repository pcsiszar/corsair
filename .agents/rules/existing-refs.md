---
trigger: always_on
---

# Never make up new concepts and content unless explicitly told so

The agent should never make up new places, new equipment, new factions, unless explicitly told so.
The only exemption being is NPCs and their names that appear in the examples.

Refer to the contents of the equipment, ships, classes and lore folder when needing to make up situations on the fly.

## Strict Rulebook Markdown Fidelity for Published HTML & Documents

When working on or generating official TTRPG publication HTML files (e.g., the complete TTRPG book HTML, chapter spreads, reference sheets, or primers), the agent is strictly forbidden from misrepresenting, rewriting, or drifting from the content described in the repository's markdown source files (`rulebook/**/*.md`).

- **Verbatim & High-Fidelity Representation:** The HTML book's text and rules content must remain as close to the source markdown documents as possible.
- **Zero Mechanical Drift:** Never alter die sizes, action point costs, success thresholds, effect names, or mathematical formulas established in `rulebook/core/`.
- **Lore Canon Integrity:** Never summarize away essential nuances, contradict historical timelines (518 AA), or conflate public sphere lore with confidential material (e.g., `rulebook/lore/forbidden_archives/`).
- **Preserve Source Intent:** Adapt layout and formatting for print/display aesthetics, but preserve the exact prose, tone, and technical precision authored in the markdown files.