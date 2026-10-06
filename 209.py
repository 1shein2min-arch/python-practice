def shop_name():
    print("Shop Name : ShieN Store")

def show_products() :
    print("Phone")
    print("Laptop")
    print("Tablet")
    print("Watch")

def opening_hours() :
    print("Opening Hours")
    print("9:00 AM - 8:00PM")

def exit():
    print("Goodbye!")

while True:
    print("===== Shop Menu =====")
    print("1. Show Shop Name")
    print("2. Shoe Products")
    print("3. Show Opening Hours")
    print("4. Exit")

    choice = int(input("Enter Choose :"))
    if choice == 1 :
        shop_name()

    elif choice == 2 :
        show_products()

    elif choice == 3 :
        opening_hours()

    elif choice == 4 :
        exit()

    else :
        print("Invalid Choice")