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
    VALUES ('Ko Ko', 'Samsung A52', 150000)
""")

connection.commit()

data = connection.execute("""
    SELECT * FROM repairs
    WHERE fee >= 100000
""")

for row in data:
    print(f"Customer : {row[1]}")
    print(f"Model : {row[2]}")
    print(f"Fee : {row[3]}")
    print("----------")

connection.close()