students = {
    "Aung" : 85,
    "Ko Ko" : 70, 
    "Hla Hla" : 95
}
print(f"Aung Score : {students.get('Aung')}")
print(f"Mg Mg Score : {students.get('Mg Mg',0)}")
print(f"Su Su Score : {students.get('Su Su',0)}")

if "Aung" in students:
    print("Aung Found")

if "Mg Mg" in students:
    print("Mg Mg Found")
else :
    print("Mg Mg Not Found")