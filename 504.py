import requests

def search_user(keyword) :

    params = {
        "q" : keyword
    }

    response = requests.get(
        "https://api.github.com/search/users",
        params=params
    )

    response.raise_for_status()

    data = response.json()

    return data["items"]

users = search_user("python")

print(users)

for user in users :
    print(user['login'])