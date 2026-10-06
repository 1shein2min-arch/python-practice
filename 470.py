import sqlite3

def show_expensive_repair() :
    connection = sqlite3.connect("repair.db")

    data = connection.execute("""
    SELECT * FROM repairs
    ORDER BY fee DESC
    """)

    rows = data.fetchall()

    for row in rows:
        print(f"ID       : {row[0]}")
        print(f"Customer : {row[1]}")
        print(f"Model    : {row[2]}")
        print(f"Fee      : {row[3]}")
        print("-" * 30)

    connection.close()

show_expensive_repair()