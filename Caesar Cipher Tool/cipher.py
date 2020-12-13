# Originally written by Stronkfish
# Rewritten by ADifferentPerson

print("Stronkfish Brand Caesar Ciper Tool")
print()

a_char = ord("A") # ASCII char code of the character "A" (this should be 65)

def char_to_int(c: str) -> int:
    """Gets the ASCII char code of an uppercase character, then returns its difference from the A char."""
    return ord(c) - a_char

def int_to_char(i: int) -> str:
    """Adds a number 0-25 to the char code of A, then returns the uppercase character corresponding to it."""
    return chr(i + a_char)

# Take the first character of the input and make it uppercase
e_or_d = input("Encrypt or Decrypt? (E/D) ")[:1].upper()

# Verify that it's "E" or "D"
decrypt = e_or_d == "D"
if e_or_d != "E" and not decrypt:
    print("Please specify either encrypt (E) or decrypt (D)")
    exit()

# Get the message from input
message = input(f"Enter the message you would like to {'decrypt' if decrypt else 'encrypt'}: ")

# Get the key from input, then ensure that the key is an integer
original_key = input("What would you like the key to be? ")
try:
    original_key = int(original_key)
except ValueError:
    print("Please enter an integer")
    exit()

# Make the key negative when decrypting, so the cipher is flipped
key = -original_key if decrypt else original_key

def shift(char: str) -> str:
    """Shifts an uppercase character by the key"""
    return int_to_char((char_to_int(char) + key) % 26)

# For each character in the uppercase version of the message:
# If the character is A-Z, apply the shift to the character
# Otherwise, keep the character the same
ciphered_message = "".join(shift(char) if char.isalpha() else char for char in message.upper())

# Show results
print("""
Stronkfish Brand Caesar Ciper Results:
Original message: {}
{}ed message: {}
Key: {}
""".format(message, "Decrypt" if decrypt else "Encrypt", ciphered_message, original_key))
