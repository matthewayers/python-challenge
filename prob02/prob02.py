"""
Problem 02 of the python challenge

URL: http://www.pythonchallenge.com/pc/def/ocr.html
Soln:
"""

from collections import defaultdict

import sample_text as sample

def get_char_freq(text):

    freq_dict = defaultdict(int)

    for char in text:
        freq_dict[char] += 1

    return freq_dict

def main():
    """
    look for rare characters in a giant block of text from the page source
    
    
    :return: none 
    """

    fd = get_char_freq(sample.txt)

    print(fd)

if __name__ == '__main__':
    main()
