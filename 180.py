scores = {
    "Aung" : 75 ,
    "Ko Ko" : 90 ,
    "Hla Hla" : 65 ,
    "Mg Mg" : 85 
}

highest_score = 0
highest_name = ""

lowest_score = 999
lowest_name = ""

for name,score in scores.items() :
    if score > highest_score :
        highest_score = score
        highest_name = name

    if score < lowest_score :
        lowest_score = score
        lowest_name = name

print(f"Highest :{highest_name} : {highest_score}")
print(f"lowest : {lowest_name} : {lowest_score}")