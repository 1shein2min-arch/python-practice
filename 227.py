students = {
    "Aung": 85,
    "Ko Ko": 45,
    "Hla Hla": 95,
    "Mg Mg": 60,
    "Su Su": 35
}

def status(name,score) :
    if score >= 50 :
        print(f"{name} : Passed")
    else :
        print(f"{name} : Failed")

print("===== Student Status =====")

for name,score in students.items():
    status(name,score)
    