import csv

repairs = [
    ["Aung", "iPhone 11", 30000, 5000, "Done"],
    ["Mg Mg", "Redmi Note 13", 50000, 10000, "Pending"],
    ["Ko Ko", "Samsung A52", 80000, 15000, "Done"],
    ["Kyaw Kyaw", "Vivo Y55", 25000, 5000, "Pending"]
]

with open("repairs.csv","w",newline="") as file :
    data = csv.writer(file)

    data.writerow(["Customer","Model","Repair Fee","Parts Fee","Status"])

    data.writerows(repairs)