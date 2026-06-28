

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from app import schemas
from app import models
from app.database import DbSession
from app.middleware import get_user_id



router = APIRouter()

@router.get("/todo/all")
async def get_todos(request: Request, db:DbSession):
    user_id = get_user_id(request)
    data = (
    db.query(models.Todo)
    .options(joinedload(models.Todo.owner))
    .all()
    )
    count = db.query(models.Todo).count()
    
    return {"count": count, "data" : data }

@router.post("/todo")
async def add_todo(data:schemas.TodoBase, request: Request, db:DbSession):
    user_id = get_user_id(request)
    new_todo = models.Todo(owner_id=user_id,**data.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.get("/todo/{user_id}")
async def get_user_todos(user_id: int, db:DbSession):
    data = (
    db.query(models.Todo)
    .options(joinedload(models.Todo.owner))
    .filter(models.Todo.owner_id == user_id)
    .all()
    )
    count = db.query(models.Todo).filter(models.Todo.owner_id == user_id).count()
    
    return {"count": count, "data" : data }

