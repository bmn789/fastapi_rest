from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from . import crud
from . import schemas, models
from .database import DbSession, engine
from starlette import status
from .routes.user import router as user_routes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(Exception)
async def http_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": str(exc)
        })


app.include_router(user_routes, prefix="/api")


@app.get("/")
async def users(db:DbSession):
    return await crud.get_users(db)


@app.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_user(db:DbSession, user:schemas.UserBase):
    # user = db.query(models.User).first()
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    u1 = db.refresh(new_user)
    print(u1)
    
    return new_user


@app.delete("/")
def delete_user():
   raise HTTPException(status_code=400, detail="User not found")

