"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to find maximum and the minimum value in a Set.)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def maximum_value_in_Set():
    """
       Description:
           Function is used to find maximum value in Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """
    # Create a set
    set = {5, 10, 3, 15, 2, 20}
    logging.debug("Original set elements: {} ".format(set))
    logging.debug("Maximum value of the said set: {} ".format(max(set)))


def minimum_value_in_set():
    """
       Description:
           Function is used to find minimum value in Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """
    # Create a set
    set = {5, 10, 3, 15, 2, 20}
    logging.debug("Original set elements: {} ".format(set))
    logging.debug("Minimum value of the said set: {} ".format(min(set)))


if __name__ == "__main__":
    maximum_value_in_Set()
    minimum_value_in_set()