name = input("Enter your Name")
price = int(input("Enter price"))
member = input("Is member (yes/no)").lower()
coupon = input("Enter coupon SAVE10 or Not")
order = input("First order (yes/no)")
if price<50000:
    print("No Discount")
elif price>=50000 and member == "yes" or coupon == "SAVE10":
    discount = price*0.1
    total_price = price - discount
    if order == "yes":
        extra_discount = total_price*0.05
        final_price = total_price - extra_discount
        print(f"Final price: {final_price}")
    else:
        print(f"Final price: {total_price}")
else:
    print(f"Final price: {price}")
    




