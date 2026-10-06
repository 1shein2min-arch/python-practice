students = {
    "Aung": 85,
    "Ko Ko": 70,
    "Hla Hla": 95,
    "Mg Mg": 45,
    "Su Su": 60
}


def show_students():
    print("Students:")

    for name, score in students.items():
        print(f"{name} : {score}")


def add_student():
    name = input("Enter Name : ")

    if name not in students:
        score = int(input("Enter Score : "))
        students.update({name: score})
        print(f"{name} Added")
    else:
        print("Student Already Exists")


def update_score():
    name = input("Enter Name : ")

    if name in students:
        score = int(input("Enter New Score : "))
        students.update({name: score})
        print(f"{name} Updated")
    else:
        print("Student Not Found")


def remove_student():
    name = input("Enter Name : ")

    if name in students:
        students.pop(name)
        print(f"{name} Removed")
    else:
        print("Student Not Found")


def check_student():
    name = input("Enter Name : ")

    if name in students:
        print(f"{name} : {students.get(name)}")
    else:
        print("Student Not Found")


def show_passed():
    print("Passed:")

    for name, score in students.items():
        if score >= 50:
            print(name)


def show_failed():
    print("Failed:")

    for name, score in students.items():
        if score < 50:
            print(name)


def show_highest():
    highest_score = 0
    highest_name = ""

    for name, score in students.items():
        if score > highest_score:
            highest_score = score
            highest_name = name

    print("Highest:")
    print(f"{highest_name} : {highest_score}")


def show_lowest():
    lowest_score = 999999
    lowest_name = ""

    for name, score in students.items():
        if score < lowest_score:
            lowest_score = score
            lowest_name = name

    print("Lowest:")
    print(f"{lowest_name} : {lowest_score}")


def total_score():
    total = 0

    for score in students.values():
        total = total + score

    print(f"Total Score: {total}")


def total_students():
    print(f"Total Students: {len(students)}")


def sorted_names():
    names = []

    for name in students.keys():
        names.append(name)

    names.sort()

    print("Sorted Names:")
    print(names)


def goodbye():
    print("Goodbye!")


while True:

    print()
    print("===== Student Management =====")

    print("1. Show Students")
    print("2. Add Student")
    print("3. Update Score")
    print("4. Remove Student")
    print("5. Check Student")
    print("6. Show Passed")
    print("7. Show Failed")
    print("8. Show Highest")
    print("9. Show Lowest")
    print("10. Total Score")
    print("11. Total Students")
    print("12. Sorted Names")
    print("13. Exit")

    choice = int(input("Enter Choose : "))

    if choice == 1:
        show_students()

    elif choice == 2:
        add_student()

    elif choice == 3:
        update_score()

    elif choice == 4:
        remove_student()

    elif choice == 5:
        check_student()

    elif choice == 6:
        show_passed()

    elif choice == 7:
        show_failed()

    elif choice == 8:
        show_highest()

    elif choice == 9:
        show_lowest()

    elif choice == 10:
        total_score()

    elif choice == 11:
        total_students()

    elif choice == 12:
        sorted_names()

    elif choice == 13:
        goodbye()
        break

    else:
        print("Invalid Choice")