products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}
def show_product() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def show_total(price,quantity) :
    return price * quantity 

print("===== Order Check =====")

print("Products :")
show_product() 

name = input("Enter Product :")
if name in products :
    quantity = int(input("Enter Quantity :"))
    total = show_total(products.get(name),quantity)

    print(f"Total Price : {total}")
    if total >= 1000000 :
        print("Order Status : VIP Order")

    else :
        print("Order Status : Normal Order")

else :
    print("Product Not Found")
