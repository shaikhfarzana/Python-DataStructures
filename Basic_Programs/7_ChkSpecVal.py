"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Basic Python(To check whether a specified value is contained in a group of values.)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def is_data_present(group_data, num):
    """
       Description:
           Function is used to check whether the specific value is present in the list or not.
       Parameter:
          List and N element as parameter.
       Return:
           Returns the Boolean values.
    """
    for value in group_data:
        if num == value:
            return True
    return False


def given_list():
    """
       Description:
           Function is used to call the test method .
       Parameter:
          List and N element as parameter.
       Return:
           Returns nothing and prints the statements.
    """
    logging.debug("The given test data is present in the list " + str(is_data_present([1, 5, 8, 3], 3)))
    logging.debug("The given test data is not present in the list " +  str(is_data_present([5, 8, 3], -1)))


if __name__ == "__main__":
    given_list()

