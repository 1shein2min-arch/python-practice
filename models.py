from datetime import date

class Repair:
    def __init__(self, repair_id, customer, model, fee):
        self.id = repair_id
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"
        self.payment = "Unpaid"
        self.date = date.today().isoformat()

    def change_fee(self, new_fee):
        if new_fee < 0:
            print("Invalid Fee")
            return False

        self.fee = new_fee
        return True

    def change_status(self, new_status):
        if new_status == "Pending" or new_status == "Done":
            self.status = new_status
            return True

        print("Invalid Status")
        return False

    def change_payment(self, new_payment):
        if new_payment == "Paid" or new_payment == "Unpaid":
            self.payment = new_payment
            return True

        print("Invalid Payment")
        return False

    def show_info(self):
        print(f"ID       : {self.id}")
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")
        print(f"Payment  : {self.payment}")
        print(f"Date     : {self.date}")
        print("-" * 30)

