import glob, re

for f in sorted(glob.glob('html/*.html')):
    txt = open(f, encoding='utf-8').read()
    pages = re.findall(r'class=[\'"]book-page[^\'"]*[\'"]\s+id=[\'"]([^\'"]+)[\'"]', txt)
    page_nums = re.findall(r'class=[\'"]page-number[\'"]>(\d+)</span>', txt)
    first_p = page_nums[0] if page_nums else '?'
    last_p = page_nums[-1] if page_nums else '?'
    print(f'{f}: {len(pages)} pages (numbered {first_p} to {last_p})')
