price = int(input("Enter Price :"))

def calculate_discount(price) :
    if price >= 100000 :
        discount = price * 10/100
        return discount
    else :
        return 0

print(calculate_discount(price))