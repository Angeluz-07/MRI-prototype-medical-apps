from fastapi import APIRouter
from src.context import algorithm_service


router = APIRouter(prefix="/algorithms", tags=["Auth"])

from pydantic import BaseModel
class AlgorithmRun(BaseModel):
    algorithm_id: str
    filename: str
    user_id: str
    
@router.post("/run")
def segment_brain(algorithm_run: AlgorithmRun):
    msg = algorithm_service.run_algorithm(algorithm_run.algorithm_id, algorithm_run.filename, algorithm_run.user_id)
    return { "message": msg }