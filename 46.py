while True :
    command = input("Enter command").lower()
    if command == "start" :
        print("Game Started")
    elif command == "stop" :
        print("Game Stop")
        break
    elif command == "skip" :
        continue
    elif command == "status" :
        print("Game is running")
    else :
        print("Unknown Command")