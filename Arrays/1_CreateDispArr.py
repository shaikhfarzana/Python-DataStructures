"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : Array in Python(Program to create an array of 5 integers and display the array items.Access individual element through indexes.)
"""

# importing "array" for array creations
import array as arr
import logging
logging.basicConfig(level=logging.DEBUG)


def create_array():
    """
       Description:
           Function is used to create an array.
       Parameter:
          No parameters required.
       Return:
           Returns nothing.
    """
    my_array = arr.array('i', [1, 3, 5, 9, 11])
    print("The new created array is : ", end=" ")
    display_array(my_array)


def display_array(my_array):
    """
       Description:
           Function is used to display an array.
       Parameter:
          Array numbers as a parameter required.
       Return:
           Returns nothing but prints the array.
    """
    try:
        for i in range(0, len(my_array)-1):
            print(my_array[i], end=" ")
        print()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_array()
