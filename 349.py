repairs = [
    {"model": "iPhone 11", "name": "SheiN", "fee": 30000, "status": "Done"},
    {"model": "Redmi Note 13", "name": "Aung", "fee": 50000, "status": "Pending"},
    {"model": "Vivo Y55", "name": "Mg Mg", "fee": 25000, "status": "Done"}
]

total_fee = 0
count = 0
for repair in repairs :
    if repair["name"] == "Aung" and repair["status"] == "Pending":
        total_fee = total_fee + repair["fee"]
        count = count + 1
        print(f"{repair['model']} - {repair['name']} - {repair['fee']} - {repair['status']}")

print(f"Aung Pending Repairs : {count}")
print(f"Aung Pending Fee : {total_fee}")