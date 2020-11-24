print("Stronkfish Brand Caeser Cipher Tool")
# Letters to Integers / Inverse 
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# Cipher Spec
cry = int(input("Encrypt or Decrypt? (1/2) "))
pltxt = input("Enter the Message you would like to Encrypt/Decrypt: ")
key = int(input("What would you like the Key to be? "))
# Cipher
citxt = ""
if cry == 2:
    key = -key
for c in pltxt.upper():
    if c.isalpha():
        citxt += I2L[ (L2I[c] + key)%26 ]
    else:
        citxt += c
# Cipher & Settings
print(f"Original Message: {pltxt} \nCiphered Message: {citxt} \nKey: {key}")
