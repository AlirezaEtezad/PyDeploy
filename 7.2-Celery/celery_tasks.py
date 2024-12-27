import os
from time import sleep
from datetime import datetime
import numpy as np
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379", backend="redis://localhost:6379")


@app.task
def hello_world():
    return "Hello World"

@app.task
def dummy_task():
    os.makedirs("./tmp/celery", exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%s")
    with open(f"./tmp/celery/task-{now}.txt", "w") as f:
        f.write("Hi Everybody.")

@app.task
def dummy_task_2(name="Ali"):
    sleep(10)
    return f"Hello {name}."


@app.task
def dummy_task_3() -> str:
    return open('/tmp/celery/x.txt', 'w')


app.task
def add(x, y):
    print("add function")
    return x + y