import csv

customers = [
    ["Aung", "09123456789", "iPhone 11"],
    ["Mg Mg", "09234567890", "Redmi Note 13"],
    ["Ko Ko", "09345678901", "Samsung A52"]
]

with open("customers.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Phone", "Model"])
    writer.writerows(customers)