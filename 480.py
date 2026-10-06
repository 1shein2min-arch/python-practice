class Repair:
    def __init__(self, repair_id, customer, model, fee):
        self.id = repair_id
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"

    def change_fee(self, new_fee):
        if new_fee < 0 :
            print("Invalid Fee")
        else :
            self.fee = new_fee
            print("Fee Updated")

    def show_info(self):
        print(f"ID       : {self.id}")
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")


repair1 = Repair(1, "Aung", "Redmi", 50000)
repair2 = Repair(2, "Mg Mg", "iPhone 11", 80000)
repair3 = Repair(3, "Ko Ko", "Samsung A52", 100000)

repairs = [repair1, repair2, repair3]

search_id = 3

for repair in repairs:
    if repair.id == search_id :
        repair.change_fee(150000)
        repair.show_info()