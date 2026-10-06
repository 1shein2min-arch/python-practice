import json

repair = {
    "customer": "Aung",
    "model": "Redmi Note 13",
    "fee": 50000,
    "status": "Pending"
}

text = json.dumps(repair)

print(text)