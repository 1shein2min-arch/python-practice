repairs = [
    ("iPhone 11", "SheiN", 30000, "Done"),
    ("Redmi Note 13", "Aung", 50000, "Pending"),
    ("Vivo Y55", "Mg Mg", 25000, "Done"),
    ("Samsung A52", "Ko Ko", 80000, "Pending"),
    ("Redmi 12", "Aung", 35000, "Done")
]

def new_repair() :
    model = input("Enter Model :")
    name = input("Enter Name :")
    fee = int(input("Enter Fee :"))
    status = input("Enter Status :")

    item = (model,name,fee,status)

    repairs.append(item)

def view_repairs() :
    print("--- Repair List ---")
    number = 1
    for item in repairs:
        model,name,fee,status = item
        print(f"{number} .{model} - {name} - {fee} - {status}")
        number = number + 1

def search_customer() :
    name1 = input("Enter Customer Name :")
    print("--- Search Result ---")
    found = False
    for item in repairs :
        model,name,fee,status = item

        if name1 == name :
            print(f"{model} - {name} - {fee} - {status}")
            found = True

    if found == False :
        print("Customer Not Found")


def update_fee() :
    name1 = input("Enter Customer Name :")
    model1 = input("Enter Phone Model :")
    fee1 = int(input("Enter New Fee :"))

    found = False

    for i in range(len(repairs)) :
        model,name,fee,status = repairs[i]

        if name1 == name and model1 == model :
            fee = fee1
            found = True

            repairs[i] = (model1,name1,fee1,status)

            print(repairs[i])

    if found == False :
        print("Repair Not Found")

def delete_repair() :
    name1 = input("Enter Customer Name :")
    model1 = input("Enter Phone Model :")

    found = False 
    for i in range(len(repairs)):
        model,name,fee,status = repairs[i]
        if name1 == name and model1 == model :
            found = True
            repairs.remove(repairs[i])

            print("Repair Deleted")
            print(repairs)
            break
    if found == False :
        print("Repair Not Found")

def daily_summary() :
    print(f"Total Repairs :{len(repairs)}")

    done_count = 0 
    pending_count = 0
    done_fee = 0
    pending_fee = 0
    for item in repairs:
        model,name,fee,status = item
        if status == "Done" :
            done_count = done_count + 1
            done_fee = done_fee + fee
        elif status == "Pending" :
            pending_count = pending_count + 1
            pending_fee = pending_fee + fee
    print(f"Done Repairs : {done_count}")
    print(f"Pending Repairs : {pending_count}")

    total_fee = done_fee + pending_fee

    print(f"Total Repair Fee :{total_fee}")
    print(f"Done Fee : {done_fee}")
    print(f"Pending Fee : {pending_fee}")

def repair_history() :
    name1 = input("Enter Customer Name :")
    print("--- Repair History ---")
    count = 0
    fees = 0
    found = False
    for item in repairs :
        model,name,fee,status = item
        if name1 == name :
            found = True
            print(f"{model} - {fee} - {status}")
            count = count + 1
            fees = fees + fee

    print()
    print(f"Total Repairs : {count}")
    print(f"Total Fee : {fees}")

    if found == False :
        print("Repair History Not Found")

while True :
    print("1. New Repair")
    print("2. View Repairs")
    print("3. Search Customer")
    print("4. Update Fee")
    print("5. Delete Repair")
    print("6. Daily Summary")
    print("7. Repair History")
    print("8. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        new_repair()

    elif choice == 2 :
        view_repairs()

    elif choice == 3 :
        search_customer()

    elif choice == 4 :
        update_fee()

    elif choice == 5 :
        delete_repair()

    elif choice == 6 :
        daily_summary()

    elif choice == 7 :
        repair_history()

    elif choice == 8 :
        print("Exit")
        break
    else :
        print("Invalid Choice")



        


    
    