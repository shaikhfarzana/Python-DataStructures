"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00PM
@Title : Set in Python(Program to create a Set.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def create_set():
    """
       Description:
           Function is used to create a Set.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    # Creating a Set
    set1 = set()
    logging.debug("Initial blank Set: {} ".format(set1))

    # Creating a Set with
    # the use of a String
    set1 = set('HelloUniverse')
    logging.debug("\nSet with the use of String: {} ".format(set1))

    # Creating a Set with
    # the use of Constructor
    # (Using object to Store String)
    String = 'HelloUniverse'
    set1 = set(String)
    logging.debug("\nSet with the use of an Object: {} ".format(set1))

    # Creating a Set with
    # the use of a List
    list = ["Hello", "World", "Hello", "Universe"]
    logging.debug("\nSet with the use of List: " + str(set(list)))


def create_list_from_user_input():
    """
       Description:
           Function is used to create a Set from user input.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Sets.
    """

    user_input = str(input("Enter the string : "))
    set2 = set(user_input)
    logging.debug("\nThe Set from List is : " + str(set2))


if __name__ == "__main__":
    create_set()
    create_list_from_user_input()
