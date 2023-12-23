from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int]

class Users(BaseModelModify):
    login: str
    password: str
    power_level: Optional[int]

class subject(BaseModelModify):
    Start_Time: Optional[str]
    end_Time: Optional[str]
    date: Optional[str]

class Teachers(BaseModelModify):
    FirstName: Optional[str]
    email: Optional[str]
    Phone: Optional[int]
    LastName: Optional[str]

class Students(BaseModelModify):
    FirsName: Optional[str]
    Gender: Optional[str]
    email: Optional[int]
    LastName: Optional[str]

class Courses(BaseModelModify):
    CourseName: Optional[str]
    Description: Optional[str]

class Enrollment(BaseModelModify):
    StudentID: Optional[int]
    CourselID: Optional[int]
    Date: Optional[int]

class Grades(BaseModelModify):
    EnrollmentID: Optional[int]
    Grade: Optional[str]

