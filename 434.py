import csv

repairs = [
    ["Aung", "iPhone 11", 80000, 30000],
    ["Mg Mg", "Redmi Note 13", 120000, 40000],
    ["Ko Ko", "Samsung A52", 600000, 50000],
    ["Kyaw Kyaw", "Vivo Y55", 50000, 10000],
    ["Hla Hla", "iPhone 13", 200000, 50000]
]

data =[]

for repair in repairs :
    customer = repair[0]
    model = repair[1]
    repair_fee = repair[2]
    part_fee = repair[3]
    total_fee = repair_fee + part_fee

    if total_fee > 100000 :
        data.append([customer,model,repair_fee,part_fee,total_fee])

with open ("repair_total.csv","w",newline="")as file :
    data1 = csv.writer(file)

    data1.writerow(["Customer","Model","Repair Fee","Parts Fee","Total Fee"])
    data1.writerows(data)