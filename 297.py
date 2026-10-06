name = input("Enter Product :")
price = input("Enter Price :")

with open("products.txt","a") as file :
    file.write("\n" + name + ":" + price )

print("Product List")
print("------------")

with open("products.txt","r") as file:
    data = file.read()

    print(data)
