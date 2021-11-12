ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crackCipher(cipherText):
    for key in range(len(ALPHABET)):
        plainText = ''

        for char in cipherText:
           index = ALPHABET.find(char)

           # decryption formula
           decrypt = (index - key) % len(ALPHABET)

           plainText = plainText + ALPHABET[decrypt] 
        
        print('for key: %s, the result is: %s' %(key, plainText))

if __name__ == '__main__' :
    encrypted = 'RCTVJKDCP'
    crackCipher(encrypted)