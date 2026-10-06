import json

try:
    with open("repair.json","r") as file :
        repairs = json.load(file)

except FileNotFoundError:
    repairs = []

except json.JSONDecodeError :
    repairs = []

def add_repair(repairs,model,name,fee,status) :
    repair = {
        "model" : model ,
        "name" : name ,
        "fee" : fee,
        "status" : status
    }

    repairs.append(repair)
    save_data(repairs)

def save_data(repairs) :

    with open("repair.json","w") as file :
        json.dump(repairs,file,indent=4)

def update_fee(repairs,model,name,fee) :
    for repair in repairs:
        if repair["model"] == model and repair["name"] == name :
            repair["fee"] = fee
            save_data(repairs)
            break

def delete_repair(repairs,model,name) :
    for repair in repairs :
        if repair["model"] == model and repair["name"] == name :
            repairs.remove(repair)
            save_data(repairs)
            break

def update_status(repairs,model,name,status) :
    for repair in repairs :
        if repair["model"] == model and repair["name"] == name :
            repair["status"] = status
            save_data(repairs)
            break

def view_repairs(repairs):
    for repair in repairs :
        print(f"{repair["model"]} - {repair["name"]} - {repair["fee"]} - {repair["status"]}")

def search_customer(repairs,model,name) :
    for repair in repairs :
        if repair["model"] == model and repair["name"] == name :
            print(f"{repair["model"]} - {repair["name"]} - {repair["fee"]} - {repair["status"]}")
            
 
while True :

    print("===== Repair Management =====")

    print("1. Add Repair")
    print("2. View Repairs")
    print("3. Search Customer")
    print("4. Update Fee")
    print("5. Delete Repair")
    print("6. Update Status")
    print("7. Exit")

    while True :
        try :
            choice = int(input("Enter Choose :"))
            break
        except ValueError :
            print("Please Enter Number")

    if choice == 1 :
        model = input("Enter Model :")
        name = input("Enter Name :")
        while True :
            try :
                fee = int(input("Enter Fee :"))
                if fee <= 0 :
                    print("Fee Must Be Greater Than 0")
                    continue
                break
            except ValueError :
                print("Fee Must Be Number")
        status = input("Enter Status :")
        add_repair(repairs,model,name,fee,status)

    elif choice == 2 :
        view_repairs(repairs)

    elif choice == 3 :
        model = input("Enter Model :")
        name = input("Enter Name :")
        search_customer(repairs,model,name)

    elif choice == 4 :
        model = input("Enter Model :")
        name = input("Enter Name :")
        while True :
            try :
                fee = int(input("Enter Fee :"))
                if fee <= 0 :
                    print("Fee Must Be Greater Than 0")
                    continue
                break
            except ValueError :
               print("Fee Must Be Number")
        update_fee(repairs,model,name,fee)

    elif choice == 5 :
        model = input("Enter Model :")
        name = input("Enter Name :")
        delete_repair(repairs,model,name)

    elif choice == 6 :
        model = input("Enter Model :")
        name = input("Enter Name :")
        status = input("Enter Status :")
        update_status(repairs,model,name,status)

    elif choice == 7 :
        print("Goodbye !")
        break

    else :
        print("Invalid Choice")
