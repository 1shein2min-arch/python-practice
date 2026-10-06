import os 

folder = "reports"

file_name = "repair_history.txt"

path = os.path.join(folder,file_name)

with open(path,"w") as file :
    file.write("Phone Repair History")

print(path)