````markdown
# Task Management API

This is a simple Task Management API created using FastAPI and MongoDB.  
The project is used to create and manage tasks using API endpoints tested in Postman.

## Features

- Create new tasks
- Get task details
- MongoDB Atlas connection
- Automatic task ID generation
- FastAPI backend
- Simple API testing with Postman

## Technologies Used

- Python
- FastAPI
- MongoDB Atlas
- PyMongo
- Uvicorn
- Pydantic

## Project Setup

### Install Requirements

```bash
pip install -r requirements.txt
````

or using uv

```bash
uv sync
```

## Create .env File

```env
MONGO_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority
```

## Run the Server

```bash
uvicorn main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create Task

```http
POST /tasks
```

Request Body:

```json
{
  "task_description": "Complete project",
  "assigned_person": "Ashok",
  "status": "Pending"
}
```

Response:

```json
{
  "message": "Task created successfully",
  "task_id": 1
}
```

---

### Get Task

```http
GET /tasks/{task_id}
```

## Project Structure

```text
├── main.py
├── database.py
├── models.py
├── .env
└── requirements.txt
```

