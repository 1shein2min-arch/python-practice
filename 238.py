products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}

def product():
    for name,price in products.items() :
        print(f"{name} : {price}")

def total(price,quantity) :
    return price * quantity

print("===== Store Order =====")

product()

name = input("Enter Product :")
if name in products :
    quantity = int(input("Enter Quantity"))
    result = total(products.get(name),quantity)

    print(f"Total Price :{result}")
    discount = result * 0.1
    print(f"Discount : {discount}")

    final_price = result - discount
    print(f"Final Price : {final_price}")
else :
    print("Product Not Found")