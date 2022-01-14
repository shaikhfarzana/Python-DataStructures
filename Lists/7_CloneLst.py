"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to  clone or copy a list.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def clone_list(lst):
    """
       Description:
           Function is used to clone the list.
       Parameter:
          List as a parameter required.
       Return:
           Returns nothing but prints the cloned lists.
    """
    new_list = lst[:]
    logging.debug("The cloned list is " + str(new_list))


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
    logging.debug("The Original list is", lst)
    clone_list(lst)


if __name__ == "__main__":
    create_list()
