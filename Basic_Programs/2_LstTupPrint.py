"""
@Author: Farzana Shaikh
@Date: 11-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 04:00PM
@Title : Basic Python(To print list and tuple from user input)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def list_tuple_display():
    """
     Description:
         Function is used to take input from user and display it as list and tuple.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the user input as list and tuple.
    """
    values = input("Enter some comma separated values : ")
    list = values.split(",")
    converted_tuple = tuple(list)
    logging.debug("List :" + str(list))
    logging.debug("Tuple :" + str(converted_tuple))


if __name__ == "__main__":
    list_tuple_display()


