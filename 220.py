students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 60
}
def stu() :
    print("Students :")
    for name,score in students.items() :
        print(f"{name} : {score}")

def status() :
    print("Student Status :")
    for name,score in students.items() :
        if score >= 50 :
            print(f"{name} : Passed")
        else :
            print(f"{name} : Failed")

def passed() :
    print("Passed Students :")
    for name,score in students.items() :
        if score >= 50 :
            print(name)

def failed() :
    print("Failed Students :")
    for name,score in students.items() :
        if score < 50 :
            print(name)

def total_stu() :
    print(f"Total Students : {len(students)}")

print("===== Student Information =====")

stu()

status()

passed()

failed()

total_stu()
    