import os

if os.path.exists("reports") :
    print("Folder exists")
else :
    print("Folder does not exist")

if not os.path.exists("reports") :
    os.mkdir("reports")

