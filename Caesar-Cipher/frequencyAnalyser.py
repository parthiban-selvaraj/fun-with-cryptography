# Matplotlib is a low level graph plotting library in python that serves as a visualization utility
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

# function to display frequency distribution in graphical way by using matplotlib
def plot_distribution(frequency):
    # input to BAR chart X-axis: letters and Y-axis: frequency value
    plt.bar(frequency.keys(), frequency.values())
    plt.show()




if __name__ == '__main__':

    plain_text = 'one way to solve an encrypted message, if we know its language, is to find a different plaintext of the same language long enough to fill one sheet or so, and then we count the occurrences of each letter'
    frequency = frequency_analysis(plain_text)
    plot_distribution(frequency)





