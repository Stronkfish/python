L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26))) # Letters to Integers / Inverse (1-2)
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
cry = int(input("Stronkfish Brand Caeser Cipher Tool\n\nEncrypt or Decrypt? (1/2) ")) # Cipher Spec (3-5)
pltxt = input("Enter the Message you would like to Encrypt/Decrypt: ")
key = int(input("What would you like the Key to be? "))
citxt = "" # Cipher (6-13)
if cry == 2:
    key = -key
for c in pltxt.upper():
    if c.isalpha():
        citxt += I2L[ (L2I[c] + key)%26 ]
    else:
        citxt += c
print(f"Original Message: {pltxt} \nCiphered Message: {citxt} \nKey: {key}") # Cipher & Settings (14)
