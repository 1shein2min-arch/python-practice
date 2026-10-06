import requests

def count_long_users(keyword) :

    params = {
        "q" : keyword
    }

    response = requests.get(
        "https://api.github.com/search/users",
        params=params
    )

    response.raise_for_status()

    data = response.json()

    count = 0

    for user in data["items"] :
        if len(user["login"]) >= 10 :
            count += 1

    return count

users = count_long_users("python")

print(users)


