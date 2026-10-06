employees = {
    "Aung": 450000,
    "Ko Ko": 800000,
    "Hla Hla": 1200000,
    "Mg Mg": 650000,
    "Su Su": 1500000
}

def show_employees() :
    for name,salary in employees.items() :
        print(f"{name} : {salary}")

def check_salary (salary) :
    if salary >= 1000000 :
        return "Senior"
    elif salary > 500000 :
        return "Mid_Level"
    else :
        return "Junior"

def count() :
    junior = 0
    mid = 0 
    senior = 0 
    for name,salary in employees.items() :
        if salary >= 1000000 :
            senior += 1
        elif salary > 500000 :
            mid += 1
        else :
            junior += 1

    print(f"Junior Employees :{junior}")
    print(f"Mid-Level Employees : {mid}")
    print(f"Senior Employees : {senior}")

def show_high() :
    for name,salary in employees.items() :
        if salary >= 1000000 :
            print(f"{name} : {salary}")


def increase_percent() :
    name = input("Enter Name :")
    if name in employees :
        percent = int(input("Enter Percent :"))
        old_salary = employees.get(name)
        increase = old_salary * percent/100
        new_salary = old_salary + increase
        employees[name] = new_salary

        print(f"Old Salary : {old_salary}")
        print(f"Increase : {increase}")
        print(f"New Salary : {new_salary}")
    else :
        print("Employee Not Found")

def goodbye() :
    print("Goodbye !")

while True :

    print("===== Employee Analyzer =====")

    print("1. Show Employees")
    print("2. Check Salary Level")
    print("3. Count Salary Levels")
    print("4. Show High Salary")
    print("5. Increase Salary")
    print("6. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_employees()

    elif choice == 2 :
        name = input("Enter Name :")
        if name in employees :
            salary = employees.get(name)
            print(check_salary(salary))
        else :
            print("Employee Not Found")

    elif choice == 3 :
        count()

    elif choice == 4 :
        show_high()

    elif choice == 5 :
        increase_percent()

    elif choice == 6 :
        goodbye()
        break
    else :
        print("Invalid Choice")



    

