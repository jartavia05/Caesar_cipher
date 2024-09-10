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

plain_text = 'ESTE ES ALPHA BRAVO CONTACTANDO A MIKE DEL HOTEL TANGO'
criptogram = 'JXYJ JX FQUMF GWFAT HTSYFHYFSIT F RNPJ IJQ MTYJQ YFSLT'
key = 5

print(caesar_cipher(plain_text,key))
print(caesar_decipher(criptogram,key))

