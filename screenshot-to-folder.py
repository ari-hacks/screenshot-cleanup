import os
import fnmatch
import shutil
from pathlib import Path

home = str(Path.home())

for file_name in os.listdir(home + '/Desktop/'):
    if fnmatch.fnmatch(file_name, 'Screen*.png'):
        print(file_name)
        shutil.move(home + "/Desktop/"+ file_name, home + "/Desktop/Screenshots/ "+ file_name)
print('Finished moving screen shots')
