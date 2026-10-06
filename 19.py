age = int(input("Enter your age :"))
day = input("Is today a weekend ?(yes/no)").lower()
if age<=0:
    print("Invalid age")
elif age<5:
    price = 0 
    print("Free")
elif age<=12:
    price = 3000
    print("3000ks")
elif age<=59:
    price = 6000
    print("6000ks")
else :
    price = 4000
    print("4000ks")
if day == "Yes":
    total_price = price + 1000
    print(f"Total Price is {total_price}")
else:
    print(f"Total price is {price}")
 

