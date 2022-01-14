"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Strings in Python(To calculate character frequency)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def user_input():
    """
      Description:
          Function is used to take string as a input from user.
      Parameter:
         No parameter required.
      Return:
          Returns nothing but prints the character count of the string.
       """
    string = input("Enter the String:")
    logging.debug("The Frequency of each character is " + str(count_character(string)))


def count_character(string):
    """
      Description:
          Function is used to count the frequency of characters in the string.
      Parameter:
         String as a parameter required.
      Return:
          Returns the calculated frequency of the characters.
       """
    string_to_list = list(string)
    temp = sorted(set(string_to_list))  # can be done without sorted method also
    temp = list(temp)
    result = {}
    for i in temp:
        result[i] = string_to_list.count(i)
    return result


if __name__ == "__main__":
    user_input()
