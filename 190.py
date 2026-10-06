employees = {
    "Aung" : 450000 ,
    "Ko Ko" : 650000 ,
    "Hla Hla" : 550000 ,
    "Mg Mg" : 400000,
    "Su Su" : 750000
}
print("Employees :")
for name in employees.keys() :
    print(name)

print("Salaries :")
for salary in employees.values() :
    print(salary)

high_salary = 0
high_name = ""

low_salary = 999999
low_name = ""

print("High Salary :")
for name,salary in employees.items() :
    if salary > high_salary :
        high_salary = salary
        high_name = name

        print(name)

print("Low Salary :")
for name,salary in employees.items() :
    if salary < low_salary :
        low_salary = salary
        low_name = name

        print(name)

total = 0
for salary in employees.values() :
    total = total + salary
print(f"Total Salary :{total}")

names = []
for name in employees.keys() :
    names.append(name)

names.sort()
print("Sorted Names :")
print(names)

highest_name = ""
highest_salary = 0

lowest_name = ""
lowest_salary = 999999

for name,salary in employees.items() :
    if salary > highest_salary :
        highest_salary = salary
        highest_name = name

    if salary < lowest_salary :
        lowest_salary = salary
        lowest_name = name

print(f"Highest : {highest_name} : {highest_salary}")
print(f"Lowest : {lowest_name} : {lowest_salary}")