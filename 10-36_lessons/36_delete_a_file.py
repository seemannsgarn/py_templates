import os
import shutil

path = "C:\\usr\\folder"

try:
    # os.remove(path)   # delete a file
    # os.rmdir(path)    # delete an empty directory
    shutil.rmtree(path) # delete a directory containing files
except Exception as e:
    print(e)
else:
    print(path + " was deleted")


