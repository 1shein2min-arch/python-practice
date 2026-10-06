repairs = [
    {
        "model": "iPhone 11",
        "name": "SheiN",
        "fee": 30000,
        "status": "Done"
    },

    {
        "model": "Redmi Note 13",
        "name": "Aung",
        "fee": 50000,
        "status": "Pending"
    },

    {
        "model": "Vivo Y55",
        "name": "Mg Mg",
        "fee": 25000,
        "status": "Done"
    }
]

for repair in repairs :
    if repair["status"] == "Pending" :
        print(f" {repair["model"]} - {repair['name']} - {repair["fee"]}")