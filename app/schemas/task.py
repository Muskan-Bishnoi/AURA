from pydantic import BaseModel
from datetime import time

class Task(BaseModel):
    title: str
    description: str
    time: time
    is_important: bool
    task_type: str  # "wellness" or "regular"
