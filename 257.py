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

def add_mark(mark,marks) :
    return mark + marks

def add_student() :
    name = input("Enter Name :")
    if name not in students :
        score = int(input("Enter Initial Score :"))
        students[name] = score
        print("Student Added")
    else :
        print("Student Already Exists")

def remove_student() :
    name = input("Enter Name :")
    if name in students :
        students.pop(name)
        print("Student Removed")
    else :
        print("Student Not Found")

def goodbye() :
    print("Goodbye !")

while True :

    print("===== Student System =====")

    print("1. Show Students")
    print("2. Check Student")
    print("3. Add Marks")
    print("4. Add Student")
    print("5. Remove Studnet")
    print("6. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_student()

    elif choice == 2 :
        check_student()

    elif choice == 3 :
        name = input("Enter Name :")
        if name in students :
            mark = int(input("Enter Add Marks :"))
            marks = students.get(name)
            total = add_mark(marks,mark)
            students[name] = total
            print(total)
            print("Added Marks")
        else :
            print("Student Not Found")

    elif choice == 4 :
        add_student()

    elif choice == 5 :
        remove_student()

    elif choice == 6 :
        goodbye()
        break
