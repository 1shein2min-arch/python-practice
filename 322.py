def new_repair():
    print("New Repair")

def view_repair() :
    print("view Repair")

def goodbye() :
    print("Exit")

while True :
    print("1. New Repair")
    print("2. View Repair")
    print("3. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        new_repair()

    elif choice == 2 :
        view_repair()

    elif choice == 3 :
        goodbye()
        break

    else :
        print("Invalid Choice")