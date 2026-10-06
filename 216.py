students = {
    "Aung" : 85 ,
    "Ko Ko" : 45 ,
    "Hla Hla" : 92
}

print("===== Student Check =====")
print("Students :")
for name,score in students.items() :
    print(f"{name} : {score}")

print("Passed :")
for name,score in students.items() :
    if score >= 50 :
        print(name)

print("Failed :")
for name,score in students.items() :
    if score < 50 :
        print(name)

print(f"Total Students : {len(students)}")

print("Highest :")
highest_score = 0
highest_name = ""
for name,score in students.items() :
    if score > highest_score :
        highest_score = score
        highest_name = name
print(f"{highest_name} : {highest_score}")

lowest_score = 99
lowest_name = ""
for name,score in students.items() :
    if score < lowest_score :
        lowest_score = score
        lowest_name = name
print(f"{lowest_name} : {lowest_score}")