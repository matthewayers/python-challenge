"""
prob 11

odd-even - there's a blurry picture
I'm guessing that odd/even refers to the columns;
let's render them to two separate canvases

(may be the rows but... we'll see)

ok so after looking at all the evens, odds, condensing the bright pixels...
I was stumped. Went to the internet - it suggested dark pixels

EVIL

URL:http://www.pythonchallenge.com/pc/return/5808.html
Soln:URL:http://www.pythonchallenge.com/pc/return/evil.html
"""

import io

import requests

from PIL import Image
from PIL import ImageDraw


def get_every_other(source_image, return_even):
    """
        return an image containing every other row in the original image

    :param source_image: the source image
    :param return_even: return the even rows? odd if false
    :return: image of same size w/ every other column filled in
    """

    return_image = Image.new(
        "RGB", (source_image.width, source_image.height), color=(220, 220, 220))
    draw = ImageDraw.Draw(return_image)

    if return_even:
        start_x = 0
        start_y = 0
    else:
        start_x = 1
        start_y = 0

    for y in range(start_y, source_image.height, 2):
        for x in range(start_x, source_image.width, 2):
            pixel = source_image.getpixel((x, y))
            draw.point((x / 2, y / 2), pixel)

    return return_image


def main():
    """
    load the image and render the columns
    """

    image_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
    user = 'huge'
    passwd = 'file'

    response = requests.get(image_url,
                            auth=requests.auth.HTTPBasicAuth(user, passwd),
                            stream=True)

    image_file = io.BytesIO(response.content)
    full_image = Image.open(image_file)

    even_image = get_every_other(source_image=full_image, return_even=True)
    odd_image = get_every_other(source_image=full_image, return_even=False)

    even_image.save("even.bmp")
    odd_image.save("odd.bmp")


if __name__ == '__main__':
    main()
