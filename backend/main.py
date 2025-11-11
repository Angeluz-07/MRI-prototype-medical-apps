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

from fastapi import FastAPI, UploadFile, File, Form
from typing import Annotated
import shutil
@app.post("/mri/segment-brain")
def segment_brain(
    fileMRI: Annotated[UploadFile, File(...)],
    operation: Annotated[str, Form(...)]
):
    # Process the file
    with open(f"{fileMRI.filename}", "wb") as buffer:
        shutil.copyfileobj(fileMRI.file, buffer)
    import img_process
    img_process.run(fileMRI.filename)

    # Use the other data
    print(f"Received other property: {operation}")

    return {
        "filename": fileMRI.filename,
        "other_property_value": operation
    }