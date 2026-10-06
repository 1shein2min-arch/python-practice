import sqlite3

connection = sqlite3.connect("repair.db")

minimum_fee = 100000
data = connection.execute("""
SELECT * FROM repairs
WHERE fee >= ?""",(minimum_fee,))

rows = data.fetchall()

for row in rows :
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print(f"Fee : {row[3]}")

connection.close()