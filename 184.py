students = {
    "Aung" : 85 ,
    "Ko Ko": 70 ,
    "Hla Hla" : 95 ,
    "Mg Mg" : 60 ,
}
total = 0
for score in students.values() :
    print(score)
    total = total + score
print(f"Total Score : {total}")