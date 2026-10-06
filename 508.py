import requests

def search_paid_users(keyword) :
    try :
        params = {
            "q" : keyword
        }

        response = requests.get(
            "https://api.github.com/search/users",
            params=params
        )

        response.raise_for_status()

        data = response.json()

        result = []

        for user in data["items"] :
            if len(user["login"]) >= 8 :
                result.append(user)

        return result

    except requests.RequestException :
        print("API Request Failed")
        return None

users = search_paid_users("python")

for user in users :
    print(user["login"])