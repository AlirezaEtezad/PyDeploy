from pydantic import BaseModel

class CourseBase(BaseModel):
    unit: int
    name: str

class CourseCreate(CourseBase):
    pass
    

class Course(CourseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    firstname: str
    lastname: str
    average: float
    graduated: bool


class StudentCreate(StudentBase):
    pass



class Student(StudentBase):
    id: int
  #  courses: list[Course] = []

    class Config:
        orm_mode = True