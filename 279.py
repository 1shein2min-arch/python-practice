products = ["Phone", "Laptop", "Phone", "Mouse", "Phone", "Laptop"]

def count_product () :
    name = input("Enter Product :")
    if name in products :
        print(f"{name} count : {products.count(name)}")

    else :
        print("Product Not Found")

count_product()

        