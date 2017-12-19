#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
prob 13
call him

picture of a phone - 5 is clickable and gives a bad xmldoc - SOAP? XML RPC


URL: http://www.pythonchallenge.com/pc/return/disproportional.html
soln: http://www.pythonchallenge.com/pc/return/italy.html
"""
import io
import requests
import xmlrpc.client

from pprint import pprint as pp

def main():
    """
    read in the file and create 5 files (since the cards have 5s)
    ...
    """
    server_url = "http://www.pythonchallenge.com/pc/phonebook.php"

    server = xmlrpc.client.ServerProxy(server_url)

    print(server.system.listMethods())

    print(server.phone("Bert"))

    #returns 555-ITALY

if __name__ == '__main__':
    main()
