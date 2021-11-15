import matplotlib.pyplot as plt

# we are not including BLANK_SPACE in initial set because SPACE is most frequent letter so we are dropping it
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    # convert given text to uppercase to elimanate case sensitiveness
    text = text.upper()

    # define empty dict 
    # e.g {A:2, B:5, C:10}
    letter_frequency = {}

    # initialize dict with 0 frequency 
    for letter in LETTERS:
        letter_frequency[letter] = 0
    
    # find presence given text and update the frequency
    for letter in text:
        if letter in LETTERS:
            letter_frequency[letter] += 1
    
    return letter_frequency

def plot_distribution(frequency):
    # input to BAR chart X-axis: letters and Y-axis: frequency value
    plt.bar(frequency.keys(), frequency.values())
    plt.show()

def caesar_crack(text):
    frequency = frequency_analysis(text)
    # plot_distribution(frequency)

    # sort the given dict into descending order based on frequency value using lambda
    # x[1] denotes the dict value in key-value pair
    # lambda return in array of tuple
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    # print(frequency)

    # find possible key used for encryption using below formula
    #  key = index of most frequent letter - value of 'E'
    # abs() to get absolute values rather than negative value
    KEY = abs(LETTERS.find(frequency[0][0]) - LETTERS.find('E'))
    print("possible encryption key is: ", KEY)
    
    # call decryption function with just found key to decrypt the cipher text
    plainText = caesarDecryption(text, KEY)

    return plainText

def caesarDecryption(cipherText, KEY):
    plainText = ''
    cipherText = cipherText.upper()

    for char in cipherText:
        index = LETTERS.find(char)

        # decryption formula
        decrypt = (index - KEY) % len(LETTERS)

        plainText = plainText + LETTERS[decrypt]
    
    return plainText   

if __name__ == '__main__':

    cipher_text = 'RCTVJKDCP'
    print('Before Decryption: ', cipher_text)
    plain_text = caesar_crack(cipher_text)

    print('After Decryption: ', plain_text)