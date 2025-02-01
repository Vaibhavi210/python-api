from .base import *
from .validation_service import validate
from rest_framework.response import Response
class emailandPhoneImplement(baseClass):
    def validationForEmail(self,email):
        validate.validateEmail(email)
        print("your email is validated")
    def validationForPhone(self,contactNo):
        validate.validatePhoneNo(contactNo)
        print("your phone number  is validated")
        

# class contactImplement(baseClass):
   

    