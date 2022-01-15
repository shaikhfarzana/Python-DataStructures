"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python program to check multiple keys exists in a dictionary.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def check_for_multiple_key_dictionary():
    """
        Description:
            Function is used to check whether multiple key is present or not.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """
    student = {
        'name': 'Alex',
        'class': 'V',
        'roll_id': '2'
    }
    logging.debug("If multiple key exist then True else false:")
    logging.debug(student.keys() >= {'class', 'name'})
    logging.debug(student.keys() >= {'name', 'Alex'})
    logging.debug(student.keys() >= {'roll_id', 'name'})


if __name__ == "__main__":
    check_for_multiple_key_dictionary()