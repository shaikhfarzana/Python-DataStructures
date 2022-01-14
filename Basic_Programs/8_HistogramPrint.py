"""
@Author: Farzana Shaikh
@Date: 12-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 02:45AM
@Title : Basic Python(To create a histogram from a given list of integers./Print Pattern)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def histogram(items):
    """
       Description:
           Function is used to create histogram from integer.
       Parameter:
          List as parameter.
       Return:
           Returns nothing but prints the pattern.
    """
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times = times - 1
        print(output)


if __name__ == "__main__":
    histogram([1, 2, 3, 4, 3, 2, 1])
