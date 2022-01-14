"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to print a specified list after removing the 0th, 4th and 5th elements.)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def remove_specific_elements():
    """
       Description:
           Function is used to remove elements from specific position.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the lists after removing specified elements.
    """

    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
    logging.debug("The list after removing elements from specified position is " + str(color))


if __name__ == "__main__":
    remove_specific_elements()