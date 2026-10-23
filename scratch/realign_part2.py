import re
from pathlib import Path

# 1. Update 03_Classes.html
classes_file = Path("html/03_Classes.html")
classes_content = classes_file.read_text(encoding="utf-8")

# Replace page numbers in <span class="page-num">XX</span>
def shift_classes_num(m):
    old_num = int(m.group(1))
    new_num = old_num - 5
    return f'<span class="page-num">{new_num}</span>'

classes_content_new = re.sub(r'<span class="page-num">(\d+)</span>', shift_classes_num, classes_content)

# Replace page numbers in HTML comments <!-- PAGE XX ... -->
def shift_classes_comment(m):
    old_num = int(m.group(1))
    new_num = old_num - 5
    return f'PAGE {new_num}'

classes_content_new = re.sub(r'PAGE (\d+)', shift_classes_comment, classes_content_new)

classes_file.write_text(classes_content_new, encoding="utf-8")
print(f"Updated {classes_file}")

# 2. Update 03b_Interlude_Post_War.html
postwar_file = Path("html/03b_Interlude_Post_War.html")
postwar_content = postwar_file.read_text(encoding="utf-8")

def shift_postwar_num(m):
    old_num = int(m.group(1))
    new_num = old_num - 5
    return f'<span class="page-num">{new_num}</span>'

postwar_content_new = re.sub(r'<span class="page-num">(\d+)</span>', shift_postwar_num, postwar_content)
postwar_content_new = re.sub(r'PAGE (\d+)', shift_classes_comment, postwar_content_new)

postwar_file.write_text(postwar_content_new, encoding="utf-8")
print(f"Updated {postwar_file}")

# 3. Update assemble_book.py: remove 02b_Interlude_Great_Tithe.html from between 02 and 03
assemble_file = Path(".agents/skills/corsair-book-publishing/scripts/assemble_book.py")
assemble_content = assemble_file.read_text(encoding="utf-8")
assemble_content = assemble_content.replace('    "02b_Interlude_Great_Tithe.html",\n', '')
assemble_file.write_text(assemble_content, encoding="utf-8")
print(f"Updated {assemble_file}")
