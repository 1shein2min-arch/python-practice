import requests 

def search_users(keyword) :

    try :
        result = []
        for page in range(1,4) :

            params = {
                "q" : keyword,
                "page" : page,
                "per_page" : 5 
            }

            response = requests.get(
                "https://api.github.com/search/users",
                params=params
            )

            response.raise_for_status()

            data = response.json()

            for user in data["items"] :
                result.append(user)

        return result
    
    except requests.RequestException:
        print("API Request Failed")
        return None

users = search_users("python")

for user in users :
    print(user["login"])

