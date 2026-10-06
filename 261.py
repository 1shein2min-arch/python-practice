students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 60,
    "Su Su": 35
}
def show_result(score) :
    if score >= 50 :
        return "Passed"
    else :
        return "Failed"
 
def count():
    passed = 0
    failed = 0 
    for name,score in students.items() :
        if score >= 50 :
            passed += 1
        else :
            failed += 1 

    print(f"Pass Students :{passed}")
    print(f"Failed Students : {failed}")

def high_score() :
    for name,score in students.items() :
        if score >= 90 :
            print(f"{name} : {score}")

def goodbye() :
    print("Goodbye !")


while True :

    print("===== Student Analyzer =====")

    print("1. Show Results")
    print("2. Count Passed/Failed")
    print("3. Show High Score")
    print("4. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        name = input("Enter Name :")
        if name in students :
            score = students.get(name)
            print(f"{name} : {score} -{show_result(score)}")
            
        else :
            print("Student Not Found")

    elif choice == 2 :
        count()

    elif choice == 3 :
        high_score()

    elif choice == 4 :
        goodbye()
        break
    else :
        print("Invalid Choice")

