"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to  use of FrozenSet.)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def frozen_set():
    """
       Description:
           Function is used to perform various operation on FrozenSet.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    x = frozenset([1, 2, 3, 4, 5])
    y = frozenset([3, 4, 5, 6, 7])
    # use isdisjoint(). Return True if the set has no elements in common with others.
    logging.debug("The result after applying  isdisjoint method is {} ".format(x.isdisjoint(y)))

    # use difference(). Return a new set with elements in the set that are not in the others.
    logging.debug("The result after applying difference method is {} ".format(x.difference(y)))

    # new set with elements from both x and y
    logging.debug("The result after applying union operator is {} ".format(x | y))


if __name__ == "__main__":
    frozen_set()