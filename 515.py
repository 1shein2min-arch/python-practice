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


def get_all_users():

    connection = sqlite3.connect("users.db")

    cursor = connection.execute("""
    SELECT * FROM users
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


def update_followers(login, followers):

    connection = sqlite3.connect("users.db")

    connection.execute("""
    UPDATE users
    SET followers = ?
    WHERE login = ?
    """, (followers, login))

    connection.commit()
    connection.close()


def delete_user(login):

    connection = sqlite3.connect("users.db")

    connection.execute("""
    DELETE FROM users
    WHERE login = ?
    """, (login,))

    connection.commit()
    connection.close()


def show_users():

    users = get_all_users()

    if not users:
        print("No Users Found")
        return

    for user in users:
        print(f"Username    : {user[0]}")
        print(f"Followers   : {user[1]}")
        print(f"Public Repos: {user[2]}")
        print("-" * 30)


create_table()


while True:

    print("\n1. Add User")
    print("2. View Users")
    print("3. Update Followers")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":

        username = input("Enter GitHub Username: ")

        user = get_user_from_api(username)

        if user:
            save_user(user)
            print("User Saved")

    elif choice == "2":

        show_users()

    elif choice == "3":

        username = input("Enter Username: ")
        followers = int(input("Enter New Followers: "))

        update_followers(username, followers)

        print("Followers Updated")

    elif choice == "4":

        username = input("Enter Username: ")

        delete_user(username)

        print("User Deleted")

    elif choice == "5":

        print("Goodbye")

        break

    else:

        print("Invalid Choice")