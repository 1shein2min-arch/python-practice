budget = 0
mid_range = 0
premium = 0

total = 0
phone_count = 0

while True :
    model = input("Enter Phone Model : ")
    if model == "exit" :
        print("Exit")
        break
    length = len(model)
    if length < 3 :
        print("Model Name Too Short")
        continue

    price = int(input("Enter Price :"))
    if price <= 0 :
        print("Invalid Price")
        continue
    else :
        if price < 300000 :
            discount = price * 0.05
            budget = budget + 1

        elif price < 50000 :
            discount = price * 0.1
            mid_range = mid_range + 1

        else :
            discount = price * 0.15
            premium = premium + 1

    quantity = int(input("Enter Quantity"))
    if quantity <= 0 :
        print("Invalid Quantity")
        continue

    else :
        subtotal = price * quantity
        subdiscount = discount * quantity
        final_bill = subtotal - subdiscount

    total = total + final_bill
    phone_count = phone_count + quantity

    print(f"Model = {model}")
    print(f"Price = {price}")
    print(f"Quantity = {quantity}")

    print(f"Subtotal = {subtotal}")
    print(f"Discount = {subdiscount}")
    print(f"Final Bill = {final_bill}")

print(f"Budget Count : {budget}")
print(f"Mid-range Count : {mid_range}")
print(f"Premium Count : {premium}")

print(f"Total Sales : {total}")
print(f"Total Phone Quantity : {phone_count}")

if phone_count > 0 :
    average = total/phone_count
    print(f"Average Price Per Phone : {average}")

    if average >= 500000 :
        print("Premium Market")

    elif average >= 300000 :
        print("Mid-range Market")

    else :
        print("Budget Market")

else :
    print("No Phone Sales")










    
