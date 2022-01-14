"""
@Author: Farzana Shaikh
@Date: 12-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 02:45AM
@Title : Basic Python(To concatenate all elements in a list into a string and return it.)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def convert_list_data_into_string(list):
    """
       Description:
           Function is used to convert list into string.
       Parameter:
          List as a parameter.
       Return:
           Returns the converted string.
    """
    result = ''
    for element in list:
        result += str(element)
    return result


if __name__ == "__main__":
    logging.debug("The converted string from list is " + str(convert_list_data_into_string([1, 5, 12, 2,"Farz"])))
