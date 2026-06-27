from typing import Optional, TypeVar

from fastapi import HTTPException
from starlette import status

T = TypeVar("T")

def none_check(value: Optional[T])-> T:
    if value is None:
       raise HTTPException(status.HTTP_404_NOT_FOUND, detail="record not found with associated id")

    return value