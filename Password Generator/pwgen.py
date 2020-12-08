import random # Random Gen Plugin (1)
pwlen = int(input("Stronkfish Brand Password Generator\n\nHow long do you want your Password to be? ")) # Preset Spec (2-3)
psORu = input("Would you like to use your own Set of Characters? (Y/N) ")
if psORu == "Y": # Char Sets (4-13)
    c2 = input("Which Characters would you like to use? ")
if psORu == "N":
    c3s = int(input("Please choose from a selection of character sets. \nAll Characters = 1 \nAlphanumeric Characters = 2 \nNumbers & Symbols = 3 \nCharacter Set: "))
    if c3s == 1:
        c2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[];,./{}|:<>?"
    if c3s == 2:
        c2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if c3s == 3:
        c2 = "1234567890/*-!@#$%^&*()_+[];',./{}|:<>?"
pw = "" # Gen (14-16)
for c in range(pwlen):
    pw += random.choice(c2)
print(f"String Generated \nLength: {pwlen} \nCharacter Set: {c2} \nPassword: {pw}") # String & Settings (17)
