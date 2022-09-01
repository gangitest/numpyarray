from pathlib import Path
import os

#Creates new Directory if not available 
if not os.path.exists('files'):
    os.makedirs('files')

root_dir = Path('files')

for i in range(21,31):
  filename = 'gangi' + str(i)  +'.txt'
  filepath = root_dir / Path(filename)
  filepath.touch()