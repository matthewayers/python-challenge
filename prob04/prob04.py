"""
Solution for problem 04 of the python challenge

when you click you get: and the next nothing is 44827

src shows:
linkedlist.php?nothing=12345

ok - so it seems like you follow the list of next nothings using URL LIB

URL: http://www.pythonchallenge.com/pc/def/linkedlist.php
Soln:
"""

import re
import urllib

def follow_nothing_link(link_number):
    """
    Takes a number for the linkedlist.php?nothing list and returns the text
    
    :param link_number: the 'nothing link' 
    :return: the body of the result
    """

    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(link_number)

    with urllib.request.urlopen(url) as response:
        html = response.read()

    return html


def parse_for_nothing(text):
    """
    parses a string to find the number to follow
    :param text: the body of the webpage
    :return: a number 
    """

    pattern = r'.*(\d+)'
    match = pattern.search(pattern, text)

    return match.group(1)


def main():
    """
    follow the linked list of 'nothings' until?
    """

    nothing_link_number = 12345
    iteration = 0
    while nothing_link_number:
        iteration += 1
        result = follow_nothing_link(nothing_link_number)
        print("#{} - {}".format(iteration, result))
        nothing_link_number = parse_for_nothing(result)


if __name__ == '__main__':
    main()
