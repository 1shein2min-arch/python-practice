def get_number(message):
    while True:
        try:
            number = int(input(message))

            if number < 0:
                print("Number Cannot Be Negative")
            else:
                return number

        except ValueError:
            print("Please Enter a Number")


def get_fee():
    while True:
        try:
            fee = int(input("Enter Fee : "))

            if fee < 0:
                print("Fee Cannot Be Negative")
            else:
                return fee

        except ValueError:
            print("Please Enter a Number")


def get_text(message):
    while True:
        text = input(message).strip()

        if text == "":
            print("This Field Cannot Be Empty")
        else:
            return text