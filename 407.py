def show_repair(**repair) :
    print(repair['customer'])
    print(repair['model'])
    print(repair['fee'])

show_repair(
    customer = "Aung",
    model = "Redmi Note 13",
    fee = 50000
)