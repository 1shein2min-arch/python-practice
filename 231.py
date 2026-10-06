students = {
    "Aung" : 85,
    "Ko Ko" : 45,
    "Hla Hla ":95,
    "Mg Mg" : 60 ,
    "Su Su" : 35
}

def stu(name,score) :
    print(f"{name} : {score}")

def status(name,score) :
    if score >= 50 :
        print(f"{name} : Passed")
    else :
        print(f"{name} : Failed")

def passed(name,score) :
    if score >= 50 :
        print(name)

def failed(name,score) :
    if score < 50 :
        print(name)

def total() :
    print(f"Total Students : {len(students)}")

def total_score() :
    total = 0
    for score in students.values() :
        total = total + score 
    print(f"Total Score : {total}")

print("===== Student Management =====")

print("Students :")
for name,score in students.items():
    stu(name,score)

print("Status :")
for name,score in students.items() :
    status(name,score)

print("Passed Students :")
for name,score in students.items() :
    passed(name,score)

print("Failed Students :")
for name,score in students.items() :
    failed(name,score)

total()

total_score()