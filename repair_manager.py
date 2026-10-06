import sqlite3
import math


class Repair:
    def __init__(self, repair_id, customer, model, fee):
        self.id = repair_id
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"
        self.payment = "Unpaid"

    def change_fee(self, new_fee):
        if new_fee < 0:
            print("Invalid Fee")
            return False

        self.fee = new_fee
        return True

    def change_status(self, new_status):
        if new_status == "Pending" or new_status == "Done":
            self.status = new_status
            return True

        print("Invalid Status")
        return False

    def change_payment(self, new_payment):
        if new_payment == "Paid" or new_payment == "Unpaid":
            self.payment = new_payment
            return True

        print("Invalid Payment")
        return False

    def show_info(self):
        print(f"ID       : {self.id}")
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")
        print(f"Payment  : {self.payment}")
        print("-" * 30)


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

    connection.commit()
    connection.close()


def get_number(message):
    while True:
        try:
            number = int(input(message))

            if number < 0:
                print("Number Cannot Be Negative")
            else:
                return number

        except ValueError:
            print("Please Enter a Number")


def get_fee():
    while True:
        try:
            fee = int(input("Enter Fee : "))

            if fee < 0:
                print("Fee Cannot Be Negative")
            else:
                return fee

        except ValueError:
            print("Please Enter a Number")


def get_text(message):
    while True:
        text = input(message).strip()

        if text == "":
            print("This Field Cannot Be Empty")
        else:
            return text


def save_repair(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    INSERT INTO repairs(
        id, customer, model, fee, status, payment_status
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        repair.id,
        repair.customer,
        repair.model,
        repair.fee,
        repair.status,
        repair.payment
    ))

    connection.commit()
    connection.close()


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

        repairs.append(repair)

    connection.close()

    return repairs


def find_repair(repairs, repair_id):
    for repair in repairs:
        if repair.id == repair_id:
            return repair

    return None


def find_by_customer(repairs, customer):
    results = []

    for repair in repairs:
        if repair.customer.lower() == customer.lower():
            results.append(repair)

    return results


def get_pending_repairs(repairs):
    results = []

    for repair in repairs:
        if repair.status == "Pending":
            results.append(repair)

    return results


def get_unpaid_repairs(repairs):
    results = []

    for repair in repairs:
        if repair.payment == "Unpaid":
            results.append(repair)

    return results


def get_total_repairs(repairs):
    return len(repairs)


def get_pending_count(repairs):
    count = 0

    for repair in repairs:
        if repair.status == "Pending":
            count += 1

    return count


def get_done_count(repairs):
    count = 0

    for repair in repairs:
        if repair.status == "Done":
            count += 1

    return count


def get_paid_count(repairs):
    count = 0

    for repair in repairs:
        if repair.payment == "Paid":
            count += 1

    return count


def get_unpaid_count(repairs):
    count = 0

    for repair in repairs:
        if repair.payment == "Unpaid":
            count += 1

    return count


def get_total_fee(repairs):
    total = 0

    for repair in repairs:
        total += repair.fee

    return total


def get_unpaid_fee(repairs):
    total = 0

    for repair in repairs:
        if repair.payment == "Unpaid":
            total += repair.fee

    return total


def add_repair(repairs):
    repair_id = get_number("Enter Repair ID : ")

    if find_repair(repairs, repair_id) is not None:
        print("ID Already Exists")
        return

    customer = get_text("Enter Customer Name : ")
    model = get_text("Enter Phone Model : ")
    fee = get_fee()

    repair = Repair(
        repair_id,
        customer,
        model,
        fee
    )

    save_repair(repair)
    repairs.append(repair)

    print("Repair Added Successfully!")


def show_repairs(repairs):
    show_pages(repairs)

def search_repair(repairs):
    repair_id = get_number("Enter Repair ID : ")

    repair = find_repair(repairs, repair_id)

    if repair is None:
        print("Repair Not Found")
    else:
        repair.show_info()


def search_by_customer(repairs):
    customer = get_text("Enter Customer Name : ")

    results = find_by_customer(repairs, customer)

    if len(results) == 0:
        print("Repair Not Found")
        return

    for repair in results:
        repair.show_info()


def search_menu(repairs):
    print("\n===== Search =====")
    print("1. Search by ID")
    print("2. Search by Customer")

    choice = input("Choose : ").strip()

    if choice == "1":
        search_repair(repairs)

    elif choice == "2":
        search_by_customer(repairs)

    else:
        print("Invalid Choice")


def update_fee(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET fee = ?
    WHERE id = ?
    """, (repair.fee, repair.id))

    connection.commit()
    connection.close()


def edit_fee(repairs):
    repair_id = get_number("Enter Repair ID : ")

    repair = find_repair(repairs, repair_id)

    if repair is None:
        print("Repair Not Found")
        return

    print(f"Old Fee : {repair.fee}")

    new_fee = get_fee()

    if repair.change_fee(new_fee):
        update_fee(repair)
        print("Fee Updated Successfully!")


def update_status(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET status = ?
    WHERE id = ?
    """, (repair.status, repair.id))

    connection.commit()
    connection.close()


def edit_status(repairs):
    repair_id = get_number("Enter Repair ID : ")

    repair = find_repair(repairs, repair_id)

    if repair is None:
        print("Repair Not Found")
        return

    new_status = get_text(
        "Enter Status (Pending/Done) : "
    ).title()

    if repair.change_status(new_status):
        update_status(repair)
        print("Status Updated Successfully!")


