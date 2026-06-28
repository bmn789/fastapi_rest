from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    despcription: Optional[str] = None

class TodoResponse(TodoBase):
    id : int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name:str
    email: str
    is_active:Optional[bool] = True


class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True