class Phone:

    def __init__(self, model, price):
        self.model = model
        self.price = price


phone1 = Phone("iPhone 11", 300000)

print(phone1.model)
print(phone1.price)

phone2 = Phone("Redmi Note 13",500000)

print(phone2.model)
print(phone2.price)