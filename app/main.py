from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from . import schemas, models
from .database import DbSession, engine
from starlette import status
from .routes.user import router as user_routes
from .routes.todo import router as todo_routes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def middleware(req:Request, call_next):
    user_id = req.headers.get("x-user-id")
    print("user_id", user_id)
    if user_id is not None:
        req.state.user_id = int(user_id)
    else :
        req.state.user_id = None
    return await call_next(req)

@app.exception_handler(Exception)
async def http_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": str(exc)
        })




router = APIRouter(prefix="/api")

router.include_router(user_routes)



router.include_router(todo_routes)

app.include_router(router)

