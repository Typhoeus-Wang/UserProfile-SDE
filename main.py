from fastapi import FastAPI, HTTPException
from typing import List, Optional
from uuid import UUID, uuid4
from models import User, Gender, Role, BaseModel
from enum import Enum


app = FastAPI()

db: List[User] = [
    User(id=UUID("f8b998d8-35d7-4913-b4df-d1278dc1b29b"), 
         first_name="Jamila", 
         last_name="Ahmed",
         gender=Gender.female,
         roles=[Role.student]
    ),
    User(
        id=UUID("ab1e8909-61d4-45c0-bb57-27360bc200a1"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail = f"user with id: {user_id} does not exists"
    )