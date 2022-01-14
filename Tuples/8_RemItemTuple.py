"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to remove an item from a Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_remove_item_from_tuple():
    """
       Description:
           Function is used to remove items from tuple.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """

    # create a tuple
    tuplex = ("H", "e", "l", "l", "o", 1, 2, 3)
    logging.debug("The given Tuple is {} ".format(tuplex))
    # tuples are immutable, so you can not remove elements
    # using merge of tuples with the + operator you can remove an item and it will create a new tuple
    # using slice operator
    tuplex = tuplex[:2] + tuplex[3:]
    logging.debug("The Tuple after removing element with ( :,+) operator is {} ".format(tuplex))

    # converting the tuple to list
    new_list = list(tuplex)
    # use different ways to remove an item of the list
    new_list.remove("e")
    # converting the tuple to list
    tuplex = tuple(new_list)
    logging.debug("The Tuple after removing element with converting it to list is {} ".format(tuplex))


if __name__ == "__main__":
    to_remove_item_from_tuple()
