def total_price(price, quantity):
    return price * quantity


print("===== Shopping =====")

price = int(input("Enter Price : "))
quantity = int(input("Enter Quantity : "))

total = total_price(price, quantity)

print(f"Total Price : {total}")