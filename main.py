import json
from datetime import datetime


def load_repairs():
    try:
        with open("repairs.json", "r") as file:
            repairs_data = json.load(file)

            for index, repair in enumerate(repairs_data, start=1):
                if "id" not in repair:
                    repair["id"] = index

            return repairs_data

    except FileNotFoundError:
        return []


def save_repairs():
    with open("repairs.json", "w") as file:
        json.dump(repairs, file, indent=4)


def get_next_id():
    next_id = 1

    for repair in repairs:
        if repair["id"] >= next_id:
            next_id = repair["id"] + 1

    return next_id


def get_positive_number(message):
    while True:
        try:
            number = int(input(message))

            if number <= 0:
                print("Number must be greater than 0")
                continue

            return number

        except ValueError:
            print("Please enter a number")


def get_non_negative_number(message):
    while True:
        try:
            number = int(input(message))

            if number < 0:
                print("Number cannot be negative")
                continue

            return number

        except ValueError:
            print("Please enter a number")


def get_non_empty_text(message):
    while True:
        text = input(message).strip()

        if text == "":
            print("Input cannot be empty")
            continue

        return text


def get_phone_number(message):
    while True:
        phone_num = input(message).strip()

        if phone_num.isdigit():
            return phone_num

        print("Please enter numbers only")


def get_status(message):
    while True:
        status = input(message).lower().strip()

        if status == "done":
            return "Done"

        elif status == "pending":
            return "Pending"

        else:
            print("Invalid Status")


def calculate_fee(fee, parts_fee):
    total_fee = fee + parts_fee

    if total_fee >= 500000:
        discount = 10
    elif total_fee >= 100000:
        discount = 5
    else:
        discount = 0

    discount_amount = total_fee * discount / 100
    after_discount = total_fee - discount_amount

    tax_percent = 5
    tax_amount = after_discount * tax_percent / 100

    final_fee = after_discount + tax_amount

    return total_fee, discount_amount, tax_amount, final_fee


def edit_repair():
    repair_id = get_positive_number("Enter Repair ID : ")

    found = False

    for repair in repairs:
        if repair["id"] == repair_id:
            customer = get_non_empty_text("New Customer Name : ")
            phone = get_phone_number("New Customer Phone : ")
            model = get_non_empty_text("New Phone Model : ")
            fee = get_positive_number("New Repair Fee : ")
            parts_fee = get_non_negative_number("New Parts Fee : ")

            total_fee, discount_amount, tax_amount, final_fee = calculate_fee(
                fee,
                parts_fee
            )

            if total_fee >= 500000:
                discount_percent = 10
            elif total_fee >= 100000:
                discount_percent = 5
            else:
                discount_percent = 0

            repair["customer"] = customer
            repair["phone"] = phone
            repair["model"] = model
            repair["fee"] = fee
            repair["parts_fee"] = parts_fee
            repair["total_fee"] = total_fee
            repair["discount_percent"] = discount_percent
            repair["discount_amount"] = discount_amount
            repair["tax_percent"] = 5
            repair["tax_amount"] = tax_amount
            repair["final_fee"] = final_fee

            save_repairs()

            print("Repair updated successfully!")
            found = True
            break

    if found == False:
        print("Repair ID not found")


def show_summary():
    total_repairs = len(repairs)

    pending_count = 0
    done_count = 0

    total_revenue = 0
    paid_revenue = 0
    unpaid_revenue = 0

    for repair in repairs:
        final_fee = repair.get(
            "final_fee",
            repair.get("fee", 0) + repair.get("parts_fee", 0)
        )

        total_revenue += final_fee

        if repair["status"] == "Pending":
            pending_count += 1

        elif repair["status"] == "Done":
            done_count += 1

        payment_status = repair.get("payment_status", "Unpaid")

        if payment_status == "Paid":
            paid_revenue += final_fee
        else:
            unpaid_revenue += final_fee

    print("\n===== Repair Summary =====")
    print(f"Total Repairs : {total_repairs}")
    print(f"Pending : {pending_count}")
    print(f"Done : {done_count}")
    print(f"Total Revenue : {total_revenue}")
    print(f"Paid Revenue : {paid_revenue}")
    print(f"Unpaid Amount : {unpaid_revenue}")


