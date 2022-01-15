"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to convert a list into a nested dictionary of keys.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def list_to_nested_dictionary():
    """
        Description:
            Function is used to get nested dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    number_list = [1, 2, 3, 4]
    new_dict = current = {}
    for num in number_list:
        current[num] = {}
        current = current[num]
    logging.debug("The nested dictionary is" + str(new_dict))


def nested_dictionary():
    """
        Description:
            Function is used to get nested dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    # Convert Lists to Nestings Dictionary
    # Using list comprehension + zip()

    # initializing list
    test_list1 = ["gfg", 'is', 'best']
    test_list2 = ['ratings', 'price', 'score']
    test_list3 = [5, 6, 7]

    # printing original list
    logging.debug("The original list 1 is : " + str(test_list1))
    logging.debug("The original list 2 is : " + str(test_list2))
    logging.debug("The original list 3 is : " + str(test_list3))

    # Convert Lists to Nestings Dictionary
    # Using list comprehension + zip()
    res = [{a: {b: c}} for (a, b, c) in zip(test_list1, test_list2, test_list3)]

    # printing result
    logging.debug("The constructed dictionary : " + str(res))


if __name__ == "__main__":
    list_to_nested_dictionary()
    nested_dictionary()