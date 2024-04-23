from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    average = Column(Float)
    graduated = Column(Boolean, default=False)

    courses = relationship("Course", back_populates="owner")



class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    unit = Column(Integer)
    owner_id = Column(Integer, ForeignKey("students.id"))

    owner = relationship("Student", back_populates="courses")


