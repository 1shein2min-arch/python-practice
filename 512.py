import requests

def create_repair(customer,model,fee) :
    try :

        data = {
            "customer" : customer,
            "model" : model,
            "fee" : fee
        }

        response = requests.post(
            "https://httpbin.org/post",
            json=data
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException :
        print("API Request Failed")
        return None
    
users = create_repair("SheiN","Redmi Note 13",50000)


if users :
    print(users["json"]["customer"])
    print(users["json"]["fee"])  