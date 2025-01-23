import re
from rest_framework.exceptions import ValidationError


class validate:

    def validatePhoneNo(contactNo):
        # contact=str(contactNo)
        symbols=r'^\+?[1-9]\d{1,14}$'
        if not re.match(symbols,contactNo):
            raise ValidationError({"contactNo":"invalid phone number"}) 
    def validateEmail(email):
        symbols=r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(symbols,email):
            raise ValidationError({"contactNo":"invalid email"})

