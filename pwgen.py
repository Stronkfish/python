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
    c3s = int(input("Please choose from a selection of character sets. \n1 = All characters \n2 = Alphanumeric Characters \n3 = Numbers & Symbols \nChar Set: "))
    if c3s == 1:
        c2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[];,./{}|:<>?"
    if c3s == 2:
        c2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if c3s == 3:
        c2 = "1234567890/*-!@#$%^&*()_+[];',./{}|:<>?"
# Gen
pw = ""
for c in range(pwlen):
    pw += random.choice(c2)
# String & Settings
print(f"String Generated \nLength: {pwlen} \nCharacter Set: {c2} \nPassword: {pw}")
# pwlen = Password Length
    # psORu = Preselected Character set or User Character set
        # c = Characters
            # c2 = Character set
                # c3s Preselected Character Sets
                    # pw = Password
