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

connection.execute("""
INSERT INTO repairs(customer, model, fee)
VALUES
    ('Aung', 'iPhone 11', 50000),
    ('Mg Mg', 'Redmi Note 13', 80000),
    ('Ko Ko', 'Samsung A52', 150000),
    ('Hla Hla', 'iPhone 13', 250000),
    ('Kyaw Kyaw', 'Vivo Y55', 120000)
""")

connection.commit()

minimum_fee = 100000

data = connection.execute("""
SELECT * FROM repairs
WHERE fee >= ?
""", (minimum_fee,))

print("\n===== Fee >= 100000 =====")

for row in data:
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print(f"Fee : {row[3]}")
    print("----------------")

customer_name = input("\nEnter Customer Name : ").strip()

data1 = connection.execute("""
SELECT * FROM repairs
WHERE customer = ?
""", (customer_name,))

found = False

print("\n===== Customer Search =====")

for row in data1:
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print(f"Fee : {row[3]}")

    found = True

if found == False:
    print("Customer Not Found")

data2 = connection.execute("""
SELECT * FROM repairs
""")

count = 0
total_fees = 0

for row in data2:
    total_fees += row[3]
    count += 1

print("\n===== Summary =====")
print(f"Total Repairs : {count}")
print(f"Total Fees : {total_fees}")

connection.close()