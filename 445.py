import os

print(f"Current Folder : {os.getcwd()}")

folder = "reports"
file_name = "repair_history.txt"
backup_name = "repair_backup.txt"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Reports folder created")
else:
    print("Reports folder already exists")

file_path = os.path.join(folder, file_name)
backup_path = os.path.join(folder, backup_name)

if not os.path.isfile(file_path):
    with open(file_path, "w") as file:
        file.write("Phone Repair History")
    print("Repair history file created")
else:
    print("Repair history file already exists")

print(f"Files in reports : {os.listdir(folder)}")

if os.path.isfile(file_path):

    if not os.path.exists(backup_path):
        os.rename(file_path, backup_path)
        print("File renamed successfully")

    else:
        print("Backup file already exists")

if os.path.isfile(backup_path):
    print("Backup file exists")
else:
    print("Backup file not found")

print(f"Files in reports : {os.listdir(folder)}")