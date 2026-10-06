class Repair:
    def __init__(self, customer, model, fee):
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"

    def show_info(self):
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")


repairs = []

repair1 = Repair("Aung", "Redmi", 50000)
repair2 = Repair("Mg Mg", "iPhone 11", 80000)
repair3 = Repair("Aung", "Samsung A55", 120000)

repairs.append(repair1)
repairs.append(repair2)
repairs.append(repair3)

for repair in repairs :
    if repair.status == "Pending" :
        repair.show_info()