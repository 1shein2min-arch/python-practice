class Repair:
    def __init__(self, repair_id, customer, model, fee):
        self.id = repair_id
        self.customer = customer
        self.model = model
        self.fee = fee
        self.status = "Pending"
        self.payment = "Unpaid"

    def receive_payment(self,new_payment):
        if self.payment == "Paid" or self.payment == "Unpaid" :
            self.payment = new_payment
            print("Payment Updated")

        else :
            print("Invalid Payment")

    def show_info(self):
        print(f"ID       : {self.id}")
        print(f"Customer : {self.customer}")
        print(f"Model    : {self.model}")
        print(f"Fee      : {self.fee}")
        print(f"Status   : {self.status}")
        print(f"Payment  : {self.payment}")


repair1 = Repair(1, "Aung", "Redmi", 50000)
repair2 = Repair(2, "Mg Mg", "iPhone 11", 80000)
repair3 = Repair(3, "Ko Ko", "Samsung A52", 100000)

repairs = [repair1, repair2, repair3]

search_id = 3

for repair in repairs :
    if repair.id == search_id :
        repair.receive_payment("Paid")
        repair.show_info()