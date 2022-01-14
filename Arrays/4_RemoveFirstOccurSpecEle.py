"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : Array in Python(Program to remove the first occurrence of the specified element in an array.)
"""


# importing "array" for array creations
from array import *
import array as arr


def create_array():
    """
       Description:
           Function is used to create an array.
       Parameter:
          No parameters required.
       Return:
           Returns nothing.
    """
    my_array = arr.array('i', [1, 3, 5, 13, 11, 13, 15, 13, 19, 21, 13, 25])
    print("The new created array is : ", end=" ")
    display_array(my_array)
    remove_occurrence_of_specific_value(my_array)


def display_array(my_array):
    """
       Description:
           Function is used to display an array.
       Parameter:
          Array as a parameter required.
       Return:
           Returns nothing but prints the array.
    """
    for value in range(0,len(my_array)-1):
        print(my_array[value], end=" ")
    print()


def remove_occurrence_of_specific_value(my_array):
    """
       Description:
           Function is used to remove the element at its first occurrence in an array.
       Parameter:
          Array required as a parameter.
       Return:
           Returns nothing.
    """
    try:
        print("Original array: " + str(my_array))
        user_input = int(input("Enter the element which you want to remove:"))
        my_array.remove(user_input)
        print("The array after removing is : ", end="")
        print(my_array)
    except ValueError:
        print("Given element is not present in the array.")


if __name__ == "__main__":
    create_array()
