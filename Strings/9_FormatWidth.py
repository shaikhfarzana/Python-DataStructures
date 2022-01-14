"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:45AM
@Title : Strings in Python(To format the text as width=50)
"""

import textwrap
import logging
logging.basicConfig(level=logging.DEBUG)


def format_width_paragraph():
    """
       Description:
           Function is used to format the text width.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the formatted text as a paragraph.
    """
    sample_text = '''
          Python is a widely used high-level, general-purpose, interpreted,
          dynamic programming language. Its design philosophy emphasizes
          code readability, and its syntax allows programmers to express
          concepts in fewer lines of code than possible in languages such
          as C++ or Java.      Python is a widely used high-level, general-purpose, interpreted,
          dynamic programming language. Its design philosophy emphasizes
          code readability, and its syntax allows programmers to express
          concepts in fewer lines of code than possible in languages such
          as C++ or Java.
          '''
    wrapper = textwrap.TextWrapper(width=30)
    word_list = wrapper.wrap(text=sample_text)
    for element in word_list:
        logging.debug(element)


if __name__ == "__main__":
    format_width_paragraph()
