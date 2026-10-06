students = {
    "Aung": 85,
    "Ko Ko": 70,
    "Su Su": 95,
    "Mg Mg": 80,
    "Hla Hla": 90
}

def highest() :
    high = 0
    high_name = ""
    for name , score in students.items() :
        if score > high :
            high = score 
            high_name = name 
    print(f"Top Student : {high_name} : {high}")

highest()