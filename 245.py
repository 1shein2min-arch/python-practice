products = {
    "Phone" : 500000 ,
    "Laptop" : 1200000 ,
    "Watch" : 250000 ,
    "Mouse" : 150000
}

def show_product() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def show_price(price,quantity) :
    return price * quantity

print("===== Shoppint Cart =====")

print("Products")

show_product()

name = input("Enter Product :")
if name in products :
    quantity = int(input("Enter Quantity :"))
    total = show_price(products.get(name),quantity)
    print(f"Total Price : {total}")
    if quantity >= 5 :
        discount = total * 0.1
        final_price = total - discount
        print(f"Discount : {discount}")
        print(f"Final Price : {final_price}")
    else :
        print(f"Discount : 0")
        print(f"Final Price : {total}")

else :
    print("Product Not Found")