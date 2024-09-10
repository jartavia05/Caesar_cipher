from caesar_cipher import caesar_cipher, caesar_decipher

criptogram = 'JXYJ JX FQUMF GWFAT HTSYFHYFSIT F RNPJ IJQ MTYJQ YFSLT'
key = 5
# Brute force in case you don't have the key. In caesar the key could only between 1 and 25
for i in range(1,26):
    print(caesar_decipher(criptogram,i))