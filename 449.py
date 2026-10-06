import sqlite3

connection = sqlite3.connect("repair.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS repairs(
    id INTEGER PRIMARY KEY,
    customer TEXT,
    model TEXT,
    fee INTEGER
)
""")

connection.commit()

print("Table Create")

connection.close()