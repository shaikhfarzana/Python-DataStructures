"""
@Author: Farzana Shaikh
@Date: 12-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 02:45AM
@Title : Basic Python(To print out a set containing all the colors from list1 which are not present in list2.)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def compare_list():
    """
       Description:
           Function is used to compare the lists.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the difference between the lists.
    """
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", "Green"}
    logging.debug("Original set elements:")
    logging.debug(color_list_1)
    logging.debug(color_list_2)
    logging.debug("\nDifference of color_list_1 from color_list_2: " + str((color_list_1 - color_list_2)))
    logging.debug("\nDifference of color_list_2 from color_list_1: " + str((color_list_2.difference(color_list_1))))


if __name__ == "__main__":
    compare_list()
