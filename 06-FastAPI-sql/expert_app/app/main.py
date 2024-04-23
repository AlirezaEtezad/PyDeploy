
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    uni_db = SessionLocal()
    yield uni_db
    uni_db.close()


@app.get("/")
def read_root():
    return {"Student management": "This is an API DB for students and their courses"}

@app.get("/students", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session=Depends(get_db)):
    db_student = crud.get_student_by_lastname(db, lastname=student.lastname)
    if db_student:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_student(db=db, student=student)


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.post("/students/{student_id}/courses/", response_model=schemas.Course)
def create_course_for_student(student_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_student_course(db=db, course=course, student_id=student_id)


@app.get("/courses", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    response = crud.remove_student_id(id=student_id, db=db)
    return response


@app.put("/students/{student_id}")
def update_student(student_id: int, firstname: str = None, lastname: str = None, average: float = None, graduated: bool = None, db: Session = Depends(get_db)):
    if not firstname and not lastname and not average and not graduated:
        raise HTTPException(status_code=400, detail="No information is provided to update")
    response = crud.edit_student_id(id=student_id, db=db, firstname=firstname, lastname=lastname, average=average, graduated=graduated)
    return response