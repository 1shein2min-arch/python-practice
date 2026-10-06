def check_parts_fee(fee) :
    if fee<= 0 :
        raise ValueError ("Parts Fee Cannot Be Negative")
    return fee

fee = int(input("Enter Fee :"))

try :
    check_parts_fee(fee)
    print("Valid Fee")

except ValueError as error :
    print(error)
