employees = {
    "Aung" : 450000 ,
    "Ko Ko" : 600000 ,
    "Hla Hla" : 550000 ,
    "Mg Mg" : 400000 ,
    "Su Su" : 700000
}
print("Employees : ")
for name in employees.keys() :
    print(name)

print("Salaries :")
for salary in employees.values() :
    print(salary)

print("Employee Details")
for name,salary in employees.items() :
    print(f"{name} :{salary}")

print(f"Total Employees :{len(employees)}")

print("High Salary :")
for name,salary in employees.items():
    if salary >= 500000 :
        print(name)

print("Low Salary")
for name,salary in employees.items() :
    if salary < 500000 :
        print(name)