"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def match_word(lst):
    """
       Description:
           Function is used to match the items of List.
       Parameter:
          List as a  parameter required.
       Return:
          Returns nothing but prints the total number of matched items.
    """
    match = 0

    for items in lst:
        if len(items) > 1 and items[0] == items[-1]:
            match += 1
    logging.debug("The total number of items that are matching the giving condition is " + str(match))


if __name__ == "__main__":
    match_word(['abc', 'xyzx', 'aba', '1221'])
