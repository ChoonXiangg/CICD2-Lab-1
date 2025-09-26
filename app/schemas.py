from pydantic import BaseModel, EmailStr, constr, conint
from typing import Optional

class User(BaseModel):
    user_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)
    student_id: constr(pattern=r'^S\d{7}$')

#I want to allow users to only write the name and value they want to update instead of every name and value so I created a new class
#For example, user_id: Optional[int] = None means if user_id is not in the request body, it will be None
class UserUpdate(BaseModel):
    user_id: Optional[int] = None
    name: Optional[constr(min_length=2, max_length=50)] = None
    email: Optional[EmailStr] = None
    age: Optional[conint(gt=18)] = None
    student_id: Optional[constr(pattern=r'^S\d{7}$')] = None