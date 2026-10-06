employees = {
    "Aung" : 450000 ,
    "Ko Ko" : 600000 ,
    "Hla Hla" : 550000 ,
    "Mg Mg" : 400000 ,
    "Su Su" : 700000
}

for name in employees :
    print(f"{name} : {employees[name]}")

print(len(employees))
if "Ko Ko" in employees :
    print("Ko Ko Found")

if "Ma Ma" in employees:
    print("Ma Ma Found")
else :
    print("Ma Ma Not Found")

employees_name = []
for name in employees :
    employees_name.append(name)

employees_name.sort()
print(employees_name)

score = []
for name in employees:
    score.append(employees[name])

score.sort()

print(f"Highest Salary :{score[-1]}")
print(f"Lowest Salary : {score[0]}")