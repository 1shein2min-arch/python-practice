import sqlite3
import os

print("Database path:", os.path.abspath("repair.db"))


def delete_repair(repair_id):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    DELETE FROM repairs
    WHERE id = ?
    """, (repair_id,))

    connection.commit()
    connection.close()


delete_repair(3)

connection = sqlite3.connect("repair.db")

data = connection.execute("""
SELECT * FROM repairs
""")

rows = data.fetchall()

for row in rows:
    print(row)

connection.close()