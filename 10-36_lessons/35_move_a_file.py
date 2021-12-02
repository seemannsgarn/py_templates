import os

source = "C:\\test.txt"
destination = "C:\\usr\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source + " was not found")