repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]

def update_status(repairs,model,name,status) :
    for repair in repairs :
        if repair["model"] == model and repair["name"] == name :
            repair["status"] = status
            return True 
            break
    return False

name = input("Enter Name :")
model = input("Enter Model :")
status = input("Enter Status :")

update = update_status(repairs,model,name,status)

if update :
    print("Status update")
else :
    print("Not Found")

print(repairs)
