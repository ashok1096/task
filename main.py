from fastapi import FastAPI, HTTPException, Query
from models import Task
from database import task_collection

app = FastAPI(title="Task Management API")
@app.get("/")
def home():
    return {
        "message": "API Running Successfully!"
        }



# POST API - CREATE TASK
@app.post("/tasks")
def create_task(task: Task):

    # Find last inserted task
    last_task = task_collection.find_one(
        sort=[("task_id", -1)]
    )

    # Generate next task ID
    next_id = 1 if not last_task else last_task["task_id"] + 1

    # Convert request body into dictionary
    task_data = task.dict()

    # Add task ID
    task_data["task_id"] = next_id

    # Insert into MongoDB
    task_collection.insert_one(task_data)

    # Return response
    return {
        "message": "Task created successfully",
        "task": {
            "task_id": task_data["task_id"],
            "title": task_data["title"],
            "assigned_person": task_data["assigned_person"],
            "status": task_data["status"],
            "priority": task_data["priority"],
            "completed": task_data["completed"]
        }
    }


# GET API - FETCH TASK BY ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    # Find task using task_id
    task = task_collection.find_one(
        {"task_id": task_id}
    )

    # If task not found
    if not task:

        raise HTTPException(
            status_code=404,
            detail=f"Task with ID {task_id} not found"
        )

    # Completion message
    completion_message = (
        "Task completed"
        if task["completed"]
        else "Task pending"
    )

    # Return task details
    return {
        "task_id": task["task_id"],
        "title": task["title"],
        "assigned_person": task["assigned_person"],
        "status": task["status"],
        "priority": task["priority"],
        "completion_message": completion_message
    }


# FILTER TASKS BY STATUS
@app.get("/filter/tasks")
def filter_tasks(
    status: str = Query(...)
):

    # Allowed status values
    allowed_status = [
        "active",
        "inactive",
        "pending",
        "completed"
    ]

    # Convert status to lowercase
    status = status.lower()

    # Validate status
    if status not in allowed_status:

        raise HTTPException(
            status_code=400,
            detail="Invalid status value"
        )

    # Find tasks
    tasks = list(
        task_collection.find(
            {"status": status}
        )
    )

    # If no tasks found
    if not tasks:

        return {
            "message": f"No tasks found for status '{status}'",
            "tasks": []
        }

    results = []

    # Convert MongoDB documents
    for task in tasks:

        results.append({
            "task_id": task["task_id"],
            "title": task["title"],
            "assigned_person": task["assigned_person"],
            "status": task["status"],
            "priority": task["priority"],
            "completed": task["completed"]
        })

    # Return response
    return {
        "count": len(results),
        "tasks": results
    }