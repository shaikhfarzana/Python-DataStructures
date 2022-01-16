"""
@Author: Farzana Shaikh
@Date: 15-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 15-01-2022 04:00PM
@Title : Taking user input for dictionary.
"""

import json
import logging
logging.basicConfig(level=logging.DEBUG)


def user_dictionary():
    """
       Description:
           Function is used to take user input for creating dictionary.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Dictionary.
    """
    dict1 = {}
    element = int(input("Enter the total element:"))
    for i in range(element):
        key = input("Enter key: ")
        value = input("Enter value:")
        dict1[key] = [value]
    logging.debug("The dictionary with user input is\n {}".format(dict1))
    dictionary_with_json_object(dict1)
    dictionary_with_json(dict1)


def dictionary_with_json_object(dict1):
    """
       Description:
           Function is used to print dictionary with json object.
       Parameter:
           Dictionary as a parameter required.
       Return:
           Returns nothing but prints the Dictionary.
    """
    json_object = json.dumps(dict1, indent=4)
    logging.debug("The dictionary with Json Object is {} ".format(json_object))


def dictionary_with_json(dict1):
    """
       Description:
           Function is used to print dictionary in json file.
       Parameter:
          Dictionary as a parameter required.
       Return:
           Returns nothing.
    """
    with open("dict1.json", "a") as outfile:
        json.dump(dict1, outfile)


def nested_dictionary():
    """
       Description:
           Function is used to take user input for nested dictionary .
       Parameter:
          No parameter required.
       Return:
           Returns nothing.
    """
    nested_dict = {}
    size = int(input("Enter the size of nested dictionary: "))
    for i in range(size):
        dict_name = input("Enter the name of child dictionary: ")
        nested_dict[dict_name] = {}
        name = input("Enter name: ")
        age = input("Enter Age: ")
        nested_dict[dict_name]["Name"] = name
        nested_dict[dict_name]["Age"] = age
    logging.debug("The nested dictionary with user input is\n {}".format(nested_dict))
    dictionary_with_json_object(nested_dict)
    dictionary_with_json(nested_dict)


if __name__ == "__main__":
    user_dictionary()
    # nested_dictionary()
