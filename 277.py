products = ["Phone", "Laptop", "Headset", "Charger", "Mouse"]

def remove_product() :
    name = input("Enter Name :")
    if name in products:
        products.remove(name)
        print("Product Removed")
    else :
        print("Product Not Found")

remove_product()
print(products)