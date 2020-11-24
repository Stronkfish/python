# Admin Account Details
u3 = "sysadmin"
pw3 = "boomer"
e3 = "sysadmin@gmail.com"
# Create or Login Account
main = input("create = Create Account \nlogin = Login an Existing Account \n")
# Create, then Login
if main == "create":
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
            # Login Details Checking
            if u1 == u2:
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
# Login without Creating
if main == "login":
    u2 = input("Username/Email Address: ")
    pw2 = input("Password: ")
    if u2 == u3 or e3:
        if pw2 == pw3:
            print(f"Logged in Successfully as {u3}!")
