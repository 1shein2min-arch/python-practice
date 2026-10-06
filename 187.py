students = {
    "Aung" : 80 ,
    "Ko Ko" : 70 ,
    "Hla Hla" : 90 ,
    "Mg Mg" : 60 
}

for name in students.keys() :
    print(name)
    len(students)
print(f"Total Students : {len(students)}")

if "Aung" in students :
    print("Aung Found")

if "Ma Ma" in students :
    print("Ma Ma Found")
else:
    print("Ma Ma Not Found")