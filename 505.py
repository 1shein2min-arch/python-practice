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

    result = []

    for user in data['item'] :
        if len(user['login']) >= 10 :
            result.append(user)

    return result

users = search_user("python")

for user in users :
    print(user)