def load_repair() :
    repair = []

    try :
        with open("repair.txt","r") as file:
            data = file.readlines()

            for item in data:
                data1 = item.strip().split(",")

                if len(data1) != 4 :
                    continue
                
                model = data1[0]
                name = data1[1]
                try :
                    fee = int(data1[2])
                except ValueError :
                    print("Invalid Fee Data")
                    continue
                status = data1[3]

                repair.append((model,name,fee,status))

    except FileNotFoundError :
        print("Repair File Not Found")

    return repair

repair = load_repair()

def save_repair() :
    with open ("repair.txt","w") as file :
        for item in repair :
            model,name,fee,status = item

            file.write(f"{model},{name},{fee},{status}\n")

def new_repair() :
    while True :
        name = input("Enter Name :").strip()
        model = input("Enter Phone :").strip()
        if name == "" or model == "" :
            print("Name and Model Cannot Be Empty")
            continue
        break

    while True :
        try :
            fee = int(input("Enter Fee :"))
            if fee <= 0 :
                print("Fee Must Be Greater Than 0")
                continue
            break
        except ValueError:
            print("Please Enter Number")

    while True :
        status = input("Enter Status :").lower()
        if status != "done" and status != "pending" :
            print("Invalid Status")
            continue 
        break

    repair.append((model,name,fee,status))
    save_repair()
    

def view_repairs() :
    num = 1
    for item in repair :
        model,name,fee,status = item
        print(f"{num}. {model} - {name} - {fee} - {status}")
        num = num + 1

def search_customer() :
    while True :
        name1 = input("Enter Name :").strip()

        if name1 == "" :
            print("Name Cannot Be Empty")
            continue

        break
    found = False
    for item in repair :
        model,name,fee,status = item

        if name1 == name :
            found = True
            print(f"{model},{name},{fee},{status}")

    if found == False :
        print("Customer Not Found")

def update_fee() :
    while True :
        name1 = input("Enter Name :").strip()
        model1 = input("Enter Phone :").strip()
        if name1 == "" or model1 == "" :
            print("Name and Model Cannot Be Empty")
            continue
        break
    while True :
        try :
            fees = int(input("Enter Fee :"))
            if fees <= 0 :
                print("Fee Must Be Greater Than 0")
                continue
            break
        except ValueError :
            print("Please Enter Number")

    found = False
    for i in range(len(repair)) :
        model,name,fee,status = repair[i]

        if name1 == name and model1 == model :
            found = True
            fee = fees 
            repair[i] =(model,name,fee,status)
            print("Fee Updated")
            save_repair()

    if found == False :
        print("Repair Not Found")

def delete_repair() :
    while True :
        name1 = input("Enter Name :").strip()
        model1 = input("Enter Phone :").strip()
        if name1 == "" or model1 == "" :
            print("Name and Model Cannot Be Empty")
            continue
        break
    found = False

    for i in range(len(repair)) :
        model,name,fee,status = repair[i]

        if name1 == name and model1 == model :
            found = True
            repair.remove(repair[i])
            save_repair()
            break

    if found == False :
        print("Repair Not Found")

def summary() :

    done_count = 0
    pending_count = 0

    done_fee = 0
    pending_fee = 0

    for item in repair :
        model,name,fee,status = item

        if status == "Done" :
            done_count = done_count + 1
            done_fee = done_fee + fee

        elif status == "Pending" :
            pending_count = pending_count + 1
            pending_fee = pending_fee + fee

    total_count = done_count + pending_count
    total_fee = done_fee + pending_fee

    print(f"Total Repairs : {total_count}")
    print(f"Done Repair : {done_count}")
    print(f"Pending Repair : {pending_count}")

    print(f"Total Fee : {total_fee}")
    print(f"Done Fee : {done_fee}")
    print(f"Pending Fee : {pending_fee}")

def repair_history() :
    while True :
        name1 = input("Enter Name :").strip()
        if name1 == "" :
            print("Name Cannot Be Empty")
            continue
        break

    found = False
    total_repair = 0
    total_fee = 0
    for item in repair :
        model,name,fee,status = item

        if name1 == name :
            found = True
            total_repair = total_repair + 1
            total_fee = total_fee + fee

            print(f"{model},{name},{fee},{status}")
    print(f"Total Repairs : {total_repair}")
    print(f"Total Fee : {total_fee}")

    if found == False :
        print("Name Not Found")

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

    while True :
        try :
            choice = int(input("Enter Choose :"))
            if choice < 1 or choice > 9 :
                print("Invalid Choice")
                continue
            break
        except ValueError:
            print("Please Enter Number")

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
        summary()

    elif choice == 7 :
        repair_history()

    elif choice == 8 :
        save_repair()

    elif choice == 9 :
        print("Exit")
        break

    



