size = input("Enter coffee size (small/medium/large): ")
takeaway = input("Is this takeaway? (yes/no): ")
if size == "small":
    price = 2000
elif size == "medium":
    price = 3000
elif size == "large" :
    price = 4000
else :
    print("Invalid price")
if takeaway == "yes":
    final_price = price + 200
else:
    final_price= price
    print(f"final price is {final_price}")