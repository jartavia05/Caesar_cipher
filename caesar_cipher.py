"""
Python script to encrypt and decrypt using caesar cipher
@author: jartavia05

"""

def caesar_cipher(text, shift):
  result = []
  for char in text:
    if char.isupper():
      result.append(chr((ord(char) + shift - 65) % 26 + 65))
    elif char.islower():
      result.append(chr((ord(char) + shift - 97) % 26 + 97))
    else:
      result.append(char)
  return ''.join(result)

def caesar_decipher(text, shift):
  return caesar_cipher(text, -shift)

plain_text = ''
criptogram = 'YMNX NX FQUMF GWFAT HTSYFHYNSL YFSLT MTYJQ RNPJ'
key = 5

print(caesar_cipher(plain_text,key))
print(caesar_decipher(criptogram,key))

# Brute force in case you don't have the key. In caesar the key could only between 1 and 25
for i in range(1,26):
    print(caesar_decipher(criptogram,i))
