import sqlite3


def add_repair():
    customer = input("Customer Name : ").strip()
    model = input("Phone Model : ").strip()
    fee = int(input("Repair Fee : "))

    connection = sqlite3.connect("repair.db")

    connection.execute("""
    INSERT INTO repairs(customer, model, fee)
    VALUES (?, ?, ?)
    """, (customer, model, fee))

    connection.commit()
    connection.close()

    print("Repair Added Successfully!")


def show_repairs():
    connection = sqlite3.connect("repair.db")

    data = connection.execute("""
    SELECT * FROM repairs
    """)

    rows = data.fetchall()

    for row in rows:
        print(f"ID       : {row[0]}")
        print(f"Customer : {row[1]}")
        print(f"Model    : {row[2]}")
        print(f"Fee      : {row[3]}")
        print("-" * 30)

    connection.close()


while True:
    print("\n1. Add Repair")
    print("2. View Repairs")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter Choice : "))
            break
        except ValueError:
            print("Please Enter a Number")

    if choice == 1:
        add_repair()

    elif choice == 2:
        show_repairs()

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")