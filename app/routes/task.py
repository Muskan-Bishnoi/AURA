from fastapi import APIRouter
from typing import List
from datetime import time
from pydantic import BaseModel

router = APIRouter()

# Data model
class Task(BaseModel):
    user_id: str
    title: str
    description: str
    time: time
    is_important: bool
    task_type: str  # "wellness" or "regular"

# Simulate a DB (you can replace with real DB later)
tasks_db = []

# @router.post("/add-tasks/")
# async def add_tasks(task_list: List[Task]):
#     tasks_db.extend(task_list)
#     return {"message": "Tasks added successfully", "count": len(task_list)}

@router.post("/add-tasks/")
async def add_tasks(task_list: List[Task]):
    for task in task_list:
        tasks_db.append(task.dict())  # <- this makes them plain dicts
    return {"message": "Tasks added successfully", "count": len(task_list)}


@router.get("/get-user-schedule/")
async def get_user_schedule(user_id: str):
    # Get all tasks for this user
    # user_tasks = [task for task in tasks_db if task.user_id == user_id]
    user_tasks = [task for task in tasks_db if task["user_id"] == user_id]
    # sorted_tasks = sorted(user_tasks, key=lambda x: x.time)
    sorted_tasks = sorted(user_tasks, key=lambda task: task["time"])


    return {"user_id": user_id, "schedule": sorted_tasks}
