"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to iteration over Set.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def iteration_over_set():
    """
       Description:
           Function is used to iterate over a Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    # Create a set
    num_set = {0, 1, 2, 3, 4, 5}
    [logging.debug(n) for n in num_set]
    print("\n\nCreating a set using string:")
    char_set = set("HelloUniverse")
    # Iterating using for loop
    [logging.debug(val) for val in char_set]
    print()


if __name__ == "__main__":
    iteration_over_set()
