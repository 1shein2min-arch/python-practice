phones = {
    "Phone": 500000,
    "Laptop": 1200000,
    "Watch": 250000,
    "Camera": 800000
}
def show_phone() :
    for name,price in phones.items() :
        print(f"{name} : {price}")

def show_total(price,quantity) :
    return price * quantity

print("===== Phone Shop =====")

show_phone()

name = input("Enter Name :")
if name in phones :
    quantity = int(input("Enter Quantity :"))
    total = show_total(phones.get(name),quantity)

    print(f"Total Price : {total}")
    if total >= 1000000 :
        print("Customer Type : VIP Customer")
    else :
        print("Customer Type : Normal Customer")

else :
    print("Phone Not Found")
