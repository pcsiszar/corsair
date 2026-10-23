#!/usr/bin/env python3
from pathlib import Path

def clean_mechanisms():
    src_file = Path("scratch/generate_ch05_starships.py")
    lines = src_file.read_text(encoding="utf-8").splitlines()
    new_lines = []
    
    for line in lines:
        if '<strong>Mechanism:</strong>' in line:
            # extract text between <strong>Mechanism:</strong> and </p>
            start = line.find('<strong>Mechanism:</strong>') + len('<strong>Mechanism:</strong>')
            end = line.find('</p>')
            mech_text = line[start:end].strip() if end != -1 else line[start:].strip()
            new_lines.append(f'                <strong>Mount:</strong> {mech_text}<br>')
        else:
            new_lines.append(line)
            
    result = "\n".join(new_lines)
    src_file.write_text(result, encoding="utf-8")
    print("Cleaned all mechanism lines.")

if __name__ == "__main__":
    clean_mechanisms()
