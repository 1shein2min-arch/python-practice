class Repair:
    def __init__(self, customer, model, fee):
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"

    def add_fee(self, amount):
        self.fee = self.fee + amount

    def complete_repair(self):
        self.status = "Done"

    def show_info(self):
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")


repair1 = Repair("Aung", "Redmi", 50000)

repair1.add_fee(10000)
repair1.complete_repair()

repair1.show_info()