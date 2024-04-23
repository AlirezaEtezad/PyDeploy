from sqlalchemy.orm import Session

from . import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student_by_lastname(db: Session, lastname: str):
    return db.query(models.Student).filter(models.Student.lastname == lastname).first()





def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(firstname = student.firstname, lastname = student.lastname, average = student.average, graduated = student.graduated)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_courses(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Course).offset(skip).limit(limit).all()




def create_student_course(db: Session, Course: schemas.CourseCreate, student_id: int):
    db_course = models.Course(name=Course.name, unit=Course.unit, owner_id=student_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def remove_student_id(id: int , db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)
    firstname = student.first().firstname
    lastname = student.first().lastname
    student.delete()
    db.commit()
    return{"message": f"{firstname} {lastname} deleted succussfully"}



def edit_student_id(id: int, db: Session, firstname: str = None, lastname: str = None, average: float = None, graduated: bool = None):
    if firstname:
        db.query(models.Student).filter(models.Student.id == id).update({models.Student.firstname: firstname})
    if lastname:
        db.query(models.Student).filter(models.Student.id == id).update({models.Student.lastname: lastname})
    if average:
        db.query(models.Student).filter(models.Student.id == id).update({models.Student.average: average})
    if graduated:
        db.query(models.Student).filter(models.Student.id == id).update({models.Student.graduated: graduated})
    db.commit()
    return {"message": f"Student ID:{id} is updated successfully"}


