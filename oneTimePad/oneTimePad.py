# below module for producing rando number between range
# for actual implementation use secreats module ranther randint
from random import randint
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility
import matplotlib.pyplot as plt

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryption(text, key):
    text = text.upper()
    cipher_text = ''

    # for each character in the text enumerate will return character + index of it
    for index, char in enumerate(text):
        # random key value for which each letter is shifted to its right
        key_index = key[index]

        char_index = ALPHABET.find(char)
        # formula encryption = (char value + random value) modulus of 26 
        cipher_text = cipher_text + ALPHABET[(char_index + key_index) % len(ALPHABET)]

    return cipher_text

def decryption(cipher_text, key):
    plain_text = ''

    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        # formula decryption = (char value - random value) modulus of 26
        plain_text = plain_text + ALPHABET[(char_index - key_index) % len(ALPHABET)]
    
    return plain_text


def random_sequence(text):
    # takes plain text as an input and produces randon sequence
    # length of random sequence is always equals to length of input text
    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET)-1))

    return random

def frequency_analysis(text):
    # convert given text to uppercase to elimanate case sensitiveness
    text = text.upper()

    # define empty dict 
    # e.g {A:2, B:5, C:10}
    letter_frequency = {}

    # initialize dict with 0 frequency 
    for letter in ALPHABET:
        letter_frequency[letter] = 0
    
    # find presence given text and update the frequency
    for letter in text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1
    
    return letter_frequency

# function to display frequency distribution in graphical way by using matplotlib
def plot_distribution(frequency):
    # input to BAR chart X-axis: letters and Y-axis: frequency value
    plt.bar(frequency.keys(), frequency.values())
    plt.show()

if __name__ == '__main__':

    plain_text = "Shannon defined the quantity of information produced by a source for example the quantity in a message by a formula similar to the equation that defines thermodynamic entropy in physics. In its most basic terms Shannons informational entropy is the number of binary digits required to encode a message. Today that sounds like a simple even obvious way to define how much information is in a message. In 1948, at the very dawn of the information age, this digitizing of information of any sort was a revolutionary step. His paper may have been the first to use the word bit, short for binary digit. As well as defining information, Shannon analyzed the ability to send information through a communications channel. He found that a channel had a certain maximum transmission rate that could not be exceeded. Today we call that the bandwidth of the channel. Shannon demonstrated mathematically that even in a noisy channel with a low bandwidth, essentially perfect, error-free communication could be achieved by keeping the transmission rate within the channel's bandwidth and by using error-correcting schemes: the transmission of additional bits that would enable the data to be extracted from the noise-ridden signal. Today everything from modems to music CDs rely on error-correction to function. A major accomplishment of quantum-information scientists has been the development of techniques to correct errors introduced in quantum information and to determine just how much can be done with a noisy quantum communications channel or with entangled quantum bits (qubits) whose entanglement has been partially degraded by noise"
    
    seq = random_sequence(plain_text)
    print("Input message: ", plain_text.upper())
    print("Random sequence number: ", seq)
    cipher_text = encryption(plain_text, seq)
    print("Encrypted message: ", cipher_text)
    text = decryption(cipher_text, seq)
    print("Decrypted message: ", text)
    plot_distribution(frequency_analysis(cipher_text))
