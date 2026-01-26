from fastapi import FastAPI
from repository import TasksRepository, Task
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

# repository
repository = TasksRepository()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": repository.get_all()}


@app.post("/tasks")
def add_task(new_task: Task):
    repository.save(new_task)
    return {"message": repository.get_all()}
    

@app.post("/tasks/{id}/")
def update_task_status(id: int):
    item = repository.get_by_id(id)
    item.status = not (item.status)
    return {"task": item}

from repository import FileRepository
@app.get("/mri/images")
def mri_images():

    return {"images": FileRepository().get_all()}

@app.get("/mri/images/{id}")
def mri_images(id:str):
    return {"basestr": FileRepository().get_str_by_id(id)}
    
from repository import FileRepositoryResults
@app.get("/mri/results")
def mri_images_results():
    return {"images": FileRepositoryResults().get_all()}

@app.get("/mri/results/{id}")
def mri_images_results(id:str):
    return {"basestr": FileRepositoryResults().get_str_by_id(id)}

from fastapi import FastAPI, UploadFile, File, Form
from typing import Annotated

@app.post("/mri/images")
def save_mri_image( fileMRI: Annotated[UploadFile, File(...)]):
    filename = FileRepository().add_raw(fileMRI)
    return {"filename":filename}


from pydantic import BaseModel
class Algorithm(BaseModel):
    filename: str
    name: str 
    
from src.service_layer.algorithm  import run_algorithm
@app.post("/algorithm/run")
def segment_brain(algorithm:Algorithm):
    msg = run_algorithm(algorithm.filename, algorithm.name)
    return { "message": msg }

from src.service_layer.algorithm import get_algorithms
from pydantic import BaseModel, ConfigDict
from typing import List

class AlgorithmPublicSchema(BaseModel):
    # This configuration is required to map from objects/dataclasses
    model_config = ConfigDict(from_attributes=True)
    id: int 
    name: str
    description: str
    
class AlgorithmsResponse(BaseModel):
    items: List[AlgorithmPublicSchema]

@app.get("/algorithms", response_model=AlgorithmsResponse)
def get_operations():
    return {"items":get_algorithms()}
