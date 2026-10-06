students = {
    "Aung": 80,
    "Ko Ko": 60,
    "Su Su": 100,
    "Mg Mg": 70,
    "Hla Hla": 90
}

total = 0
for score in students.values() :
    total += score
    
print(f"Total Score : {total}")

print(f"Total Students : {len(students)}")

average = total/len(students)

print(f"Average Score : {average}")