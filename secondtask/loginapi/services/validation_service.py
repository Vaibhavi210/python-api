import re
from rest_framework.exceptions import ValidationError
from pydantic import BaseModel,EmailStr,Field
from functools import wraps




class validate:

    def validatePhoneNo(contactNo):
        # contact=str(contactNo)
        symbols=r'^\+?[1-9]\d{9}$'
        if not re.match(symbols,contactNo):
            raise ValidationError({"contactNo":"invalid phone number"}) 
    def validateEmail(email):
        symbols=r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(symbols,email):
            raise ValidationError({"email":"invalid email"})
        
class validInput(BaseModel):
    email:EmailStr
    contactNo:str = Field(pattern=r'^\+?[1-9]\d{9}$')

pattern=r'^\+?[1-9]\d{9}$'
def validPhone(callFunc):
    @wraps(callFunc)
    def wrapper(self,request):
        contactNo = request.data.get('contactNo')
       
        if not re.match(pattern,contactNo):
             raise ValidationError({"ContactNo":"invalid contact number"})
             
        return callFunc(self,request)
    return wrapper



