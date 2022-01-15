"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def user_input_dictionary():
    """
        Description:
            Function is used to generate specific dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    number = int(input("Input a number "))
    dict1 = dict()

    for x in range(1, number + 1):
        dict1[x] = x * x

    logging.debug("The dictionary is " + str(dict1))


if __name__ == "__main__":
    user_input_dictionary()