age = int(input("Enter Age :"))

def check_age(age) :
    if age < 18 :
        raise ValueError ("Age Must Be 18 or Older")
    print("Valid Age")
try :
    check_age(age)

except ValueError as error :
    print(error)

