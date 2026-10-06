phones = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}

def show_phone () :
    for name,price in phones.items() :
        print(f"{name} : {price}")

def show_pro (price,quantity) :
    return price * quantity

print("===== Phone Shop =====")

print("Phone :")
show_phone()

name = input("Enter Name :")
if name in phones :
    quantity = int(input("Enter Quantity :"))
    total = show_pro(phones.get(name),quantity)

    print(f"Total Price : {total}")
    if quantity >= 3 :
        discount = total * 0.05 
        final_price = total - discount

        print(f"Discount : {discount}")
        print(f"Final Price : {final_price}")

    else :
        discount = 0
        final_price = total - discount
        print(f"Discount : {discount}")
        print(f"Final Price : {final_price}")

else :
    print("Phone Not Found")