#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
prob 12
dealing evil

another blurry picture - maybe another even odd problem?


URL: http://www.pythonchallenge.com/pc/return/evil.html
soln: http://www.pythonchallenge.com/pc/return/disproportional.html

"""
import io
import requests

def main():
    """
    read in the file and create 5 files (since the cards have 5s)
    """
    image_url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
    user = 'huge'
    passwd = 'file'

    response = requests.get(image_url,
                            auth=requests.auth.HTTPBasicAuth(user, passwd),
                            stream=True)

    # read chunked - probably not necessary but since I had the wrong URL, I thought
    # that I was getting a truncation error. Good practice.

    full_content = b''
    for chunk in response.iter_content(chunk_size=256):
        full_content += chunk

    image_file = io.BytesIO(full_content)
    source_bytes = image_file.read()

    for idx in range(5):
        open(f'image_{idx}.jpg', 'wb').write(source_bytes[idx::5])


if __name__ == '__main__':
    main()
