students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 40
}

def show_student() :
    for name,score in students.items() :
        print(f"{name} : {score}")

def mark(score,add_mark) :
    return score + add_mark

print("===== Student Update =====")

print("Students :")
show_student()

name = input("Enter Student :")
if name in students :
    add_mark = int(input("Enter Add Marks :"))
    total = mark(students.get(name),add_mark)

    print(f"Old Score : {students.get(name)}")
    print(f"New Score : {total}")
    if total >= 50 :
        print("Status : Passed")
    else :
        print("Status : Failed")

else :
    print("Student Not Found")