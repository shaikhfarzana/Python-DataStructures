"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to clear a Set.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def clear_set():
    """
       Description:
           Function is used to clear the Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    set_c = {"Red", "Green", "Black", "White"}
    logging.debug("Original set elements: {}".format(set_c))
    # clear() method doesn't take any argument but removes all the element if the set
    set_c.clear()
    logging.debug("After removing all elements of the said set: {}".format(set_c))


if __name__ == "__main__":
    clear_set()

