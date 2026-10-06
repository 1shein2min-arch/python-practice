def total(price,quantity) :
    return price * quantity

print("===== Order Check =====")

price = int(input("Enter Price :"))
quantity = int(input("Enter quantity :"))

total_price = total(price,quantity)

print(f"Total Price : {total_price}")

if total_price >= 1000000 :
    print("Order Status : VIP Order")

else :
    print("Order Status : Normal Order")