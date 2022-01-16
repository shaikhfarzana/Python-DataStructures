"""
@Author: Farzana Shaikh
@Date: 14-01-2022 06:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 06:00AM
@Title : Dictionary in Python( Python script to sort (ascending and descending) a dictionary by value.)
"""
import operator
import logging
logging.basicConfig(level=logging.DEBUG)


def sort_dictionary():
    """
        Description:
            Function is used to sort the dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the sorted dictionary.
     """

    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    logging.debug('Original dictionary : {}'.format(d))
    sorted_d = sorted(d.items(), key=operator.itemgetter(0))
    logging.debug('Dictionary in ascending order by value : {}'.format(sorted_d))
    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    logging.debug('Dictionary in descending order by value : {}'.format(sorted_d))


def sort_dictionary_by_value():
    """
        Description:
            Function is used to sort the dictionary.
        Parameter:
           No parameter required.
        Return:
            Returns nothing but prints the sorted dictionary.
     """

    # Initialize a dictionary
    my_dict = {'c': 3,
               'a': 1,
               'd': 4,
               'b': 2}

    # Sorting dictionary
    sorted_dict = sorted([(value, key) for (key, value) in my_dict.items()])
    # Print sorted dictionary
    logging.debug("Sorted dictionary is :{}".format(sorted_dict))


# def display():
#     print("Original dictionary elements:")
#     colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
#     print(colors)
#     print("\nSort (ascending) the said dictionary elements by value:")
#     print(sort_dict_by_value(colors))
#     print("\nSort (descending) the said dictionary elements by value:")
#     print(sort_dict_by_value(colors, True))
#
#
# def sort_dict_by_value(d, reverse=False):
#     return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


if __name__ == "__main__":
    sort_dictionary()
    sort_dictionary_by_value()
