from pydantic import BaseModel, Field
from typing import Optional, TypedDict

class User(BaseModel):
    id:int
    name: str

class Todo(TypedDict):
    id: int
    title: str


d:Todo = {  'id': 1, 'title': "Barath"}
t = Todo(**d)

for item in t:
    print(item, t[item])

