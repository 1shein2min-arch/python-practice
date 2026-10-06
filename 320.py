print("1. Phone Price")
print("2. Repair Fee")
print("3. Parts Fee")

phone_price = int(input("Enter Phone Price :"))
repair_fee = int(input("Enter Repair Fee :"))
parts_fee = int(input("Enter Parts Fee :"))

def total(phone_price,repair_fee,parts_fee) :
    return phone_price + repair_fee + parts_fee


print(f"Total : {total(phone_price,repair_fee,parts_fee)}")