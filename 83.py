child_count = 0
adult_count = 0
senior_count = 0

total = 0
ticket_count = 0

while True :
    age = int(input("Enter age"))
    if age == -1 :
        print("Exit")
        break
    elif age <= 0 :
        print("Invalid Age")
        continue
    elif age < 13 :
        price = 3000
        discount = price * 0
        child_count = child_count + 1  

    elif age < 60 :
        price = 5000
        discount = price * 0.1
        adult_count = adult_count + 1

    else :
        price = 3500
        discount = price * 0.05
        senior_count = senior_count + 1

    quantity = int(input("Enter Quantity"))
    if quantity <= 0 :
        print("Invalid Quantity")
        continue
    else :
        total_price = price * quantity
        total_discount = quantity * discount
        final_bill = total_price - total_discount
    print(f"Age = {age}")
    print(f"Quantity = {quantity}")
    print(f"Price = {price}")

    print(f"Subtotal = {total_price}")
    print(f"Discount = {total_discount}")
    print(f"Final Bill = {final_bill}")

    total = total + final_bill
    ticket_count = ticket_count + quantity

print(f"Child Count : {child_count}")
print(f"Adult Count : {adult_count}")
print(f"Senior Count : {senior_count}")

print(f"Total Sales : {total}")
print(f"Ticket Count : {ticket_count}")

if ticket_count > 0 :
    average = total/ticket_count 

    print(f"Average ticket Price : {average}")

    if average >= 5000 :
        print("Expensive Tickets")
    elif average >= 3500 :
        print("Normal Tickets")
    else :
        print("Cheap Tickets")
else :
    print("No ticket Sale")

    






