"""
@Author: Farzana Shaikh
@Date: 11-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 04:00PM
@Title : Basic Python(To print the documents (syntax, description etc.) of Python built-in function(s).)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def user_input():
    """
     Description:
         Function is used to take input from user as choice.
     Parameter:
        No parameter required.
     Return:
         Returns nothing.
    """

    choice = int(input("Enter the option whose docstring you want to see:\n 1.Addition\n 2.Difference\n 3.Power\n"))
    to_print_docstring(choice)


def to_print_docstring(choice):
    """
     Description:
         Function is used to display the docstring as per the choice of user .
     Parameter:
        Choice as integer is required as a parameter.
     Return:
         Returns choice integer to switcher and prints the corresponding docstring .
    """
    switcher = {
            1: logging.debug(addition.__doc__),
            2: logging.debug(differentiation.__doc__),
            3: logging.debug(raise_to_power.__doc__),
        }

    return switcher.get(choice, "nothing")


def addition(a, b):
    """Returns addition of arg1 and arg2."""
    return a + b


def differentiation(a, b):
    """Returns difference of arg1 and arg2."""
    return a - b


def raise_to_power(a, b):
    """Returns arg1 raised to power arg2."""
    return a ** b


if __name__ == "__main__":
    user_input()