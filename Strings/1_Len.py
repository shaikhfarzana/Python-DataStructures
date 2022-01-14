"""
@Author: Farzana Shaikh
@Date: 11-01-2022 11:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:00AM
@Title : Strings in Python(To calculate the length of the string)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def __str__():
    """
       Description:
           Function is used to find the length of the string.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the length of the given string.
    """
    string = input("Enter the String:")
    logging.debug("The Length of the given string is " + str(string.__len__()))


if __name__ == "__main__":
    __str__()
