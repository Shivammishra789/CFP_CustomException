
import re
from user_registration_exception import UserRegistrationException


class UserRegistration:
    '''
    contains all getter and setter methods for user validation
    throws custom exception when regex pattern does not match
    '''

    def get_first_name(self):
        return self.first_name

    def set_first_name(self,first_name):
        if first_name == "":
            raise UserRegistrationException("First name can't be empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", first_name):
            self.first_name = first_name
        else:
            raise UserRegistrationException('Invalid first name')

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        if last_name == "":
            raise UserRegistrationException("Last name can't be empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", last_name):
            self.last_name = last_name
        else:
            raise UserRegistrationException('Invalid last name')

    def get_phone_no(self):
        return self.phone_no

    def set_phone_no(self, phone_no):
        if phone_no == "":
            raise UserRegistrationException("Phone no cannot be empty")
        if re.fullmatch("^([91]{2}[ ])?[0-9]{10}$", phone_no):
            self.phone_no = phone_no
        else:
            raise UserRegistrationException('Invalid phone number')

    def get_email(self):
        return self.email

    def set_email(self,email):
        if email == "":
            raise UserRegistrationException("Email id cannot be empty")
        if re.fullmatch("^[\\w!#$%&'*+/=?`{|}~^-]+(?:\\.[\\w!#$%&'*+/=?`{|}~^-]+)*@(?:([0-9-]{1}|[a-zA-Z]{3,5})\\.)+[a-zA-Z]{2,3}", email):
            self.email = email
        else:
            raise UserRegistrationException('Invalid email id')


user = UserRegistration()
first_name = input("Enter first name: ")
try:
    user.set_first_name(first_name)
    user.set_first_name = first_name
except UserRegistrationException as exception:
    print(exception.__str__())
last_name = input("Enter last name: ")
try:
    user.set_first_name(last_name)
except UserRegistrationException as exception:
    print(exception.__str__())

phone_no = input('Enter phone number')
try:
    user.set_phone_no()
except UserRegistrationException as exception:
    print(exception.__str__())

email = input("Enter email id: ")
try:
    user.set_email(email)
except UserRegistrationException as exception:
    print(exception.__str__())
finally:
    print('finally block is executed')