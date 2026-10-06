import requests
import sqlite3


def create_table():

    connection = sqlite3.connect("users.db")

    connection.execute("""
    CREATE TABLE IF NOT EXISTS users(
        login TEXT PRIMARY KEY,
        followers INTEGER,
        public_repos INTEGER
    )
    """)

    connection.commit()
    connection.close()


def get_user_from_api(username):

    try:
        response = requests.get(
            f"https://api.github.com/users/{username}"
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:
        print("API Request Failed")
        return None


def save_user(user):

    connection = sqlite3.connect("users.db")

    connection.execute("""
    INSERT OR REPLACE INTO users(
        login,
        followers,
        public_repos
    )
    VALUES (?, ?, ?)
    """, (
        user["login"],
        user["followers"],
        user["public_repos"]
    ))

    connection.commit()
    connection.close()


def find_user(login):

    connection = sqlite3.connect("users.db")

    cursor = connection.execute("""
    SELECT * FROM users
    WHERE login = ?
    """, (login,))

    row = cursor.fetchone()

    connection.close()

    return row


create_table()

user = get_user_from_api("octocat")

if user:
    save_user(user)

result = find_user("octocat")

print(result)