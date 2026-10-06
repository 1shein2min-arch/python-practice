import csv

from database import (
    create_table,
    load_repairs,
    save_repair,
    update_fee,
    update_status,
    update_payment,
    delete_from_database
)

from models import Repair

from validators import (
    get_number,
    get_fee,
    get_text
)

from services import (
    find_repair,
    find_by_customer,
    search_customer,
    search_by_model,
    get_pending_repairs,
    get_unpaid_repairs,
    get_total_repairs,
    get_pending_count,
    get_done_count,
    get_total_fee,
    get_average_fee,
    get_paid_fee,
    get_unpaid_fee,
    sort_by_fee,
    sort_by_fee_high_to_low,
    sort_by_customer,
    get_by_status,
    get_by_payment,
    get_today_repairs
)


create_table()
repairs = load_repairs()


def add_repair():
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


def show_repairs():
    if len(repairs) == 0:
        print("No Repairs Found")
        return

    for repair in repairs:
        repair.show_info()


def search_repair():
    repair_id = get_number("Enter Repair ID : ")

    repair = find_repair(repairs, repair_id)

    if repair is None:
        print("Repair Not Found")
    else:
        repair.show_info()


def search_by_customer():
    customer = get_text("Enter Customer Name : ")

    results = find_by_customer(repairs, customer)

    if len(results) == 0:
        print("Repair Not Found")
        return

    for repair in results:
        repair.show_info()


def search_customer_partial():
    keyword = get_text("Enter Customer Keyword : ")

    results = search_customer(repairs, keyword)

    if len(results) == 0:
        print("Repair Not Found")
        return

    for repair in results:
        repair.show_info()


def search_model():
    keyword = get_text("Enter Model Keyword : ")

    results = search_by_model(repairs, keyword)

    if len(results) == 0:
        print("Repair Not Found")
        return

    for repair in results:
        repair.show_info()


def search_menu():
    print("\n===== Search =====")
    print("1. Search by ID")
    print("2. Search by Customer")
    print("3. Search Customer Keyword")
    print("4. Search Model Keyword")

    choice = input("Choose : ").strip()

    if choice == "1":
        search_repair()

    elif choice == "2":
        search_by_customer()

    elif choice == "3":
        search_customer_partial()

    elif choice == "4":
        search_model()

    else:
        print("Invalid Choice")


def show_pending_repairs():
    results = get_pending_repairs(repairs)

    if len(results) == 0:
        print("No Pending Repairs")
        return

    for repair in results:
        repair.show_info()


def show_unpaid_repairs():
    results = get_unpaid_repairs(repairs)

    if len(results) == 0:
        print("No Unpaid Repairs")
        return

    for repair in results:
        repair.show_info()


def show_by_status():
    status = get_text(
        "Enter Status (Pending/Done) : "
    ).title()

    results = get_by_status(repairs, status)

    if len(results) == 0:
        print("No Repairs Found")
        return

    for repair in results:
        repair.show_info()


def show_by_payment():
    payment = get_text(
        "Enter Payment (Paid/Unpaid) : "
    ).title()

    results = get_by_payment(repairs, payment)

    if len(results) == 0:
        print("No Repairs Found")
        return

    for repair in results:
        repair.show_info()


def show_today_repairs():
    results = get_today_repairs(repairs)

    if len(results) == 0:
        print("No Repairs Today")
        return

    for repair in results:
        repair.show_info()


def show_summary():
    total_repairs = get_total_repairs(repairs)
    pending_count = get_pending_count(repairs)
    done_count = get_done_count(repairs)
    total_fee = get_total_fee(repairs)
    average_fee = get_average_fee(repairs)
    paid_fee = get_paid_fee(repairs)
    unpaid_fee = get_unpaid_fee(repairs)

    print("\n===== Repair Summary =====")
    print(f"Total Repairs : {total_repairs}")
    print(f"Pending       : {pending_count}")
    print(f"Done          : {done_count}")
    print(f"Total Fee     : {total_fee}")
    print(f"Average Fee   : {average_fee}")
    print(f"Paid Fee      : {paid_fee}")
    print(f"Unpaid Fee    : {unpaid_fee}")


def sort_menu():
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


def edit_fee():
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


def edit_status():
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


def edit_payment():
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


def delete_repair_from_list():
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


def export_csv():
    with open("repairs.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Customer",
            "Model",
            "Fee",
            "Status",
            "Payment",
            "Date"
        ])

        rows = []

        for repair in repairs:
            rows.append([
                repair.id,
                repair.customer,
                repair.model,
                repair.fee,
                repair.status,
                repair.payment,
                repair.date
            ])

        writer.writerows(rows)

    print("CSV Exported Successfully!")


def show_menu():
    print("\n===== Repair Manager =====")
    print("1. Add Repair")
    print("2. Show Repairs")
    print("3. Search")
    print("4. Update Fee")
    print("5. Update Status")
    print("6. Update Payment")
    print("7. Summary")
    print("8. Pending Repairs")
    print("9. Unpaid Repairs")
    print("10. Sort")
    print("11. Delete Repair")
    print("12. Show by Status")
    print("13. Show by Payment")
    print("14. Today's Repairs")
    print("15. Export CSV")
    print("16. Exit")


while True:
    show_menu()

    choice = input("Choose : ").strip()

    if choice == "1":
        add_repair()

    elif choice == "2":
        show_repairs()

    elif choice == "3":
        search_menu()

    elif choice == "4":
        edit_fee()

    elif choice == "5":
        edit_status()

    elif choice == "6":
        edit_payment()

    elif choice == "7":
        show_summary()

    elif choice == "8":
        show_pending_repairs()

    elif choice == "9":
        show_unpaid_repairs()

    elif choice == "10":
        sort_menu()

    elif choice == "11":
        delete_repair_from_list()

    elif choice == "12":
        show_by_status()

    elif choice == "13":
        show_by_payment()

    elif choice == "14":
        show_today_repairs()

    elif choice == "15":
        export_csv()

    elif choice == "16":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")