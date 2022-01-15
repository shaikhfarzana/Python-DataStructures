"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python program to count number of items in a dictionary value that is a list)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def count_items_in_dictionary():
    """
        Description:
            Function is used to check whether multiple key is present or not.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    count = sum(map(len, dict.values()))
    logging.debug("The total values in dictionary are {}".format(count))


if __name__ == "__main__":
    count_items_in_dictionary()