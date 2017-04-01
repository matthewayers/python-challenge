"""
prob01:

URL: http://www.pythonchallenge.com/pc/def/map.html
Soln: http://www.pythonchallenge.com/pc/def/ocr.html
"""

def rotate_byte(char_to_rotate):
    """
    :param char_to_rotate: the byte that you want to rotate
    :return: the mapped byte if it's a-z, char to rotate, otherwise
    """
    rotate_val = 2
    alphabet = b'abcdefghijklmnopqrstuvwxyz'
    new_alpha = alphabet[rotate_val:] + alphabet[:rotate_val]

    retval = char_to_rotate
    posn = alphabet.find(char_to_rotate)

    if posn >= 0:
        retval = new_alpha[posn]

    return retval

def main():
    """
    rotate the cipher text by two positions in the alphabet
    A->C
    B->D
    etc
    """

    cipher_text = b"""
    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
    bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
    """

    plain_text = list(map(rotate_byte, cipher_text))
    plain_string = ''.join(list(map(chr, plain_text)))
    print(plain_string)

    # the hint leads us to replace the URL (map.html) - but they just man the map part
    cipher_text = b'map'
    plain_text = list(map(rotate_byte, cipher_text))
    plain_string = ''.join(list(map(chr, plain_text)))
    print(plain_string)


if __name__ == '__main__':
    main()
