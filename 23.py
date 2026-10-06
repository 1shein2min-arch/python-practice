name = input("Enter Name")
level = int(input("Enter Level"))
gold = int(input("Enter Gold"))
has_Key = input("Enter Has Key(yes/no)").lower()
if level <10 :
    print("Beginner")
elif level< 49:
    print("Warrior")
else:
    if gold>= 1000 and has_Key == "yes" :
        print("Legendary Player")
    else :
        print("Master Player")


