ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# array to store all possible english words which will be used to compare the output of brute force method
ENGLISH_WORDS = []


def crackCipher(cipherText):
    matchedText = ''
    possibleKey = 0
    for key in range(len(ALPHABET)):
        plainText = ''

        for char in cipherText:
           index = ALPHABET.find(char)

           # decryption formula
           decrypt = (index - key) % len(ALPHABET)

           plainText = plainText + ALPHABET[decrypt] 
        
        # print('for key: %s, the result is: %s' %(key, plainText))
        text = count_words(plainText)
        if text :
            matchedText = text
            possibleKey = key
    print('possible match: ', matchedText, ' for key: ', possibleKey)

def read_english_words():
    # read all english words from file
    dictionary = open('english_words.txt', 'r')

    # read file content and split them based on newline character
    for word in dictionary.read().split('\n'):
        
        ENGLISH_WORDS.append(word)

    dictionary.close()
    # print(len(ENGLISH_WORDS))

def count_words(text):
    # function to split the output of brute force method
    text = text.upper()
    # split words based on space in the result 
    words = text.split(' ')
    wordMatch = 0
    for word in words:
        # below comparision is time complexity algorithm. Replace it with TRIE or TERNARY search algorithm
        if word in ENGLISH_WORDS:
            wordMatch += 1
    # print(wordMatch, len(words))

    # below implementation expects every word to be present. This won't be true in case of names, places and some 
    # advanced english words, verbs etc 
    # if wordMatch == len(words):
    #     print("possible match found", text)
    #     return(text)

    # to include variety of english words then use below relative formula
    # if X% of matches present then declare that as english setence. X need to be optimized
    if (float(wordMatch) / len(words)) * 100 >= 60:
        # print("possible match found", text)
        return(text)

if __name__ == '__main__' :
    # encrypted = 'VJKUBKUBOGUUCIG' # Equals to this is message
    encrypted = 'O BPCOGBKUBDCNCAUBJQNEAGTBHTQOBDWFCRGUVABJWPICT ABKBCOBYQTMKPIBCUBCBUQHVYCTGBGPIKPGGTBUQHVYCTGBGPIKPGGTBUQHVYCTGBGPIKPGGTBCVBVJGBOQOGPV'
    read_english_words()
    print("Encrypted word: ", encrypted)
    crackCipher(encrypted)
    