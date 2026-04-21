from fastapi import APIRouter
from src.context import file_service
from fastapi import UploadFile, File
from typing import Annotated

router = APIRouter(prefix="/mri", tags=["MRI"])


@router.get("/images")
def mri_images():
    return {"images": file_service.get_input_files()}


@router.get("/images/{id}")
def mri_images(id: str):
    return {"basestr": file_service.get_input_file_as_base64(id)}


@router.get("/results")
def mri_images_results():
    return {"images": file_service.get_output_files()}


@router.get("/results/{id}")
def mri_images_results(id: str):
    return {"basestr": file_service.get_output_file_as_base64(id)}


@router.post("/images")
def save_mri_image(fileMRI: Annotated[UploadFile, File(...)]):
    filename = file_service.save_input_file(fileMRI.filename, fileMRI.file)
    return {"filename": filename}
