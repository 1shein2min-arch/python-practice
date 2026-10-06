import json

products = [
    {
        "name": "Redmi Note 13",
        "price": 450000,
        "stock": 10,
        "category": "Phone"
    },
    {
        "name": "Mi Power Bank",
        "price": 35000,
        "stock": 20,
        "category": "Accessory"
    }
]

with open("product.json","w") as file :
    json.dump(products,file,indent=4)

