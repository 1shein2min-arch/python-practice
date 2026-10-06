class Repair:
    def __init__(self, customer, model, fee, status):
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = status

    def change_status(self, new_status):
        self.status = new_status

    def show_info(self):
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")


repair1 = Repair("Aung", "Redmi Note 13", 50000, "Pending")

repair1.show_info()

print()

repair1.change_status("Done")

repair1.show_info()