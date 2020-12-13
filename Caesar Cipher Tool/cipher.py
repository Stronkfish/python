print("Stronkfish Brand Caesar Ciper Tool")
print()

a_char = ord("A") # is 65

def char_to_int(c):
    return ord(c) - a_char

def int_to_char(i):
    return chr(i % 26 + a_char)

e_or_d = input("Encrypt or Decrypt? (E/D) ")[:1].upper() # Take the first character and make it uppercase
decrypt = e_or_d == "D"
if e_or_d != "E" and not decrypt:
    print("Please specify either encrypt (E) or decrypt (D)")
    exit()

message = input(f"Enter the message you would like to {'decrypt' if decrypt else 'encrypt'}: ")

original_key = input("What would you like the key to be? ")
try:
    original_key = int(original_key)
except ValueError:
    print("Please enter an integer")
    exit()

# Flip if should decrypt
key = -original_key if decrypt else original_key

ciphered_message = "".join(int_to_char(char_to_int(c) + key % 26) if c.isalpha() else c for c in message.upper())

print("""
Stronkfish Brand Caesar Ciper Results:
Original message: {}
{}ed message: {}
Key: {}
""".format(message, "Decrypt" if decrypt else "Encrypt", ciphered_message, original_key))
