import sqlite3

def show_payment_summary() :

    connection = sqlite3.connect("repair.db")

    data = connection.execute("""
    SELECT * FROM repairs
    """)
    rows = data.fetchall()

    print("===== Payment Summary =====")

    paid_repair=0
    paid_fee = 0

    unpaid_repair=0
    unpaid_fee=0
    
    for row in rows:
        if row[5] == "paid" :
            paid_fee += row[3]
            paid_repair += 1
        elif row[5] == "unpaid" :
            unpaid_fee += row[3]
            unpaid_repair += 1
    
    print(f"Paid Repair : {paid_repair}")
    print(f"Paid Fee : {paid_fee}")
    print()
    print(f"Unpaid Repair : {unpaid_repair}")
    print(f"Unpaid Fee :{unpaid_fee}") 

    connection.close()       

