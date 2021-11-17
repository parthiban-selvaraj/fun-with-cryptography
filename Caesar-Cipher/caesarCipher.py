# cipher key is predefined as 3
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 2

def caesarEncryption(plainText):
    # this will read individual letters  in input and find out corresponding index and apply encryption formula
    cipherText = ''
    plainText = plainText.upper()
    
    for char in plainText:
        # returns current postion of each letter
        index = ALPHABET.find(char)

        # encryption formula
        encrypt = (index + KEY) % len(ALPHABET)

        # append encrypted text and populate cipherText
        cipherText = cipherText + ALPHABET[encrypt]

    return cipherText

def caesarDecryption(cipherText):
    plainText = ''
    cipherText = cipherText.upper()

    for char in cipherText:
        index = ALPHABET.find(char)

        # decryption formula
        decrypt = (index -KEY) % len(ALPHABET)

        plainText = plainText + ALPHABET[decrypt]
    
    return plainText

if __name__ == '__main__' :
    message = input('Enter the message to encrypt/decrypt: ').strip()
    option = int(input('Enter your option 1.Encyption 2.Decryption: '))

    if (len(message) > 0 and (option > 0 or option < 2)):
        if(option == 1) :
            output = caesarEncryption(message)
        else :
            output = caesarDecryption(message) 
        print(output)
    else:
        print('invalid input or options')

