import requests

params = {
    "q": "python",
    "page": 2,
    "per_page": 5
}

response = requests.get(
    "https://api.github.com/search/users",
    params=params
)

response.raise_for_status()

data = response.json()

for user in data["items"]:
    print(user["login"])