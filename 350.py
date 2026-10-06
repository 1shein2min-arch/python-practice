repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]

def search_customer(repairs) :
    while True :
        name = input("Enter Name :").strip()
        if name == "" :
            print("Name Cannot Be Empty")
            continue
        break
    found = False

    total = 0
    count = 0
    for repair in repairs :
        if name == repair["name"] :
            found = True
            total = total + repair["fee"]
            count = count + 1
            print(f"{repair['model']} - {repair['name']} - {repair['fee']} - {repair['status']}")

    if found == False :
        print("Customer Not Found")

    else :
        print(f"{name} Repairs : {count}")
        print(f"{name} Total Fee : {total}")

    return count,total

def get_done_fee(repairs) :
    done_fee = 0
    done_count = 0
    for repair in repairs :
        if repair["status"] == "Done" :
            done_fee = done_fee + repair["fee"]
            done_count = done_count + 1
    return done_fee,done_count

fee,count = get_done_fee(repairs)
print(f"Done Fee : {fee}")
print(f"Done Count : {count}")

def get_customer_total(repairs,name) :
    total = 0

    for repair in repairs :
        if repair["name"] == name :
            total = total + repair["fee"]

    return total

total = get_customer_total(repairs,"Aung")

def get_customer_summary(repairs,name) :
    count = 0
    fee = 0
    found = False
    for repair in repairs :
        if repair["name"] == name :
            found = True
            count = count + 1
            fee = fee + repair["fee"]

    return found,count,fee 

name = input("Enter Name :").strip()
found,count,fee = get_customer_summary(repairs,name)

if found : 
    print(f"{name} Repair : {count}")
    print(f"{name} Total : {fee}")
else :
    print("Customer Not Found")









