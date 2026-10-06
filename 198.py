scores = {
    "Aung" : 85,
    "Ko Ko" : 70,
    "Hla Hla" : 95,
    "Mg Mg" : 45
}

print(f"Aung Score :{scores.get('Aung')}")
print(f"Su Su Score : {scores.get('Su Su',0)}")

print("Students :")
for name,score in scores.items() :
    print(f"{name} : {score}")

print("Passed :")
for name,score in scores.items() :
    if score >= 50 :
        print(name)

print("Failed :")
for name,score in scores.items() :
    if score < 50 :
        print(name)

total = 0
for name,score in scores.items() :
    total = total + score

print(f"Total Score: {total}")

highest_score = 0
highest_name = ""

lowest_score = 99
lowest_name = ""

for name,score in scores.items() :
    if score > highest_score :
        highest_score = score
        highest_name = name

    if score < lowest_score :
        lowest_score = score
        lowest_name = name

print(f"Highest : {highest_name} : {highest_score}")
print(f"Lowest : {lowest_name} : {lowest_score}")