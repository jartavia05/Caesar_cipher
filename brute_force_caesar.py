from caesar_cipher import caesar_cipher, caesar_decipher

ciphertext = 'JXYJ JX FQUMF GWFAT HTSYFHYFSIT F RNPJ IJQ MTYJQ YFSLT'
key = 5
# Podemos intentar esto usando la fuerza bruta, es decir, podemos probar todas las claves posibles y ver cuál tiene más sentido.
for i in range(26):
    print(f'(key = {i}) {caesar_decipher(ciphertext,i)}')