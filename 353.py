repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]

name = input("Enter Name :")
model = input("Enter Model :")
def delete_repair(repairs,model,name) :
    found = False
    for repair in repairs :
        if repair["model"] == model and repair["name"] == name :
            repairs.remove(repair)
            found = True
            break
    return found
            
delete = delete_repair(repairs,model,name)

if delete :
    print("Delete Successful")
else :
    print("Repair Not Found")

print(repairs)