from .base import *
from .validation_service import validate
from rest_framework.response import Response
class emailImplement(baseClass):
    def abstractMethod(self,email):
        validate.validateEmail(email)
        print("your email is validated")
        

class contactImplement(baseClass):
    def abstractMethod(self,contactNo):
        validate.validatePhoneNo(contactNo)
        print("your phone number  is validated")

    