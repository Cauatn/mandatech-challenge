from pydantic import BaseModel, Field
from typing import Literal, Optional

class TaskSchema(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: Literal["done", "in_progress", "pending"]
    owner: str = Field(..., min_length=1)

class TaskUpdateSchema(BaseModel):
    status: Optional[Literal["done", "in_progress", "pending"]] = None
    title: Optional[str] = None
    description: Optional[str] = None
