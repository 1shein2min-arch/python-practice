import sqlite3

minimum_fee = 150000

connection = sqlite3.connect("repair.db")

data =connection.execute("""
SELECT * FROM repairs
WHERE fee>= ?""",(minimum_fee,))

for row in data :
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print(f"Fee : {row[3]}")

connection.close()
