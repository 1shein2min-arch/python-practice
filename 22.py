member = input("Member yes/no").lower()
price = int(input("Enter price"))
if member == "Yes" and price >=100000 :
    discount = price *0.2
    print(discount)
    total_price = price - discount
    print(f"Total Price is {total_price}")
elif member == "Yes" and price< 100000 :
    discount = price * 0.1
    print(discount)
    total_price = price - discount
    print(f"Total Price is {total_price}")
elif member == "No" and price >= 100000:
    discount = price * 0.05
    print(discount)
    total_price = price - discount
    print(f"Total Price is {total_price}")
else:
    print("No Discount")
    print(f"Total Price is {price}")