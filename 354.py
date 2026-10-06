repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]

name = input("Enter Name :")
model = input("Enter Model :")
fee = int(input("Enter Fee :"))
status = input("Enter status :")

def add_repair(repairs,model,name,fee,status) :
    repair = {
        "model" : model ,
        "name" : name ,
        "fee" : fee ,
        "status" : status
    }
    repairs.append(repair)

add_repair(repairs,model,name,fee,status)

def view_repair(repairs) :
    for repair in repairs :
        print(f"{repair['model']} - {repair['name']} - {repair['fee']} - {repair['status']}")

view_repair(repairs)