"""
problem 05 - peak hell

which sounds like pickle- which means that I'm loading some data
there's a banner.p link - I'm guess that holds the data

URL: http://www.pythonchallenge.com/pc/def/peak.html
Soln: http://www.pythonchallenge.com/pc/def/channel.html
"""

import pickle
import urllib

def load_data():
    """
    load the raw pickle data bytes from a URL
    :return: a set of bytes to be unpickled
    """
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'

    retval = ''

    with urllib.request.urlopen(url) as response:
        retval = response.read()

    return retval

def print_banner_line(line_array):
    """
    take a line which is a set of tuples - each contains a character and a count
    print the character 'count' times
    :param line_array: the array of tuples to print
    :return: nothing
    """
    line = ''
    for char_tuple in line_array:
        line += char_tuple[0] * char_tuple[1]

    print(line)

def main():
    """
    grab the data and unpickle
    """

    data = load_data()
    result = pickle.loads(data)

    # result is an array of tuples with # and '' and counts - print it

    for line in result:
        print_banner_line(line)

    # and it prints 'channel'

    print("done")

if __name__ == '__main__':
    main()
