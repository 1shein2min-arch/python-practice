class Repair:
    def __init__(self, repair_id, customer, model, fee):
        self.id = repair_id
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"
        self.payment = "Unpaid"

    def get_discount(self):
        if self.fee >= 100000 :
            return self.fee * 5/100
        else :
            return 0

    def total(self) :
        discount = self.get_discount()
        total = self.fee - discount
        return total

    def show_info(self):
        print(f"ID       : {self.id}")
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Discount : {self.get_discount()}")
        print(f"Total    : {self.get_total()}")
        print(f"Status   : {self.status}")
        print(f"Payment  : {self.payment}")


repair1 = Repair(1, "Aung", "Redmi", 50000)
repair2 = Repair(2, "Mg Mg", "iPhone 11", 120000)
repair3 = Repair(3, "Ko Ko", "Samsung A52", 200000)

repairs = [repair1,repair2,repair3]

search_id = 3 

for repair in repairs :
    if repair.id == search_id :
        print(repair.get_discount())
        print(repair.total())