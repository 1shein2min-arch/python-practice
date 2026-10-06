repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]


def add_repair(repairs,model,name,fee,status) :
    repair = {
        "model" : model,
        "name" : name,
        "fee" : fee,
        "status" : status
    }
    repairs.append(repair)

def view_repairs(repairs) :
    for repair in repairs :
        print(f"{repair['model']} - {repair['name']} - {repair['fee']} - {repair['status']}")

def search_customer(repairs,name) :
    for repair in repairs :
        if repair["name"] == name :
            print(f"{repair['model']} - {repair['name']} - {repair['fee']} - {repair['status']}")

def update_fee(repairs,name,model,new_fee) :
    for repair in repairs :
        if repair["name"] == name and repair["model"] == model :
            repair["fee"] = new_fee
            break

def delete_repair(repairs,name,model) :
    for repair in repairs :
        if repair["name"] == name and repair["model"] == model :
            repairs.remove(repair)
            break

def update_status(repairs,name,model,status) :
    for repair in repairs :
        if repair["name"] == name and repair["model"] == model:
            repair["status"] = status
            break

def summary(repairs) :
    total_fee = 0
    done_repairs = 0
    pending_repairs = 0

    for repair in repairs :
        total_fee = total_fee + repair["fee"]

        if repair["status"] == "Done" :
            done_repairs = done_repairs + 1

        elif repair["status"] == "Pending" :
            pending_repairs = pending_repairs + 1

    total_repairs = done_repairs + pending_repairs
    
    print(f"Total Repairs : {total_repairs}")
    print(f"Total Fee : {total_fee}")
    print(f"Done Repairs : {done_repairs}")
    print(f"Pending Repairs : {pending_repairs}")

while True :
    print("===== Repair Management =====")
    print("1. Add Repair")
    print("2. View Repairs")
    print("3. Search Customer")
    print("4. Update Fee")
    print("5. Delete Repair")
    print("6. Update Status")
    print("7. Summary")
    print("8. Exit")

    while True :
        try :
            choice = int(input("Enter Choose :"))
            break
        except ValueError:
            print("Please Enter Number")

    if choice == 1 :
        model = input("Enter Model :")
        name = input("Enter Name :")

        while True :
            try :
                fee = int(input("Enter Fee :"))
                break
            except ValueError :
                print("Please Enter Number")

        status = input("Enter Status :")

        add_repair(repairs,model,name,fee,status)

    elif choice == 2 :
        view_repairs(repairs)

    elif choice == 3 :
        name = input("Enter Name :")
        search_customer(repairs,name)

    elif choice == 4 :
        name = input("Enter Name :")
        model = input("Enter Model :")
        while True :
            try:
                new_fee = int(input("Enter Fee :"))
                break
            except ValueError :
                print("Fee Must Be Number")
        update_fee(repairs,name,model,new_fee)

    elif choice == 5 :
        name = input("Enter Name :")
        model = input("Enter Model :")
        delete_repair(repairs,name,model)

    elif choice == 6:
        name = input("Enter Name :")
        model = input("Enter Model :")
        status = input("Enter Status :")
        update_status(repairs,name,model,status)

    elif choice == 7 :
        summary(repairs)

    elif choice == 8 :
        print("Exit")
        break

    else :
        print("Invalid Choice")



