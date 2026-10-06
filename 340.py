def load_repair() :
    repair = []

    with open("repair.txt" , "r")as file :
        data = file.readlines()

    for item in data:
        data1 = item.strip().split(",")

        model = data1[0]
        name = data1[1]
        fee = int(data1[2])
        status = data1[3]

        repair.append((model,name,fee,status))

    return repair

repair = load_repair()

def save_repair() :
    with open("repair.txt","w") as file :
        for item in repair :
            model,name,fee,status = item
            file.write(f"{model},{name},{fee},{status}\n")

    
def new_repair() :
    model = input("Enter Model :")
    name = input("Enter Name :")
    fee = int(input("Enter Fee :"))
    status = input("Enter Status :")

    repair.append((model,name,fee,status))
    save_repair()
    

def view_repair():
    count = 1
    for item in repair:
        model,name,fee,status = item
        print(f"{count}. {model} - {name} - {fee} - {status}")
        count = count + 1

def update_fee() :
    name1 = input("Enter Name :")
    model1 = input("Enter Phone :")
    fees = int(input("Enter Fee :"))
    found = False
    for i in range(len(repair)) :
        model,name,fee,status = repair[i]
        if name1 == name and model1 == model :
            found = True
            fee = fees
            repair[i] = (model,name,fee,status)
            print("Fee Update")
            save_repair()

    if found == False :
        print("Customer Not Found")

def delete_repair() :
    name1 = input("Enter Name :")
    model1 = input("Enter Phone :")
    found = False
    for i in range(len(repair)):
        model,name,fee,status = repair[i]
        if name1 == name and model1 == model :
            found = True
            repair.remove(repair[i])
            save_repair()
            break
    if found == False :
        print("Repair Not Found")    

while True:
    print("1. New Repair")
    print("2. View Repairs")
    print("3. Update Fee")
    print("4. Delete Repair")
    print("5. Save")
    print("6. Exit")  

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        new_repair()

    elif choice == 2 :
        view_repair()

    elif choice == 3 :
        update_fee()

    elif choice == 4 :
        delete_repair()

    elif choice == 5 :
        save_repair()

    elif choice == 6 :
        print("Exit")
        break
    else :
        print("Invalid Choice")









        




