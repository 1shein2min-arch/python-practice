repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]

name = input("Enter Name :")
model = input("Enter Model :")
fee = int(input("Enter Fee :"))

def update_fee(repairs,model,name,fee) :
    for repair in repairs :
        if repair["name"] == name and repair["model"] == model :
            repair["fee"] = fee
            return True
            
    return False
result = update_fee(repairs,model,name,fee)

print(result)
print(repairs)