repairs = load_repairs()


while True:
    print("\n===== Phone Repair Manager =====")
    print("1. Add Repair")
    print("2. View Repairs")
    print("3. Search Customer")
    print("4. Search by Repair ID")
    print("5. Edit Repair")
    print("6. Update Status")
    print("7. Delete Repair")
    print("8. Pending Repairs")
    print("9. Done Repairs")
    print("10. Repair Summary")
    print("11. Mark Payment")
    print("12. Exit")

    choice = input("Choose : ")

    if choice == "1":
        customer = get_non_empty_text("Customer Name : ")
        phone = get_phone_number("Customer Phone : ")
        model = get_non_empty_text("Phone Model : ")

        fee = get_positive_number("Repair Fee : ")
        parts_fee = get_non_negative_number("Parts Fee : ")

        status = get_status("Status (Pending/Done) : ")

        total_fee, discount_amount, tax_amount, final_fee = calculate_fee(
            fee,
            parts_fee
        )

        if total_fee >= 500000:
            discount_percent = 10
        elif total_fee >= 100000:
            discount_percent = 5
        else:
            discount_percent = 0

        current_time = datetime.now()
        repair_date = current_time.strftime("%d/%m/%Y")
        repair_time = current_time.strftime("%H:%M:%S")

        repair_id = get_next_id()

        repair = {
            "id": repair_id,
            "customer": customer,
            "phone": phone,
            "model": model,
            "fee": fee,
            "parts_fee": parts_fee,
            "total_fee": total_fee,
            "discount_percent": discount_percent,
            "discount_amount": discount_amount,
            "tax_percent": 5,
            "tax_amount": tax_amount,
            "final_fee": final_fee,
            "status": status,
            "payment_status": "Unpaid",
            "date": repair_date,
            "time": repair_time
        }

        repairs.append(repair)
        save_repairs()

        print("\nRepair added successfully!")
        print(f"ID : {repair_id}")
        print(f"Final Fee : {final_fee}")
        print(f"Repair Status : {status}")
        print("Payment Status : Unpaid")

    elif choice == "2":
        print("\n===== Repair List =====")

        if len(repairs) == 0:
            print("No repairs found")
        else:
            for repair in repairs:
                repair_fee = repair.get("fee", 0)
                parts_fee = repair.get("parts_fee", 0)

                total_fee = repair.get(
                    "total_fee",
                    repair_fee + parts_fee
                )

                discount_percent = repair.get("discount_percent", 0)
                discount_amount = repair.get("discount_amount", 0)

                tax_percent = repair.get("tax_percent", 0)
                tax_amount = repair.get("tax_amount", 0)

                final_fee = repair.get(
                    "final_fee",
                    repair_fee + parts_fee
                )

                payment_status = repair.get(
                    "payment_status",
                    "Unpaid"
                )

                print(f"ID : {repair['id']}")
                print(f"Customer : {repair['customer']}")
                print(f"Phone : {repair.get('phone', 'Old Record')}")
                print(f"Model : {repair['model']}")
                print(f"Repair Fee : {repair_fee}")
                print(f"Parts Fee : {parts_fee}")
                print(f"Total Fee : {total_fee}")
                print(f"Discount : {discount_percent}%")
                print(f"Discount Amount : {discount_amount}")
                print(f"Tax : {tax_percent}%")
                print(f"Tax Amount : {tax_amount}")
                print(f"Final Fee : {final_fee}")
                print(f"Repair Status : {repair['status']}")
                print(f"Payment Status : {payment_status}")
                print(f"Date : {repair.get('date', 'Old Record')}")
                print(f"Time : {repair.get('time', 'Old Record')}")
                print("--------------------")

    elif choice == "3":
        search_name = get_non_empty_text(
            "Enter Customer Name : "
        ).lower()

        found = False

        print("\n===== Search Result =====")

        for repair in repairs:
            if search_name in repair["customer"].lower():
                final_fee = repair.get(
                    "final_fee",
                    repair.get("fee", 0) + repair.get("parts_fee", 0)
                )

                payment_status = repair.get(
                    "payment_status",
                    "Unpaid"
                )

                print(f"ID : {repair['id']}")
                print(f"Customer : {repair['customer']}")
                print(f"Phone : {repair.get('phone', 'Old Record')}")
                print(f"Model : {repair['model']}")
                print(f"Final Fee : {final_fee}")
                print(f"Repair Status : {repair['status']}")
                print(f"Payment Status : {payment_status}")
                print(f"Date : {repair.get('date', 'Old Record')}")
                print(f"Time : {repair.get('time', 'Old Record')}")
                print("--------------------")

                found = True

        if found == False:
            print("Customer not found")

    elif choice == "4":
        repair_id = get_positive_number("Enter Repair ID : ")

        found = False

        for repair in repairs:
            if repair["id"] == repair_id:
                final_fee = repair.get(
                    "final_fee",
                    repair.get("fee", 0) + repair.get("parts_fee", 0)
                )

                print("\n===== Repair Found =====")
                print(f"ID : {repair['id']}")
                print(f"Customer : {repair['customer']}")
                print(f"Phone : {repair.get('phone', 'Old Record')}")
                print(f"Model : {repair['model']}")
                print(f"Repair Fee : {repair.get('fee', 0)}")
                print(f"Parts Fee : {repair.get('parts_fee', 0)}")
                print(f"Final Fee : {final_fee}")
                print(f"Repair Status : {repair['status']}")
                print(
                    f"Payment Status : "
                    f"{repair.get('payment_status', 'Unpaid')}"
                )
                print(f"Date : {repair.get('date', 'Old Record')}")
                print(f"Time : {repair.get('time', 'Old Record')}")

                found = True
                break

        if found == False:
            print("Repair ID not found")

    elif choice == "5":
        edit_repair()

    elif choice == "6":
        repair_id = get_positive_number("Enter Repair ID : ")

        found = False

        for repair in repairs:
            if repair["id"] == repair_id:
                status = get_status(
                    "New Status (Pending/Done) : "
                )

                repair["status"] = status
                save_repairs()

                print("Repair status updated successfully!")
                found = True
                break

        if found == False:
            print("Repair ID not found")

    elif choice == "7":
        repair_id = get_positive_number("Enter Repair ID : ")

        found = False

        for repair in repairs:
            if repair["id"] == repair_id:
                repairs.remove(repair)
                save_repairs()

                print("Repair deleted successfully!")
                found = True
                break

        if found == False:
            print("Repair ID not found")

    elif choice == "8":
        print("\n===== Pending Repairs =====")

        found = False

        for repair in repairs:
            if repair["status"] == "Pending":
                final_fee = repair.get(
                    "final_fee",
                    repair.get("fee", 0) + repair.get("parts_fee", 0)
                )

                print(f"ID : {repair['id']}")
                print(f"Customer : {repair['customer']}")
                print(f"Phone : {repair.get('phone', 'Old Record')}")
                print(f"Model : {repair['model']}")
                print(f"Final Fee : {final_fee}")
                print("--------------------")

                found = True

        if found == False:
            print("No pending repairs")

    elif choice == "9":
        print("\n===== Done Repairs =====")

        found = False

        for repair in repairs:
            if repair["status"] == "Done":
                final_fee = repair.get(
                    "final_fee",
                    repair.get("fee", 0) + repair.get("parts_fee", 0)
                )

                print(f"ID : {repair['id']}")
                print(f"Customer : {repair['customer']}")
                print(f"Phone : {repair.get('phone', 'Old Record')}")
                print(f"Model : {repair['model']}")
                print(f"Final Fee : {final_fee}")
                print("--------------------")

                found = True

        if found == False:
            print("No done repairs")

    elif choice == "10":
        show_summary()

    elif choice == "11":
        repair_id = get_positive_number("Enter Repair ID : ")

        found = False

        for repair in repairs:
            if repair["id"] == repair_id:
                repair["payment_status"] = "Paid"
                save_repairs()

                print("Payment updated successfully!")
                found = True
                break

        if found == False:
            print("Repair ID not found")

    elif choice == "12":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")