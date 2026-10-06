repairs = []

next_id = 1

customer = input("Customer Name : ")
model = input("Phone Model : ")
fee = int(input("Repair Fee : "))

repair = {
    "id": next_id,
    "customer": customer,
    "model": model,
    "fee": fee
}

repairs.append(repair)

next_id =next_id + 1

print(repairs)