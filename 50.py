while True :
    mark = int(input("Enter Marks"))
    if mark< -1 :
        print("Invalid Mark")
        continue
    elif mark == -1 :
        print("Exit")
        break
    elif mark < 40 :
        print("Fail")
    elif mark < 60 :
        print("Pass")
    elif mark < 80 :
        print("Good")
    elif mark <= 100 :
        print("Excellent")
    else :
        print("Invalid Mark")
        continue