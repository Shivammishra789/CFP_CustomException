'''
@author: Shivam Mishra
@date: 20-12-21 8:59 PM
@desc: test cases done with help of unit test
'''

from user_registration_exception import UserRegistrationException
from user_registration import UserRegistration
import unittest


class TestUserDetails(unittest.TestCase):
    '''
    Contains all test cases for validation
    '''

    def test_given_first_name_is_valid(self):
        excepted = 'Shivam'
        user = UserRegistration()
        user.set_first_name(excepted)
        self.assertEqual(excepted,user.get_first_name())

    def test_given_first_name_is_invalid(self):
        result = 'shivam'
        user = UserRegistration()
        try:
            user.set_first_name(result)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid first name", exception.__str__())

    def test_given_first_name_is_empty(self):
        result = ''
        user = UserRegistration()
        try:
            user.set_first_name(result)
        except UserRegistrationException as exception:
            self.assertEqual("First name can't be empty", exception.__str__())

    def test_given_last_name_is_valid(self):
        result = 'Mishra'
        user = UserRegistration()
        user.set_last_name(result)
        self.assertEqual(result, user.get_last_name())

    def test_given_last_name_is_invalid(self):
        result = 'mis'
        user = UserRegistration()
        try:
            user.set_last_name(result)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid last name", exception.__str__())

    def test_given_last_name_is_empty(self):
        result = ''
        user = UserRegistration()
        try:
            user.set_last_name(result)
        except UserRegistrationException as exception:
            self.assertEqual("Last name can't be empty", exception.__str__())

    def test_given_phone_no_is_valid(self):
        result = "91 8904662775"
        user = UserRegistration()
        user.set_phone_no(result)
        self.assertEqual(result, user.get_phone_no())

    def test_given_phone_no_is_invalid(self):
        result = "510845144"
        user = UserRegistration()
        try:
            user.set_phone_no(result)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid phone number", exception.__str__())

    def test_given_phone_no_if_empty(self):
        result = ""
        user = UserRegistration()
        try:
            user.set_phone_no(result)
        except UserRegistrationException as exception:
            self.assertEqual("Phone no cannot be empty", exception.__str__())

    def test_given_email_is_valid(self):
        result = "shiv@gmail.com"
        user = UserRegistration()
        user.set_email(result)
        self.assertEqual(result, user.get_email())

    def test_given_email_is_invalid(self):
        result = "sa!@gmail"
        user = UserRegistration()
        try:
            user.set_email(result)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid email id", exception.__str__())

    def test_given_email_is_empty(self):
        result = ""
        user = UserRegistration()
        try:
            user.set_email(result)
        except UserRegistrationException as exception:
            self.assertEqual("Email id cannot be empty", exception.__str__())







