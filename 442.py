import os 

old_file = "reports/repair_history.txt"
new_file = "reports/repair_backup.txt"

if os.path.exists(old_file) :
    if not os.path.exists(new_file) :
        os.rename(old_file,new_file)
        print("File renamed successfully")
    else :
        print("New File Already Exists")

else :
    print("Old File Not Found")