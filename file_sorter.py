import os
import shutil
files = os.listdir()
for i in files:
    name, extension  = os.path.splitext(i)
    if os.path.isdir(i):
        continue
    elif (extension == ""):
        continue
    else:
        exists = os.path.exists(extension)
        if(not exists):
            os.mkdir(extension)
        shutil.move(i,extension)