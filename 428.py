import csv

product = [
    ["iPhone 11",300000,5],
    ["Redmi Note 13",250000,8],
    ["Samsung A52",200000,3]
]

with open("products.csv","w",newline="")as file :
    data = csv.writer(file)

    data.writerow(["Product","Price","Stock"])
    data.writerows(product)