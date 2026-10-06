students = {
    "Aung Aung" : 85 ,
    "Ko Ko" : 70 ,
    "Hla Hla" : 95 ,
    "Mg Mg" : 60 ,
    "Su Su" : 85
}

for name in students :
    print(f"{name} : {students[name]}")

print(f"Total Students :{len(students)}")

if "Hla Hla" in students :
    print("Hla Hla Found")

if "Ma Ma" in students :
    print("Ma Ma Found")
else :
    print("Ma Ma Not Found")

names = []
for name in students :
    names.append(name)

names.sort()

print("Names :")
print(names)

score = []
for name in students :
    score.append(students[name])

score.sort()

print("Scores :")
print(score)

print(f"Highest Score : {score[-1]}")
print(f"Lowest Score : {score[0]}")

print(f"85 Count : {score.count(85)}")

