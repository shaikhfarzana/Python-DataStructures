"""
@Author: Farzana Shaikh
@Date: 15-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 15-01-2022 04:00PM
@Title : Python Program for user registration.
"""
from Logger import logger
import re


def main():
    """
       Description:
           Function is used to take input from user.
       Parameter:
          No parameter required.
       Return:
           Returns nothing.
    """
    # user_input = input('Enter Valid First Name : ')
    # logger.debug("{}".format(first_name_regex(user_input)))
    # user_input = input('Enter Valid Last Name : ')
    # logger.debug("{}".format(last_name_regex(user_input)))
    # user_input = input('Enter Valid EmailId : ')
    # logger.debug("{}".format(email_id_regex(user_input)))
    # user_input = input('Enter Valid Mobile Number : ')
    # logger.debug("{}".format(mobile_number_regex(user_input)))
    # logger.debug('Password must be of minimum 8 character:')
    # user_input = input('Enter Valid Password:')
    # logger.debug("{}".format(password_rule1_regex(user_input)))
    # logger.debug('Password must be of minimum 8 character and atleast contain 1 uppercase alphabet:')
    # user_input = input('Enter Valid Password: ')
    # logger.debug("{}".format(password_rule2_regex(user_input)))
    # logger.debug('Password must be of minimum 8 characters,atleast contain 1 uppercase alphabet and a digit :')
    # user_input = input('Enter Valid Password: ')
    # logger.debug("{}".format(password_rule3_regex(user_input)))
    # logger.debug('Password should be of minimum 8 characters, atleast 1 uppercase alphabet, one digit and a special character')
    # user_input = input('Enter The Valid Password : ')
    # logger.debug("{}".format(password_rule4_regex(user_input)))
    sample_emailid = ['abc@yahoo.com', 'abc-100@yahoo.com', 'abc.100@yahoo.com', 'abc111@abccom', 'abc-100@abc.net',
                      'abc.100@abc.com.au', 'abc@1.com', 'abc@gmail.com.com', 'abc+100@gmail.com']
    for i in sample_emailid:
        email_id_regex(i)
    logger.debug("{}".format(email_id_regex(i)))


def first_name_regex(user_string):
    """
       Description:
           Function is used to check whether the firstname of the user is valid or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    patt = r'^[A-Z][a-z]{3,30}'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(patt, user_string)
    if matches:
        return True
    else:
        return False


def last_name_regex(user_string):
    """
       Description:
           Function is used to check whether the firstname of the user is valid or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern = r'^[A-Z][a-z]{3,30}'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


def email_id_regex(user_string):
    """
       Description:
           Function is used to check whether the EmailId of user is valid or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


def mobile_number_regex(user_string):
    """
       Description:
           Function is used to check whether the Mobile number of user is valid or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern = r'([0-9]{2,})+(\s[0-9]{10})+'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


def password_rule1_regex(user_string):
    """
       Description:
           Function is used to check whether the password has minimum 8 characters or not.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern = r'(.{8,})+'

    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


def password_rule2_regex(user_string):
    """
       Description:
           Function is used to check whether the password has minimum 8 characters and atleast contain 1 uppercase alphabet.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern =  r'(?=.*[A-Z]).{8,}'
    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


def password_rule3_regex(user_string):
    """
       Description:
           Function is used to check whether the password has minimum 8 characters,atleast contain 1 uppercase alphabet and a digit
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern = r'(?=.*[0-9])(?=.*[A-Z]).{8,}'
    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


def password_rule4_regex(user_string):
    """
       Description:
           Function is used to check whether the password has minimum 8 characters, atleast 1 uppercase alphabet, one digit and a special character.
       Parameter:
          String as a parameter required.
       Return:
           Returns boolean value.
    """
    pattern = r'(?=.*[~!@#$%^&*_])(?=.*[0-9])(?=.*[A-Z]).{8,}'
    # re.fullmatch function matches from beginning to end.
    matches = re.fullmatch(pattern, user_string)
    if matches:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
