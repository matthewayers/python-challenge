"""
prob10

ok, so it's a picture of a cow - no wait, a bull.
the caption is:
len(a[30]) = ?

and clicking on the cow takes you to the following txt
a = [1, 11, 21, 1211, 111221,

oh, good google almighty - read this as:

one 1 (11)
two ones (21)
one 2, one 1 (1211) etc etc etc

URL: http://www.pythonchallenge.com/pc/return/bull.html
Soln: http://www.pythonchallenge.com/pc/return/5808.html
"""

def get_next_in_seq(value_string):
    """
    ok, so this will count the occurances of a digit until it changes.
    It then records the count and digit in a tuple
    
    :param value_string: the initial value
    :return: the set of ordered counts - length = # of changes + 1
    """
    result_arr = []
    cur_char = value_string[0]
    count = 1
    for next_char in value_string[1:]:
        if cur_char == next_char:
            count += 1
        else:
            result_arr.append((count, cur_char))
            count = 1
            # fun fact - if you don't reset the count,
            # you turn your laptop into a space heater (oops)
        cur_char = next_char
    
    # and take care of the last ones
    result_arr.append((count, cur_char))
    
    return result_arr

def count_array_to_string(count_array):
    """
    takes an array of tuples of the form [(1,2), (2,1)] and creates a string "1221"
    
    [(1,'1')] -> "11"
    [(2,'1')] -> "21"
    [(1, '2'), (1, '1')] -> "1211"
    
    :param count_array: the array of tuples
    :return: the string
    """

    retval = ''
    for pair in count_array:
        retval += '{}{}'.format(pair[0], pair[1])

    return retval

def main():
    """
    compute the length of the 1, 11, 21, 1211 series
    """
    next_val_string = '1'
    
    for counter in range(0, 31):
        print("{}:\t[{}]".format(counter, len(next_val_string)))
        next_val_list = get_next_in_seq(next_val_string)
        next_val_string = count_array_to_string(next_val_list)

    # and so it ends with 5808

if __name__ == '__main__':
    main()
