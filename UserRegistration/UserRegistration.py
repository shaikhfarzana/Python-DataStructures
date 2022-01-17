"""
@Author: Farzana Shaikh
@Date: 15-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 15-01-2022 04:00PM
@Title : Python Program for user registration.
"""
from Logger import logger
import re


def main():
    """
       Description:
           Function is used to take input from user.
       Parameter:
          No parameter required.
       Return:
           Returns nothing.
    """
    user_input = input('Enter Valid First Name : ')
    logger.debug("{}".format(first_name_regex(user_input)))


def first_name_regex(user_string):
    """
       Description:
           Function is used to check whether the firstname of the user is valid or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    patt = r'^[A-Z][a-z]{3,30}'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(patt, user_string)
    if matches:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
