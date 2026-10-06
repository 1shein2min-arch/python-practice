students = {
    "Aung Aung" : 85,
    "Ko Ko" : 55 ,
    "Hla Hla" : 92 ,
    "Mg Mg" : 48 ,
    "Su Su" : 76 
}
for name , score in students.items() :
    print(name,score)

print("Passed :")
for name ,score in students.items() :
    if score >= 50 :
        print(name)

print("Failed :")
for name ,score in students.items() :
    if score< 50 :
        print(name)


