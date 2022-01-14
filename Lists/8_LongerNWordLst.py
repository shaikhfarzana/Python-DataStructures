"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to find the list of words that are longer than n from a given list of words.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def long_word_count(number, user_input):
    """
       Description:
           Function is used to find the word of given length from string.
       Parameter:
          Length and String as a parameter.
       Return:
           Returns nothing but prints the list of given word length.
    """

    word_len = []
    txt = user_input.split(" ")
    for x in txt:
        if len(x) > number:
            word_len.append(x)
    logging.debug("Words with more the given length are: " + str(word_len))


def create_list():
    """
       Description:
           Function is used to create a List.
       Parameter:
          No parameter required.
       Return:
           Returns nothing.
    """
    user_input = str(input("Enter the String: "))
    number = int(input("Enter the number you want to compare with words in string: "))
    long_word_count(number, user_input)


if __name__ == "__main__":
    create_list()
