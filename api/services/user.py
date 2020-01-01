from re import match

from django.conf import settings


class UserService():

    def email_valid(self, email):
        return match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$', email)

    def password_valid(self, password):
        return len(password) >= 8

    def send_email_confirmation(self, email_confirmation):
        return True
