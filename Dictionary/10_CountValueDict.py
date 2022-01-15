"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python program to count the values associated with key in a dictionary.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def count_in_dictionary():
    """
        Description:
            Function is used to count the values associated with key.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
    """
    student = [{'id': 1, 'success': True, 'name': 'Lary'},
               {'id': 2, 'success': False, 'name': 'Rabi'},
               {'id': 3, 'success': True, 'name': 'Alex'}]
    logging.debug("The count of is " + str(sum(d['id'] for d in student)))
    logging.debug("The count of success in student is " + str(sum(d['success'] for d in student)))


if __name__ == "__main__":
    count_in_dictionary()