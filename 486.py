import csv

with open("repairs.csv","r",newline="") as file :
    reader = csv.reader(file)

    next(reader)
    total = 0

    for row in reader :
        total += int(row[1])
print(f"Total : {total}")


