repairs = [
    {
        "id": 1,
        "customer": "Aung",
        "model": "Redmi Note 13",
        "fee": 50000,
        "parts_fee": 10000
    },
    {
        "id": 2,
        "customer": "Ko Ko",
        "model": "Vivo Y55",
        "fee": 30000,
        "parts_fee": 5000
    }
]

def calculate_fee(fee,parts_fee) :
    total_fee = fee + parts_fee

    if total_fee >= 500000 :
        discount = 10
    elif total_fee >= 100000 :
        discount = 5
    else :
        discount = 0

    discount_amount = total_fee * discount/100
    after_discount = total_fee - discount_amount

    tax_percent = 5
    tax_amount = after_discount * tax_percent/100

    final_fee = after_discount + tax_amount

    return total_fee,discount_amount,tax_amount,final_fee

def edit_repair() :
    repair_id = int(input("Enter Repair ID :"))
    customer = input("Enter New Customer :")
    model = input("Enter New Model :")
    repair_fee = int(input("Enter New Repair Fee :"))
    new_parts_fee = int(input("Enter New Parts Fee : "))

    found = False
                
    for repair in repairs :
        if repair['id'] == repair_id:
            repair['customer'] = customer
            repair['model'] = model
            repair['fee'] = repair_fee
            repair['parts_fee'] = new_parts_fee
            total_fee,discount_amount,tax_amount,final_fee = calculate_fee(repair_fee,new_parts_fee)

            repair['total_fee'] = total_fee
            repair['discount_amount'] = discount_amount
            repair['tax_amount'] = tax_amount
            repair['final_fee'] = final_fee

            found = True

    if found == False :
        print("Repair ID Not Found")

                       

    