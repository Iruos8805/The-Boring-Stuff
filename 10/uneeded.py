import os
from pathlib import Path

p = Path('/home/souri/Desktop/uneededmass')

for filename in p.glob('*'):
    if os.path.getsize(str(filename))>104857600:
        print(filename)
        print(os.path.abspath(filename))
