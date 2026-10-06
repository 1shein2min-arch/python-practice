print("1. Search Phone")
print("2. Search Customer")

choice = input("Enter Choose :")

if choice == "1":
    phone2 = input("Enter Phone :")
    found = False

    with open("repair.txt", "r") as file:
        for line in file:
            data = line.split("|")

            name = data[0].strip()
            phone = data[1].strip()
            problem = data[2].strip()

            if phone2 == phone:
                print(f"Customer : {name}")
                print(f"Phone : {phone}")
                print(f"Problem : {problem}")
                print()

                found = True

    if found == False:
        print("Record Not Found")

elif choice == "2":
    name2 = input("Enter Customer :")
    found = False

    with open("repair.txt", "r") as file:
        for line in file:
            data = line.split("|")

            name = data[0].strip()
            phone = data[1].strip()
            problem = data[2].strip()

            if name2 == name:
                print(f"Customer : {name}")
                print(f"Phone : {phone}")
                print(f"Problem : {problem}")
                print()

                found = True

    if found == False:
        print("Record Not Found")

else:
    print("Invalid Choice")