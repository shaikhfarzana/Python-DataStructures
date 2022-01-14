"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to create a Tuple with different data types.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_create_tuple_with_different_datatype():
    """
       Description:
           Function is used to create a Tuple with different datatype.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuple.
    """

    # Create a tuple with different data types
    tuplex = ("tuple", False, 3.2, 1)
    logging.debug("The tuple with different datatype is {} ".format(tuplex))


if __name__ == "__main__":
    to_create_tuple_with_different_datatype()