from fastapi import FastAPI, HTTPException
from models import Task
from database import task_collection

app = FastAPI()


@app.post("/tasks")
def create_task(task: Task):

    task_data = task.dict()

    next_id = task_collection.count_documents({}) + 1

    if next_id > 9:
        next_id = (next_id - 1) % 9 + 1

    task_data["task_id"] = next_id

    task_collection.insert_one(task_data)

    return {
        "message": "Task created successfully",
        "task_id": next_id,
        "task_status": task.status
    }


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    task = task_collection.find_one({"task_id": task_id})

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task["_id"] = str(task["_id"])

    return {
        "message": "Task fetched successfully",
        "task": task
    }