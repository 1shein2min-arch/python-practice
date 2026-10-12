import json

customer = {
    "name": "မောင်မောင်",
    "fee" : 30000
}

with open("customer.json","w",encoding="utf-8") as file:
    json.dump(customer,file,indent=4,ensure_ascii=False)