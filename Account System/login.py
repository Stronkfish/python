u3 = "sysadmin" # Admin Account Details (1-3)
e3 = "sysadmin@gmail.com"
pw3 = "boomer"
main = input("Stronkfish Brand Login System\n\ncreate = Create Account \nlogin = Login an Existing Account \n") # Create or Login Account (4)
if main == "create": # Create, then Login (5-15)
    u1 = input("Username: ")
    e1 = input("Email Address: ")
    pw1 = input("Password: ")
    cpw1 = input("Confirm Password: ")
    if cpw1 == pw1:
        print("\nAccount successfully created!\n")
        main2 = input("login = Login to Your New Account \nclose = Close this Window \n\n")
        if main2 == "login":
            u2 = input("Username/Email Address: ")
            pw2 = input("Password: ")
            if u1 == u2: # Login Details Checking (16-31)
                if pw1 == pw2:
                    print(f"Logged in Successfully as {u2}!")
            if e1 == u2:
                if pw1 == pw2:
                    print(f"Logged in Successfully as {u2}!")
            if u3 == u2:
                if pw3 == pw2:
                    print(f"Logged in Successfully as {u2}!")
            if e3 == u2:
                if pw3 == pw2:
                    print(f"Logged in Successfully as {u2}!")
        if main2 == "close":
            print("Window Closed.")   
    if cpw1 != pw1:
        print("Password and Confirm Password Mismatched.")
if main == "login": # Login without Creating (32-37)
    u2 = input("Username/Email Address: ")
    pw2 = input("Password: ")
    if u2 == u3 or e3:
        if pw2 == pw3:
            print(f"Logged in Successfully as {u3}!")
