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
        

while True:
    print("1. New Repair")
    print("2. View Repairs")
    print("3. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        new_repair()

    elif choice == 2 :
        view_repairs()

    elif choice == 3 :
        print("Exit")
        break

    else:
        print("Invalid Choice")
