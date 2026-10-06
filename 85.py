standard_count = 0
deluxe_count = 0
suite_count = 0

total = 0
night_count = 0

while True :
    name = input("Enter customer name :").lower()
    if name == "exit" :
        print("Exit")
        break
    length = len(name)
    if length < 3 :
        print("Name Too Short")
        continue
    room = input("Enter Room Type standard/deluxe/suite :").lower()
    if room == "standard" :
        price = 30000
        discount = price * 0
        standard_count = standard_count + 1

    elif room == "deluxe" :
        price = 50000
        discount = price * 0.1
        deluxe_count = deluxe_count + 1

    elif room == "suite":
        price = 80000
        discount = price * 0.15
        suite_count = suite_count + 1

    else :
        print("Invalid Room Type")
        continue

    night = int(input("Enter Night :"))
    if night <= 0 :
        print("Invalid Nights")
        continue

    
    subtotal = price * night
    subdiscount = discount * night
    final_bill = subtotal - subdiscount

    print(f"Room = {room}")
    print(f"Price = {price}")
    print(f"Nights = {night}")

    print(f"Subtotal = {subtotal}")
    print(f"Discount = {discount}")
    print(f"Final Bill = {final_bill}")
    

    total = total + final_bill
    night_count = night_count + night

if night_count > 0 :
    average = total/night_count

    if average >= 70000 :
        print("Luxury Booking")

    elif average >= 40000 :
        print("Normal Booking")

    else :
        print("Budget Booking")

    print(f"Standard Count : {standard_count}")
    print(f"Deluxe Count : {deluxe_count}")
    print(f"Suite Count : {suite_count}")

    print(f"Total Sales : {total}")
    print(f"Total Nights : {night_count}")
    print(f"Average Cost Per Night : {average}")
        

else :
    print("There is no Booking")



    

    








