repairs = [
    {"id": 1, "customer": "Aung Min"},
    {"id": 2, "customer": "Ko Ko"},
    {"id": 3, "customer": "Mg Aung"},
    {"id": 4, "customer": "SheiN"}
]

search_name = input("Enter Customer :").lower().strip()

print("===== Search Result =====")
for repair in repairs :
    if search_name in repair['customer']:
        print(f"ID : {repair['id']}")
        print(f"Customer : {repair['customer']}")