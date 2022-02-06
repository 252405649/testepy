import os
print(os.path.abspath('..'))
print(os.path.exists('/user'))
print(os.path.isfile('/user'))
print(os.path.isdir('/user'))
print(os.path.join('./aa/bb/', 'ff/cc'))

from pathlib import Path
p = Path('.')
print(p.resolve())
print(p.is_dir())

q = Path('d:/aa/qq/p')
Path.mkdir(q, parents=True)