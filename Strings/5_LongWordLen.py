"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Strings in Python(To find the length of long word from the list)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def my_list():
    """
       Description:
           Function is used to print the lengthiest word from the string.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the lengthiest word from given string.
    """
    my_list = ['Amsterdam', 'New York', 'Los Angelos', 'Cape Town', 'Singapore']
    logging.debug("The lengthiest word from the given list is " + str(long_word(my_list)))


def long_word(lst):
    """
       Description:
           Function is used to find the lengthiest word from the string.
       Parameter:
           String as a parameter required.
       Return:
           Returns the lengthiest word and its length from the string.
    """
    result = []
    for i in lst:
        result.append(i.__len__())
        result_index = result.index(max(result))
    return lst[result_index], max(result)


if __name__ == "__main__":
    my_list()

