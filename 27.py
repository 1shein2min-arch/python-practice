mark = 0
mark = int(input("Mark"))
while mark<=100:
    if mark<50:
        print("Fail")
    elif mark<80:
        print("Pass")
    else:
        print("Excellent")
    mark = mark + 10