import os
import re
from pathlib import Path
import shutil


p = Path('/home/souri/Desktop/gapfill')


prefix = re.compile(r'(image)(\d{1,3})')


i = 1

matched_numbers = []

for filename in os.listdir(p):
    match = prefix.search(filename)
    if match:
        number = int(match.group(2))  
        matched_numbers.append(number)


matched_numbers.sort()


for number in matched_numbers:
    while number != i:
        old_name = f'image{number:03}.ext'  
        new_name = f'image{i:03}.ext' 
        old_path = p / old_name
        new_path = p / new_name
        if old_path.exists():
            shutil.move(old_path, new_path)
        i += 1
    i += 1  