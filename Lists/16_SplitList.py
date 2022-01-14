"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : List in Python(Program to split a list based on first character of word.)
"""
from itertools import groupby
from operator import itemgetter
import logging
logging.basicConfig(level=logging.DEBUG)


def split_list_from_word():
    """
       Description:
           Function is used to split a list  based on the first character of word.
       Parameter:
          No parameter is required.
       Return:
           Returns nothing but prints the list.
    """
    word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

    for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)


if __name__ == "__main__":
    split_list_from_word()
