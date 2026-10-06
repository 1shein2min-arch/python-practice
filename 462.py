import sqlite3

connection = sqlite3.connect("repair.db")

repair_id = 5

connection.execute("""
DELETE FROM repairs
WHERE id = ?
""",(repair_id,))

connection.commit()

data = connection.execute("""
SELECT * FROM repairs
""")

rows = data.fetchall()

for row in rows :
    print(row)

connection.close()