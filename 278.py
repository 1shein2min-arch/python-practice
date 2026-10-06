products = ["Phone", "Laptop", "Headset", "Charger", "Mouse"]

name = input("Enter Product :")
if name in products :
    print("Product Found")

    products.remove(name)
    print("Product Removed")
    print(products)
    
else :
    print("Product Not Found")
