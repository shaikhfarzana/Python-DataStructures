"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to unpack a tuple in several variables.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_unpack_tuple_in_several_variable():
    """
       Description:
           Function is used to unpack tuple in several variables.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuple.
    """

    # create a tuple
    tuplex = 4, 8, 3
    logging.debug("The given tuple is {}".format(tuplex))
    n1, n2, n3 = tuplex
    # unpack a tuple in variables
    logging.debug("Unpacking the tuple and adding its variables: {}".format((n1 + n2 + n3)))
    # the number of variables must be equal to the number of items of the tuple
    try:
        n1, n2, n3, n4= tuplex
    except Exception:
        print("Number of variables should be as same as number of elements in tuple.")


if __name__ == "__main__":
    to_unpack_tuple_in_several_variable()