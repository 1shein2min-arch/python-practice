import sqlite3

connection = sqlite3.connect("repair.db")

data = connection.execute("""
SELECT * FROM repairs
""")

for row in data :
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print("------------")

connection.close()