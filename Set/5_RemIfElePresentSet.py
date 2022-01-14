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
    number_set = {0, 1, 2, 3, 4, 5}
    logging.debug("Original set elements: {}".format(number_set))
    try:
        element = int(input("Enter the number you want to remove from above Set: "))
        # remove method removes the given element, If the element is not present then it throws KeyError.
        number_set.remove(element)
        logging.debug("Set after removing the given element is : {}".format(number_set))
    except KeyError:
        logging.debug("The number you have entered is not present in the given Set")


if __name__ == "__main__":
    remove_items_from_set()