scores = {
    "Aung" : 78,
    "Ko Ko" : 92,
    "Hla Hla" : 65,
    "Mg Mg" : 88,
    "Su Su" : 55 
}
highest_name = "" 
highest_score = 0

lowest_name = ""
lowest_score = 99

for name,score in scores.items() :
    if score > highest_score :
        highest_score = score
        highest_name = name
        
    if score < lowest_score :
        lowest_score = score
        lowest_name = name

print(f"Highest : {highest_name} : {highest_score}")
print(f"Lowest : {lowest_name} : {lowest_score}")