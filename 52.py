while True :
    first = int(input("Enter first number"))
    operator = input("Enter operator")
    second = int(input("Enter second number"))
    if operator == "q": 
        print("Exit")
        break   
    elif operator == "+":
        result = first + second
        print(result)
    elif operator == "-" :
        result = first - second
        print(result)
    elif operator == "*" :
        result = first * second
        print(result)
    elif operator == "/" :
        result = first / second
        print(result)
    else :
        print("Invalid")
    
