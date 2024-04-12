from fastapi import FastAPI, File, Form, HTTPException
# from database import Database
from app.database import Database

app = FastAPI()
database = Database()


@app.get("/")
def read_root():
    note = "This API is connected to a database to make a ToDoList. Use '/tasks' to see all tasks."
    return note


@app.get("/tasks")
async def read_tasks():
    tasks = database.get_tasks()
    return tasks


@app.post("/tasks")
async def add_task(title: str = Form(None), description: str = Form(None), time:str = Form(None), priority: str = Form(None)):
    if not title or not description or not priority or not time:
        raise HTTPException(status_code=400, detail="All fields are required")
    if priority not in ["High", "Medium", "Low"]:
        raise HTTPException(status_code=400, detail="Priority can only be 'High', 'Medium' or 'Low'.")
    else:
        result = database.add_new_task(title, description, time, priority)
        if not result:
            raise HTTPException(status_code=500, detail="Failed to add task to database")
        return {"message": "Task added successfully"}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if not database.remove_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, title: str = Form(None), description: str = Form(None), time : str = Form(None), priority: str = Form(None)):
    if priority not in ["High", "Medium", "Low"]:
        raise HTTPException(status_code=400, detail="Priority can only be 'High', 'Medium' or 'Low'.")
    else:
        if not database.update_task(task_id, title, description, time, priority):
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task updated successfully"}
