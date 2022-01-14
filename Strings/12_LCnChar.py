"""
@Author: Farzana Shaikh
@Date: 11-01-2022 10:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 10:45AM
@Title : Strings in Python(To lowercase the n character in string)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def lowercase_n_character():
    """
     Description:
         Function is used to lowercase the n character in string.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the string with n character in lowercase.
    """
    string = input("Enter the String:")
    num = int(input("Enter the N number of chars to convert it to lowercase:"))
    logging.debug("The string with N character in lowercase is " + string[:num].lower() + string[num:])


if __name__ == "__main__":
    lowercase_n_character()
