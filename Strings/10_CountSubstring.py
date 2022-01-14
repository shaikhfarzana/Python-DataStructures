"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Strings in Python(To count the occurrence of substring in string )
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def count_substring():
    """
      Description:
          Function is used to count the occurrence of given substring.
      Parameter:
         No parameter required.
      Return:
          Returns nothing but prints the total occurrence of given substring.
    """
    sample_text = '''
          Python is a widely used high-level, general-purpose, interpreted,
          dynamic programming language. Its design philosophy emphasizes
          code readability, and its syntax allows programmers to express
          concepts in fewer lines of code than possible in languages such
          as C++ or Java.
        '''
    user_input = input("Enter the word whose count you want to find from the paragraph:")
    logging.debug("The total count of given word in the paragraph is " + str(sample_text.count(user_input)))


if __name__ == "__main__":
    count_substring()