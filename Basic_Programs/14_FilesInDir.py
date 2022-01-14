"""
@Author: Farzana Shaikh
@Date: 12-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 02:45AM
@Title : Basic Python(To list all files in a directory in Python.)
"""

# Refactor
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/user/') if isfile(join('contacts.csv', f))]
print(files_list)
