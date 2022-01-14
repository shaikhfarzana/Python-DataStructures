"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to multiplies all the items in a list.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def multiply_of_list(lst):
    """
       Description:
           Function is used to calculate multiplications of items in a list.
       Parameter:
          List required as a parameter.
       Return:
           Returns nothing but prints the multiplied value.
    """
    total_number = 1
    for element in lst:
        total_number *= element
    logging.debug("The multiplied value of the items in list is " + str(total_number))


def create_list():
    """
       Description:
           Function is used to create a List.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the lists.
    """
    # creating an empty list
    lst = []

    # number of elements as input
    user_input = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, user_input):
        element = int(input())
        lst.append(element)  # adding the element
    logging.debug(lst)
    multiply_of_list(lst)


if __name__ == "__main__":
    create_list()