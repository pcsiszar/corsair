import re

for f in ['html/00_Front_Matter.html', 'html/01_Core_Mechanics.html', 'html/01b_Interlude_27th_Hour.html', 'html/02_Character_Creation.html', 'html/02b_Interlude_Great_Tithe.html', 'html/03_Classes.html', 'html/03b_Interlude_Post_War.html', 'html/04_Armory_and_Gear.html', 'html/05_Starships.html']:
    txt = open(f, encoding='utf-8').read()
    footers = re.findall(r'<div class=[\'"]page-running-footer[\'"]>(.*?)</div>', txt, re.DOTALL)
    pages = re.findall(r'class=[\'"]book-page[^\'"]*[\'"]\s+id=[\'"]([^\'"]+)[\'"]', txt)
    first_f = footers[0].strip().replace('\n', ' ') if footers else 'NONE'
    last_f = footers[-1].strip().replace('\n', ' ') if footers else 'NONE'
    print(f'{f} ({len(pages)} pages):')
    print(f'   First footer: {first_f}')
    print(f'   Last footer:  {last_f}')
