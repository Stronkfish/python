print("Stronkfish Brand Password Generator")
# Random Gen Plugin
import random
# Preset Spec
pwlen = int(input("How long do you want your Password to be? "))
psORu = input("Would you like to use your own Set of Characters? (Y/N) ")
# Char Sets
if psORu == "Y":
    c2 = input("Which Characters would you like to use? ")
if psORu == "N":
    c2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[];,./{}|:<>?"
# Gen
pw = ""
for c in range(pwlen):
    pw += random.choice(c2)
# String & Settings
print(f"String Generated \n Length: {pwlen} \n Character Set: {c2} \n Password: {pw}")
