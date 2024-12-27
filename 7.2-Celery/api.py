from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
import celery_tasks

app = FastAPI()

class TaskOut(BaseModel):
    id: str
    status: str



# @app.get("/start")
# def start() -> TaskOut:
#     t = celery_tasks.dummy_task_2.delay()
#     return TaskOut(id=t.task_id, status=t.status)

# @app.get("/status")
# def status(task_id) -> TaskOut:
#     t = celery_tasks.app.AsyncResult(task_id)
#     return TaskOut(id=t.task_id, status=t.status)


def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status)


@app.get("/start")
def start() -> TaskOut:
    r = celery_tasks.dummy_task_2.delay()
    return _to_task_out(r)


@app.get("/status")
def status(task_id: str) -> TaskOut:
    r = celery_tasks.app.AsyncResult(task_id)
    return _to_task_out(r)

