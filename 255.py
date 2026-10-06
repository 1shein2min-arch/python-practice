products = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}
def show_product() :
    for name,price in products.items() :
        print(f"{name} : {price}")

def show_pro(price,quantity) :
    return price * quantity

def show_dis(total) :
    if total >= 1000000 :
        return total * 0.1
    else :
        return 0
    
def can_vip(final_price) :
    if final_price >= 1000000 :
        return True 
    else :
        return False

print("===== Shoppint Cart =====")

print("Products :")
show_product()

name = input("Enter Name :")
if name in products :
    quantity = int(input("Enter Quantity :"))
    total = show_pro(products.get(name),quantity)
    print(f"Total Price : {total}")

    discount = show_dis(total)
    print(f"Discount : {discount}")

    final_price = total - discount
    print(f"Final Price : {final_price}")

    if can_vip(final_price) :
        print("Order Status : VIP")
    else :
        print("Order Status : Normal")


else :
    print("Product Not Found")