"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to create a Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def create_tuple():
    """
       Description:
           Function is used to create a Tuple.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """

    # Creating an empty Tuple
    Tuple1 = ()
    logging.debug("Initial empty Tuple: {} ".format(Tuple1))

    # Creating a Tuple with the use of string.
    Tuple1 = ('Hello', 'Universe')
    logging.debug("Tuple with the use of String: {}".format(Tuple1))

    # Creating a Tuple with the use of list.
    list1 = [1, 2, 4, 5, 6]
    logging.debug("Tuple using List: {}".format(tuple(list1)))

    # Creating a Tuple with the use of built-in function.
    Tuple1 = tuple('Hello')
    logging.debug("Tuple with the use of function: {} ".format(Tuple1))


if __name__ == "__main__":
    create_tuple()