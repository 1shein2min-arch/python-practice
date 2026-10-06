phones = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}


def show_phone():
    for name, price in phones.items():
        print(f"{name} : {price}")


def show_price(price, quantity):
    return price * quantity


print("===== Phone Shop =====")

print("Phones :")
show_phone()

name = input("Enter Phone : ")

if name in phones:

    quantity = int(input("Enter Quantity : "))

    total = show_price(phones.get(name), quantity)

    print(f"Total Price : {total}")

    if quantity >= 3:
        discount = total * 0.05
    else:
        discount = 0

    print(f"Quantity Discount : {discount}")

    price_after_quantity_discount = total - discount

    coupon = input("Enter Coupon : ")

    if coupon == "SAVE10":
        coupon_discount = price_after_quantity_discount * 0.10
    else:
        coupon_discount = 0

    final_price = price_after_quantity_discount - coupon_discount

    print(f"Coupon Discount : {coupon_discount}")
    print(f"Final Price : {final_price}")

else:
    print("Phone Not Found")