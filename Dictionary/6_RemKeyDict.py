"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python program to remove a key from a dictionary.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def remove_key_from_dictionary():
    """
        Description:
            Function is used to remove key from dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    logging.debug("The dictionary is " + str(myDict))
    if 'a' in myDict:
        del myDict['a']
    logging.debug("The dictionary after removing a key is " + str(myDict))


if __name__ == "__main__":
    remove_key_from_dictionary()