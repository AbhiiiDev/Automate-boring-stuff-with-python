import os,shutil
from pathlib import Path
h=Path.cwd()

for folder_name,sub_folders,files in os.walk('file_handling'):
    print('The current folder name is : ',folder_name)

    for subfolder in sub_folders:
        print('SubFolder of %s : %s' % (folder_name,subfolder))

    for file in files:
        print('file inside '+folder_name+":"+file)
        p=Path(folder_name)
        shutil.move(p/file,p/file.upper())

    print(' ')