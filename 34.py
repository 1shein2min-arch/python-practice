mark = int(input("Enter Marks :"))
while mark <= 100:
    if mark >= 80 :
        print(f"{mark} - Excellent")
    elif mark >= 60 :
        print(f"{mark} - Good")
    elif mark >= 40 :
        print(f"{mark} - Pass")
    else :
        print(f"{mark} - Fail")
    mark = mark + 10
