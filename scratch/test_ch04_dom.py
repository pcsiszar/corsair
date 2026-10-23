import subprocess
import json
from pathlib import Path

# Run export_pdf.py first to compile the PDF and verify dimensions
cmd = [
    "python",
    ".agents/skills/corsair-book-publishing/scripts/export_pdf.py",
    "--input", "html/04_Armory_and_Gear.html",
    "--output", "html/04_Armory_and_Gear.pdf"
]
print("Running PDF export...")
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)
