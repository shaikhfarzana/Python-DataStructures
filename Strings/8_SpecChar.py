"""
@Author: Farzana Shaikh
@Date: 11-01-2022 10:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 10:45AM
@Title : Strings in Python(To print specified character)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def specific_character():
    """
       Description:
           Function is used to print the specified character.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the specified character.
    """
    str1 = 'https://www.w3resource.com/python-exercises/string'
    logging.debug("The string after specified character as / is " + str1.rsplit('/', 1)[0])
    logging.debug("The string after specified character as - is " + str1.rsplit('-', 1)[0])


if __name__ == "__main__":
    specific_character()

