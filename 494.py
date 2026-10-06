import requests

params = {
    "q": "python"
}

response = requests.get(
    "https://api.github.com/search/users",
    params=params
)

response.raise_for_status()

data = response.json()

for user in data["items"]:
    print(user["login"])