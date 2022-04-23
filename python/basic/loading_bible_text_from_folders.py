from pathlib import Path

p = Path('.')
r = p / 'resources' / 'La Santa Biblia' / 'assets' / 'ntv' / 'LIB1'
for child in r.iterdir(): 
    with child.open() as f:
        print(f.readline())