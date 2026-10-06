students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 60
}


def show_students():
    for name, score in students.items():
        print(f"{name} : {score}")


def status(score):
    if score >= 50:
        return "Passed"
    else:
        return "Failed"


def add_marks(score):
    return score + 5


print("===== Student Management =====")

print("Students:")
show_students()

name = input("Enter Student : ")

if name in students:

    score = students.get(name)

    print(f"Score : {score}")
    print(f"Status : {status(score)}")

    print("Add 5 Marks")

    new_score = add_marks(score)

    students[name] = new_score

    print(f"New Score : {new_score}")
    print(f"New Status : {status(new_score)}")

else:
    print("Student Not Found")