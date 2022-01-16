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
    logger.debug("Password should be of minimum 8 characters, atleast 1 uppercase, one digit and a special character")
    user_input = input('Enter The Valid Password : ')
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
    patt = r'(?=.*[~!@#$%^&*_])(?=.*[0-9])(?=.*[A-Z]).{8,}'
    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(patt, string)
    if matches:
        logger.debug('Password is Valid')
        logger.info(f"Executed Successfully {string}")
    else:
        try:
            raise Exception('Wrong Pattern Entered, should follow the given rule')
        except Exception as e:
            print(e)
            logger.error(e)


if __name__ == '__main__':
    main()
