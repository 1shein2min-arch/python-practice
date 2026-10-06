def get_pending_unpaid_total_fee(repairs):
    total = 0

    for repair in repairs :
        if repair.status == "Pending" and repair.payment == "Unpaid" :
            total += repair.fee
    return total
