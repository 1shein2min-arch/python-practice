import os

data = "reports"

if os.path.isfile(data):
    print("This is a file")

if os.path.isdir(data):
    print("This is a folder")