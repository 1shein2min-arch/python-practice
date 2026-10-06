import csv 

repairs = [
    ["Aung", "iPhone 11", 30000, 5000],
    ["Mg Mg", "Redmi Note 13", 50000, 10000],
    ["Ko Ko", "Samsung A52", 80000, 15000],
    ["Kyaw Kyaw", "Vivo Y55", 25000, 5000]
]

data = []

for repair in repairs :
    customer = repair[0]
    model = repair[1]
    repair_fee = repair[2]
    part_fee = repair[3]
    total_fees = repair_fee + part_fee

    data.append([customer,model,repair_fee,part_fee,total_fees])

with open("repair_total.csv","w",newline="")as file :
    data1 = csv.writer(file)

    data1.writerow(["Customer","Model","Repair Fee","Parts Fee","Total Fee"])
    data1.writerows(data)
