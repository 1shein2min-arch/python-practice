hero = input("Enter hero warrior/mage/archer")
enemy_armor = int(input("Enter Enemy Armor"))
use_ultimate = int(input("Use Ultimate yes/no?"))
if hero != "warrior" and hero !="mage" and hero != "archer":
    print("Invalid Hero")
elif enemy_armor<0 :
    print("Invalid Armor")
elif use_ultimate != "Yes" and use_ultimate != "No":
    print("Invalid Ultimate")
else:
    if

