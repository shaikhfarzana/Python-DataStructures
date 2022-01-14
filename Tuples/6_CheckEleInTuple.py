"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to check whether an element exists within a Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def check_element_in_tuple():
    """
       Description:
           Function is used to check whether the element is present or not.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """
    tuplex = ("H", "e", "l", "l","o", 1, 2, 3)
    logging.debug("The given element is present or not:" + str("r" in tuplex))
    logging.debug("The given element is present or not:" + str(2 in tuplex))


if __name__ == "__main__":
    check_element_in_tuple()

