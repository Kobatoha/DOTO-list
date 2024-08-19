from pydantic import BaseModel
from typing import Optional


class TodoItemCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TodoItemUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
