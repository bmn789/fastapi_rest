from .database import DbSession
from . import models

async def get_users(db:DbSession):
    data = db.query(models.User).all()
    count = db.query(models.User).count()

    return { "count": count, "data": data }