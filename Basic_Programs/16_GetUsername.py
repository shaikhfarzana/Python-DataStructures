"""
@Author: Farzana Shaikh
@Date: 12-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 04:45AM
@Title : Basic Python(To get the current username.)
"""


# importing required module
import os

# using getlogin() returning username
print(os.getlogin())
# using path.expanduser() getting username
print(os.path.expanduser('~'))