repairs = [
    {"id": 1, "customer": "Aung", "status": "Done"},
    {"id": 2, "customer": "Ko Ko", "status": "Pending"},
    {"id": 3, "customer": "Mg Mg", "status": "Done"},
    {"id": 4, "customer": "SheiN", "status": "Pending"}
]

for repair in repairs :
    if not repair['status'] == "Done" :
        print(f"ID : {repair['id']}")
        print(f"Customer : {repair['customer']}")
        print("-----------------")