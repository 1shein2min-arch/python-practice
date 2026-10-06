import csv

with open("repair.csv","r") as file :
    data = csv.reader(file)

    next(data)

    for row in data :
        repair_fee = int(row[2])
        part_fee = int(row[3])
        total_fee = repair_fee + part_fee
        if total_fee >= 200000:
            print(f"Customer : {row[0]}")
            print(f"Model : {row[1]}")
            print(f"Total Fee :{total_fee}")
            print("--------------")

