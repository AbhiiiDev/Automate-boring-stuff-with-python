import shutil
from pathlib import Path
h=Path.cwd()
# (h/'spam').mkdir(exist_ok=True)
# (h/'eggs').mkdir(exist_ok=True)
# (h/'spam/eggs').mkdir(exist_ok=True)
# (h/'eggs/spam').mkdir(exist_ok=True)

# for f in ['spam/file1.txt', 'spam/eggs/file2.txt', 'spam/eggs/file3.txt',
# 'eggs/spam/file4.txt']:
#     with open(h/f,'w',encoding='UTF-8') as file:
#         file.write('hello !')
s='eggs/spam/file4.txt'
shutil.copy(s,'eggs/spam/file3.txt')
