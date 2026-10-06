import sqlite3

connection = sqlite3.connect("repair.db")

connection.execute("""
    INSERT INTO repairs(customer,model,fee)
    VALUES ('Mg Mg','Redmi Note 13','80000')
""")

connection.commit()
print("Repair Added !")

connection.close()