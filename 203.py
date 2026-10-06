students = {
    "Aung" : 85,
    "Ko Ko" : 55,
    "Hla Hla" : 92,
    "Mg Mg": 45,
    "Su Su" : 76,
    "Ma Ma" : 88
}

print("===== Student Groups =====")

print("A:")
for name,score in students.items() :
    if score >= 80 :
        print(name)

print("B:")
for name,score in students.items() :
    if score < 80 and score >= 60 :
        print(name)

print("C:")
for name,score in students.items() :
    if score < 60 and score >= 50 :
        print(name)

print("Fail:")
for name,score in students.items() :
    if score < 50 :
        print(name)

print(f"Total Students : {len(students)}")