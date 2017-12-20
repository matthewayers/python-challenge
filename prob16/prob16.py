#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
prob16
let me get this straight

URL: http://www.pythonchallenge.com/pc/return/mozart.html
soln: http://www.pythonchallenge.com/pc/return/romance.html
"""


import io
import requests

from PIL import Image
from PIL import ImageDraw


def print_pixel_row(source_img, row_num):
    """
    prints the pixels in a given image row (using it for debugging)

    :param source_img: the image to print from
    :param row_num: the row (zero-based) to print
    :return: nothing
    """

    for idx in range(0, source_img.width):
        pixel = source_img.getpixel((idx, row_num))
        print(pixel)

    print(f"WIDTH - {source_img.width}")

def make_aligned_img(source_gif):
    """
    takes and image, creates one which is twice the size, and aligns the pink bits that we found
    passing a gif and
    :param source_img:
    :param source_gif:
    :return:
    """

    source_img = source_gif.convert('RGB')    # change the gif into a pixel image
    new_img_width = source_img.width * 2
    new_img_center = source_img.width

    return_image = Image.new(
        "RGB", (new_img_width, source_img.height), color=(220, 220, 220))
    draw = ImageDraw.Draw(return_image)

    for row in range(0, source_img.height):
        # get the row and find the marker
        target_col = 0
        for col in range(0, source_img.width):
            if (source_gif.getpixel((col, row)) >= 249 and
                    source_gif.getpixel((col+6, row)) >= 249):

                target_col = col
                break

        # write at an offset
        start_col = new_img_center - target_col
        for col in range(0, source_img.width):
            pixel = source_img.getpixel((col, row))
            draw.point((start_col + col, row), pixel)

    return return_image

def main():
    """
    ok - looking at this, there are a bunch of pink dashes - I bet we have to align them

    vgrepping in the .gif there's a string of 249-195-195-195-195-195-252...
    we'll align that into a larger image

    :return:
    """
    image_url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
    user = 'huge'
    passwd = 'file'

    response = requests.get(image_url,
                            auth=requests.auth.HTTPBasicAuth(user, passwd),
                            stream=True)

    image_file = io.BytesIO(response.content)
    source_gif = Image.open(image_file)\

    new_image = make_aligned_img(source_gif=source_gif)

    new_image.save('new_image.bmp')


if __name__ == '__main__':
    main()
