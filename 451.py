import sqlite3

connection = sqlite3.connect("repair.db")

connection.execute("""
    INSERT INTO repairs(customer,model,fee)
    VALUES('Aung','iPhone 11',50000
)
""")

connection.commit()

print("Repair Added!")

connection.close()