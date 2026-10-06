import sqlite3

connection = sqlite3.connect("repair.db")

customer_name = "Ko Ko"
new_fee = 180000

connection.execute("""
UPDATE repairs
SET fee = ?
WHERE customer = ?""",(new_fee,customer_name))

connection.commit()

data = connection.execute("""
SELECT * FROM repairs
WHERE customer = ?""",(customer_name,))

row = data.fetchone()

if row:
    print(f"Customer : {row[1]}")
    print(f"Fee : {row[3]}")





