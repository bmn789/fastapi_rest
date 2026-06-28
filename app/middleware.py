from fastapi import HTTPException, Request
from starlette import status


def get_user_id(request:Request):
     user_id = request.state.user_id
     if user_id is None:
          raise HTTPException(status.HTTP_400_BAD_REQUEST, "User id not found")
    
     return user_id