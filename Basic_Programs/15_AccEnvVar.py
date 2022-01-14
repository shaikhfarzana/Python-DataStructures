"""
@Author: Farzana Shaikh
@Date: 12-01-2022 02:32AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 12-01-2022 02:45AM
@Title : Basic Python(To access environment variables.)
"""


import os
for item, value in os.environ.items():
   print('{}: {}'.format(item, value))
