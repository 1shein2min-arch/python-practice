repairs = [
    {"id": 1, "customer": "Aung", "status": "Pending", "payment_status": "Unpaid"},
    {"id": 2, "customer": "Ko Ko", "status": "Pending", "payment_status": "Paid"},
    {"id": 3, "customer": "Mg Mg", "status": "Done", "payment_status": "Unpaid"},
    {"id": 4, "customer": "SheiN", "status": "Done", "payment_status": "Paid"},
    {"id": 5, "customer": "Kyaw", "status": "Pending", "payment_status": "Unpaid"}
]

for repair in repairs :
    if repair['status'] == "Pending" and repair['payment_status'] == "Unpaid" :
        print(f"ID : {repair['id']}")
        print(f"Customer : {repair['customer']}")
        print("-----------------")