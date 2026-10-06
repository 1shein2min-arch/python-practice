child_count = 0
adult_count = 0
senior_count = 0

total = 0
ticket_count = 0
while True :
    name = input("Enter Name")
    length = len(name)
    if length < 4 :
        print("Name Too Short")
    elif length < 10 :
        print("Valid Name")
    else :
        print("Name Too Long")

    age = int(input("Enter Age"))
    if age == -1 :
        print("Exit")
        break
    elif age < 0 :
        print("Invalid Age")
        continue
    elif age == 0 :
        print("Invalid Age")
        continue
    else :
        if age < 13 :
            price = 3000
            child_count = child_count + price
        elif age< 60 :
            price = 5000
            adult_count = adult_count + price
        else :
            price = 3500
            senior_count = senior_count + price
        quantity = int(input("Enter Quantity"))
        if quantity <=0 :
            print("Invalid Quantity")
            continue
        else :
            total_price = price * quantity
    total = total + total_price
    ticket_count = ticket_count + quantity
    average = total/ticket_count
    if average < 3500 :
        print("Cheap")
    elif average < 5000 :
        print("Normal")
    else :
        print("Expensive")



