"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to iterate over dictionaries using for loops.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def iterating_over_dictionary():
    """
        Description:
            Function is used to concatenate the dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    dict = {'Red': 1, 'Green': 2, 'Blue': 3}
    for color_key, value in dict.items():
         logging.debug("The iteration over the dictionary is {}".format(color_key, 'corresponds to ', dict[color_key]))


if __name__ == "__main__":
    iterating_over_dictionary()