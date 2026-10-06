class Phone:
    def __init__(self, model, price, brand):
        self.model = model
        self.price = price
        self.brand = brand

    def change_price(self, new_price):
        self.price = new_price

phone1 = Phone("Xiaomi",500000,"Redmi")

phone1.change_price(450000)

print(phone1.price)