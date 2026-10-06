students = {
    "Aung" : 85,
    "Ko KO" : 45,
    "Hla Hla" :95,
    "Mg Mg" : 60
}

def status(name,score) :
    if score >= 50:
        print(f"{name} : Passed")
    else :
        print(f"{name} : Failed")

print("===== Student Status =====")

status("Aung",85)
status("Ko Ko",45)
status("Hla Hla",95)
status("Mg Mg",60)
