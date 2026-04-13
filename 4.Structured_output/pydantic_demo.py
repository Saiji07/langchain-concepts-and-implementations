from pydantic import BaseModel,EmailStr
from typing import Optional
class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr


new_student={'name':'nitish','age':21,'email':'abs@icloud.com'}
student=Student(**new_student)
print(student)