repairs = [
    {
        "id" : 1,
        "customer" : "Aung",
        "model" : "Redmi Note 13",
        "fee" :  50000 ,
        "status" : "Pending"
    },
    {
        "id" : 2,
        "customer" : "Aung",
        "model" : "Vivo Y55",
        "fee" :  30000 ,
        "status" : "Done"
    },
{
        "id" : 3,
        "customer" : "Ko Ko",
        "model" : "Samsung A52",
        "fee" :  80000 ,
        "status" : "Pending"
    },
]

print("===== Repair =====")
for repair in repairs :
    print(f"ID : {repair['id']}")
    print(f"Customer : {repair['customer']}")
    print(f"Model : {repair['model']}")
    print(f"Fee : {repair['fee']}")
    print(f"Status : {repair['status']}")
    print("------------------------------")