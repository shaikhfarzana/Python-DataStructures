"""
@Author: Farzana Shaikh
@Date: 11-01-2022 02:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 11-01-2022 02:00PM
@Title : Basic Python(To reverse the order of firstname amd lastname of the user)
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def reverse_order_name():
    """
     Description:
         Function is used to reverse the order of firstname and lastname.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the username in reverse order.
    """
    first_name = input("Enter Your First Name:")
    last_name = input("Enter Your Last Name:")
    logging.debug("The username is {} {}".format(last_name, first_name))


if __name__ == "__main__":
    reverse_order_name()
