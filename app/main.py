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
