import requests

params = {
    "q" : "python"
}
response = requests.get(
    "https://api.github.com/search/users",
    params=params
)

response.raise_for_status()

data= response.json()

results = []
count = 0

for user in data['items'] :
    if len(user['login']) >= 10 :
        results.append(user['login'])
        count += 1
print(f"User : {count}")

for username in results :
    print(username)