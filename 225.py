def status(name,balance) :
    if balance >= 1000000 :
        print(f"{name} : VIP")
    else :
        print(f"{name} : Normal")

print("===== Account Status =====")

status("Aung",600000)
status("Ko Ko",1200000)
status("Hla Hla",700000)
status("Su Su",1400000)
status("Mg Mg",800000)