def load_repair() :
    repair = []
    with open ("repair.txt","r") as file :
        data = file.readlines()

        for line in data :
            data1 = line.strip().split(",")

            model = data1[0]
            name = data1[1]
            fee = int(data1[2])
            status = data1[3]

            repair.append((model,name,fee,status))

    return repair

repair = load_repair()

def save_repair() :
    with open ("repair.txt","w") as file :
        for item in repair:
            model,name,fee,status = item
            file.write(f"{model},{name},{fee},{status}\n")

def new_repair() :
    name1 = input("Enter Name :")
    model1 = input("Enter Phone :")
    fee1 = int(input("Enter Fee :"))
    status1 = input("Enter Status :")

    repair.append((model1,name1,fee1,status1))
    save_repair()

def view_repair() :
    count = 1
    for item in repair:
        model,name,fee,status = item
        print(f"{count}. {model} - {name} - {fee} - {status}")
        count = count + 1

def search_customer() :
    name1 = input("Enter Name :")
    found = False
    for item in repair :
        model,name,fee,status = item

        if name1 == name :
            found = True 
            print(f"Model : {model}")
            print(f"Name : {name}")
            print(f"Fee : {fee}")
            print(f"Status : {status}")

    if found == False :
        print("Customer Not Found")

def update_fee() :
    name1 = input("Enter Name :")
    model1 = input("Enter Phone :")
    fee1 = int(input("Enter Fee :"))
    found = False 
    for i in range(len(repair)):
        model,name,fee,status = repair[i]

        if name1 == name and model1 == model :
            found = True
            fee = fee1

            repair[i] = (model,name,fee,status)
            save_repair()
    if found == False :
        print("Customer Not Found")

def delete_repair() :
    name1 = input("Enter Name :")
    model1 = input("Enter Model :")
    found = False

    for i in range(len(repair)):
        model,name,fee,status = repair[i]
        if name1 == name and model1 == model :
            found = True
            repair.remove(repair[i])
            save_repair()
            break
    if found == False:
        print("Repair Not Found")

def total() :
    print("---- Daily Summary ----")

    done_count = 0
    pending_count = 0
    done_fee = 0
    pending_fee = 0
    for item in repair :
        model,name,fee,status = item
        if status == "Done" :
            done_fee = done_fee + fee
            done_count = done_count + 1
        elif status == "Pending" :
            pending_fee = pending_fee + fee
            pending_count = pending_count + 1

    total_repair = done_count + pending_count
    total_fee = done_fee + pending_fee

    print(f"Total Repairs : {total_repair}")
    print(f"Done Repairs : {done_count}")
    print(f"Pending Repairs : {pending_count}")
    print()
    print(f"Total Repair Fee : {total_fee}")
    print(f"Done Fee : {done_fee}")
    print(f"Pending Fee : {pending_fee}")

def repair_history() :
    name1 = input("Enter Name :")
    count = 0
    total_fee = 0
    for item in repair :
        model,name,fee,status = item
        if name1 == name :
            print(f"{model},{name},{fee},{status}")
            count = count + 1
            total_fee = total_fee + fee
    print(f"Total Repair : {count}")
    print(f"Total Fee : {total_fee}")

while True :

    print("1. New Repair")
    print("2. View Repairs")
    print("3. Search Customer")
    print("4. Update Fee")
    print("5. Delete Repair")
    print("6. Daily Summary")
    print("7. Repair History")
    print("8. Save")
    print("9. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        new_repair()

    elif choice == 2 :
        view_repair()

    elif choice == 3 :
        search_customer()

    elif choice == 4 :
        update_fee()

    elif choice == 5 :
        delete_repair() 

    elif choice == 6 :
        total()

    elif choice == 7 :
        repair_history()

    elif choice == 8 :
        save_repair() 

    elif choice == 9 :
        print("Exit")
        break

    else :
        print("Invalid Choice")        








