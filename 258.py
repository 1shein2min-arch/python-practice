patients = {
    "Aung": 25,
    "Ko Ko": 40,
    "Hla Hla": 30,
    "Su Su": 55
}

def show_patients():
    for name,age in patients.items() :
        print(f"{name} : {age}")

def check_patient():
    name = input("Enter Name :")
    if name in patients :
        print(f"{name} : {patients.get(name)}")
    else:
        print("Patient Not Found")

def add_patient() :
    name = input("Enter Name :")
    if name not in patients:
        age = int(input("Enter Age :"))
        patients[name] = age
        print("Patient Added")
    else :
        print("Patient Already Exists")

def update_age () :
    name = input("Enter Name :")
    if name in patients :
        old_age = patients.get(name)
        new_age = int(input("Enter New Age :"))
        patients[name] = new_age
        print(f"Old Age :{old_age}")
        print(f"New Age :{new_age}")
    else:
        print("Patient Not Found")

def remove_patient() :
    name = input("Enter Name :")
    if name in patients :
        patients.pop(name)
        print("Patient removed")
    else :
        print("Patient Not Found")

def check_age(age) :
    if age < 18 :
        return "Child"
    elif age < 60 :
        return "Adult"
    else :
        return "Senior"

def goodbye() :
    print("Goodbye !")

while True :
    print("===== Clinic System =====")

    print("1. Show Patients")
    print("2. Check Patient")
    print("3. Add Patient")
    print("4. Update Age")
    print("5. Remove Patient")
    print("6. Check Age Group")
    print("7. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_patients()

    elif choice == 2 :
        check_patient()

    elif choice == 3 :
        add_patient()

    elif choice == 4 :
        update_age()

    elif choice == 5 :
        remove_patient()

    elif choice == 6 :
        name = input("Enter Name :")
        if name in patients :
            age = patients.get(name)
            print(check_age(age))
            
        else :
            print("Patient Not Found")

    elif choice == 7 :
        goodbye()
        break

    else :
        print("Invalid Choice")
