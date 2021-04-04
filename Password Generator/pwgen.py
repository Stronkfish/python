# Random Plugin.
import random

# Password Length.
passlength = int(input("Stronkfish Brand Password Generator\n\nPassword Length: "))

# Custom Character Set.
selection = input("Would you like to use your own Set of Characters? (Y/N) ")

# Choose which Characters you want in your Password.
if selection.upper() == "Y":
    characters = input("Characters: ")

# All Characters.
if selection.upper() == "N":
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[];,./{}|:<>?"

# Pre-Defined Variable.
password = ""

# At the specified Length of the Password, Generate a Random String with the Character Set chosen.
for c in range(passlength):
    password += random.choice(characters)

# Generated String, Characters Used, and the Length.
print(f"String Generated \nLength: {passlength} \nCharacters Used: {characters} \nPassword: {password}")
