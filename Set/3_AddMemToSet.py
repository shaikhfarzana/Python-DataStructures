"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to add member(s) in a  Set.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def add_member_to_set():
    """
       Description:
           Function is used to add members to a Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    # A new empty set
    color_set = set()
    logging.info(color_set)
    logging.debug("Added single element:")
    # add method adds single element at a time.
    color_set.add("Red")
    logging.debug("The Set after adding the element is {} ".format(color_set))
    logging.debug('Added multiple items:')
    # update method adds multiple element at a time.
    color_set.update(["Blue", "Green"])
    logging.debug("The Set after adding multiple element is {} ".format(color_set))


def add_member_to_set_from_user():
    """
       Description:
           Function is used to add members to a Set from user input.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    # Create a new set
    number_set = {0, 1, 2, 3, 4, 5}
    logging.debug("Original set elements: {}".format(number_set))
    element = int(input("Enter the number you want to add to given Set:"))
    number_set.add(element)
    logging.debug("Set after adding the given element is {} ".format(number_set))


if __name__ == "__main__":
    add_member_to_set()
    add_member_to_set_from_user()

