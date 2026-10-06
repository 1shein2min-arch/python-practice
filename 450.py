import sqlite3

connection = sqlite3.connect("repair.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT
)
""")

connection.commit()

print("Customer table created")

connection.close()