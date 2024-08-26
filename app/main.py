from bson import ObjectId
from fastapi import FastAPI, HTTPException
from app.models import TodoItem
from app.schemas import TodoItemCreate, TodoItemUpdate
from app.crud import *


app = FastAPI()


def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"],
    }


@app.post("/todos/")
async def create_todo_item(todo: TodoItemCreate):
    new_todo = await create_todo(TodoItem(**todo.dict()))
    return todo_serializer(new_todo)


@app.get("/todos/{id}")
async def read_todo_item(id: str):
    todo = await get_todo_by_id(id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo_serializer(todo)


@app.get("/todos/")
async def read_all_todos():
    todos = await get_all_todos()
    return [todo_serializer(todo) for todo in todos]


@app.put("/todos/{id}")
async def update_todo_item(id: str, todo: TodoItemUpdate):
    updated_todo = await update_todo_by_id(id, todo.dict(exclude_unset=True))
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo_serializer(updated_todo)


@app.delete("/todos/{id}")
async def delete_todo_item(id: str):
    todo = await get_todo_by_id(id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    await delete_todo_by_id(id)
    return {"message": "Todo item deleted"}
