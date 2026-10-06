patients = {
    "Aung": 25,
    "Ko Ko": 65,
    "Hla Hla": 40,
    "Su Su": 72,
    "Mg Mg": 17
}

def show_patient():
    for name, age in patients.items():
        print(f"{name} : {age}")

def add_patient():
    name = input("Enter Name :")
    if name not in patients:
        age = int(input("Enter Age :"))
        patients[name] = age
        print("Patient Added")
    else:
        print("Patient Already Exists")

def update_age():
    name = input("Enter Name :")
    if name in patients:
        age = int(input("Enter Age :"))
        patients[name] = age
        print("Age Updated")
    else:
        print("Patient Not Found")

def remove_patient():
    name = input("Enter Name :")
    if name in patients:
        patients.pop(name)
        print("Patient Removed")
    else:
        print("Patient Not Found")

def age_group(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

def count_group():
    child_count = 0
    adult_count = 0
    senior_count = 0

    for name, age in patients.items():
        if age < 18:
            child_count += 1
        elif age < 60:
            adult_count += 1
        else:
            senior_count += 1

    print(f"Child Count : {child_count}")
    print(f"Adult Count : {adult_count}")
    print(f"Senior Count : {senior_count}")

def oldest_patient():
    old = 0
    old_name = ""

    for name, age in patients.items():
        if age > old:
            old = age
            old_name = name

    print(f"Oldest Patient : {old_name} : {old}")

def goodbye():
    print("Goodbye !")

while True:

    print("===== Clinic System =====")

    print("1. Show Patients")
    print("2. Add Patient")
    print("3. Update Age")
    print("4. Remove Patient")
    print("5. Age Group")
    print("6. Count Group")
    print("7. Oldest Patient")
    print("8. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1:
        show_patient()

    elif choice == 2:
        add_patient()

    elif choice == 3:
        update_age()

    elif choice == 4:
        remove_patient()

    elif choice == 5:
        for name, age in patients.items():
            print(f"{name} : {age_group(age)}")

    elif choice == 6:
        count_group()

    elif choice == 7:
        oldest_patient()

    elif choice == 8:
        goodbye()
        break

    else:
        print("Invalid Choice")