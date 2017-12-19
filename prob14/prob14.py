#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
prob 14
walk around

picture of a cinnamon roll; weird lined box at the bottom


URL: http://www.pythonchallenge.com/pc/return/italy.html
soln: http://www.pythonchallenge.com/pc/return/uzi.html
"""

import io
import requests

from PIL import Image
from PIL import ImageDraw

def transform_image_spiral(source_image):
    """
    take a line of pixels and run it in a spiral shape (clockwise) into an image
    :param source_image: the line of pixels
    :return: a square image with the line wrapped into is (size is sqrt(len(line)))
    """

    # ok - so I could do the sqrt of the image width but I'm not making a general purpose solution here
    img_width = 100
    img_height = 100

    return_image = Image.new(
        "RGB", (img_width, img_height), color=(220, 220, 220))
    draw = ImageDraw.Draw(return_image)
    pixel_idx = 0
    start_x = 0
    end_x = 100
    start_y = 0
    end_y = 100

    while pixel_idx < 10000:
        # paint the top
        for idx in range(start_x, end_x):
            pixel = source_image.getpixel((pixel_idx, 0))
            draw.point((idx, start_y), pixel)
            pixel_idx += 1

        # now paint the left side
        start_y += 1
        end_x -= 1
        for idx in range(start_y, end_y):
            pixel = source_image.getpixel((pixel_idx, 0))
            draw.point((end_x, idx), pixel)
            pixel_idx += 1

        # now paint the bottom
        end_y -= 1
        for idx in range(end_x - 1, start_x, -1):
            pixel = source_image.getpixel((pixel_idx, 0))
            draw.point((idx, end_y), pixel)
            pixel_idx += 1

        # now paint the left side
        for idx in range(end_y, start_y - 1, -1):
            pixel = source_image.getpixel((pixel_idx, 0))
            draw.point((start_x, idx), pixel)
            pixel_idx += 1

        start_x += 1

    return return_image


def main():
    """
    uhhh... not sure on this one; time to start looking

    ok - so there's a comment: <!-- remember: 100*100 = (100+99+99+98) + (...  -->
    and the image is 100 x 100 -- well, it's 100x100 in the markup but looking at wire.png,
    looks like it's 10000x1...hmmm

    ok, we'll try taking each 100 pixels and making an image in a spiral

    ...... and it's a cat
    but wait - going to soln: http://www.pythonchallenge.com/pc/return/cat.html
    says and 'its name is uzi. you'll hear from him later.' so we go to uzi, not cat
    """
    image_url = 'http://www.pythonchallenge.com/pc/return/wire.png'
    user = 'huge'
    passwd = 'file'

    response = requests.get(image_url,
                            auth=requests.auth.HTTPBasicAuth(user, passwd),
                            stream=True)

    image_file = io.BytesIO(response.content)
    line_image = Image.open(image_file)
    new_image = transform_image_spiral(source_image=line_image)

    new_image.save('new_image.bmp')

if __name__ == '__main__':
    main()
