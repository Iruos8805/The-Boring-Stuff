import shutil
from pathlib import Path

p = Path('/home/souri/Desktop')

for filename in p.glob('forselect/*.pdf'):
    shutil.copy(filename, p / '10')

for filename in p.glob('forselect/*.png'):
    shutil.copy(filename, p / '10')
