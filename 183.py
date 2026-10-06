students = {
    "Aung" : 85 ,
    "Ko Ko" : 45 ,
    "Hla Hla" : 92 ,
    "Mg Mg" : 38 ,
    "Su Su" : 75 
}
print("Passed :")
for name,score in students.items() :
    if score > 40 :
        print(name)

print("Failed :")
for name,score in students.items() :
    if score < 40 :
        print(name)

highest_score = 0
highest_name = "" 

lowest_score = 99
lowest_name = ""

for name,score in students.items() :
    if score > highest_score :
        highest_score = score
        highest_name = name
    if score < lowest_score :
        lowest_score = score
        lowest_name = name

print(f"Highest : {highest_name} : {highest_score}")
print(f"Lowest : {lowest_name} : {lowest_score}")