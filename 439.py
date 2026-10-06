import os

if not os.path.exists("reports/daily.txt") :
    with open("reports/daily.txt","w")as file :
        file.write("Daily Repair Report")

print("Done")