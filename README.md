# Task Management Capstone Project

A simple and robust Python-based Task Management API built with **FastAPI** and **MongoDB**. This project allows users to create, manage, and filter tasks efficiently.

## 🚀 Features

- **Dynamic Task Creation**: Store titles, assigned persons, status, priority, and completion flags.
- **Automated ID Management**: Incremental `task_id` for easy reference.
- **Completion Status Logic**: Automatically provides a human-readable completion message based on the task's state.
- **Task Filtering**: Filter tasks by their current status (e.g., "Pending", "In Progress", "Completed").
- **Error Handling**: Comprehensive 404 error messages for non-existent tasks.

## 🛠️ Tech Stack

- **FastAPI**: Web framework.
- **MongoDB**: NoSQL database.
- **Pydantic**: Data validation.

## 📦 API Documentation

### 1. Create a Task
**POST** `/tasks`
- **Request Body**:
```json
{
  "title": "Complete Capstone",
  "assigned_person": "Student",
  "status": "In Progress",
  "priority": "High",
  "completed": false
}
```
- **Response**:
```json
{
  "message": "Task created successfully",
  "task_id": 1
}
```

### 2. Fetch Task Details
**GET** `/tasks/{task_id}`
- **Response**:
```json
{
  "title": "Complete Capstone",
  "assigned_person": "Student",
  "status": "In Progress",
  "priority": "High",
  "completion_message": "Task pending"
}
```

### 3. Filter Tasks by Status
**GET** `/tasks?status=In Progress`
- **Response**:
```json
{
  "count": 1,
  "tasks": [
    {
      "task_id": 1,
      "title": "...",
      "assigned_person": "...",
      "status": "In Progress",
      "priority": "...",
      "completed": false
    }
  ]
}
```

## ⚙️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` with `MONGO_URL`.
3. Run the app: `uvicorn main:app --reload`
