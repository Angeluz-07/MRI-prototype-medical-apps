from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from typing import List

from src.context import algorithm_service


router = APIRouter(prefix="/algorithms", tags=["Algorithms"])


class AlgorithmRun(BaseModel):
    algorithm_id: str
    filename: str
    user_id: str


@router.post("/run")
def segment_brain(algorithm_run: AlgorithmRun):
    msg = algorithm_service.run_algorithm(
        algorithm_run.algorithm_id, algorithm_run.filename, algorithm_run.user_id
    )
    return {"message": msg}


class AlgorithmPublicSchema(BaseModel):
    # This configuration is required to map from objects/dataclasses
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str
    description: str


class AlgorithmsResponse(BaseModel):
    items: List[AlgorithmPublicSchema]


@router.get("/", response_model=AlgorithmsResponse)
def get_operations():
    return {"items": algorithm_service.get_algorithms()}
