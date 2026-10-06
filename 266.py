students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 60
}

def show_student() :
    for name,score in students.items() :
        print(f"{name} : {score}")

def check_student() :
    name = input("Enter Name :")
    if name in students :
        print(f"Score : {students.get(name)}")
    else :
        print("Student Not Found")

def add_student() :
    name = input("Enter Name :")
    if name not in students :
        score = int(input("Enter Score :"))
        students[name] = score
        print("Add Student")
    else :
        print("Student Already Exists")

def update_score () :
    name = input("Enter Name :")
    if name in students :
        score = int(input("Enter Score :"))
        students[name] = score 
        print("Updated Score")
    else :
        print("Student Not Found")

def remove_student() :
    name = input("Enter Name :")
    if name in students :
        students.pop(name)
        print("Student Removed")
    else :
        print("Student Not Found")

def add_mark(score,mark) :
    return score + mark

def passed() :
    for name,score in students.items() :
        if score >= 50 :
            print(f"{name} : {score}")

def high() :
    high_score = 0
    high_name = ""
    for name,score in students.items():
        if score > high_score:
            high_score = score
            high_name = name
    print(f"High Name  {high_name} : High Score {high_score}")

def count_student() :
    count = 0 
    for name,score in students.items() :
        count += 1
    print(f"Student Count : {count}")

def goodbye() :
    print("Goodbye !")

while True :

    print("1. Show Students")
    print("2. Check Student")
    print("3. Add Student")
    print("4. Update Score")
    print("5. Remove Student")
    print("6. Add Marks")
    print("7. Show Passed")
    print("8. Show High Score")
    print("9. Count Students")
    print("10. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_student()

    elif choice == 2 :
        check_student()

    elif choice == 3 :
        add_student()

    elif choice == 4 :
        update_score()

    elif choice == 5 :
        remove_student()

    elif choice == 6 :
        name = input("Enter Name :")
        if name in students:
            score = students.get(name)
            mark = int(input("Enter Marks :"))
            total = add_mark(score,mark)
            students[name] = total
            print("Marks Added")
        else :
            print("Student Not Found")

    elif choice == 7 :
        passed()

    elif choice == 8 :
        high()

    elif choice == 9 :
        count_student()

    elif choice == 10 :
        goodbye()
        break

    else :
        print("Invalid Choice")