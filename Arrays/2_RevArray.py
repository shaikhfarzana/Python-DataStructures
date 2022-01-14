"""
@Author: Farzana Shaikh
@Date: 13-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 13-01-2022 04:00PM
@Title : Array in Python(Program to reverse the order of the items in the array.)
"""


# importing "array" for array creations
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
    my_array = arr.array('i', [1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23, 25])
    print("The new created array is : ", end=" ")
    display_array(my_array)
    reverse_array(my_array)


def display_array(a):
    """
       Description:
           Function is used to display an array.
       Parameter:
          Array as a parameter required.
       Return:
           Returns nothing but prints the array.
    """
    for i in range(0, 12):
        print(a[i], end=" ")
    print()


def reverse_array(my_array):
    """
       Description:
           Function is used to reverse an array.
       Parameter:
          Array as a parameter required.
       Return:
           Returns nothing but prints the reversed array.
    """
    reversed_array = my_array[::-1]
    print("\nThe reversed array is: \n", reversed_array)


if __name__ == "__main__":
    create_array()