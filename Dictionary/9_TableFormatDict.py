"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python program to  print a dictionary in table format.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def iteration_of_dictionary_for_formatting():
    """
        Description:
            Function is used to print dictionary in table format.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
    """
    # Define the dictionary
    dict = {}

    # Insert data into dictionary
    dict1 = {1: ["Samuel", 21, 'Data Structures'],
             2: ["Richie", 20, 'Machine Learning'],
             3: ["Lauren", 21, 'OOPS with java'],
             }

    # Print the names of the columns.
    logging.debug("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

    # print each data item.
    for key, value in dict1.items():
        name, age, course = value
        logging.debug("{:<10} {:<10} {:<10}".format(name, age, course))


def zip_format_for_dictionary():
    """
        Description:
            Function is used to print dictionary in table format.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the dictionary.
    """
    # define the dictionary
    dict1 = {}

    # insert data into dictionary.
    dict1 = {'NAME': ['Samuel', 'Richie', 'Lauren'],
             'AGE': [21, 20, 21],
             'COURSE': ['Data Structures', 'Machine Learning', 'OOPS with Java']}

    # print the contents using zip format.
    for each_row in zip(*([i] + (j)
                          for i, j in dict1.items())):
        logging.debug(*each_row, " ")


if __name__ == "__main__":
    iteration_of_dictionary_for_formatting()
    zip_format_for_dictionary()