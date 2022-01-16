"""
@Author: Farzana Shaikh
@Date: 15-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 15-01-2022 04:00AM
@Title : ATM Program
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def main():
    """
       Description:
           Function is used to calculate the denominations of note.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the required denomination.
    """
    note_denomination = {}
    rupees = int(input("Enter the amount to withdraw in rupees:"))
    notes = (1000, 500, 100, 50, 20, 10, 5, 2, 1)
    try:
        for i in notes:
            note_denomination[i] = rupees // i
            rupees %= i
    except ZeroDivisionError:
        logging.error("Integer division or modulo by zero")

    logging.debug("{:<8} {:<15} ".format('Notes', 'Denominations'))
    total_denominations = {key: value for key, value in note_denomination.items() if value != 0}
    logging.debug("The total denominations for given amount of money:\n " + str(total_denominations))


if __name__ == "__main__":
    main()

