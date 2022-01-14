"""
@Author: Farzana Shaikh
@Date: 12-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 04:45AM
@Title : Basic Python(To get execution time for a Python method.)
"""

import time


def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s, end_time-start_time


if __name__ == "__main__":
    num = int(input("Enter the Nth Integer to calculate sum:"))
    print("\nTime to sum of 1 to ", num, " and required time to calculate is :", sum_of_n_numbers(num))
