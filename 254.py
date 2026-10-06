products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}

def show_name() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def show_price(price,quantity) :
    return price * quantity

def can_vip(total_price) :
    if total_price >= 1000000 :
        return True
    else :
        return False

print("===== Shopping Order =====")

print("Products :")
show_name()

name = input("Enter Product :")
if name in products :
    quantity = int(input("Enter Quantity :"))
    total = show_price(products.get(name),quantity)
    print(f"Total Price : {total}")

    if total >= 1000000 :
        discount = total * 0.1
        print(f"Discount : {discount}")

        final_price = total - discount
        print(f"Final Price : {final_price}")
    else :
        discount = 0 
        print("Discount : 0")
        print(f"Final Price : {total}")

    if can_vip(final_price) :
        print("Customer Type : VIP")
    else :
        print("Customer Type : Normal")
else :
    print("Product Not Found")