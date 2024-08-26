from app.database import todo_collection
from app.models import TodoItem
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId


async def create_todo(todo: TodoItem) -> dict:
    result = await todo_collection.insert_one(todo.model_dump())
    new_todo = await todo_collection.find_one({"_id": result.inserted_id})
    return new_todo


async def get_todo_by_id(id: str) -> dict:
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    return todo


async def get_all_todos() -> list:
    todos = await todo_collection.find().to_list(100)
    return todos


async def update_todo_by_id(id: str, todo: dict) -> dict:
    await todo_collection.update_one({"_id": ObjectId(id)}, {"$set": todo})
    updated_todo = await todo_collection.find_one({"_id": ObjectId(id)})
    return updated_todo


async def delete_todo_by_id(id: str):
    await todo_collection.delete_one({"_id": ObjectId(id)})
