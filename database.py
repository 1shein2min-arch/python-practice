import sqlite3

from models import Repair


def load_repairs():
    connection = sqlite3.connect("repair.db")

    data = connection.execute("""
    SELECT * FROM repairs
    """)

    rows = data.fetchall()

    repairs = []

    for row in rows:
        repair = Repair(
            row[0],
            row[1],
            row[2],
            row[3]
        )

        repair.status = row[4]
        repair.payment = row[5]
        repair.date = row[6]

        repairs.append(repair)

    connection.close()

    return repairs

def save_repair(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    INSERT INTO repairs(
        id, customer, model, fee, status, payment_status , date
    )
    VALUES (?, ?, ?, ?, ?, ? , ?)
    """, (
        repair.id,
        repair.customer,
        repair.model,
        repair.fee,
        repair.status,
        repair.payment,
        repair.date
    ))

    connection.commit()
    connection.close()

def create_table():
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    CREATE TABLE IF NOT EXISTS repairs(
        id INTEGER PRIMARY KEY,
        customer TEXT,
        model TEXT,
        fee INTEGER,
        status TEXT DEFAULT 'Pending',
        payment_status TEXT DEFAULT 'Unpaid'
    )
    """)

    columns = connection.execute(
        "PRAGMA table_info(repairs)"
    ).fetchall()

    column_names = []

    for column in columns:
        column_names.append(column[1])

    if "date" not in column_names:
        connection.execute("""
        ALTER TABLE repairs
        ADD COLUMN date TEXT
        """)

    connection.commit()
    connection.close()
    
def update_fee(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET fee = ?
    WHERE id = ?
    """, (repair.fee, repair.id))

    connection.commit()
    connection.close()


def update_status(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET status = ?
    WHERE id = ?
    """, (repair.status, repair.id))

    connection.commit()
    connection.close()


def update_payment(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET payment_status = ?
    WHERE id = ?
    """, (repair.payment, repair.id))

    connection.commit()
    connection.close()

def delete_from_database(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    DELETE FROM repairs
    WHERE id = ?
    """, (repair.id,))

    connection.commit()
    connection.close()



