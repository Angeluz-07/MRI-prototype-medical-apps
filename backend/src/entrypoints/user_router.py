from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from typing import List
from src.context import user_service

router = APIRouter(prefix="/users", tags=["Users"])


class UserDetailPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    username: str
    email: str

class UsersResponse(BaseModel):
    items: List[UserDetailPublicSchema]

@router.get("/users", response_model=UsersResponse)
def get_users():
    return {"items":user_service.get_users()}