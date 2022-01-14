"""
@Author: Farzana Shaikh
@Date: 12-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 04:45AM
@Title : Basic Python(To get an absolute file path.)
"""


def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')


if __name__ == "__main__":
    print("Absolute file path: ", absolute_file_path("hello.py"))
