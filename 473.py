class Repair:
    def __init__(self, customer, model, fee):
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"

repair1 = Repair("Aung", "Redmi", 50000)