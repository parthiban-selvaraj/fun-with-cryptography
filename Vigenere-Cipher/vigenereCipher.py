ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encryption(plain_text, KEYS):
    # uses a multiple letters for encryption like caesar cipher
    plain_text = plain_text.upper()
    cipher_text = ''

    # contains multiple letters which will be used for encryption
    KEYS = KEYS.upper()

    # denotes the first index (ie letter) of KEY
    KEY_INDEX = 0

    for character in plain_text:
        # add index of plain text letter + index key space letter and modulus by 26
        index = (ALPHABET.find(character) + ALPHABET.find(KEYS[KEY_INDEX])) % len(ALPHABET) 

        cipher_text = cipher_text + ALPHABET[index]
        
        # increment key index for traversing to next letter in key
        KEY_INDEX += 1

        if KEY_INDEX == len(KEYS):
            KEY_INDEX = 0

    return cipher_text

def vigenere_decryption(cipher_text, KEYS):
    cipher_text = cipher_text.upper()
    plain_text = ''

    KEYS = KEYS.upper()

    KEY_INDEX = 0

    for character in cipher_text:
        # add index of plain text letter - index key space letter and modulus by 26
        index = (ALPHABET.find(character) - ALPHABET.find(KEYS[KEY_INDEX])) % len(ALPHABET) 

        plain_text = plain_text + ALPHABET[index]

        KEY_INDEX += 1

        if KEY_INDEX == len(KEYS):
            KEY_INDEX = 0
    
    return plain_text

if __name__ == '__main__' :

    message = input('Enter the message to encrypt/decrypt: ').strip()
    option = int(input('Enter your option 1.Encyption 2.Decryption: '))
    secret = input('Enter secret key: ').strip()

    if (len(message) > 0 and (option > 0 or option < 2)):
        if(option == 1) :
            output = vigenere_encryption(message, secret)
        else :
            output = vigenere_decryption(message, secret) 
        print(output)
    else:
        print('invalid input or options')





