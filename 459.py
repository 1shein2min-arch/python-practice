import sqlite3

connection = sqlite3.connect("repair.db")

customer_name = "Ko Ko"

data = connection.execute("""
SELECT * FROM repairs
WHERE customer = ?""",(customer_name,))

row = data.fetchone()

if row :
    print(f"Customer :{row[1]}")
    print(f"Model : {row[2]}")
    print(f"fee : {row[3]}")
else :
    print("Customer Not Found")

connection.close()