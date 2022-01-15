"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to add a key to a dictionary.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def update_dictionary():
    """
        Description:
            Function is used to update the dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
     """

    d = {0: 10, 1: 20}
    logging.debug("The existing dictionary is {}".format(d))
    d.update({2: 30})
    logging.debug("The updated dictionary is {}".format(d))


if __name__ == "__main__":
    update_dictionary()