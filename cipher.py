print("Stronkfish Brand Caeser Cipher Tool")
# Cipher Range
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# Cipher Spec
cry = int(input("Encrypt or Decrypt? (1/2) "))
plaintext = input("Enter the Message you would like to Encrypt/Decrypt: ")
key = int(input("What would you like the Key to be? "))
# Cipher
ciphertext = ""
plaintext2 = ""
if cry == 2:
    key = -key
for c in plaintext.upper():
    if c.isalpha():
        ciphertext += I2L[ (L2I[c] + key)%26 ]
    else:
        ciphertext += c
for c in ciphertext.upper():
    if c.isalpha():
        plaintext2 += I2L[ (L2I[c] - key)%26 ]
    else:
        plaintext2 += c
# Cipher & Settings
print(f"Original Message: {plaintext} \n Ciphered Message: {ciphertext} \n Key: {key}")
