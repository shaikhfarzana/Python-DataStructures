"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python program to create a dictionary from a string.)
"""

from collections import defaultdict, Counter
import logging
logging.basicConfig(level=logging.DEBUG)


def dictionary_from_string():
    """
        Description:
            Function is used to create dictionary from string.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
    """
    string = 'HelloUniverse'
    my_dict = {}
    for letter in string:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    logging.debug("The dictionary is " + str(my_dict))


if __name__ == "__main__":
    dictionary_from_string()