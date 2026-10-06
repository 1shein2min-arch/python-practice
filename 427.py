import csv

customers = [
    ["Aung", "09123456789", "iPhone 11"],
    ["Mg Mg", "09234567890", "Redmi Note 13"],
    ["Ko Ko", "09345678901", "Samsung A52"]
]

with open("customer.csv","w",newline="")as file :
    data = csv.writer(file)

    data.writerow(["Name", "Phone", "Model"])
    data.writerows(customers)