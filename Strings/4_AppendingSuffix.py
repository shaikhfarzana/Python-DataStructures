"""
@Author: Farzana Shaikh
@Date: 11-01-2022 11:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:00AM
@Title : Strings in Python(To append suffix in string)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def user_input():
    """
       Description:
           Function is used to take string as input from the user.
       Parameter:
          No parameter required.
       Return:
           Returns nothing.
    """
    string = input("Enter the String:")
    logging.debug("The string after appending the suffix is " + suffix_append(string))


def suffix_append(string):
    """
       Description:
           Function is used to append suffix to the string.
       Parameter:
          String as a parameter required.
       Return:
           Returns the suffix appended string.
    """
    if string.__len__() >= 3:
        if string[-3:] == 'ing':
            return string + 'ly'
        else:
            return string + 'ing'


if __name__ == "__main__":
    user_input()

