"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to create an intersection of Set.)
"""

import logging

logging.basicConfig(level=logging.DEBUG)


def to_find_intersection_of_sets():
    """
       Description:
           Function is used to find Intersection of Sets.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    set_a = set(["Green", "Blue"])
    set_b = set(["Blue", "Yellow", "Green"])
    set_c = set(["Red", "Yellow", "Blue"])
    logging.debug("Original set elements: {}".format(set_a, set_b))
    # using intersection operator (&)
    result = set_a & set_b
    logging.debug("The Intersection of two Sets A and B are: {}".format(result))
    result = set_a.intersection(set_b, set_c)
    logging.debug("The Intersection of three Sets A,B and C are: {}".format(result))


if __name__ == "__main__":
    to_find_intersection_of_sets()
