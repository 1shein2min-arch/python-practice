products = [
    "Redmi Note 13",
    "iPhone 11",
    "Samsung A52",
    "Vivo Y20"
]

with open("products.txt","w") as file :
    for product in products :
        file.write(product + "\n")
