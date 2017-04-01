"""
problem 06

started and noticed zipper and 'zip' in the comments.
Replaced .html with .zip and downloaded channel.zip

URL: http://www.pythonchallenge.com/pc/def/channel.html
Soln: http://www.pythonchallenge.com/pc/def/oxygen.html
"""

import re
import zipfile

def parse_for_nothing(text_str):
    """
    parses a string to find the number to follow
    :param text: the body of the webpage
    :return: a number
    """

    pattern = r'nothing is (\d+)'
    match = re.search(pattern, text_str)

    retval = ''

    if match:
        retval = match.group(1)

    return retval



def get_infolist(filename):
    """
    initial attempt to get the solution. nothing interesting.

    :param filename:
    :return: a ZipInfo for the zipfile
    """
    infolist = ''
    with zipfile.ZipFile(filename, 'r') as myzip:
        infolist = myzip.infolist()

    return infolist


def get_file_contents(filename):
    """
    returns the contents of filename
    :param filename: the file to parse
    :return: the contents of 'filenname'
    """
    retval = ''

    with open(filename, "r") as nothing_file:
        for line in nothing_file:
            retval += line

    return retval

def collect_comments(zip_data):
    """
    ok, so originally, this created a concated string of comments - which was garbage
    now it creates a hash, indexed by file, so that we can print
    the next_nothing linked list of comment chars

    :param zip_data: a zipInfo structure
    :return: a hash where the key is the file number and the value is the
             'comment' field from the zip info
    """

    comment_dict = {}

    for file_entry in zip_data:
        file_number = file_entry.filename[:-4]  # strip the .txt from the filename
        comment_dict[file_number] = file_entry.comment

    return comment_dict


def main():
    """
    run through the files to get the answer to the riddle
    """
    nothing_filename = "./output/90052.txt"
    file_contents = get_file_contents(nothing_filename)
    next_nothing_string = parse_for_nothing(file_contents)

    while next_nothing_string:
        print(file_contents)
        nothing_filename = "./output/{}.txt".format(next_nothing_string)
        file_contents = get_file_contents(nothing_filename)
        next_nothing_string = parse_for_nothing(file_contents)

    # ok so this craps out on 46145 with the value 'collect the comments'
    # I'm guessing that's the comment on each file in the .zip
    zip_filename = "./channel.zip"
    data = get_infolist(zip_filename)

    comments = collect_comments(data)

    nothing_filename = "./output/90052.txt"
    file_contents = get_file_contents(nothing_filename)
    next_nothing_string = parse_for_nothing(file_contents)
    result_str = ''
    while next_nothing_string:
        result_str += comments[next_nothing_string].decode('ascii')
        nothing_filename = "./output/{}.txt".format(next_nothing_string)
        file_contents = get_file_contents(nothing_filename)
        next_nothing_string = parse_for_nothing(file_contents)


    print(result_str)

    #aaaaand the banner prints 'hockey'
    # which prints
    # it's in the air. look at the letters.

    # which gives us 'oxygen'
if __name__ == '__main__':
    main()
