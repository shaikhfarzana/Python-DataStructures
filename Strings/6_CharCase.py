"""
@Author: Farzana Shaikh
@Date: 11-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 04:00AM
@Title : Strings in Python(To print input in Uppercase and Lowercase)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def case_of_character():
    """
       Description:
           Function is used to change the Character case of the string.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but print the uppercase and lowercase of the given string.
    """
    string = input("Enter the String:")
    logging.debug("The Uppercase of the given string is " + string.upper())
    logging.debug("The Lowercase of the given string is " + string.lower())


if __name__ == "__main__":
    case_of_character()

