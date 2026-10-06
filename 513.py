import sqlite3

connection = sqlite3.connect("users.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    followers INTEGER,
    public_repos INTEGER
)
""")

connection.commit()
connection.close()

import requests
import sqlite3


def get_user(username):

    response = requests.get(
        f"https://api.github.com/users/{username}"
    )

    response.raise_for_status()

    return response.json()


user = get_user("octocat")

connection = sqlite3.connect("users.db")

connection.execute("""
INSERT INTO users(
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