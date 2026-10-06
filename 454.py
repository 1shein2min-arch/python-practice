import sqlite3 

connection = sqlite3.connect("repair.db")

data = connection.execute("""
SELECT *FROM repairs
Where fee >= 100000
""")

for row in data :
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print(f"Fee : {row[3]}")
    print("----------")