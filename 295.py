with open("products.txt","w") as file :
    file.write("iPhone - 1200000\n")
    file.write("Redmi - 600000\n")
    file.write("Samsung - 900000\n")
    file.write("Vivo - 500000")

print("Product List")

print("------------")

with open("products.txt","r") as file :
    data = file.read()

    print(data)

    print("------------")

    print("Total Products : 4")