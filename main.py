from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    due_date: datetime
    priority: int
    completed: bool = False

    @app.get("/")
    def read_root():
        return "Welcome to the Study Planner!"