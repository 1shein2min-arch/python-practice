students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 60
}

def show_stu() :
    for name,score in students.items() :
        print(f"{name} : {score}")

def show(score) :
    if score >= 50 :
        return "Passed"
    else :
        return "Failed"

print("===== Student Check =====")

print("Students :")
show_stu()

name = input("Enter Name :")
if name in students :
    score = students.get(name)
    print(f"Score : {score}")
    print(f"Status :{show(score)}")
else :
    print("Student Not Found")