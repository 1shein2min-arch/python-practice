students = {
    "Aung" : 85,
    "Ko Ko" : 45,
    "Hla Hla" : 95,
    "Mg Mg" : 60,
    "Su Su" : 35
}

print("===== Student Management =====")

print("Students :")
for name,score in students.items() :
    print(f"{name} : {score}")

print(f"Total Students : {len(students)}")

print("Passed :")
for name,score in students.items() :
    if score >= 50 :
        print(name)

print("Failed :")
for name,score in students.items() :
    if score < 50 :
        print(name)

total = 0
for score in students.values() :
    total =total + score

print(f"Total Score :{total}")

highest_score = 0
highest_name = ""

lowest_score = 99
lowest_name = ""

for name,score in students.items() :
    if score > highest_score :
        highest_score = score
        highest_name = name
    if score < lowest_score :
        lowest_score = score
        lowest_name = name

print(f"Highest : {highest_name} : {highest_score}")
print(f"Lowest : {lowest_name} : {lowest_score}")

names = []
for name in students.keys() :
    names.append(name)

names.sort()

print("Sorted Names :")
print(names)

print(f"Aung Score : {students.get('Aung')}")
print(f"Ma Ma Score : {students.get('Ma Ma' , 0)}")