while True :
    age = int(input("Enter age"))
    if age < 0 :
        print("Invalid Age")
        continue
    elif age == 0 :
        print("Exit")
        break
    elif age < 18 :
        print("Minor")
    elif age < 60 :
        print("Adult")
    else :
        print("Senior")
