import random # Random Gen Plugin (1)
passlength = int(input("Stronkfish Brand Password Generator\n\nHow long do you want your Password to be? ")) # Preset Spec (2-3)
selection = input("Would you like to use your own Set of Characters? (Y/N) ")
if selection == "Y": # Char Sets (4-13)
    chars = input("Which Characters would you like to use? ")
if selection == "N":
    charset = int(input("Please choose from a selection of character sets. \nAll Characters = 1 \nAlphanumeric Characters = 2 \nNumbers & Symbols = 3 \nCharacter Set: "))
    if charset == 1:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[];,./{}|:<>?"
    if charset == 2:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if charset == 3:
        chars = "1234567890/*-!@#$%^&*()_+[];',./{}|:<>?"
passw = "" # Gen (14-16)
for c in range(passlength):
    passw += random.choice(chars)
print(f"String Generated \nLength: {passlength} \nCharacter Set: {chars} \nPassword: {passw}") # String & Settings (17)
