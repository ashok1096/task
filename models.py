from pydantic import BaseModel

class Task(BaseModel):
    title: str
    assigned_person: str
    status: str
    priority: str
    completed: bool

