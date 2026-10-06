repairs = [
    ("iPhone 11", "SheiN", 30000, "Done"),
    ("Redmi Note 13", "Aung", 50000, "Pending"),
    ("Vivo Y55", "Mg Mg", 25000, "Done"),
    ("Samsung A52", "Ko Ko", 80000, "Pending"),
    ("Redmi 12", "Aung", 35000, "Done")
]

fees = 0
pending_fees = 0
done_fees = 0
done_count = 0
pending_count = 0
for item in repairs:
    model,name,fee,status = item
    if status == "Pending" :
        pending_fees = pending_fees + fee
        pending_count = pending_count + 1
        
    elif status == "Done" :
        done_fees = done_fees + fee
        done_count = done_count + 1

total = pending_count + done_count
print(f"Total Repairs : {total}")
print(f"Done Repairs : {done_count}")
print(f"Pending Repairs : {pending_count}")

total_fees = pending_fees + done_fees

print(f"Total Repair Fee : {total_fees}")