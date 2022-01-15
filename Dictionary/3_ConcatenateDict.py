"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to concatenate following dictionaries to create a new one.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def update_dictionary():
    """
        Description:
            Function is used to concatenate the dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    dict1 = {1: 10, 2: 20}
    dict2 = {3: 30, 4: 40}
    dict3 = {5: 50, 6: 60}
    dict4 = {}
    for d in (dict1, dict2, dict3): dict4.update(d)
    logging.debug("The concatenated dictionary is {} ".format(dict4))


if __name__ == "__main__":
    update_dictionary()