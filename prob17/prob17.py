#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
prob17
eat?

A picture of a cookie with a picture in the bottom left
of a couple of wooden figures working

URL: http://www.pythonchallenge.com/pc/return/romance.html
soln:
"""

import re
import bz2

from urllib.parse import unquote_to_bytes, quote_plus
from xmlrpc.client import ServerProxy

import requests

def follow_busynothing(link_number):
    """
    follows the busynothing links (similar to prob04 but with busynothing= instead of nothing=
    :param link_number: the busynothing link to follow
    :return:
    """
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(link_number)
    response = requests.get(url)
    html = response.text
    print(f"COOKIES {link_number}")
    info = response.cookies['info']
    return info, html

def parse_for_nothing_new(text_str):
    """
    parses a string to find the number to follow
    :param text: the body of the webpage
    :return: a number
    """

    pattern = r'next busynothing is (\d+)'
    match = re.search(pattern, text_str)

    return match.group(1)

def main():
    """
    I think this one has something to do with cookies - first step, get
    the page and look at the cookies
    """

    nothing_link_number = '12345'
    iteration = 0
    info_string = ''
    while nothing_link_number:
        iteration += 1
        info_byte, result = follow_busynothing(nothing_link_number)
        info_string += info_byte
        if nothing_link_number != '16044':
            try:
                nothing_link_number = parse_for_nothing_new(result)
            except AttributeError:
                print("DONE: {}".format(result))
                nothing_link_number = ''  # terminate the loop
        else:
            nothing_link_number = '8022'      # 16044/2 as per the instructions on 16044
        print("#{} - {} [{}]".format(iteration, result, nothing_link_number))
    print(f"INFO STRING: {info_string}")
    res = unquote_to_bytes(info_string.replace('+', ' '))
    print(res)
    print(bz2.decompress(res).decode())

    # ok, so now we know that we have to call Mozart's father (Leopold) -
    #  using the xmlrpc phonebook, probably
    call = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(call.phone("Leopold"))

    # results in 555-VIOLIN
    # http://www.pythonchallenge.com/pc/phonebook.php results in
    # no! i mean yes! but ../stuff/violin.php.
    # http://www.pythonchallenge.com/pc/stuff/violin.php

    # ok - so I had to get help here - you have to tell him that
    # "the flowers are on their way" by setting the info field in the header

    url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    msg = "the flowers are on their way"
    response = requests.get(url, headers={"Cookie": "info=" + quote_plus(msg)})

    print(response.text)

    # this prints a webpage with the following relevant line:
    #  "oh well, don't you dare to forget the balloons."
    #  ...and the answer is balloons

if __name__ == '__main__':
    main()
