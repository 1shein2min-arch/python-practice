products = [
    "Redmi Note 13 | 250000",
    "iPhone 11 | 450000",
    "Samsung A52 | 300000"
]

with open("products.txt","w")as file :
    for line in products :
        file.write(line + "\n")

product = input("Enter Product :")
price = input("Enter Price :")

with open("products.txt","a") as file :
    file.write("\n" + product +" | " + price)

print("Product List")

print("------------")

with open("products.txt","r") as file :
    for line in file :
        data = line.split(" | ")

        name = data[0].strip()
        price = data[1].strip()

        print(f"Product : {name}")
        print(f"Price : {price}")
        print()
