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
    user_input = input('Enter Valid Last Name : ')
    regex(user_input)


def regex(string):
    """
       Description:
           Function is used to check whether the given input is valid or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns nothing.
    """
    patt = r'^[A-Z][a-z]{3,30}'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(patt, string)
    if matches:
        logger.debug('Last name is Valid')
        logger.info(f"executed Successfully {string}")
    else:
        try:
            raise Exception('Wrong Pattern Entered atleast length should be 4 and first alphabet should be capital ')
        except Exception as e:
            print(e)
            logger.error(e)


if __name__ == '__main__':
    main()