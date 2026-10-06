time = int(input("Enter your hours :"))
if time<=1:
    print("Free")
elif time<=3:
    print("3$")
elif time>3:
    print("5$")
else:
    print("invalid")