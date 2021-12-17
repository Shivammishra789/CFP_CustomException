''''
throws custom exception when regex pattern does not match
'''

import re
from user_registration_exception import UserRegistrationException


class UserRegistration:

    def get_first_name(self):
        return self.first_name

    def set_first_name(self,first_name):
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", first_name):
            self.first_name = first_name
        else:
            raise UserRegistrationException('Invalid first name')

    def get_email(self):
        return self.email

    def set_email(self,email):
        if re.fullmatch("^[\\w!#$%&'*+/=?`{|}~^-]+(?:\\.[\\w!#$%&'*+/=?`{|}~^-]+)*@(?:([0-9-]{1}|[a-zA-Z]{3,5})\\.)+[a-zA-Z]{2,3}", email):
            self.email = email
        else:
            raise UserRegistrationException('Invalid email id')


first_name = input("Enter first name: ")
user = UserRegistration()
try:
    user.set_first_name(first_name)
except UserRegistrationException as exception:
    print(exception.__str__())

email = input("Enter email id: ")
try:
    user.set_email(email)
except UserRegistrationException as exception:
    print(exception.__str__())
finally:
    print('finally block is executed')
