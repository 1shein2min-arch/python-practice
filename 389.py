repairs = [
    {"id": 1, "customer": "Aung", "status": "Pending"},
    {"id": 2, "customer": "Ko Ko", "status": "Done"},
    {"id": 3, "customer": "Mg Mg", "status": "Cancelled"},
    {"id": 4, "customer": "SheiN", "status": "Pending"}
]

for repair in repairs :
    if repair['status'] == "Pending" or repair['status'] == "Cancelled" :
        print(f"ID : {repair['id']}")
        print(f"Customer : {repair['customer']}")
        print("------------------")