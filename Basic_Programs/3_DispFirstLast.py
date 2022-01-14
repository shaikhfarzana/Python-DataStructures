"""
@Author: Farzana Shaikh
@Date: 11-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 04:00PM
@Title : Basic Python(To display first and last element)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def display_element():
    """
     Description:
         Function is used to take input from user and display first and last element.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the first and last element from the input taken from user.
    """
    color_list = ["Red", "Green", "White", "Black"]
    new_color_list = color_list[:1] + color_list[-1:]
    logging.debug("The first and last element of the list is" + str(new_color_list))

    values = input("Enter some comma separated values : ")
    list = values.split(",")
    new_list = list[:1] + list[-1:]
    logging.debug("The first and last element of the list is " + str(new_list))


if __name__ == "__main__":
    display_element()
