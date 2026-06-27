from fastapi import APIRouter, HTTPException
from starlette import status

from app.database import DbSession
from app.lib.none_check import none_check
from app.models import User
from  app.schemas import UserBase, UserResponse


router = APIRouter()

@router.get("/user/all")
async def get_users(db: DbSession):
    count = db.query(User).count()
    data = db.query(User).all()
    return {"count": count, "data": data }


@router.get("/user/{user_id}")
async def get_user(user_id: int, db:DbSession):
    data = db.query(User).filter(User.id==user_id).first()
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return data

@router.post("/user", response_model=UserResponse)
def add_user(user:UserBase, db:DbSession):
    data = User(**user.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

@router.put("/user/{user_id}", response_model=UserResponse)
def update_user(user_id:int, user:UserBase, db:DbSession):
    values = user.model_dump(exclude_unset=True)
    data = db.query(User).filter(User.id == user_id).first()
   
    data = none_check(data)
    print(data.id)


    for key, value in values.items():
        setattr(data, key, value)

    db.commit()
    db.refresh(data)
    
    return none_check(data)

@router.delete("/user/{user_id}")
def user_delete(user_id:int, db:DbSession):
    data = db.query(User).filter(User.id == user_id).first()
    data = none_check(data)
    db.delete(data)
    db.commit()

    return data