def toggle_payment_status(payment_status) :
    if payment_status == "unpaid" :
        return "paid"
    else :
        return "unpaid"
payment_status = "paid"

payment_status = toggle_payment_status(payment_status)

print(payment_status)