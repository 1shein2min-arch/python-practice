import os

if not os.path.exists("reports/repair_final.txt") :
    with open("reports/repair_final.txt","w") as file :
        file.write("Repair Done")
