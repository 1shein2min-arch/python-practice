def calculate_repair(*fee,**repair) :
    print("Customer",repair['customer'])
    print("Model" , repair['model'])
    print(sum(fee))

calculate_repair(
    30000,
    20000,
    10000,
    customer = "Aung",
    model = "iPhone 11"
)

