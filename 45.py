while True :
    type = input("Enter type").lower()
    if type == "quit" :
        print("Goodbye")
        break
    elif type == "skip" :
        continue
    elif type == "Hello" :
        print("Hello User")
    else :
        print("Unknown Command")


