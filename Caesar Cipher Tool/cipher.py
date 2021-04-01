 # Letters to Integers / Inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

# Cipher Specification
enc_or_dec = int(input("Stronkfish Brand Caesar Cipher Tool\n\nEncrypt or Decrypt? (1/2) ")) 

plaintext = input("Enter the Message you would like to Encrypt/Decrypt: ")

key = int(input("What would you like the Key to be? "))

# Inverses Key for Decryption
if enc_or_dec == 2:
    key = -key

# Cipher
cipheredtext = ""
for c in plaintext.upper():
    if c.isalpha():
        cipheredtext += I2L[ (L2I[c] + key)%26 ]
    else:
        cipheredtext += c

# Result, Settings Chosen
print(f"Original Message: {plaintext} \nCiphered Message: {cipheredtext} \nKey: {key}")
