scores = {
    "Aung" : 80 ,
    "Ko Ko" : 45 ,
    "Hla Hla" : 90 ,
    "Mg Mg" : 35 ,
    "Su Su" : 70 
}
total = 0 
for score in scores.values() :
    print(score)
    total = total + score
print(f"Total Score : {total}")

print("Passed :")
for score in scores.values() :
    if score >= 50 :
        print(score)
print("Failed :")
for score in scores.values() :
    if score < 50 :
        print(score)
