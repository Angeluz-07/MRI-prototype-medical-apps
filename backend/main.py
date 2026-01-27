from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Handle CORS in local dev
origins= [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_methods=["*"],
)

from src.services.file import get_input_files, get_input_file_as_base64
from src.services.file import get_output_files, get_output_file_as_base64
from src.services.file import save_input_file

@app.get("/mri/images")
def mri_images():
    return {"images": get_input_files()}

@app.get("/mri/images/{id}")
def mri_images(id:str):
    return {"basestr": get_input_file_as_base64(id)}
    
@app.get("/mri/results")
def mri_images_results():
    return {"images": get_output_files()}

@app.get("/mri/results/{id}")
def mri_images_results(id:str):
    return {"basestr": get_output_file_as_base64(id)}

from fastapi import UploadFile, File
from typing import Annotated

@app.post("/mri/images")
def save_mri_image( fileMRI: Annotated[UploadFile, File(...)]):
    filename = save_input_file(fileMRI.filename, fileMRI.file)
    return {"filename":filename}

from pydantic import BaseModel
class AlgorithmRun(BaseModel):
    algorithm_id: str
    filename: str
    
from src.services.algorithm  import run_algorithm
from src.repository.execution import InMemoryExecutionRepository
execution_repository = InMemoryExecutionRepository()
@app.post("/algorithm/run")
def segment_brain(algorithm_run: AlgorithmRun):
    msg = run_algorithm(algorithm_run.algorithm_id, algorithm_run.filename, execution_repository)
    return { "message": msg }

from src.services.algorithm import get_algorithms
from pydantic import BaseModel, ConfigDict
from typing import List

class AlgorithmPublicSchema(BaseModel):
    # This configuration is required to map from objects/dataclasses
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str
    description: str
    
class AlgorithmsResponse(BaseModel):
    items: List[AlgorithmPublicSchema]

@app.get("/algorithms", response_model=AlgorithmsResponse)
def get_operations():
    return {"items":get_algorithms()}

from src.services.execution import get_executions
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class ExecutionDetailPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    timestamp: datetime
    message: str
    level: str 
    id: str 

class ExecutionPublicSchema(BaseModel):
    # This configuration is required to map from objects/dataclasses
    model_config = ConfigDict(from_attributes=True)
    id: str 
    algorithm_id: str
    details: List[ExecutionDetailPublicSchema]
    
class ExecutionsResponse(BaseModel):
    items: List[ExecutionPublicSchema]

@app.get("/executions", response_model=ExecutionsResponse)
def get_operations():
    return {"items":get_executions(execution_repository)}
