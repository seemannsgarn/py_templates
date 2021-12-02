import os

path = "C:\\test folder"

if os.path.exists(path):
    print('This location exists!')
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print('That is a directory!')
else:
    print("This location doesn't exist!")