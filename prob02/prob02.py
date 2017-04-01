"""
Problem 02 of the python challenge

URL: http://www.pythonchallenge.com/pc/def/ocr.html
Soln: http://www.pythonchallenge.com/pc/def/equality.html
"""

from collections import defaultdict

import sample_text as sample

def get_char_freq(text):
    """
    given a block of text return a hash of characters with each one's frequency
    :param text: the block of text to analyze
    :return: a hash of frequencies - letters are keys and frequencies are values
    """
    freq_dict = defaultdict(int)

    for char in text:
        freq_dict[char] += 1

    return freq_dict

def main():
    """
    look for rare characters in a giant block of text from the page source

    :return: none
    """

    freq_dict = get_char_freq(sample.txt)

    for entry in freq_dict:
        if freq_dict[entry] == 1:
            print(entry)

if __name__ == '__main__':
    main()
