from pydantic import BaseModel, EmailStr, Field
from typing import Optional


#inherit baseclass model
class Student(BaseModel):
    #has only one attribute
#   #simple ex
#     name:str

   #default value asie rkhte hai
    name: str = 'nitsihs'
    #optional
    age: Optional[int] = None

    email:EmailStr

    #rangeme aaygi
    #gt means-- greaterthan equal
    #lt means == > less than equal
    cgpa: float = Field(gt=0, lt=10, default=5, description=('A decimal vallue represneting the cgpa of the student'))

#dict create
new_student  = {'age':23,'email':'abc@gmail.com', 'cgpa':9}

#return pydantic ceovnert in json or dict ormat
student = Student(**new_student)
#dict converion

student_dict = dict(student)
print(student_dict['age'])

#json me lana answer
student_json = student.model_dump_json()
print(student_json)



print(student)


