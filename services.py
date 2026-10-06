from datetime import date

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


def get_total_fee(repairs):
    total = 0

    for repair in repairs:
        total += repair.fee

    return total

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
        key=lambda repair: repair.customer.lower()
    )

def get_by_status(repairs, status):
    results = []

    for repair in repairs:
        if repair.status == status:
            results.append(repair)

    return results

def get_by_payment(repairs, payment):
    results = []

    for repair in repairs:
        if repair.payment == payment:
            results.append(repair)

    return results

def search_customer(repairs, keyword):
    results = []

    for repair in repairs:
        if keyword.lower() in repair.customer.lower():
            results.append(repair)

    return results

def search_by_model(repairs, keyword):
    results = []

    for repair in repairs:
        if keyword.lower() in repair.model.lower():
            results.append(repair)

    return results

def get_average_fee(repairs):
    if len(repairs) == 0:
        return 0

    total = 0

    for repair in repairs:
        total += repair.fee

    return total / len(repairs)

def get_paid_fee(repairs):
    total = 0

    for repair in repairs:
        if repair.payment == "Paid":
            total += repair.fee

    return total

def get_unpaid_fee(repairs):
    total = 0

    for repair in repairs:
        if repair.payment == "Unpaid":
            total += repair.fee

    return total

def get_today_repairs(repairs):
    results = []

    today = date.today().isoformat()

    for repair in repairs:
        if repair.date == today:
            results.append(repair)

    return results

def get_today_repairs(repairs):
    results = []

    today = date.today().isoformat()

    for repair in repairs:
        if repair.date == today:
            results.append(repair)

    return results
