from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI
from typing import List
import json

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    due_date: datetime
    priority: int
    completed: bool = False

DATA_FILE = "tasks.json"

@app.get("/")

def read_root():
    return 'Welcome to the Study Planner API!'

def read_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=2, default=str)    

@app.get("/tasks", response_model=List[Task])

def get_tasks():
    return read_tasks()

@app.post("/tasks")

def add_task(task: Task):
    tasks = read_tasks()
    tasks.append(task.dict())
    save_tasks(tasks)
    return {"message": "Task added successfully", "task": task}