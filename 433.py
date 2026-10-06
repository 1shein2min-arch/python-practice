import csv

repairs = [
    ["Aung", "iPhone 11", 80000, 30000],
    ["Mg Mg", "Redmi Note 13", 120000, 40000],
    ["Ko Ko", "Samsung A52", 600000, 50000],
    ["Kyaw Kyaw", "Vivo Y55", 50000, 10000]
]

data = []

for repair in repairs:
    customer = repair[0]
    model = repair[1]
    repair_fee = repair[2]
    part_fee = repair[3]
    totol_fee = repair_fee + part_fee

    if totol_fee >= 500000:
        discount = 10
        discount_amount = totol_fee * 10 / 100

    elif totol_fee >= 100000:
        discount = 5
        discount_amount = totol_fee * 5 / 100

    else:
        discount = 0
        discount_amount = 0

    final_fee = totol_fee - discount_amount

    data.append([
        customer,
        model,
        repair_fee,
        part_fee,
        totol_fee,
        discount,
        final_fee
    ])

with open("repair_total.csv", "w", newline="") as file:
    data1 = csv.writer(file)

    data1.writerow([
        "Customer",
        "Model",
        "Repair Fee",
        "Part Fee",
        "Total Fee",
        "Discount",
        "Final Fee"
    ])

    data1.writerows(data)