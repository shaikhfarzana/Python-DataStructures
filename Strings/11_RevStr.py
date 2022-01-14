"""
@Author: Farzana Shaikh
@Date: 11-01-2022 10:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 10:45AM
@Title : Strings in Python(To Reverse a string)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def reverse_string():
    """
     Description:
         Function is used to reverse the given string.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the reversed string.
    """
    string = input("Enter the String:")
    logging.debug("The reversed string is " + string[::-1])


if __name__ == "__main__":
    reverse_string()