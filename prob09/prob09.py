"""
prob09

ok, connect the dots, picture of a tree

URL: http://www.pythonchallenge.com/pc/return/good.html
Soln: http://www.pythonchallenge.com/pc/return/bull.html
"""

import io

import requests

from PIL import Image
from PIL import ImageDraw

import prob09_data as data


def load_image_from_url(url, user, passwd):
    """
    download a password protected image
    :param url: the url to grab
    :param user: username
    :param passwd: password
    :return: the image
    """

    response = requests.get(url,
                            auth=requests.auth.HTTPBasicAuth(user, passwd),
                            stream=True)

    image_file = io.BytesIO(response.content)
    image = Image.open(image_file)

    return image


def plot_pixels(target_image, coordinate_list):
    """
    takes an array of ints with x in the even and y in the odd and plots it onto image
    :param target_image: the image to draw on
    :param coordinate_list: an array of ints of the form [x0, y0, x1, y1, x2, y2...]
    :return: the over drawn image
    """
    pixel_list = []
    for x, y in zip(coordinate_list[0::2], coordinate_list[1::2]):
        pixel_list.append((x, y))

    draw = ImageDraw.Draw(target_image)
    draw.line(pixel_list, fill=128, width=3)

    return target_image


def main():
    """
    ok, so there's a tree and in the src, a string of numbers labeled first and second.
    we're gonna guess that those are pixel coords

    ...and we're gonna be wrong.

     let's try plotting those two (640x480 seems like a good bet -- same size as the tree image
    """

    # image_url = 'http://www.pythonchallenge.com/pc/return/good.jpg'
    # image = load_image_from_url(image_url, 'huge', 'file')

    my_image = Image.new('RGB', (640, 480))
    my_image = plot_pixels(my_image, data.first)
    my_image = plot_pixels(my_image, data.second)

    my_image.save('out.bmp')

    # and the picture is a bull


if __name__ == '__main__':
    main()
