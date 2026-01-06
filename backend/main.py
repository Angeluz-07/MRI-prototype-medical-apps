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
    
from fastapi import FastAPI, UploadFile, File, Form
from typing import Annotated

@app.post("/mri/images")
def save_mri_image( fileMRI: Annotated[UploadFile, File(...)]):
    filename = FileRepository().add_raw(fileMRI)
    return {"filename":filename}


from pydantic import BaseModel


class FileOperation(BaseModel):
    fileName: str
    operation: str 
    

@app.post("/mri/segment-brain")
def segment_brain(file_operation:FileOperation):
    FileRepository().service_segment_brain(file_operation.fileName)
    # Use the other data
    print(f"Received other property: {file_operation.operation}")

    return { "message": "success"}
