"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to remove item(s) from Set.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def remove_items_from_set():
    """
       Description:
           Function is used to remove members from a Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    # Create a new set
    num_set = {0, 1, 2, 3, 4, 5}
    logging.debug("Original set elements: {} ".format(num_set))
    element = int(input("Enter the number you want to remove from above Set:"))
    # discard method removes the given element but doesn't throw any error if the element is not present.
    num_set.discard(element)
    logging.debug("Set after removing the given element is : {}".format(num_set))


if __name__ == "__main__":
    remove_items_from_set()