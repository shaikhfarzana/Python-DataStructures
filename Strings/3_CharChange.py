"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Strings in Python(To change the Occurrence of first char in string)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def user_input():
    """
     Description:
         Function is used to print the changed string.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the changed string.
     """
    logging.debug("The string after the replacement of first occurrence of the character is  " + str(change_character('restart')))


def change_character(string):
    """
     Description:
         Function is used to change character of the first occurrence in the string .
     Parameter:
       String as a parameter required.
     Return:
         Returns the changed string.
    """
    temp = list(string)
    for i in range(1, temp.__len__()):
        if temp[i] == temp[0]:
            temp[i] = '$'
    result = ''
    for i in temp:
        result = result + i
    return result


if __name__ == "__main__":
    user_input()





