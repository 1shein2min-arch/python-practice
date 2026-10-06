phone_price = int(input("Enter Phone Price :"))
repair_fee = int(input("Enter Repair Fee :"))
parts_fee = int(input("Enter Parts Fee :"))

def total(phone_price,repair_fee,parts_fee) :
    return phone_price + repair_fee + parts_fee

def discount(total) :
    if total >= 500000 :
        return total * 10/100
    elif total >= 100000 :
        return total * 5/100
    else :
        return 0

total1 = total(phone_price,repair_fee,parts_fee) 
    
print(f"Total : {total1}")

discount1 = discount(total1)

print(f"Discount : {discount1}")

final_price = total1 - discount1

print(f"Final Price : {final_price}")

def tax(final_price) :
    return final_price * 5/100

tax_price = tax(final_price)

grand_total = final_price + tax_price

print(f"Grand Total : {grand_total}")