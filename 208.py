students = {
    "Aung": 85,
    "Ko Ko": 70,
    "Hla Hla": 95 ,
    "Mg Mg" : 45
}
while True :
    print("===== Student Menu =====")
    print("1. Show Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Remove Student")
    print("5. Check Score")
    print("6. Show Passed")
    print("7. Show Failed")
    print("8. Total Score")
    print("9. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        for name,score in students.items() :
            print(f"{name} : {score}")

    elif choice == 2 :
        name= input("Enter Name :")
        if name not in students :
            score = int(input("Enter Score :"))
            students.update({name : score})
            print(f"{name} Added")
        else :
            print("Name Already Exists")

    elif choice == 3 :
        name = input("Enter Name :")
        if name in students :
            score = int(input("Enter New Score"))
            students.update({name : score})
            print(f"{name} Updated")
        else :
            print("Name Not Found")

    elif choice == 4 :
        name = input("Enter Name :")
        if name in students :
            students.pop(name)
            print(f"{name} Removed")
        else :
            print("Name Not Found")

    elif choice == 5 :
        name = input("Enter Name :")
        if name in students :
            print(f"{name} : Score {students.get(name)}")
        else :
            print("Name Not Found")

    elif choice == 6 :
        print("Passed")
        for name,score in students.items() :
            if score >= 50 :
                print(name)

    elif choice == 7 :
        print("Failed")
        for name,score in students.items() :
            if score < 50 :
                print(name)

    elif choice == 8 :
        total = 0
        for name,score in students.items() :
            total = total + score
        print(f"Total Score : {total}")

    elif choice == 9 :
        print("Goodbye!")
        break




 