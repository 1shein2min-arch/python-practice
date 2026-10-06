def show_page (repairs,page,per_page=10) :
    start = (page - 1) * per_page

    results = repairs[start:start + per_page]

    for repair in results:
        repair.show_info()

def show_pages(repairs) :

    page = 1 
    per_page = 10

    while True:
        show_page(repairs, page, per_page)

        print("N. Next Page")
        print("P. Previous Page")
        print("Q. Quit")

        choice = input("Choose :").lower().strip()

        if choice == "n":
            page += 1

        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("Already at first page.")

        elif choice == "q":
            break

        else :
            print("Invalid choice. Please try again.")