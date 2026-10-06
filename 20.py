coffee_size = input("Enter coffee size small/medium/large")
takeaway = input("Is this takeaway? Yes/No")
member = input("Are you a member? Yes/No")
if coffee_size == "small":
    price = 2000
elif coffee_size == "medium":
    price = 3000
elif coffee_size == "large":
    price = 4000
else:
    print("Invalid Size")
if takeaway == "Yes":
    total_price = price + 200
else:
    total_price = price
if member == "Yes":
    total_price = total_price * 0.9
    print(f"Price is {total_price}")
else:
    total_price = total_price
    print(f"Price is {total_price}")