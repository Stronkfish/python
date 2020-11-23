# Create or Login
main = input("create = Create Account \nlogin = Login an Existing Account \n")
# Create, then Login
if main == "create":
    u1 = input("Username: ")
    e1 = input("Email Address: ")
    pw1 = input("Password: ")
    print("Account successfully created!")
    main2 = input("login = Login to Your New Account \nclose = Close this Window \n")
    if main2 == "login":
        u2 = input("Username/Email Address: ")
        pw2 = input("Password: ")
    if main2 == "close":
        print("Window Closed.")
    else:
        print("User Input was not recognised.")
# Login without Creating
if main == "login":
    u2 = input("Username/Email Address: ")
    pw2 = input("Password: ")
    u1 = "sysadmin"
    e1 = "sysadmin@gmail.com"
    pw1 = "boomer"
else:
    print("User Input was not recognised.")
    u1 = "a"
    e1 = "b"
    pw1 = "c"
    u2 = "d"
    pw2 = "e"
# Login Details Checking
if u2 == u1 or e1:
    if pw2 == pw1:
        print(f"Logged in Successfully as {u1}!")
    else:
        print("Username, Email Address or Password were not recognised.")

elif u2 == "sysadmin" or "sysadmin@gmail.com":
    if pw2 == "boomer":
        print(f"Logged in Successfully as {u2}!")
    else:
        print("Username, Email Address or Password were not recognised.")
