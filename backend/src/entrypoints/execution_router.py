from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime
from src.context import execution_service

router = APIRouter(prefix="/execution-details", tags=["Executions"])


class ExecutionDetailPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    algorithm_name: str
    user_name: str
    timestamp: datetime
    message: str
    level: str
    id: str


class ExecutionsResponse(BaseModel):
    items: List[ExecutionDetailPublicSchema]


@router.get("/", response_model=ExecutionsResponse)
def get_operations():
    return {"items": execution_service.get_execution_details()}
