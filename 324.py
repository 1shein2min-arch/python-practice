repair = []

def new_repair() :
    name = input("Name :")
    phone = input("Phone :")
    fee = int(input("Fee :"))

    return name,phone,fee

def view_repair() :
    print(new_repair())
    
while True:

    print("1. New Repair")
    print("2. View Repair")
    print("3. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        data = new_repair()
        repair.append(data)

    elif choice == 2 :
        view_repair()

    elif choice == 3 :
        print("Exit !")
        break

    else:
        print("Invalid Choice")