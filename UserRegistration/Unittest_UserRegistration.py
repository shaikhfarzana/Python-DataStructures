"""
@Author: Farzana Shaikh
@Date: 15-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 15-01-2022 04:00PM
@Title : Python Program for Unit testing user registration.
"""

import unittest
import UserRegistration as UR


class Validate(unittest.TestCase):

    def test_first_name_regex_pass(self):
        """
           Description:
               Function is used to Test the Firstname of the user for valid input.
           Parameter:
              Self object as a parameter
           Return:
               Returns nothing.
        """
        first_name = 'Abcd'
        actual = UR.first_name_regex(first_name)
        self.assertEqual(actual, True)

    def test_first_name_regex_fail(self):
        """
           Description:
               Function is used to Test the Firstname of the user for invalid input.
           Parameter:
              Self object as a parameter
           Return:
               Returns nothing.
        """
        first_name = 'ab'
        actual = UR.first_name_regex(first_name)
        self.assertEqual(actual, False)

    def test_last_name_regex_pass(self):
        """
           Description:
               Function is used to Test the Lastname of the user for valid input.
           Parameter:
              Self object as a parameter
           Return:
               Returns nothing.
        """
        last_name = 'Abcd'
        actual = UR.last_name_regex(last_name)
        self.assertEqual(actual, True)

    def test_last_name_regex_fail(self):
        """
           Description:
               Function is used to Test the Lastname of the user for invalid input.
           Parameter:
              Self object as a parameter
           Return:
               Returns nothing.
        """
        last_name = 'abc'
        actual = UR.last_name_regex(last_name)
        self.assertEqual(actual, False)

    def test_email_id_regex_pass(self):
        """
           Description:
               Function is used to Test the EmailId of the user for valid input.
           Parameter:
              Self object as a parameter
           Return:
               Returns nothing.
        """
        emailid = 'Abc12@gmail.com'
        actual = UR.email_id_regex(emailid)
        self.assertEqual(actual, True)

    def test_email_id_regex_fail(self):
        """
             Description:
                 Function is used to Test the EmailId of the user for invalid input.
             Parameter:
                Self object as a parameter
             Return:
                 Returns nothing.
        """
        emailid = 'abcgmail'
        actual = UR.email_id_regex(emailid)
        self.assertEqual(actual, False)

    def test_mobile_number_regex_pass(self):
        """
             Description:
                 Function is used to Test the Mobile number of the user for valid input.
             Parameter:
                Self object as a parameter
             Return:
                 Returns nothing.
        """
        mobile_number = '91 9004563484'
        actual = UR.mobile_number_regex(mobile_number)
        self.assertEqual(actual, True)

    def test_mobile_number_regex_fail(self):
        """
             Description:
                 Function is used to Test the Mobile number of the user for invalid input.
             Parameter:
                Self object as a parameter
             Return:
                 Returns nothing.
        """
        mobile_number = '9004563484'
        actual = UR.mobile_number_regex(mobile_number)
        self.assertEqual(actual, False)

    def test_password_rule1_regex_pass(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character for valid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'abcdefghk'
        actual = UR.password_rule1_regex(password)
        self.assertEqual(actual, True)

    def test_password_rule1_regex_fail(self):
        """
            Description:
                Function is used to Test the Password which should be of minimum 8 character for invalid input.
            Parameter:
               Self object as a parameter
            Return:
                Returns nothing.
       """
        password = 'abcd'
        actual = UR.password_rule1_regex(password)
        self.assertEqual(actual, False)

    def test_password_rule2_regex_pass(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character and 1 uppercase alphabet for valid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'Abcdefghik'
        actual = UR.password_rule2_regex(password)
        self.assertEqual(actual, True)

    def test_password_rule2_regex_fail(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character and 1 uppercase alphabet for invalid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'abcdefghik'
        actual = UR.password_rule2_regex(password)
        self.assertEqual(actual, False)

    def test_password_rule3_regex_pass(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character, 1 uppercase alphabet and a digit for valid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'Abcdefghik123'
        actual = UR.password_rule3_regex(password)
        self.assertEqual(actual, True)

    def test_password_rule3_regex_fail(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character, 1 uppercase alphabet and a digit for invalid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'abcdefghik'
        actual = UR.password_rule3_regex(password)
        self.assertEqual(actual, False)

    def test_password_rule4_regex_pass(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character, 1 uppercase alphabet,a digit and a special character for valid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'Abcdefghikj122#%'
        actual = UR.password_rule4_regex(password)
        self.assertEqual(actual, True)

    def test_password_rule4_regex_fail(self):
        """
          Description:
             Function is used to Test the Password which should be of minimum 8 character, 1 uppercase alphabet,a digit and a special character for invalid input.
          Parameter:
            Self object as a parameter
          Return:
             Returns nothing.
        """
        password = 'abcdefghijk123A'
        actual = UR.password_rule4_regex(password)
        self.assertEqual(actual, False)


if __name__ == '__main__':
    unittest.main()