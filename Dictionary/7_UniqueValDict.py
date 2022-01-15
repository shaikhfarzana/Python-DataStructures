"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to print all unique values in a dictionary.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def unique_value_in_dictionary():
    """
        Description:
            Function is used to get unique values from the dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    List = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    logging.debug("Original List: {}".format(List))
    unique_value = set(val for dict in List for val in dict.values())
    logging.debug("The Unique values in dictionary are {} ".format(unique_value))


if __name__ == "__main__":
    unique_value_in_dictionary()