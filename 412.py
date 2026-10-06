class Phone :

    def ___init___(self,model,price) :
        self.model = model
        self.price = price

    def show_phone(self) :
        print(self.model)
        print(self.price)

phone1 = Phone("iphone 11",30000)

phone1.show_phone()