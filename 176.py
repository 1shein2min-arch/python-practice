students = {
    "Aung Aung": 85,
    "Ko Ko": 70,
    "Hla Hla": 95,
    "Mg Mg": 60
}
for name , score in students.items() :
    print(name,score)

score = []
for name in students :
    score.append(students[name])

score.sort()
print(f"Highest : {score[-1]}")
print(f"Lowest : {score[0]}")