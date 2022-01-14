"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : Array in Python(Program to get the number of occurrences of a specified element in an array.)
"""


# importing "array" for array creations
from array import *


def create_array():
    """
       Description:
           Function is used to create an array.
       Parameter:
          No parameters required.
       Return:
           Returns nothing.
    """
    my_array = array('i', [1, 3, 5, 13, 11, 13, 15, 13, 19, 21, 13, 25])
    print("The new created array is : ", end=" ")
    display_array(my_array)
    count_occurrence_of_specific_value(my_array)


def display_array(my_array):
    """
       Description:
           Function is used to display an array.
       Parameter:
          Array as a parameter required.
       Return:
           Returns nothing but prints the array.
    """
    for element in range(0, len(my_array)-1):
        print(my_array[element], end=" ")
    print()


def count_occurrence_of_specific_value(my_array):
    """
       Description:
           Function is used to count the occurrence of specified element in an array.
       Parameter:
          Array required as a parameter.
       Return:
           Returns nothing but prints the total number of occurrence of that specified element.
    """
    try:
        array_occurrence = my_array
        print("Original array: " + str(my_array))
        user_input = int(input("Enter the number to count its occurrence:"))
        print("Number of occurrences of given value is ", array_occurrence.count(user_input))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_array()
