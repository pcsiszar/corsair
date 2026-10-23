#!/usr/bin/env python3
from pathlib import Path
import re

def fix_nested_p():
    src_file = Path("scratch/generate_ch05_starships.py")
    code = src_file.read_text(encoding="utf-8")

    # Replace <p ...><strong>Mechanism:</strong> (.*?)</p>\s*<strong>Size:</strong>
    # with <strong>Mount:</strong> \1<br>\n            <strong>Size:</strong>
    pattern = re.compile(
        r'<p style="font-size: 7.5pt; line-height: 1.22; margin-bottom: 0.8mm; color: var(--text-body);"><strong>Mechanism:</strong> (.*?)</p>\s*<strong>Size:</strong>',
        re.DOTALL
    )

    def repl(m):
        mech = m.group(1).strip()
        return f'<strong>Mount:</strong> {mech}<br>\n            <strong>Size:</strong>'

    code, count = pattern.subn(repl, code)
    print(f"Fixed {count} nested mechanism tags.")
    src_file.write_text(code, encoding="utf-8")

if __name__ == "__main__":
    fix_nested_p()
