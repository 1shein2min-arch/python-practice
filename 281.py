students = {}

def add_student() :
    name = input("Enter Name :")
    score = int(input("Enter Score :"))
    students[name] = score
    print("Student Added")

def show_students () :
    for name,score in students.items() :
        print(f"{name} : {score}")

def search_student () :
    name = input("Enter Name :")
    if name in students :
        print(f"{name} : {students.get(name)}")
    else :
        print("Student Not Found")

def goodbye() :
    print("Goodbye !")

while True:

    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    try :
        choice = int(input("Enter Choose :"))

        if choice == 1 :
            add_student()

        elif choice == 2 :
            show_students()

        elif choice == 3 :
            search_student()

        elif choice == 4 :
            goodbye()
            break

        else :
            print("Invalid Choice")

    except ValueError :
        print("Please Enter A Valid Choice")