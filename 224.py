def status(name,price) :
    if price >= 500000 :
        print(f"{name} : Expensive")
    else :
        print(f"{name} : Cheap")

print("===== Product Status =====")

status("Phone",600000)
status("Laptop",800000)
status("Watch",300000)
status("Mouse",200000)
status("Camera",500000)