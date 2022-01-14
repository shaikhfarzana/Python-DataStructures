"""
@Author: Farzana Shaikh
@Date: 12-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 04:45AM
@Title : Basic Python(To get file creation and modification date/times.)
"""

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))
