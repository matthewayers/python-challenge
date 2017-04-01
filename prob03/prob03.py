"""
problem 03
Find three caps followed by a lower followed by 3 caps

URL: http://www.pythonchallenge.com/pc/def/equality.html
Soln: http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import re

import sample_text as sample     # get the chunk of text


def main():
    """
    use a regex to find the UUUlUUU pattern
    the clue says EXACTLY so I'm surrounding the desired pattern w/lowercase
    """

    pattern = r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'

    match_list = re.findall(pattern, sample.txt)

    # print the matches
    for match in match_list:
        print(match[1:-1])

    # ugh, ok, when you print these, you get 'linkedlist' as the lowercase letters

    # visiting linkedlist.html reveals a page that just says linkedlist.php
    # and that's the answer

if __name__ == '__main__':
    main()