def update_payment(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    UPDATE repairs
    SET payment_status = ?
    WHERE id = ?
    """, (repair.payment, repair.id))

    connection.commit()
    connection.close()


def edit_payment(repairs):
    repair_id = get_number("Enter Repair ID : ")

    repair = find_repair(repairs, repair_id)

    if repair is None:
        print("Repair Not Found")
        return

    new_payment = get_text(
        "Enter Payment (Paid/Unpaid) : "
    ).title()

    if repair.change_payment(new_payment):
        update_payment(repair)
        print("Payment Updated Successfully!")


def delete_from_database(repair):
    connection = sqlite3.connect("repair.db")

    connection.execute("""
    DELETE FROM repairs
    WHERE id = ?
    """, (repair.id,))

    connection.commit()
    connection.close()


def delete_repair(repairs):
    repair_id = get_number("Enter Repair ID : ")

    repair = find_repair(repairs, repair_id)

    if repair is None:
        print("Repair Not Found")
        return

    repair.show_info()

    confirm = input(
        "Delete this repair? (yes/no) : "
    ).strip().lower()

    if confirm == "yes":
        delete_from_database(repair)
        repairs.remove(repair)
        print("Repair Deleted Successfully!")

    else:
        print("Delete Cancelled")


def show_summary(repairs):
    total_repairs = get_total_repairs(repairs)
    pending_count = get_pending_count(repairs)
    done_count = get_done_count(repairs)
    paid_count = get_paid_count(repairs)
    unpaid_count = get_unpaid_count(repairs)
    total_fee = get_total_fee(repairs)
    unpaid_fee = get_unpaid_fee(repairs)

    print("\n===== Repair Summary =====")
    print(f"Total Repairs : {total_repairs}")
    print(f"Pending       : {pending_count}")
    print(f"Done          : {done_count}")
    print(f"Paid          : {paid_count}")
    print(f"Unpaid        : {unpaid_count}")
    print(f"Total Fee     : {total_fee}")
    print(f"Unpaid Fee    : {unpaid_fee}")


def show_pending_repairs(repairs):
    results = get_pending_repairs(repairs)

    if len(results) == 0:
        print("No Pending Repairs")
        return

    for repair in results:
        repair.show_info()


def show_unpaid_repairs(repairs):
    results = get_unpaid_repairs(repairs)

    if len(results) == 0:
        print("No Unpaid Repairs")
        return

    for repair in results:
        repair.show_info()


def sort_by_fee(repairs):
    return sorted(
        repairs,
        key=lambda repair: repair.fee
    )


def sort_by_fee_high_to_low(repairs):
    return sorted(
        repairs,
        key=lambda repair: repair.fee,
        reverse=True
    )


def sort_by_customer(repairs):
    return sorted(
        repairs,
        key=lambda repair: repair.customer
    )


def sort_menu(repairs):
    print("\n===== Sort =====")
    print("1. Fee: Low to High")
    print("2. Fee: High to Low")
    print("3. Customer Name")

    choice = input("Choose : ").strip()

    if choice == "1":
        results = sort_by_fee(repairs)

    elif choice == "2":
        results = sort_by_fee_high_to_low(repairs)

    elif choice == "3":
        results = sort_by_customer(repairs)

    else:
        print("Invalid Choice")
        return

    if len(results) == 0:
        print("No Repairs Found")
        return

    for repair in results:
        repair.show_info()


def show_page(repairs, page, per_page=10):
    start = (page - 1) * per_page

    results = repairs[start:start + per_page]

    for repair in results:
        repair.show_info()


def show_pages(repairs):
    if len(repairs) == 0:
        print("No Repairs Found")
        return

    page = 1
    per_page = 10

    total_pages = math.ceil(len(repairs) / per_page)

    while True:
        print(f"\n===== Page {page} / {total_pages} =====")

        show_page(repairs, page, per_page)

        print("\nN. Next Page")
        print("P. Previous Page")
        print("Q. Quit")

        choice = input("Choose : ").strip().lower()

        if choice == "n":
            if page < total_pages:
                page += 1
            else:
                print("Already at last page")

        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("Already at first page")

        elif choice == "q":
            break

        else:
            print("Invalid Choice")


create_table()

repairs = load_repairs()


while True:
    print("\n===== Repair Manager =====")
    print("1. Add Repair")
    print("2. Show Repairs")
    print("3. Search")
    print("4. Update Fee")
    print("5. Update Status")
    print("6. Update Payment")
    print("7. Delete Repair")
    print("8. Summary")
    print("9. Pending Repairs")
    print("10. Unpaid Repairs")
    print("11. Sort")
    print("12. View Pages")
    print("13. Exit")

    choice = input("Choose : ").strip()

    if choice == "1":
        add_repair(repairs)

    elif choice == "2":
        show_repairs(repairs)

    elif choice == "3":
        search_menu(repairs)

    elif choice == "4":
        edit_fee(repairs)

    elif choice == "5":
        edit_status(repairs)

    elif choice == "6":
        edit_payment(repairs)

    elif choice == "7":
        delete_repair(repairs)

    elif choice == "8":
        show_summary(repairs)

    elif choice == "9":
        show_pending_repairs(repairs)

    elif choice == "10":
        show_unpaid_repairs(repairs)

    elif choice == "11":
        sort_menu(repairs)

    elif choice == "12":
        show_pages(repairs)

    elif choice == "13":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")