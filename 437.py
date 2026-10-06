import os

with open("reports/repair.txt","w") as file :
    file.write("Aung\n")
    file.write("Mg Mg\n")
    file.write("Ko Ko")

data = os.listdir("reports")
print(data)