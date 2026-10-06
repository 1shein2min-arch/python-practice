import requests 

response = requests.post(
    "https://httpbin.org/post" ,
    json={
        "name" : "SheiN" ,
        "age" : 24 ,
        "job" : "Developer"
    }
)

data = response.json()
print("===== User =====")
print(f"Name : {data['json']['name']}")
print(f"Age : {data['json']['age']}")
print(f"Job : {data['json']['job']}")