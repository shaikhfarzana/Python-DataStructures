"""
@Author: Farzana Shaikh
@Date: 11-01-2022 10:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 10:30AM
@Title : Strings in Python(To print unique words in sorted form)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def my_list():
    """
       Description:
           Function is used to print the list with unique values.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the unique values from the list.
    """
    my_list = ['red', 'white', 'black', 'red', 'green', 'black']
    logging.debug("The sorted list with unique values is " + str(sort_list(my_list)))
    my_list = ['Amsterdam', 'New York', 'Los Angelos', 'Cape Town', 'Singapore']
    logging.debug("The sorted list with unique values is " + str(sort_list(my_list)))


def sort_list(string):
    """
       Description:
           Function is used to find unique values from the list.
       Parameter:
          String as a parameter required.
       Return:
           Returns the list with unique values.
    """
    string1 = list(string)
    temp = sorted(set(string1))  #set method for distinguish value and sorted method for sorting the values
    return temp


if __name__ == "__main__":
    my_list()
