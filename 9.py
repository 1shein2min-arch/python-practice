menu = int(input("Enter Menu 1,2,3"))
quantity = int(input("Enter your amount"))
total_price = 5*quantity
if menu not in (1,2,3):
    print("invalid menu")
if quantity < 5:
    print(total_price)
elif quantity >=5:
    print(total_price-2)
else :
    print("invalid")