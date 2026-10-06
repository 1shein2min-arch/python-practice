import sqlite3

def edit_repair() :
    repair_id = int(input("Enter Repair ID :"))
    new_fee = int(input("Enter New Fee :"))

    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET fee = ?
    WHERE id = ?""",(new_fee,repair_id))

    connection.commit()
    connection.close()

    print("Repair Updated Successfully!")