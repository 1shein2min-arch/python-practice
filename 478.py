class Repair:
    def __init__(self, customer, model, fee):
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"

    def change_status(self, new_status):
        self.status = new_status

    def show_info(self):
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")


repair1 = Repair("Aung", "Redmi", 50000)
repair2 = Repair("Mg Mg", "iPhone 11", 80000)
repair3 = Repair("Ko Ko", "Samsung A52", 100000)

repairs = [repair1, repair2, repair3]

for repair in repairs :
    if repair.customer == "Ko Ko" :
        repair.status = "Done"
        print(repair.show_info())