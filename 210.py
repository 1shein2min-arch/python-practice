def shop_name () :
    print("Shop Name : SheiN Phone Shop")

def show_phones() :
    print("Phones :")
    print("Redmi Note 13 Pro")
    print("Vivo Y55A")
    print("Samsung S24 Ultra")
    print("iPhone 15")

def show_address() :
    print("Address:")
    print("Amarapura")

def opening_hours () :
    print("Opening Hours :")
    print("9:00 AM - 8:00 PM")

def goodbye() :
    print("Goodbye!")

while True :
    print("===== Phone Shop =====")

    print("1. Show Shop Name")
    print("2. Show Phones")
    print("3. Show Address")
    print("4. Show Opening Hours")
    print("5. Exit")

    choice = int(input("Enter Choose :"))
    if choice == 1 :
        shop_name()

    elif choice == 2 :
        show_phones()

    elif choice == 3 :
        show_address()

    elif choice == 4 :
        opening_hours()

    elif choice == 5 :
        goodbye()
        break

    else :
        print("Invalid Choice")