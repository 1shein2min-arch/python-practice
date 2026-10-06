students = {
    "Aung" : 80 ,
    "Ko Ko" : 70 ,
}
print("Before :")
print(students)

students.setdefault("Hla Hla",90)
students.setdefault("Aung" , 100)
print("After :")
print(students)

print(f"Aung Score: {students.get('Aung')}")
print(f"Hla Hla Score : {students.get('Hla Hla')}")
