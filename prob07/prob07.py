"""
prob07

ok, so running down the middle of this image is a set of grey bars.
time to poke around the image and see what the values are

URL: http://www.pythonchallenge.com/pc/def/oxygen.html
Soln: http://www.pythonchallenge.com/pc/def/integrity.html
"""

import io
from urllib.request import urlopen

from PIL import Image

def get_image_row(image, row_idx):
    """
    read the value of a row of bytes from an Image

    :param row_idx:
    :return: a row of pixel tuples of size image.width
    """

    row_values = []

    for col_idx in range(0, image.width):
        row_values.append(image.getpixel((col_idx, row_idx)))

    return row_values

def main():
    """
    read the grey blocks out of the iamge and convert to ASCII letters
    """

    image_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

    file_descriptor = urlopen(image_url)
    image_file = io.BytesIO(file_descriptor.read())
    image = Image.open(image_file)

    row_values = get_image_row(image, 48)    # grab the middle row

    answer = ''
    for pixel in row_values[::7]: # the blocks are 7x7, just get one value per block
        answer += (chr(pixel[0]))

    print(answer)

    # this prints:
    # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]oe]

    real_answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]

    real_answer_string = ''
    for letter in real_answer:
        real_answer_string += chr(letter)

    print(real_answer_string)


if __name__ == '__main__':
    main()
