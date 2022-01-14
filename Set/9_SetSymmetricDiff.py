"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to create Symmetric Difference of Set.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_find_symmetric_difference_of_sets():
    """
       Description:
           Function is used to find Symmetric Difference of Sets.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    set_a = set(["Green", "Blue"])
    set_b = set(["Yellow","Green"])
    set_c = set(["Red", "Purple","Blue"])
    logging.debug("Original set elements: {}".format(set_a, set_b))
    # using symmetric difference operator (^)
    result = set_a ^ set_b
    logging.debug("The Symmetric Difference  of two Sets A and B are: {}".format(result))
    result = set_a.symmetric_difference(set_c)
    logging.debug("The Symmetric Difference of two Sets A and C are: {}".format(result))


if __name__ == "__main__":
    to_find_symmetric_difference_of_sets()
