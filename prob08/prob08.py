"""
prob08

ok, so the source leads us to

un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

BZ + the bee image == bzip? We'll try that, first

URL: http://www.pythonchallenge.com/pc/def/integrity.html
Soln: http://www.pythonchallenge.com/pc/def/integrity.html (user: huge, pass: file)
"""

import bz2

def main():
    """
    let's bunzip the username and password, above
    """
    user_bz = \
        b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    user_pw = \
        b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    user_string = bz2.decompress(user_bz)
    pw_string = bz2.decompress(user_pw)

    print("USER: {}".format(user_string))
    print("PASS: {}".format(pw_string))

    # this gives us "huge" and "file" -- something tells me that there's more to it
    # nope. wow.

    print("done")

if __name__ == '__main__':
    main()
