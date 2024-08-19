from pydantic import BaseModel, Field
from typing import Optional


class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)
