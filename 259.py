employees = {
    "Aung" : 500000 ,
    "Ko Ko" : 800000,
    "Hla Hla" : 650000,
    "Su Su" : 1200000
}

def show_employees() :
    for name,salary in employees.items() :
        print(f"{name} : {salary}")

def check_salary():
    name = input("Enter Name :")
    if name in employees:
        print(f"Salary : {employees.get(name)}")
    else :
        print("Employee Not Found")

def add_employee():
    name = input("Enter Name :")
    if name not in employees:
        salary = int(input("Enter Initial Salary :"))
        employees[name] = salary
        print("Employee Added")
    else :
        print("Employee Already Exists")

def update_salary() :
    name = input("Enter Name :")
    if name in employees :
        salary = int(input("Enter New Salary :"))
        employees[name] = salary
        print("Salary Updated")
    else :
        print("Employee Not Found")

def increase_salary(salary,percent) :
    increase = salary * percent/100
    return increase

def remove_employee ():
    name = input("Enter Name :")
    if name in employees :
        employees.pop(name)
        print("Employee Removed")
    else :
        print("Employee Not Found")

def check_level(salary) :
    if salary < 500000 :
        return "Junior"
    elif salary < 1000000 :
        return "Mid-Level"
    else :
        return "Senior"

def goodbye() :
    print("Goodbye !")

while True :
    print("===== Employee System =====")

    print("1. Show Employees")
    print("2. Check Salary")
    print("3. Add Employee")
    print("4. Update Salary")
    print("5. Increase Salary")
    print("6. Remove Employee")
    print("7. Check Employee Level")
    print("8. Exit")

    choice = int(input("Enter Choose :"))

    if choice == 1 :
        show_employees()

    elif choice == 2 :
        check_salary()

    elif choice == 3 :
        add_employee()

    elif choice == 4 :
        update_salary()

    elif choice == 5 :
        name = input("Enter Name :")
        if name in employees :
            salary = employees.get(name) 
            percent = int(input("Enter Percent"))
            increase = increase_salary(salary,percent)
            total = increase + salary 
            employees[name] = total

            print(f"Old Salary : {salary}")
            print(f"Increase : {increase}")
            print(f"New Salary : {total}")

        else :
            print("Employee Not Found")

    elif choice == 6 :
        remove_employee()

    elif choice == 7:
        name = input("Enter Name :")

        if name in employees:
            salary = employees.get(name)
            print(f"Salary : {salary}")
            print(f"Level : {check_level(salary)}")
        else:
            print("Employee Not Found")

    elif choice == 8 :
        goodbye()
        break 

    else:
        print("Invalid Choice")