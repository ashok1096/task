from pydantic import BaseModel

class Task(BaseModel):
    task_description: str
    assigned_person: str
    status: str

